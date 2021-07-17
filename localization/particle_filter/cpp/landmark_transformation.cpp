#include <cmath>
#include <iostream>
#include <vector>
#include <iomanip>

struct Point {
    double x;
    double y;
    double theta;
};

std::ostream& operator<<(std::ostream& out, const Point& p) {
    out << "(" << std::setprecision(1) << p.x << ", " << p.y << ", " << p.theta << ")";
    return out;
}

Point carToMapTransform(Point p, Point obs) {
    double theta = p.theta - obs.theta;
    double x_m = p.x + (cos(theta) * obs.x) - (sin(theta) * obs.y);
    double y_m = p.y + (sin(theta) *  obs.x) + (cos(theta) * obs.y);
    return Point{x_m, y_m, theta};
}

int main()
{
    Point particle{4.0,5.0, -M_PI / 2};
    std::cout << "Particle at " << particle << std::endl;

    std::vector<Point> obs = {{2.0, 2.0, 0.0}, {3.0, -2.0, 0.0}, {0.0, -4.0, 0.0}};
    for(Point ob: obs) {
        std::cout << "Observation in car coordinate system: " << ob << std::endl;
        std::cout << "Map coordinate system: " << carToMapTransform(particle, ob) << std::endl;
    }

    return 0;
}