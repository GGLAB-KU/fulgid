# Initial state of boxes
boxes = {
    0: ['rain', 'scissors', 'mirror'],
    1: ['guitar', 'scarf', 'starfish', 'puzzle'],
    2: ['cat'],
    3: ['sock', 'desert'],
    4: ['fish', 'headphone', 'needle', 'planet', 'pot'],
    5: ['jungle'],
    6: ['shorts', 'beach', 'seaweed', 'book']
}

# Move the shorts and the seaweed and the book from Box 6 to Box 2.
items_to_move = ['shorts', 'seaweed', 'book']
for item in items_to_move:
    boxes[6].remove(item)
    boxes[2].append(item)

# Swap the headphone in Box 4 with the mirror in Box 0.
boxes[4].remove('headphone')
boxes[0].remove('mirror')
boxes[4].append('mirror')
boxes[0].append('headphone')

# Replace the jungle with the moon in Box 5.
boxes[5].remove('jungle')
boxes[5].append('moon')

# Put the submarine and the snow into Box 6.
boxes[6].append('submarine')
boxes[6].append('snow')

# Swap the snow in Box 6 with the moon in Box 5.
boxes[6].remove('snow')
boxes[5].remove('moon')
boxes[6].append('moon')
boxes[5].append('snow')

# Swap the snow in Box 5 with the sock in Box 3.
boxes[5].remove('snow')
boxes[3].remove('sock')
boxes[5].append('sock')
boxes[3].append('snow')

# Put the fork into Box 6.
boxes[6].append('fork')

# Put the beach and the sock into Box 1.
boxes[1].append('beach')
boxes[1].append('sock')

# Replace the scissors and the rain with the soap and the lamp in Box 0.
boxes[0].remove('scissors')
boxes[0].remove('rain')
boxes[0].append('soap')
boxes[0].append('lamp')

# Remove the starfish from Box 1.
boxes[1].remove('starfish')

# Replace the desert with the lipstick in Box 3.
boxes[3].remove('desert')
boxes[3].append('lipstick')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")