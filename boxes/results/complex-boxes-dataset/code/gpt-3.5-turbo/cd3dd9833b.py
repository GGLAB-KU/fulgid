# Initial state of boxes
boxes = {
    0: [],
    1: ['shoes', 'seaweed'],
    2: ['horse'],
    3: ['coin', 'makeup', 'truck'],
    4: ['toothbrush', 'blanket']
}

# Swap the makeup in Box 3 with the horse in Box 2.
boxes[2].remove('horse')
boxes[3].remove('makeup')
boxes[2].append('makeup')
boxes[3].append('horse')

# Swap the toothbrush in Box 4 with the seaweed in Box 1.
boxes[1].remove('seaweed')
boxes[4].remove('toothbrush')
boxes[1].append('toothbrush')
boxes[4].append('seaweed')

# Swap the makeup in Box 2 with the shoes in Box 1.
boxes[1].remove('shoes')
boxes[2].remove('makeup')
boxes[1].append('makeup')
boxes[2].append('shoes')

# Put the starfish and the helmet and the branch into Box 0.
items_to_put = ['starfish', 'helmet', 'branch']
for item in items_to_put:
    boxes[0].append(item)

# Replace the starfish and the branch with the cloud and the soap in Box 0.
boxes[0].remove('starfish')
boxes[0].remove('branch')
boxes[0].append('cloud')
boxes[0].append('soap')

# Swap the shoes in Box 2 with the cloud in Box 0.
boxes[0].remove('cloud')
boxes[2].remove('shoes')
boxes[0].append('shoes')
boxes[2].append('cloud')

# Move the makeup and the toothbrush from Box 1 to Box 2.
items_to_move = ['makeup', 'toothbrush']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[2].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")