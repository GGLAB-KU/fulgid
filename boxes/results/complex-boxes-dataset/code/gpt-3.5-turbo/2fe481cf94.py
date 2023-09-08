# Initial state of boxes
boxes = {
    0: ['boat', 'laptop', 'earring'],
    1: ['mirror'],
    2: ['planet', 'violin', 'speaker', 'motorcycle'],
    3: ['island'],
    4: ['fish', 'harmonica', 'sandals', 'glove'],
    5: ['elephant'],
    6: ['pillow', 'pen', 'scissors', 'plane'],
    7: ['apple', 'comb', 'controller', 'rock', 'soap'],
    8: ['polish', 'watch'],
    9: ['magnet'],
    10: ['seaweed', 'pants', 'dolphin', 'dog'],
    11: ['game', 'blender', 'desert'],
    12: ['telescope', 'mountain'],
    13: ['puzzle'],
    14: []
}

# Remove the mirror from Box 1.
boxes[1].remove('mirror')

# Swap the controller in Box 7 with the island in Box 3.
boxes[7].remove('controller')
boxes[3].remove('island')
boxes[7].append('island')
boxes[3].append('controller')

# Move the boat and the earring and the laptop from Box 0 to Box 7.
items_to_move = ['boat', 'earring', 'laptop']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[7].append(item)

# Swap the earring in Box 7 with the controller in Box 3.
boxes[7].remove('earring')
boxes[3].remove('controller')
boxes[7].append('controller')
boxes[3].append('earring')

# Move the scissors from Box 6 to Box 10.
boxes[6].remove('scissors')
boxes[10].append('scissors')

# Swap the magnet in Box 9 with the harmonica in Box 4.
boxes[9].remove('magnet')
boxes[4].remove('harmonica')
boxes[9].append('harmonica')
boxes[4].append('magnet')

# Replace the scissors and the dolphin and the seaweed with the jacket and the lion and the rocket in Box 10.
boxes[10].remove('scissors')
boxes[10].remove('dolphin')
boxes[10].remove('seaweed')
boxes[10].append('jacket')
boxes[10].append('lion')
boxes[10].append('rocket')

# Remove the pillow from Box 6.
boxes[6].remove('pillow')

# Swap the puzzle in Box 13 with the comb in Box 7.
boxes[13].remove('puzzle')
boxes[7].remove('comb')
boxes[13].append('comb')
boxes[7].append('puzzle')

# Replace the pen and the plane with the forest and the usb in Box 6.
boxes[6].remove('pen')
boxes[6].remove('plane')
boxes[6].append('forest')
boxes[6].append('usb')

# Move the puzzle and the apple from Box 7 to Box 9.
boxes[7].remove('puzzle')
boxes[7].remove('apple')
boxes[9].append('puzzle')
boxes[9].append('apple')

# Swap the magnet in Box 4 with the blender in Box 11.
boxes[4].remove('magnet')
boxes[11].remove('blender')
boxes[4].append('blender')
boxes[11].append('magnet')

# Swap the elephant in Box 5 with the motorcycle in Box 2.
boxes[5].remove('elephant')
boxes[2].remove('motorcycle')
boxes[5].append('motorcycle')
boxes[2].append('elephant')

# Remove the comb from Box 13.
boxes[13].remove('comb')

# Put the cat and the spoon and the game into Box 2.
items_to_move = ['cat', 'spoon', 'game']
for item in items_to_move:
    boxes[2].append(item)

# Replace the telescope with the grass in Box 12.
boxes[12].remove('telescope')
boxes[12].append('grass')

# Move the dog and the jacket and the lion from Box 10 to Box 13.
items_to_move = ['dog', 'jacket', 'lion']
for item in items_to_move:
    boxes[10].remove(item)
    boxes[13].append(item)

# Remove the polish from Box 8.
boxes[8].remove('polish')

# Put the rock and the pan into Box 7.
items_to_move = ['rock', 'pan']
for item in items_to_move:
    boxes[7].append(item)

# Replace the lion with the blender in Box 13.
boxes[13].remove('lion')
boxes[13].append('blender')

# Move the pants from Box 10 to Box 12.
boxes[10].remove('pants')
boxes[12].append('pants')

# Remove the motorcycle from Box 5.
boxes[5].remove('motorcycle')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")