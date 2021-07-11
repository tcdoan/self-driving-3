The observation model will be implemented by performing the following at each time step:

- Measure the range to landmarks up to 100m from the vehicle, in the driving direction (forward)
- Estimate a pseudo range from each landmark by subtracting pseudo position ($x^k_t$) from the landmark position
- Match each pseudo range estimate $z^{*k}_t$ to its closest observation measurement $z^k_t$
- For each pseudo range and observation measurement pair $(z^{*k}_t, z^k_t)$, calculate a probability by passing relevant values to norm_pdf:
  - norm_pdf(observation_measurement, pseudo_range_estimate, observation_stdev)
  - $p(z^k_t|x^k_t, m)$ ~ $N(z^k_t; z^{*k}_t, \sigma_{zt})$
- Return the product of all probabilities
  - Why do we multiply all the probabilities in the last step? 
  - Our final signal (probability) must reflect all pseudo range, observation pairs. This blends our signal. 

Given:
- pseudo position: $x^t$ = 10m
- vector of landmark positions from our map: m = [6m, 15m, 21m, 40m]
- observation measurements: $z^t$ =[5.5m, 11m]
- observation standard deviation: $\sigma$=1.0m

## Estimate Pseudo Ranges
First step is to estimate pseudo ranges:

$z^*_t$ = [6m, 15m, 21m, 40m] - $x^t$  = [5, 11, 30]

## Association
- Match each observation measurement with the nearest estimated pseudo range. 
  - We will only use each measurement and pseudo range once.
  - [(5.5,5), (11,11)]

## Determine Probabilities
- Calculate a probability for each observation measurement and pseudo range estimate pair by passing relevant data to norm_pdf
    - Enter your response as a vector of probabilities in scientific notation with an accuracy of two decimal places, and no spaces. 
    - **norm_pdf(observation_measurement, pseudo_range_estimate, observation_stdev)**
    - norm_pdf(z, mu, sigma) -> norm_pdf$(z^k_t, z^{*k}_t, \sigma_{zt})$

  ```
    float prob1 = Helpers::normpdf(5.5, 5, stdev);
    float prob2 = Helpers::normpdf(11, 11, stdev);

    std::cout << prob1 << std::endl;
    std::cout << prob2 << std::endl;

    0.352065
    0.398942
  ```

## Return the product of all probabilities
- Why do we multiply all the probabilities in the last step?
- Our final signal (probability) must reflect all pseudo range, observation pairs. This blends our signal.
- Return $0.352065*0.398942$