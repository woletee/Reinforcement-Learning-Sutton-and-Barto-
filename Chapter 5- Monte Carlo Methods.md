# Chaptr-5 (Monte Carlo Methods)

What is Monte Carlo Method 

- Monte carol method are ways of solving the reinforcement learning (RL) problem based on sampling the average returns.
- Here we will define monte carol methods only for episodic tasks to ensure well defined returns.
- That is we assume experience is divided into episodes and those episodes terminate eventually no matter what action is taken.
- Only on the completion of episodes is the policy and the value estimates changed.

What is Monte carol prediction.
- There are basically two methods for estimating the value states in MC methods.
- The first one is First-visit MC method where the value of a state is calculated on the very first visit of a state.
- This method basically does not require too much space since it doesn’t consider the revisited states.
- The next method is every-visit MC method. This method calculates the value states at every time a state is visited.
- This method basically takes too much of the space since it considers every state.
- The difference between the two states lies in the treatment of the states.
  
What is Monte carol estimation of action-values?
- If a model is not available, it is more appropriate to estimate the action-state values (or the action-state values) instead of the just the state values.
- With a model only estimating the state values is just enough.
- from the above state values are just enough for making or for estimating the state values.
- state values are enough to estimate the policy.
But without a model, one must also determine the action-state values in order to determining or making estimation the policy.

What is Monte Carol control?

- The overall idea is to proceed according to the same pattern as the dynamic programming (DP).
- Which is according to the idea of Generalized Policy Iteration (GPI)
- In GPI, one maintains both the:
1. an approximate policy 
2. an appropriate value functions.
- The value function is repeatedly altered to make closely approximate the value function for the current policy.
- Policy evaluation: is done exactly as it is described on the previous section.
- Policy improvement is done by making the policy greedy with respect to the current value functions.
- The monte Carlo control method refers to the Reinforcement learning method refers to a technique for finding the optimal policy for a decision-making process.
- This method combines the principles of Monte carol sampling with the control or optimization aspect of learning the best actions to take in each state.
- Unlike Monte Carlo prediction which is concerned with evaluating the a given policy, Monte Carlo is concerned with the improving the policy based on the feedback received from the Interactions with the environment.
- 
What are the key concepts of the Monte Carlo method 

- Policy improvement: The primary purpose of the Monte Carlo control is to update iteratively the policy until it converges to an optimal policy.
- Monte Carlo control must balance between exploration and exploitation.
- This is often achieved through methods like the e-greedy method or the e-greedy policy.
- where most of the time the best action is selected but with a small probability a random action is selected.
- Monte Carlo control does not bootstrap (It doesn’t update its estimates based on the other estimates.)
- It waits until the end of the episode and uses the actual returns for updating.
- There are basically two algorithms for Monte Carlo Control
1. Monte carlo with exploring starts (MCES): This method ensures exploring by starting episodes from every state-action pair.
2. On-policy First-visit MC control (for e-soft policy): This policy involves generating episodes were following an e-soft policy (a policy where all actions are selected with non-zero probability) and then improving the policy based on the returns.
   
What are the steps in Monte Carlo Control?
1. Initialization- start with a random policy and the initialize value functions estimates.
2. Generate episodes- Run an episode based on the current policy.
3. Update the value estimates- at the end of the episode update the value estimates.
4. Policy improvement- Improve the policy based on the updated value estimates.
5. Repeat- continue repeating the above process (generate episodes, update values, Improve policy)
- Under policy evaluation the monte carol method will compute each action-values for an arbitrary policy.
- Policy improvement is done by making the policy greedy with respect to the current value function. In this case we have action-values and so there is no need for model in order to construct the greedy policy.
- Under policy evaluation the monte carol method will compute each action-values for an arbitrary policy.
- Policy improvement is done by making the policy greedy with respect to the current value function. In this case we have action-values and so there is no need for model in order to construct the greedy policy.
