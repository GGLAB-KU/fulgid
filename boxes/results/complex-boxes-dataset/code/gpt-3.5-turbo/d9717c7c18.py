# Initial state of boxes
boxes = {
    0: ['piano'],
    1: ['controller'],
    2: ['sock'],
    3: [],
    4: ['mixer'],
    5: ['makeup', 'blanket', 'bicycle', 'plane', 'fork'],
    6: ['tiger'],
    7: ['zipper', 'bird', 'card', 'spoon', 'mountain'],
    8: [],
    9: ['motorcycle', 'tree', 'gloves'],
    10: ['doll'],
    11: ['thunder', 'mask'],
    12: ['earring'],
    13: ['flower', 'shark'],
    14: ['watch', 'laptop']
}

# Replace the shark with the paint in Box 13.
boxes[13].remove('shark')
boxes[13].append('paint')

# Move the controller from Box 1 to Box 3.
boxes[1].remove('controller')
boxes[3].append('controller')

# Replace the watch with the tape in Box 14.
boxes[14].remove('watch')
boxes[14].append('tape')

# Remove the zipper and the bird from Box 7.
boxes[7].remove('zipper')
boxes[7].remove('bird')

# Empty Box 4.
boxes[4] = []

# Put the swimsuit and the glove into Box 11.
boxes[11].append('swimsuit')
boxes[11].append('glove')

# Remove the piano from Box 0.
boxes[0].remove('piano')

# Remove the fork and the blanket and the bicycle from Box 5.
items_to_remove = ['fork', 'blanket', 'bicycle']
for item in items_to_remove:
    boxes[5].remove(item)

# Swap the makeup in Box 5 with the doll in Box 10.
boxes[5].remove('makeup')
boxes[10].remove('doll')
boxes[5].append('doll')
boxes[10].append('makeup')

# Replace the flower with the violin in Box 13.
boxes[13].remove('flower')
boxes[13].append('violin')

# Move the paint from Box 13 to Box 10.
boxes[13].remove('paint')
boxes[10].append('paint')

# Remove the violin from Box 13.
boxes[13].remove('violin')

# Swap the gloves in Box 9 with the tape in Box 14.
boxes[9].remove('gloves')
boxes[14].remove('tape')
boxes[9].append('tape')
boxes[14].append('gloves')

# Put the chair into Box 13.
boxes[13].append('chair')

# Remove the mountain from Box 7.
boxes[7].remove('mountain')

# Move the sock from Box 2 to Box 0.
boxes[2].remove('sock')
boxes[0].append('sock')

# Remove the gloves from Box 14.
boxes[14].remove('gloves')

# Replace the makeup with the belt in Box 10.
boxes[10].remove('makeup')
boxes[10].append('belt')

# Replace the card and the spoon with the butterfly and the basket in Box 7.
boxes[7].remove('card')
boxes[7].remove('spoon')
boxes[7].append('butterfly')
boxes[7].append('basket')

# Move the controller from Box 3 to Box 4.
boxes[3].remove('controller')
boxes[4].append('controller')

# Remove the controller from Box 4.
boxes[4].remove('controller')

# Move the butterfly from Box 7 to Box 14.
boxes[7].remove('butterfly')
boxes[14].append('butterfly')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")