import utils
clear()
world_size = get_world_size()

while True:
    column = get_pos_x()
    for i in range(world_size):
        if column == 0:
            utils.water()
            if can_harvest():
                harvest()
            utils.travel()
        elif column == 1:
            utils.water()
            if can_harvest():
                harvest()
                if (utils.plant_trees() == False):
                    utils.plant_bushes()
            utils.travel()
        elif column == 2:
            utils.water()
            if can_harvest():
                harvest()
                if (utils.plant_trees() == False):
                    utils.plant_carrots()
            utils.travel()
        elif column == 3:
            utils.water()
            if can_harvest():
                harvest()
                utils.plant_carrots()
            utils.travel()
        elif column == 4 or column == 5:
            utils.water()
            if can_harvest():
                harvest()
                utils.plant_sunflowers()
            utils.travel()