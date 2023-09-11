# Initial state of boxes
boxes = {
    0: ['lipstick'],
    1: ['jacket', 'wire', 'plate', 'grinder'],
    2: ['earring', 'island', 'pillow', 'mixer', 'oven'],
    3: ['blender', 'button', 'mountain', 'whistle', 'rock'],
    4: ['makeup', 'violin', 'lamp', 'rain', 'pot'],
    5: ['piano'],
    6: ['dolphin', 'scissors', 'camera', 'magnet']
}

# Swap the jacket in Box 1 with the blender in Box 3.
boxes[1].remove('jacket')
boxes[3].remove('blender')
boxes[1].append('blender')
boxes[3].append('jacket')

# Put the jacket into Box 4.
boxes[4].append('jacket')

# Move the mountain and the jacket from Box 3 to Box 1.
boxes[3].remove('mountain')
boxes[3].remove('jacket')
boxes[1].append('mountain')
boxes[1].append('jacket')

# Swap the piano in Box 5 with the makeup in Box 4.
boxes[5].remove('piano')
boxes[4].remove('makeup')
boxes[5].append('makeup')
boxes[4].append('piano')

# Replace the lipstick with the table in Box 0.
boxes[0].remove('lipstick')
boxes[0].append('table')

# Move the makeup from Box 5 to Box 4.
boxes[5].remove('makeup')
boxes[4].append('makeup')

# Put the comb into Box 4.
boxes[4].append('comb')

# Put the jungle into Box 1.
boxes[1].append('jungle')

# Move the rain and the comb and the lamp from Box 4 to Box 3.
items_to_move = ['rain', 'comb', 'lamp']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[3].append(item)

# Swap the jacket in Box 4 with the jacket in Box 1.
boxes[4].remove('jacket')
boxes[1].remove('jacket')
boxes[4].append('jacket')
boxes[1].append('jacket')

# Put the truck and the shampoo into Box 5.
boxes[5].extend(['truck', 'shampoo'])

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")