# Initial state of boxes
boxes = {
    0: ['glove', 'microscope'],
    1: [],
    2: ['needle', 'camera', 'zipper', 'shark'],
    3: [],
    4: ['rocket', 'forest', 'key'],
    5: ['ship'],
    6: ['bicycle', 'bus', 'bird', 'shoe'],
    7: ['toothpaste', 'pants', 'frame', 'candle'],
    8: []
}

# Move the bus and the shoe and the bird from Box 6 to Box 4.
items_to_move = ['bus', 'bird', 'shoe']
for item in items_to_move:
    boxes[6].remove(item)
    boxes[4].append(item)

# Replace the ship with the bird in Box 5.
boxes[5].remove('ship')
boxes[5].append('bird')

# Move the forest from Box 4 to Box 3.
boxes[4].remove('forest')
boxes[3].append('forest')

# Swap the candle in Box 7 with the bird in Box 5.
boxes[7].remove('candle')
boxes[5].remove('bird')
boxes[7].append('bird')
boxes[5].append('candle')

# Move the key and the rocket and the bus from Box 4 to Box 1.
items_to_move = ['key', 'rocket', 'bus']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[1].append(item)

# Put the towel into Box 4.
boxes[4].append('towel')

# Remove the bicycle from Box 6.
boxes[6].remove('bicycle')

# Put the scissors and the wire and the bell into Box 3.
items_to_move = ['scissors', 'wire', 'bell']
for item in items_to_move:
    boxes[3].append(item)

# Move the rocket from Box 1 to Box 0.
boxes[1].remove('rocket')
boxes[0].append('rocket')

# Replace the key and the bus with the bell and the keyboard in Box 1.
boxes[1].remove('key')
boxes[1].remove('bus')
boxes[1].append('bell')
boxes[1].append('keyboard')

# Move the shark and the needle and the camera from Box 2 to Box 6.
items_to_move = ['shark', 'needle', 'camera']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[6].append(item)

# Remove the towel and the shoe from Box 4.
boxes[4].remove('towel')
boxes[4].remove('shoe')

# Swap the bird in Box 7 with the bird in Box 4.
boxes[7].remove('bird')
boxes[4].remove('bird')
boxes[7].append('bird')
boxes[4].append('bird')

# Replace the bird with the crown in Box 4.
boxes[4].remove('bird')
boxes[4].append('crown')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")