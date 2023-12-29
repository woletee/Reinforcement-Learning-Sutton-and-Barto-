
- ![what is Reinforcement learning](/Images/rl3.jpg "Optional title attribute")
# Chaptr-4 (Dynamic programming

- What is dynamic programming?
- The term dynamic programming refers to collecting of algorithms that can be used to compute optimal policies given the perfect model of the environment as MDP.
- Classical DP algorithms are of limited utility in RL both because of their assumption of a perfect model and their great computational expenses.
- Here we will assume that the environment for MDP is finite (S, A, R and all are finite)
- The key idea of DP and of reinforcement learning is that the environment for MDP is finite and the structure the search for good policies.
- How do you iteratively optimize a policy or a value function by solving subproblems with dynamic programming.
- For the above problem we will assume that the environment the agent is interaction with is a Markov decision process (MDP) on some probabilistic transition.
- we will assume that our agent is interacting with an environment, and it senses its state through a series of measurement at time t3, t4………tn.
- and at each time stamp I have to decide which action I have to take.
- We are trying to design an optimal policy that will give us the maximum possible rewards.
- The value function tells us that given a policy what is the expected reward of being in that state.
- I don’t know the best policy or the value function for the best policy and that is what the agent trying to learn which is the optimal policy and also the optimal value function that will tell me the how good is to be being in that state.
- For model-based RL what we have is we assume that we know how the model environment works.
- we will assume that the environment evolves according to a Markov Decision Proces (MDP)
- The probability of being in some state is being conditioned or depends on the state or the new state and this idea is called MDP.
- we also look for the expected reward. which is given some current state s and a current action a assuming that I have moved to the next state what is the probability of the expected reward.
- To solve for the optimal policy and to get the optimal value function is kind of brute force attack which is searching over all states.
