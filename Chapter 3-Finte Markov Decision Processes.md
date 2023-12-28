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
