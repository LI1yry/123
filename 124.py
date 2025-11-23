from mcpi.minecraft import Minecraft
import random

mc = Minecraft.create()

krator = input("Создать кратер? да/нет ")
if krator == "да":
    x, y, z = mc.player.getTilePos()
    mc.setBlocks(x+1, y+1, z+1, x-8, y-8, z-8,0 )
    mc.postToChat("Бабах!!!!")
else:
    x_rand = random.randint( -200, 200)
    y_rand = random.randint(10, 50)
    z_rand = random.randint(-200, 200)
    mc.player.setTilePos(x_rand, y_rand, z_rand)