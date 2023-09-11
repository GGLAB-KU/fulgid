# Initial state of boxes
boxes = {
    0: ['toy', 'forest', 'coat'],
    1: ['bag', 'bicycle', 'storm', 'piano', 'cloud'],
    2: ['toothpaste', 'lamp', 'hat', 'octopus'],
    3: ['laptop', 'bell', 'pot'],
    4: ['pen', 'lion', 'brush'],
    5: ['crown', 'needle', 'watch', 'necklace'],
    6: [],
    7: ['bus', 'cup', 'branch'],
    8: ['bird', 'console', 'sock', 'fish', 'telescope'],
    9: [],
    10: ['sculpture', 'belt', 'tree', 'speaker', 'thunder'],
    11: ['truck', 'sun', 'plane'],
    12: ['train', 'book']
}

# Replace the bird and the telescope with the tree and the microscope in Box 8.
boxes[8].remove('bird')
boxes[8].remove('telescope')
boxes[8].append('tree')
boxes[8].append('microscope')

# Replace the coat and the forest and the toy with the bird and the ocean and the toothbrush in Box 0.
boxes[0].remove('coat')
boxes[0].remove('forest')
boxes[0].remove('toy')
boxes[0].append('bird')
boxes[0].append('ocean')
boxes[0].append('toothbrush')

# Remove the sculpture and the speaker and the tree from Box 10.
boxes[10].remove('sculpture')
boxes[10].remove('speaker')
boxes[10].remove('tree')

# Put the ring and the towel and the game into Box 0.
boxes[0].append('ring')
boxes[0].append('towel')
boxes[0].append('game')

# Move the pen and the lion and the brush from Box 4 to Box 7.
items_to_move = ['pen', 'lion', 'brush']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[7].append(item)

# Move the toothpaste and the hat from Box 2 to Box 8.
items_to_move = ['toothpaste', 'hat']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[8].append(item)

# Swap the book in Box 12 with the ocean in Box 0.
boxes[12].remove('book')
boxes[0].remove('ocean')
boxes[12].append('ocean')
boxes[0].append('book')

# Move the thunder and the belt from Box 10 to Box 9.
items_to_move = ['thunder', 'belt']
for item in items_to_move:
    boxes[10].remove(item)
    boxes[9].append(item)

# Move the lamp and the octopus from Box 2 to Box 7.
items_to_move = ['lamp', 'octopus']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[7].append(item)

# Move the sun and the plane from Box 11 to Box 9.
items_to_move = ['sun', 'plane']
for item in items_to_move:
    boxes[11].remove(item)
    boxes[9].append(item)

# Replace the bicycle with the camera in Box 1.
boxes[1].remove('bicycle')
boxes[1].append('camera')

# Put the flute into Box 4.
boxes[4].append('flute')

# Remove the toothpaste and the microscope from Box 8.
boxes[8].remove('toothpaste')
boxes[8].remove('microscope')

# Move the storm and the piano and the bag from Box 1 to Box 5.
items_to_move = ['storm', 'piano', 'bag']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[5].append(item)

# Remove the toothbrush and the book from Box 0.
boxes[0].remove('toothbrush')
boxes[0].remove('book')

# Move the flute from Box 4 to Box 11.
boxes[4].remove('flute')
boxes[11].append('flute')

# Move the towel from Box 0 to Box 2.
boxes[0].remove('towel')
boxes[2].append('towel')

# Move the bag and the piano and the watch from Box 5 to Box 3.
items_to_move = ['bag', 'piano', 'watch']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[3].append(item)

# Replace the pot and the bag and the piano with the seaweed and the fish and the toaster in Box 3.
boxes[3].remove('pot')
boxes[3].remove('bag')
boxes[3].remove('piano')
boxes[3].append('seaweed')
boxes[3].append('fish')
boxes[3].append('toaster')

# Remove the bus and the lion from Box 7.
boxes[7].remove('bus')
boxes[7].remove('lion')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")