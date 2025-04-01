# Globals
world_size = get_world_size()

# Function to ensure water level is maintained above 75%
def water():
    while get_water() <= 0.75:
        use_item(Items.Water)

# Function to navigate through the map, moving north and east
def travel():
    move(North)
    if get_pos_y() == 0:
        move(East)

# Function to plant bush entities
def plant_bushes():
    plant(Entities.Bush)

# Function to plant trees in alternating rows based on y position
def plant_trees():
    if get_pos_y() % 2 == 0:
        plant(Entities.Tree)
        return True
    else:
        return False

# Function to plant carrots, tilling soil if necessary
def plant_carrots():
    if get_ground_type() != Grounds.Soil:
        till()
    plant(Entities.Carrot)

# Function to plant sunflowers
    # tilling soil if necessary
    # harvesting if sunflower is already planted
def plant_sunflowers():
    if plant(Entities.Sunflower) == False:
        if get_ground_type() != Grounds.Soil:
            till()
        if get_entity_type() != None:
            harvest()
        plant(Entities.Sunflower)

# Function to plant cactus
    # tilling soil if necessary
def plant_cactus():
    if plant(Entities.Cactus) == False:
        if get_ground_type() != Grounds.Soil:
            till()
        plant(Entities.Cactus)

# Function to move to a specific x coordinate efficiently
def move_to_x(target_x):
    current_x = get_pos_x()
    world_size = get_world_size()

    # Calculate shortest path considering world wrap
    right_distance = (target_x - current_x) % world_size
    left_distance = (current_x - target_x) % world_size

    if right_distance <= left_distance:
        for _ in range(right_distance):
            move(East)
    else:
        for _ in range(left_distance):
            move(West)

# Function to move to a specific y coordinate efficiently
def move_to_y(target_y):
    current_y = get_pos_y()
    world_size = get_world_size()

    # Calculate shortest path considering world wrap
    up_distance = (target_y - current_y) % world_size
    down_distance = (current_y - target_y) % world_size

    if up_distance <= down_distance:
        for _ in range(up_distance):
            move(North)
    else:
        for _ in range(down_distance):
            move(South)

# Function to move to specific coordinates efficiently
def move_to_position(target_x, target_y):
    move_to_x(target_x)
    move_to_y(target_y)