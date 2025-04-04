# Version: 1.4

def farm_hay():
    # Harvest if grown, then plant new hay across the field
    for x in range(utils.world_size):
        for y in range(utils.world_size):
            if can_harvest():
                harvest()
            # skip water, it grows fast enough without it
            # skip planting, it grows back by itself and the clear() resets it to grass
            utils.travel()

import utils

if __name__ == "__main__":
    clear()
    while True:
        farm_hay()
