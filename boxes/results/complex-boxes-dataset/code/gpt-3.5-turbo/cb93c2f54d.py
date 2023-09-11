# Initial state of boxes
boxes = {
    0: ['mask', 'star', 'toothbrush', 'shark'],
    1: ['fridge'],
    2: ['shoe', 'river'],
    3: ['polish', 'lion', 'elephant'],
    4: ['starfish', 'chair', 'gloves', 'comb']
}

# Swap the shoe in Box 2 with the fridge in Box 1.
boxes[1].remove('fridge')
boxes[2].remove('shoe')
boxes[1].append('shoe')
boxes[2].append('fridge')

# Remove the comb and the gloves from Box 4.
boxes[4].remove('comb')
boxes[4].remove('gloves')

# Replace the chair with the forest in Box 4.
boxes[4].remove('chair')
boxes[4].append('forest')

# Put the fish and the note into Box 2.
boxes[2].append('fish')
boxes[2].append('note')

# Replace the forest and the starfish with the seaweed and the wallet in Box 4.
boxes[4].remove('forest')
boxes[4].remove('starfish')
boxes[4].append('seaweed')
boxes[4].append('wallet')

# Remove the shoe from Box 1.
boxes[1].remove('shoe')

# Replace the seaweed with the lion in Box 4.
boxes[4].remove('seaweed')
boxes[4].append('lion')

# Put the keyboard and the sandals and the freezer into Box 4.
boxes[4].append('keyboard')
boxes[4].append('sandals')
boxes[4].append('freezer')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")