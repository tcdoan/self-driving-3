#include <algorithm>
#include <iostream>
#include <vector>

#include "helpers.h"

using std::vector;

// set standard deviation of control:
float control_stdev = 1.0f;

// meters vehicle moves per time step
float movement_per_timestep = 1.0f;

// number of x positions on map
int map_size = 25;

// define landmarks
vector<float> landmark_positions {5, 10, 12, 20};

vector<float> pseudo_range_estimator
(
    vector<float> landmark_positions, 
    float pseudo_position
) 
{
  vector<float> pseudo_ranges;
            
  // loop over number of landmarks and estimate pseudo ranges
  for (int k = 0; k < landmark_positions.size(); k++)
  {
      if (landmark_positions[k] > pseudo_position) 
      {
          pseudo_ranges.push_back(landmark_positions[k] - pseudo_position);
      }
  }
  
  // sort pseudo range vector
  std::sort(pseudo_ranges.begin(), pseudo_ranges.end());
    
  return pseudo_ranges;
}

int main() {    
  
  // step through each pseudo position x (i)
  for (int i = 0; i < map_size; ++i) {
    float pseudo_position = float(i);

    // get pseudo ranges
    vector<float> pseudo_ranges = pseudo_range_estimator(
        landmark_positions,
        pseudo_position);

    if (pseudo_ranges.size() > 0) 
    {
      for (int s = 0; s < pseudo_ranges.size(); ++s) 
      {
        std::cout << "x: " << i << "\t" << pseudo_ranges[s] << std::endl;
      }

      std::cout << "-----------------------" << std::endl;
    }   
  } 

  return 0;
}
