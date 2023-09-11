# Initial state of boxes
boxes = {
    0: ['blanket', 'glove', 'wire', 'motorcycle', 'boot'],
    1: ['glasses', 'skirt', 'cat'],
    2: ['thread', 'battery', 'fish', 'storm', 'sock'],
    3: ['card', 'helmet', 'comet'],
    4: ['key', 'starfish'],
    5: ['toothbrush'],
    6: ['star', 'lock', 'shelf', 'shampoo'],
    7: [],
    8: ['plate'],
    9: ['bracelet', 'dolphin'],
    10: ['oven']
}

# Move the dolphin and the bracelet from Box 9 to Box 7.
boxes[9].remove('dolphin')
boxes[9].remove('bracelet')
boxes[7].append('dolphin')
boxes[7].append('bracelet')

# Remove the oven from Box 10.
boxes[10].remove('oven')

# Move the comet and the helmet and the card from Box 3 to Box 4.
items_to_move = ['comet', 'helmet', 'card']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[4].append(item)

# Put the pants and the thunder into Box 7.
boxes[7].append('pants')
boxes[7].append('thunder')

# Empty Box 4.
boxes[4] = []

# Move the plate from Box 8 to Box 6.
boxes[8].remove('plate')
boxes[6].append('plate')

# Move the bracelet from Box 7 to Box 1.
boxes[7].remove('bracelet')
boxes[1].append('bracelet')

# Remove the glasses and the bracelet and the skirt from Box 1.
items_to_remove = ['glasses', 'bracelet', 'skirt']
for item in items_to_remove:
    boxes[1].remove(item)

# Put the telescope and the magnet and the earring into Box 2.
items_to_put = ['telescope', 'magnet', 'earring']
for item in items_to_put:
    boxes[2].append(item)

# Move the toothbrush from Box 5 to Box 4.
boxes[5].remove('toothbrush')
boxes[4].append('toothbrush')

# Replace the toothbrush with the bell in Box 4.
boxes[4].remove('toothbrush')
boxes[4].append('bell')

# Put the clock and the pot and the thread into Box 2.
items_to_put = ['clock', 'pot', 'thread']
for item in items_to_put:
    boxes[2].append(item)

# Move the pants and the thunder from Box 7 to Box 5.
boxes[7].remove('pants')
boxes[7].remove('thunder')
boxes[5].append('pants')
boxes[5].append('thunder')

# Replace the bell with the towel in Box 4.
boxes[4].remove('bell')
boxes[4].append('towel')

# Swap the dolphin in Box 7 with the towel in Box 4.
boxes[7].remove('dolphin')
boxes[4].remove('towel')
boxes[7].append('towel')
boxes[4].append('dolphin')

# Replace the cat with the boot in Box 1.
boxes[1].remove('cat')
boxes[1].append('boot')

# Replace the storm and the telescope and the clock with the sculpture and the tape and the horn in Box 2.
boxes[2].remove('storm')
boxes[2].remove('telescope')
boxes[2].remove('clock')
boxes[2].append('sculpture')
boxes[2].append('tape')
boxes[2].append('horn')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")