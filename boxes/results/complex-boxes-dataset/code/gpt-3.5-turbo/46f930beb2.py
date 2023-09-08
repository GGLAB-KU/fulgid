# Initial state of boxes
boxes = {
    0: ['tape'],
    1: ['storm', 'umbrella', 'microscope', 'sock'],
    2: ['bicycle', 'pillow', 'fork', 'brush', 'shampoo'],
    3: ['perfume', 'coral'],
    4: ['controller', 'swimsuit'],
    5: ['wallet', 'magnet']
}

# Swap the magnet in Box 5 with the swimsuit in Box 4.
boxes[4].remove('swimsuit')
boxes[5].remove('magnet')
boxes[4].append('magnet')
boxes[5].append('swimsuit')

# Put the note and the controller and the train into Box 3.
items_to_move = ['note', 'controller', 'train']
for item in items_to_move:
    boxes[3].append(item)

# Replace the note and the perfume with the tie and the shorts in Box 3.
boxes[3].remove('note')
boxes[3].remove('perfume')
boxes[3].append('tie')
boxes[3].append('shorts')

# Put the swimsuit and the headphone into Box 2.
boxes[2].append('swimsuit')
boxes[2].append('headphone')

# Swap the swimsuit in Box 5 with the sock in Box 1.
boxes[1].remove('sock')
boxes[5].remove('swimsuit')
boxes[1].append('swimsuit')
boxes[5].append('sock')

# Empty Box 5.
boxes[5] = []

# Remove the fork and the shampoo from Box 2.
boxes[2].remove('fork')
boxes[2].remove('shampoo')

# Replace the controller with the necklace in Box 4.
boxes[4].remove('controller')
boxes[4].append('necklace')

# Replace the magnet with the drum in Box 4.
boxes[4].remove('magnet')
boxes[4].append('drum')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")