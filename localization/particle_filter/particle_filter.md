# Particle Filter

### Particle Filter Algorithm Flowchart
![Particle Filter Algorithm Flowchart](filter_flow_chart.png)

### Psuedo Code
To implement a particle filter for localizing an autonomous vehicle. The pseudo code steps correspond to the steps in the algorithm flow chart, initialization, prediction, particle weight updates, and resampling.
- Python implementation of these steps was covered in robot.py

### Initialization
At the initialization step we estimate our position from GPS input. 
- The subsequent steps in the process will refine this estimate to localize our vehicle.

### Prediction
During the prediction step we add the control input (yaw rate & velocity) for all particles

![Particle Filter Prediction Step](filter_prediction.png)

### Update
During the update step, we update our particle weights using map landmark positions and feature measurements.

![Particle Filter Update Step](filter_update.png)

### Resampling
During resampling we will resample M times (M is range of 0 to length_of_particleArray) drawing a particle i (i is the particle index) proportional to its weight.

Sebastian covered one implementation of this in his [discussion and implementation of a resampling wheel](https://youtu.be/wNQVo6uOgYA).

![Particle Filter Resampling Step](filter_resampling.png)

### Return New Particle Set
The new set of particles represents the Bayes filter posterior probability. 
- We now have a refined estimate of the vehicles position based on input evidence.
  