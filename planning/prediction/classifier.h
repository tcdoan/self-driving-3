#ifndef CLASSIFIER_H
#define CLASSIFIER_H

#include <string>
#include <vector>
#include <unordered_map>

using std::string;
using std::vector;

class GNB
{
public:
    /**
   * Constructor
   */
    GNB();

    /**
   * Destructor
   */
    virtual ~GNB();

    /**
   * Train classifier
   */
    void train(const vector<vector<double>> &data,
               const vector<string> &labels);

    /**
   * Predict with trained classifier
   */
    string predict(const vector<double> &sample);

    vector<string> possible_labels = {"left", "keep", "right"};
private:

    int num_labels;
    int state_size;
    double lane_width = 4.0;

    struct GaussianVar {
        double mean = 0.0;
        double variance = 0.0;
    };

    vector<double> priors;
    vector<vector<GaussianVar>> gaussian_vars;
    std::unordered_map<string, int> label_to_idx;

    double compute_probability(double value, int label, int state);
};

#endif // CLASSIFIER_H