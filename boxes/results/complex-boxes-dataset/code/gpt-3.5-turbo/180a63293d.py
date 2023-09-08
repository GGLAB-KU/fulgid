# Initial state of boxes
boxes = {
    0: ['comb', 'key', 'rock', 'shampoo', 'towel'],
    1: ['storm', 'dice', 'rocket', 'sandals'],
    2: ['bear', 'shorts', 'belt'],
    3: [],
    4: [],
    5: ['oven', 'pan', 'game', 'bicycle'],
    6: ['coat', 'branch', 'bracelet', 'blanket']
}

# Remove the storm and the rocket and the sandals from Box 1.
items_to_remove = ['storm', 'rocket', 'sandals']
for item in items_to_remove:
    boxes[1].remove(item)

# Swap the shampoo in Box 0 with the game in Box 5.
boxes[0].remove('shampoo')
boxes[5].remove('game')
boxes[0].append('game')
boxes[5].append('shampoo')

# Empty Box 6.
boxes[6] = []

# Move the belt and the shorts and the bear from Box 2 to Box 0.
items_to_move = ['belt', 'shorts', 'bear']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[0].append(item)

# Remove the towel and the shorts from Box 0.
items_to_remove = ['towel', 'shorts']
for item in items_to_remove:
    boxes[0].remove(item)

# Put the fish and the whistle into Box 2.
boxes[2].append('fish')
boxes[2].append('whistle')

# Remove the comb from Box 0.
boxes[0].remove('comb')

# Swap the whistle in Box 2 with the dice in Box 1.
boxes[2].remove('whistle')
boxes[1].remove('dice')
boxes[2].append('dice')
boxes[1].append('whistle')

# Put the rain and the bell and the mountain into Box 1.
boxes[1].append('rain')
boxes[1].append('bell')
boxes[1].append('mountain')

# Remove the fish from Box 2.
boxes[2].remove('fish')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")