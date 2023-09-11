# Initial state of boxes
boxes = {
    0: ['comet'],
    1: ['wallet', 'toy'],
    2: ['ring', 'basket', 'river', 'earring', 'charger'],
    3: ['plane', 'motorcycle', 'usb', 'freezer', 'table'],
    4: ['towel', 'storm', 'tie', 'octopus', 'rock'],
    5: ['scissors', 'shoes', 'blanket', 'card'],
    6: ['makeup', 'cow', 'branch'],
    7: ['ocean'],
    8: ['car', 'cat', 'mirror'],
    9: ['seaweed', 'pen', 'mask'],
    10: []
}

# Empty Box 3
boxes[3] = []

# Move the wallet and the toy from Box 1 to Box 10
items_to_move = ['wallet', 'toy']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[10].append(item)

# Move the basket and the earring and the charger from Box 2 to Box 6
items_to_move = ['basket', 'earring', 'charger']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[6].append(item)

# Move the seaweed and the pen and the mask from Box 9 to Box 4
items_to_move = ['seaweed', 'pen', 'mask']
for item in items_to_move:
    boxes[9].remove(item)
    boxes[4].append(item)

# Swap the cat in Box 8 with the ocean in Box 7
boxes[8].remove('cat')
boxes[7].remove('ocean')
boxes[8].append('ocean')
boxes[7].append('cat')

# Move the comet from Box 0 to Box 2
boxes[0].remove('comet')
boxes[2].append('comet')

# Put the octopus and the coin and the magnet into Box 2
items_to_put = ['octopus', 'coin', 'magnet']
for item in items_to_put:
    boxes[2].append(item)

# Swap the comet in Box 2 with the tie in Box 4
boxes[2].remove('comet')
boxes[4].remove('tie')
boxes[2].append('tie')
boxes[4].append('comet')

# Empty Box 8
boxes[8] = []

# Replace the cat with the tree in Box 7
boxes[7].remove('cat')
boxes[7].append('tree')

# Put the towel into Box 8
boxes[4].remove('towel')
boxes[8].append('towel')

# Put the guitar and the candle into Box 3
items_to_put = ['guitar', 'candle']
for item in items_to_put:
    boxes[3].append(item)

# Put the cup into Box 1
boxes[1].append('cup')

# Replace the storm with the flute in Box 4
boxes[4].remove('storm')
boxes[4].append('flute')

# Swap the wallet in Box 10 with the flute in Box 4
boxes[10].remove('wallet')
boxes[4].remove('flute')
boxes[10].append('flute')
boxes[4].append('wallet')

# Move the toy and the flute from Box 10 to Box 4
items_to_move = ['toy', 'flute']
for item in items_to_move:
    boxes[10].remove(item)
    boxes[4].append(item)

# Move the cow from Box 6 to Box 2
boxes[6].remove('cow')
boxes[2].append('cow')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")