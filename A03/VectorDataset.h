#include <string>
#include <fstream>
#include <sstream>

#include "DataVector.h"

class VectorDataset
{
    vector<DataVector> dataset;

public:
    // Constructor
    VectorDataset() {}
    // Constructor with a vector size
    VectorDataset(int dimension) { dataset.resize(dimension); }

    // Destructor
    ~VectorDataset() {}

    // Method to read a dataset from a CSV file
    void readDataset(string filename)
    {
        ifstream file(filename);
        string line;
        while (getline(file, line))
        {
            stringstream ss(line);
            string token;
            DataVector dv;
            vector<double> v;
            while (getline(ss, token, ','))
            {
                v.push_back(stod(token));
            }
            dv.setDimension(v.size());

            // assign the values of v to dv, as the dv is private we need to use the assign method
            for (int i = 0; i < v.size(); i++)
            {
                dv.assign(i, v[i]);
            }
            dataset.push_back(dv);
        }
    }

    // Method to add a vector to the dataset
    void addVector(DataVector vector) { dataset.push_back(vector); }

    // Getter for the dataset
    vector<DataVector> getDataset() { return dataset; }

    // is the dataset empty
    bool empty() { return dataset.empty(); }

    // check all vectors have same dimension, also check if the dataset is empty
    bool checkDimension()
    {
        if (dataset.empty())
        {
            return false;
        }
        int dimension = dataset[0].getDimension();
        for (auto &v : dataset)
        {
            if (v.getDimension() != dimension)
            {
                return false;
            }
        }
        return true;
    }

    // Method to find the k nearest neighbors of a given vector
    VectorDataset kNearestNeighbors(DataVector vector, int k);

    // Print the dataset
    void print()
    {
        for (auto &v : dataset)
        {
            v.print();
        }
    }
};