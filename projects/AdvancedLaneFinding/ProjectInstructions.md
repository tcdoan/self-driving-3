#  Project Instructions


### The Goal of this Project

Goal is to write a software pipeline to identify the lane boundaries in a video from a front-facing camera on a car. The camera calibration images, test road images, and project videos are available in the project repository or in the repository folder included with the workspace.

### The Writeup
The writeup will be the primary output you submit (along with your code of course).

Within the project repository, there is a writeup template that you can use as a starting point for your project writeup.

A great writeup should include the rubric points as well as your description of how you addressed each point. You should include a detailed description of the code used in each step (with line-number references and code snippets where appropriate) and links to other supporting documents or external references. You should also include images in your writeup to illustrate how your code works.

### The Code

Code should stand on its own as readable material. Explain in code comments, as well as in your writeup, how your code works and why you wrote it that way.

Make it easy for a reviewer to understand your code.

You are more than welcome to use code from the lesson. But if you copy something explain how it works and why you used it.


### Advanced Lane Finding project workspace
This workspace is designed to be a simple, easy to use environment in which you can code and run the Advanced Lane Finding project. The project instructions can be found in the final concept of this project. The project repo and is already included so steps for downloading the repo can be bypassed.

Note that while this workspace is set up as a Jupyter workspace to help you visualize your pipeline (click *New->Notebook: Python 3*), you can also choose to use Python files by clicking *New->Other: Text File* and saving it as a `.py` file.

For tips on workspace use, please review the Workspaces lesson earlier in the course.

### Accessing and using the workspace:
- Go to the workspace node and the project repo will open
- Complete the project using the instructions in the final concept of this project, keeping in mind that the repo is already in the workspace.


### Common issues
The classroom workspace does not support OpenCV's `cv2.imshow()` method - please use matplotlib - pyplot's `imshow()` method instead!

### Commit to GitHub

Students are highly encouraged to commit their project to a GitHub repo. To do this, you must change the upstream of the current repository and add your credentials. We have supplied a bash script to help you do this. Please open up a terminal, navigate to the project repository, and enter: `./set_git.sh`, then follow the prompts. This will set the upstream remote to your own repository and add your email and username to the git configuration. At this time we are not configuring passwords, so you will need to enter your username and password for each push. Since credentials are not persistent, it will be necessary to run this script each time you open, refresh, or reset the workspace.

### What It Takes to Pass

Read the ['project rubric'](https://review.udacity.com/#!/rubrics/1966/view) for details on the requirements for a passing submission.

Your writeup should include each rubric point and your description of how you addressed that point in your submission. The repository folder in the workspace provides an example template (write_up_template.md), for your write up. This template can also be found on GitHub ['example template'](https://github.com/udacity/CarND-Advanced-Lane-Lines/blob/master/writeup_template.md).

To help the reviewer evaluate your project, please save example images from each stage of your pipeline to the `output_images` folder and provide in your writeup a description of each image. Please also save your output video and include it with your submission.

### Evaluation
Once you have completed your project, double check the Project Rubric to make sure you have addressed all the rubric points. Your project will be evaluated by a Udacity reviewer according to that same rubric.

Your project must "meet specifications" in each category in order for your submission to pass. If you are happy with your submission, then you are ready to submit! If you see room for improvement in any category in which you do not meet specifications, keep working!


### Submission
Project submission if you run the project in your local machine:
Include a zipped file with your:

1. writeup
2. code (or a Jupyter notebook)
3. example output images
4. output video

Alternatively, you may submit a link to your GitHub repo for the project.

In either case, **remember to include example images for each stage of your pipeline and your final output video in your submission**.

### Project submission when using workspaces:
Click on the **Submit Project** button and follow the instructions!

##### Things to keep in mind:
- If you leave your workspace unattended, it will time out and need to be refreshed. Your most recent work will be restored, but the list of open files or any running shell sessions will not be restored.

### Project Support

If you are stuck or having difficulties with the project, don't lose hope! Remember to talk to your mentors and fellow students in your Study Group, as well as ask (and answer!) questions on ['Knowledge'](https://knowledge.udacity.com)  tagged with the project name. We also have a previously recorded project Q&A that you can watch ['here'](https://www.youtube.com/watch?v=vWY8YUayf9Q)!



