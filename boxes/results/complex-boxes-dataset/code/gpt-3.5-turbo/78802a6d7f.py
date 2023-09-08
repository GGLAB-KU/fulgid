# Initial state of boxes
boxes = {
    0: ['lamp', 'clock', 'tiger', 'headphone'],
    1: ['brush'],
    2: ['button'],
    3: [],
    4: ['bell', 'zipper', 'toothpaste', 'microwave'],
    5: ['lightning']
}

# Swap the brush in Box 1 with the zipper in Box 4.
boxes[1].remove('brush')
boxes[4].remove('zipper')
boxes[1].append('zipper')
boxes[4].append('brush')

# Move the tiger and the headphone and the clock from Box 0 to Box 4.
items_to_move = ['tiger', 'headphone', 'clock']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[4].append(item)

# Empty Box 0.
boxes[0] = []

# Remove the button from Box 2.
boxes[2].remove('button')

# Move the zipper from Box 1 to Box 0.
boxes[1].remove('zipper')
boxes[0].append('zipper')

# Replace the lightning with the frame in Box 5.
boxes[5].remove('lightning')
boxes[5].append('frame')

# Put the controller and the razor and the sculpture into Box 3.
items_to_move = ['controller', 'razor', 'sculpture']
for item in items_to_move:
    boxes[3].append(item)

# Swap the zipper in Box 0 with the brush in Box 4.
boxes[0].remove('zipper')
boxes[4].remove('brush')
boxes[0].append('brush')
boxes[4].append('zipper')

# Move the tiger and the bell from Box 4 to Box 5.
items_to_move = ['tiger', 'bell']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[5].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")