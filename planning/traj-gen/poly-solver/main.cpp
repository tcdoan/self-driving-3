#include <cmath>
#include <iostream>
#include <vector>

#include "Eigen/Dense"
#include "grader.h"

using Eigen::MatrixXd;
using Eigen::VectorXd;
using std::vector;

/**
 * TODO: complete this function
 */
vector<double> JMT(vector<double> &start, vector<double> &end, double T)
{
    /**
   * Calculate the Jerk Minimizing Trajectory that connects the initial state
   * to the final state in time T.
   *
   * @param start - the vehicles start location given as a length three array
   *   corresponding to initial values of [s, s_dot, s_double_dot]
   * @param end - the desired end state for vehicle. Like "start" this is a
   *   length three array.
   * @param T - The duration, in seconds, over which this maneuver should occur.
   *
   * @output an array of length 6, each value corresponding to a coefficent in 
   *   the polynomial:
   *   s(t) = a_0 + a_1 * t + a_2 * t**2 + a_3 * t**3 + a_4 * t**4 + a_5 * t**5
   *
   * EXAMPLE
   *   > JMT([0, 10, 0], [10, 10, 0], 1)
   *     [0.0, 10.0, 0.0, 0.0, 0.0, 0.0]
   */
    Eigen::Matrix3f A;
    Eigen::Vector3f b;
    A << T*T*T, T*T*T*T, T*T*T*T*T,
       3*T*T, 4*T*T*T,5*T*T*T*T,
       6*T, 12*T*T, 20*T*T*T;
    b << end[0]-(start[0]+start[1]*T+start[2]/2*T*T),
       end[1]-(start[1]+start[2]*T),
       end[2]-start[2];
    Eigen::Vector3f x = A.partialPivLu().solve(b);
    return {start[0], start[1], start[2]/2, x[0], x[1], x[2]};
}

int main()
{

    // create test cases
    vector<test_case> tc = create_tests();

    bool total_correct = true;

    for (int i = 0; i < tc.size(); ++i)
    {
        vector<double> jmt = JMT(tc[i].start, tc[i].end, tc[i].T);
        bool correct = close_enough(jmt, answers[i]);
        total_correct &= correct;
    }

    if (!total_correct)
    {
        std::cout << "Try again!" << std::endl;
    }
    else
    {
        std::cout << "Nice work!" << std::endl;
    }

    return 0;
}