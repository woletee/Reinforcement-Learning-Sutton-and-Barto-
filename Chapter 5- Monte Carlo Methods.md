
#Chapter-5 (Monte Carlo Methods)

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
