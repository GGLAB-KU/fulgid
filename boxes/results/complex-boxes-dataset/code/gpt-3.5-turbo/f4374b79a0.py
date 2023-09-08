# Initial state of boxes
boxes = {
    0: ['dress'],
    1: ['swimsuit', 'toothbrush', 'towel', 'ocean', 'gloves'],
    2: [],
    3: ['glasses', 'snow'],
    4: ['rock', 'seaweed'],
    5: ['needle'],
    6: ['game', 'coral', 'grass', 'wig'],
    7: ['scarf', 'horn', 'octopus', 'razor'],
    8: ['lion', 'freezer'],
    9: ['boot'],
    10: ['moon', 'earring', 'card', 'frame'],
    11: ['motorcycle', 'bowl', 'magnet'],
    12: ['mask']
}

# Put the sandals into Box 2.
boxes[2].append('sandals')

# Remove the boot from Box 9.
boxes[9].remove('boot')

# Swap the game in Box 6 with the earring in Box 10.
boxes[6].remove('game')
boxes[10].remove('earring')
boxes[6].append('earring')
boxes[10].append('game')

# Move the toothbrush from Box 1 to Box 11.
boxes[1].remove('toothbrush')
boxes[11].append('toothbrush')

# Put the coral into Box 4.
boxes[4].append('coral')

# Put the shoes into Box 7.
boxes[7].extend(['shoe', 'lock'])

# Move the needle from Box 5 to Box 8.
boxes[5].remove('needle')
boxes[8].append('needle')

# Move the ocean from Box 1 to Box 4.
boxes[1].remove('ocean')
boxes[4].append('ocean')

# Replace the coral and the wig with the sculpture and the magnet in Box 6.
boxes[6].remove('coral')
boxes[6].remove('wig')
boxes[6].append('sculpture')
boxes[6].append('magnet')

# Put the shoe and the lock into Box 4.
boxes[4].extend(['shoe', 'lock'])

# Replace the dress with the toothbrush in Box 0.
boxes[0].remove('dress')
boxes[0].append('toothbrush')

# Swap the glasses in Box 3 with the lock in Box 4.
boxes[3].remove('glasses')
boxes[4].remove('lock')
boxes[3].append('lock')
boxes[4].append('glasses')

# Move the lion and the needle from Box 8 to Box 7.
boxes[8].remove('lion')
boxes[8].remove('needle')
boxes[7].extend(['lion', 'needle'])

# Put the butterfly into Box 4.
boxes[4].append('butterfly')

# Replace the freezer with the fridge in Box 8.
boxes[8].remove('freezer')
boxes[8].append('fridge')

# Swap the bowl in Box 11 with the mask in Box 12.
boxes[11].remove('bowl')
boxes[12].remove('mask')
boxes[11].append('mask')
boxes[12].append('bowl')

# Put the console into Box 9.
boxes[9].append('console')

# Remove the swimsuit and the towel and the gloves from Box 1.
items_to_remove = ['swimsuit', 'towel', 'gloves']
for item in items_to_remove:
    boxes[1].remove(item)

# Move the toothbrush from Box 0 to Box 9.
boxes[0].remove('toothbrush')
boxes[9].append('toothbrush')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")