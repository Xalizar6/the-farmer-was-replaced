import utils
clear()
world_size = get_world_size()

while True:
    grown_pumpkins = 0
    quick_print('Reset pumpkin counter')
    for x in range(world_size):
        for i in range(world_size):
            if get_ground_type() != Grounds.Soil:
                till()
            utils.water()
            if get_entity_type() == None:
                plant(Entities.Pumpkin)
            if get_entity_type() == Entities.Pumpkin and can_harvest():
                grown_pumpkins += 1
                quick_print(grown_pumpkins)
            if grown_pumpkins == 16:
                if can_harvest():
                    harvest()
            utils.travel()