import sunflowers
clear()

while True:
    if num_items(Items.Carrot) > 500:
        quick_print('Farming sunflowers...')
        sunflowers.farm_sunflowers()
    else:
        quick_print('Carrot count:', num_items(Items.Carrot))
        quick_print('Not enough carrots to farm sunflowers.')