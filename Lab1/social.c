#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include "social.h"

individual *create_individual(int id, char name[20], char content[200], int birthday[3])
{
    individual *new_individual = (individual *)malloc(sizeof(individual));

    new_individual->id = id;
    strcpy(new_individual->name, name);
    strcpy(new_individual->content, content);

    time_t t = time(NULL);
    struct tm tm = *localtime(&t);

    new_individual->creation_date[0] = tm.tm_mday;
    new_individual->creation_date[1] = tm.tm_mon + 1;
    new_individual->creation_date[2] = tm.tm_year + 1900;

    new_individual->birthday[0] = birthday[0];
    new_individual->birthday[1] = birthday[1];
    new_individual->birthday[2] = birthday[2];

    new_individual->cnt_businesses_as_owner = 0;
    new_individual->cnt_businesses_as_customer = 0;
    new_individual->cnt_organisations = 0;
    new_individual->cnt_groups = 0;

    return new_individual;
}

business *create_business(int id, char name[20], char content[200], int location[2])
{
    business *new_business = (business *)malloc(sizeof(business));

    new_business->id = id;
    strcpy(new_business->name, name);
    strcpy(new_business->content, content);

    time_t t = time(NULL);
    struct tm tm = *localtime(&t);

    new_business->creation_date[0] = tm.tm_mday;
    new_business->creation_date[1] = tm.tm_mon + 1;
    new_business->creation_date[2] = tm.tm_year + 1900;

    new_business->location[0] = location[0];
    new_business->location[1] = location[1];

    new_business->cnt_owners = 0;
    new_business->cnt_customers = 0;
    new_business->cnt_groups = 0;

    return new_business;
}

organisation *create_organisation(int id, char name[20], char content[200], int location[2])
{
    organisation *new_organisation = (organisation *)malloc(sizeof(organisation));

    new_organisation->id = id;
    strcpy(new_organisation->name, name);
    strcpy(new_organisation->content, content);

    time_t t = time(NULL);
    struct tm tm = *localtime(&t);

    new_organisation->creation_date[0] = tm.tm_mday;
    new_organisation->creation_date[1] = tm.tm_mon + 1;
    new_organisation->creation_date[2] = tm.tm_year + 1900;

    new_organisation->location[0] = location[0];
    new_organisation->location[1] = location[1];

    new_organisation->cnt_members = 0;

    return new_organisation;
}

group *create_group(int id, char name[20], char content[200])
{
    group *new_group = (group *)malloc(sizeof(group));

    new_group->id = id;
    strcpy(new_group->name, name);
    strcpy(new_group->content, content);

    time_t t = time(NULL);
    struct tm tm = *localtime(&t);

    new_group->creation_date[0] = tm.tm_mday;
    new_group->creation_date[1] = tm.tm_mon + 1;
    new_group->creation_date[2] = tm.tm_year + 1900;

    new_group->cnt_members = 0;
    new_group->cnt_businesses = 0;

    return new_group;
}

// initialize the ids_info linked list
ids_info *ids_head = NULL;

// get smallest unused id by iterating
int get_smallest_unused_id()
{
    // if ids_head is NULL, return 1
    if (ids_head == NULL)
    {
        return 1;
    }

    int smallest_unused_id = 1;
    ids_info *current = ids_head;

    while (current != NULL)
    {
        if (current->id == smallest_unused_id)
        {
            smallest_unused_id++;
            current = ids_head;
        }
        else
        {
            current = current->next;
        }
    }

    return smallest_unused_id;
}

// add id to ids_info linked list in ascending order
void add_id(int id, int type, individual *individual, business *business, organisation *organisation, group *group)
{
    ids_info *new_id = (ids_info *)malloc(sizeof(ids_info));

    new_id->id = id;
    new_id->type = type;

    new_id->individual = individual;
    new_id->business = business;
    new_id->organisation = organisation;
    new_id->group = group;

    new_id->next = NULL;

    // if ids_head is NULL, make new_id the head
    if (ids_head == NULL)
    {
        ids_head = new_id;

        return;
    }

    // if new_id->id is smaller than ids_head->id, make new_id the head
    if (new_id->id < ids_head->id)
    {
        new_id->next = ids_head;
        ids_head = new_id;
        return;
    }

    // else iterate through ids_info linked list and add new_id in ascending order
    ids_info *current = ids_head;

    while (current->next != NULL)
    {
        if (new_id->id < current->next->id)
        {
            new_id->next = current->next;
            current->next = new_id;
            return;
        }
        else
        {
            current = current->next;
        }
    }

    current->next = new_id;
    return;
}

// create node

int is_birthday_possible(int birthday[3])
{
    // check if birthday is possible
    if (birthday[2] >= 1900 && birthday[2] <= 2023)
    {
        if ((birthday[1] == 2) && ((birthday[0] >= 1 && birthday[0] <= 28 && birthday[2] % 4 != 0) || (birthday[0] >= 1 && birthday[0] <= 29 && birthday[2] % 4 == 0)))
        {
            return 1;
        }
        else if ((birthday[1] >= 1 && birthday[1] <= 12) && (birthday[1] % 2 == 0 && birthday[0] >= 1 && birthday[0] <= 30) || (birthday[0] % 2 != 0 && birthday[0] >= 1 && birthday[0] <= 31))
        {
            return 1;
        }
        else
        {
            return 0;
        }
    }
    else
    {
        return 0;
    }
}

void create_node(int type)
{
    if (type <= 0 || type > 4)
    {
        printf("Invalid type\n");
        return;
    }

    else
    {
        // ids are unique and filled by the smallest natural number not used yet
        int id = get_smallest_unused_id();

        if (type == 1) // create individual
        {
            printf("Creating individual with id %d\n", id);
            printf("Enter name: ");
            char name[20];
            scanf("%s", name);

            printf("Enter content: ");
            char content[200];
            scanf("%s", content);
            while(is_content_duplicate(content))
            {
                printf("Content already exists. Enter again: ");
                scanf("%s", content);
            }

            int birthday[3];
            // input pracical birthday date, month and year
            printf("Enter birthday date:\nDate:");
            scanf("%d", &birthday[0]);
            printf("Month:");
            scanf("%d", &birthday[1]);
            printf("Year:");
            scanf("%d", &birthday[2]);

            while (!is_birthday_possible(birthday))
            {
                printf("Invalid birthday. Enter again:\nDate:");
                scanf("%d", &birthday[0]);
                printf("Month:");
                scanf("%d", &birthday[1]);
                printf("Year:");
                scanf("%d", &birthday[2]);
            }

            individual *new_individual = create_individual(id, name, content, birthday);

            add_id(id, type, new_individual, NULL, NULL, NULL);
        }
        else if (type == 2) // create business
        {
            printf("Creating business with id %d\n", id);
            printf("Enter name: ");
            char name[20];
            scanf("%s", name);

            printf("Enter content: ");
            char content[200];
            scanf("%s", content);
            while(is_content_duplicate(content))
            {
                printf("Content already exists. Enter again: ");
                scanf("%s", content);
            }

            int location[2];
            printf("Enter location:\nX:");
            scanf("%d", &location[0]);
            printf("Y:");
            scanf("%d", &location[1]);

            business *new_business = create_business(id, name, content, location);

            add_id(id, type, NULL, new_business, NULL, NULL);
        }
        else if (type == 3) // create organisation
        {
            printf("Creating organisation with id %d\n", id);
            printf("Enter name: ");
            char name[20];
            scanf("%s", name);

            printf("Enter content: ");
            char content[200];
            scanf("%s", content);
            while(is_content_duplicate(content))
            {
                printf("Content already exists. Enter again: ");
                scanf("%s", content);
            }

            int location[2];
            printf("Enter location:\nX:");
            scanf("%d", &location[0]);
            printf("Y:");
            scanf("%d", &location[1]);

            organisation *new_organisation = create_organisation(id, name, content, location);

            add_id(id, type, NULL, NULL, new_organisation, NULL);
        }
        else if (type == 4) // create group
        {
            printf("Creating group with id %d\n", id);
            printf("Enter name: ");
            char name[20];
            scanf("%s", name);

            printf("Enter content: ");
            char content[200];
            scanf("%s", content);
            while(is_content_duplicate(content))
            {
                printf("Content already exists. Enter again: ");
                scanf("%s", content);
            }

            group *new_group = create_group(id, name, content);

            add_id(id, type, NULL, NULL, NULL, new_group);
        }

        printf("\nNode created.\n");
    }
}
void create()
{
    printf("------------------------------------------------------------------------------------\n");
    printf("\nNode type:\n");
    printf("1.Individual\n2.Business\n3.Organisation\n4.Group\nEnter type of node: ");
    int type;
    scanf("%d", &type);
    printf("\n------------------------------------------------------------------------------------\n");

    create_node(type);
}

// delete node
void delete_linked_node(int id)
{
    // also delete the the elements in the arrays where this id is stored
    ids_info *node = does_node_exists(id);
    int type = node->type;

    if (node)
    {
        if (type == 1)
        {
            // delete individual from all linked nodes
            for (int i = 0; i < node->individual->cnt_groups; i++)
            {
                group *group = does_group_exists(node->individual->linked_groups[i]);
                for (int j = 0; j < group->cnt_members; j++)
                {
                    if (group->linked_members[j] == id)
                    {
                        // swap the last element here and reduce the size of the array
                        int t = group->linked_members[j];
                        group->linked_members[j] = group->linked_members[group->cnt_members - 1];
                        group->linked_members[group->cnt_members - 1] = t;
                        group->cnt_members--;
                        break;
                    }
                }
            }
            for (int i = 0; i < node->individual->cnt_businesses_as_owner; i++)
            {
                business *business = does_business_exists(node->individual->linked_businesses_as_owner[i]);
                for (int j = 0; j < business->cnt_owners; j++)
                {
                    if (business->linked_owners[j] == id)
                    {
                        // swap the last element here and reduce the size of the array
                        int t = business->linked_owners[j];
                        business->linked_owners[j] = business->linked_owners[business->cnt_owners - 1];
                        business->linked_owners[business->cnt_owners - 1] = t;
                        business->cnt_owners--;
                        break;
                    }
                }
            }
            for (int i = 0; i < node->individual->cnt_businesses_as_customer; i++)
            {
                business *business = does_business_exists(node->individual->linked_businesses_as_customer[i]);
                for (int j = 0; j < business->cnt_customers; j++)
                {
                    if (business->linked_customers[j] == id)
                    {
                        // swap the last element here and reduce the size of the array
                        int t = business->linked_customers[j];
                        business->linked_customers[j] = business->linked_customers[business->cnt_customers - 1];
                        business->linked_customers[business->cnt_customers - 1] = t;
                        business->cnt_customers--;
                        break;
                    }
                }
            }
            for (int i = 0; i < node->individual->cnt_organisations; i++)
            {
                organisation *organisation = does_organisation_exists(node->individual->linked_organisations[i]);
                for (int j = 0; j < organisation->cnt_members; j++)
                {
                    if (organisation->linked_members[j] == id)
                    {
                        // swap the last element here and reduce the size of the array
                        int t = organisation->linked_members[j];
                        organisation->linked_members[j] = organisation->linked_members[organisation->cnt_members - 1];
                        organisation->linked_members[organisation->cnt_members - 1] = t;
                        organisation->cnt_members--;
                        break;
                    }
                }
            }
        }

        else if (type == 2)
        {
            // delete business from all linked nodes
            for (int i = 0; i < node->business->cnt_groups; i++)
            {
                group *group = does_group_exists(node->business->linked_groups[i]);
                for (int j = 0; j < group->cnt_businesses; j++)
                {
                    if (group->linked_businesses[j] == id)
                    {
                        // swap the last element here and reduce the size of the array
                        int t = group->linked_businesses[j];
                        group->linked_businesses[j] = group->linked_businesses[group->cnt_businesses - 1];
                        group->linked_businesses[group->cnt_businesses - 1] = t;
                        group->cnt_businesses--;
                        break;
                    }
                }
            }
        }
        else if (type == 3)
        {
            // delete organisation from all linked nodes
            for (int i = 0; i < node->organisation->cnt_members; i++)
            {
                individual *individual = does_individual_exists(node->organisation->linked_members[i]);
                for (int j = 0; j < individual->cnt_organisations; j++)
                {
                    if (individual->linked_organisations[j] == id)
                    {
                        // swap the last element here and reduce the size of the array
                        int t = individual->linked_organisations[j];
                        individual->linked_organisations[j] = individual->linked_organisations[individual->cnt_organisations - 1];
                        individual->linked_organisations[individual->cnt_organisations - 1] = t;
                        individual->cnt_organisations--;
                        break;
                    }
                }
            }
        }
        else if (type == 4)
        {
            // delete group from all linked nodes
            for (int i = 0; i < node->group->cnt_members; i++)
            {
                individual *individual = does_individual_exists(node->group->linked_members[i]);
                for (int j = 0; j < individual->cnt_groups; j++)
                {
                    if (individual->linked_groups[j] == id)
                    {
                        // swap the last element here and reduce the size of the array
                        int t = individual->linked_groups[j];
                        individual->linked_groups[j] = individual->linked_groups[individual->cnt_groups - 1];
                        individual->linked_groups[individual->cnt_groups - 1] = t;
                        individual->cnt_groups--;
                        break;
                    }
                }
            }
            for (int i = 0; i < node->group->cnt_businesses; i++)
            {
                business *business = does_business_exists(node->group->linked_businesses[i]);
                for (int j = 0; j < business->cnt_groups; j++)
                {
                    if (business->linked_groups[j] == id)
                    {
                        // swap the last element here and reduce the size of the array
                        int t = business->linked_groups[j];
                        business->linked_groups[j] = business->linked_groups[business->cnt_groups - 1];
                        business->linked_groups[business->cnt_groups - 1] = t;
                        business->cnt_groups--;
                        break;
                    }
                }
            }
        }
    }
}

void delete_node()
{
    printf("\n------------------------------------------------------------------------------------\n");
    printf("Enter id of node to delete: ");
    int id;
    scanf("%d", &id);

    ids_info *current = ids_head;
    ids_info *previous = NULL;
    int found = 0;

    while (current != NULL)
    {
        if (current->id == id)
        {
            found = 1;
            delete_linked_node(id);

            if (previous == NULL)
            {
                ids_head = current->next;
            }
            else
            {
                previous->next = current->next;
            }

            free(current);
            printf("\n Node with id %d deleted. \n", id);
            break;
        }
        previous = current;
        current = current->next;
    }

    if (!found)
    {
        printf("# Node with id %d does not exist #\n", id);
    }
}

// search node
int search_node_by_id(int id)
{
    ids_info *current = ids_head;
    int found = 0;

    while (current != NULL)
    {
        if (current->id == id)
        {
            found = 1;
            printf("\nNode found with following details:\n");
            if (current->type == 1)
            {
                printf("Individual\n");
                printf("Id: %d\n", current->id);
                printf("Name: %s\n", current->individual->name);
                printf("Content: %s\n", current->individual->content);
                printf("Creation date: %d/%d/%d\n", current->individual->creation_date[0], current->individual->creation_date[1], current->individual->creation_date[2]);
                printf("Birthday: %d/%d/%d\n", current->individual->birthday[0], current->individual->birthday[1], current->individual->birthday[2]);
            }
            else if (current->type == 2)
            {
                printf("Business\n");
                printf("Id: %d\n", current->id);
                printf("Name: %s\n", current->business->name);
                printf("Content: %s\n", current->business->content);
                printf("Creation date: %d/%d/%d\n", current->business->creation_date[0], current->business->creation_date[1], current->business->creation_date[2]);
                printf("Location: (%d, %d)\n", current->business->location[0], current->business->location[1]);
            }
            else if (current->type == 3)
            {
                printf("Organisation\n");
                printf("Id: %d\n", current->id);
                printf("Name: %s\n", current->organisation->name);
                printf("Content: %s\n", current->organisation->content);
                printf("Creation date: %d/%d/%d\n", current->organisation->creation_date[0], current->organisation->creation_date[1], current->organisation->creation_date[2]);
                printf("Location: (%d, %d)\n", current->organisation->location[0], current->organisation->location[1]);
            }
            else if (current->type == 4)
            {
                printf("Group\n");
                printf("Id: %d\n", current->id);
                printf("Name: %s\n", current->group->name);
                printf("Content: %s\n", current->group->content);
                printf("Creation date: %d/%d/%d\n", current->group->creation_date[0], current->group->creation_date[1], current->group->creation_date[2]);
            }
        }
        current = current->next;
    }

    if (!found)
    {
        printf("Node with id %d does not exist.\n", id);
    }
    return found;
}
void search_node_by_name(char name[20])
{
    ids_info *current = ids_head;
    int found = 0;

    while (current != NULL)
    {
        // search all linked nodes name
        if (current->type == 1)
        {
            if (strcmp(current->individual->name, name) == 0)
            {
                found = 1;
                printf("\nNode found with following details:\n");
                printf("Individual\n");
                printf("Id: %d\n", current->id);
                printf("Name: %s\n", current->individual->name);
                printf("Content: %s\n", current->individual->content);
                printf("Creation date: %d/%d/%d\n", current->individual->creation_date[0], current->individual->creation_date[1], current->individual->creation_date[2]);
                printf("Birthday: %d/%d/%d\n", current->individual->birthday[0], current->individual->birthday[1], current->individual->birthday[2]);
            }
        }
        else if (current->type == 2)
        {
            if (strcmp(current->business->name, name) == 0)
            {
                found = 1;
                printf("\nNode found with following details:\n");
                printf("Business\n");
                printf("Id: %d\n", current->id);
                printf("Name: %s\n", current->business->name);
                printf("Content: %s\n", current->business->content);
                printf("Creation date: %d/%d/%d\n", current->business->creation_date[0], current->business->creation_date[1], current->business->creation_date[2]);
                printf("Location: (%d, %d)\n", current->business->location[0], current->business->location[1]);
            }
        }
        else if (current->type == 3)
        {
            if (strcmp(current->organisation->name, name) == 0)
            {
                found = 1;
                printf("\nNode found with following details:\n");
                printf("Organisation\n");
                printf("Id: %d\n", current->id);
                printf("Name: %s\n", current->organisation->name);
                printf("Content: %s\n", current->organisation->content);
                printf("Creation date: %d/%d/%d\n", current->organisation->creation_date[0], current->organisation->creation_date[1], current->organisation->creation_date[2]);
                printf("Location: (%d, %d)\n", current->organisation->location[0], current->organisation->location[1]);
            }
        }
        else if (current->type == 4)
        {
            if (strcmp(current->group->name, name) == 0)
            {
                found = 1;
                printf("\nNode found with following details:\n");
                printf("Group\n");
                printf("Id: %d\n", current->id);
                printf("Name: %s\n", current->group->name);
                printf("Content: %s\n", current->group->content);
                printf("Creation date: %d/%d/%d\n", current->group->creation_date[0], current->group->creation_date[1], current->group->creation_date[2]);
            }
        }

        current = current->next;
        printf("\n");
    }

    if (!found)
    {
        printf("Node with name %s does not exist.\n", name);
    }
}
void search_node_by_birthday(int birthday[3])
{
    ids_info *current = ids_head;
    int found = 0;

    while (current != NULL)
    {
        // search all linked nodes birthday
        if (current->type == 1)
        {
            if (current->individual->birthday[0] == birthday[0] && current->individual->birthday[1] == birthday[1] && current->individual->birthday[2] == birthday[2])
            {
                found = 1;
                printf("\nNode found with following details:\n");
                printf("Individual\n");
                printf("Id: %d\n", current->id);
                printf("Name: %s\n", current->individual->name);
                printf("Content: %s\n", current->individual->content);
                printf("Creation date: %d/%d/%d\n", current->individual->creation_date[0], current->individual->creation_date[1], current->individual->creation_date[2]);
                printf("Birthday: %d/%d/%d\n", current->individual->birthday[0], current->individual->birthday[1], current->individual->birthday[2]);
            }
        }
        current = current->next;
        printf("\n");
    }

    if (!found)
    {
        printf("Node with birthday %d/%d/%d does not exist.\n", birthday[0], birthday[1], birthday[2]);
    }
}
void search_node_by_type(int type)
{
    ids_info *current = ids_head;
    int found = 0;

    while (current != NULL)
    {
        // search all linked nodes type
        if (current->type == type)
        {
            found = 1;
            printf("\nNode found with following details:\n");
            if (current->type == 1)
            {
                printf("Individual\n");
                printf("Id: %d\n", current->id);
                printf("Name: %s\n", current->individual->name);
                printf("Content: %s\n", current->individual->content);
                printf("Creation date: %d/%d/%d\n", current->individual->creation_date[0], current->individual->creation_date[1], current->individual->creation_date[2]);
                printf("Birthday: %d/%d/%d\n", current->individual->birthday[0], current->individual->birthday[1], current->individual->birthday[2]);
            }
            else if (current->type == 2)
            {
                printf("Business\n");
                printf("Id: %d\n", current->id);
                printf("Name: %s\n", current->business->name);
                printf("Content: %s\n", current->business->content);
                printf("Creation date: %d/%d/%d\n", current->business->creation_date[0], current->business->creation_date[1], current->business->creation_date[2]);
                printf("Location: (%d, %d)\n", current->business->location[0], current->business->location[1]);
            }
            else if (current->type == 3)
            {
                printf("Organisation\n");
                printf("Id: %d\n", current->id);
                printf("Name: %s\n", current->organisation->name);
                printf("Content: %s\n", current->organisation->content);
                printf("Creation date: %d/%d/%d\n", current->organisation->creation_date[0], current->organisation->creation_date[1], current->organisation->creation_date[2]);
                printf("Location: (%d, %d)\n", current->organisation->location[0], current->organisation->location[1]);
            }
            else if (current->type == 4)
            {
                printf("Group\n");
                printf("Id: %d\n", current->id);
                printf("Name: %s\n", current->group->name);
                printf("Content: %s\n", current->group->content);
                printf("Creation date: %d/%d/%d\n", current->group->creation_date[0], current->group->creation_date[1], current->group->creation_date[2]);
            }
        }
        current = current->next;
    }

    if (!found)
    {
        printf("Node with type %d does not exist.\n", type);
    }
}

void search_node()
{
    printf("\nSearch option:\n");
    printf("1. Search by id\n");
    printf("2. Search by name\n");
    printf("3. Search by birthday\n");
    printf("4. Search by type\n");
    printf("Enter choice: ");
    int choice;
    scanf("%d", &choice);
    printf("\n------------------------------------------------------------------------------------\n");

    if (choice == 1)
    {
        printf("Enter id of node to search: ");
        int id;
        scanf("%d", &id);

        search_node_by_id(id);
    }
    else if (choice == 2)
    {
        printf("Enter name of node to search: ");
        char name[20];
        scanf("%s", name);

        search_node_by_name(name);
    }
    else if (choice == 3)
    {
        int birthday[3];
        printf("Enter birthday date of node to search: ");
        scanf("%d", &birthday[0]);
        printf("Enter birthday month of node to search: ");
        scanf("%d", &birthday[1]);
        printf("Enter birthday year of node to search: ");
        scanf("%d", &birthday[2]);

        search_node_by_birthday(birthday);
    }
    else if (choice == 4)
    {
        printf("Node type:\n");
        printf("1.Individual\n2.Business\n3.Organisation\n4.Group\n");
        printf("Enter type of node to search: ");
        int type;
        scanf("%d", &type);

        search_node_by_type(type);
    }
    else
    {
        printf("Invalid choice.\n");
    }
}

// making the social network
individual *does_individual_exists(int id)
{
    individual *found = NULL;
    ids_info *current = ids_head;

    while (current != NULL)
    {
        if (current->id == id)
        {
            if (current->type == 1)
            {
                found = current->individual;
            }
        }
        current = current->next;
    }

    if (!found)
    {
        printf("Individual with id %d does not exist.\n", id);
    }
    return found;
}
business *does_business_exists(int id)
{
    business *found = NULL;
    ids_info *current = ids_head;

    while (current != NULL)
    {
        if (current->id == id)
        {
            if (current->type == 2)
            {
                found = current->business;
            }
        }
        current = current->next;
    }

    if (!found)
    {
        printf("Business with id %d does not exist.\n", id);
    }
    return found;
}
organisation *does_organisation_exists(int id)
{
    organisation *found = NULL;
    ids_info *current = ids_head;

    while (current != NULL)
    {
        if (current->id == id)
        {
            if (current->type == 3)
            {
                found = current->organisation;
            }
        }
        current = current->next;
    }

    if (!found)
    {
        printf("Organisation with id %d does not exist.\n", id);
    }
    return found;
}
group *does_group_exists(int id)
{
    group *found = NULL;
    ids_info *current = ids_head;

    while (current != NULL)
    {
        if (current->id == id)
        {
            if (current->type == 4)
            {
                found = current->group;
            }
        }
        current = current->next;
    }

    if (!found)
    {
        printf("Group with id %d does not exist.\n", id);
    }
    return found;
}
ids_info *does_node_exists(int id)
{
    ids_info *found = NULL;
    ids_info *current = ids_head;

    while (current != NULL)
    {
        if (current->id == id)
        {
            found = current;
        }
        current = current->next;
    }

    if (!found)
    {
        printf("Node with id %d does not exist.\n", id);
    }
    return found;
}

// list of all individual else print no individual
void list_all_individuals()
{
    ids_info *current = ids_head;
    int found = 0;
    printf("List of individuals present: \n");

    while (current != NULL)
    {
        if (current->type == 1)
        {
            found = 1;
            printf("Id: %d\n", current->id);
            printf("Name: %s\n\n", current->individual->name);
        }
        current = current->next;
    }

    if (!found)
    {
        printf(" # No individual # \n");
    }
}
// list of all organisation else print no organisation
void list_all_organisations()
{
    ids_info *current = ids_head;
    int found = 0;
    printf("List of organisations present: \n");

    while (current != NULL)
    {
        if (current->type == 3)
        {
            found = 1;
            printf("Id: %d\n", current->id);
            printf("Name: %s\n\n", current->organisation->name);
        }
        current = current->next;
    }

    if (!found)
    {
        printf(" # No organisation. #\n");
    }
}
// list of all business else print no business
void list_all_businesses()
{
    ids_info *current = ids_head;
    int found = 0;
    printf("List of businesses present: \n");

    while (current != NULL)
    {
        if (current->type == 2)
        {
            found = 1;
            printf("Id: %d\n", current->id);
            printf("Name: %s\n\n", current->business->name);
        }
        current = current->next;
    }

    if (!found)
    {
        printf(" # No business # \n");
    }
}
// list of all group else print no group
void list_all_groups()
{
    ids_info *current = ids_head;
    int found = 0;
    printf("List of groups present: \n");

    while (current != NULL)
    {
        if (current->type == 4)
        {
            found = 1;
            printf("Id: %d\n", current->id);
            printf("Name: %s\n\n", current->group->name);
        }
        current = current->next;
    }

    if (!found)
    {
        printf(" # No group # \n");
    }
}

int individual_already_member_of_group(int individual_id, int group_id)
{
    individual *individual = does_individual_exists(individual_id);
    group *group = does_group_exists(group_id);

    if (individual && group)
    {
        if (individual->cnt_groups == 0)
        {
            return 0;
        }
        for (int i = 0; i < individual->cnt_groups; i++)
        {
            if (individual->linked_groups[i] == group_id)
            {
                return 1;
            }
        }
    }
    return 0;
}

int business_already_member_of_group(int business_id, int group_id)
{
    business *business = does_business_exists(business_id);
    group *group = does_group_exists(group_id);

    if (business && group)
    {
        if (business->cnt_groups == 0)
        {
            return 0;
        }
        for (int i = 0; i < business->cnt_groups; i++)
        {
            if (business->linked_groups[i] == group_id)
            {
                return 1;
            }
        }
    }
    return 0;
}

int individual_already_member_of_organisation(int individual_id, int organisation_id)
{
    individual *individual = does_individual_exists(individual_id);
    organisation *organisation = does_organisation_exists(organisation_id);

    if (individual && organisation)
    {
        if (individual->cnt_organisations == 0)
        {
            return 0;
        }
        for (int i = 0; i < individual->cnt_organisations; i++)
        {
            if (individual->linked_organisations[i] == organisation_id)
            {
                return 1;
            }
        }
    }
    return 0;
}

int individual_already_owner_of_business(int individual_id, int business_id)
{
    individual *individual = does_individual_exists(individual_id);
    business *business = does_business_exists(business_id);

    if (individual && business)
    {
        if (individual->cnt_businesses_as_owner == 0)
        {
            return 0;
        }
        for (int i = 0; i < individual->cnt_businesses_as_owner; i++)
        {
            if (individual->linked_businesses_as_owner[i] == business_id)
            {
                return 1;
            }
        }
    }
    return 0;
}

int individual_already_customer_of_business(int individual_id, int business_id)
{
    individual *individual = does_individual_exists(individual_id);
    business *business = does_business_exists(business_id);

    if (individual && business)
    {
        if (individual->cnt_businesses_as_customer == 0)
        {
            return 0;
        }
        for (int i = 0; i < individual->cnt_businesses_as_customer; i++)
        {
            if (individual->linked_businesses_as_customer[i] == business_id)
            {
                return 1;
            }
        }
    }
    return 0;
}

void individual_as_member_of_group()
{
    list_all_individuals();
    list_all_groups();
    printf("Enter id of individual: ");
    int individual_id;
    scanf("%d", &individual_id);

    printf("Enter id of group: ");
    int group_id;
    scanf("%d", &group_id);

    individual *individual = does_individual_exists(individual_id);
    group *group = does_group_exists(group_id);

    if (individual && group && !individual_already_member_of_group(individual_id, group_id))
    {
        // add group to groups array of individual
        individual->linked_groups[individual->cnt_groups++] = group_id;

        // add individual to members array of group
        group->linked_members[group->cnt_members++] = individual_id;

        printf("\nIndividual with id %d added as member of group with id %d.\n", individual_id, group_id);
    }
    else
    {
        printf("Individual with id %d or group with id %d does not exist or individual is already a member of group.\n", individual_id, group_id);
    }
}

void business_as_member_of_group()
{
    list_all_businesses();
    list_all_groups();
    printf("Enter id of business: ");
    int business_id;
    scanf("%d", &business_id);

    printf("Enter id of group: ");
    int group_id;
    scanf("%d", &group_id);

    business *business = does_business_exists(business_id);
    group *group = does_group_exists(group_id);

    if (business && group && !business_already_member_of_group(business_id, group_id))
    {
        // add group to groups array of business
        business->linked_groups[business->cnt_groups++] = group_id;

        // add business to businesses array of group
        group->linked_businesses[group->cnt_businesses++] = business_id;

        printf("\nBusiness with id %d added as member of group with id %d.\n", business_id, group_id);
    }
    else
    {
        printf("Business with id %d or group with id %d does not exist or business is already a member of group.\n", business_id, group_id);
    }
}

void individual_as_member_of_organisation()
{
    list_all_individuals();
    list_all_organisations();
    printf("Enter id of individual: ");
    int individual_id;
    scanf("%d", &individual_id);

    printf("Enter id of organisation: ");
    int organisation_id;
    scanf("%d", &organisation_id);

    individual *individual = does_individual_exists(individual_id);
    organisation *organisation = does_organisation_exists(organisation_id);

    if (individual && organisation && !individual_already_member_of_organisation(individual_id, organisation_id))
    {
        // add organisation to organisations array of individual
        individual->linked_organisations[individual->cnt_organisations++] = organisation_id;

        // add individual to members array of organisation
        organisation->linked_members[organisation->cnt_members++] = individual_id;

        printf("\nIndividual with id %d added as member of organisation with id %d.\n", individual_id, organisation_id);
    }
    else
    {
        printf("Individual with id %d or organisation with id %d does not exist or individual is already a member of organisation.\n", individual_id, organisation_id);
    }
}

void individual_as_owner_of_business()
{
    list_all_individuals();
    list_all_businesses();
    printf("Enter id of individual: ");
    int individual_id;
    scanf("%d", &individual_id);

    printf("Enter id of business: ");
    int business_id;
    scanf("%d", &business_id);

    individual *individual = does_individual_exists(individual_id);
    business *business = does_business_exists(business_id);

    if (individual && business && !individual_already_owner_of_business(individual_id, business_id))
    {
        // add business to businesses array of individual
        individual->linked_businesses_as_owner[individual->cnt_businesses_as_owner++] = business_id;

        // add individual to owners array of business
        business->linked_owners[business->cnt_owners++] = individual_id;

        printf("\nIndividual with id %d added as owner of business with id %d.\n", individual_id, business_id);
    }
    else
    {
        printf("Individual with id %d or business with id %d does not exist or individual is already an owner of business.\n", individual_id, business_id);
    }
}

void individual_as_customer_of_business()
{
    list_all_individuals();
    list_all_businesses();
    printf("Enter id of individual: ");
    int individual_id;
    scanf("%d", &individual_id);

    printf("Enter id of business: ");
    int business_id;
    scanf("%d", &business_id);

    individual *individual = does_individual_exists(individual_id);
    business *business = does_business_exists(business_id);

    if (individual && business && !individual_already_customer_of_business(individual_id, business_id))
    {
        // add business to businesses array of individual
        individual->linked_businesses_as_customer[individual->cnt_businesses_as_customer++] = business_id;

        // add individual to customers array of business
        business->linked_customers[business->cnt_customers++] = individual_id;

        printf("\nIndividual with id %d added as customer of business with id %d.\n", individual_id, business_id);
    }
    else
    {
        printf("Individual with id %d or business with id %d does not exist or individual is already a customer of business.\n", individual_id, business_id);
    }
}

void add_linked_node()
{

    printf("\nAdd option:\n");
    printf("1. Individual as member of group\n");
    printf("2. Business as member of group\n");
    printf("3. Individual as member of organisation\n");
    printf("4. Individual as owner of business\n");
    printf("5. Individual as customer of business\n");
    printf("Enter choice: ");
    int choice;
    scanf("%d", &choice);

    if (choice == 1)
    {
        individual_as_member_of_group();
    }
    else if (choice == 2)
    {
        business_as_member_of_group();
    }
    else if (choice == 3)
    {
        individual_as_member_of_organisation();
    }
    else if (choice == 4)
    {
        individual_as_owner_of_business();
    }
    else if (choice == 5)
    {
        individual_as_customer_of_business();
    }
    else
    {
        printf("Invalid choice.\n");
    }
}

// post content int the said node(it appends at the end)
// int is_content_duplicate in any node that exists
int is_content_duplicate(char content[200])
{
    ids_info *current = ids_head;
    int found = 0;

    while (current != NULL)
    {
        // search all linked nodes content
        if (current->type == 1)
        {
            if (strcmp(current->individual->content, content) == 0)
            {
                found = 1;
                printf("Individual\n");
                printf("Id: %d\n", current->id);
                printf("Name: %s\n", current->individual->name);
                printf("Content: %s\n", current->individual->content);
                printf("Creation date: %d/%d/%d\n", current->individual->creation_date[0], current->individual->creation_date[1], current->individual->creation_date[2]);
                printf("Birthday: %d/%d/%d\n", current->individual->birthday[0], current->individual->birthday[1], current->individual->birthday[2]);
            }
        }
        else if (current->type == 2)
        {
            if (strcmp(current->business->content, content) == 0)
            {
                found = 1;
                printf("Business\n");
                printf("Id: %d\n", current->id);
                printf("Name: %s\n", current->business->name);
                printf("Content: %s\n", current->business->content);
                printf("Creation date: %d/%d/%d\n", current->business->creation_date[0], current->business->creation_date[1], current->business->creation_date[2]);
                printf("Location: (%d, %d)\n", current->business->location[0], current->business->location[1]);
            }
        }
        else if (current->type == 3)
        {
            if (strcmp(current->organisation->content, content) == 0)
            {
                found = 1;
                printf("Organisation\n");
                printf("Id: %d\n", current->id);
                printf("Name: %s\n", current->organisation->name);
                printf("Content: %s\n", current->organisation->content);
                printf("Creation date: %d/%d/%d\n", current->organisation->creation_date[0], current->organisation->creation_date[1], current->organisation->creation_date[2]);
                printf("Location: (%d, %d)\n", current->organisation->location[0], current->organisation->location[1]);
            }
        }
        else if (current->type == 4)
        {
            if (strcmp(current->group->content, content) == 0)
            {
                found = 1;
                printf("Group\n");
                printf("Id: %d\n", current->id);
                printf("Name: %s\n", current->group->name);
                printf("Content: %s\n", current->group->content);
                printf("Creation date: %d/%d/%d\n", current->group->creation_date[0], current->group->creation_date[1], current->group->creation_date[2]);
            }
        }

        current = current->next;
        printf("\n");
    }

    if (!found)
    {
        printf("Node with content %s does not exist.\n", content);
    }

    return found;
}

void add_content(int id)
{
    ids_info *node = does_node_exists(id);
    int type = node->type;

    if (node)
    {
        printf("Enter content: ");
        char content[200];
        scanf("%s", content);

        // append content to existing content
        if (type == 1)
        {
            strcat(node->individual->content, "\n");
            strcat(node->individual->content, content);
        }
        else if (type == 2)
        {
            strcat(node->business->content, "\n");
            strcat(node->business->content, content);
        }
        else if (type == 3)
        {
            strcat(node->organisation->content, "\n");
            strcat(node->organisation->content, content);
        }
        else if (type == 4)
        {
            strcat(node->group->content, "\n");
            strcat(node->group->content, content);
        }
    }
    else
    {
        printf("Node with id %d does not exist.\n", id);
    }
}

// print 1-hop neighbours of the said id
void print_1_hop_linked_nodes(int id)
{
    ids_info *node = does_node_exists(id);
    int type = node->type;

    if (node)
    {
        printf("\nLinked nodes of node with id %d:\n", id);
        if (type == 1)
        {
            // display content of all linked nodes
            for (int i = 0; i < node->individual->cnt_groups; i++)
            {
                search_node_by_id(node->individual->linked_groups[i]);
            }
            for (int i = 0; i < node->individual->cnt_businesses_as_owner; i++)
            {
                search_node_by_id(node->individual->linked_businesses_as_owner[i]);
            }
            for (int i = 0; i < node->individual->cnt_businesses_as_customer; i++)
            {
                search_node_by_id(node->individual->linked_businesses_as_customer[i]);
            }
            for (int i = 0; i < node->individual->cnt_organisations; i++)
            {
                search_node_by_id(node->individual->linked_organisations[i]);
            }
        }
        else if (type == 2)
        {
            // display content of all linked nodes
            for (int i = 0; i < node->business->cnt_groups; i++)
            {
                search_node_by_id(node->business->linked_groups[i]);
            }
            for (int i = 0; i < node->business->cnt_owners; i++)
            {
                search_node_by_id(node->business->linked_owners[i]);
            }
            for (int i = 0; i < node->business->cnt_customers; i++)
            {
                search_node_by_id(node->business->linked_customers[i]);
            }
        }
        else if (type == 3)
        {
            // display content of all linked nodes
            for (int i = 0; i < node->organisation->cnt_members; i++)
            {
                search_node_by_id(node->organisation->linked_members[i]);
            }
        }
        else if (type == 4)
        {
            // display content of all linked nodes
            for (int i = 0; i < node->group->cnt_members; i++)
            {
                search_node_by_id(node->group->linked_members[i]);
            }
            for (int i = 0; i < node->group->cnt_businesses; i++)
            {
                search_node_by_id(node->group->linked_businesses[i]);
            }
        }
    }
    else
    {
        printf("Node with id %d does not exist.\n", id);
    }
}

// search content
void search_content_using_substring(char substring[20])
{
    ids_info *current = ids_head;
    int found = 0;

    while (current != NULL)
    {
        // search all linked nodes content
        if (current->type == 1)
        {
            if (strstr(current->individual->content, substring) != NULL)
            {
                found = 1;
                printf("Individual\n");
                printf("Id: %d\n", current->id);
                printf("Name: %s\n", current->individual->name);
                printf("Content: %s\n", current->individual->content);
                printf("Creation date: %d/%d/%d\n", current->individual->creation_date[0], current->individual->creation_date[1], current->individual->creation_date[2]);
                printf("Birthday: %d/%d/%d\n", current->individual->birthday[0], current->individual->birthday[1], current->individual->birthday[2]);
            }
        }
        else if (current->type == 2)
        {
            if (strstr(current->business->content, substring) != NULL)
            {
                found = 1;
                printf("Business\n");
                printf("Id: %d\n", current->id);
                printf("Name: %s\n", current->business->name);
                printf("Content: %s\n", current->business->content);
                printf("Creation date: %d/%d/%d\n", current->business->creation_date[0], current->business->creation_date[1], current->business->creation_date[2]);
                printf("Location: (%d, %d)\n", current->business->location[0], current->business->location[1]);
            }
        }
        else if (current->type == 3)
        {
            if (strstr(current->organisation->content, substring) != NULL)
            {
                found = 1;
                printf("Organisation\n");
                printf("Id: %d\n", current->id);
                printf("Name: %s\n", current->organisation->name);
                printf("Content: %s\n", current->organisation->content);
                printf("Creation date: %d/%d/%d\n", current->organisation->creation_date[0], current->organisation->creation_date[1], current->organisation->creation_date[2]);
                printf("Location: (%d, %d)\n", current->organisation->location[0], current->organisation->location[1]);
            }
        }
        else if (current->type == 4)
        {
            if (strstr(current->group->content, substring) != NULL)
            {
                found = 1;
                printf("Group\n");
                printf("Id: %d\n", current->id);
                printf("Name: %s\n", current->group->name);
                printf("Content: %s\n", current->group->content);
                printf("Creation date: %d/%d/%d\n", current->group->creation_date[0], current->group->creation_date[1], current->group->creation_date[2]);
            }
        }

        current = current->next;
        printf("\n");
    }

    if (!found)
    {
        printf("Node with substring %s does not exist.\n", substring);
    }
}

// prints all the id & type of all nodes before asking what to do
void print_ids_info()
{
    {
        ids_info *current = ids_head;

        while (current != NULL)
        {
            printf("\n~~~~~~~~~~~~~~~~\n");
            if (current->type == 1)
            {
                printf("Individual\n");
                printf("Id: %d\n", current->id);
                printf("Name: %s\n", current->individual->name);
                printf("Content: %s\n", current->individual->content);
                printf("Creation date: %d/%d/%d\n", current->individual->creation_date[0], current->individual->creation_date[1], current->individual->creation_date[2]);
                printf("Birthday: %d/%d/%d\n", current->individual->birthday[0], current->individual->birthday[1], current->individual->birthday[2]);
            }
            else if (current->type == 2)
            {
                printf("Business\n");
                printf("Id: %d\n", current->id);
                printf("Name: %s\n", current->business->name);
                printf("Content: %s\n", current->business->content);
                printf("Creation date: %d/%d/%d\n", current->business->creation_date[0], current->business->creation_date[1], current->business->creation_date[2]);
                printf("Location: (%d, %d)\n", current->business->location[0], current->business->location[1]);
            }
            else if (current->type == 3)
            {
                printf("Organisation\n");
                printf("Id: %d\n", current->id);
                printf("Name: %s\n", current->organisation->name);
                printf("Content: %s\n", current->organisation->content);
                printf("Creation date: %d/%d/%d\n", current->organisation->creation_date[0], current->organisation->creation_date[1], current->organisation->creation_date[2]);
                printf("Location: (%d, %d)\n", current->organisation->location[0], current->organisation->location[1]);
            }
            else if (current->type == 4)
            {
                printf("Group\n");
                printf("Id: %d\n", current->id);
                printf("Name: %s\n", current->group->name);
                printf("Content: %s\n", current->group->content);
                printf("Creation date: %d/%d/%d\n", current->group->creation_date[0], current->group->creation_date[1], current->group->creation_date[2]);
            }

            current = current->next;
        }
    }
}

// print 2-hop contents
void display_content_of_individual(int id)
{
    individual *node = does_individual_exists(id);
    if (node)
    {
        printf("Content of %d node:\n", id);
        printf("%s\n\n", node->content);
    }
}

void print_2_hop_content(int id)
{
    individual *ind = does_individual_exists(id);
    if (ind)
    {
        if (ind->cnt_groups)
        {
            printf("Content of 2-hop neighbour individuals(same group) of individual with id %d:\n", id);
            for (int i = 0; i < ind->cnt_groups; ++i)
            {
                group *grp = does_group_exists(ind->linked_groups[i]);
                if (grp->cnt_members)
                    for (int j = 0; j < grp->cnt_members; ++j)
                    {
                        if (grp->linked_members[j] != id)
                            display_content_of_individual(grp->linked_members[j]);
                    }
            }
        }

        if (ind->cnt_organisations)
        {
            printf("Content of 2-hop neighbour individuals(same organisation) of individual with id %d:\n", id);
            for (int i = 0; i < ind->cnt_organisations; ++i)
            {
                group *org = does_group_exists(ind->linked_organisations[i]);
                if (org->cnt_members)
                    for (int j = 0; j < org->cnt_members; ++j)
                    {
                        if (org->linked_members[j] != id)
                            display_content_of_individual(org->linked_members[j]);
                    }
            }
        }
    }
}

int main()
{
    while (1)
    {
        printf("\n 1. Create\n");
        printf(" 2. Delete\n");
        printf(" 3. Search a node\n");
        printf(" 4. Print all 1-hop linked nodes to a given input node\n");
        printf(" 5. Make an individual as member of a group\n");
        printf(" 6. Make an individual as member of an organisation\n");
        printf(" 7. Make an individual as owner of a business\n");
        printf(" 8. Make an individual as customer of a business\n");
        printf(" 9. Add business as a member of group\n");
        printf("10. Create & post content to a node\n");
        printf("11. Search for content posted by any node\n");
        printf("12. Display all content posted by nodes linked to a given node\n");
        printf("13. Print all nodes\n");
        printf("14.Exit\n");
        printf("ENTER CHOICE: ");

        int choice;
        scanf("%d", &choice);

        if (choice == 1)
        {
            create();
        }
        else if (choice == 2)
        {
            delete_node();
        }
        else if (choice == 3)
        {
            search_node();
        }
        else if (choice == 4)
        {
            printf("Enter id of node: ");
            int id;
            scanf("%d", &id);

            print_1_hop_linked_nodes(id);
        }
        else if (choice == 5)
        {
            individual_as_member_of_group();
        }
        else if (choice == 6)
        {
            individual_as_member_of_organisation();
        }
        else if (choice == 7)
        {
            individual_as_owner_of_business();
        }
        else if (choice == 8)
        {
            individual_as_customer_of_business();
        }
        else if (choice == 9)
        {
            business_as_member_of_group();
        }
        else if (choice == 10)
        {
            printf("Enter id of node: ");
            int id;
            scanf("%d", &id);

            add_content(id);
        }
        else if (choice == 11)
        {
            printf("Enter substring to search: ");
            char substring[20];
            scanf("%s", substring);

            search_content_using_substring(substring);
        }
        else if (choice == 12)
        {
            printf("This will print the contents of 2-hop neighbour individuals(same group or organisation) of an individual\n");
            list_all_individuals();

            printf("\nEnter id of node: ");
            int id;
            scanf("%d", &id);
            print_2_hop_content(id);
        }
        else if (choice == 13)
        {
            print_ids_info();
        }
        else if (choice == 14)
        {
            printf("Exiting...\n");
            break;
        }
        else
        {
            printf("Invalid choice.\n");
        }
        printf("====================================================================================\n\n");
    }
    return 0;
}