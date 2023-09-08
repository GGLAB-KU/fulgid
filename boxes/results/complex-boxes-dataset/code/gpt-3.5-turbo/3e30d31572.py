# Initial state of boxes
boxes = {
    0: ['planet', 'grass'],
    1: ['flower', 'butterfly', 'button', 'starfish', 'toy'],
    2: [],
    3: ['card', 'plate', 'shampoo', 'wire', 'towel'],
    4: [],
    5: ['tree'],
    6: ['perfume', 'shoe', 'brush', 'comb'],
    7: ['magnet', 'lock'],
    8: ['dress', 'soap', 'seaweed', 'necklace', 'flute']
}

# Swap the wire in Box 3 with the shoe in Box 6.
boxes[3].remove('wire')
boxes[6].remove('shoe')
boxes[3].append('shoe')
boxes[6].append('wire')

# Replace the brush and the perfume and the comb with the scarf and the jungle and the jacket in Box 6.
boxes[6].remove('brush')
boxes[6].remove('perfume')
boxes[6].remove('comb')
boxes[6].append('scarf')
boxes[6].append('jungle')
boxes[6].append('jacket')

# Move the tree from Box 5 to Box 3.
boxes[5].remove('tree')
boxes[3].append('tree')

# Swap the lock in Box 7 with the shoe in Box 3.
boxes[7].remove('lock')
boxes[3].remove('shoe')
boxes[7].append('shoe')
boxes[3].append('lock')

# Move the flower from Box 1 to Box 2.
boxes[1].remove('flower')
boxes[2].append('flower')

# Move the dress and the necklace and the flute from Box 8 to Box 6.
items_to_move = ['dress', 'necklace', 'flute']
for item in items_to_move:
    boxes[8].remove(item)
    boxes[6].append(item)

# Move the grass and the planet from Box 0 to Box 3.
items_to_move = ['grass', 'planet']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[3].append(item)

# Put the controller and the pillow into Box 5.
items_to_put = ['controller', 'pillow']
for item in items_to_put:
    boxes[5].append(item)

# Put the elephant and the paint and the skirt into Box 3.
items_to_put = ['elephant', 'paint', 'skirt']
for item in items_to_put:
    boxes[3].append(item)

# Replace the grass with the pan in Box 3.
boxes[3].remove('grass')
boxes[3].append('pan')

# Replace the starfish with the tape in Box 1.
boxes[1].remove('starfish')
boxes[1].append('tape')

# Move the pillow from Box 5 to Box 6.
boxes[5].remove('pillow')
boxes[6].append('pillow')

# Remove the seaweed from Box 8.
boxes[8].remove('seaweed')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")