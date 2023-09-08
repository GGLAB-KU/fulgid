# Initial state of boxes
boxes = {
    0: ['coral', 'mask'],
    1: [],
    2: ['dog'],
    3: ['needle'],
    4: ['phone', 'glasses'],
    5: [],
    6: ['jungle', 'dress', 'cloud', 'desert'],
    7: ['sock'],
    8: [],
    9: ['ring', 'usb', 'moon'],
    10: ['razor'],
    11: ['motorcycle', 'storm'],
    12: ['wallet', 'whistle'],
    13: ['tie', 'plane', 'jacket', 'toaster'],
    14: ['microscope', 'sun', 'tree', 'tiger', 'coat']
}

# Put the plane and the necklace into Box 2.
boxes[2].append('plane')
boxes[2].append('necklace')

# Remove the needle from Box 3.
boxes[3].remove('needle')

# Empty Box 0.
boxes[0] = []

# Replace the necklace and the plane with the cat and the tape in Box 2.
boxes[2].remove('necklace')
boxes[2].remove('plane')
boxes[2].append('cat')
boxes[2].append('tape')

# Move the usb and the moon and the ring from Box 9 to Box 0.
items_to_move = ['usb', 'moon', 'ring']
for item in items_to_move:
    boxes[9].remove(item)
    boxes[0].append(item)

# Replace the sock with the blender in Box 7.
boxes[7].remove('sock')
boxes[7].append('blender')

# Put the button into Box 3.
boxes[3].append('button')

# Move the motorcycle and the storm from Box 11 to Box 3.
boxes[11].remove('motorcycle')
boxes[11].remove('storm')
boxes[3].append('motorcycle')
boxes[3].append('storm')

# Move the phone and the glasses from Box 4 to Box 12.
boxes[4].remove('phone')
boxes[4].remove('glasses')
boxes[12].append('phone')
boxes[12].append('glasses')

# Replace the cat with the spoon in Box 2.
boxes[2].remove('cat')
boxes[2].append('spoon')

# Put the submarine and the thread into Box 11.
boxes[11].append('submarine')
boxes[11].append('thread')

# Replace the jacket with the toothpaste in Box 13.
boxes[13].remove('jacket')
boxes[13].append('toothpaste')

# Put the blender and the telescope and the pan into Box 0.
boxes[0].append('blender')
boxes[0].append('telescope')
boxes[0].append('pan')

# Move the tree and the tiger and the sun from Box 14 to Box 8.
items_to_move = ['tree', 'tiger', 'sun']
for item in items_to_move:
    boxes[14].remove(item)
    boxes[8].append(item)

# Put the dog and the island into Box 7.
boxes[7].append('dog')
boxes[7].append('island')

# Swap the pan in Box 0 with the jungle in Box 6.
boxes[0].remove('pan')
boxes[6].remove('jungle')
boxes[0].append('jungle')
boxes[6].append('pan')

# Move the blender and the dog and the island from Box 7 to Box 5.
items_to_move = ['blender', 'dog', 'island']
for item in items_to_move:
    boxes[7].remove(item)
    boxes[5].append(item)

# Move the razor from Box 10 to Box 9.
boxes[10].remove('razor')
boxes[9].append('razor')

# Move the coat from Box 14 to Box 8.
boxes[14].remove('coat')
boxes[8].append('coat')

# Swap the blender in Box 5 with the razor in Box 9.
boxes[5].remove('blender')
boxes[9].remove('razor')
boxes[5].append('razor')
boxes[9].append('blender')

# Move the sun from Box 8 to Box 9.
boxes[8].remove('sun')
boxes[9].append('sun')

# Swap the plane in Box 13 with the microscope in Box 14.
boxes[13].remove('plane')
boxes[14].remove('microscope')
boxes[13].append('microscope')
boxes[14].append('plane')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")