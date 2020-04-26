# -*- coding: utf-8 -*-
"""
@Created at 2020/4/22 19:40
@Author: Kurt
@file:normalizer.py
@Desc:
"""
import gym
from utils import config
class NormalizedActions():
    def __init__(self):
        self.cfg = config.Config()

    def _action(self, action):
        action = (action + 1) / 2  # [-1, 1] => [0, 1]
        action *= (self.cfg.action_space_high - self.cfg.action_space_low)
        action += self.cfg.action_space_low
        return action

    def _reverse_action(self, action):
        action -= self.cfg.action_space_low
        action /= (self.cfg.action_space_high - self.cfg.action_space_low)
        action = action * 2 - 1
        return action