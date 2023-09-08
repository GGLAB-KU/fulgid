# Initial state of boxes
boxes = {
    0: ['towel', 'mixer', 'pen'],
    1: ['speaker', 'lightning', 'battery', 'soap', 'shorts'],
    2: [],
    3: ['basket', 'button', 'charger', 'plane', 'elephant'],
    4: ['makeup', 'belt'],
    5: [],
    6: [],
    7: ['coral', 'bag', 'boat', 'chair'],
    8: ['branch', 'dress', 'flower'],
    9: ['bus', 'lock', 'note', 'vase'],
    10: ['blanket', 'sun', 'desert'],
    11: ['bird', 'spoon', 'shark', 'microwave', 'pan']
}

# Swap the belt in Box 4 with the note in Box 9.
boxes[4].remove('belt')
boxes[9].remove('note')
boxes[4].append('note')
boxes[9].append('belt')

# Put the controller into Box 3.
boxes[3].append('controller')

# Move the lock from Box 9 to Box 3.
boxes[9].remove('lock')
boxes[3].append('lock')

# Put the star into Box 0.
boxes[0].append('star')

# Move the desert and the blanket and the sun from Box 10 to Box 8.
items_to_move = ['desert', 'blanket', 'sun']
for item in items_to_move:
    boxes[10].remove(item)
    boxes[8].append(item)

# Swap the pan in Box 11 with the bus in Box 9.
boxes[11].remove('pan')
boxes[9].remove('bus')
boxes[11].append('bus')
boxes[9].append('pan')

# Put the helmet and the pants into Box 3.
boxes[3].append('helmet')
boxes[3].append('pants')

# Remove the elephant and the pants and the controller from Box 3.
items_to_remove = ['elephant', 'pants', 'controller']
for item in items_to_remove:
    boxes[3].remove(item)

# Replace the chair and the coral and the boat with the tree and the skirt and the cup in Box 7.
boxes[7].remove('chair')
boxes[7].remove('coral')
boxes[7].remove('boat')
boxes[7].append('tree')
boxes[7].append('skirt')
boxes[7].append('cup')

# Swap the branch in Box 8 with the pan in Box 9.
boxes[8].remove('branch')
boxes[9].remove('pan')
boxes[8].append('pan')
boxes[9].append('branch')

# Move the makeup and the note from Box 4 to Box 2.
items_to_move = ['makeup', 'note']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[2].append(item)

# Replace the star and the pen and the mixer with the horn and the dog and the hat in Box 0.
boxes[0].remove('star')
boxes[0].remove('pen')
boxes[0].remove('mixer')
boxes[0].append('horn')
boxes[0].append('dog')
boxes[0].append('hat')

# Replace the pan and the sun with the gloves and the zipper in Box 8.
boxes[8].remove('pan')
boxes[8].remove('sun')
boxes[8].append('gloves')
boxes[8].append('zipper')

# Remove the zipper and the desert from Box 8.
boxes[8].remove('zipper')
boxes[8].remove('desert')

# Remove the makeup and the note from Box 2.
boxes[2].remove('makeup')
boxes[2].remove('note')

# Remove the cup and the tree and the skirt from Box 7.
boxes[7].remove('cup')
boxes[7].remove('tree')
boxes[7].remove('skirt')

# Put the shoes and the bicycle into Box 6.
boxes[6].append('shoes')
boxes[6].append('bicycle')

# Swap the spoon in Box 11 with the shorts in Box 1.
boxes[11].remove('spoon')
boxes[1].remove('shorts')
boxes[11].append('shorts')
boxes[1].append('spoon')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")