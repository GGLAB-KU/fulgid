# Initial state of boxes
boxes = {
    0: ['cow', 'ship', 'pot', 'fish', 'towel'],
    1: ['mirror'],
    2: [],
    3: ['bear', 'whistle'],
    4: ['fork', 'grass', 'sun', 'tie', 'bird'],
    5: ['charger', 'swimsuit', 'microwave'],
    6: ['comb', 'coat', 'boot', 'battery'],
    7: [],
    8: ['branch', 'shark', 'bag']
}

# Put the apple and the toothbrush and the shampoo into Box 8.
boxes[8].append('apple')
boxes[8].append('toothbrush')
boxes[8].append('shampoo')

# Remove the shampoo and the toothbrush and the branch from Box 8.
boxes[8].remove('shampoo')
boxes[8].remove('toothbrush')
boxes[8].remove('branch')

# Swap the grass in Box 4 with the bear in Box 3.
boxes[4].remove('grass')
boxes[3].remove('bear')
boxes[4].append('bear')
boxes[3].append('grass')

# Empty Box 3.
boxes[3] = []

# Remove the ship from Box 0.
boxes[0].remove('ship')

# Swap the fish in Box 0 with the mirror in Box 1.
boxes[0].remove('fish')
boxes[1].remove('mirror')
boxes[0].append('mirror')
boxes[1].append('fish')

# Remove the mirror from Box 0.
boxes[0].remove('mirror')

# Replace the charger and the swimsuit and the microwave with the umbrella and the violin and the coat in Box 5.
boxes[5].remove('charger')
boxes[5].remove('swimsuit')
boxes[5].remove('microwave')
boxes[5].append('umbrella')
boxes[5].append('violin')
boxes[5].append('coat')

# Replace the apple with the freezer in Box 8.
boxes[8].remove('apple')
boxes[8].append('freezer')

# Swap the fish in Box 1 with the fork in Box 4.
boxes[1].remove('fish')
boxes[4].remove('fork')
boxes[1].append('fork')
boxes[4].append('fish')

# Replace the bag with the tie in Box 8.
boxes[8].remove('bag')
boxes[8].append('tie')

# Put the coat and the tape into Box 6.
boxes[6].append('coat')
boxes[6].append('tape')

# Swap the tie in Box 4 with the coat in Box 5.
boxes[4].remove('tie')
boxes[5].remove('coat')
boxes[4].append('coat')
boxes[5].append('tie')

# Swap the boot in Box 6 with the umbrella in Box 5.
boxes[6].remove('boot')
boxes[5].remove('umbrella')
boxes[6].append('umbrella')
boxes[5].append('boot')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")