# Initial state of boxes
boxes = {
    0: ['camera', 'hat', 'starfish'],
    1: ['blender', 'table', 'dice', 'pen'],
    2: ['frame', 'glove', 'comb', 'scissors'],
    3: ['helmet', 'flute'],
    4: ['tape', 'headphone', 'moon', 'tie', 'perfume'],
    5: [],
    6: ['planet'],
    7: ['cloud'],
    8: ['towel', 'dress']
}

# Move the towel and the dress from Box 8 to Box 4.
items_to_move = ['towel', 'dress']
for item in items_to_move:
    boxes[8].remove(item)
    boxes[4].append(item)

# Remove the towel from Box 4.
boxes[4].remove('towel')

# Remove the flute from Box 3.
boxes[3].remove('flute')

# Replace the helmet with the star in Box 3.
boxes[3].remove('helmet')
boxes[3].append('star')

# Remove the tie and the headphone from Box 4.
items_to_remove = ['tie', 'headphone']
for item in items_to_remove:
    boxes[4].remove(item)

# Remove the dice and the blender from Box 1.
items_to_remove = ['dice', 'blender']
for item in items_to_remove:
    boxes[1].remove(item)

# Replace the table and the pen with the pants and the cat in Box 1.
boxes[1].remove('table')
boxes[1].remove('pen')
boxes[1].append('pants')
boxes[1].append('cat')

# Swap the perfume in Box 4 with the starfish in Box 0.
boxes[4].remove('perfume')
boxes[0].remove('starfish')
boxes[4].append('starfish')
boxes[0].append('perfume')

# Remove the pants from Box 1.
boxes[1].remove('pants')

# Swap the dress in Box 4 with the cloud in Box 7.
boxes[4].remove('dress')
boxes[7].remove('cloud')
boxes[4].append('cloud')
boxes[7].append('dress')

# Move the planet from Box 6 to Box 2.
boxes[6].remove('planet')
boxes[2].append('planet')

# Remove the tape and the starfish and the cloud from Box 4.
items_to_remove = ['tape', 'starfish', 'cloud']
for item in items_to_remove:
    boxes[4].remove(item)

# Move the star from Box 3 to Box 2.
boxes[3].remove('star')
boxes[2].append('star')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")