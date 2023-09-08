# Initial state of boxes
boxes = {
    0: ['tree', 'lion', 'beach'],
    1: ['lock', 'towel'],
    2: ['shoe', 'fish'],
    3: ['horn', 'desert', 'river'],
    4: ['usb', 'sun'],
    5: ['pillow', 'perfume', 'cat', 'watch'],
    6: ['bowl'],
    7: ['boat', 'soap', 'umbrella'],
    8: []
}

# Empty Box 4
boxes[4] = []

# Empty Box 5
boxes[5] = []

# Replace the lock with the car in Box 1
boxes[1].remove('lock')
boxes[1].append('car')

# Move the fish from Box 2 to Box 6
boxes[2].remove('fish')
boxes[6].append('fish')

# Move the bowl from Box 6 to Box 4
boxes[6].remove('bowl')
boxes[4].append('bowl')

# Swap the shoe in Box 2 with the beach in Box 0
boxes[0].remove('beach')
boxes[2].remove('shoe')
boxes[0].append('shoe')
boxes[2].append('beach')

# Move the bowl from Box 4 to Box 7
boxes[4].remove('bowl')
boxes[7].append('bowl')

# Put the sculpture into Box 6
boxes[6].append('sculpture')

# Move the desert from Box 3 to Box 1
boxes[3].remove('desert')
boxes[1].append('desert')

# Move the river from Box 3 to Box 8
boxes[3].remove('river')
boxes[8].append('river')

# Swap the river in Box 8 with the car in Box 1
boxes[1].remove('car')
boxes[8].remove('river')
boxes[1].append('river')
boxes[8].append('car')

# Swap the beach in Box 2 with the sculpture in Box 6
boxes[2].remove('beach')
boxes[6].remove('sculpture')
boxes[2].append('sculpture')
boxes[6].append('beach')

# Put the doll into Box 7
boxes[7].append('doll')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")