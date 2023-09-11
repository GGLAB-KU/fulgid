# Initial state of boxes
boxes = {
    0: [],
    1: ['telescope', 'glasses', 'wallet', 'bicycle'],
    2: ['mask', 'planet', 'forest', 'shoe', 'phone'],
    3: ['pillow', 'river', 'soap', 'sun']
}

# Put the soap into Box 3.
boxes[3].append('soap')

# Move the pillow and the soap from Box 3 to Box 1.
items_to_move = ['pillow', 'soap']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[1].append(item)

# Swap the forest in Box 2 with the dress in Box 3.
boxes[2].remove('forest')
boxes[3].remove('dress')
boxes[2].append('dress')
boxes[3].append('forest')

# Put the oven into Box 2.
boxes[2].append('oven')

# Put the scarf and the needle into Box 3.
boxes[3].append('scarf')
boxes[3].append('needle')

# Move the soap from Box 1 to Box 3.
boxes[1].remove('soap')
boxes[3].append('soap')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")