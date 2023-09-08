# Initial state of boxes
boxes = {
    0: ['camera'],
    1: ['phone', 'brush', 'tiger', 'fork', 'dress'],
    2: ['keyboard', 'desert'],
    3: ['planet', 'basket'],
    4: ['shirt', 'snow']
}

# Swap the dress in Box 1 with the desert in Box 2.
boxes[1].remove('dress')
boxes[2].remove('desert')
boxes[1].append('desert')
boxes[2].append('dress')

# Replace the snow and the shirt with the bracelet and the key in Box 4.
boxes[4].remove('shirt')
boxes[4].remove('snow')
boxes[4].append('bracelet')
boxes[4].append('key')

# Remove the bracelet and the key from Box 4.
boxes[4].remove('bracelet')
boxes[4].remove('key')

# Swap the keyboard in Box 2 with the planet in Box 3.
boxes[2].remove('keyboard')
boxes[3].remove('planet')
boxes[2].append('planet')
boxes[3].append('keyboard')

# Remove the keyboard from Box 3.
boxes[3].remove('keyboard')

# Put the flower and the oven and the branch into Box 2.
boxes[2].append('flower')
boxes[2].append('oven')
boxes[2].append('branch')

# Remove the tiger and the brush and the desert from Box 1.
items_to_remove = ['tiger', 'brush', 'desert']
for item in items_to_remove:
    boxes[1].remove(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")