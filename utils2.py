# Function to ensure water level is maintained above 75%
def water():
    while get_water() <= 0.75:
        # quick_print('Watering: ', get_water())
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

# Function to plant sunflowers, tilling soil if necessary
def plant_sunflowers():
    if get_ground_type() != Grounds.Soil:
        till()
    plant(Entities.Sunflower)