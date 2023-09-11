# Initial state of boxes
boxes = {
    0: [],
    1: ['thread', 'usb', 'comet'],
    2: ['perfume'],
    3: ['game', 'planet', 'phone', 'leaf'],
    4: ['bear']
}

# Empty Box 4
boxes[4] = []

# Move the leaf and the game and the planet from Box 3 to Box 4
items_to_move = ['leaf', 'game', 'planet']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[4].append(item)

# Put the car and the pot and the star into Box 3
items_to_add = ['car', 'pot', 'star']
for item in items_to_add:
    boxes[3].append(item)

# Move the perfume from Box 2 to Box 1
boxes[2].remove('perfume')
boxes[1].append('perfume')

# Replace the car and the phone and the star with the pan and the bicycle and the brush in Box 3
items_to_remove = ['car', 'phone', 'star']
items_to_add = ['pan', 'bicycle', 'brush']
for item in items_to_remove:
    boxes[3].remove(item)
for item in items_to_add:
    boxes[3].append(item)

# Move the usb and the perfume and the comet from Box 1 to Box 2
items_to_move = ['usb', 'perfume', 'comet']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[2].append(item)

# Move the brush and the pan and the bicycle from Box 3 to Box 0
items_to_move = ['brush', 'pan', 'bicycle']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[0].append(item)

# Move the pan and the brush and the bicycle from Box 0 to Box 3
items_to_move = ['pan', 'brush', 'bicycle']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[3].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")