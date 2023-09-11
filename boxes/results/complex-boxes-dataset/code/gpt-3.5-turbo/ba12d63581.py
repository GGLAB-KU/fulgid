# Initial state of boxes
boxes = {
    0: ['desert', 'book', 'toothbrush', 'sculpture'],
    1: ['microwave', 'flower', 'boat', 'magnet'],
    2: ['seaweed', 'submarine'],
    3: ['card'],
    4: [],
    5: ['butterfly', 'console', 'telescope'],
    6: ['wig', 'helmet', 'fish'],
    7: ['elephant', 'sandals', 'beach', 'necklace'],
    8: ['mixer'],
    9: ['ocean', 'lipstick', 'zipper', 'usb', 'soap'],
    10: ['button', 'scissors', 'river', 'puzzle', 'oven']
}

# Replace the sandals and the elephant with the puzzle and the pants in Box 7.
boxes[7].remove('sandals')
boxes[7].remove('elephant')
boxes[7].append('puzzle')
boxes[7].append('pants')

# Remove the puzzle and the beach and the pants from Box 7.
items_to_remove = ['puzzle', 'beach', 'pants']
for item in items_to_remove:
    boxes[7].remove(item)

# Swap the fish in Box 6 with the soap in Box 9.
boxes[6].remove('fish')
boxes[9].remove('soap')
boxes[6].append('soap')
boxes[9].append('fish')

# Replace the sculpture and the desert with the hat and the shirt in Box 0.
boxes[0].remove('sculpture')
boxes[0].remove('desert')
boxes[0].append('hat')
boxes[0].append('shirt')

# Move the card from Box 3 to Box 1.
boxes[3].remove('card')
boxes[1].append('card')

# Put the flower into Box 5.
boxes[5].append('flower')

# Remove the hat and the shirt and the book from Box 0.
items_to_remove = ['hat', 'shirt', 'book']
for item in items_to_remove:
    boxes[0].remove(item)

# Replace the toothbrush with the plane in Box 0.
boxes[0].remove('toothbrush')
boxes[0].append('plane')

# Swap the plane in Box 0 with the card in Box 1.
boxes[0].remove('plane')
boxes[1].remove('card')
boxes[0].append('card')
boxes[1].append('plane')

# Move the submarine and the seaweed from Box 2 to Box 7.
items_to_move = ['submarine', 'seaweed']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[7].append(item)

# Move the card from Box 0 to Box 9.
boxes[0].remove('card')
boxes[9].append('card')

# Remove the soap and the wig from Box 6.
boxes[6].remove('soap')
boxes[6].remove('wig')

# Replace the puzzle with the beach in Box 10.
boxes[10].remove('puzzle')
boxes[10].append('beach')

# Put the wig into Box 0.
boxes[0].append('wig')

# Put the table and the crown into Box 8.
boxes[8].append('table')
boxes[8].append('crown')

# Move the magnet and the boat and the flower from Box 1 to Box 10.
items_to_move = ['magnet', 'boat', 'flower']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[10].append(item)

# Swap the beach in Box 10 with the helmet in Box 6.
boxes[10].remove('beach')
boxes[6].remove('helmet')
boxes[10].append('helmet')
boxes[6].append('beach')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")