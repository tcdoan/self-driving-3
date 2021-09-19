#include "classifier.h"
#include <math.h>
#include <string>
#include <vector>

using Eigen::ArrayXd;
using std::string;
using std::vector;

// Initializes GNB
GNB::GNB()
{
  leftMean << 0,0,0,0;
  rightMean << 0,0,0,0;
  keepMean << 0,0,0,0;

  leftVar << 0,0,0,0;
  rightVar << 0,0,0,0;
  keepVar << 0,0,0,0;

  leftPrior = 0;
  rightPrior = 0;
  keepPrior = 0;
}

GNB::~GNB() {}

void GNB::train(
  const vector<vector<double>> &data, 
  const vector<string> &labels)
{
  /**
   * Trains the classifier with N data points and labels.
   * @param data - array of N observations
   *   - Each observation is a tuple with 4 values: s, d, s_dot and d_dot.
   *   - Example : [[3.5, 0.1, 5.9, -0.02],
   *                [8.0, -0.3, 3.0, 2.2],
   *                 ...
   *                ]
   * @param labels - array of N labels
   *   - Each label is one of "left", "keep", or "right".
   *
   * TODO: Implement the training function for your classifier.
   */
  float leftCount = 0;
  float rightCount = 0;
  float keepCount = 0;
  ArrayXd data_point;

  for (int i = 0; i < labels.size(); i++)
  {
    data_point = ArrayXd::Map(data[i].data(), data[i].size());
    if (labels[i] == "left") 
    {      
      leftCount +=1;
      ArrayXd delta = data_point - leftMean;
      leftMean += delta/leftCount;
      leftVar += (delta*(data_point - leftMean));
    } 
    else if (labels[i] == "right") 
    {
      rightCount +=1;
      ArrayXd delta = data_point - rightMean;
      rightMean += delta/rightCount;
      rightVar += (delta*(data_point - rightMean));
    }
    else if (labels[i] == "keep")
    {
      keepCount +=1;
      ArrayXd delta = data_point - keepMean;
      keepMean += delta/keepCount;
      keepVar += (delta*(data_point - keepMean));
    }
  }
  leftVar  = leftVar  / leftCount;
  rightVar = rightVar / rightCount;
  keepVar  = keepVar  / keepCount;
  leftPrior  = leftCount / labels.size();
  rightPrior = rightCount / labels.size();
  keepPrior  = keepPrior  / labels.size();
}

string GNB::predict(const vector<double> &sample) 
{
  /**
   * Once trained, this method is called and expected to return 
   *   a predicted behavior for the given observation.
   * @param observation - a 4 tuple with s, d, s_dot, d_dot.
   *   - Example: [3.5, 0.1, 8.5, -0.2]
   * @output A label representing the best guess of the classifier. Can
   *   be one of "left", "keep" or "right".
   *
   * TODO: Complete this function to return your classifier's prediction
   */
  double leftP = 1.0;
  double keepP = 1.0;
  double rightP = 1.0;
  for (int i = 0; i < 4; i++) 
  {
    leftP *= (1.0/(sqrt(2*M_PI*leftVar[i])))
              * exp(-pow((sample[i] -leftMean[i]), 2)/(2*leftVar[i]));
    rightP *= (1.0/(sqrt(2*M_PI*rightVar[i])))
              * exp(-pow((sample[i] -rightMean[i]), 2)/(2*rightVar[i]));
    keepP *= (1.0/(sqrt(2*M_PI*keepVar[i])))
              * exp(-pow((sample[i] -keepMean[i]), 2)/(2*keepVar[i]));
  }

  leftP  *= leftPrior;
  rightP *= rightPrior;
  keepP  *= keepPrior;

  double probs[3] = {leftP, rightP, keepP};
  
  int maxIdx = 0;
  double maxProb = probs[maxIdx];
  for (int i = 0; i < 3; i++)
  {
    if (probs[i] > maxProb)
    {
      maxProb = probs[i];
      maxIdx = i;
    }
  }
  
  return this -> possible_labels[maxIdx];
}