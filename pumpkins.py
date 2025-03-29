import utils
clear()
world_size = get_world_size()
total_cells = world_size * world_size

def plant_and_grow():
    # Plants a pumpkin and ensures it grows fully
    plant(Entities.Pumpkin)
    while not can_harvest():
        use_item(Items.Fertilizer)
        if get_entity_type() == None:
            plant(Entities.Pumpkin)
    return True

while True:
    quick_print('Reset pumpkin counter')
    grown_pumpkins = 0

    for x in range(world_size):
        for i in range(world_size):
            if get_ground_type() != Grounds.Soil:
                till()
            utils.water()

            # Plant and grow pumpkin, retry if it dies
            if plant_and_grow():
                grown_pumpkins += 1
                quick_print(grown_pumpkins)

            if grown_pumpkins == total_cells:
                use_item(Items.Weird_Substance)
                harvest()
            utils.travel()