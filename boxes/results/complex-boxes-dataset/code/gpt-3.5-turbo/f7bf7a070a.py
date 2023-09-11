# Initial state of boxes
boxes = {
    0: ['starfish', 'bag'],
    1: ['paint', 'beach'],
    2: ['shorts'],
    3: ['bird', 'shirt', 'rocket'],
    4: ['microwave', 'forest']
}

# Replace the paint with the bicycle in Box 1.
boxes[1].remove('paint')
boxes[1].append('bicycle')

# Move the microwave from Box 4 to Box 1.
boxes[4].remove('microwave')
boxes[1].append('microwave')

# Replace the shorts with the whistle in Box 2.
boxes[2].remove('shorts')
boxes[2].append('whistle')

# Put the keyboard and the fish and the helmet into Box 0.
items_to_move = ['keyboard', 'fish', 'helmet']
for item in items_to_move:
    boxes[0].append(item)

# Remove the bird from Box 3.
boxes[3].remove('bird')

# Swap the microwave in Box 1 with the starfish in Box 0.
boxes[1].remove('microwave')
boxes[0].remove('starfish')
boxes[1].append('starfish')
boxes[0].append('microwave')

# Swap the helmet in Box 0 with the shirt in Box 3.
boxes[0].remove('helmet')
boxes[3].remove('shirt')
boxes[0].append('shirt')
boxes[3].append('helmet')

# Swap the beach in Box 1 with the helmet in Box 3.
boxes[1].remove('beach')
boxes[3].remove('helmet')
boxes[1].append('helmet')
boxes[3].append('beach')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")