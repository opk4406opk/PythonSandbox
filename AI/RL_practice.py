
# Open AI Gym을 활용한 학습 레퍼런스

# 유튜브 링크
# https://www.youtube.com/playlist?list=PLlMkM4tgfjnKsCWav-Z2F-MMFRx-2gMGG

# 깃허브 
# https://github.com/hunkim/ReinforcementZeroToAll


import gym
import random
from gym.envs.registration import register
import matplotlib.pyplot as plt

register(
    id='FrozenLake-v3',
    entry_point='gym.envs.toy_text:FrozenLakeEnv',
    kwargs={'map_name': '4x4',
            'is_slippery': False}
)

env = gym.make('FrozenLake-v0')
env.render()

num_episodes = 2000

rewardList = []
for i in range(num_episodes):
    # Reset environment and get first new observation
    env.reset()
    rewardAll = 0
    done = False

    while not done:
        # Random action
        action = random.randint(0, env.action_space.n - 1)

        # Get new state and reward from environment
        _state, reward, done, _info = env.step(action)

        # rAll will be 1 if success, o otherwise
        rewardAll += reward

    rewardList.append(rewardAll)

print("Success rate: " + str(sum(rewardList) / num_episodes))
plt.plot(rewardList)
plt.show()