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
