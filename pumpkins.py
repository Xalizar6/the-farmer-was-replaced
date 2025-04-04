# Version 1.0.1
# Script to plant and grow pumpkins across entire map grid

def farm_pumpkins():
    # quick_print('Reset pumpkin counter')
    grown_pumpkins = 0

    for x in range(utils.world_size):
        for y in range(utils.world_size):
            if get_ground_type() != Grounds.Soil:
                till()
            utils.water()

            # Plant and grow pumpkin, retry if it dies
            if plant_and_grow():
                grown_pumpkins += 1
                # quick_print(grown_pumpkins)

            if grown_pumpkins == total_cells:
                use_item(Items.Weird_Substance)
                harvest()
            utils.travel()

def plant_and_grow():
    # Plants a pumpkin and ensures it grows fully
    plant(Entities.Pumpkin)
    while not can_harvest():
        use_item(Items.Fertilizer)
        if get_entity_type() == None:
            plant(Entities.Pumpkin)
    return True


import utils
total_cells = utils.world_size * utils.world_size

if __name__ == "__main__":
    clear()
    while True:
        farm_pumpkins()