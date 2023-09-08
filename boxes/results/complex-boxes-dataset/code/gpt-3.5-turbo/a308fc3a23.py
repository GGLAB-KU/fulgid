# Initial state of boxes
boxes = {
    0: ['puzzle', 'cup', 'train'],
    1: ['fish', 'submarine'],
    2: ['spoon', 'coin', 'boat'],
    3: ['forest', 'bird', 'cat', 'star'],
    4: ['pan', 'bear', 'tree'],
    5: ['tie', 'shorts', 'scissors', 'mountain', 'microwave'],
    6: ['skirt', 'elephant', 'umbrella', 'button', 'cow'],
    7: ['wire', 'polish', 'oven', 'game', 'thread'],
    8: [],
    9: ['grinder', 'swimsuit', 'plane', 'drum'],
    10: ['plate', 'usb', 'dress', 'comb'],
    11: [],
    12: ['note', 'phone', 'basket']
}

# Move the button and the cow and the skirt from Box 6 to Box 3.
items_to_move = ['button', 'cow', 'skirt']
for item in items_to_move:
    boxes[6].remove(item)
    boxes[3].append(item)

# Remove the swimsuit and the drum and the grinder from Box 9.
items_to_remove = ['swimsuit', 'drum', 'grinder']
for item in items_to_remove:
    boxes[9].remove(item)

# Swap the thread in Box 7 with the plane in Box 9.
boxes[7].remove('thread')
boxes[9].remove('plane')
boxes[7].append('plane')
boxes[9].append('thread')

# Swap the thread in Box 9 with the pan in Box 4.
boxes[9].remove('thread')
boxes[4].remove('pan')
boxes[9].append('pan')
boxes[4].append('thread')

# Empty Box 1.
boxes[1] = []

# Swap the plate in Box 10 with the pan in Box 9.
boxes[10].remove('plate')
boxes[9].remove('pan')
boxes[10].append('pan')
boxes[9].append('plate')

# Swap the elephant in Box 6 with the pan in Box 10.
boxes[6].remove('elephant')
boxes[10].remove('pan')
boxes[6].append('pan')
boxes[10].append('elephant')

# Swap the puzzle in Box 0 with the plane in Box 7.
boxes[0].remove('puzzle')
boxes[7].remove('plane')
boxes[0].append('plane')
boxes[7].append('puzzle')

# Remove the note from Box 12.
boxes[12].remove('note')

# Move the comb from Box 10 to Box 7.
boxes[10].remove('comb')
boxes[7].append('comb')

# Put the swimsuit into Box 10.
boxes[10].append('swimsuit')

# Move the elephant and the usb from Box 10 to Box 12.
boxes[10].remove('elephant')
boxes[10].remove('usb')
boxes[12].append('elephant')
boxes[12].append('usb')

# Put the rocket into Box 3.
boxes[3].append('rocket')

# Remove the mountain and the tie and the shorts from Box 5.
items_to_remove = ['mountain', 'tie', 'shorts']
for item in items_to_remove:
    boxes[5].remove(item)

# Replace the plate with the storm in Box 9.
boxes[9].remove('plate')
boxes[9].append('storm')

# Swap the bear in Box 4 with the scissors in Box 5.
boxes[4].remove('bear')
boxes[5].remove('scissors')
boxes[4].append('scissors')
boxes[5].append('bear')

# Put the thunder into Box 1.
boxes[1].append('thunder')

# Move the thunder from Box 1 to Box 5.
boxes[1].remove('thunder')
boxes[5].append('thunder')

# Remove the microwave from Box 5.
boxes[5].remove('microwave')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")