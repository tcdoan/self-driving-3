#ifndef CLASSIFIER_H
#define CLASSIFIER_H

#include <string>
#include <vector>
#include "Dense"

using Eigen::ArrayXd;
using std::string;
using std::vector;

class GNB 
{
 public:
  ArrayXd leftMean;
  ArrayXd rightMean;
  ArrayXd keepMean;

  ArrayXd leftVar;
  ArrayXd rightVar;
  ArrayXd keepVar;

  double leftPrior;
  double rightPrior;
  double keepPrior;

  GNB();
  virtual ~GNB();

  void train(const vector<vector<double>> &data, 
             const vector<string> &labels);

  string predict(const vector<double> &sample);

  vector<string> possible_labels = {"left","keep","right"};
};

#endif  // CLASSIFIER_H