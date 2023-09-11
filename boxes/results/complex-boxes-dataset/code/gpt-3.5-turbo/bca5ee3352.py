# Initial state of boxes
boxes = {
    0: ['spoon', 'elephant', 'shorts', 'laptop', 'necklace'],
    1: ['moon', 'tiger', 'shark', 'tie'],
    2: ['gloves', 'apple', 'pillow', 'sculpture', 'plane'],
    3: ['book', 'lion'],
    4: ['submarine', 'headphone', 'toy', 'forest']
}

# Move the tiger from Box 1 to Box 2.
boxes[1].remove('tiger')
boxes[2].append('tiger')

# Replace the submarine with the hat in Box 4.
boxes[4].remove('submarine')
boxes[4].append('hat')

# Move the pillow and the gloves from Box 2 to Box 3.
items_to_move = ['pillow', 'gloves']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[3].append(item)

# Remove the pillow and the lion from Box 3.
boxes[3].remove('pillow')
boxes[3].remove('lion')

# Put the toy and the shampoo into Box 3.
boxes[3].append('toy')
boxes[3].append('shampoo')

# Move the tie and the moon and the shark from Box 1 to Box 3.
items_to_move = ['tie', 'moon', 'shark']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[3].append(item)

# Put the rock and the shoe into Box 0.
boxes[0].append('rock')
boxes[0].append('shoe')

# Swap the tiger in Box 2 with the shoe in Box 0.
boxes[2].remove('tiger')
boxes[0].remove('shoe')
boxes[2].append('shoe')
boxes[0].append('tiger')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")