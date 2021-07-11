#include <algorithm>
#include <iostream>
#include <vector>
#include "helpers.h"

using std::vector;

vector<float> pseudo_range_estimator(
    const vector<float> &landmark_positions,
    float pseudo_position)
{
  vector<float> pseudo_ranges;

  // loop over number of landmarks and estimate pseudo ranges
  for (int l = 0; l < landmark_positions.size(); ++l)
  {
    // estimate pseudo range for each single landmark
    // and the current state position pose_i:
    float range_l = landmark_positions[l] - pseudo_position;
    if (range_l > 0.0f)
    {
      pseudo_ranges.push_back(range_l);
    }
  }

  sort(pseudo_ranges.begin(), pseudo_ranges.end());
  return pseudo_ranges;
}

// Observation model function
// calculates likelihood prob term based on landmark proximity
// For each observation:
//  - determine if a pseudo range vector exists for the current pseudo position x
//  - if the pseudo range vector exists, extract and store the minimum distance, element 0 of the sorted vector,
//    and remove that element (so we don't re-use it). This will be passed to norm_pdf
//  - if the pseudo range vector does not exist, pass the maximum distance to norm_pdf
//    use norm_pdf to determine the observation model probability
//  - return the total probability
float observation_model
(
    vector<float> landmark_positions,
    vector<float> observations,
    vector<float> pseudo_ranges,
    float distance_max,
    float observation_stdev
)
{

  float distance_prob = 1.0;
  for (int i = 0; i < observations.size(); i++)
  {
    float p_likelihood;
    if (!pseudo_ranges.empty()) 
    {
      float minDist = pseudo_ranges[0];
      p_likelihood =  Helpers::normpdf( observations[i], minDist, observation_stdev);
      pseudo_ranges.erase(pseudo_ranges.begin());
    } 
    else 
    {
      p_likelihood =  Helpers::normpdf(observations[i], distance_max, observation_stdev);
    }
    distance_prob *= p_likelihood;
  }
  return distance_prob;
}

int main()
{
  float observation_stdev = 1.0f;
  int map_size = 25;
  float distance_max = map_size;
  vector<float> landmark_positions{5, 10, 12, 20};
  vector<float> observations{5.5, 13, 15};

  // step through each pseudo position x (i)
  for (int i = 0; i < map_size; ++i)
  {
    float pseudo_position = float(i);

    // get pseudo ranges
    vector<float> pseudo_ranges = pseudo_range_estimator(
        landmark_positions,
        pseudo_position);

    //get observation probability
    float observation_prob = observation_model(
        landmark_positions,
        observations,
        pseudo_ranges,
        distance_max,
        observation_stdev);

    std::cout << observation_prob << std::endl;
  }

  return 0;
}

