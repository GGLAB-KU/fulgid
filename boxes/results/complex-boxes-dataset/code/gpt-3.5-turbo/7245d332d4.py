# Initial state of boxes
boxes = {
    0: [],
    1: ['shelf', 'sculpture', 'violin'],
    2: ['river', 'bag'],
    3: ['tie', 'blender'],
    4: ['shoes', 'elephant', 'table', 'necklace'],
    5: ['butterfly', 'train', 'pot', 'storm', 'puzzle'],
    6: ['button'],
    7: ['glasses'],
    8: ['polish', 'skirt', 'umbrella'],
    9: ['dolphin']
}

# Swap the river in Box 2 with the elephant in Box 4.
boxes[2].remove('river')
boxes[4].remove('elephant')
boxes[2].append('elephant')
boxes[4].append('river')

# Remove the dolphin from Box 9.
boxes[9].remove('dolphin')

# Replace the puzzle and the pot with the sun and the dog in Box 5.
boxes[5].remove('puzzle')
boxes[5].remove('pot')
boxes[5].append('sun')
boxes[5].append('dog')

# Swap the button in Box 6 with the glasses in Box 7.
boxes[6].remove('button')
boxes[7].remove('glasses')
boxes[6].append('glasses')
boxes[7].append('button')

# Remove the shelf and the sculpture and the violin from Box 1.
items_to_remove = ['shelf', 'sculpture', 'violin']
for item in items_to_remove:
    boxes[1].remove(item)

# Move the table from Box 4 to Box 0.
boxes[4].remove('table')
boxes[0].append('table')

# Move the shoes and the necklace from Box 4 to Box 9.
items_to_move = ['shoes', 'necklace']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[9].append(item)

# Move the table from Box 0 to Box 8.
boxes[0].remove('table')
boxes[8].append('table')

# Swap the blender in Box 3 with the necklace in Box 9.
boxes[3].remove('blender')
boxes[9].remove('necklace')
boxes[3].append('necklace')
boxes[9].append('blender')

# Replace the elephant with the shampoo in Box 2.
boxes[2].remove('elephant')
boxes[2].append('shampoo')

# Put the camera and the keyboard into Box 5.
boxes[5].append('camera')
boxes[5].append('keyboard')

# Move the dog and the sun from Box 5 to Box 2.
items_to_move = ['dog', 'sun']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[2].append(item)

# Empty Box 3.
boxes[3] = []

# Empty Box 4.
boxes[4] = []

# Put the bird and the motorcycle into Box 0.
boxes[0].append('bird')
boxes[0].append('motorcycle')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")