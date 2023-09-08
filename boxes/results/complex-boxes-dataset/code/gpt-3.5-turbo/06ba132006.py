# Initial state of boxes
boxes = {
    0: ['coat', 'sandals'],
    1: ['toothpaste', 'ring', 'toaster', 'candle', 'pen'],
    2: ['jungle'],
    3: ['meteor', 'puzzle'],
    4: ['lightning'],
    5: ['cloud', 'coin', 'pot', 'tie', 'planet'],
    6: ['ocean', 'dress', 'bird', 'bear'],
    7: ['storm', 'submarine', 'zipper'],
    8: ['leaf', 'necklace', 'motorcycle', 'wig', 'apple'],
    9: ['key', 'frame'],
    10: ['swimsuit', 'seaweed', 'elephant']
}

# Move the puzzle from Box 3 to Box 6.
boxes[3].remove('puzzle')
boxes[6].append('puzzle')

# Empty Box 5.
boxes[5] = []

# Swap the jungle in Box 2 with the meteor in Box 3.
boxes[2].remove('jungle')
boxes[3].remove('meteor')
boxes[2].append('meteor')
boxes[3].append('jungle')

# Move the meteor from Box 2 to Box 9.
boxes[2].remove('meteor')
boxes[9].append('meteor')

# Move the sandals and the coat from Box 0 to Box 8.
items_to_move = ['sandals', 'coat']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[8].append(item)

# Remove the jungle from Box 3.
boxes[3].remove('jungle')

# Move the sandals and the apple from Box 8 to Box 10.
items_to_move = ['sandals', 'apple']
for item in items_to_move:
    boxes[8].remove(item)
    boxes[10].append(item)

# Swap the necklace in Box 8 with the sandals in Box 10.
boxes[8].remove('necklace')
boxes[10].remove('sandals')
boxes[8].append('sandals')
boxes[10].append('necklace')

# Remove the meteor from Box 9.
boxes[9].remove('meteor')

# Swap the key in Box 9 with the lightning in Box 4.
boxes[9].remove('key')
boxes[4].remove('lightning')
boxes[9].append('lightning')
boxes[4].append('key')

# Empty Box 9.
boxes[9] = []

# Put the leaf and the pants into Box 6.
items_to_move = ['leaf', 'pants']
for item in items_to_move:
    boxes[6].append(item)

# Put the perfume and the coral into Box 3.
items_to_move = ['perfume', 'coral']
for item in items_to_move:
    boxes[3].append(item)

# Replace the motorcycle and the coat with the book and the watch in Box 8.
boxes[8].remove('motorcycle')
boxes[8].remove('coat')
boxes[8].append('book')
boxes[8].append('watch')

# Swap the ring in Box 1 with the necklace in Box 10.
boxes[1].remove('ring')
boxes[10].remove('necklace')
boxes[1].append('necklace')
boxes[10].append('ring')

# Move the zipper from Box 7 to Box 5.
boxes[7].remove('zipper')
boxes[5].append('zipper')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")