# Initial state of boxes
boxes = {
    0: ['table', 'dress', 'card'],
    1: ['sculpture'],
    2: ['tape', 'fridge', 'oven'],
    3: [],
    4: [],
    5: ['toaster', 'cup', 'violin', 'ship', 'bell'],
    6: ['island', 'cow', 'speaker'],
    7: ['toothpaste', 'dog'],
    8: ['soap', 'towel', 'glove'],
    9: ['branch'],
    10: ['coral', 'camera']
}

# Remove the table and the card and the dress from Box 0.
items_to_remove = ['table', 'card', 'dress']
for item in items_to_remove:
    boxes[0].remove(item)

# Move the toothpaste from Box 7 to Box 8.
boxes[7].remove('toothpaste')
boxes[8].append('toothpaste')

# Put the belt and the sun into Box 3.
boxes[3].append('belt')
boxes[3].append('sun')

# Move the branch from Box 9 to Box 6.
boxes[9].remove('branch')
boxes[6].append('branch')

# Remove the toothpaste and the glove from Box 8.
boxes[8].remove('toothpaste')
boxes[8].remove('glove')

# Put the coin and the glove and the helmet into Box 7.
boxes[7].append('coin')
boxes[7].append('glove')
boxes[7].append('helmet')

# Swap the fridge in Box 2 with the cup in Box 5.
boxes[2].remove('fridge')
boxes[5].remove('cup')
boxes[2].append('cup')
boxes[5].append('fridge')

# Move the camera from Box 10 to Box 7.
boxes[10].remove('camera')
boxes[7].append('camera')

# Put the mixer into Box 6.
boxes[6].append('mixer')

# Put the glove and the leaf and the river into Box 9.
boxes[9].append('glove')
boxes[9].append('leaf')
boxes[9].append('river')

# Replace the camera and the dog with the piano and the keyboard in Box 7.
boxes[7].remove('camera')
boxes[7].remove('dog')
boxes[7].append('piano')
boxes[7].append('keyboard')

# Remove the towel and the soap from Box 8.
boxes[8].remove('towel')
boxes[8].remove('soap')

# Move the helmet and the coin and the glove from Box 7 to Box 1.
items_to_move = ['helmet', 'coin', 'glove']
for item in items_to_move:
    boxes[7].remove(item)
    boxes[1].append(item)

# Move the coral from Box 10 to Box 6.
boxes[10].remove('coral')
boxes[6].append('coral')

# Remove the glove and the leaf from Box 9.
boxes[9].remove('glove')
boxes[9].remove('leaf')

# Put the glove into Box 6.
boxes[6].append('glove')

# Remove the river from Box 9.
boxes[9].remove('river')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")