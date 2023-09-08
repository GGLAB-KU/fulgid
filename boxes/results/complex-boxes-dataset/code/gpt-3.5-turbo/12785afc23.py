# Initial state of boxes
boxes = {
    0: ['pot', 'wire', 'bicycle', 'cup'],
    1: ['needle', 'fridge', 'scissors', 'pan'],
    2: ['basket'],
    3: ['note'],
    4: ['bird', 'shirt'],
    5: ['mixer', 'bear'],
    6: ['coin'],
    7: ['blanket', 'soap', 'toaster', 'microwave', 'towel'],
    8: ['telescope'],
    9: ['belt', 'fork', 'puzzle'],
    10: ['glasses', 'usb'],
    11: []
}

# Remove the glasses from Box 10.
boxes[10].remove('glasses')

# Empty Box 0.
boxes[0] = []

# Swap the needle in Box 1 with the telescope in Box 8.
boxes[1].remove('needle')
boxes[8].remove('telescope')
boxes[1].append('telescope')
boxes[8].append('needle')

# Empty Box 9.
boxes[9] = []

# Remove the shirt and the bird from Box 4.
boxes[4].remove('shirt')
boxes[4].remove('bird')

# Remove the coin from Box 6.
boxes[6].remove('coin')

# Swap the blanket in Box 7 with the needle in Box 8.
boxes[7].remove('blanket')
boxes[8].remove('needle')
boxes[7].append('needle')
boxes[8].append('blanket')

# Swap the needle in Box 7 with the pan in Box 1.
boxes[7].remove('needle')
boxes[1].remove('pan')
boxes[7].append('pan')
boxes[1].append('needle')

# Replace the note with the earring in Box 3.
boxes[3].remove('note')
boxes[3].append('earring')

# Put the polish and the jungle and the pot into Box 8.
items_to_move = ['polish', 'jungle', 'pot']
for item in items_to_move:
    boxes[8].append(item)

# Swap the towel in Box 7 with the fridge in Box 1.
boxes[7].remove('towel')
boxes[1].remove('fridge')
boxes[7].append('fridge')
boxes[1].append('towel')

# Remove the usb from Box 10.
boxes[10].remove('usb')

# Replace the earring with the phone in Box 3.
boxes[3].remove('earring')
boxes[3].append('phone')

# Remove the basket from Box 2.
boxes[2].remove('basket')

# Put the gloves and the planet into Box 8.
items_to_move = ['gloves', 'planet']
for item in items_to_move:
    boxes[8].append(item)

# Replace the polish and the jungle with the lightning and the coral in Box 8.
boxes[8].remove('polish')
boxes[8].remove('jungle')
boxes[8].append('lightning')
boxes[8].append('coral')

# Swap the bear in Box 5 with the phone in Box 3.
boxes[5].remove('bear')
boxes[3].remove('phone')
boxes[5].append('phone')
boxes[3].append('bear')

# Move the bear from Box 3 to Box 8.
boxes[3].remove('bear')
boxes[8].append('bear')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")