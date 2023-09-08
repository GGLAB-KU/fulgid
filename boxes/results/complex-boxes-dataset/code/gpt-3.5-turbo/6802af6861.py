# Initial state of boxes
boxes = {
    0: ['keyboard', 'plate'],
    1: ['dog', 'forest', 'pen'],
    2: ['tiger', 'toaster', 'razor', 'shoe'],
    3: ['oven', 'hat', 'branch'],
    4: ['jacket', 'lock']
}

# Move the hat from Box 3 to Box 1.
boxes[3].remove('hat')
boxes[1].append('hat')

# Replace the branch and the oven with the toaster and the key in Box 3.
boxes[3].remove('branch')
boxes[3].remove('oven')
boxes[3].append('toaster')
boxes[3].append('key')

# Move the dog and the pen and the hat from Box 1 to Box 3.
items_to_move = ['dog', 'pen', 'hat']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[3].append(item)

# Put the swimsuit and the table into Box 2.
boxes[2].append('swimsuit')
boxes[2].append('table')

# Replace the jacket with the grass in Box 4.
boxes[4].remove('jacket')
boxes[4].append('grass')

# Remove the forest from Box 1.
boxes[1].remove('forest')

# Replace the dog and the pen and the key with the guitar and the scissors and the submarine in Box 3.
boxes[3].remove('dog')
boxes[3].remove('pen')
boxes[3].remove('key')
boxes[3].append('guitar')
boxes[3].append('scissors')
boxes[3].append('submarine')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")