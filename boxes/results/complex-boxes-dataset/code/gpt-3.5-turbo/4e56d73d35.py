# Initial state of boxes
boxes = {
    0: ['rain', 'lightning', 'headphone', 'vase', 'ship'],
    1: ['seaweed', 'desert', 'coin'],
    2: ['bag'],
    3: ['rock', 'cloud', 'jungle'],
    4: [],
    5: ['lock', 'book', 'lion', 'sun'],
    6: ['sandals', 'puzzle', 'violin', 'laptop', 'truck'],
    7: ['bicycle'],
    8: ['shirt', 'planet'],
    9: ['oven', 'paint', 'wig', 'belt', 'dress'],
    10: ['bell'],
    11: ['fork', 'console', 'cow', 'thunder', 'mirror']
}

# Move the seaweed and the desert and the coin from Box 1 to Box 8.
items_to_move = ['seaweed', 'desert', 'coin']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[8].append(item)

# Put the starfish and the butterfly into Box 6.
boxes[6].append('starfish')
boxes[6].append('butterfly')

# Swap the bell in Box 10 with the bicycle in Box 7.
boxes[10], boxes[7] = boxes[7], boxes[10]

# Remove the fork and the cow and the console from Box 11.
items_to_remove = ['fork', 'cow', 'console']
for item in items_to_remove:
    boxes[11].remove(item)

# Swap the truck in Box 6 with the desert in Box 8.
boxes[6], boxes[8] = boxes[8], boxes[6]

# Put the tie into Box 10.
boxes[10].append('tie')

# Move the thunder and the mirror from Box 11 to Box 2.
items_to_move = ['thunder', 'mirror']
for item in items_to_move:
    boxes[11].remove(item)
    boxes[2].append(item)

# Move the bell from Box 7 to Box 5.
boxes[7].remove('bell')
boxes[5].append('bell')

# Put the battery and the mixer into Box 8.
boxes[8].append('battery')
boxes[8].append('mixer')

# Move the wig and the dress and the belt from Box 9 to Box 1.
items_to_move = ['wig', 'dress', 'belt']
for item in items_to_move:
    boxes[9].remove(item)
    boxes[1].append(item)

# Swap the dress in Box 1 with the desert in Box 6.
boxes[1], boxes[6] = boxes[6], boxes[1]

# Move the sandals and the laptop from Box 6 to Box 10.
items_to_move = ['sandals', 'laptop']
for item in items_to_move:
    boxes[6].remove(item)
    boxes[10].append(item)

# Move the puzzle from Box 6 to Box 11.
boxes[6].remove('puzzle')
boxes[11].append('puzzle')

# Remove the vase and the rain from Box 0.
boxes[0].remove('vase')
boxes[0].remove('rain')

# Replace the wig and the belt and the desert with the zipper and the snow and the tape in Box 1.
boxes[1].remove('wig')
boxes[1].remove('belt')
boxes[1].remove('desert')
boxes[1].append('zipper')
boxes[1].append('snow')
boxes[1].append('tape')

# Empty Box 3.
boxes[3] = []

# Move the puzzle from Box 11 to Box 6.
boxes[11].remove('puzzle')
boxes[6].append('puzzle')

# Move the puzzle and the dress and the violin from Box 6 to Box 9.
items_to_move = ['puzzle', 'dress', 'violin']
for item in items_to_move:
    boxes[6].remove(item)
    boxes[9].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")