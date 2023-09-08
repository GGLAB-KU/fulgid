# Initial state of boxes
boxes = {
    0: ['game', 'needle', 'charger'],
    1: ['bag', 'ship', 'oven', 'flower'],
    2: ['plane', 'octopus', 'toaster', 'tape', 'forest'],
    3: ['wig'],
    4: [],
    5: ['pot', 'piano', 'table'],
    6: ['speaker', 'doll'],
    7: []
}

# Empty Box 5
boxes[5] = []

# Swap the needle in Box 0 with the oven in Box 1.
boxes[0].remove('needle')
boxes[1].remove('oven')
boxes[0].append('oven')
boxes[1].append('needle')

# Empty Box 0
boxes[0] = []

# Put the apple and the bear and the boat into Box 2.
items_to_put = ['apple', 'bear', 'boat']
for item in items_to_put:
    boxes[2].append(item)

# Replace the forest and the apple and the boat with the flower and the clock and the blender in Box 2.
boxes[2].remove('forest')
boxes[2].remove('apple')
boxes[2].remove('boat')
boxes[2].append('flower')
boxes[2].append('clock')
boxes[2].append('blender')

# Put the dress and the desert and the tie into Box 7.
items_to_put = ['dress', 'desert', 'tie']
for item in items_to_put:
    boxes[7].append(item)

# Move the clock and the tape from Box 2 to Box 3.
items_to_move = ['clock', 'tape']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[3].append(item)

# Put the fridge and the cloud into Box 0.
items_to_put = ['fridge', 'cloud']
for item in items_to_put:
    boxes[0].append(item)

# Put the swimsuit and the rocket and the ship into Box 7.
items_to_put = ['swimsuit', 'rocket', 'ship']
for item in items_to_put:
    boxes[7].append(item)

# Empty Box 2
boxes[2] = []

# Swap the needle in Box 1 with the desert in Box 7.
boxes[1].remove('needle')
boxes[7].remove('desert')
boxes[1].append('desert')
boxes[7].append('needle')

# Remove the speaker and the doll from Box 6.
boxes[6] = []

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")