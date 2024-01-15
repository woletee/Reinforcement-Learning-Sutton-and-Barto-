
# Chapter-8(Planning and learning with tabular methods)

What do we mean by tabular methods, planning and learning?

- Tabular methods are a particular type of RL approach that uses tables or arrays to store and update values associated with states and actions in a discrete and finite space.
- Planning in the context of RL refers to the process of selecting actions to maximize a cumulative expected rewards while considering the current states and knowledge that the agent has about the environment.
  - Tabular methods for planning and involves creating arrays or tables and then updating the Q values. one of the algorithms used for learning is dynamic programming.
- Learning in the context of RL involves acquiring about the environment and improving the agent's decision-making ability through time.
- One of the algorithms used for learning are SARSA and Q-learning.

Models and Planning

Model based: when we say that an agent has model of the environment, we mean that anything that an agent can use to predict how the environment will respond to its action or to the action the agent has took.
- In model based , given a state and an action a model produces a prediction of the resultant next sate and next reward.
- If the model is stochastic there is different probability of states and actions we call this distribution models.
Prioritized Sweeping 

- prioritized sweeping is a strategy for efficiently updating the values of the states in a reinforcement learning algorithm.
- particularly in methods that use dynamic programming like Q-learning.
- In a standard reinforcement learning setting an agent learns by updating the estimated value of actions based on the observed rewards and the estimated values of the subsequent states.
- which is like updating the values of the actions based on the observed rewards and the estimated values of the subsequent states.
- These values are backpropagated to the previous states and the actions and this process is known as the backpropagation.
- However, the standard approach is basically inefficient because it typically updates values in a fixed order without considering their significance.
Prioritized sweeping improves this process by prioritizing updates for those states that have the most significance difference between their estimated value which is called the temporal difference.
The intuition behind this prioritizing sweeping is to update those states that will change the policy the most.
