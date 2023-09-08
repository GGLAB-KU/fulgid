# Initial state of boxes
boxes = {
    0: ['camera', 'dolphin', 'jungle'],
    1: ['wallet', 'bird', 'toaster', 'boat'],
    2: ['whistle'],
    3: ['seaweed', 'telescope', 'cat', 'drum', 'lightning'],
    4: [],
    5: ['piano', 'fish', 'mask', 'sculpture', 'table'],
    6: ['pot'],
    7: ['zipper', 'tree', 'sun'],
    8: ['island', 'mountain'],
    9: ['game', 'usb', 'lion', 'shoe'],
    10: []
}

# Remove the mask and the sculpture and the table from Box 5.
items_to_remove = ['mask', 'sculpture', 'table']
for item in items_to_remove:
    boxes[5].remove(item)

# Move the tree and the sun from Box 7 to Box 0.
items_to_move = ['tree', 'sun']
for item in items_to_move:
    boxes[7].remove(item)
    boxes[0].append(item)

# Replace the game and the usb with the octopus and the seaweed in Box 9.
boxes[9].remove('game')
boxes[9].remove('usb')
boxes[9].append('octopus')
boxes[9].append('seaweed')

# Swap the boat in Box 1 with the mountain in Box 8.
boxes[1].remove('boat')
boxes[8].remove('mountain')
boxes[1].append('mountain')
boxes[8].append('boat')

# Replace the whistle with the pan in Box 2.
boxes[2].remove('whistle')
boxes[2].append('pan')

# Swap the lion in Box 9 with the cat in Box 3.
boxes[9].remove('lion')
boxes[3].remove('cat')
boxes[9].append('cat')
boxes[3].append('lion')

# Remove the pot from Box 6.
boxes[6].remove('pot')

# Move the cat and the seaweed and the shoe from Box 9 to Box 1.
items_to_move = ['cat', 'seaweed', 'shoe']
for item in items_to_move:
    boxes[9].remove(item)
    boxes[1].append(item)

# Remove the octopus from Box 9.
boxes[9].remove('octopus')

# Move the boat from Box 8 to Box 0.
boxes[8].remove('boat')
boxes[0].append('boat')

# Swap the zipper in Box 7 with the island in Box 8.
boxes[7].remove('zipper')
boxes[8].remove('island')
boxes[7].append('island')
boxes[8].append('zipper')

# Swap the zipper in Box 8 with the shoe in Box 1.
boxes[8].remove('zipper')
boxes[1].remove('shoe')
boxes[8].append('shoe')
boxes[1].append('zipper')

# Replace the boat and the tree and the sun with the lamp and the moon and the bird in Box 0.
boxes[0].remove('boat')
boxes[0].remove('tree')
boxes[0].remove('sun')
boxes[0].append('lamp')
boxes[0].append('moon')
boxes[0].append('bird')

# Replace the lamp and the moon with the dice and the ocean in Box 0.
boxes[0].remove('lamp')
boxes[0].remove('moon')
boxes[0].append('dice')
boxes[0].append('ocean')

# Put the shirt into Box 6.
boxes[6].append('shirt')

# Remove the island from Box 7.
boxes[7].remove('island')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")