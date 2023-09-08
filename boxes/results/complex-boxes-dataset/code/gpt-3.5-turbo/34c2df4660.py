# Initial state of boxes
boxes = {
    0: ['razor', 'plate'],
    1: [],
    2: [],
    3: ['laptop', 'belt', 'lightning', 'puzzle', 'shelf'],
    4: [],
    5: ['bell', 'mountain', 'gloves', 'pants', 'lock']
}

# Replace the shelf and the puzzle and the laptop with the river and the tree and the dress in Box 3.
boxes[3].remove('shelf')
boxes[3].remove('puzzle')
boxes[3].remove('laptop')
boxes[3].append('river')
boxes[3].append('tree')
boxes[3].append('dress')

# Empty Box 0.
boxes[0] = []

# Put the crown and the glove and the forest into Box 5.
items_to_move = ['crown', 'glove', 'forest']
for item in items_to_move:
    boxes[5].append(item)

# Move the tree and the river and the belt from Box 3 to Box 4.
items_to_move = ['tree', 'river', 'belt']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[4].append(item)

# Move the forest and the mountain from Box 5 to Box 2.
items_to_move = ['forest', 'mountain']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[2].append(item)

# Move the river and the tree from Box 4 to Box 3.
items_to_move = ['river', 'tree']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[3].append(item)

# Replace the dress and the lightning with the makeup and the thread in Box 3.
boxes[3].remove('dress')
boxes[3].remove('lightning')
boxes[3].append('makeup')
boxes[3].append('thread')

# Swap the forest in Box 2 with the tree in Box 3.
boxes[2].remove('forest')
boxes[3].remove('tree')
boxes[2].append('tree')
boxes[3].append('forest')

# Replace the thread with the soap in Box 3.
boxes[3].remove('thread')
boxes[3].append('soap')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")