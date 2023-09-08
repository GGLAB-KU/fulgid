# Initial state of boxes
boxes = {
    0: ['fish', 'star', 'river', 'lightning'],
    1: ['cat', 'toothpaste', 'tape', 'coin', 'wire'],
    2: ['tiger', 'planet'],
    3: ['shark', 'sun', 'lion', 'boot'],
    4: [],
    5: ['toy'],
    6: ['table', 'dress', 'drum', 'tie', 'seaweed'],
    7: ['horn', 'doll', 'swimsuit', 'plane', 'shampoo']
}

# Put the phone and the snow into Box 0.
boxes[0].append('phone')
boxes[0].append('snow')

# Replace the seaweed and the tie with the vase and the sun in Box 6.
boxes[6].remove('seaweed')
boxes[6].remove('tie')
boxes[6].append('vase')
boxes[6].append('sun')

# Remove the boot and the shark from Box 3.
boxes[3].remove('boot')
boxes[3].remove('shark')

# Move the lightning and the phone and the star from Box 0 to Box 4.
items_to_move = ['lightning', 'phone', 'star']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[4].append(item)

# Remove the tiger from Box 2.
boxes[2].remove('tiger')

# Move the wire and the cat and the tape from Box 1 to Box 6.
items_to_move = ['wire', 'cat', 'tape']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[6].append(item)

# Move the toy from Box 5 to Box 0.
boxes[5].remove('toy')
boxes[0].append('toy')

# Put the lion and the ship into Box 3.
boxes[3].append('lion')
boxes[3].append('ship')

# Move the lightning and the star from Box 4 to Box 3.
items_to_move = ['lightning', 'star']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[3].append(item)

# Swap the phone in Box 4 with the planet in Box 2.
boxes[4].remove('phone')
boxes[2].remove('planet')
boxes[4].append('planet')
boxes[2].append('phone')

# Swap the toothpaste in Box 1 with the sun in Box 3.
boxes[1].remove('toothpaste')
boxes[3].remove('sun')
boxes[1].append('sun')
boxes[3].append('toothpaste')

# Remove the doll and the shampoo from Box 7.
boxes[7].remove('doll')
boxes[7].remove('shampoo')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")