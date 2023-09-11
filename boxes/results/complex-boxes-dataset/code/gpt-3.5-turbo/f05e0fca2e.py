# Initial state of boxes
boxes = {
    0: [],
    1: ['hat'],
    2: [],
    3: ['bus', 'snow', 'bear', 'ship'],
    4: ['book', 'thunder', 'cup'],
    5: ['makeup', 'violin', 'console', 'wallet'],
    6: ['planet', 'helmet'],
    7: ['usb', 'note', 'shark', 'freezer'],
    8: ['leaf', 'star', 'plane', 'ocean'],
    9: ['seaweed', 'mountain', 'needle', 'dolphin', 'lipstick'],
    10: ['island', 'magnet']
}

# Swap the hat in Box 1 with the helmet in Box 6.
boxes[1].remove('hat')
boxes[6].remove('helmet')
boxes[1].append('helmet')
boxes[6].append('hat')

# Move the bus from Box 3 to Box 4.
boxes[3].remove('bus')
boxes[4].append('bus')

# Put the card into Box 4.
boxes[4].append('card')

# Put the doll into Box 2.
boxes[2].append('doll')

# Replace the bear and the snow and the ship with the skirt and the perfume and the shelf in Box 3.
boxes[3].remove('bear')
boxes[3].remove('snow')
boxes[3].remove('ship')
boxes[3].append('skirt')
boxes[3].append('perfume')
boxes[3].append('shelf')

# Replace the plane and the ocean with the mask and the boot in Box 8.
boxes[8].remove('plane')
boxes[8].remove('ocean')
boxes[8].append('mask')
boxes[8].append('boot')

# Remove the doll from Box 2.
boxes[2].remove('doll')

# Swap the planet in Box 6 with the seaweed in Box 9.
boxes[6].remove('planet')
boxes[9].remove('seaweed')
boxes[6].append('seaweed')
boxes[9].append('planet')

# Remove the thunder from Box 4.
boxes[4].remove('thunder')

# Swap the note in Box 7 with the mask in Box 8.
boxes[7].remove('note')
boxes[8].remove('mask')
boxes[7].append('mask')
boxes[8].append('note')

# Move the star from Box 8 to Box 9.
boxes[8].remove('star')
boxes[9].append('star')

# Swap the bus in Box 4 with the seaweed in Box 6.
boxes[4].remove('bus')
boxes[6].remove('seaweed')
boxes[4].append('seaweed')
boxes[6].append('bus')

# Remove the makeup and the console and the violin from Box 5.
items_to_remove = ['makeup', 'console', 'violin']
for item in items_to_remove:
    boxes[5].remove(item)

# Remove the magnet and the island from Box 10.
boxes[10].remove('magnet')
boxes[10].remove('island')

# Swap the helmet in Box 1 with the book in Box 4.
boxes[1].remove('helmet')
boxes[4].remove('book')
boxes[1].append('book')
boxes[4].append('helmet')

# Move the boot and the leaf from Box 8 to Box 5.
boxes[8].remove('boot')
boxes[8].remove('leaf')
boxes[5].append('boot')
boxes[5].append('leaf')

# Remove the dolphin and the planet from Box 9.
boxes[9].remove('dolphin')
boxes[9].remove('planet')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")