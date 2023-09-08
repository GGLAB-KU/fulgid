# Initial state of boxes
boxes = {
    0: ['shoes', 'mask'],
    1: ['forest'],
    2: [],
    3: ['horn', 'harmonica', 'flower'],
    4: ['toothbrush', 'usb'],
    5: ['hat', 'phone', 'dog', 'frame'],
    6: ['lion', 'starfish'],
    7: ['headphone'],
    8: ['cup', 'cat', 'speaker', 'guitar', 'snow'],
    9: ['helmet', 'lipstick', 'shirt', 'shoe', 'coral']
}

# Move the forest from Box 1 to Box 7.
boxes[1].remove('forest')
boxes[7].append('forest')

# Swap the usb in Box 4 with the mask in Box 0.
boxes[4].remove('usb')
boxes[0].remove('mask')
boxes[4].append('mask')
boxes[0].append('usb')

# Move the mask from Box 4 to Box 1.
boxes[4].remove('mask')
boxes[1].append('mask')

# Move the shoes and the usb from Box 0 to Box 9.
items_to_move = ['shoes', 'usb']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[9].append(item)

# Put the charger and the tiger and the necklace into Box 9.
items_to_put = ['charger', 'tiger', 'necklace']
for item in items_to_put:
    boxes[9].append(item)

# Put the violin and the bell and the pants into Box 3.
items_to_put = ['violin', 'bell', 'pants']
for item in items_to_put:
    boxes[3].append(item)

# Move the flower and the bell from Box 3 to Box 7.
items_to_move = ['flower', 'bell']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[7].append(item)

# Replace the hat and the phone with the telescope and the watch in Box 5.
boxes[5].remove('hat')
boxes[5].remove('phone')
boxes[5].append('telescope')
boxes[5].append('watch')

# Move the violin and the pants from Box 3 to Box 4.
items_to_move = ['violin', 'pants']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[4].append(item)

# Move the toothbrush and the pants and the violin from Box 4 to Box 9.
items_to_move = ['toothbrush', 'pants', 'violin']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[9].append(item)

# Swap the shoes in Box 9 with the mask in Box 1.
boxes[9].remove('shoes')
boxes[1].remove('mask')
boxes[9].append('mask')
boxes[1].append('shoes')

# Move the telescope from Box 5 to Box 2.
boxes[5].remove('telescope')
boxes[2].append('telescope')

# Replace the harmonica and the horn with the coin and the shoe in Box 3.
boxes[3].remove('harmonica')
boxes[3].remove('horn')
boxes[3].append('coin')
boxes[3].append('shoe')

# Replace the frame and the dog and the watch with the shampoo and the controller and the jungle in Box 5.
boxes[5].remove('frame')
boxes[5].remove('dog')
boxes[5].remove('watch')
boxes[5].append('shampoo')
boxes[5].append('controller')
boxes[5].append('jungle')

# Replace the shampoo with the key in Box 5.
boxes[5].remove('shampoo')
boxes[5].append('key')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")