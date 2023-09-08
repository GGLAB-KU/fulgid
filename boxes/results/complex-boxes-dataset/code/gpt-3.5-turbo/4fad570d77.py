# Initial state of boxes
boxes = {
    0: ['shelf'],
    1: ['speaker', 'belt', 'book'],
    2: ['horn', 'lion', 'earring'],
    3: ['bus', 'mixer', 'polish', 'glove'],
    4: [],
    5: ['paint', 'seaweed', 'charger', 'puzzle', 'fork'],
    6: [],
    7: ['vase', 'camera', 'lipstick'],
    8: ['usb', 'harmonica', 'lock'],
    9: ['shark'],
    10: [],
    11: ['lamp', 'console', 'sandals'],
    12: ['battery'],
    13: ['fridge', 'needle'],
    14: ['submarine', 'scarf', 'tree', 'thunder']
}

# Replace the sandals and the lamp and the console with the elephant and the island and the jacket in Box 11.
boxes[11].remove('sandals')
boxes[11].remove('lamp')
boxes[11].remove('console')
boxes[11].append('elephant')
boxes[11].append('island')
boxes[11].append('jacket')

# Put the mirror and the dolphin and the mask into Box 14.
boxes[14].append('mirror')
boxes[14].append('dolphin')
boxes[14].append('mask')

# Put the ring into Box 3.
boxes[3].append('ring')

# Move the needle and the fridge from Box 13 to Box 3.
boxes[13].remove('needle')
boxes[13].remove('fridge')
boxes[3].append('needle')
boxes[3].append('fridge')

# Move the dolphin and the mask and the tree from Box 14 to Box 7.
items_to_move = ['dolphin', 'mask', 'tree']
for item in items_to_move:
    boxes[14].remove(item)
    boxes[7].append(item)

# Put the cloud and the towel and the dog into Box 8.
boxes[8].append('cloud')
boxes[8].append('towel')
boxes[8].append('dog')

# Replace the lion and the horn with the helmet and the mask in Box 2.
boxes[2].remove('lion')
boxes[2].remove('horn')
boxes[2].append('helmet')
boxes[2].append('mask')

# Swap the camera in Box 7 with the shelf in Box 0.
boxes[7].remove('camera')
boxes[0].remove('shelf')
boxes[7].append('shelf')
boxes[0].append('camera')

# Replace the shark with the mixer in Box 9.
boxes[9].remove('shark')
boxes[9].append('mixer')

# Remove the mixer from Box 9.
boxes[9].remove('mixer')

# Remove the belt and the book and the speaker from Box 1.
items_to_remove = ['belt', 'book', 'speaker']
for item in items_to_remove:
    boxes[1].remove(item)

# Swap the scarf in Box 14 with the camera in Box 0.
boxes[14].remove('scarf')
boxes[0].remove('camera')
boxes[14].append('camera')
boxes[0].append('scarf')

# Remove the usb and the dog and the cloud from Box 8.
items_to_remove = ['usb', 'dog', 'cloud']
for item in items_to_remove:
    boxes[8].remove(item)

# Replace the mask and the helmet and the earring with the fridge and the bell and the grinder in Box 2.
boxes[2].remove('mask')
boxes[2].remove('helmet')
boxes[2].remove('earring')
boxes[2].append('fridge')
boxes[2].append('bell')
boxes[2].append('grinder')

# Empty Box 3.
boxes[3] = []

# Replace the scarf with the towel in Box 0.
boxes[0].remove('scarf')
boxes[0].append('towel')

# Remove the island and the elephant and the jacket from Box 11.
items_to_remove = ['island', 'elephant', 'jacket']
for item in items_to_remove:
    boxes[11].remove(item)

# Put the forest and the umbrella into Box 10.
boxes[10].append('forest')
boxes[10].append('umbrella')

# Put the sandals into Box 2.
boxes[2].append('sandals')

# Remove the tree and the dolphin and the lipstick from Box 7.
items_to_remove = ['tree', 'dolphin', 'lipstick']
for item in items_to_remove:
    boxes[7].remove(item)

# Move the vase and the mask from Box 7 to Box 1.
boxes[7].remove('vase')
boxes[7].remove('mask')
boxes[1].append('vase')
boxes[1].append('mask')

# Replace the towel with the lipstick in Box 0.
boxes[0].remove('towel')
boxes[0].append('lipstick')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")