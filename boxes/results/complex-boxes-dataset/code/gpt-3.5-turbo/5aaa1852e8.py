# Initial state of boxes
boxes = {
    0: ['needle', 'grinder', 'ring'],
    1: ['toy', 'crown', 'note'],
    2: ['rain', 'tape', 'drum', 'key', 'thunder'],
    3: ['coat', 'console', 'polish', 'battery', 'plane'],
    4: ['shoes', 'scissors', 'jungle', 'paint', 'gloves'],
    5: ['toothpaste', 'wallet', 'island', 'dice'],
    6: ['tie', 'elephant', 'whistle', 'pot'],
    7: ['star', 'usb'],
    8: ['tiger', 'microscope', 'earring', 'lion', 'microwave'],
    9: []
}

# Replace the toy and the note and the crown with the zipper and the shoes and the dolphin in Box 1.
boxes[1].remove('toy')
boxes[1].remove('note')
boxes[1].remove('crown')
boxes[1].append('zipper')
boxes[1].append('shoes')
boxes[1].append('dolphin')

# Move the rain and the drum from Box 2 to Box 8.
items_to_move = ['rain', 'drum']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[8].append(item)

# Swap the elephant in Box 6 with the tiger in Box 8.
boxes[6].remove('elephant')
boxes[8].remove('tiger')
boxes[6].append('tiger')
boxes[8].append('elephant')

# Remove the whistle and the pot and the tie from Box 6.
items_to_remove = ['whistle', 'pot', 'tie']
for item in items_to_remove:
    boxes[6].remove(item)

# Move the key and the thunder and the tape from Box 2 to Box 9.
items_to_move = ['key', 'thunder', 'tape']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[9].append(item)

# Move the zipper and the shoes and the dolphin from Box 1 to Box 5.
items_to_move = ['zipper', 'shoes', 'dolphin']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[5].append(item)

# Replace the ring with the train in Box 0.
boxes[0].remove('ring')
boxes[0].append('train')

# Replace the gloves with the glove in Box 4.
boxes[4].remove('gloves')
boxes[4].append('glove')

# Put the shoe and the bag into Box 5.
boxes[5].append('shoe')
boxes[5].append('bag')

# Replace the tiger with the crown in Box 6.
boxes[6].remove('tiger')
boxes[6].append('crown')

# Put the submarine and the sculpture into Box 5.
boxes[5].append('submarine')
boxes[5].append('sculpture')

# Replace the needle and the train and the grinder with the island and the leaf and the ocean in Box 0.
boxes[0].remove('needle')
boxes[0].remove('train')
boxes[0].remove('grinder')
boxes[0].append('island')
boxes[0].append('leaf')
boxes[0].append('ocean')

# Replace the crown with the ring in Box 6.
boxes[6].remove('crown')
boxes[6].append('ring')

# Move the polish and the battery from Box 3 to Box 8.
items_to_move = ['polish', 'battery']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[8].append(item)

# Replace the island and the leaf and the ocean with the dog and the mask and the thunder in Box 0.
boxes[0].remove('island')
boxes[0].remove('leaf')
boxes[0].remove('ocean')
boxes[0].append('dog')
boxes[0].append('mask')
boxes[0].append('thunder')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")