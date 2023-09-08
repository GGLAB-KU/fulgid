# Initial state of boxes
boxes = {
    0: ['chair', 'starfish', 'makeup', 'clock'],
    1: ['pants', 'coin', 'freezer', 'river', 'shoes'],
    2: ['earring', 'harmonica', 'headphone'],
    3: ['toaster', 'mixer', 'cloud', 'lamp', 'fridge'],
    4: ['wig', 'magnet'],
    5: ['storm', 'cow'],
    6: ['sun', 'tie', 'desert', 'battery', 'necklace'],
    7: ['tree', 'razor', 'cat'],
    8: ['polish'],
    9: ['shelf', 'spoon', 'violin', 'ocean', 'console']
}

# Put the bag and the butterfly and the mask into Box 2.
boxes[2].append('bag')
boxes[2].append('butterfly')
boxes[2].append('mask')

# Replace the storm and the cow with the earring and the lamp in Box 5.
boxes[5].remove('storm')
boxes[5].remove('cow')
boxes[5].append('earring')
boxes[5].append('lamp')

# Move the headphone and the butterfly from Box 2 to Box 8.
boxes[2].remove('headphone')
boxes[2].remove('butterfly')
boxes[8].append('headphone')
boxes[8].append('butterfly')

# Swap the console in Box 9 with the wig in Box 4.
boxes[9].remove('console')
boxes[4].remove('wig')
boxes[9].append('wig')
boxes[4].append('console')

# Move the console and the magnet from Box 4 to Box 1.
boxes[4].remove('console')
boxes[1].append('console')
boxes[4].remove('magnet')
boxes[1].append('magnet')

# Replace the bag with the bell in Box 2.
boxes[2].remove('bag')
boxes[2].append('bell')

# Replace the necklace and the battery and the tie with the ocean and the microscope and the butterfly in Box 6.
boxes[6].remove('necklace')
boxes[6].remove('battery')
boxes[6].remove('tie')
boxes[6].append('ocean')
boxes[6].append('microscope')
boxes[6].append('butterfly')

# Move the earring from Box 5 to Box 6.
boxes[5].remove('earring')
boxes[6].append('earring')

# Put the skirt and the note into Box 4.
boxes[4].append('skirt')
boxes[4].append('note')

# Remove the mask and the harmonica and the earring from Box 2.
boxes[2].remove('mask')
boxes[2].remove('harmonica')
boxes[2].remove('earring')

# Replace the bell with the bus in Box 2.
boxes[2].remove('bell')
boxes[2].append('bus')

# Replace the fridge with the shorts in Box 3.
boxes[3].remove('fridge')
boxes[3].append('shorts')

# Move the starfish and the clock and the chair from Box 0 to Box 9.
items_to_move = ['starfish', 'clock', 'chair']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[9].append(item)

# Move the lamp from Box 5 to Box 9.
boxes[5].remove('lamp')
boxes[9].append('lamp')

# Put the needle and the cat and the bowl into Box 4.
boxes[4].append('needle')
boxes[4].append('cat')
boxes[4].append('bowl')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")