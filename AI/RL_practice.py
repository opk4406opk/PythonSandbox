
# Open AI Gym을 활용한 학습 레퍼런스

# 유튜브 링크
# https://www.youtube.com/playlist?list=PLlMkM4tgfjnKsCWav-Z2F-MMFRx-2gMGG

# 깃허브 
# https://github.com/hunkim/ReinforcementZeroToAll


import gym

env = gym.make('FrozenLake-v0')

for episodeIndex in range(1):
    observation = env.reset()

    while True :
        env.render()
        print(observation)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break
env.close()