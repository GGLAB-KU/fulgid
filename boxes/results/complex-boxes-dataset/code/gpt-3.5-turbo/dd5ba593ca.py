# Initial state of boxes
boxes = {
    0: ['comb', 'puzzle', 'sock', 'boat', 'glasses'],
    1: ['chair', 'dog'],
    2: ['razor', 'fork', 'controller'],
    3: ['scarf', 'star', 'gloves', 'forest'],
    4: ['soap', 'ship', 'pillow'],
    5: [],
    6: ['bowl', 'butterfly', 'clock'],
    7: ['charger', 'violin'],
    8: [],
    9: ['umbrella', 'ring'],
    10: [],
    11: ['branch', 'pen', 'basket', 'skirt', 'grinder'],
    12: ['tie']
}

# Remove the scarf from Box 3.
boxes[3].remove('scarf')

# Swap the violin in Box 7 with the controller in Box 2.
boxes[7].remove('violin')
boxes[2].remove('controller')
boxes[7].append('controller')
boxes[2].append('violin')

# Empty Box 6.
boxes[6] = []

# Replace the fork with the pillow in Box 2.
boxes[2].remove('fork')
boxes[2].append('pillow')

# Put the cow and the usb and the candle into Box 0.
items_to_put = ['cow', 'usb', 'candle']
for item in items_to_put:
    boxes[0].append(item)

# Move the ship and the soap from Box 4 to Box 6.
items_to_move = ['ship', 'soap']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[6].append(item)

# Replace the basket and the branch with the cloud and the sun in Box 11.
boxes[11].remove('basket')
boxes[11].remove('branch')
boxes[11].append('cloud')
boxes[11].append('sun')

# Move the pillow from Box 4 to Box 0.
boxes[4].remove('pillow')
boxes[0].append('pillow')

# Swap the chair in Box 1 with the star in Box 3.
boxes[1].remove('chair')
boxes[3].remove('star')
boxes[1].append('star')
boxes[3].append('chair')

# Move the gloves and the forest from Box 3 to Box 8.
items_to_move = ['gloves', 'forest']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[8].append(item)

# Remove the ring from Box 9.
boxes[9].remove('ring')

# Swap the umbrella in Box 9 with the charger in Box 7.
boxes[9].remove('umbrella')
boxes[7].remove('charger')
boxes[9].append('charger')
boxes[7].append('umbrella')

# Swap the gloves in Box 8 with the skirt in Box 11.
boxes[8].remove('gloves')
boxes[11].remove('skirt')
boxes[8].append('skirt')
boxes[11].append('gloves')

# Move the ship and the soap from Box 6 to Box 5.
items_to_move = ['ship', 'soap']
for item in items_to_move:
    boxes[6].remove(item)
    boxes[5].append(item)

# Empty Box 12.
boxes[12] = []

# Replace the grinder with the blender in Box 11.
boxes[11].remove('grinder')
boxes[11].append('blender')

# Put the necklace and the soap and the jacket into Box 6.
items_to_put = ['necklace', 'soap', 'jacket']
for item in items_to_put:
    boxes[6].append(item)

# Put the book into Box 8.
boxes[8].append('book')

# Replace the controller and the umbrella with the jungle and the charger in Box 7.
boxes[7].remove('controller')
boxes[7].remove('umbrella')
boxes[7].append('jungle')
boxes[7].append('charger')

# Swap the dog in Box 1 with the ship in Box 5.
boxes[1].remove('dog')
boxes[5].remove('ship')
boxes[1].append('ship')
boxes[5].append('dog')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")