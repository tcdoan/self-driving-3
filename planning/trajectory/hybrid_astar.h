#ifndef HYBRID_BREADTH_FIRST_H_
#define HYBRID_BREADTH_FIRST_H_

#include <vector>
using std::vector;

class HBF 
{
public:
    HBF();
    virtual ~HBF();

    struct maze_s {
        int g;
        int f;
        double x;
        double y;
        double theta;
    };

    struct maze_path {
        vector<vector<vector<int>>> closed;
        vector<vector<vector<maze_s>>> came_from;
        maze_s final;
    };

    int theta_to_stack_number(double theta);

    int idx(double float_num);

    vector<maze_s> expand(const maze_s &state,  const vector<int> &goal);

    vector<maze_s> reconstruct_path
    (
        vector<vector<vector<maze_s>>> &came_from,
        vector<double> &start, HBF::maze_s &final
    );

    maze_path search
    (
        vector<vector<int>> &grid,
        vector<double> &start,
        vector<int> &goal
    );

private:
    double h(double x, double y, const vector<int> &goal);
    int h2(double x, double y, const vector<int> &goal);
    const int NUM_THETA_CELLS = 90;
    const double SPEED = 1.45;
    const double LENGTH = 0.5;
};

#endif  // HYBRID_BREADTH_FIRST_H_