# Initial state of boxes
boxes = {
    0: ['card', 'shirt', 'ring', 'fish'],
    1: ['shorts', 'helmet', 'desert'],
    2: ['piano', 'blender', 'cloud'],
    3: ['book', 'star', 'lightning', 'thunder'],
    4: [],
    5: ['microwave', 'lock', 'branch'],
    6: ['comet', 'butterfly']
}

# Remove the cloud and the blender and the piano from Box 2.
boxes[2].remove('piano')
boxes[2].remove('blender')
boxes[2].remove('cloud')

# Remove the comet from Box 6.
boxes[6].remove('comet')

# Move the card from Box 0 to Box 1.
boxes[0].remove('card')
boxes[1].append('card')

# Move the card from Box 1 to Box 4.
boxes[1].remove('card')
boxes[4].append('card')

# Move the shirt from Box 0 to Box 5.
boxes[0].remove('shirt')
boxes[5].append('shirt')

# Swap the lock in Box 5 with the helmet in Box 1.
boxes[5].remove('lock')
boxes[1].remove('helmet')
boxes[5].append('helmet')
boxes[1].append('lock')

# Move the butterfly from Box 6 to Box 1.
boxes[6].remove('butterfly')
boxes[1].append('butterfly')

# Remove the ring from Box 0.
boxes[0].remove('ring')

# Remove the lock from Box 1.
boxes[1].remove('lock')

# Put the sandals and the lipstick into Box 4.
boxes[4].append('sandals')
boxes[4].append('lipstick')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")