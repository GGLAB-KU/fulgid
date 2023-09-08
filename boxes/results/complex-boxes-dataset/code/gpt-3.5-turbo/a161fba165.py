# Initial state of boxes
boxes = {
    0: ['flower', 'bell', 'coin', 'violin'],
    1: ['usb', 'microscope', 'coat'],
    2: ['thunder', 'tape'],
    3: ['toothbrush', 'battery', 'speaker'],
    4: ['snow', 'needle'],
    5: [],
    6: ['whistle', 'shorts', 'plane', 'plate'],
    7: ['car'],
    8: ['cow', 'watch', 'microwave', 'frame', 'lion'],
    9: ['chair', 'crown', 'octopus', 'rocket'],
    10: ['pants', 'doll', 'tree', 'shoes', 'puzzle'],
    11: ['boot'],
    12: ['lock', 'starfish', 'phone', 'cat'],
    13: ['horn', 'clock', 'flute', 'freezer', 'bird']
}

# Replace the boot with the drum in Box 11.
boxes[11].remove('boot')
boxes[11].append('drum')

# Replace the microscope with the thunder in Box 1.
boxes[1].remove('microscope')
boxes[1].append('thunder')

# Swap the starfish in Box 12 with the battery in Box 3.
boxes[12].remove('starfish')
boxes[3].remove('battery')
boxes[12].append('battery')
boxes[3].append('starfish')

# Put the octopus and the blanket into Box 13.
boxes[13].append('octopus')
boxes[13].append('blanket')

# Move the plane and the whistle from Box 6 to Box 4.
boxes[6].remove('plane')
boxes[6].remove('whistle')
boxes[4].append('plane')
boxes[4].append('whistle')

# Move the watch from Box 8 to Box 9.
boxes[8].remove('watch')
boxes[9].append('watch')

# Move the octopus from Box 13 to Box 7.
boxes[13].remove('octopus')
boxes[7].append('octopus')

# Move the drum from Box 11 to Box 1.
boxes[11].remove('drum')
boxes[1].append('drum')

# Move the thunder from Box 2 to Box 1.
boxes[2].remove('thunder')
boxes[1].append('thunder')

# Replace the thunder and the drum with the mixer and the rock in Box 1.
boxes[1].remove('thunder')
boxes[1].remove('drum')
boxes[1].append('mixer')
boxes[1].append('rock')

# Swap the rock in Box 1 with the watch in Box 9.
boxes[1].remove('rock')
boxes[9].remove('watch')
boxes[1].append('watch')
boxes[9].append('rock')

# Remove the bird from Box 13.
boxes[13].remove('bird')

# Move the shorts and the plate from Box 6 to Box 5.
boxes[6].remove('shorts')
boxes[6].remove('plate')
boxes[5].append('shorts')
boxes[5].append('plate')

# Move the horn from Box 13 to Box 10.
boxes[13].remove('horn')
boxes[10].append('horn')

# Replace the tape with the toaster in Box 2.
boxes[2].remove('tape')
boxes[2].append('toaster')

# Swap the crown in Box 9 with the car in Box 7.
boxes[9].remove('crown')
boxes[7].remove('car')
boxes[9].append('car')
boxes[7].append('crown')

# Swap the freezer in Box 13 with the plane in Box 4.
boxes[13].remove('freezer')
boxes[4].remove('plane')
boxes[13].append('plane')
boxes[4].append('freezer')

# Move the octopus and the crown from Box 7 to Box 13.
boxes[7].remove('octopus')
boxes[7].remove('crown')
boxes[13].append('octopus')
boxes[13].append('crown')

# Put the octopus into Box 4.
boxes[4].append('octopus')

# Put the earring and the necklace and the speaker into Box 6.
boxes[6].append('earring')
boxes[6].append('necklace')
boxes[6].append('speaker')

# Remove the toaster from Box 2.
boxes[2].remove('toaster')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")