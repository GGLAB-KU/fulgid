# Initial state of boxes
boxes = {
    0: ['shoe', 'snow', 'lamp', 'violin'],
    1: ['perfume', 'laptop', 'boat', 'scarf', 'gloves'],
    2: ['tiger'],
    3: ['tape', 'soap', 'fridge', 'thunder', 'headphone'],
    4: ['razor'],
    5: ['phone', 'note'],
    6: [],
    7: ['guitar', 'elephant'],
    8: ['harmonica', 'tree', 'glove', 'submarine', 'jungle'],
    9: ['island'],
    10: ['makeup', 'wire', 'cup'],
    11: ['starfish', 'chair', 'dice'],
    12: ['octopus', 'rock', 'spoon', 'blender', 'rain']
}

# Remove the island from Box 9.
boxes[9].remove('island')

# Move the cup and the makeup from Box 10 to Box 5.
items_to_move = ['cup', 'makeup']
for item in items_to_move:
    boxes[10].remove(item)
    boxes[5].append(item)

# Move the razor from Box 4 to Box 11.
boxes[4].remove('razor')
boxes[11].append('razor')

# Remove the soap and the thunder and the tape from Box 3.
items_to_remove = ['soap', 'thunder', 'tape']
for item in items_to_remove:
    boxes[3].remove(item)

# Remove the wire from Box 10.
boxes[10].remove('wire')

# Move the laptop and the scarf and the gloves from Box 1 to Box 8.
items_to_move = ['laptop', 'scarf', 'gloves']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[8].append(item)

# Put the star and the speaker into Box 9.
boxes[9].append('star')
boxes[9].append('speaker')

# Empty Box 11.
boxes[11] = []

# Remove the headphone and the fridge from Box 3.
boxes[3].remove('headphone')
boxes[3].remove('fridge')

# Replace the guitar with the drum in Box 7.
boxes[7].remove('guitar')
boxes[7].append('drum')

# Remove the phone from Box 5.
boxes[5].remove('phone')

# Swap the tiger in Box 2 with the blender in Box 12.
boxes[2].remove('tiger')
boxes[12].remove('blender')
boxes[2].append('blender')
boxes[12].append('tiger')

# Swap the violin in Box 0 with the speaker in Box 9.
boxes[0].remove('violin')
boxes[9].remove('speaker')
boxes[0].append('speaker')
boxes[9].append('violin')

# Empty Box 1.
boxes[1] = []

# Replace the drum with the bowl in Box 7.
boxes[7].remove('drum')
boxes[7].append('bowl')

# Replace the submarine and the harmonica with the bag and the scarf in Box 8.
boxes[8].remove('submarine')
boxes[8].remove('harmonica')
boxes[8].append('bag')
boxes[8].append('scarf')

# Swap the snow in Box 0 with the star in Box 9.
boxes[0].remove('snow')
boxes[9].remove('star')
boxes[0].append('star')
boxes[9].append('snow')

# Put the forest and the lamp into Box 10.
boxes[10].append('forest')
boxes[10].append('lamp')

# Move the forest and the lamp from Box 10 to Box 3.
items_to_move = ['forest', 'lamp']
for item in items_to_move:
    boxes[10].remove(item)
    boxes[3].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")