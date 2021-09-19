# Implement a Behavior Planner

Implement a behavior planner and cost functions for highway driving. 
- The planner will use prediction data to set the state of the ego vehicle to one of 5 values 
- and generate a corresponding vehicle trajectory:
    - "KL" - Keep Lane
    - "LCL" / "LCR"- Lane Change Left / Lane Change Right
    - "PLCL" / "PLCR" - Prepare Lane Change Left / Prepare Lane Change Right

The objective is to navigate through traffic to the goal in as little time as possible.
- Note that the goal lane and **s** value, as well as the traffic speeds for each lane, are set in *main.cpp* below. 
- Since the goal is in the slowest lane, in order to get the lowest time, you'll want to choose cost functions and weights to drive in faster lanes when appropriate. 
- We've provided two suggested cost functions in *cost.cpp*.

### Implement the `choose_next_state` method in the vehicle.cpp class. 
- You can use the Behavior Planning Pseudocode concept as a guideline for your implementation. 
- In this quiz, there are a couple of small differences from that pseudocode: you'll be returning a best trajectory corresponding to the best state instead of the state itself. 
- Additionally, the function inputs will be slightly different in this quiz than in the classroom concept. For this part of the quiz, we have provided several useful functions:
    - `successor_states()` - Uses the current state to return a vector of possible successor states for the finite state machine.
    - `generate_trajectory()` - Returns a vector of Vehicle objects representing a vehicle trajectory, given a state and predictions. Note that trajectory vectors might have size 0 if no possible trajectory exists for the state.
    - `calculate_cost()` - Included from cost.cpp, computes the cost for a trajectory.

### Choose appropriate weights for the cost functions in `cost.cpp` to induce the desired vehicle behavior. 
- Two suggested cost functions have been implemented based on previous quizzes, 
- You are free to experiment with your own cost functions. 
- The `get_helper_data()` function in cost.cpp provides some preprocessing of vehicle data that may be useful in your cost functions. 
- See if you can get the vehicle to move into a fast lane for a portion of the track and then move back to reach the goal!