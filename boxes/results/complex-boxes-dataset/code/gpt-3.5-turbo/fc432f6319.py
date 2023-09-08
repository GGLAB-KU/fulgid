# Initial state of boxes
boxes = {
    0: ['coral', 'usb', 'makeup', 'rain', 'sock'],
    1: ['puzzle', 'shorts', 'lipstick'],
    2: ['umbrella', 'toothbrush'],
    3: [],
    4: ['bowl', 'scissors', 'bus', 'snow'],
    5: ['train', 'microscope', 'coin'],
    6: ['earring', 'truck', 'magnet', 'shampoo'],
    7: ['brush', 'tape', 'razor', 'charger', 'rock'],
    8: ['clock', 'freezer', 'ship'],
    9: ['cup', 'drum', 'game', 'seaweed'],
    10: ['apple', 'sculpture', 'bag', 'dress', 'gloves'],
    11: [],
    12: ['key', 'watch', 'blender', 'beach']
}

# Remove the bus and the bowl from Box 4.
boxes[4].remove('bus')
boxes[4].remove('bowl')

# Remove the rain and the sock and the coral from Box 0.
boxes[0].remove('rain')
boxes[0].remove('sock')
boxes[0].remove('coral')

# Swap the beach in Box 12 with the brush in Box 7.
boxes[12].remove('beach')
boxes[7].remove('brush')
boxes[12].append('brush')
boxes[7].append('beach')

# Move the shampoo from Box 6 to Box 8.
boxes[6].remove('shampoo')
boxes[8].append('shampoo')

# Remove the shorts and the lipstick and the puzzle from Box 1.
boxes[1].remove('shorts')
boxes[1].remove('lipstick')
boxes[1].remove('puzzle')

# Swap the apple in Box 10 with the magnet in Box 6.
boxes[10].remove('apple')
boxes[6].remove('magnet')
boxes[10].append('magnet')
boxes[6].append('apple')

# Move the gloves and the magnet from Box 10 to Box 3.
boxes[10].remove('gloves')
boxes[6].remove('magnet')
boxes[3].append('gloves')
boxes[3].append('magnet')

# Put the shoes into Box 5.
boxes[5].append('shoes')

# Put the thunder and the moon into Box 9.
boxes[9].append('thunder')
boxes[9].append('moon')

# Put the table and the thread into Box 2.
boxes[2].append('table')
boxes[2].append('thread')

# Replace the scissors with the mirror in Box 4.
boxes[4].remove('scissors')
boxes[4].append('mirror')

# Put the pillow and the spoon and the card into Box 4.
boxes[4].append('pillow')
boxes[4].append('spoon')
boxes[4].append('card')

# Swap the gloves in Box 3 with the shoes in Box 5.
boxes[3].remove('gloves')
boxes[5].remove('shoes')
boxes[3].append('shoes')
boxes[5].append('gloves')

# Put the mirror into Box 5.
boxes[5].append('mirror')

# Put the ring and the paint and the storm into Box 9.
boxes[9].append('ring')
boxes[9].append('paint')
boxes[9].append('storm')

# Remove the umbrella from Box 2.
boxes[2].remove('umbrella')

# Move the earring from Box 6 to Box 0.
boxes[6].remove('earring')
boxes[0].append('earring')

# Move the sculpture and the dress and the bag from Box 10 to Box 8.
boxes[10].remove('sculpture')
boxes[10].remove('dress')
boxes[10].remove('bag')
boxes[8].append('sculpture')
boxes[8].append('dress')
boxes[8].append('bag')

# Move the earring and the makeup from Box 0 to Box 7.
boxes[0].remove('earring')
boxes[0].remove('makeup')
boxes[7].append('earring')
boxes[7].append('makeup')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")