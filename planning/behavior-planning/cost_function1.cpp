#include <iostream>
#include <cmath>

using std::abs;
using std::cout;
using std::endl;
using std::exp;

double goal_distance_cost(int goal_lane, int intended_lane, int final_lane,
                          double distance_to_goal)
{
    // The cost increases with both the distance of intended lane from the goal
    //   and the distance of the final lane from the goal. The cost of being out
    //   of the goal lane also becomes larger as the vehicle approaches the goal.

    double delta_d = abs(intended_lane - goal_lane) + abs(final_lane - goal_lane);
    double cost = 1 - exp(-delta_d / distance_to_goal);

    return cost;
}

int main()
{
    int goal_lane = 0;

    // Test cases used for grading - do not change.
    double cost;
    cout << "Costs for (intended_lane, final_lane, goal_distance):" << endl;
    cout << "---------------------------------------------------------" << endl;
    cost = goal_distance_cost(goal_lane, 2, 2, 1.0);
    cout << "The cost is " << cost << " for "
         << "(2, 2, 1.0)" << endl;
    cost = goal_distance_cost(goal_lane, 2, 2, 10.0);
    cout << "The cost is " << cost << " for "
         << "(2, 2, 10.0)" << endl;
    cost = goal_distance_cost(goal_lane, 2, 2, 100.0);
    cout << "The cost is " << cost << " for "
         << "(2, 2, 100.0)" << endl;
    cost = goal_distance_cost(goal_lane, 1, 2, 100.0);
    cout << "The cost is " << cost << " for "
         << "(1, 2, 100.0)" << endl;
    cost = goal_distance_cost(goal_lane, 1, 1, 100.0);
    cout << "The cost is " << cost << " for "
         << "(1, 1, 100.0)" << endl;
    cost = goal_distance_cost(goal_lane, 0, 1, 100.0);
    cout << "The cost is " << cost << " for "
         << "(0, 1, 100.0)" << endl;
    cost = goal_distance_cost(goal_lane, 0, 0, 100.0);
    cout << "The cost is " << cost << " for "
         << "(0, 0, 100.0)" << endl;

    return 0;
}