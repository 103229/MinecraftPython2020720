# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 10:41:40 2020

@author: user
"""


from mcpi.minecraft import Minecraft
mc = Minecraft.create()

print(mc.player.getTilePos())