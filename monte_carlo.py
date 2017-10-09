from emulator import Emulator
from policy import Policy
import random
import api

EPISODE_LENGTH = 3


class MC:
    emulator = Emulator("MC")
    epsilon = 0.1
    G = {}
    tuple_plot_x = []
    tuple_plot_y = []

    def run(self, limit):
        i = 0
        dice = random.uniform(0, 1)
        policy = Policy()
        policy.init_policy(1000)
        q = {}
        sa_counter = {}
        index_policy = 0
        while i < limit:
            i += 1

            # Generate EPISODE_LENGTH episodes

            index_episode = 1
            average_reward_episode = 0

            # First episode

            s = api.randomstate()

            # print("index_episode: ", index_episode)
            # api.printstate(s)

            hash_s = s.to_string()

            if dice > self.epsilon:
                if policy.state_exists(hash_s) != -1:
                    a = policy.get_action_given_state(hash_s)[0]
                    r = policy.get_action_given_state(hash_s)[1]
                else:
                    a = api.ACTIONS[random.randrange(len(api.ACTIONS))]
                    r = self.emulator.simulate(s, a)[0]
            else:
                a = api.ACTIONS[random.randrange(len(api.ACTIONS))]
                r = self.emulator.simulate(s, a)[0]
            average_reward_episode += r

            # Update policy

            if policy.state_exists(hash_s) != -1:
                old_r = policy.get_action_given_state(hash_s)[1]
                if r > old_r:
                    policy.update_action_for_state(hash_s, a, r)
            else:
                policy.insert_state_action(index_policy, hash_s, a, r)
                index_policy += 1

            # if (hash_s, a) in sa_counter.keys():
            #     sa_counter[hash_s, a] += 1
            #     q[hash_s, a] = (r + sa_counter[hash_s, a] * q[hash_s, a]) / (sa_counter[hash_s, a] + 1)
            # else:
            #     sa_counter[hash_s, a] = 1
            #     q[hash_s, a] = r

            # Next EPISODE_LENGTH - 1 episodes

            while index_episode < EPISODE_LENGTH:
                index_episode += 1
                s = self.emulator.simulate(s, a)[1]

                # print("index_episode: ", index_episode)
                # api.printstate(s)

                hash_s = s.to_string()
                if dice > self.epsilon:
                    if policy.state_exists(hash_s) != -1:
                        a = policy.get_action_given_state(hash_s)[0]
                        r = policy.get_action_given_state(hash_s)[1]
                    else:
                        a = api.ACTIONS[random.randrange(len(api.ACTIONS))]
                        r = self.emulator.simulate(s, a)[0]
                else:
                    a = api.ACTIONS[random.randrange(len(api.ACTIONS))]
                    r = self.emulator.simulate(s, a)[0]

                # Update policy

                if policy.state_exists(hash_s) != -1:
                    old_r = policy.get_action_given_state(hash_s)[1]
                    if r > old_r:
                        policy.update_action_for_state(hash_s, a, r)
                else:
                    policy.insert_state_action(index_policy, hash_s, a, r)
                    index_policy += 1

                average_reward_episode += r

                # if (hash_s, a) in sa_counter.keys():
                #     sa_counter[hash_s, a] += 1
                #     q[hash_s, a] = (r + sa_counter[hash_s, a] * q[hash_s, a]) / (sa_counter[hash_s, a] + 1)
                # else:
                #     sa_counter[hash_s, a] = 1
                #     q[hash_s, a] = r

            average_reward_episode = average_reward_episode / (EPISODE_LENGTH - 1)

            self.tuple_plot_x.append(i)
            self.tuple_plot_y.append(average_reward_episode)
