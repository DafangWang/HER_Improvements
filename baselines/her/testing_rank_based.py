#!/usr/bin/python
# -*- encoding=utf-8 -*-
# author: Ian
# e-mail: stmayue@gmail.com
# description: 

from baselines.her.rank_based_new import Experience


def test():
    conf = {'size': 1000000,
            'learn_start': 1400,
            # 'partition_size':10,
            'partition_num': 1000,
            'total_step': 10000,
            'batch_size': 256}
    experience = Experience(conf)

    # insert to experience
    print('test insert experience')
    for i in range(1, 1500):
        # tuple, like(state_t, a, r, state_t_1, t)
        to_insert = (i, 1, 1, i, 1)
        experience.store(to_insert)
    # print(experience.priority_queue)
    # print(experience._experience[1])
    # print(experience._experience[2])
    print('test replace')
    to_insert = (51, 1, 1, 51, 1)
    experience.store(to_insert)
    # print(experience.priority_queue)
    # print(experience._experience[1])
    # print(experience._experience[2])

    # sample
    print('test sample')
    sample, w, e_id = experience.sample(51)
    # print(sample)
    # print(w)
    # print(e_id)

    # update delta to priority
    print('test update delta')
    delta = [v for v in range(1, len(e_id)+1)]
    experience.update_priority(e_id, delta)
    # print(experience.priority_queue)
    sample, w, e_id = experience.sample(51)
    # print(sample)
    # print(w)
    # print(e_id)

    # rebalance
    print('test rebalance')
    experience.rebalance()
    # print(experience.priority_queue)


def main():
    test()


if __name__ == '__main__':
    main()

