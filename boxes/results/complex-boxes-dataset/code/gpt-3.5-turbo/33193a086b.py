# Initial state of boxes
boxes = {
    0: ['zipper', 'whistle'],
    1: ['blender', 'starfish', 'boat'],
    2: ['console'],
    3: []
}

# Swap the console in Box 2 with the blender in Box 1.
boxes[1].remove('blender')
boxes[2].remove('console')
boxes[1].append('console')
boxes[2].append('blender')

# Swap the starfish in Box 1 with the blender in Box 2.
boxes[1].remove('starfish')
boxes[2].remove('blender')
boxes[1].append('blender')
boxes[2].append('starfish')

# Empty Box 2.
boxes[2] = []

# Put the laptop into Box 1.
boxes[1].append('laptop')

# Replace the whistle with the keyboard in Box 0.
boxes[0].remove('whistle')
boxes[0].append('keyboard')

# Remove the console from Box 1.
boxes[1].remove('console')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")