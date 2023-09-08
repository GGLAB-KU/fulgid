# Initial state of boxes
boxes = {
    0: ['pan', 'boot', 'jungle', 'book', 'bear'],
    1: ['branch'],
    2: [],
    3: ['shirt'],
    4: ['razor', 'piano', 'controller'],
    5: ['moon', 'seaweed', 'chair'],
    6: []
}

# Replace the moon with the coin in Box 5.
boxes[5].remove('moon')
boxes[5].append('coin')

# Remove the branch from Box 1.
boxes[1].remove('branch')

# Remove the chair from Box 5.
boxes[5].remove('chair')

# Put the gloves into Box 5.
boxes[5].append('gloves')

# Empty Box 4.
boxes[4] = []

# Replace the pan and the bear with the tiger and the fridge in Box 0.
boxes[0].remove('pan')
boxes[0].remove('bear')
boxes[0].append('tiger')
boxes[0].append('fridge')

# Remove the fridge and the tiger and the boot from Box 0.
boxes[0].remove('fridge')
boxes[0].remove('tiger')
boxes[0].remove('boot')

# Move the book from Box 0 to Box 1.
boxes[0].remove('book')
boxes[1].append('book')

# Swap the coin in Box 5 with the jungle in Box 0.
boxes[5].remove('coin')
boxes[0].remove('jungle')
boxes[5].append('jungle')
boxes[0].append('coin')

# Replace the shirt with the cup in Box 3.
boxes[3].remove('shirt')
boxes[3].append('cup')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")