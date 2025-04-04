# Version 1.1.0
import sunflowers
import cactus
import pumpkins
clear()

# Constants for resource thresholds
MIN_POWER_THRESHOLD = 1000
TARGET_POWER = 10000
MIN_PUMPKIN_THRESHOLD = 1000
TARGET_PUMPKIN = 10000
MIN_CACTUS_THRESHOLD = 1000
TARGET_CACTUS = 10000

while True:
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