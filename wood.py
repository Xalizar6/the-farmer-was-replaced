# Version: 1.0

def farm_wood():
    for x in range(utils.world_size):
        for y in range(utils.world_size):
            utils.water()
            if can_harvest():
                harvest()
                if (utils.plant_trees() == False):
                    utils.plant_bushes()
            utils.travel()

import utils

if __name__ == "__main__":
    clear()
    while True:
        farm_wood()
