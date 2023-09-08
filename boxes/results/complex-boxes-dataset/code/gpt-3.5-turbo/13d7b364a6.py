# Initial state of boxes
boxes = {
    0: [],
    1: ['thread'],
    2: ['puzzle', 'console'],
    3: ['pillow', 'ocean', 'butterfly'],
    4: ['flute', 'key'],
    5: ['earring', 'cat', 'belt', 'shampoo'],
    6: [],
    7: ['dice', 'lamp', 'coin'],
    8: ['book', 'bear', 'basket', 'guitar'],
    9: ['sculpture', 'game'],
    10: ['tie', 'octopus', 'sun', 'beach'],
    11: []
}

# Replace the console with the chair in Box 2.
boxes[2].remove('console')
boxes[2].append('chair')

# Empty Box 4.
boxes[4] = []

# Swap the game in Box 9 with the thread in Box 1.
boxes[9].remove('game')
boxes[1].remove('thread')
boxes[9].append('thread')
boxes[1].append('game')

# Empty Box 1.
boxes[1] = []

# Remove the puzzle from Box 2.
boxes[2].remove('puzzle')

# Remove the pillow and the butterfly from Box 3.
boxes[3].remove('pillow')
boxes[3].remove('butterfly')

# Swap the chair in Box 2 with the ocean in Box 3.
boxes[2].remove('chair')
boxes[3].remove('ocean')
boxes[2].append('ocean')
boxes[3].append('chair')

# Put the bell and the tree into Box 11.
boxes[11].append('bell')
boxes[11].append('tree')

# Replace the bell and the tree with the seaweed and the tiger in Box 11.
boxes[11].remove('bell')
boxes[11].remove('tree')
boxes[11].append('seaweed')
boxes[11].append('tiger')

# Empty Box 10.
boxes[10] = []

# Put the plate and the necklace into Box 2.
boxes[2].append('plate')
boxes[2].append('necklace')

# Replace the chair with the button in Box 3.
boxes[3].remove('chair')
boxes[3].append('button')

# Move the button from Box 3 to Box 9.
boxes[3].remove('button')
boxes[9].append('button')

# Move the tiger and the seaweed from Box 11 to Box 10.
boxes[11].remove('tiger')
boxes[11].remove('seaweed')
boxes[10].append('tiger')
boxes[10].append('seaweed')

# Remove the cat from Box 5.
boxes[5].remove('cat')

# Remove the lamp and the dice and the coin from Box 7.
boxes[7].remove('lamp')
boxes[7].remove('dice')
boxes[7].remove('coin')

# Replace the seaweed and the tiger with the sock and the necklace in Box 10.
boxes[10].remove('seaweed')
boxes[10].remove('tiger')
boxes[10].append('sock')
boxes[10].append('necklace')

# Swap the sock in Box 10 with the earring in Box 5.
boxes[10].remove('sock')
boxes[5].remove('earring')
boxes[10].append('earring')
boxes[5].append('sock')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")