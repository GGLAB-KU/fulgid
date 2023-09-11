# Initial state of boxes
boxes = {
    0: [],
    1: ['jacket', 'belt', 'boat', 'fork', 'keyboard'],
    2: ['starfish'],
    3: ['sculpture', 'mirror', 'shirt', 'note', 'ring'],
    4: ['speaker'],
    5: [],
    6: []
}

# Move the keyboard and the boat from Box 1 to Box 3.
boxes[1].remove('keyboard')
boxes[1].remove('boat')
boxes[3].append('keyboard')
boxes[3].append('boat')

# Put the octopus and the thread into Box 6.
boxes[6].append('octopus')
boxes[6].append('thread')

# Replace the sculpture with the game in Box 3.
boxes[3].remove('sculpture')
boxes[3].append('game')

# Swap the speaker in Box 4 with the octopus in Box 6.
boxes[4], boxes[6] = boxes[6], boxes[4]

# Swap the shirt in Box 3 with the jacket in Box 1.
boxes[3].remove('shirt')
boxes[1].remove('jacket')
boxes[3].append('jacket')
boxes[1].append('shirt')

# Move the speaker and the thread from Box 6 to Box 2.
boxes[6].remove('speaker')
boxes[6].remove('thread')
boxes[2].append('speaker')
boxes[2].append('thread')

# Remove the shirt and the belt and the fork from Box 1.
items_to_remove = ['shirt', 'belt', 'fork']
for item in items_to_remove:
    boxes[1].remove(item)

# Put the mountain and the dolphin and the thunder into Box 3.
items_to_add = ['mountain', 'dolphin', 'thunder']
for item in items_to_add:
    boxes[3].append(item)

# Put the shelf and the perfume into Box 2.
boxes[2].append('shelf')
boxes[2].append('perfume')

# Put the lipstick and the watch and the lock into Box 6.
boxes[6].append('lipstick')
boxes[6].append('watch')
boxes[6].append('lock')

# Empty Box 3.
boxes[3] = []

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")