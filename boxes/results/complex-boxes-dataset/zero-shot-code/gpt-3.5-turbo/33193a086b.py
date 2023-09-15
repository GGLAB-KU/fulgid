boxes = [[], [], [], []]

# Initial state
boxes[0] = ['zipper', 'whistle']
boxes[1] = ['blender', 'starfish', 'boat']
boxes[2] = ['console']
boxes[3] = []

# Swap console and blender
boxes[1].remove('blender')
boxes[2].remove('console')
boxes[1].append('console')
boxes[2].append('blender')

# Swap starfish and blender
boxes[1].remove('starfish')
boxes[2].remove('blender')
boxes[1].append('blender')
boxes[2].append('starfish')

# Empty Box 2
boxes[2] = []

# Put laptop into Box 1
boxes[1].append('laptop')

# Replace whistle with keyboard
boxes[0].remove('whistle')
boxes[0].append('keyboard')

# Remove console from Box 1
boxes[1].remove('console')

# Print the final state of the boxes
for i, box in enumerate(boxes):
    print(f"Box {i}: {box}")