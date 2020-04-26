# -*- coding: utf-8 -*-
"""
@Created at 2020/4/22 18:05
@Author: Kurt
@file:networks.py
@Desc:
"""
# import sys
# sys.path.append(".\\utils")
import numpy as np
import time
from utils import config, calc_cost
from envs.demand import stochastic_demand
import collections


class Backorder:
    def __init__(self, cfg):
        self.cfg = cfg
        self.number_samples = cfg.number_samples
        self.number_products = cfg.number_products
        self.lead_time = cfg.lead_time
        self.state_space = (self.number_samples,
                            self.number_products + self.number_products*self.lead_time)
        self.action_space = (self.number_samples,
                             self.number_products * 2)
        self.inventory = np.array([0] * self.number_products)
        self.outstanding = collections.deque(maxlen=self.lead_time)

    def step(self, actions):

        prices, orders = actions  # 注意：距离期末，如果当前期+提前期大于期末，此时orders应该为0
        received_inventory = self.outstanding.popleft() if self.outstanding else orders
        print("received orders:{}".format(received_inventory))

        demand = np.round(stochastic_demand(self.cfg.market_size, self.cfg.stochastic_demand_params) +
                          self.cfg.demand_elasticity.dot(prices))  # round to get integer demands

        for ind, val in enumerate(demand):
            print("Realized demand of product {} : {}".format(ind+1, val))

        next_inventory = self.inventory + received_inventory - demand
        hold_backlog_cost = calc_cost.holding_backlog_cost(next_inventory, mute=False)

        profits = demand.dot(prices) - orders.dot(self.cfg.unit_order_cost) - hold_backlog_cost

        self.inventory = next_inventory
        self.outstanding.append(orders)
        if self.outstanding:
            return np.hstack((self.inventory, np.hstack(self.outstanding))), profits, False
        else:
            return self.inventory, profits, False

    def reset(self):
        """
        initial the environment model
        :return: initial state
        """
        [self.outstanding.append([0]*self.number_products) for i in range(self.lead_time)]

        self.inventory = np.array([5]*self.number_products)

        if self.outstanding:  # existence of lead time
            initial_state = np.hstack((self.inventory, np.hstack(self.outstanding)))
            print("initial state: {}".format(initial_state))
            return initial_state
        else:  # no lead time
            print("initial state: {}".format(self.inventory))
            return self.inventory


if __name__ == "__main__":
    config = config.Config()
    env = Backorder(config)
    state = env.reset()
    i = 1
    total_profit = 0
    while True:
        print("#"*50)
        print("Period {}: state-->{}".format(i, state))
        if (i % 5) != 0:
            prices = np.array([1, 2])
            orders = np.array([1, 2])
        else:
            prices = np.array([0.5, 1])
            orders = np.array([2, 3])
        action = (prices, orders)

        print("current prices: {} ".format(prices))
        print("current orders: {} ".format(orders))
        print("current order cost: {} ".format(config.unit_order_cost.dot(orders)))

        next_state, reward, done = env.step(action)
        total_profit += reward
        print("profit-->{:g}, next_state-->{}, total_profit-->{:g}, done-->{}".format(
            reward, next_state, total_profit, done))

        state = next_state
        i += 1
        time.sleep(1)
