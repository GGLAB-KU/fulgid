# Initial state of boxes
boxes = {
    0: ['star', 'mixer'],
    1: [],
    2: [],
    3: ['toothbrush', 'lightning', 'freezer', 'gloves'],
    4: [],
    5: ['shampoo', 'bird'],
    6: ['horse'],
    7: ['harmonica', 'helmet', 'shoes', 'apple'],
    8: ['razor', 'comb', 'controller']
}

# Put the belt and the oven and the bell into Box 1.
items_to_put = ['belt', 'oven', 'bell']
for item in items_to_put:
    boxes[1].append(item)

# Replace the star with the coin in Box 0.
boxes[0].remove('star')
boxes[0].append('coin')

# Remove the bell from Box 1.
boxes[1].remove('bell')

# Put the lamp and the forest and the fridge into Box 1.
items_to_put = ['lamp', 'forest', 'fridge']
for item in items_to_put:
    boxes[1].append(item)

# Swap the mixer in Box 0 with the shampoo in Box 5.
boxes[0].remove('mixer')
boxes[5].remove('shampoo')
boxes[0].append('shampoo')
boxes[5].append('mixer')

# Move the shoes from Box 7 to Box 3.
boxes[7].remove('shoes')
boxes[3].append('shoes')

# Remove the shampoo and the coin from Box 0.
boxes[0].remove('shampoo')
boxes[0].remove('coin')

# Swap the helmet in Box 7 with the horse in Box 6.
boxes[7].remove('helmet')
boxes[6].remove('horse')
boxes[7].append('horse')
boxes[6].append('helmet')

# Move the apple and the harmonica from Box 7 to Box 5.
boxes[7].remove('apple')
boxes[7].remove('harmonica')
boxes[5].append('apple')
boxes[5].append('harmonica')

# Empty Box 3.
boxes[3] = []

# Replace the helmet with the shorts in Box 6.
boxes[6].remove('helmet')
boxes[6].append('shorts')

# Remove the horse from Box 7.
boxes[7].remove('horse')

# Move the shorts from Box 6 to Box 0.
boxes[6].remove('shorts')
boxes[0].append('shorts')

# Put the flute and the clock and the drum into Box 4.
items_to_put = ['flute', 'clock', 'drum']
for item in items_to_put:
    boxes[4].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")