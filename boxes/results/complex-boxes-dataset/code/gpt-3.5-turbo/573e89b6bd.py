# Initial state of boxes
boxes = {
    0: ['cat', 'bell', 'mixer'],
    1: ['thunder', 'brush', 'rain', 'mountain', 'harmonica'],
    2: ['shark'],
    3: ['headphone', 'card', 'shirt', 'piano'],
    4: ['forest', 'grass', 'microscope'],
    5: [],
    6: ['puzzle', 'elephant'],
    7: ['note', 'lipstick', 'tie', 'planet', 'comet'],
    8: [],
    9: ['shelf', 'ship'],
    10: ['swimsuit'],
    11: ['desert'],
    12: ['rocket', 'helmet'],
    13: [],
    14: []
}

# Put the shorts and the beach and the oven into Box 4.
items_to_put = ['shorts', 'beach', 'oven']
for item in items_to_put:
    boxes[4].append(item)

# Put the toothbrush and the phone and the game into Box 13.
items_to_put = ['toothbrush', 'phone', 'game']
for item in items_to_put:
    boxes[13].append(item)

# Remove the headphone and the card and the piano from Box 3.
items_to_remove = ['headphone', 'card', 'piano']
for item in items_to_remove:
    boxes[3].remove(item)

# Remove the comet from Box 7.
boxes[7].remove('comet')

# Put the pot into Box 3.
boxes[3].append('pot')

# Replace the shark with the thunder in Box 2.
boxes[2].remove('shark')
boxes[2].append('thunder')

# Put the sun into Box 12.
boxes[12].append('sun')

# Put the plane into Box 3.
boxes[3].append('plane')

# Put the gloves and the whistle into Box 7.
items_to_put = ['gloves', 'whistle']
for item in items_to_put:
    boxes[7].append(item)

# Remove the thunder from Box 2.
boxes[2].remove('thunder')

# Replace the desert with the camera in Box 11.
boxes[11].remove('desert')
boxes[11].append('camera')

# Move the puzzle and the elephant from Box 6 to Box 5.
items_to_move = ['puzzle', 'elephant']
for item in items_to_move:
    boxes[6].remove(item)
    boxes[5].append(item)

# Move the swimsuit from Box 10 to Box 13.
boxes[10].remove('swimsuit')
boxes[13].append('swimsuit')

# Remove the toothbrush from Box 13.
boxes[13].remove('toothbrush')

# Replace the forest and the microscope and the grass with the perfume and the wig and the harmonica in Box 4.
boxes[4].remove('forest')
boxes[4].remove('grass')
boxes[4].remove('microscope')
boxes[4].append('perfume')
boxes[4].append('wig')
boxes[4].append('harmonica')

# Replace the whistle with the helmet in Box 7.
boxes[7].remove('whistle')
boxes[7].append('helmet')

# Replace the mountain and the rain with the usb and the jungle in Box 1.
boxes[1].remove('mountain')
boxes[1].remove('rain')
boxes[1].append('usb')
boxes[1].append('jungle')

# Move the camera from Box 11 to Box 6.
boxes[11].remove('camera')
boxes[6].append('camera')

# Replace the ship and the shelf with the boat and the bear in Box 9.
boxes[9].remove('ship')
boxes[9].remove('shelf')
boxes[9].append('boat')
boxes[9].append('bear')

# Move the gloves and the note from Box 7 to Box 12.
items_to_move = ['gloves', 'note']
for item in items_to_move:
    boxes[7].remove(item)
    boxes[12].append(item)

# Move the swimsuit from Box 13 to Box 10.
boxes[13].remove('swimsuit')
boxes[10].append('swimsuit')

# Remove the swimsuit from Box 10.
boxes[10].remove('swimsuit')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")