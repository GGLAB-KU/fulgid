# Initial state of boxes
boxes = {
    0: ['harmonica', 'boat', 'cup', 'dress'],
    1: [],
    2: ['candle', 'tie', 'sock', 'keyboard', 'puzzle'],
    3: [],
    4: [],
    5: [],
    6: ['bowl', 'river', 'mask', 'shark'],
    7: ['storm', 'pan', 'laptop'],
    8: ['cloud', 'zipper', 'microwave', 'chair', 'mountain']
}

# Move the keyboard and the sock and the tie from Box 2 to Box 0.
items_to_move = ['keyboard', 'sock', 'tie']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[0].append(item)

# Remove the candle from Box 2.
boxes[2].remove('candle')

# Move the cloud from Box 8 to Box 6.
boxes[8].remove('cloud')
boxes[6].append('cloud')

# Put the mountain and the grinder and the bell into Box 3.
items_to_move = ['mountain', 'grinder', 'bell']
for item in items_to_move:
    boxes[8].remove(item)
    boxes[3].append(item)

# Move the microwave and the zipper from Box 8 to Box 5.
items_to_move = ['microwave', 'zipper']
for item in items_to_move:
    boxes[8].remove(item)
    boxes[5].append(item)

# Remove the grinder and the bell and the mountain from Box 3.
items_to_remove = ['grinder', 'bell', 'mountain']
for item in items_to_remove:
    boxes[3].remove(item)

# Swap the pan in Box 7 with the chair in Box 8.
boxes[7].remove('pan')
boxes[8].remove('chair')
boxes[7].append('chair')
boxes[8].append('pan')

# Put the helmet and the river into Box 4.
boxes[4].append('helmet')
boxes[4].append('river')

# Move the helmet and the river from Box 4 to Box 5.
boxes[4].remove('helmet')
boxes[4].remove('river')
boxes[5].append('helmet')
boxes[5].append('river')

# Move the harmonica and the keyboard from Box 0 to Box 5.
boxes[0].remove('harmonica')
boxes[0].remove('keyboard')
boxes[5].append('harmonica')
boxes[5].append('keyboard')

# Remove the boat and the cup and the dress from Box 0.
items_to_remove = ['boat', 'cup', 'dress']
for item in items_to_remove:
    boxes[0].remove(item)

# Move the helmet and the keyboard and the river from Box 5 to Box 1.
boxes[5].remove('helmet')
boxes[5].remove('keyboard')
boxes[5].remove('river')
boxes[1].append('helmet')
boxes[1].append('keyboard')
boxes[1].append('river')

# Put the branch into Box 2.
boxes[2].append('branch')

# Put the shirt and the charger into Box 8.
boxes[8].append('shirt')
boxes[8].append('charger')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")