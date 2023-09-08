# Initial state of boxes
boxes = {
    0: ['dice', 'tree'],
    1: ['fridge', 'speaker', 'laptop', 'wire', 'pants'],
    2: ['rain', 'razor'],
    3: ['branch'],
    4: [],
    5: ['island'],
    6: ['wallet', 'shoe', 'dress', 'elephant'],
    7: ['note', 'chair', 'bag', 'boot'],
    8: [],
    9: ['starfish'],
    10: ['rocket', 'mountain'],
    11: [],
    12: ['thread', 'bicycle', 'pen', 'grinder'],
    13: ['magnet', 'lion', 'jacket', 'motorcycle'],
    14: []
}

# Swap the starfish in Box 9 with the branch in Box 3.
boxes[9].remove('starfish')
boxes[3].remove('branch')
boxes[9].append('branch')
boxes[3].append('starfish')

# Move the wire from Box 1 to Box 11.
boxes[1].remove('wire')
boxes[11].append('wire')

# Remove the speaker and the pants and the laptop from Box 1.
items_to_remove = ['speaker', 'pants', 'laptop']
for item in items_to_remove:
    boxes[1].remove(item)

# Replace the chair with the thread in Box 7.
boxes[7].remove('chair')
boxes[7].append('thread')

# Replace the razor and the rain with the pot and the lock in Box 2.
boxes[2].remove('razor')
boxes[2].remove('rain')
boxes[2].append('pot')
boxes[2].append('lock')

# Move the note and the bag from Box 7 to Box 10.
items_to_move = ['note', 'bag']
for item in items_to_move:
    boxes[7].remove(item)
    boxes[10].append(item)

# Replace the fridge with the lipstick in Box 1.
boxes[1].remove('fridge')
boxes[1].append('lipstick')

# Replace the dice with the thread in Box 0.
boxes[0].remove('dice')
boxes[0].append('thread')

# Put the lipstick into Box 10.
boxes[10].append('lipstick')

# Put the chair and the cat and the shelf into Box 10.
items_to_move = ['chair', 'cat', 'shelf']
for item in items_to_move:
    boxes[10].append(item)

# Remove the thread and the grinder and the bicycle from Box 12.
items_to_remove = ['thread', 'grinder', 'bicycle']
for item in items_to_remove:
    boxes[12].remove(item)

# Put the towel and the train and the table into Box 13.
items_to_move = ['towel', 'train', 'table']
for item in items_to_move:
    boxes[13].append(item)

# Move the boot from Box 7 to Box 11.
boxes[7].remove('boot')
boxes[11].append('boot')

# Remove the starfish from Box 3.
boxes[3].remove('starfish')

# Move the lipstick from Box 1 to Box 13.
boxes[1].remove('lipstick')
boxes[13].append('lipstick')

# Swap the pen in Box 12 with the chair in Box 10.
boxes[12].remove('pen')
boxes[10].remove('chair')
boxes[12].append('chair')
boxes[10].append('pen')

# Put the towel and the bracelet into Box 13.
items_to_move = ['towel', 'bracelet']
for item in items_to_move:
    boxes[13].append(item)

# Remove the lock from Box 2.
boxes[2].remove('lock')

# Remove the thread from Box 7.
boxes[7].remove('thread')

# Remove the thread from Box 0.
boxes[0].remove('thread')

# Swap the branch in Box 9 with the island in Box 5.
boxes[9].remove('branch')
boxes[5].remove('island')
boxes[9].append('island')
boxes[5].append('branch')

# Move the shoe from Box 6 to Box 3.
boxes[6].remove('shoe')
boxes[3].append('shoe')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")