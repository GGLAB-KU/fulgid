# Initial state of boxes
boxes = {
    0: [],
    1: ['harmonica', 'mountain', 'brush', 'fridge', 'shirt'],
    2: ['telescope', 'desert'],
    3: ['chair', 'zipper'],
    4: ['car', 'mask', 'bell'],
    5: ['ring', 'thread', 'bird', 'lock', 'submarine']
}

# Replace the car with the microwave in Box 4.
boxes[4].remove('car')
boxes[4].append('microwave')

# Replace the telescope and the desert with the microwave and the cup in Box 2.
boxes[2].remove('telescope')
boxes[2].remove('desert')
boxes[2].append('microwave')
boxes[2].append('cup')

# Remove the zipper from Box 3.
boxes[3].remove('zipper')

# Swap the lock in Box 5 with the chair in Box 3.
boxes[5].remove('lock')
boxes[3].remove('chair')
boxes[5].append('chair')
boxes[3].append('lock')

# Put the shoe into Box 5.
boxes[5].append('shoe')

# Remove the microwave and the cup from Box 2.
boxes[2].remove('microwave')
boxes[2].remove('cup')

# Move the brush and the shirt from Box 1 to Box 3.
items_to_move = ['brush', 'shirt']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[3].append(item)

# Put the table into Box 4.
boxes[4].append('table')

# Move the mountain and the fridge and the harmonica from Box 1 to Box 4.
items_to_move = ['mountain', 'fridge', 'harmonica']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[4].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")