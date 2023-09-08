# Initial state of boxes
boxes = {
    0: [],
    1: ['guitar'],
    2: ['flute', 'gloves'],
    3: ['swimsuit', 'thread', 'sandals', 'dice', 'magnet'],
    4: ['shoes', 'mirror'],
    5: ['sculpture', 'sun', 'helmet'],
    6: ['thunder', 'lightning']
}

# Swap the sandals in Box 3 with the lightning in Box 6.
boxes[3].remove('sandals')
boxes[6].remove('lightning')
boxes[3].append('lightning')
boxes[6].append('sandals')

# Put the plane into Box 0.
boxes[0].append('plane')

# Remove the guitar from Box 1.
boxes[1].remove('guitar')

# Swap the helmet in Box 5 with the sandals in Box 6.
boxes[5].remove('helmet')
boxes[6].remove('sandals')
boxes[5].append('sandals')
boxes[6].append('helmet')

# Remove the gloves from Box 2.
boxes[2].remove('gloves')

# Put the headphone into Box 1.
boxes[1].append('headphone')

# Remove the headphone from Box 1.
boxes[1].remove('headphone')

# Replace the thread and the dice with the horn and the whistle in Box 3.
boxes[3].remove('thread')
boxes[3].remove('dice')
boxes[3].append('horn')
boxes[3].append('whistle')

# Replace the plane with the horse in Box 0.
boxes[0].remove('plane')
boxes[0].append('horse')

# Swap the flute in Box 2 with the sculpture in Box 5.
boxes[2].remove('flute')
boxes[5].remove('sculpture')
boxes[2].append('sculpture')
boxes[5].append('flute')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")