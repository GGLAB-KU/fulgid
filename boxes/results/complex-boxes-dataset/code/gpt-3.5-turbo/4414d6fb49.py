# Initial state of boxes
boxes = {
    0: ['razor', 'mixer', 'necklace'],
    1: ['bus', 'fork', 'wallet'],
    2: ['gloves', 'mask', 'wig', 'pen', 'swimsuit'],
    3: ['grass', 'pants'],
    4: ['storm', 'ship', 'truck', 'plane'],
    5: [],
    6: ['mirror', 'dress', 'thread', 'dolphin'],
    7: ['speaker', 'pan', 'ocean', 'coral', 'guitar'],
    8: ['leaf', 'lamp'],
    9: ['violin', 'shelf', 'rain', 'thunder'],
    10: ['book', 'makeup', 'earring', 'console'],
    11: [],
    12: ['hat', 'boat', 'motorcycle'],
    13: ['rock', 'horse']
}

# Remove the mixer and the necklace and the razor from Box 0.
items_to_remove = ['mixer', 'necklace', 'razor']
for item in items_to_remove:
    boxes[0].remove(item)

# Remove the boat and the hat from Box 12.
items_to_remove = ['boat', 'hat']
for item in items_to_remove:
    boxes[12].remove(item)

# Put the shelf and the necklace and the coral into Box 0.
items_to_add = ['shelf', 'necklace', 'coral']
for item in items_to_add:
    boxes[0].append(item)

# Swap the motorcycle in Box 12 with the horse in Box 13.
boxes[12].remove('motorcycle')
boxes[13].remove('horse')
boxes[12].append('horse')
boxes[13].append('motorcycle')

# Replace the ship with the toaster in Box 4.
boxes[4].remove('ship')
boxes[4].append('toaster')

# Remove the rock from Box 13.
boxes[13].remove('rock')

# Move the shelf and the rain from Box 9 to Box 13.
items_to_move = ['shelf', 'rain']
for item in items_to_move:
    boxes[9].remove(item)
    boxes[13].append(item)

# Remove the book from Box 10.
boxes[10].remove('book')

# Replace the motorcycle with the freezer in Box 13.
boxes[13].remove('motorcycle')
boxes[13].append('freezer')

# Remove the wig and the mask and the pen from Box 2.
items_to_remove = ['wig', 'mask', 'pen']
for item in items_to_remove:
    boxes[2].remove(item)

# Replace the coral and the shelf with the horn and the boat in Box 0.
boxes[0].remove('coral')
boxes[0].remove('shelf')
boxes[0].append('horn')
boxes[0].append('boat')

# Remove the necklace and the boat and the horn from Box 0.
items_to_remove = ['necklace', 'boat', 'horn']
for item in items_to_remove:
    boxes[0].remove(item)

# Swap the pants in Box 3 with the guitar in Box 7.
boxes[3].remove('pants')
boxes[7].remove('guitar')
boxes[3].append('guitar')
boxes[7].append('pants')

# Replace the violin and the thunder with the blender and the glasses in Box 9.
boxes[9].remove('violin')
boxes[9].remove('thunder')
boxes[9].append('blender')
boxes[9].append('glasses')

# Replace the dress with the wire in Box 6.
boxes[6].remove('dress')
boxes[6].append('wire')

# Put the jungle and the bear and the river into Box 10.
items_to_add = ['jungle', 'bear', 'river']
for item in items_to_add:
    boxes[10].append(item)

# Move the storm and the toaster and the plane from Box 4 to Box 3.
items_to_move = ['storm', 'toaster', 'plane']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[3].append(item)

# Swap the lamp in Box 8 with the truck in Box 4.
boxes[8].remove('lamp')
boxes[4].remove('truck')
boxes[8].append('truck')
boxes[4].append('lamp')

# Move the ocean and the speaker from Box 7 to Box 9.
items_to_move = ['ocean', 'speaker']
for item in items_to_move:
    boxes[7].remove(item)
    boxes[9].append(item)

# Replace the lamp with the speaker in Box 4.
boxes[4].remove('lamp')
boxes[4].append('speaker')

# Remove the swimsuit and the gloves from Box 2.
items_to_remove = ['swimsuit', 'gloves']
for item in items_to_remove:
    boxes[2].remove(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")