# Initial state of boxes
boxes = {
    0: ['basket', 'candle', 'pan', 'hat', 'brush'],
    1: ['toy', 'crown', 'jacket'],
    2: ['mixer', 'shirt', 'cloud'],
    3: ['coral', 'fork'],
    4: ['fridge', 'island', 'bird', 'coat', 'book'],
    5: ['sculpture', 'console'],
    6: ['rock', 'sock', 'frame', 'butterfly', 'skirt'],
    7: [],
    8: ['flower', 'ocean', 'lipstick', 'dog', 'perfume'],
    9: ['spoon']
}

# Swap the basket in Box 0 with the fork in Box 3.
boxes[0].remove('basket')
boxes[3].remove('fork')
boxes[0].append('fork')
boxes[3].append('basket')

# Replace the coat with the bracelet in Box 4.
boxes[4].remove('coat')
boxes[4].append('bracelet')

# Put the lipstick into Box 7.
boxes[7].append('lipstick')

# Put the perfume and the plane into Box 3.
boxes[3].append('perfume')
boxes[3].append('plane')

# Remove the sculpture from Box 5.
boxes[5].remove('sculpture')

# Swap the brush in Box 0 with the butterfly in Box 6.
boxes[0].remove('brush')
boxes[6].remove('butterfly')
boxes[0].append('butterfly')
boxes[6].append('brush')

# Remove the fridge and the bracelet from Box 4.
boxes[4].remove('fridge')
boxes[4].remove('bracelet')

# Replace the lipstick with the bird in Box 7.
boxes[7].remove('lipstick')
boxes[7].append('bird')

# Move the mixer and the shirt from Box 2 to Box 6.
boxes[2].remove('mixer')
boxes[2].remove('shirt')
boxes[6].append('mixer')
boxes[6].append('shirt')

# Empty Box 9.
boxes[9] = []

# Move the island from Box 4 to Box 5.
boxes[4].remove('island')
boxes[5].append('island')

# Swap the frame in Box 6 with the console in Box 5.
boxes[6].remove('frame')
boxes[5].remove('console')
boxes[6].append('console')
boxes[5].append('frame')

# Move the bird and the book from Box 4 to Box 0.
boxes[4].remove('bird')
boxes[4].remove('book')
boxes[0].append('bird')
boxes[0].append('book')

# Swap the console in Box 6 with the crown in Box 1.
boxes[6].remove('console')
boxes[1].remove('crown')
boxes[6].append('crown')
boxes[1].append('console')

# Remove the cloud from Box 2.
boxes[2].remove('cloud')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")