# Initial state of boxes
boxes = {
    0: ['toothbrush', 'flower', 'scissors'],
    1: ['console', 'key', 'tiger', 'tree'],
    2: ['grinder', 'cloud', 'thunder'],
    3: ['keyboard', 'octopus', 'soap', 'hat'],
    4: ['moon', 'pot', 'boot', 'polish'],
    5: ['bag'],
    6: [],
    7: ['car', 'oven', 'submarine', 'ring', 'jungle'],
    8: ['bell'],
    9: ['cow', 'sandals', 'toy', 'makeup', 'shelf'],
    10: ['dolphin', 'lightning', 'dress', 'planet', 'bowl'],
    11: ['headphone', 'charger']
}

# Replace the bowl with the horse in Box 10.
boxes[10].remove('bowl')
boxes[10].append('horse')

# Put the flower and the bird into Box 3.
boxes[0].remove('flower')
boxes[3].append('flower')
boxes[3].append('bird')

# Swap the bag in Box 5 with the scissors in Box 0.
boxes[0].remove('scissors')
boxes[5].remove('bag')
boxes[0].append('bag')
boxes[5].append('scissors')

# Replace the bell with the basket in Box 8.
boxes[8].remove('bell')
boxes[8].append('basket')

# Remove the pot from Box 4.
boxes[4].remove('pot')

# Swap the octopus in Box 3 with the sandals in Box 9.
boxes[3].remove('octopus')
boxes[9].remove('sandals')
boxes[3].append('sandals')
boxes[9].append('octopus')

# Remove the scissors from Box 5.
boxes[5].remove('scissors')

# Replace the submarine and the jungle with the blender and the tie in Box 7.
boxes[7].remove('submarine')
boxes[7].remove('jungle')
boxes[7].append('blender')
boxes[7].append('tie')

# Move the basket from Box 8 to Box 6.
boxes[8].remove('basket')
boxes[6].append('basket')

# Put the leaf into Box 10.
boxes[10].append('leaf')

# Put the lion and the chair into Box 9.
boxes[9].append('lion')
boxes[9].append('chair')

# Replace the moon with the necklace in Box 4.
boxes[4].remove('moon')
boxes[4].append('necklace')

# Move the flower from Box 0 to Box 3.
boxes[0].remove('flower')
boxes[3].append('flower')

# Empty Box 4.
boxes[4] = []

# Replace the tie and the car and the oven with the toy and the dice and the rocket in Box 7.
boxes[7].remove('tie')
boxes[7].remove('car')
boxes[7].remove('oven')
boxes[7].append('toy')
boxes[7].append('dice')
boxes[7].append('rocket')

# Remove the charger and the headphone from Box 11.
boxes[11].remove('charger')
boxes[11].remove('headphone')

# Replace the basket with the drum in Box 6.
boxes[6].remove('basket')
boxes[6].append('drum')

# Put the magnet and the dice and the grass into Box 1.
boxes[1].append('magnet')
boxes[1].append('dice')
boxes[1].append('grass')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")