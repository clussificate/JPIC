# -*- coding: utf-8 -*-
"""
@Created at 2020/4/26 16:19
@Author: Kurt
@file:calc_cost.py
@Desc:
"""
from utils import config


def holding_backlog_cost(inventory, mute=True):
    """

    :param inventory: inventory at the end of a period
    :param mute: whether print cost information
    :return: holing cost or backlog cost,
             flag == 0； holding cost
             flag == 1: backlog cost
    """
    cfg = config.Config()
    total_cost = 0
    for ind, val in enumerate(inventory):
        if val <= 0:
            cost = cfg.unit_backlog_cost[ind] * val
            total_cost += cost
            if not mute:
                print("backlog_cost of product {}: {}".format(ind+1, cost))
        else:
            cost = cfg.unit_holing_cost[ind] * val
            total_cost += cost
            if not mute:
                print("holding_cost of product {}: {}".format(ind+1, cost))
    return total_cost
