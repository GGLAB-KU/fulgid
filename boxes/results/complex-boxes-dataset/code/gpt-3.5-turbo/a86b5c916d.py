# Initial state of boxes
boxes = {
    0: ['grass', 'basket'],
    1: [],
    2: ['earring', 'desert', 'keyboard', 'rain', 'coat'],
    3: ['button', 'coral', 'doll', 'wig'],
    4: ['freezer', 'frame', 'whistle', 'lock', 'belt'],
    5: ['watch', 'plane', 'moon', 'flower'],
    6: ['cat', 'sculpture', 'dice', 'elephant'],
    7: ['glasses', 'dog'],
    8: [],
    9: ['seaweed', 'train', 'book'],
    10: ['bag', 'submarine', 'clock'],
    11: ['truck', 'pants', 'octopus', 'flute'],
    12: [],
    13: ['boat', 'puzzle']
}

# Remove the boat and the puzzle from Box 13.
boxes[13].remove('boat')
boxes[13].remove('puzzle')

# Replace the book with the sandals in Box 9.
boxes[9].remove('book')
boxes[9].append('sandals')

# Replace the glasses with the shorts in Box 7.
boxes[7].remove('glasses')
boxes[7].append('shorts')

# Remove the shorts and the dog from Box 7.
boxes[7].remove('shorts')
boxes[7].remove('dog')

# Move the grass and the basket from Box 0 to Box 4.
items_to_move = ['grass', 'basket']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[4].append(item)

# Move the flower and the plane from Box 5 to Box 12.
items_to_move = ['flower', 'plane']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[12].append(item)

# Remove the sandals and the train from Box 9.
boxes[9].remove('sandals')
boxes[9].remove('train')

# Swap the coral in Box 3 with the submarine in Box 10.
boxes[3].remove('coral')
boxes[10].remove('submarine')
boxes[3].append('submarine')
boxes[10].append('coral')

# Put the leaf and the soap into Box 11.
boxes[11].append('leaf')
boxes[11].append('soap')

# Move the belt and the frame from Box 4 to Box 10.
items_to_move = ['belt', 'frame']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[10].append(item)

# Move the plane and the flower from Box 12 to Box 8.
items_to_move = ['plane', 'flower']
for item in items_to_move:
    boxes[12].remove(item)
    boxes[8].append(item)

# Put the horn and the wig and the island into Box 0.
items_to_put = ['horn', 'wig', 'island']
for item in items_to_put:
    boxes[0].append(item)

# Put the skirt and the pen and the bus into Box 8.
items_to_put = ['skirt', 'pen', 'bus']
for item in items_to_put:
    boxes[8].append(item)

# Remove the truck from Box 11.
boxes[11].remove('truck')

# Move the keyboard from Box 2 to Box 1.
boxes[2].remove('keyboard')
boxes[1].append('keyboard')

# Replace the wig with the usb in Box 3.
boxes[3].remove('wig')
boxes[3].append('usb')

# Replace the octopus with the shorts in Box 11.
boxes[11].remove('octopus')
boxes[11].append('shorts')

# Remove the pen and the skirt from Box 8.
boxes[8].remove('pen')
boxes[8].remove('skirt')

# Remove the usb and the button and the submarine from Box 3.
boxes[3].remove('usb')
boxes[3].remove('button')
boxes[3].remove('submarine')

# Replace the bag and the clock and the frame with the pen and the key and the shark in Box 10.
boxes[10].remove('bag')
boxes[10].remove('clock')
boxes[10].remove('frame')
boxes[10].append('pen')
boxes[10].append('key')
boxes[10].append('shark')

# Move the keyboard from Box 1 to Box 6.
boxes[1].remove('keyboard')
boxes[6].append('keyboard')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")