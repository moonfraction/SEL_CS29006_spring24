#include <iostream>
#include <chrono>
#include <iomanip>

#include "VectorDataset.h"

int main()
{
    // read the dataset: these are the set of vectors to be used to find the k nearest neighbors
    VectorDataset dataset;
    auto start = chrono::high_resolution_clock::now();
    dataset.readDataset("fmnist-train.csv");
    auto end = chrono::high_resolution_clock::now();
    auto duration = chrono::duration_cast<chrono::seconds>(end - start);
    cout << "Elapsed time to read dataset: " << duration.count() << " s\n";

    // check if all vectors of dataset have the same dimension
    if (!dataset.checkDimension())
    {
        cout << "The dataset has vectors with different dimensions" << endl;
        return 1;
    }

    // find the dimension of the dataset
    int dimension = dataset.getDataset()[0].getDimension();
    cout << "Dimension of vectors in train dataset: " << dimension << endl;
    // find the number of vectors in the dataset
    int numVectors = dataset.getDataset().size();
    cout << "Number of vectors in train dataset: " << numVectors << endl;
    cout << "----------------------------------------------------------------------------------\n";

    // find the k nearest neighbors of the first 100 vector in the dataset, here k=5
    VectorDataset testdataset;
    // read the test dataset: these are the set of vectors whose k nearest neighbors are to be found
    testdataset.readDataset("fmnist-test.csv");
    cout << "Total number of vectors in the test dataset: " << testdataset.getDataset().size() << endl;

    VectorDataset TestDataSet;
    // take 100 vectors from the test dataset
    int numTestVectors = 100;
    for (int i = 0; i < numTestVectors; i++)
    {
        TestDataSet.addVector(testdataset.getDataset()[i]);
    }

    // check if all vectors have the same dimension
    if (!TestDataSet.checkDimension())
    {
        cout << "The test dataset has vectors with different dimensions" << endl;
        return 1;
    }
    // check if test data vectors have the same dimension as the dataset
    if (TestDataSet.getDataset()[0].getDimension() != dimension)
    {
        cout << "The test dataset has vectors with different dimension than the dataset" << endl;
        return 1;
    }
    // number of vectors in the test dataset
    cout << "Number of vectors to be tested from test dataset: " << TestDataSet.getDataset().size() << endl;
    cout << "----------------------------------------------------------------------------------\n";

    int k; // number of nearest neighbors to be found
    cout << "Enter the value of k: ";
    cin >> k;
    cout << "Finding the " << k << " nearest neighbors of the first " << numTestVectors << " vectors in the test dataset\n\n";
    int count = 0; // to count the number of test data vectors

    auto total_start = chrono::high_resolution_clock::now();
    for (auto &v : TestDataSet.getDataset())
    {
        printf("TestDataVector %3d: ", ++count);
        auto start = chrono::high_resolution_clock::now();
        VectorDataset nearestNeighbors = dataset.kNearestNeighbors(v, k);
        auto end = chrono::high_resolution_clock::now();
        auto duration = chrono::duration_cast<chrono::milliseconds>(end - start);
        cout << fixed << setprecision(4);
        cout << "Elapsed time: " << duration.count() << " ms\n";
    }
    auto total_end = chrono::high_resolution_clock::now();
    auto total_duration = chrono::duration_cast<chrono::seconds>(total_end - total_start);
    cout << "Total Elapsed time to find the " << k << " nearest neighbors of the first " << numTestVectors << " vectors in the test dataset: " << total_duration.count() << " s\n";

    return 0;
}
