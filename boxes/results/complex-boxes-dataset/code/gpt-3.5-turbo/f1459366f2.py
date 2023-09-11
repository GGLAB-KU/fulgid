# Initial state of boxes
boxes = {
    0: ['dress', 'truck', 'sock', 'leaf'],
    1: ['sun'],
    2: ['elephant'],
    3: [],
    4: ['scissors', 'shoe', 'train', 'thread', 'pan'],
    5: [],
    6: ['table', 'soap', 'seaweed'],
    7: [],
    8: []
}

# Swap the sock in Box 0 with the table in Box 6.
boxes[0].remove('sock')
boxes[6].remove('table')
boxes[0].append('table')
boxes[6].append('sock')

# Replace the elephant with the shirt in Box 2.
boxes[2].remove('elephant')
boxes[2].append('shirt')

# Empty Box 4.
boxes[4] = []

# Put the meteor and the pen and the shoes into Box 5.
items_to_move = ['meteor', 'pen', 'shoes']
for item in items_to_move:
    boxes[5].append(item)

# Move the soap from Box 6 to Box 5.
boxes[6].remove('soap')
boxes[5].append('soap')

# Swap the shirt in Box 2 with the table in Box 0.
boxes[2].remove('shirt')
boxes[0].remove('table')
boxes[2].append('table')
boxes[0].append('shirt')

# Move the table from Box 2 to Box 5.
boxes[2].remove('table')
boxes[5].append('table')

# Replace the shoes and the meteor with the blanket and the boat in Box 5.
boxes[5].remove('shoes')
boxes[5].remove('meteor')
boxes[5].append('blanket')
boxes[5].append('boat')

# Move the boat from Box 5 to Box 7.
boxes[5].remove('boat')
boxes[7].append('boat')

# Put the island into Box 8.
boxes[8].append('island')

# Move the shirt and the leaf from Box 0 to Box 5.
items_to_move = ['shirt', 'leaf']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[5].append(item)

# Put the beach into Box 8.
boxes[8].append('beach')

# Empty Box 7.
boxes[7] = []

# Remove the soap and the table and the shirt from Box 5.
items_to_remove = ['soap', 'table', 'shirt']
for item in items_to_remove:
    boxes[5].remove(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")