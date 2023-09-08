# Initial state of boxes
boxes = {
    0: ['cat', 'card', 'polish', 'sun', 'pan'],
    1: ['spoon'],
    2: ['octopus', 'apple', 'shoes', 'lightning', 'tie'],
    3: ['boot', 'bird', 'toaster', 'guitar', 'comet'],
    4: ['needle', 'butterfly', 'lock', 'mixer', 'soap'],
    5: ['necklace', 'skirt'],
    6: ['fish', 'shark']
}

# Put the guitar and the helmet and the headphone into Box 2.
items_to_move = ['guitar', 'helmet', 'headphone']
for item in items_to_move:
    boxes[2].append(item)

# Swap the necklace in Box 5 with the spoon in Box 1.
boxes[1].remove('spoon')
boxes[5].remove('necklace')
boxes[1].append('necklace')
boxes[5].append('spoon')

# Move the fish from Box 6 to Box 3.
boxes[6].remove('fish')
boxes[3].append('fish')

# Move the mixer and the butterfly from Box 4 to Box 3.
items_to_move = ['mixer', 'butterfly']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[3].append(item)

# Put the toothbrush and the coin and the watch into Box 1.
items_to_move = ['toothbrush', 'coin', 'watch']
for item in items_to_move:
    boxes[1].append(item)

# Empty Box 2.
boxes[2] = []

# Move the shark from Box 6 to Box 4.
boxes[6].remove('shark')
boxes[4].append('shark')

# Put the dress and the laptop into Box 1.
items_to_move = ['dress', 'laptop']
for item in items_to_move:
    boxes[1].append(item)

# Move the skirt and the spoon from Box 5 to Box 4.
items_to_move = ['skirt', 'spoon']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[4].append(item)

# Move the bird and the guitar and the mixer from Box 3 to Box 2.
items_to_move = ['bird', 'guitar', 'mixer']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[2].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")