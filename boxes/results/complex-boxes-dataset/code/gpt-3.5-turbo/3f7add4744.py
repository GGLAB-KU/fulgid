# Initial state of boxes
boxes = {
    0: ['boot', 'branch', 'pillow', 'wallet'],
    1: ['wig'],
    2: ['river', 'usb', 'drum', 'scarf'],
    3: ['submarine', 'mirror'],
    4: ['speaker'],
    5: ['card', 'lipstick'],
    6: ['moon', 'console', 'microwave', 'meteor', 'bear'],
    7: ['phone', 'shoe', 'charger'],
    8: [],
    9: ['keyboard', 'swimsuit', 'bowl', 'rain', 'magnet'],
    10: [],
    11: ['microscope', 'glasses', 'tape', 'thunder'],
    12: ['crown', 'mountain', 'toothpaste']
}

# Swap the wig in Box 1 with the speaker in Box 4.
boxes[1].remove('wig')
boxes[4].remove('speaker')
boxes[1].append('speaker')
boxes[4].append('wig')

# Move the boot and the pillow from Box 0 to Box 4.
items_to_move = ['boot', 'pillow']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[4].append(item)

# Put the pen into Box 12.
boxes[12].append('pen')

# Remove the bear from Box 6.
boxes[6].remove('bear')

# Move the wallet from Box 0 to Box 1.
boxes[0].remove('wallet')
boxes[1].append('wallet')

# Remove the lipstick and the card from Box 5.
items_to_remove = ['lipstick', 'card']
for item in items_to_remove:
    boxes[5].remove(item)

# Remove the wig and the boot from Box 4.
items_to_remove = ['wig', 'boot']
for item in items_to_remove:
    boxes[4].remove(item)

# Replace the crown and the toothpaste and the mountain with the keyboard and the train and the game in Box 12.
boxes[12].remove('crown')
boxes[12].remove('toothpaste')
boxes[12].remove('mountain')
boxes[12].append('keyboard')
boxes[12].append('train')
boxes[12].append('game')

# Move the meteor from Box 6 to Box 12.
boxes[6].remove('meteor')
boxes[12].append('meteor')

# Remove the glasses and the microscope and the thunder from Box 11.
items_to_remove = ['glasses', 'microscope', 'thunder']
for item in items_to_remove:
    boxes[11].remove(item)

# Remove the branch from Box 0.
boxes[0].remove('branch')

# Put the perfume and the thread into Box 11.
boxes[11].append('perfume')
boxes[11].append('thread')

# Swap the scarf in Box 2 with the tape in Box 11.
boxes[2].remove('scarf')
boxes[11].remove('tape')
boxes[2].append('tape')
boxes[11].append('scarf')

# Move the shoe and the charger and the phone from Box 7 to Box 9.
items_to_move = ['shoe', 'charger', 'phone']
for item in items_to_move:
    boxes[7].remove(item)
    boxes[9].append(item)

# Remove the mirror and the submarine from Box 3.
items_to_remove = ['mirror', 'submarine']
for item in items_to_remove:
    boxes[3].remove(item)

# Put the butterfly and the bicycle into Box 10.
boxes[10].append('butterfly')
boxes[10].append('bicycle')

# Replace the scarf and the thread and the perfume with the violin and the ocean and the bracelet in Box 11.
boxes[11].remove('scarf')
boxes[11].remove('thread')
boxes[11].remove('perfume')
boxes[11].append('violin')
boxes[11].append('ocean')
boxes[11].append('bracelet')

# Move the usb and the tape from Box 2 to Box 12.
items_to_move = ['usb', 'tape']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[12].append(item)

# Replace the pillow with the needle in Box 4.
boxes[4].remove('pillow')
boxes[4].append('needle')

# Move the speaker from Box 1 to Box 5.
boxes[1].remove('speaker')
boxes[5].append('speaker')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")