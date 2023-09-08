# Initial state of boxes
boxes = {
    0: ['fish', 'wire', 'jungle', 'scarf'],
    1: ['table', 'needle', 'boot', 'tie'],
    2: ['sandals', 'pen', 'magnet', 'spoon'],
    3: ['freezer', 'motorcycle', 'submarine', 'perfume', 'bracelet'],
    4: ['pan', 'coat'],
    5: ['horse', 'cloud', 'storm'],
    6: ['rocket'],
    7: [],
    8: ['elephant', 'cup', 'shark'],
    9: [],
    10: [],
    11: ['lion', 'mountain', 'thread', 'snow', 'oven']
}

# Remove the cloud from Box 5.
boxes[5].remove('cloud')

# Move the coat and the pan from Box 4 to Box 8.
items_to_move = ['coat', 'pan']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[8].append(item)

# Put the bracelet into Box 11.
boxes[11].append('bracelet')

# Replace the coat and the elephant and the cup with the charger and the thunder and the bell in Box 8.
boxes[8].remove('coat')
boxes[8].remove('elephant')
boxes[8].remove('cup')
boxes[8].append('charger')
boxes[8].append('thunder')
boxes[8].append('bell')

# Remove the pan and the thunder from Box 8.
boxes[8].remove('pan')
boxes[8].remove('thunder')

# Replace the storm with the microwave in Box 5.
boxes[5].remove('storm')
boxes[5].append('microwave')

# Replace the motorcycle with the tape in Box 3.
boxes[3].remove('motorcycle')
boxes[3].append('tape')

# Replace the rocket with the clock in Box 6.
boxes[6].remove('rocket')
boxes[6].append('clock')

# Swap the charger in Box 8 with the horse in Box 5.
boxes[8].remove('charger')
boxes[5].remove('horse')
boxes[8].append('horse')
boxes[5].append('charger')

# Move the thread and the lion and the bracelet from Box 11 to Box 2.
items_to_move = ['thread', 'lion', 'bracelet']
for item in items_to_move:
    boxes[11].remove(item)
    boxes[2].append(item)

# Remove the table and the boot from Box 1.
boxes[1].remove('table')
boxes[1].remove('boot')

# Remove the oven and the mountain and the snow from Box 11.
items_to_remove = ['oven', 'mountain', 'snow']
for item in items_to_remove:
    boxes[11].remove(item)

# Swap the sandals in Box 2 with the charger in Box 5.
boxes[2].remove('sandals')
boxes[5].remove('charger')
boxes[2].append('charger')
boxes[5].append('sandals')

# Swap the pen in Box 2 with the tape in Box 3.
boxes[2].remove('pen')
boxes[3].remove('tape')
boxes[2].append('tape')
boxes[3].append('pen')

# Replace the tie and the needle with the bus and the mask in Box 1.
boxes[1].remove('tie')
boxes[1].remove('needle')
boxes[1].append('bus')
boxes[1].append('mask')

# Replace the bracelet and the perfume and the submarine with the cup and the whistle and the skirt in Box 3.
boxes[3].remove('bracelet')
boxes[3].remove('perfume')
boxes[3].remove('submarine')
boxes[3].append('cup')
boxes[3].append('whistle')
boxes[3].append('skirt')

# Swap the mask in Box 1 with the skirt in Box 3.
boxes[1].remove('mask')
boxes[3].remove('skirt')
boxes[1].append('skirt')
boxes[3].append('mask')

# Move the shark and the bell from Box 8 to Box 10.
boxes[8].remove('shark')
boxes[8].remove('bell')
boxes[10].append('shark')
boxes[10].append('bell')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")