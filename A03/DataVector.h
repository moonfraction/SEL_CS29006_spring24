#include <vector>
using namespace std;

class DataVector
{
    vector<double> v;

public:
    // Constructor
    DataVector(int dimension = 0);
    // Copy constructor
    DataVector(const DataVector &other);
    // Destructor
    ~DataVector();

    // Set dimension removing old data
    void setDimension(int dimension = 0);
    // Get dimension
    int getDimension() const;

    // Overloaded operators
    DataVector &operator=(const DataVector &other);
    DataVector operator+(const DataVector &other);
    DataVector operator-(DataVector other);
    double operator*(const DataVector &other);

    // Methods
    double norm();
    double dist(const DataVector &other);
    double distSquared(const DataVector &other);
    void assign(int index, double value);
    void print();
};