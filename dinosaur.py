# Version 1.10
# Info for LLM
    # The hat can be equipped with change_hat(Hats.Dinosaur_Hat)
    # If you equip the dinosaur hat and have enough pumpkins, an apple will automatically be purchased and placed under the drone.
    # When the drone is over an apple and moves again, it will eat the apple and grow its tail by one. If you can afford it,
    # a new apple will be purchased and placed in a random location.
    # The apple cannot spawn if something else is planted where it wants to be.

    # The tail of the dinosaur will be dragged behind the drone filling the previous tiles the drone moved over. If a drone tries
    #  to move on top of the tail move() will fail and return False.
    # The last segment of the tail will move out of the way during the move, so you can move onto it. However, if the snake fills
    # out the whole farm, you will not be able to move anymore. So you can check if the snake is fully grown by checking if you can't move anymore.

    # Using measure() on an apple will return the position of the next apple as a tuple.

    # next_x, next_y = measure()

    # When the hat is unequipped again by equipping a different hat, the tail will be harvested.
    # You will receive bones equal to the tail length squared. So for a tail of length n you will receive n**2 Items.Bone.
    # For Example:
    # length 1 => 1 bone
    # length 2 => 4 bones
    # length 3 => 9 bones
    # length 4 => 16 bones
    # length 16 => 256 bones
    # length 100 => 10000 bones

    # The Dinosaur Hat is very heavy, so if you equip it, it will make move() take 800 ticks instead of 200. However,
    # each time you pick up an apple, the number of ticks used by move() is reduced by 3% (rounded down), because a longer tail can help you move.

    # The following loop prints the number of ticks used by move() after any number of apples:

    # ticks = 800
    # for i in range(100):
    #     print("ticks after ", i, " apples: ", ticks)
    #     ticks -= ticks * 0.03 // 1

    # You cannot use the world wrap functionality while wearing the dinosaur hat.

def prepare_field():
    # Clear the entire field by tilling all soil
    for x in range(utils.world_size):
        for y in range(utils.world_size):
            if get_entity_type() != None:
                harvest()
            if get_ground_type() != Grounds.Soil:
                till()
            utils.travel()

def farm_bones():
    starting_tick_count = get_tick_count()

    # Start at bottom left and equip hat
    utils.move_to_position(0, 0)
    change_hat(Hats.Dinosaur_Hat)

    # Keep moving in pattern until we can't move anymore
    can_move = True
    while can_move:
        # Move up to top (y=5)
        while can_move and get_pos_y() < utils.world_size - 1:
            can_move = move(North)

        # Move right one step if not at edge
        if can_move and get_pos_x() < utils.world_size - 1:
            can_move = move(East)

        # Move down to y=1 (not 0)
        while can_move and get_pos_y() > 1:
            can_move = move(South)

        # Move right one step if not at edge
        if can_move and get_pos_x() < utils.world_size - 1:
            can_move = move(East)

        # If we reached right edge at y=0, move back to start
        if get_pos_x() == utils.world_size - 1 and get_pos_y() == 1:
            while can_move and get_pos_y() > 0:
                can_move = move(South)
            while can_move and get_pos_x() > 0:
                can_move = move(West)

    change_hat(Hats.Dinosaur_Hat)
    ending_tick_count = get_tick_count()
    quick_print('Total time taken:', ending_tick_count - starting_tick_count, 'ticks')

import utils

if __name__ == "__main__":
    clear()
    # Prepare field once at startup
    prepare_field()

    while True:
        if num_items(Items.Pumpkin) > 2:
            farm_bones()
        else:
            quick_print('Pumpkin count:', num_items(Items.Pumpkin))
            quick_print('Not enough pumpkins to spawn apples.')
