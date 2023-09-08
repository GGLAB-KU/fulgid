# Initial state of boxes
boxes = {
    0: [],
    1: ['dog'],
    2: ['thunder', 'shelf', 'horn', 'starfish'],
    3: ['bird', 'charger', 'pants', 'camera', 'chair'],
    4: ['telescope'],
    5: ['grinder', 'mask', 'toothpaste', 'lion', 'bowl']
}

# Put the zipper into Box 0.
boxes[0].append('zipper')

# Swap the bowl in Box 5 with the dog in Box 1.
boxes[1].remove('dog')
boxes[5].remove('bowl')
boxes[1].append('bowl')
boxes[5].append('dog')

# Remove the zipper from Box 0.
boxes[0].remove('zipper')

# Move the dog and the lion and the grinder from Box 5 to Box 1.
items_to_move = ['dog', 'lion', 'grinder']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[1].append(item)

# Move the shelf from Box 2 to Box 4.
boxes[2].remove('shelf')
boxes[4].append('shelf')

# Remove the telescope from Box 4.
boxes[4].remove('telescope')

# Put the drum into Box 3.
boxes[3].append('drum')

# Replace the bird and the drum with the blender and the cow in Box 3.
boxes[3].remove('bird')
boxes[3].remove('drum')
boxes[3].append('blender')
boxes[3].append('cow')

# Replace the mask and the toothpaste with the zipper and the paint in Box 5.
boxes[5].remove('mask')
boxes[5].remove('toothpaste')
boxes[5].append('zipper')
boxes[5].append('paint')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")