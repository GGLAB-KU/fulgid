# Initial state of boxes
boxes = {
    0: ['comet', 'comb', 'tie', 'sandals'],
    1: ['note'],
    2: ['coat', 'bird'],
    3: ['tree', 'lightning', 'bicycle'],
    4: ['truck']
}

# Put the apple and the forest and the earring into Box 4.
boxes[4].append('apple')
boxes[4].append('forest')
boxes[4].append('earring')

# Put the meteor and the seaweed into Box 0.
boxes[0].append('meteor')
boxes[0].append('seaweed')

# Put the apple and the butterfly and the pillow into Box 0.
boxes[0].append('apple')
boxes[0].append('butterfly')
boxes[0].append('pillow')

# Remove the note from Box 1.
boxes[1].remove('note')

# Swap the apple in Box 4 with the butterfly in Box 0.
boxes[4].remove('apple')
boxes[0].remove('butterfly')
boxes[4].append('butterfly')
boxes[0].append('apple')

# Move the sandals from Box 0 to Box 4.
boxes[0].remove('sandals')
boxes[4].append('sandals')

# Move the apple and the seaweed and the tie from Box 0 to Box 1.
items_to_move = ['apple', 'seaweed', 'tie']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[1].append(item)

# Remove the comet from Box 0.
boxes[0].remove('comet')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")