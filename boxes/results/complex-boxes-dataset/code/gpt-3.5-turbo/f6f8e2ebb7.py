# Initial state of boxes
boxes = {
    0: [],
    1: [],
    2: [],
    3: ['shorts', 'lock', 'swimsuit', 'flower', 'shelf'],
    4: ['basket', 'umbrella', 'flute'],
    5: ['helmet', 'truck'],
    6: [],
    7: ['bear', 'comet', 'wig'],
    8: ['pan'],
    9: ['horn', 'clock', 'game', 'seaweed'],
    10: ['razor', 'harmonica', 'coin'],
    11: ['phone', 'mixer'],
    12: []
}

# Remove the harmonica and the razor and the coin from Box 10.
boxes[10].remove('harmonica')
boxes[10].remove('razor')
boxes[10].remove('coin')

# Put the octopus and the sandals and the horse into Box 0.
boxes[0].append('octopus')
boxes[0].append('sandals')
boxes[0].append('horse')

# Swap the basket in Box 4 with the flower in Box 3.
boxes[4].remove('basket')
boxes[3].remove('flower')
boxes[4].append('flower')
boxes[3].append('basket')

# Move the clock and the seaweed and the horn from Box 9 to Box 5.
items_to_move = ['clock', 'seaweed', 'horn']
for item in items_to_move:
    boxes[9].remove(item)
    boxes[5].append(item)

# Empty Box 11.
boxes[11] = []

# Put the boot and the phone into Box 4.
boxes[4].append('boot')
boxes[4].append('phone')

# Move the wig and the comet and the bear from Box 7 to Box 9.
items_to_move = ['wig', 'comet', 'bear']
for item in items_to_move:
    boxes[7].remove(item)
    boxes[9].append(item)

# Swap the game in Box 9 with the basket in Box 3.
boxes[9].remove('game')
boxes[3].remove('basket')
boxes[9].append('basket')
boxes[3].append('game')

# Put the table into Box 12.
boxes[12].append('table')

# Replace the truck with the sock in Box 5.
boxes[5].remove('truck')
boxes[5].append('sock')

# Swap the pan in Box 8 with the wig in Box 9.
boxes[8].remove('pan')
boxes[9].remove('wig')
boxes[8].append('wig')
boxes[9].append('pan')

# Move the table from Box 12 to Box 0.
boxes[12].remove('table')
boxes[0].append('table')

# Remove the horn from Box 5.
boxes[5].remove('horn')

# Move the horse from Box 0 to Box 6.
boxes[0].remove('horse')
boxes[6].append('horse')

# Move the swimsuit and the game and the shelf from Box 3 to Box 4.
items_to_move = ['swimsuit', 'game', 'shelf']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[4].append(item)

# Empty Box 8.
boxes[8] = []

# Put the elephant and the tiger into Box 6.
boxes[6].append('elephant')
boxes[6].append('tiger')

# Replace the swimsuit with the boat in Box 4.
boxes[4].remove('swimsuit')
boxes[4].append('boat')

# Replace the game and the flute with the horse and the razor in Box 4.
boxes[4].remove('game')
boxes[4].remove('flute')
boxes[4].append('horse')
boxes[4].append('razor')

# Put the telescope into Box 4.
boxes[4].append('telescope')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")