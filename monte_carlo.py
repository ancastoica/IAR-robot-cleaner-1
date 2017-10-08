from emulator import Emulator
from policy import Policy
import random
import api

EPISODE_LENGTH = 3


class MC:
    emulator = Emulator("MC")
    tuple_plot = []
    epsilon = 0.01
    G = {}

    def run(self, limit):
        i = 0
        rand = random.uniform(0, 1)
        q = {}
        sa_counter = {}
        policy = Policy()
        policy.init_policy_MC(1000)
        index_policy = 0
        while i < limit:
            i += 1

            # Generate EPISODE_LENGTH episodes

            average_reward = 0
            s = api.randomstate()
            api.printstate(s)
            hash_s = s.hash()
            if rand > self.epsilon:
                if policy.state_exists(s):
                    a = policy.get_action_given_state(hash_s)[0]
                    r = policy.get_action_given_state(hash_s)[1]
                else:
                    a = api.ACTIONS[random.randrange(len(api.ACTIONS))]
                    r = self.emulator.simulate(s, a)[0]
            else:
                a = api.ACTIONS[random.randrange(len(api.ACTIONS))]
                r = self.emulator.simulate(s, a)[0]
            average_reward += r

            if policy.state_exists(hash_s):
                old_r = policy.get_action_given_state(hash_s)[1]
                if r > old_r:
                    policy.update_action_for_state(hash_s,a,r)
            else:
                policy.insert_state_action_reward(index_policy,hash_s,a,r)
                index_policy += 1

            if (hash_s, a) in sa_counter.keys():
                sa_counter[hash_s , a] += 1
                q[hash_s, a] = (r + sa_counter[hash_s, a] * q[hash_s, a]) / (sa_counter[hash_s, a] + 1)
            else:
                sa_counter[hash_s, a] = 1
                q[hash_s, a] = r

            for j in range(2, EPISODE_LENGTH):
                s = self.emulator.simulate(s, a)[1]
                api.printstate(s)
                hash_s = s.hash()
                if rand > self.epsilon:
                    if policy.state_exists(s):
                        a = policy.get_action_given_state(hash_s)[0]
                        r = policy.get_action_given_state(hash_s)[1]
                    else:
                        a = api.ACTIONS[random.randrange(len(api.ACTIONS))]
                        r = self.emulator.simulate(s, a)[0]
                else:
                    a = api.ACTIONS[random.randrange(len(api.ACTIONS))]
                    r = self.emulator.simulate(s, a)[0]
                if policy.state_exists(hash_s):
                    old_r = policy.get_action_given_state(hash_s)[1]
                    if r > old_r:
                        policy.update_action_for_state(hash_s, a, r)
                else:
                    policy.insert_state_action_reward(index_policy, hash_s, a, r)
                    index_policy += 1
                average_reward += r

                if (hash_s, a) in sa_counter.keys():
                    sa_counter[hash_s, a] += 1
                    q[hash_s, a] = (r + sa_counter[hash_s, a] * q[hash_s, a]) / (sa_counter[hash_s, a] + 1)
                else:
                    sa_counter[hash_s, a] = 1
                    q[hash_s, a] = r

            average_reward = average_reward / (EPISODE_LENGTH - 1)
            self.tuple_plot.append(i, average_reward)
