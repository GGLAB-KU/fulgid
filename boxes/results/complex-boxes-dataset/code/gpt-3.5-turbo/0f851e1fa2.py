# Initial state of boxes
boxes = {
    0: ['rocket', 'lion', 'dog'],
    1: ['submarine', 'thread', 'doll', 'piano', 'hat'],
    2: ['spoon', 'speaker', 'book'],
    3: [],
    4: ['scissors'],
    5: ['freezer', 'game', 'wig'],
    6: ['blanket', 'harmonica', 'headphone', 'bird'],
    7: ['fridge', 'plate', 'vase', 'shorts', 'toaster'],
    8: ['battery', 'mountain', 'car']
}

# Replace the scissors with the skirt in Box 4.
boxes[4].remove('scissors')
boxes[4].append('skirt')

# Move the speaker from Box 2 to Box 3.
boxes[2].remove('speaker')
boxes[3].append('speaker')

# Remove the blanket from Box 6.
boxes[6].remove('blanket')

# Put the desert into Box 2.
boxes[2].append('desert')

# Move the bird and the headphone from Box 6 to Box 0.
boxes[6].remove('bird')
boxes[6].remove('headphone')
boxes[0].append('bird')
boxes[0].append('headphone')

# Replace the rocket and the dog and the bird with the horse and the dress and the mirror in Box 0.
boxes[0].remove('rocket')
boxes[0].remove('dog')
boxes[0].remove('bird')
boxes[0].append('horse')
boxes[0].append('dress')
boxes[0].append('mirror')

# Replace the speaker with the mask in Box 3.
boxes[3].remove('speaker')
boxes[3].append('mask')

# Remove the harmonica from Box 6.
boxes[6].remove('harmonica')

# Swap the mask in Box 3 with the spoon in Box 2.
boxes[3].remove('mask')
boxes[2].remove('spoon')
boxes[3].append('spoon')
boxes[2].append('mask')

# Empty Box 1.
boxes[1] = []

# Put the bicycle and the controller into Box 5.
boxes[5].append('bicycle')
boxes[5].append('controller')

# Put the cup and the moon into Box 6.
boxes[6].append('cup')
boxes[6].append('moon')

# Empty Box 2.
boxes[2] = []

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")