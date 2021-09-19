#include <cmath>
#include <iostream>
#include <vector>

#include <Eigen/Dense>
#include "grader.h"

using std::vector;
using Eigen::MatrixXd;
using Eigen::VectorXd;

/**
 * TODO: complete this function
 */
vector<double> JMT(
    vector<double> &start, 
    vector<double> &end, 
    double T) 
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

    double si = start[0];
    double siDot = start[1];
    double siDotDot = start[2];

    double sf = end[0];
    double sfDot = end[1];
    double sfDotDot = end[2];

    // x holds [alpha3, alpha4, alpha5]
    // Solve Ax=b for x.
    VectorXd x(3);
    MatrixXd A(3,3);

    A << T*T*T, T*T*T*T, T*T*T*T*T,
        3*T*T, 4*T*T*T, 5*T*T*T*T,
        6*T, 12*T*T, 20*T*T*T;

    VectorXd b(3);
    b << sf - (si + siDot*T + 0.5*siDotDot*T*T), sfDot - (siDot+siDotDot*T), sfDotDot - siDotDot;

    x = A.fullPivHouseholderQr().solve(b);
    return {si, siDot, 0.5*siDotDot, x(0), x(1), x(2)};
}

int main() {

  // create test cases
  vector< test_case > tc = create_tests();
  bool total_correct = true;

  for(int i = 0; i < tc.size(); ++i) 
  {
    vector<double> jmt = JMT(
        tc[i].start, 
        tc[i].end, 
        tc[i].T);

    bool correct = close_enough(jmt, answers[i]);
    total_correct &= correct;
  }

  if(!total_correct) 
  {
    std::cout << "Try again!" << std::endl;
  } else {
    std::cout << "Nice work!" << std::endl;
  }

  return 0;
}