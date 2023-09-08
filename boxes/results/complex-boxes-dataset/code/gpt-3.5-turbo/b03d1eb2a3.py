# Initial state of boxes
boxes = {
    0: ['bicycle', 'boat', 'horn', 'tie', 'toaster'],
    1: ['sock', 'boot', 'coat', 'bear', 'gloves'],
    2: ['coin', 'dolphin', 'plane'],
    3: ['microwave'],
    4: ['jacket'],
    5: ['belt', 'rock'],
    6: [],
    7: ['wallet', 'harmonica', 'thunder'],
    8: []
}

# Remove the boat from Box 0.
boxes[0].remove('boat')

# Move the horn and the toaster from Box 0 to Box 4.
boxes[0].remove('horn')
boxes[0].remove('toaster')
boxes[4].append('horn')
boxes[4].append('toaster')

# Empty Box 3.
boxes[3] = []

# Move the toaster from Box 4 to Box 8.
boxes[4].remove('toaster')
boxes[8].append('toaster')

# Put the grass into Box 6.
boxes[6].append('grass')

# Replace the horn with the fork in Box 4.
boxes[4].remove('horn')
boxes[4].append('fork')

# Put the scissors and the sandals into Box 0.
boxes[0].append('scissors')
boxes[0].append('sandals')

# Move the dolphin from Box 2 to Box 8.
boxes[2].remove('dolphin')
boxes[8].append('dolphin')

# Put the jungle and the mountain into Box 4.
boxes[4].append('jungle')
boxes[4].append('mountain')

# Move the boot and the coat and the sock from Box 1 to Box 2.
items_to_move = ['boot', 'coat', 'sock']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[2].append(item)

# Move the rock from Box 5 to Box 7.
boxes[5].remove('rock')
boxes[7].append('rock')

# Put the fish and the pot into Box 2.
boxes[2].append('fish')
boxes[2].append('pot')

# Replace the grass with the coat in Box 6.
boxes[6].remove('grass')
boxes[6].append('coat')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")