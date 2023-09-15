box = {
    0: ['puzzle', 'magnet'],
    1: ['butterfly', 'helmet', 'violin'],
    2: [],
    3: ['headphone', 'motorcycle'],
    4: ['ocean'],
    5: ['river', 'vase', 'storm', 'controller', 'horse'],
    6: ['toy', 'glasses', 'moon', 'lightning'],
    7: [],
    8: ['book', 'tree'],
    9: ['flute', 'paint', 'dice', 'polish'],
    10: ['toothbrush', 'glove', 'rock'],
    11: [],
    12: ['freezer', 'pants', 'basket'],
    13: ['frame', 'towel', 'shorts', 'key', 'skirt'],
    14: ['bear']
}

def print_boxes():
    for i in range(15):
        if i in box:
            print(f"Box {i}: {box[i]}")
        else:
            print(f"Box {i}: []")

# Initial state
print_boxes()

# Put the needle and the telescope into Box 1
box[1].extend(['needle', 'telescope'])

# Move the polish and the flute and the dice from Box 9 to Box 10
box[10].extend(box[9].pop(box[9].index('polish')))
box[10].extend(box[9].pop(box[9].index('flute')))
box[10].extend(box[9].pop(box[9].index('dice')))

# Put the boot and the telescope into Box 3
box[3].extend(['boot', 'telescope'])

# Replace the controller and the horse with the shirt and the makeup in Box 5
box[5].remove('controller')
box[5].remove('horse')
box[5].extend(['shirt', 'makeup'])

# Replace the bear with the tape in Box 14
box[14].remove('bear')
box[14].extend(['tape'])

# Swap the ocean in Box 4 with the puzzle in Box 0
box[0].remove('puzzle')
box[4].remove('ocean')
box[0].extend(['ocean'])
box[4].extend(['puzzle'])

# Swap the magnet in Box 0 with the freezer in Box 12
box[0].remove('magnet')
box[12].remove('freezer')
box[0].extend(['freezer'])
box[12].extend(['magnet'])

# Replace the freezer with the usb in Box 0
box[0].remove('freezer')
box[0].extend(['usb'])

# Remove the river from Box 5
box[5].remove('river')

# Remove the polish and the toothbrush and the dice from Box 10
box[10].remove('polish')
box[10].remove('toothbrush')
box[10].remove('dice')

# Empty Box 9
box[9] = []

# Swap the tape in Box 14 with the tree in Box 8
box[8].remove('tree')
box[14].remove('tape')
box[8].extend(['tape'])
box[14].extend(['tree'])

# Move the makeup from Box 5 to Box 0
box[0].extend(box[5].pop(box[5].index('makeup')))

# Put the chair and the snow and the boat into Box 6
box[6].extend(['chair', 'snow', 'boat'])

# Replace the glove with the toothpaste in Box 10
box[10].remove('glove')
box[10].extend(['toothpaste'])

# Swap the toothpaste in Box 10 with the storm in Box 5
box[5].remove('storm')
box[10].remove('toothpaste')
box[5].extend(['toothpaste'])
box[10].extend(['storm'])

# Swap the frame in Box 13 with the puzzle in Box 4
box[4].remove('puzzle')
box[13].remove('frame')
box[4].extend(['frame'])
box[13].extend(['puzzle'])

# Put the freezer into Box 7
box[7].extend(box[12].pop(box[12].index('freezer')))

# Empty Box 7
box[7] = []

# Swap the key in Box 13 with the tape in Box 8
box[8].remove('tape')
box[13].remove('key')
box[8].extend(['key'])
box[13].extend(['tape'])

# Swap the book in Box 8 with the storm in Box 10
box[10].remove('storm')
box[8].remove('book')
box[10].extend(['book'])
box[8].extend(['storm'])

# Put the mask and the desert and the horse into Box 5
box[5].extend(['mask', 'desert', 'horse'])

# Final state
print_boxes()