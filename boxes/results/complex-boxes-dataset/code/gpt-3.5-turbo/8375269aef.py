# Initial state of boxes
boxes = {
    0: ['telescope', 'coral'],
    1: ['polish', 'octopus', 'flute'],
    2: ['drum', 'gloves'],
    3: ['car', 'starfish', 'coin', 'basket'],
    4: []
}

# Put the towel into Box 4.
boxes[4].append('towel')

# Put the shorts and the grass and the battery into Box 2.
items_to_add = ['shorts', 'grass', 'battery']
for item in items_to_add:
    boxes[2].append(item)

# Put the book and the river into Box 1.
items_to_add = ['book', 'river']
for item in items_to_add:
    boxes[1].append(item)

# Replace the coral with the car in Box 0.
boxes[0].remove('coral')
boxes[0].append('car')

# Move the book and the flute from Box 1 to Box 2.
items_to_move = ['book', 'flute']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[2].append(item)

# Put the blender into Box 0.
boxes[0].append('blender')

# Empty Box 1.
boxes[1] = []

# Replace the shorts with the brush in Box 2.
boxes[2].remove('shorts')
boxes[2].append('brush')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")