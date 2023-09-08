# Initial state of boxes
boxes = {
    0: ['crown', 'skirt', 'flute', 'pot', 'card'],
    1: [],
    2: ['ocean', 'wallet', 'shelf', 'drum'],
    3: ['planet'],
    4: [],
    5: ['shark', 'watch'],
    6: [],
    7: [],
    8: ['motorcycle', 'moon', 'coral'],
    9: ['thread', 'perfume', 'meteor', 'dolphin', 'tree'],
    10: ['toaster', 'jungle'],
    11: ['earring']
}

# Put the shampoo and the boot into Box 6.
boxes[6].append('shampoo')
boxes[6].append('boot')

# Swap the jungle in Box 10 with the shark in Box 5.
boxes[10].remove('jungle')
boxes[5].remove('shark')
boxes[10].append('shark')
boxes[5].append('jungle')

# Move the planet from Box 3 to Box 6.
boxes[3].remove('planet')
boxes[6].append('planet')

# Empty Box 2.
boxes[2] = []

# Replace the jungle with the keyboard in Box 5.
boxes[5].remove('jungle')
boxes[5].append('keyboard')

# Put the cup into Box 7.
boxes[7].append('cup')

# Remove the skirt from Box 0.
boxes[0].remove('skirt')

# Remove the cup from Box 7.
boxes[7].remove('cup')

# Move the motorcycle and the moon and the coral from Box 8 to Box 11.
items_to_move = ['motorcycle', 'moon', 'coral']
for item in items_to_move:
    boxes[8].remove(item)
    boxes[11].append(item)

# Empty Box 6.
boxes[6] = []

# Swap the thread in Box 9 with the toaster in Box 10.
boxes[9].remove('thread')
boxes[10].remove('toaster')
boxes[9].append('toaster')
boxes[10].append('thread')

# Remove the dolphin and the meteor from Box 9.
boxes[9].remove('dolphin')
boxes[9].remove('meteor')

# Swap the motorcycle in Box 11 with the keyboard in Box 5.
boxes[11].remove('motorcycle')
boxes[5].remove('keyboard')
boxes[11].append('keyboard')
boxes[5].append('motorcycle')

# Move the watch and the motorcycle from Box 5 to Box 4.
items_to_move = ['watch', 'motorcycle']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[4].append(item)

# Move the coral and the keyboard and the moon from Box 11 to Box 3.
items_to_move = ['coral', 'keyboard', 'moon']
for item in items_to_move:
    boxes[11].remove(item)
    boxes[3].append(item)

# Swap the earring in Box 11 with the motorcycle in Box 4.
boxes[11].remove('earring')
boxes[4].remove('motorcycle')
boxes[11].append('motorcycle')
boxes[4].append('earring')

# Swap the card in Box 0 with the thread in Box 10.
boxes[0].remove('card')
boxes[10].remove('thread')
boxes[0].append('thread')
boxes[10].append('card')

# Replace the perfume with the dice in Box 9.
boxes[9].remove('perfume')
boxes[9].append('dice')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")