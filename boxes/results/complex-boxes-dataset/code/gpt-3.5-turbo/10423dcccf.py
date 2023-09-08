# Initial state of boxes
boxes = {
    0: ['camera', 'candle', 'zipper', 'basket'],
    1: ['helmet', 'needle', 'truck'],
    2: ['glove', 'bus'],
    3: ['blanket'],
    4: ['razor', 'horse', 'grass'],
    5: ['fork', 'spoon', 'coat', 'mask'],
    6: ['bear', 'shoes'],
    7: ['makeup'],
    8: []
}

# Put the toy and the submarine into Box 5.
boxes[5].append('toy')
boxes[5].append('submarine')

# Remove the helmet from Box 1.
boxes[1].remove('helmet')

# Put the toy and the desert into Box 8.
boxes[8].append('toy')
boxes[8].append('desert')

# Swap the submarine in Box 5 with the zipper in Box 0.
boxes[0].remove('zipper')
boxes[5].remove('submarine')
boxes[0].append('submarine')
boxes[5].append('zipper')

# Put the shoes and the shark into Box 4.
boxes[4].append('shoes')
boxes[4].append('shark')

# Put the shelf and the soap and the seaweed into Box 4.
boxes[4].append('shelf')
boxes[4].append('soap')
boxes[4].append('seaweed')

# Remove the grass and the seaweed from Box 4.
boxes[4].remove('grass')
boxes[4].remove('seaweed')

# Put the leaf and the shark and the chair into Box 2.
boxes[2].append('leaf')
boxes[2].append('shark')
boxes[2].append('chair')

# Remove the shoes and the shark and the soap from Box 4.
boxes[4].remove('shoes')
boxes[4].remove('shark')
boxes[4].remove('soap')

# Move the leaf from Box 2 to Box 0.
boxes[2].remove('leaf')
boxes[0].append('leaf')

# Replace the shelf with the lamp in Box 4.
boxes[4].remove('shelf')
boxes[4].append('lamp')

# Remove the shoes from Box 6.
boxes[6].remove('shoes')

# Move the fork and the coat and the zipper from Box 5 to Box 3.
items_to_move = ['fork', 'coat', 'zipper']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[3].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")