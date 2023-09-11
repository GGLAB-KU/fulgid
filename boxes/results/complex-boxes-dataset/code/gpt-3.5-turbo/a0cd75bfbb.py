# Initial state of boxes
boxes = {
    0: ['card'],
    1: ['plate', 'toothpaste', 'laptop'],
    2: ['cloud'],
    3: ['beach', 'zipper'],
    4: ['rocket', 'speaker', 'wig'],
    5: ['bracelet'],
    6: ['island', 'truck']
}

# Swap the rocket in Box 4 with the card in Box 0.
boxes[0].remove('card')
boxes[4].remove('rocket')
boxes[0].append('rocket')
boxes[4].append('card')

# Swap the wig in Box 4 with the rocket in Box 0.
boxes[0].remove('rocket')
boxes[4].remove('wig')
boxes[0].append('wig')
boxes[4].append('rocket')

# Swap the bracelet in Box 5 with the rocket in Box 4.
boxes[4].remove('rocket')
boxes[5].remove('bracelet')
boxes[4].append('bracelet')
boxes[5].append('rocket')

# Put the pot and the card into Box 0.
boxes[0].append('pot')

# Put the pants into Box 3.
boxes[3].append('pants')

# Move the bracelet and the speaker from Box 4 to Box 3.
boxes[4].remove('bracelet')
boxes[4].remove('speaker')
boxes[3].append('bracelet')
boxes[3].append('speaker')

# Remove the pot and the wig and the card from Box 0.
boxes[0].remove('pot')
boxes[0].remove('wig')
boxes[0].remove('card')

# Replace the rocket with the rain in Box 5.
boxes[5].remove('rocket')
boxes[5].append('rain')

# Replace the rain with the cat in Box 5.
boxes[5].remove('rain')
boxes[5].append('cat')

# Replace the truck and the island with the perfume and the dress in Box 6.
boxes[6].remove('truck')
boxes[6].remove('island')
boxes[6].append('perfume')
boxes[6].append('dress')

# Remove the cat from Box 5.
boxes[5].remove('cat')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")