# Initial state of boxes
boxes = {
    0: [],
    1: ['violin', 'phone', 'chair', 'toothbrush'],
    2: ['zipper'],
    3: ['lipstick', 'clock', 'lightning'],
    4: ['cat', 'cloud', 'table', 'polish']
}

# Remove the cloud and the cat and the polish from Box 4.
items_to_remove = ['cloud', 'cat', 'polish']
for item in items_to_remove:
    boxes[4].remove(item)

# Remove the table from Box 4.
boxes[4].remove('table')

# Swap the clock in Box 3 with the violin in Box 1.
boxes[3].remove('clock')
boxes[1].remove('violin')
boxes[3].append('violin')
boxes[1].append('clock')

# Swap the zipper in Box 2 with the lipstick in Box 3.
boxes[2].remove('zipper')
boxes[3].remove('lipstick')
boxes[2].append('lipstick')
boxes[3].append('zipper')

# Replace the toothbrush with the truck in Box 1.
boxes[1].remove('toothbrush')
boxes[1].append('truck')

# Remove the truck from Box 1.
boxes[1].remove('truck')

# Move the lipstick from Box 2 to Box 0.
boxes[2].remove('lipstick')
boxes[0].append('lipstick')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")