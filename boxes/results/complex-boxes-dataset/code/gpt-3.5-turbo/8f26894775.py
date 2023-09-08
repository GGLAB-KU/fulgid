# Initial state of boxes
boxes = {
    0: [],
    1: ['lamp'],
    2: ['charger', 'starfish'],
    3: [],
    4: ['fridge', 'toy', 'coral', 'forest', 'cow'],
    5: ['pot'],
    6: ['flower', 'dice', 'pillow', 'horse', 'belt'],
    7: ['cup'],
    8: ['spoon']
}

# Replace the spoon with the fish in Box 8.
boxes[8].remove('spoon')
boxes[8].append('fish')

# Empty Box 8.
boxes[8] = []

# Replace the cup with the magnet in Box 7.
boxes[7].remove('cup')
boxes[7].append('magnet')

# Put the swimsuit and the planet into Box 2.
boxes[2].append('swimsuit')
boxes[2].append('planet')

# Move the dice and the flower from Box 6 to Box 4.
items_to_move = ['dice', 'flower']
for item in items_to_move:
    boxes[6].remove(item)
    boxes[4].append(item)

# Put the oven and the earring and the truck into Box 2.
boxes[2].append('oven')
boxes[2].append('earring')
boxes[2].append('truck')

# Replace the magnet with the crown in Box 7.
boxes[7].remove('magnet')
boxes[7].append('crown')

# Put the comet and the river into Box 4.
boxes[4].append('comet')
boxes[4].append('river')

# Swap the lamp in Box 1 with the pot in Box 5.
boxes[1].remove('lamp')
boxes[5].remove('pot')
boxes[1].append('pot')
boxes[5].append('lamp')

# Replace the planet and the oven with the flute and the shirt in Box 2.
boxes[2].remove('planet')
boxes[2].remove('oven')
boxes[2].append('flute')
boxes[2].append('shirt')

# Remove the truck from Box 2.
boxes[2].remove('truck')

# Replace the horse and the belt with the ocean and the note in Box 6.
boxes[6].remove('horse')
boxes[6].remove('belt')
boxes[6].append('ocean')
boxes[6].append('note')

# Replace the lamp with the tree in Box 5.
boxes[5].remove('lamp')
boxes[5].append('tree')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")