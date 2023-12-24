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
