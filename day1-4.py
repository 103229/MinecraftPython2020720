# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 11:36:46 2020

@author: user
"""


from mcpi.minecraft import Minecraft
mc = Minecraft.create()

print(mc.player.getTilePos())
print(mc.player.getPos())

x=200.1234
y=100.5673
z=20.2222
mc.player.setPos(x,y,z)