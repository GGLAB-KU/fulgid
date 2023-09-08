# Initial state of boxes
boxes = {
    0: ['fish', 'glove', 'boot', 'watch', 'shoes'],
    1: ['sock', 'leaf'],
    2: ['horn'],
    3: ['truck', 'motorcycle', 'pen', 'fridge', 'drum'],
    4: [],
    5: ['microwave', 'coin'],
    6: ['cup', 'makeup', 'lion', 'freezer', 'pants'],
    7: ['fork'],
    8: [],
    9: []
}

# Move the glove from Box 0 to Box 3.
boxes[0].remove('glove')
boxes[3].append('glove')

# Remove the truck from Box 3.
boxes[3].remove('truck')

# Swap the boot in Box 0 with the microwave in Box 5.
boxes[0].remove('boot')
boxes[5].remove('microwave')
boxes[0].append('microwave')
boxes[5].append('boot')

# Replace the shoes with the scissors in Box 0.
boxes[0].remove('shoes')
boxes[0].append('scissors')

# Swap the coin in Box 5 with the sock in Box 1.
boxes[5].remove('coin')
boxes[1].remove('sock')
boxes[5].append('sock')
boxes[1].append('coin')

# Replace the fork with the sandals in Box 7.
boxes[7].remove('fork')
boxes[7].append('sandals')

# Replace the scissors and the fish with the comet and the star in Box 0.
boxes[0].remove('scissors')
boxes[0].remove('fish')
boxes[0].append('comet')
boxes[0].append('star')

# Replace the star and the microwave and the comet with the starfish and the shoes and the wallet in Box 0.
boxes[0].remove('star')
boxes[0].remove('microwave')
boxes[0].remove('comet')
boxes[0].append('starfish')
boxes[0].append('shoes')
boxes[0].append('wallet')

# Move the lion from Box 6 to Box 3.
boxes[6].remove('lion')
boxes[3].append('lion')

# Move the coin and the leaf from Box 1 to Box 2.
boxes[1].remove('coin')
boxes[1].remove('leaf')
boxes[2].append('coin')
boxes[2].append('leaf')

# Remove the cup and the makeup from Box 6.
boxes[6].remove('cup')
boxes[6].remove('makeup')

# Put the drum into Box 8.
boxes[3].remove('drum')
boxes[8].append('drum')

# Move the horn and the leaf and the coin from Box 2 to Box 7.
boxes[2].remove('horn')
boxes[2].remove('leaf')
boxes[2].remove('coin')
boxes[7].append('horn')
boxes[7].append('leaf')
boxes[7].append('coin')

# Put the blender and the river and the pot into Box 9.
boxes[9].extend(['blender', 'river', 'pot'])

# Remove the pants from Box 6.
boxes[6].remove('pants')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")