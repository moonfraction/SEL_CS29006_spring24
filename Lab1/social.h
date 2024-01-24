/*
Software Engineering Lab Assignment -1

Instructions:
1. You are required to implement a social network application in C.
2. The application should be menu driven.
3. The application should be able to create and delete the following entities:
    a. Individual
    b. Business
    c. Organization
    d. Group
4. The application should be able to link the above entities as follows:
    a. Individual can be a member of a group
    b. Individual can be a member of an organization
    c. Individual can be an owner of a business
    d. Individual can be a customer of a business
    e. Business can be a member of a group
5. The application should be able to add content to the above entities.
6. The application should be able to display the content of the above entities. 
7. The application should be able to display the content of the 2-hop neighbor of an individual.
8. The application should be able to search all the content for a given input string.
9. The application should be able to search for an entity by name, birthday, type, and ID.
10. The application should be able to display all the entities created so far.

Desciption:
1. Create:
    a. Individual
        i. ID is assigned by system as the smallest unused natural number
        ii. Name and content input is done by user
        iii. Creation date is assigned as today’s date by system using time.h library
        iv. Birthday is stored as array of 3 integers
        v. Checks if the birthday is valid
        vi. Birthday[0] = day, birthday[1] = month, birthday[2] = year
        vii. Store the IDs of each kind of linked nodes in separate arrays with length 100
        viii. Name of any node has max length 20
        ix. Content of any node has max length 100
    b. Business
        i. ID is assigned by system as the smallest unused natural number
        ii. Name and content input is done by user
        iii. Creation date is assigned as today’s date by system using time.h library
        iv. Location is stored as array of 2 integers
        v. Location[0] = x coordinate, location[1] = y coordinate
        vi. Store the IDs of each kind of linked nodes in separate arrays with length 100
        vii. Name of any node has max length 20
        viii. Content of any node has max length 100
    c. Organization
        i. ID is assigned by system as the smallest unused natural number
        ii. Name and content input is done by user
        iii. Creation date is assigned as today’s date by system using time.h library
        iv. Location is stored as array of 2 integers
        v. Location[0] = x coordinate, location[1] = y coordinate
        vi. Store the IDs of each kind of linked nodes in separate arrays with length 100
        vii. Name of any node has max length 20
        viii. Content of any node has max length 100
    d. Group
        i. ID is assigned by system as the smallest unused natural number
        ii. Name and content input is done by user
        iii. Creation date is assigned as today’s date by system using time.h library
        iv. Store the IDs of each kind of linked nodes in separate arrays with length 100
        v. Name of any node has max length 20
        vi. Content of any node has max length 100

    It create the said node, and adds it to a linked list containing all nodes in increasing order of IDs.

2. Delete:
    a. Ask the ID to be deleted
    b. Delete it and free the node memory from the ids_info link

3. Search:
    a. Ask to enter the way to search a node
    b. Call the search function according to the way to search
    c. Search by ID
        i. Ask for ID
        ii. Search for the ID in the ids_info link
        iii. If found, print the information of the node
        iv. If not found, print “ID not found”
    d. Search by name
        i. Ask for name
        ii. Search for the name in the ids_info link
        iii. If found, print the information of the node
        iv. If not found, print “Name not found”
    e. Search by birthday
        i. Ask for birthday
        ii. Search for the birthday in the ids_info link
        iii. If found, print the information of the node
        iv. If not found, print “Birthday not found”
    f. Search by type
        i. Ask for type
        ii. Search for the type in the ids_info link
        iii. If found, print the information of the node
        iv. If not found, print “Type not found”

    



*/


// ID is assigned by system as the smallest unused natural number
// creation date is assigned as todays date by system using time.h library
// store the ids of each kind of linked nodes in seperate arrays with length 100
// name of any node has max length 20
// content of any node has max length 100




//------------Define nodes of each type------------
/*
ID is assigned by system as the smallest unused natural number to every new node
name and content input is done by user for all kind of nodes
name of any node has max length 20
content of any node has max length 100
creation date is assigned as todays date by system using time.h library
every node can link to at max 100 other type of nodes

user input for birthday of individual
birthday is stored as array of 3 integers
birthday[0] = day, birthday[1] = month, birthday[2] = year
user input for location of business and organisation
location is stored as array of 2 integers
location[0] = x coordinate, location[1] = y coordinate
*/

// user input for birthday of individual
typedef struct individual
{
    int id;
    char name[20];
    char content[200];
    int creation_date[3]; 
    int birthday[3];  

    int cnt_businesses_as_owner, cnt_businesses_as_customer, cnt_organisations, cnt_groups;

    int linked_businesses_as_owner[100];
    int linked_businesses_as_customer[100];
    int linked_organisations[100];
    int linked_groups[100];

} individual;

//user input location (int x, int y) of business
typedef struct business
{
    int id;
    char name[20];
    int creation_date[3]; 
    char content[200];
    int location[2]; //(x, y) coordinates

    int cnt_owners, cnt_customers, cnt_groups;
    int linked_owners[100];
    int linked_customers[100];
    int linked_groups[100];

} business;

//user input location (int x, int y) of organisation
typedef struct organisation
{
    int id;
    char name[20];
    int creation_date[3];
    char content[200];
    int location[2]; //(x, y) coordinates

    int cnt_members;
    int linked_members[100];

} organisation;

typedef struct group
{
    int id;
    char name[20];
    char content[200];
    int creation_date[3]; 

    int cnt_members, cnt_businesses;
    int linked_members[100];
    int linked_businesses[100];

} group;




//--------------------linked list to store all nodes with ids, types and pointer to that type of node--------------

// this linked list stores information of all nodes
// nodes are arranged in increaing order of the "id"
//each node has an id of node, type of node and a pointer to each kind of node
//only the pointer with said stored ID and type points to that node
//all other type pointers points to NULL
typedef struct ids_info
{
    int id;
    int type;

    // link only one node and initialize others to NULL
    individual *individual;
    business *business;
    organisation *organisation;
    group *group;

    struct ids_info *next;

} ids_info;



//------------- CREATE NODE functions---------------

void create(); // create function to ask the type of node to be created
void create_node(int type); // create the required type of node 
int get_smallest_unused_id(); // get the smallest unused id(>=1) to assign the newly created node

int is_birthday_possible(int birthday[3]); // checks if the given birthday is possible or not for an individual
individual *create_individual(int id, char name[20], char content[200], int birthday[3]);
business *create_business(int id, char name[20], char content[200], int location[2]);
organisation *create_organisation(int id, char name[20], char content[200], int location[2]);
group *create_group(int id, char name[20], char content[200]);

//add the newly created node in the ids_info link
void add_id(int id, int type, individual *individual, business *business, organisation *organisation, group *group);  


//------------- DELETE NODE-------------------

void delete_node(); //asks the id to be deleted and deletes it and frees the node memory from the ids_info link



//-------------- SEARCH NODE----------------------

void search_node(); //asks to enter the way to search a node 

//call the search function according to the way to search
int search_node_by_id(int id);
void search_node_by_name(char name[20]);
void search_node_by_birthday(int birthday[3]);
void search_node_by_type(int type);


//------------------ create SOCIAL NETWORK--------------------

void add_linked_node(); //asks the way to link the nodes and calls the required function

//gives list of all nodes present that are about to be linked
void list_all_individuals();
void list_all_businesses();
void list_all_organisations();
void list_all_groups();


//Helper functions for linking various kind of nodes
//checks weather the node with given id and type exists 
//returns the pointer to the node if the ID of asked type exists

individual *does_individual_exists(int id);
business *does_business_exists(int id);
organisation *does_organisation_exists(int id);
group *does_group_exists(int id);

//returns the pointer to the node if the ID exists
ids_info *does_node_exists(int id);

//checks if the said nodes are already linked
int individual_already_member_of_group(int individual_id, int group_id);
int individual_already_member_of_organisation(int individual_id, int organisation_id);
int individual_already_owner_of_business(int individual_id, int business_id);
int individual_already_customer_of_business(int individual_id, int business_id);
int business_already_member_of_group(int business_id, int group_id);

//functions to link the said nodes
//checks if ids of given types exists that are about to be linked
//the first type node adds the id of second type node in its linked_nodes array and increase the count of that linked_node

// add group to groups array of individual
// add individual to members array of group
void individual_as_member_of_group();

// add business to businesses array of individual
// add individual to owners array of business
void individual_as_owner_of_business();

// add business to businesses array of individual
// add individual to customers array of business
void individual_as_customer_of_business();

// add organisation to organisations array of individual
// add individual to members array of organisation
void individual_as_member_of_organisation();

// add group to groups array of business
// add business to businesses array of group
void business_as_member_of_group();



//-----------------add content to said id node-----------

int is_content_duplicate(char content[200]); //checks if the content is already present in the node
void add_content(int id); //it appends at the end


//------------------display contents of 2-hop neighbour INDIVIDUALS-------------

//asks for ID of individual
//searches for individuals in same GROUP or ORGANISATION
void print_2_hop_content(int id); //prints the content of all the 2-hop neighbours of the said individual
void display_content_of_individual(int id); //prints the content of the said individual


//-------------------search all the contents for the said input string--------------

void search_content_using_substring(char substring[20]); //searches all the nodes for the said substring and prints the content of the nodes that contains the substring


//-------------------- print all the nodes created so far-----------

void print_ids_info(); //prints all the information of all the nodes that exists
