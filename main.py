# Version 1.5
import hay
import wood
import carrots
import sunflowers
import cactus
import pumpkins

# Constants for resource thresholds
MIN_HAY_THRESHOLD = 1000
TARGET_HAY = 10000
MIN_WOOD_THRESHOLD = 1000
TARGET_WOOD = 10000
MIN_CARROT_THRESHOLD = 1000
TARGET_CARROT = 10000
MIN_POWER_THRESHOLD = 1000
TARGET_POWER = 10000
MIN_PUMPKIN_THRESHOLD = 1000
TARGET_PUMPKIN = 10000
MIN_CACTUS_THRESHOLD = 1000
TARGET_CACTUS = 10000

clear()

while True:
    # Check and farm hay if needed
    current_hay = num_items(Items.Hay)
    if current_hay < MIN_HAY_THRESHOLD:
        quick_print('Hay low:', current_hay, 'farming up to:', TARGET_HAY)
        while current_hay < TARGET_HAY:
            quick_print('Farming hay...')
            hay.farm_hay()
            current_hay = num_items(Items.Hay)
    else:
        quick_print('Hay sufficient:', current_hay)

    # Check and farm wood if needed
    current_wood = num_items(Items.Wood)
    if current_wood < MIN_WOOD_THRESHOLD:
        quick_print('Wood low:', current_wood, 'farming up to:', TARGET_WOOD)
        while current_wood < TARGET_WOOD:
            quick_print('Farming wood...')
            wood.farm_wood()
            current_wood = num_items(Items.Wood)
    else:
        quick_print('Wood sufficient:', current_wood)

    # Check and farm carrots if needed
    current_carrots = num_items(Items.Carrot)
    if current_carrots < MIN_CARROT_THRESHOLD:
        quick_print('Carrots low:', current_carrots, 'farming up to:', TARGET_CARROT)
        while current_carrots < TARGET_CARROT:
            quick_print('Farming carrots...')
            carrots.farm_carrots()
            current_carrots = num_items(Items.Carrot)
    else:
        quick_print('Carrots sufficient:', current_carrots)

    current_power = num_items(Items.Power)
    # Farm power when below minimum threshold
    if current_power < MIN_POWER_THRESHOLD:
        quick_print('Power low:', current_power, 'farming up to:', TARGET_POWER)
        while current_power < TARGET_POWER:
            quick_print('Farming sunflowers for power...')
            sunflowers.farm_sunflowers()
            current_power = num_items(Items.Power)
    else:
        quick_print('Power sufficient:', current_power)

    # Check and farm pumpkins if needed
    current_pumpkins = num_items(Items.Pumpkin)
    if current_pumpkins < MIN_PUMPKIN_THRESHOLD:
        quick_print('Pumpkins low:', current_pumpkins, 'farming up to:', TARGET_PUMPKIN)
        while current_pumpkins < TARGET_PUMPKIN:
            quick_print('Farming pumpkins...')
            pumpkins.farm_pumpkins()
            current_pumpkins = num_items(Items.Pumpkin)
    else:
        quick_print('Pumpkins sufficient:', current_pumpkins)

    # Check and farm cactus if needed
    current_cactus = num_items(Items.Cactus)
    if current_cactus < MIN_CACTUS_THRESHOLD:
        quick_print('Cactus low:', current_cactus, 'farming up to:', TARGET_CACTUS)
        while current_cactus < TARGET_CACTUS:
            quick_print('Farming cactus...')
            cactus.farm_cactus()
            current_cactus = num_items(Items.Cactus)
    else:
        quick_print('Cactus sufficient:', current_cactus)