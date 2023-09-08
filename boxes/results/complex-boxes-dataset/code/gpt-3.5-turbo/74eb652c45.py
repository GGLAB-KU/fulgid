# Initial state of boxes
boxes = {
    0: ['laptop'],
    1: ['spoon', 'grinder', 'bird', 'forest'],
    2: ['coat', 'shampoo', 'puzzle', 'ring', 'toothbrush'],
    3: ['fish', 'doll', 'toy', 'towel', 'wire'],
    4: ['tiger', 'sandals', 'coin'],
    5: [],
    6: ['belt', 'watch'],
    7: ['elephant', 'snow', 'rain'],
    8: ['perfume', 'brush', 'mixer'],
    9: ['whistle', 'flute', 'vase', 'branch'],
    10: [],
    11: ['speaker', 'frame', 'tape'],
    12: ['controller'],
    13: ['candle', 'microwave', 'soap'],
    14: ['oven']
}

# Move the controller from Box 12 to Box 10.
boxes[12].remove('controller')
boxes[10].append('controller')

# Swap the forest in Box 1 with the oven in Box 14.
boxes[1].remove('forest')
boxes[14].remove('oven')
boxes[1].append('oven')
boxes[14].append('forest')

# Move the controller from Box 10 to Box 3.
boxes[10].remove('controller')
boxes[3].append('controller')

# Replace the elephant and the rain with the puzzle and the apple in Box 7.
boxes[7].remove('elephant')
boxes[7].remove('rain')
boxes[7].append('puzzle')
boxes[7].append('apple')

# Remove the belt and the watch from Box 6.
boxes[6].remove('belt')
boxes[6].remove('watch')

# Put the shorts into Box 14.
boxes[14].append('shorts')

# Move the laptop from Box 0 to Box 11.
boxes[0].remove('laptop')
boxes[11].append('laptop')

# Empty Box 3.
boxes[3] = []

# Swap the sandals in Box 4 with the perfume in Box 8.
boxes[4].remove('sandals')
boxes[8].remove('perfume')
boxes[4].append('perfume')
boxes[8].append('sandals')

# Empty Box 9.
boxes[9] = []

# Move the mixer from Box 8 to Box 13.
boxes[8].remove('mixer')
boxes[13].append('mixer')

# Move the sandals and the brush from Box 8 to Box 3.
items_to_move = ['sandals', 'brush']
for item in items_to_move:
    boxes[8].remove(item)
    boxes[3].append(item)

# Swap the frame in Box 11 with the tiger in Box 4.
boxes[11].remove('frame')
boxes[4].remove('tiger')
boxes[11].append('tiger')
boxes[4].append('frame')

# Swap the brush in Box 3 with the spoon in Box 1.
boxes[3].remove('brush')
boxes[1].remove('spoon')
boxes[3].append('spoon')
boxes[1].append('brush')

# Remove the shampoo and the ring and the coat from Box 2.
items_to_remove = ['shampoo', 'ring', 'coat']
for item in items_to_remove:
    boxes[2].remove(item)

# Swap the toothbrush in Box 2 with the sandals in Box 3.
boxes[2].remove('toothbrush')
boxes[3].remove('sandals')
boxes[2].append('sandals')
boxes[3].append('toothbrush')

# Swap the frame in Box 4 with the oven in Box 1.
boxes[4].remove('frame')
boxes[1].remove('oven')
boxes[4].append('oven')
boxes[1].append('frame')

# Move the grinder from Box 1 to Box 12.
boxes[1].remove('grinder')
boxes[12].append('grinder')

# Put the dress and the towel and the candle into Box 0.
items_to_move = ['dress', 'towel', 'candle']
for item in items_to_move:
    boxes[0].append(item)

# Put the starfish into Box 4.
boxes[4].append('starfish')

# Replace the shorts with the harmonica in Box 14.
boxes[14].remove('shorts')
boxes[14].append('harmonica')

# Move the frame and the bird from Box 1 to Box 2.
boxes[1].remove('frame')
boxes[1].remove('bird')
boxes[2].append('frame')
boxes[2].append('bird')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")