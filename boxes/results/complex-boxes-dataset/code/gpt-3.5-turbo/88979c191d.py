# Initial state of boxes
boxes = {
    0: ['frame', 'jungle', 'tape'],
    1: ['guitar'],
    2: ['cow', 'violin', 'octopus'],
    3: ['dress', 'flute'],
    4: ['toy', 'bird', 'ring', 'console'],
    5: ['puzzle', 'moon']
}

# Move the moon from Box 5 to Box 3.
boxes[5].remove('moon')
boxes[3].append('moon')

# Swap the puzzle in Box 5 with the guitar in Box 1.
boxes[5].remove('puzzle')
boxes[1].remove('guitar')
boxes[5].append('guitar')
boxes[1].append('puzzle')

# Put the keyboard and the cup into Box 2.
boxes[2].append('keyboard')
boxes[2].append('cup')

# Remove the guitar from Box 5.
boxes[5].remove('guitar')

# Put the cloud and the lock into Box 4.
boxes[4].append('cloud')
boxes[4].append('lock')

# Move the ring and the lock from Box 4 to Box 5.
boxes[4].remove('ring')
boxes[4].remove('lock')
boxes[5].append('ring')
boxes[5].append('lock')

# Move the dress and the moon from Box 3 to Box 1.
boxes[3].remove('dress')
boxes[3].remove('moon')
boxes[1].append('dress')
boxes[1].append('moon')

# Move the toy and the bird from Box 4 to Box 0.
boxes[4].remove('toy')
boxes[4].remove('bird')
boxes[0].append('toy')
boxes[0].append('bird')

# Move the tape and the bird from Box 0 to Box 3.
boxes[0].remove('tape')
boxes[0].remove('bird')
boxes[3].append('tape')
boxes[3].append('bird')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")