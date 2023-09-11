# Initial state of boxes
boxes = {
    0: ['zipper', 'blanket', 'coral', 'bag'],
    1: ['basket', 'shoes'],
    2: ['glasses', 'microscope'],
    3: ['bus'],
    4: [],
    5: ['sculpture', 'hat', 'vase', 'shirt', 'mirror'],
    6: [],
    7: ['clock'],
    8: ['tree', 'shark', 'lion'],
    9: ['belt', 'scissors', 'desert', 'button', 'book'],
    10: ['flower', 'coat', 'fork', 'ship']
}

# Move the zipper and the bag from Box 0 to Box 6.
items_to_move = ['zipper', 'bag']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[6].append(item)

# Put the glasses and the starfish and the bus into Box 7.
items_to_move = ['glasses', 'starfish', 'bus']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[7].append(item)

# Swap the coral in Box 0 with the basket in Box 1.
boxes[0].remove('coral')
boxes[1].remove('basket')
boxes[0].append('basket')
boxes[1].append('coral')

# Swap the vase in Box 5 with the shark in Box 8.
boxes[5].remove('vase')
boxes[8].remove('shark')
boxes[5].append('shark')
boxes[8].append('vase')

# Swap the bus in Box 3 with the tree in Box 8.
boxes[3].remove('bus')
boxes[8].remove('tree')
boxes[3].append('tree')
boxes[8].append('bus')

# Replace the basket and the blanket with the branch and the lipstick in Box 0.
boxes[0].remove('basket')
boxes[0].remove('blanket')
boxes[0].append('branch')
boxes[0].append('lipstick')

# Put the crown and the thunder and the thread into Box 3.
items_to_move = ['crown', 'thunder', 'thread']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[3].append(item)

# Replace the coral with the perfume in Box 1.
boxes[1].remove('coral')
boxes[1].append('perfume')

# Swap the mirror in Box 5 with the ship in Box 10.
boxes[5].remove('mirror')
boxes[10].remove('ship')
boxes[5].append('ship')
boxes[10].append('mirror')

# Put the bowl and the wallet into Box 10.
items_to_move = ['bowl', 'wallet']
for item in items_to_move:
    boxes[10].append(item)

# Replace the lion with the toy in Box 8.
boxes[8].remove('lion')
boxes[8].append('toy')

# Swap the book in Box 9 with the perfume in Box 1.
boxes[9].remove('book')
boxes[1].remove('perfume')
boxes[9].append('perfume')
boxes[1].append('book')

# Move the microscope from Box 2 to Box 3.
boxes[2].remove('microscope')
boxes[3].append('microscope')

# Replace the mirror with the butterfly in Box 10.
boxes[5].remove('mirror')
boxes[10].append('butterfly')

# Swap the clock in Box 7 with the tree in Box 3.
boxes[7].remove('clock')
boxes[3].remove('tree')
boxes[7].append('tree')
boxes[3].append('clock')

# Replace the bus and the vase with the planet and the wig in Box 8.
boxes[3].remove('bus')
boxes[8].remove('vase')
boxes[8].append('planet')
boxes[8].append('wig')

# Remove the wallet and the bowl from Box 10.
items_to_remove = ['wallet', 'bowl']
for item in items_to_remove:
    boxes[10].remove(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")