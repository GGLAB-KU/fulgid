# Initial state of boxes
boxes = {
    0: ['shark', 'controller', 'jacket', 'plate', 'seaweed'],
    1: [],
    2: [],
    3: ['starfish', 'toothpaste', 'scarf'],
    4: ['paint', 'coral', 'violin', 'phone', 'glasses'],
    5: ['lightning'],
    6: [],
    7: ['spoon', 'shoes', 'tape', 'apple', 'speaker']
}

# Replace the controller with the guitar in Box 0.
boxes[0].remove('controller')
boxes[0].append('guitar')

# Remove the paint and the violin from Box 4.
boxes[4].remove('paint')
boxes[4].remove('violin')

# Remove the apple and the speaker from Box 7.
boxes[7].remove('apple')
boxes[7].remove('speaker')

# Replace the scarf with the star in Box 3.
boxes[3].remove('scarf')
boxes[3].append('star')

# Move the lightning from Box 5 to Box 6.
boxes[5].remove('lightning')
boxes[6].append('lightning')

# Remove the tape and the shoes and the spoon from Box 7.
boxes[7].remove('tape')
boxes[7].remove('shoes')
boxes[7].remove('spoon')

# Remove the lightning from Box 6.
boxes[6].remove('lightning')

# Replace the toothpaste with the headphone in Box 3.
boxes[3].remove('toothpaste')
boxes[3].append('headphone')

# Move the shark from Box 0 to Box 4.
boxes[0].remove('shark')
boxes[4].append('shark')

# Put the shark and the seaweed into Box 3.
boxes[3].append('shark')
boxes[3].append('seaweed')

# Replace the seaweed and the headphone with the mirror and the bell in Box 3.
boxes[3].remove('seaweed')
boxes[3].remove('headphone')
boxes[3].append('mirror')
boxes[3].append('bell')

# Empty Box 4.
boxes[4] = []

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")