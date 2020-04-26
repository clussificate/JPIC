# -*- coding: utf-8 -*-
"""
@Created at 2020/4/22 19:38
@Author: Kurt
@file:config.py
@Desc:
"""
import numpy as np


class Config():
    def __init__(self):
        self.number_samples = 1
        self.number_products = 2
        self.lead_time = 3
        self.market_size = np.array([3, 3])
        self.stochastic_demand_params = [[0, 1], [0, 2]]
        self.unit_order_cost = np.array([0.5, 1])
        self.demand_elasticity = np.array([[-0.5, 0.2],
                                           [0.4, -0.3]])
        self.unit_holing_cost = [0.01, 0.02]
        self.unit_backlog_cost = [0.04, 0.08]

        self.prices_high =[]
        self.order_high = []
        self.action_space_high = np.array(self.prices_high + self.order_high)

        self.prices_low =[]
        self.order_low = []
        self.action_space_low = np.array(self.prices_low + self.order_low)

