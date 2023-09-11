# Initial state of boxes
boxes = {
    0: ['pillow', 'note', 'bell', 'coat'],
    1: ['earring', 'elephant', 'clock'],
    2: ['crown', 'fridge', 'freezer'],
    3: [],
    4: ['rocket', 'car'],
    5: ['perfume', 'train', 'dice', 'pants', 'pen'],
    6: ['jungle', 'console', 'zipper'],
    7: ['flute', 'lipstick'],
    8: ['shoe']
}

# Move the earring and the clock from Box 1 to Box 8.
boxes[1].remove('earring')
boxes[1].remove('clock')
boxes[8].append('earring')
boxes[8].append('clock')

# Move the clock from Box 8 to Box 7.
boxes[8].remove('clock')
boxes[7].append('clock')

# Replace the rocket and the car with the shoes and the sculpture in Box 4.
boxes[4].remove('rocket')
boxes[4].remove('car')
boxes[4].append('shoes')
boxes[4].append('sculpture')

# Move the note and the pillow and the bell from Box 0 to Box 5.
items_to_move = ['note', 'pillow', 'bell']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[5].append(item)

# Replace the elephant with the whistle in Box 1.
boxes[1].remove('elephant')
boxes[1].append('whistle')

# Remove the coat from Box 0.
boxes[0].remove('coat')

# Put the paint and the magnet and the grass into Box 3.
items_to_move = ['paint', 'magnet', 'grass']
for item in items_to_move:
    boxes[3].append(item)

# Replace the crown and the fridge and the freezer with the coral and the forest and the table in Box 2.
boxes[2].remove('crown')
boxes[2].remove('fridge')
boxes[2].remove('freezer')
boxes[2].append('coral')
boxes[2].append('forest')
boxes[2].append('table')

# Replace the bell with the basket in Box 5.
boxes[5].remove('bell')
boxes[5].append('basket')

# Move the shoe and the earring from Box 8 to Box 0.
boxes[8].remove('shoe')
boxes[8].remove('earring')
boxes[0].append('shoe')
boxes[0].append('earring')

# Move the lipstick and the clock and the flute from Box 7 to Box 6.
items_to_move = ['lipstick', 'clock', 'flute']
for item in items_to_move:
    boxes[7].remove(item)
    boxes[6].append(item)

# Remove the shoes and the sculpture from Box 4.
boxes[4].remove('shoes')
boxes[4].remove('sculpture')

# Remove the dice and the basket from Box 5.
boxes[5].remove('dice')
boxes[5].remove('basket')

# Move the lipstick and the zipper and the console from Box 6 to Box 8.
items_to_move = ['lipstick', 'zipper', 'console']
for item in items_to_move:
    boxes[6].remove(item)
    boxes[8].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")