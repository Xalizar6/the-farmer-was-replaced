def farm_sunflowers():
    starting_tick_count = get_tick_count()
    # Create 9 empty lists to store positions:
    # index 0 = value 7 positions
    # index 8 = value 15 positions
    value_positions = [[], [], [], [], [], [], [], [], []]
    total_sunflowers = 0

    # Water, plant, and measure sunflowers in grid location of the field
    for x in range(utils.world_size):
        for y in range(utils.world_size):
            utils.water()
            utils.plant_sunflowers()
            x, y = get_pos_x(), get_pos_y()
            value = measure()
            value_positions[value - 7].append((x, y))
            total_sunflowers += 1
            # quick_print('Position:', x, y, 'Value:', value, 'Total planted:', total_sunflowers)
            utils.travel()

    # Print summary of sunflower distribution
    for value in range(9):
        actual_value = value + 7
        count = len(value_positions[value])
        quick_print('Value', actual_value, 'count:', count, 'positions:', value_positions[value])

    # Grow and harvest in order of highest value (15->7)
    # range(8,-1,-1) gives us 8,7,6,5,4,3,2,1,0
    # which corresponds to values 15,14,13,12,11,10,9,8,7
    remaining_sunflowers = total_sunflowers
    should_stop = False
    for value in range(8, -1, -1):
        actual_value = value + 7
        # quick_print('Harvesting value', actual_value, 'sunflowers at positions:', value_positions[value])
        for x, y in value_positions[value]:
            utils.move_to_position(x, y)
            while not can_harvest():
                use_item(Items.Fertilizer)
            harvest()
            remaining_sunflowers -= 1
            # Stop harvesting if we would go below 10 sunflowers
            if remaining_sunflowers <= 9:
                quick_print('remaining_sunflowers:', remaining_sunflowers)
                quick_print('Stopping harvest to maintain minimum 10 sunflowers for yield bonus:')
                should_stop = True
                break
        if should_stop:
            break

    ending_tick_count = get_tick_count()
    quick_print('Total time taken:', ending_tick_count - starting_tick_count, 'ticks')

import utils

if __name__ == "__main__":
    clear()
    while True:
        if num_items(Items.Carrot) > 0:
            farm_sunflowers()
        else:
            quick_print('Carrot count:', num_items(Items.Carrot))
            quick_print('Not enough carrots to plant sunflowers.')