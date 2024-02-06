#include <cmath>
#include <iostream>
#include "DataVector.h"

// Class implementation
// Constructor
DataVector::DataVector(int dimension)
{
    v.resize(dimension);
}
// Copy constructor
DataVector::DataVector(const DataVector &other)
{
    v = other.v;
}
// Destructor
DataVector::~DataVector()
{
    v.clear();
}

// Set dimension removing old data
void DataVector::setDimension(int dimension)
{
    v.clear();
    v.resize(dimension);
}
// Get dimension
int DataVector::getDimension() const
{
    return v.size();
}

// Overloaded operators
// Assignment operator
DataVector &DataVector::operator=(const DataVector &other)
{
    v = other.v;
    return *this;
}

// Addition
DataVector DataVector::operator+(const DataVector &other)
{
    DataVector result;
    result.v.resize(v.size());
    for (int i = 0; i < v.size(); i++)
    {
        result.v[i] = v[i] + other.v[i];
    }
    return result;
}

// Subtraction
DataVector DataVector::operator-(DataVector other)
{
    DataVector result;
    result.v.resize(v.size());
    for (int i = 0; i < v.size(); i++)
    {
        result.v[i] = v[i] - other.v[i];
    }
    return result;
}

// Dot product
double DataVector::operator*(const DataVector &other)
{
    double result = 0;
    for (int i = 0; i < v.size(); i++)
    {
        result += v[i] * other.v[i];
    }
    return result;
}

// Methods
// norm
double DataVector::norm()
{
    double result = 0;
    for (int i = 0; i < v.size(); i++)
    {
        result += v[i] * v[i];
    }
    return sqrt(result);
}

// dist
double DataVector::dist(const DataVector &other)
{
    DataVector result = *this - other;
    return result.norm();
}

// distSquared
// to avoid the sqrt operation, and save some time
double DataVector::distSquared(const DataVector &other)
{
    DataVector result = *this - other;
    double dist = 0;
    for (int i = 0; i < v.size(); i++)
    {
        dist += result.v[i] * result.v[i];
    }
    return dist;
}

// Assign
void DataVector::assign(int index, double value)
{
    v[index] = value;
}

// Print
void DataVector::print()
{
    for (int i = 0; i < v.size(); i++)
    {
        cout << v[i] << " ";
    }
    cout << endl;
}