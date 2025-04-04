# version: 1.003
# Info for LLM
    # Like other plants, cactus can be grown on soil and harvested as usual.

    # They come in various sizes

    # If you harvest a fully-grown cactus and all neighboring cacti are in sorted order, it will also harvest all neighboring cacti recursively.

    # A cactus is considered to be in sorted order if all neighboring cacti to the North and East are fully grown and larger or equal in size
    # and all neighboring cacti to the South and West are fully grown and smaller or equal in size.

    # The harvest will only spread if all adjacent cacti are fully grown and in sorted order.
    # This means that if a square of grown cacti is sorted by size and you harvest one cactus, it will harvest the entire square.

    # You will receive cactus equal to the number of harvested cacti squared. So if you harvest n cacti simultaneously you will receive n**2 Items.Cactus.

    # The size of a cactus can be measured with measure().
    # It is always one of these numbers: 0,1,2,3,4,5,6,7,8,9.

    # You can also pass a direction into measure(direction) to measure the neighboring tile in that direction of the drone.

    # You can swap a cactus with its neighbor in any direction using the swap() command.
    # swap(direction) swaps the object under the drone with the object one tile in the direction of the drone.

    # Examples:
    # In each of these grids, all the cacti are in sorted order and the harvest will spread over the entire field:
    # 3 4 5    3 3 3    1 2 3    1 5 9
    # 2 3 4    2 2 2    1 2 3    1 3 8
    # 1 2 3    1 1 1    1 2 3    1 3 4

    # In this grid, only the lower left cactus is in sorted order, which is not enough for it to spread:
    # 1 5 3
    # 4 9 7
    # 3 3 2

# Sort a column from bottom to top using bubble sort
def sort_column_vertically(x):
    utils.move_to_position(x, 0)  # Move to bottom of column
    # Start from bottom, compare with cell above and swap if needed
    for i in range(utils.world_size - 1):
        for y in range(utils.world_size - 1):
            current = measure()
            above = measure(North)

            if current > above:
                swap(North)
            move(North)
        utils.move_to_position(x, 0)  # Reset to bottom for next pass

# Sort a row from left to right using bubble sort
def sort_horizontally(y):
    utils.move_to_position(0, y)  # Move to left edge of row
    # Start from left, compare with cell to right and swap if needed
    for i in range(utils.world_size - 1):
        for x in range(utils.world_size - 1):
            current = measure()
            right = measure(East)

            if current > right:
                swap(East)
            move(East)
        utils.move_to_position(0, y)  # Reset to left edge for next pass

# Farm cactus by planting, sorting, and harvesting
def farm_cactus():
    starting_tick_count = get_tick_count()

    # Plant and measure the whole field first
    quick_print('Planting cacti...')
    for x in range(utils.world_size):
        for y in range(utils.world_size):
            utils.water()
            utils.plant_cactus()
            utils.travel()

    # Sort each column vertically
    quick_print('Sorting columns vertically...')
    for x in range(utils.world_size):
        sort_column_vertically(x)

    # Sort each row horizontally
    quick_print('Sorting rows horizontally...')
    for y in range(utils.world_size):
        sort_horizontally(y)

    # Move to bottom-left corner and harvest
    quick_print('Harvesting from bottom-left corner...')
    utils.move_to_position(0, 0)
    harvest()

    ending_tick_count = get_tick_count()
    quick_print('Total time taken:', ending_tick_count - starting_tick_count, 'ticks')

import utils

if __name__ == "__main__":
    clear()
    while True:
        if num_items(Items.Pumpkin) > 0:
            farm_cactus()
        else:
            quick_print('Pumpkin count:', num_items(Items.Pumpkin))
            quick_print('Not enough pumpkins to plant cactus.')
