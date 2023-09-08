# Initial state of boxes
boxes = {
    0: [],
    1: ['butterfly'],
    2: ['toothpaste', 'bear', 'coin', 'ocean'],
    3: ['boat', 'glove', 'plane', 'river'],
    4: [],
    5: ['pot', 'battery', 'magnet', 'shelf', 'sock'],
    6: ['dolphin'],
    7: []
}

# Replace the butterfly with the speaker in Box 1.
boxes[1].remove('butterfly')
boxes[1].append('speaker')

# Move the dolphin from Box 6 to Box 0.
boxes[6].remove('dolphin')
boxes[0].append('dolphin')

# Swap the shelf in Box 5 with the plane in Box 3.
boxes[5].remove('shelf')
boxes[3].remove('plane')
boxes[5].append('plane')
boxes[3].append('shelf')

# Replace the ocean and the coin with the cow and the moon in Box 2.
boxes[2].remove('ocean')
boxes[2].remove('coin')
boxes[2].append('cow')
boxes[2].append('moon')

# Replace the boat with the glove in Box 3.
boxes[3].remove('boat')
boxes[3].append('glove')

# Put the chair and the telescope into Box 1.
boxes[1].append('chair')
boxes[1].append('telescope')

# Put the coral and the tree into Box 3.
boxes[3].append('coral')
boxes[3].append('tree')

# Move the dolphin from Box 0 to Box 2.
boxes[0].remove('dolphin')
boxes[2].append('dolphin')

# Replace the magnet and the battery with the grass and the coat in Box 5.
boxes[5].remove('magnet')
boxes[5].remove('battery')
boxes[5].append('grass')
boxes[5].append('coat')

# Empty Box 3.
boxes[3] = []

# Swap the grass in Box 5 with the chair in Box 1.
boxes[5].remove('grass')
boxes[1].remove('chair')
boxes[5].append('chair')
boxes[1].append('grass')

# Remove the plane and the chair and the sock from Box 5.
items_to_remove = ['plane', 'chair', 'sock']
for item in items_to_remove:
    boxes[5].remove(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")