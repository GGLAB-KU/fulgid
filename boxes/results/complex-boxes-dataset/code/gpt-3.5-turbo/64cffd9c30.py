# Initial state of boxes
boxes = {
    0: ['battery', 'truck'],
    1: ['tie', 'rocket', 'moon'],
    2: ['grinder', 'wallet', 'shoes', 'toothbrush'],
    3: ['bag', 'dog', 'dolphin'],
    4: ['mirror', 'bird'],
    5: ['rain', 'shark'],
    6: ['bear', 'crown', 'plane', 'guitar']
}

# Move the wallet from Box 2 to Box 1.
boxes[2].remove('wallet')
boxes[1].append('wallet')

# Move the plane and the crown and the guitar from Box 6 to Box 1.
items_to_move = ['plane', 'crown', 'guitar']
for item in items_to_move:
    boxes[6].remove(item)
    boxes[1].append(item)

# Put the sun into Box 0.
boxes[0].append('sun')

# Put the paint and the comet into Box 1.
boxes[1].append('paint')
boxes[1].append('comet')

# Put the magnet and the speaker into Box 5.
boxes[5].append('magnet')
boxes[5].append('speaker')

# Remove the truck and the battery and the sun from Box 0.
items_to_remove = ['truck', 'battery', 'sun']
for item in items_to_remove:
    boxes[0].remove(item)

# Put the razor into Box 2.
boxes[2].append('razor')

# Replace the bird with the glasses in Box 4.
boxes[4].remove('bird')
boxes[4].append('glasses')

# Move the razor and the grinder from Box 2 to Box 1.
items_to_move = ['razor', 'grinder']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[1].append(item)

# Put the bird into Box 4.
boxes[4].append('bird')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")