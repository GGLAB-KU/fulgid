# Initial state of boxes
boxes = {
    0: ['ocean', 'clock', 'pen', 'umbrella'],
    1: ['fish', 'game', 'rain', 'beach'],
    2: ['sun', 'bowl'],
    3: ['fridge', 'lamp', 'mixer', 'glove'],
    4: ['bell', 'headphone', 'whistle', 'microwave', 'pan'],
    5: ['watch', 'dolphin', 'usb'],
    6: ['needle', 'paint', 'mask'],
    7: ['basket', 'bird', 'speaker', 'blender', 'book'],
    8: ['wig', 'toothbrush', 'coat', 'plate', 'polish'],
    9: [],
    10: [],
    11: ['leaf', 'magnet', 'key'],
    12: ['harmonica', 'grass', 'makeup'],
    13: ['table', 'moon', 'brush', 'starfish'],
    14: []
}

# Remove the bird and the speaker from Box 7.
boxes[7].remove('bird')
boxes[7].remove('speaker')

# Move the leaf and the key and the magnet from Box 11 to Box 8.
items_to_move = ['leaf', 'key', 'magnet']
for item in items_to_move:
    boxes[11].remove(item)
    boxes[8].append(item)

# Move the paint and the needle and the mask from Box 6 to Box 12.
items_to_move = ['paint', 'needle', 'mask']
for item in items_to_move:
    boxes[6].remove(item)
    boxes[12].append(item)

# Swap the watch in Box 5 with the blender in Box 7.
boxes[5].remove('watch')
boxes[7].remove('blender')
boxes[5].append('blender')
boxes[7].append('watch')

# Replace the pan and the microwave and the whistle with the bell and the toy and the paint in Box 4.
boxes[4].remove('pan')
boxes[4].remove('microwave')
boxes[4].remove('whistle')
boxes[4].append('bell')
boxes[4].append('toy')
boxes[4].append('paint')

# Swap the usb in Box 5 with the mixer in Box 3.
boxes[5].remove('usb')
boxes[3].remove('mixer')
boxes[5].append('mixer')
boxes[3].append('usb')

# Replace the headphone and the bell and the toy with the bicycle and the charger and the table in Box 4.
boxes[4].remove('headphone')
boxes[4].remove('bell')
boxes[4].remove('toy')
boxes[4].append('bicycle')
boxes[4].append('charger')
boxes[4].append('table')

# Move the umbrella and the ocean from Box 0 to Box 6.
items_to_move = ['umbrella', 'ocean']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[6].append(item)

# Swap the fridge in Box 3 with the table in Box 13.
boxes[3].remove('fridge')
boxes[13].remove('table')
boxes[3].append('table')
boxes[13].append('fridge')

# Put the swimsuit and the shelf and the pot into Box 8.
items_to_put = ['swimsuit', 'shelf', 'pot']
for item in items_to_put:
    boxes[8].append(item)

# Remove the book and the watch and the basket from Box 7.
items_to_remove = ['book', 'watch', 'basket']
for item in items_to_remove:
    boxes[7].remove(item)

# Put the motorcycle into Box 4.
boxes[4].append('motorcycle')

# Replace the bell and the charger and the bicycle with the apple and the fish and the cloud in Box 4.
boxes[4].remove('bell')
boxes[4].remove('charger')
boxes[4].remove('bicycle')
boxes[4].append('apple')
boxes[4].append('fish')
boxes[4].append('cloud')

# Remove the sun and the bowl from Box 2.
boxes[2].remove('sun')
boxes[2].remove('bowl')

# Remove the blender from Box 5.
boxes[5].remove('blender')

# Put the mixer into Box 1.
boxes[1].append('mixer')

# Put the fridge into Box 13.
boxes[13].append('fridge')

# Swap the apple in Box 4 with the rain in Box 1.
boxes[4].remove('apple')
boxes[1].remove('rain')
boxes[4].append('rain')
boxes[1].append('apple')

# Remove the brush and the moon and the starfish from Box 13.
items_to_remove = ['brush', 'moon', 'starfish']
for item in items_to_remove:
    boxes[13].remove(item)

# Move the needle from Box 12 to Box 11.
boxes[12].remove('needle')
boxes[11].append('needle')

# Remove the ocean from Box 6.
boxes[6].remove('ocean')

# Remove the dolphin from Box 5.
boxes[5].remove('dolphin')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")