# Initial state of boxes
boxes = {
    0: ['starfish', 'paint', 'mixer', 'magnet', 'ocean'],
    1: ['toaster', 'forest', 'bell', 'chair', 'horse'],
    2: ['shorts', 'shark', 'doll', 'dog'],
    3: ['rain'],
    4: ['cat']
}

# Empty Box 3
boxes[3] = []

# Move the paint and the starfish and the ocean from Box 0 to Box 3
items_to_move = ['paint', 'starfish', 'ocean']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[3].append(item)

# Empty Box 3
boxes[3] = []

# Swap the chair in Box 1 with the shark in Box 2
boxes[1].remove('chair')
boxes[2].remove('shark')
boxes[1].append('shark')
boxes[2].append('chair')

# Move the doll and the chair from Box 2 to Box 0
items_to_move = ['doll', 'chair']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[0].append(item)

# Remove the cat from Box 4
boxes[4].remove('cat')

# Remove the shorts and the dog from Box 2
boxes[2].remove('shorts')
boxes[2].remove('dog')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")