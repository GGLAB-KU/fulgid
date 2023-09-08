# Initial state of boxes
boxes = {
    0: ['earring'],
    1: ['polish', 'tie', 'fridge', 'car', 'starfish'],
    2: ['table'],
    3: ['telescope', 'drum', 'spoon', 'planet'],
    4: ['forest', 'storm', 'helmet', 'guitar', 'cup']
}

# Remove the starfish and the fridge and the polish from Box 1.
items_to_remove = ['starfish', 'fridge', 'polish']
for item in items_to_remove:
    boxes[1].remove(item)

# Move the table from Box 2 to Box 1.
boxes[2].remove('table')
boxes[1].append('table')

# Remove the storm from Box 4.
boxes[4].remove('storm')

# Put the bowl into Box 3.
boxes[3].append('bowl')

# Swap the earring in Box 0 with the spoon in Box 3.
boxes[0].remove('earring')
boxes[3].remove('spoon')
boxes[0].append('spoon')
boxes[3].append('earring')

# Remove the spoon from Box 0.
boxes[0].remove('spoon')

# Remove the car and the tie and the table from Box 1.
items_to_remove = ['car', 'tie', 'table']
for item in items_to_remove:
    boxes[1].remove(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")