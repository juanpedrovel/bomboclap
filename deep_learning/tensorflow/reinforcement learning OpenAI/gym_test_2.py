import gym

env = gym.make("CartPole-v1")

observation = env.reset()

for t in range(1000):

    env.render()

    cart_pos, cart_vel, pole_angle, angle_vel = observation

    if pole_angle > 0:
        action = 1
    else:
        action = 0

    observation, reward, done, info = env.step(action)


