# Chapter one-1 Introduction

what is reinforcement learning?

Reinforcement learning can be considered as one of machine learning method along with the other two methods, supervised and unsupervised learning. 

The image shown below can be used to easily explain what reinforcement learning is. the figure shows that an agent takes action into the environment and then the action is interpreted as reward and state and then given back to the agent so that it can correct its action that it has taken into the environment based on the given reward.

![what is Reinforcement learning](/Images/RL.PNG "Optional title attribute")

Thus, the goal of reinforcement learning is to learn a strategy that maximizes the reward or reduce penalty over a given period of time. 

As conclusion, Reinforcement learning is a type of machine learning in which the agent learns to make decisions by taking actions into the environment and then updating the actions it has token based on the reward and the penalty it has received from the environment. 

but reinforcement learning is different from supervised and unsupervised learning methods for the following reasons:

- Reinforcement learning is not like unsupervised learning in that its goal is to maximize the reward signal instead of trying to find the hidden structure.
- Reinforcement learning is not like supervised learning in that there is not any labeled description of the correct action the system or the agent should take which exists in supervised learning.

 what are the real-world examples in which Reinforcement learning is used?

- A master chess player - in this situation the chess player can be considered as an agent, the chess board and the pieces can be considered as environments, and the feedback the user receives as eighter winning the game or losing the game can be considered as reward and penalty. so, overtime when the agent has played many games through success and failures the agent updates or improves its decision-making strategy in a way that will make the agent win in different or changing or dynamic environment.
- Below there is description of how the chess player can be considered as reinforcement learning example using the framework provided on the beginning of this page.

![Chess Player](/Images/rll1.jpg "Optional title attribute")

- An adaptive controller
- Below is an image that shows how adaptive controller can be considered as Reinforcement learning example using the farmwork of RL.

![Adaptive contolller](/Images/rll2.jpg "Optional title attribute")

- someone preparing breakfast.
- Below there is an image that shows how preparing a breakfast can be considered as reinforcement learning

![Preparing Breakfast](/Images/rll3.jpg "Optional title attribute")

- A gazelle calf

 What are Elements of Reinforcement learning 

![Elements of RL](/Images/rl2.jpg "Optional title attribute")

Exploration versus Exploitation 

- Exploration:  from its name we can see that exploration is all about discovering knowledge. for example, it can be going out to new restaurant to try new dishes and you do not know whether or not you will like the dish.
- Exploitation: is all about the existing knowledge. for example, it can be going out the same restaurant that you know before and eat the same dish that you liked before and you are sure that you will like the dish, but you didn’t try any new dish.
- Too much exploration means missing out the most known rewards and too much exploitation means missing out better strategies that will result in higher rewards than the known ones. thus, we have to find the balance between these two things for successful learning in RL.

What are the limitations of Reinforcement learning? 

- sample efficiency: Rl algorithms require a large amount of data to learn the best policy.
- credit assignment problem: if the reward from the environment is delayed then it would be difficult for the agent to determine which actions has led to the best outcome.
- Balancing between exploration and exploitation
