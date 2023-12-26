# Chapter-2 (multi-armed bandit)

- The most important feature that distinguishes Reinforcement learning from other types of learning is that it uses training information that evaluates the actions taken rather than one that instructs which actions to take by giving the correct actions like in supervised learning.
- The above idea is all about the two different types of feedback which are: instructive versus evaluative feedback.
- Instructive feedback is basically independent of the action taken. It tells which actions to take on the other hand evaluative feedback is dependent on the actions, and it evaluates how good the action taken is.

What is K-armed Bandit problem?

- K-armed Bandit problem is when you are repeatedly faced with a choice of among k different options or actions and after you made each choice you will receive a numerical reward chosen from a numerical probability of distributions that depends on the actions you have selected.
- Your objective is to maximize the total expected reward over a period of time which could be over a period of 100 action selection steps.
- In the k-armed bandit problem each of the k-actions have an expected reward given that an action is selected and let's call this reward as values of that specific action. denoted as q*(a)
- we will denote the action taken at each time stamp as At and the respective action reward as Rt.
- Thus, the value for an arbitrary action can be written as follows.
- q*(a)=E [Rt |At=a], the value is the expected reward given that an action a is taken!
- If we know the value of each of the corresponding actions, then we will end up choosing action that will result in the highest value of the action (reward)


Action value methods 

- we will now look closer at methods for estimating the values of actions and using this estimate for selecting actions to take. and these methods are collectively called action-values methods.
- True value of an action is a mean reward of an action when the action is selected.
- one natural way to estimate this is by averaging the rewards actually received.
- Qt(a)=sum of rewards when a taken prior t divided by the number of times a taken prior to t
- If the denominator goes to zero, then the estimated value of the action is random variable like 0
- If the denominator goes to infinity, then the estimated value of the actions would converge to the actual values of the action which is qt(a).
- The above methos is called sample average method for estimating the action-values. it is called average since it is an average of the sample of relevant rewards.
- The simplest action-selection rule is to select the actions with the highest estimated value (which is selecting the greedy actions)
- If there are many greedy actions, then the selection can be done arbitrarily may be randomly.
- At=argmax (Qt(a))
- The argmax denotes the action for which the following expression Qt(a) is maximized.


Exercise 2.1

Answer: The total probability of selecting the greedy action can be calculated using the following formula

Total probability of selecting the greedy action=(1-e) + e/total number of actions 

Total probability of selecting the greedy action= (1-0.5) + 0.5/2

Total probability of selecting the greedy action= 0.75 (75 %)

The 10 armed Testbed

- 10-armed test bed is a concept that is basically used in Reinforcement learning. it is a hypothetical scenario used for testing the performance of different algorithms especially in the field exploring versus exploiting.
- In this problem there are basically 10 arms: you can imagine a bandit with 10 arms. each arm when pulled will result in different values of reward. The distribution of each reward is basically unknown to the leaner and the decision-maker.
- Goal: The goal of the learning algorithm is to maximize the reward. this involves figuring out the which lever yields the highest reward.
- Exploitation versus Exploration dilemma: The key challenge in 10 armed bandit problem is to try different levels to learn which one will yield the highest reward and exploitation (pulling the lever that currently seems to result in the highest reward.)


Incremental Implementation 

- The action value methods we have seen on the previous topic all estimate action-values as sample averages of observed rewards.
- let Ri be the ith reward obtained after the ith action is selected and let Qn denote the total action-values obtained after the action has been selected for n-1 times.
- Qn=R1+R2+R3+R4+R5………. +Rn-1/n-1
- The obvious method is to store all of the rewards and to perform the above computation whenever their action-values are required.
- However, if we are going to do this it will require higher computation time and space when will have a large number of rewards.
- Each additional reward will require additional space and then computation time for performing the above numerator computation.
- But the below method will avoid the above problem and will always require constant computation space and computation time.
- The computation is shown on the below given image.

- 
  Tackling a Non-stationary Problem

- The average methods we have discussed above are more appropriate for stationary bandit problems. that is for bandit problems for which the reward probability does not vary overtime. (constant reward probability)
- - But in reality reinforcement learning problems are non stationary ( which is the reward probability varies over time)
- In this sense it makes sense to give more weight for recent weights than those of long one rewards
- - 
- One of the most popular way of doing this is to use constant stpe size parameter(alpha)

- we call the above weighted average because the sum of the weights is basically 1
- from the above we can see that the weight given to reward i ,Ri depends on how many rewards ago was it observed
- Thus weight given to the ith reward decreases exponentially as the number of rewards raises.

- ![what is Reinforcement learning](/Images/reee.jpg "Optional title attribute")


optimistic initial values 

- The concept of optimistic initial values in reinforcement leaning is a strategy used to encourage the exploration particularly in the early stages of learning.
- Initial value setting : in RL algorithms each action pair is assigned an initial estimated value
- This values are used to guide agents in order to make decisions particularly in the lack of any experience.
- The principle of optimistic initial values is setting these initial values to an artificially higher values
- This optimistic reflects the idea a belief that actions are potentially rewarding until they proven otherwise.
- This principle encourages exploration by overestimating action values the agent is encouraged to try out different actions to gain more information.
- This is particularly important in environment where the agent has no any prior experience.
- This approach is particularly useful in environment where the rewards are sparse.
- It encourages the agent to explore more instead of getting stuck into local optima.
- In other words it prevent converges to suboptimal values
