# Initial state of boxes
boxes = {
    0: [],
    1: ['snow', 'razor', 'shorts', 'jungle', 'crown'],
    2: ['tree', 'fridge', 'makeup', 'branch'],
    3: ['charger', 'drum', 'cow', 'toothpaste'],
    4: ['sandals'],
    5: [],
    6: ['frame', 'shark', 'car', 'vase', 'shoe'],
    7: [],
    8: ['game', 'glasses'],
    9: ['pot', 'mirror'],
    10: ['lamp', 'motorcycle', 'perfume', 'rock'],
    11: ['battery'],
    12: [],
    13: ['cup']
}

# Move the pot and the mirror from Box 9 to Box 7.
boxes[9].remove('pot')
boxes[9].remove('mirror')
boxes[7].append('pot')
boxes[7].append('mirror')

# Put the jungle and the shelf and the bracelet into Box 6.
items_to_move = ['jungle', 'shelf', 'bracelet']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[6].append(item)

# Move the lamp from Box 10 to Box 2.
boxes[10].remove('lamp')
boxes[2].append('lamp')

# Put the phone and the blanket into Box 1.
boxes[1].append('phone')
boxes[1].append('blanket')

# Put the perfume into Box 13.
boxes[10].remove('perfume')
boxes[13].append('perfume')

# Put the blender into Box 2.
boxes[2].append('blender')

# Swap the makeup in Box 2 with the game in Box 8.
boxes[2].remove('makeup')
boxes[8].remove('game')
boxes[2].append('game')
boxes[8].append('makeup')

# Replace the battery with the bear in Box 11.
boxes[11].remove('battery')
boxes[11].append('bear')

# Put the bus into Box 8.
boxes[8].append('bus')

# Empty Box 2.
boxes[2] = []

# Replace the bear with the usb in Box 11.
boxes[11].remove('bear')
boxes[11].append('usb')

# Swap the charger in Box 3 with the usb in Box 11.
boxes[3].remove('charger')
boxes[11].remove('usb')
boxes[3].append('usb')
boxes[11].append('charger')

# Empty Box 3.
boxes[3] = []

# Swap the bus in Box 8 with the vase in Box 6.
boxes[8].remove('bus')
boxes[6].remove('vase')
boxes[8].append('vase')
boxes[6].append('bus')

# Remove the vase from Box 8.
boxes[8].remove('vase')

# Put the chair and the razor and the bird into Box 0.
items_to_move = ['chair', 'razor', 'bird']
for item in items_to_move:
    boxes[0].append(item)

# Move the sandals from Box 4 to Box 8.
boxes[4].remove('sandals')
boxes[8].append('sandals')

# Empty Box 0.
boxes[0] = []

# Put the star and the toaster into Box 0.
boxes[0].append('star')
boxes[0].append('toaster')

# Put the octopus and the earring into Box 1.
boxes[1].append('octopus')
boxes[1].append('earring')

# Replace the cup and the perfume with the flower and the console in Box 13.
boxes[13].remove('cup')
boxes[10].remove('perfume')
boxes[13].append('flower')
boxes[13].append('console')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")