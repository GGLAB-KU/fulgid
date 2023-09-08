# Initial state of boxes
boxes = {
    0: ['camera', 'tree', 'rock', 'bag', 'pants'],
    1: ['branch', 'glove', 'thread', 'basket', 'toothbrush'],
    2: ['candle', 'brush', 'puzzle'],
    3: ['belt'],
    4: ['microscope', 'bear', 'thunder', 'perfume', 'snow'],
    5: ['storm', 'helmet'],
    6: ['pot', 'doll', 'bicycle'],
    7: ['elephant', 'phone'],
    8: ['car', 'table', 'fork'],
    9: [],
    10: ['boat', 'cloud', 'glasses'],
    11: ['comet', 'mask', 'apple', 'jacket']
}

# Swap the glove in Box 1 with the jacket in Box 11.
boxes[1].remove('glove')
boxes[11].remove('jacket')
boxes[1].append('jacket')
boxes[11].append('glove')

# Empty Box 6.
boxes[6] = []

# Remove the comet from Box 11.
boxes[11].remove('comet')

# Move the apple from Box 11 to Box 8.
boxes[11].remove('apple')
boxes[8].append('apple')

# Put the belt and the bicycle and the rocket into Box 10.
items_to_move = ['belt', 'bicycle', 'rocket']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[6].remove(item)
    boxes[10].append(item)

# Swap the brush in Box 2 with the jacket in Box 1.
boxes[2].remove('brush')
boxes[1].remove('jacket')
boxes[2].append('jacket')
boxes[1].append('brush')

# Swap the thread in Box 1 with the belt in Box 3.
boxes[1].remove('thread')
boxes[3].remove('belt')
boxes[1].append('belt')
boxes[3].append('thread')

# Move the elephant from Box 7 to Box 4.
boxes[7].remove('elephant')
boxes[4].append('elephant')

# Move the perfume and the thunder and the bear from Box 4 to Box 11.
items_to_move = ['perfume', 'thunder', 'bear']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[11].append(item)

# Remove the jacket and the candle from Box 2.
boxes[2].remove('jacket')
boxes[2].remove('candle')

# Move the boat and the belt from Box 10 to Box 2.
boxes[10].remove('boat')
boxes[10].remove('belt')
boxes[2].append('boat')
boxes[2].append('belt')

# Remove the helmet and the storm from Box 5.
boxes[5].remove('helmet')
boxes[5].remove('storm')

# Move the phone from Box 7 to Box 11.
boxes[7].remove('phone')
boxes[11].append('phone')

# Put the sock and the razor into Box 6.
boxes[6].append('sock')
boxes[6].append('razor')

# Remove the puzzle and the belt and the boat from Box 2.
boxes[2].remove('puzzle')
boxes[2].remove('belt')
boxes[2].remove('boat')

# Replace the rocket and the cloud and the glasses with the island and the puzzle and the perfume in Box 10.
boxes[10].remove('rocket')
boxes[10].remove('cloud')
boxes[10].remove('glasses')
boxes[10].append('island')
boxes[10].append('puzzle')
boxes[10].append('perfume')

# Replace the bicycle with the shorts in Box 10.
boxes[10].remove('bicycle')
boxes[10].append('shorts')

# Move the apple from Box 8 to Box 1.
boxes[8].remove('apple')
boxes[1].append('apple')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")