# Version: 1.0

def farm_carrots():
    for x in range(utils.world_size):
        for y in range(utils.world_size):
            utils.water()
            if can_harvest():
                harvest()
            utils.plant_carrots()
            utils.travel()

import utils

if __name__ == "__main__":
    clear()
    while True:
        farm_carrots()
