#include <cmath>
#include <iostream>
#include <vector>
#include <iomanip>
#include <limits>

using namespace std;

struct Point {
    double x;
    double y;
    double theta;
};

std::ostream& operator<<(std::ostream& out, const Point& p) {
    out << "(" << std::setprecision(1) << p.x << ", " << p.y << ", " << p.theta << ")";
    return out;
}

Point nearestNeighbor(Point obs, const vector<Point>& landmarks) {
    double minDist = std::numeric_limits<double>::infinity();
    Point nearest;
    for(Point p: landmarks) {
        double dist = sqrt(pow(obs.x-p.x, 2) + pow(obs.y-p.y, 2));
        if(dist < minDist) {
            minDist = dist;
            nearest = p;
        }
    }
    return nearest;
}

int main()
{
    vector<Point> mapObs = {{6, 3, -2}, {2, 2, -2}, {0, 5, -2}};
    vector<Point> landmarks = {{5,3,0},{2,1,0},{6,1,0},{7,4,0},{4,7,0}};

    for(Point ob: mapObs) {
        cout << "Closest landmark is " << nearestNeighbor(ob, landmarks) << endl;
    }

    return 0;
}