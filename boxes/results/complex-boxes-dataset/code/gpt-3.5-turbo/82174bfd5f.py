# Initial state of boxes
boxes = {
    0: ['meteor', 'headphone', 'puzzle', 'cat'],
    1: ['scissors', 'glasses', 'telescope', 'blender'],
    2: ['bracelet', 'boot', 'dice', 'swimsuit', 'scarf'],
    3: ['makeup', 'bag', 'basket'],
    4: ['frame', 'piano', 'sculpture'],
    5: ['shark', 'zipper', 'towel', 'drum'],
    6: ['paint', 'usb', 'ship'],
    7: [],
    8: [],
    9: [],
    10: ['polish']
}

# Swap the polish in Box 10 with the glasses in Box 1.
boxes[10], boxes[1] = boxes[1], boxes[10]

# Remove the scissors and the polish from Box 1.
boxes[1].remove('scissors')
boxes[1].remove('polish')

# Swap the blender in Box 1 with the sculpture in Box 4.
boxes[1], boxes[4] = boxes[4], boxes[1]

# Move the cat and the puzzle from Box 0 to Box 3.
items_to_move = ['cat', 'puzzle']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[3].append(item)

# Move the blender from Box 4 to Box 6.
boxes[4].remove('blender')
boxes[6].append('blender')

# Replace the headphone and the meteor with the toothbrush and the table in Box 0.
boxes[0].remove('headphone')
boxes[0].remove('meteor')
boxes[0].append('toothbrush')
boxes[0].append('table')

# Remove the sculpture and the telescope from Box 1.
boxes[1].remove('sculpture')
boxes[1].remove('telescope')

# Swap the zipper in Box 5 with the scarf in Box 2.
boxes[5], boxes[2] = boxes[2], boxes[5]

# Move the frame from Box 4 to Box 10.
boxes[4].remove('frame')
boxes[10].append('frame')

# Remove the shark and the drum and the scarf from Box 5.
items_to_remove = ['shark', 'drum', 'scarf']
for item in items_to_remove:
    boxes[5].remove(item)

# Move the glasses and the frame from Box 10 to Box 8.
items_to_move = ['glasses', 'frame']
for item in items_to_move:
    boxes[10].remove(item)
    boxes[8].append(item)

# Move the blender and the paint from Box 6 to Box 5.
items_to_move = ['blender', 'paint']
for item in items_to_move:
    boxes[6].remove(item)
    boxes[5].append(item)

# Replace the usb and the ship with the pan and the octopus in Box 6.
boxes[6].remove('usb')
boxes[6].remove('ship')
boxes[6].append('pan')
boxes[6].append('octopus')

# Replace the blender and the paint with the horn and the grinder in Box 5.
boxes[5].remove('blender')
boxes[5].remove('paint')
boxes[5].append('horn')
boxes[5].append('grinder')

# Remove the piano from Box 4.
boxes[4].remove('piano')

# Replace the frame and the glasses with the note and the polish in Box 8.
boxes[8].remove('frame')
boxes[8].remove('glasses')
boxes[8].append('note')
boxes[8].append('polish')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")