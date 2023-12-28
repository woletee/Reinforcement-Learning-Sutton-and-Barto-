# Chapter-3 (Finite Markov Decision Processes)

What is Finite Markov Decision Processes (MDP)

- After this I will use the abbreviation (MDP) for referring to the Markov Decision Process
- A Finite MDP is a mathematical Framework used for modeling decision making in situations where outcomes are partly random and unknown for the decision maker.

What is the Use of MDP?

- MDPS provide a structured way to make a sequence of decisions that consider both the immediate and the future sequences. This is basically useful in situations where the outcomes of decisions are uncertain.
- MDP help to find the optimal policy - strategies that will maximize the reward overtime even in situations where the reward is unknown.


What are the key components of MDP?

- States(s): are the distinct situations in which the agent can be.
- Actions(A): For each state there are various actions that an agent can agent to go into another state.
- Transition Probability (TP): This a function that gives the probability of transitioning from one state into another by taking an action in a given state.
- The above probability is basically Markvian which mean its value depends on only on the current state and action.
- Rewards(R): A reward function defines the immediate return received after transitioning into another state by taking an action.
- The goal of the agent is basically to maximize the overall reward called the cumulative reward overtime.
- Policy: This is a strategy used by the agent that determines which actions to select next.
- Policy can be : 1) deterministic (always selecting the same action) 2) selecting actions based on probability distribution.
- The objective of MDP is to find the optimal policy that will maximize the cumulative reward (overall reward received overtime).

  
How Does MDP find the Optimal Policy?

- From the above we have said that the objective of MDP is to find the optimal policy that will result in greater cumulative reward overtime but how does MDP achieve this purpose?
- The above objective involves selecting actions that will result in higher reward overtime.
- we have basically three method that will evaluate the long-term benefits of taking an action.
  
1) Value function 
- Value iteration: It is a method of computing the optimal policy by iteratively improving the value function.
- The value function estimates how good is to be in this state
- Value function: Assigns a value to each of the states which shows the cumulative reward that can be obtained starting from that state.
Process:

          1) Initialize the value of all of the states arbitrarily except for the terminal state which is 0

          2) Update the value of each of the state using Bellman Optimality equation

- The above step must be repeated until the value function converges to a stable state.
- By convergence we mean that the point where the value function stops changing significantly from the previous value.
- The policy derived from the final value function is the optimal policy.
2) Policy iteration

- There are basically two main steps in this method.
- Policy evaluation: creates the value of being in each state under current policy.
- Policy improvement: update the policy by choosing actions in each state that maximize the expected utility based on the current value functions.
- Process:

              1) starts with a random policy

              2) Evaluate the policy

              3) Improve the policy

              4) Repeat the evaluation
