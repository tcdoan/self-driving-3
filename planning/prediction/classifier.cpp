#include "classifier.h"
#include <math.h>
#include <string>
#include <vector>
#include <algorithm>
#include <numeric>
#include <iostream>

using std::string;
using std::vector;

// Initializes GNB
GNB::GNB(): num_labels(3), state_size(4)
{
    priors = vector<double>(num_labels);
    gaussian_vars = vector<vector<GaussianVar>>(num_labels, vector<GaussianVar>(state_size));
    for(int i = 0; i < num_labels; i++) {
        label_to_idx[possible_labels[i]] = i;
    }
}

GNB::~GNB() {}

void GNB::train(const vector<vector<double>> &data,
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
    vector<vector<vector<double>>> sorted_data(num_labels, vector<vector<double>>(state_size, vector<double>()));
    for(int i = 0; i < data.size(); i++) {
        int idx = label_to_idx[labels[i]];
        priors[idx] += 1;
        for(int j = 0; j < state_size; j++) {
            double data_pt = (j == 1) ? fmod((data[i][j]),lane_width) : data[i][j];
            sorted_data[idx][j].push_back(data_pt);
        }
    }
    for(int label = 0; label < num_labels; label++) {
        for(int state = 0; state < state_size; state++) {
            double size = priors[label];
            double mean = std::accumulate(sorted_data[label][state].begin(), sorted_data[label][state].end(), 0.0) / size;

            auto variance_func = [&mean, &size](double accumulator, const double& val) {
                return accumulator + ((val - mean)*(val - mean) / (size - 1));
            };
            double variance = std::accumulate(sorted_data[label][state].begin(), sorted_data[label][state].end(), 0.0, variance_func);
            gaussian_vars[label][state].mean = mean;
            gaussian_vars[label][state].variance = variance;
        }
        priors[label] /= data.size();
    }
}

double GNB::compute_probability(double value, int label, int state) {
    double coefficient = 1.0/(2.0*M_PI*gaussian_vars[label][state].variance);
    double exp_factor = - pow(value-gaussian_vars[label][state].mean, 2) / (2.0*gaussian_vars[label][state].variance);
    return coefficient*exp(exp_factor);
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
    int max_label = -1;
    double max_prob = 0.0;
    for(int label = 0; label < num_labels; label++) {
        double total_prob = priors[label];
        for(int state = 0; state < state_size; state++) {
            total_prob *= compute_probability(sample[state], label, state);
        }
        if(total_prob > max_prob) {
            max_label = label;
            max_prob = total_prob;
        }
    }
    return this->possible_labels[max_label];
}