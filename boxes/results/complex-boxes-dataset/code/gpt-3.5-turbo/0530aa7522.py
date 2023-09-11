# Initial state of boxes
boxes = {
    0: ['sculpture', 'key'],
    1: ['motorcycle', 'card', 'toy', 'phone', 'seaweed'],
    2: [],
    3: ['headphone', 'bell', 'tie', 'zipper', 'snow'],
    4: ['lightning', 'crown', 'sandals'],
    5: ['soap', 'brush'],
    6: ['harmonica', 'glove', 'microscope'],
    7: ['pan', 'controller', 'lamp'],
    8: ['octopus', 'sun', 'perfume'],
    9: ['bicycle', 'gloves', 'fish', 'pillow'],
    10: ['scissors', 'wallet']
}

# Move the fish from Box 9 to Box 3.
boxes[9].remove('fish')
boxes[3].append('fish')

# Put the polish and the battery into Box 10.
boxes[10].append('polish')
boxes[10].append('battery')

# Replace the bicycle with the truck in Box 9.
boxes[9].remove('bicycle')
boxes[9].append('truck')

# Move the truck and the gloves from Box 9 to Box 5.
boxes[9].remove('truck')
boxes[9].remove('gloves')
boxes[5].append('truck')
boxes[5].append('gloves')

# Swap the sculpture in Box 0 with the truck in Box 5.
boxes[0].remove('sculpture')
boxes[5].remove('truck')
boxes[0].append('truck')
boxes[5].append('sculpture')

# Replace the pillow with the train in Box 9.
boxes[9].remove('pillow')
boxes[9].append('train')

# Replace the snow and the tie and the zipper with the rain and the swimsuit and the chair in Box 3.
boxes[3].remove('snow')
boxes[3].remove('tie')
boxes[3].remove('zipper')
boxes[3].append('rain')
boxes[3].append('swimsuit')
boxes[3].append('chair')

# Replace the soap and the gloves and the sculpture with the helmet and the towel and the comet in Box 5.
boxes[5].remove('soap')
boxes[5].remove('gloves')
boxes[5].remove('sculpture')
boxes[5].append('helmet')
boxes[5].append('towel')
boxes[5].append('comet')

# Replace the crown with the mirror in Box 4.
boxes[4].remove('crown')
boxes[4].append('mirror')

# Put the ship into Box 6.
boxes[6].append('ship')

# Put the shirt and the scarf and the usb into Box 6.
boxes[6].append('shirt')
boxes[6].append('scarf')
boxes[6].append('usb')

# Swap the lightning in Box 4 with the motorcycle in Box 1.
boxes[4].remove('lightning')
boxes[1].remove('motorcycle')
boxes[4].append('motorcycle')
boxes[1].append('lightning')

# Remove the sun and the perfume and the octopus from Box 8.
boxes[8].remove('sun')
boxes[8].remove('perfume')
boxes[8].remove('octopus')

# Put the soap and the key and the sandals into Box 6.
boxes[6].append('soap')
boxes[6].append('key')
boxes[6].append('sandals')

# Swap the train in Box 9 with the comet in Box 5.
boxes[9].remove('train')
boxes[5].remove('comet')
boxes[9].append('comet')
boxes[5].append('train')

# Swap the motorcycle in Box 4 with the truck in Box 0.
boxes[4].remove('motorcycle')
boxes[0].remove('truck')
boxes[4].append('truck')
boxes[0].append('motorcycle')

# Swap the key in Box 0 with the wallet in Box 10.
boxes[0].remove('key')
boxes[10].remove('wallet')
boxes[0].append('wallet')
boxes[10].append('key')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")