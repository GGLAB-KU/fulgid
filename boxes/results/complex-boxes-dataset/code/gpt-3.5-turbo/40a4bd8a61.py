# Initial state of boxes
boxes = {
    0: ['zipper', 'mirror', 'magnet', 'polish', 'vase'],
    1: ['thread'],
    2: ['camera', 'clock', 'guitar'],
    3: ['battery', 'bowl', 'thunder', 'charger', 'earring'],
    4: ['horn'],
    5: ['lock', 'necklace', 'coin'],
    6: [],
    7: ['violin', 'boot'],
    8: ['doll'],
    9: ['fridge', 'star'],
    10: ['perfume', 'starfish', 'cat', 'umbrella', 'blanket']
}

# Replace the perfume and the starfish with the coin and the earring in Box 10.
boxes[10].remove('perfume')
boxes[10].remove('starfish')
boxes[10].append('coin')
boxes[10].append('earring')

# Put the brush into Box 6.
boxes[6].append('brush')

# Remove the doll from Box 8.
boxes[8].remove('doll')

# Replace the horn with the console in Box 4.
boxes[4].remove('horn')
boxes[4].append('console')

# Put the magnet and the needle into Box 1.
boxes[1].append('magnet')
boxes[1].append('needle')

# Move the fridge and the star from Box 9 to Box 3.
boxes[9].remove('fridge')
boxes[9].remove('star')
boxes[3].append('fridge')
boxes[3].append('star')

# Swap the necklace in Box 5 with the blanket in Box 10.
boxes[5].remove('necklace')
boxes[10].remove('blanket')
boxes[5].append('blanket')
boxes[10].append('necklace')

# Move the thread and the magnet and the needle from Box 1 to Box 6.
items_to_move = ['thread', 'magnet', 'needle']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[6].append(item)

# Remove the violin from Box 7.
boxes[7].remove('violin')

# Swap the thunder in Box 3 with the console in Box 4.
boxes[3].remove('thunder')
boxes[4].remove('console')
boxes[3].append('console')
boxes[4].append('thunder')

# Put the submarine and the sculpture into Box 2.
boxes[2].append('submarine')
boxes[2].append('sculpture')

# Replace the cat and the umbrella and the earring with the plate and the battery and the thunder in Box 10.
boxes[10].remove('cat')
boxes[10].remove('umbrella')
boxes[10].remove('earring')
boxes[10].append('plate')
boxes[10].append('battery')
boxes[10].append('thunder')

# Put the puzzle and the cat and the bowl into Box 2.
boxes[2].append('puzzle')
boxes[2].append('cat')
boxes[2].append('bowl')

# Swap the bowl in Box 2 with the star in Box 3.
boxes[2].remove('bowl')
boxes[3].remove('star')
boxes[2].append('star')
boxes[3].append('bowl')

# Replace the charger and the console with the ocean and the basket in Box 3.
boxes[3].remove('charger')
boxes[3].remove('console')
boxes[3].append('ocean')
boxes[3].append('basket')

# Move the blanket from Box 5 to Box 8.
boxes[5].remove('blanket')
boxes[8].append('blanket')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")