# Initial state of boxes
boxes = {
    0: ['forest'],
    1: ['bird', 'helmet', 'coral', 'glove'],
    2: ['elephant', 'perfume', 'seaweed'],
    3: [],
    4: ['glasses', 'butterfly'],
    5: ['branch', 'frame', 'sock'],
    6: ['hat'],
    7: ['scissors', 'bus']
}

# Swap the scissors in Box 7 with the hat in Box 6.
boxes[6].remove('hat')
boxes[7].remove('scissors')
boxes[6].append('scissors')
boxes[7].append('hat')

# Move the bird and the helmet from Box 1 to Box 5.
items_to_move = ['bird', 'helmet']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[5].append(item)

# Put the watch and the truck and the game into Box 7.
items_to_put = ['watch', 'truck', 'game']
for item in items_to_put:
    boxes[7].append(item)

# Move the seaweed and the elephant and the perfume from Box 2 to Box 5.
items_to_move = ['seaweed', 'elephant', 'perfume']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[5].append(item)

# Remove the scissors from Box 6.
boxes[6].remove('scissors')

# Swap the branch in Box 5 with the glove in Box 1.
boxes[1].remove('glove')
boxes[5].remove('branch')
boxes[1].append('branch')
boxes[5].append('glove')

# Move the game and the hat and the truck from Box 7 to Box 0.
items_to_move = ['game', 'hat', 'truck']
for item in items_to_move:
    boxes[7].remove(item)
    boxes[0].append(item)

# Remove the watch and the bus from Box 7.
boxes[7].remove('watch')
boxes[7].remove('bus')

# Move the forest and the game and the truck from Box 0 to Box 7.
items_to_move = ['forest', 'game', 'truck']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[7].append(item)

# Swap the butterfly in Box 4 with the branch in Box 1.
boxes[1].remove('branch')
boxes[4].remove('butterfly')
boxes[1].append('butterfly')
boxes[4].append('branch')

# Move the coral and the butterfly from Box 1 to Box 6.
items_to_move = ['coral', 'butterfly']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[6].append(item)

# Move the helmet and the frame from Box 5 to Box 3.
items_to_move = ['helmet', 'frame']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[3].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")