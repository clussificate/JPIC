# -*- coding: utf-8 -*-
"""
@Created at 2020/4/22 22:51
@Author: Kurt
@file:demand.py
@Desc:
"""
import numpy as np


def stochastic_demand(market_size, stochastic_params):
    # return: [array([-0.08251399]), array([0.88874692])]
    # -> array([-0.08251399,  0.88874692])
    stochastic_demand = [np.random.normal(params[0], params[1], 1)
                         for params in stochastic_params]
    return np.round(np.clip(market_size + np.hstack(stochastic_demand), 0, np.infty))

