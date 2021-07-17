#include <cmath>
#include <iostream>
#include <vector>
#include <iomanip>

using namespace std;

const double STD_DEV_X = .3;
const double STD_DEV_Y = .3;

struct Point {
    double x;
    double y;
    double theta;
};

std::ostream& operator<<(std::ostream& out, const Point& p) {
    out << "(" << std::setprecision(1) << p.x << ", " << p.y << ", " << p.theta << ")";
    return out;
}

double measProb(Point obs, Point landmark) {
    double coeff = 1/(2*M_PI*STD_DEV_X*STD_DEV_Y);
    double x_diff_sq = pow(obs.x - landmark.x, 2);
    double y_diff_sq = pow(obs.y - landmark.y, 2);
    double x_denom = 2*pow(STD_DEV_X, 2);
    double y_denom = 2*pow(STD_DEV_Y, 2);
    double exponent = exp(-(x_diff_sq/x_denom + y_diff_sq/y_denom));
    return coeff*exponent;
}

int main()
{
    vector<Point> mapObs = {{6, 3, -2}, {2, 2, -2}, {0, 5, -2}};
    vector<Point> landmarks = {{5,3,0},{2,1,0},{2,1,0}};

    double finalProb = 1;
    for(int i = 0; i < mapObs.size(); i++) {
        double prob = measProb(mapObs[i], landmarks[i]);
        cout << "Measurement Probability is " << std::scientific << prob << endl;
        finalProb *= prob;
    }
    cout << "Final Measurement Probability is " << std::scientific << finalProb << endl;

    return 0;
}