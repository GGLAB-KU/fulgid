# Initial state of boxes
boxes = {
    0: ['toy', 'river', 'tape'],
    1: [],
    2: ['planet', 'toaster', 'hat', 'umbrella', 'cat'],
    3: ['elephant', 'drum', 'game', 'sock'],
    4: ['earring', 'cup'],
    5: ['desert', 'scarf'],
    6: ['submarine', 'microscope', 'freezer', 'sculpture'],
    7: ['fork', 'seaweed', 'soap', 'dice'],
    8: ['mountain', 'bird', 'lion', 'controller']
}

# Replace the game and the elephant with the zipper and the coat in Box 3.
boxes[3].remove('game')
boxes[3].remove('elephant')
boxes[3].append('zipper')
boxes[3].append('coat')

# Swap the planet in Box 2 with the dice in Box 7.
boxes[2].remove('planet')
boxes[7].remove('dice')
boxes[2].append('dice')
boxes[7].append('planet')

# Remove the controller and the mountain and the lion from Box 8.
items_to_remove = ['controller', 'mountain', 'lion']
for item in items_to_remove:
    boxes[8].remove(item)

# Replace the toaster and the cat with the phone and the blender in Box 2.
boxes[2].remove('toaster')
boxes[2].remove('cat')
boxes[2].append('phone')
boxes[2].append('blender')

# Move the planet and the seaweed from Box 7 to Box 4.
items_to_move = ['planet', 'seaweed']
for item in items_to_move:
    boxes[7].remove(item)
    boxes[4].append(item)

# Put the toothpaste and the mask into Box 5.
items_to_put = ['toothpaste', 'mask']
for item in items_to_put:
    boxes[5].append(item)

# Put the boot into Box 2.
boxes[2].append('boot')

# Replace the earring and the planet and the cup with the desert and the toothpaste and the polish in Box 4.
boxes[4].remove('earring')
boxes[4].remove('cup')
boxes[4].append('desert')
boxes[4].append('toothpaste')
boxes[4].append('polish')

# Remove the blender from Box 2.
boxes[2].remove('blender')

# Replace the bird with the polish in Box 8.
boxes[8].remove('bird')
boxes[8].append('polish')

# Replace the polish with the bell in Box 8.
boxes[8].remove('polish')
boxes[8].append('bell')

# Empty Box 7.
boxes[7] = []

# Swap the submarine in Box 6 with the toy in Box 0.
boxes[6].remove('submarine')
boxes[0].remove('toy')
boxes[6].append('toy')
boxes[0].append('submarine')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")