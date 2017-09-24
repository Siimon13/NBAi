# NBAi
## Hui Wah Chiang, Simon Chen, Kevin Foo, Ashley Lee

### Mission Statement: Adding the (A)“i” to NBA
Overview: A machine learning program that is able to detect when “exciting” platform will take place using TensorFlow
Prompt: Make a model for predicting exciting runs
What is a run?
Defined by an 8 point differential by one team over a short period of time. 

### Machine Learning
	Plays are predicted by a linear model with Tensorflow
	Weights are used to determine excitement by these types:
 shot, shot clock time (Fast breaks) , hype_factor(Twitter API), and comeback_potential (score differential)
For example a dunk, pop up, alley oop, etc. are exciting. 
A long run is boring …
### Technology:
Python and TensorFlow. Twitter api

### Data used:
	We parsed through the Play by Play csv and created a new CSV file. When a team rached a minimum of 10 points, we began keeping track of point differentials. A point differential of at least +8 meant that the home team would have the value ‘run’ whereas a point differential of -8 meant that the away team would have the ‘run’ value. We also plan on using the Twitter api in order to determine a ‘hype’ factor in terms of online sentiment.


