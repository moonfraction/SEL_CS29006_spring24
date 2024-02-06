#include "VectorDataset.h"
#include <queue>
#include <vector>
#include <algorithm>

// Method to find the k nearest neighbors of a given vector
// The method returns a new VectorDataset containing the k nearest neighbors
VectorDataset VectorDataset::kNearestNeighbors(DataVector vector, int k)
{
    // Define a priority queue, the top element will be the one with the greatest distance
    auto comp = [](const pair<double, DataVector> &a, const pair<double, DataVector> &b)
    {
        return a.first < b.first;
    };
    // The priority queue will store pairs of distance and DataVector
    priority_queue<pair<double, DataVector>, std::vector<pair<double, DataVector>>, decltype(comp)> pq(comp);

    // Iterate through the dataset and calculate the distance between the given vector and each vector in the dataset
    for (const auto &dataVector : dataset)
    {
        double distance = vector.distSquared(dataVector);
        pq.push(make_pair(distance, dataVector));

        // If the size of the queue is greater than k, remove the top element
        if (pq.size() > k)
        {
            pq.pop();
        }
    }

    // Create a new VectorDataset to store the k nearest neighbors
    VectorDataset nearestNeighbors(vector.getDimension());
    while (!pq.empty())
    {
        nearestNeighbors.dataset.push_back(pq.top().second);
        pq.pop();
    }

    return nearestNeighbors;
}
