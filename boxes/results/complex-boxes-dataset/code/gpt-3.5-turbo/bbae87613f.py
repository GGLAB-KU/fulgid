# Initial state of boxes
boxes = {
    0: ['comet', 'dress', 'planet'],
    1: ['button', 'ocean', 'shampoo'],
    2: ['puzzle', 'bell'],
    3: [],
    4: ['doll', 'wire'],
    5: ['necklace'],
    6: ['helmet', 'rocket', 'harmonica', 'fish'],
    7: ['tiger', 'car'],
    8: [],
    9: [],
    10: ['makeup', 'piano']
}

# Empty Box 4.
boxes[4] = []

# Swap the ocean in Box 1 with the puzzle in Box 2.
boxes[1].remove('ocean')
boxes[2].remove('puzzle')
boxes[1].append('puzzle')
boxes[2].append('ocean')

# Swap the necklace in Box 5 with the shampoo in Box 1.
boxes[5].remove('necklace')
boxes[1].remove('shampoo')
boxes[5].append('shampoo')
boxes[1].append('necklace')

# Move the bell from Box 2 to Box 8.
boxes[2].remove('bell')
boxes[8].append('bell')

# Put the paint and the river into Box 6.
boxes[6].append('paint')
boxes[6].append('river')

# Move the bell from Box 8 to Box 1.
boxes[8].remove('bell')
boxes[1].append('bell')

# Replace the ocean with the dice in Box 2.
boxes[2].remove('ocean')
boxes[2].append('dice')

# Put the perfume and the ship and the island into Box 5.
boxes[5].append('perfume')
boxes[5].append('ship')
boxes[5].append('island')

# Remove the tiger from Box 7.
boxes[7].remove('tiger')

# Put the scissors and the ring into Box 8.
boxes[8].append('scissors')
boxes[8].append('ring')

# Put the toothpaste and the toaster into Box 5.
boxes[5].append('toothpaste')
boxes[5].append('toaster')

# Put the scarf and the polish and the submarine into Box 3.
boxes[3].append('scarf')
boxes[3].append('polish')
boxes[3].append('submarine')

# Remove the toaster and the ship and the island from Box 5.
boxes[5].remove('toaster')
boxes[5].remove('ship')
boxes[5].remove('island')

# Put the leaf and the glasses into Box 6.
boxes[6].append('leaf')
boxes[6].append('glasses')

# Replace the ring with the keyboard in Box 8.
boxes[8].remove('ring')
boxes[8].append('keyboard')

# Put the cow and the shirt into Box 3.
boxes[3].append('cow')
boxes[3].append('shirt')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")