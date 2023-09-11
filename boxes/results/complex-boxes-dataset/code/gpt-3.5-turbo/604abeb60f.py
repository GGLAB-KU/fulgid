# Initial state of boxes
boxes = {
    0: ['coin', 'umbrella'],
    1: ['storm', 'harmonica', 'puzzle', 'boat', 'shelf'],
    2: ['rock', 'razor', 'charger', 'shoes', 'skirt'],
    3: ['scarf', 'sun']
}

# Replace the sun and the scarf with the flower and the laptop in Box 3.
boxes[3].remove('scarf')
boxes[3].remove('sun')
boxes[3].append('flower')
boxes[3].append('laptop')

# Remove the coin from Box 0.
boxes[0].remove('coin')

# Swap the storm in Box 1 with the flower in Box 3.
boxes[1].remove('storm')
boxes[3].remove('flower')
boxes[1].append('flower')
boxes[3].append('storm')

# Put the hat into Box 3.
boxes[3].append('hat')

# Put the car and the tiger and the bicycle into Box 0.
items_to_add = ['car', 'tiger', 'bicycle']
for item in items_to_add:
    boxes[0].append(item)

# Move the puzzle and the harmonica and the boat from Box 1 to Box 2.
items_to_move = ['puzzle', 'harmonica', 'boat']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[2].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")