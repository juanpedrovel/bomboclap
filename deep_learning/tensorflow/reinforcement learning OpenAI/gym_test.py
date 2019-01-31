import gym

env = gym.make("CartPole-v1")

print("Initial Observation")
observation = env.reset()
print(observation)

for _ in range(100):

    #env.render()
    action = env.action_space.sample()
    observation, reward, done, info = env.step(action)

    print("Performed One Random Action")
    print("\n")
    print("Observation")
    print(observation)
    print("\n")
    print("Reward")
    print(reward)
    print("\n")
    print("Done")
    print(done)
    print("\n")
    print("Info")
    print(info)
    print("\n")
