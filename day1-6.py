from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

x,y,z=mc.player.getTilePos()

mc.player.setTilePos(x,y,z)
time.sleep(10)

x=x+50
mc.player.setTilePos(x,y,z)
time.sleep(10)

x=x+50
mc.player.setTilePos(x,y,z)
time.sleep(10)

x=x+50