# Initial state of boxes
boxes = {
    0: ['train', 'bird', 'whistle', 'perfume'],
    1: ['pan', 'rock', 'ocean'],
    2: ['cloud', 'ship', 'truck', 'scissors'],
    3: ['laptop', 'fork', 'book', 'car'],
    4: ['glove', 'fish', 'wire', 'vase', 'tie'],
    5: [],
    6: ['mirror', 'motorcycle'],
    7: ['shark', 'key', 'lightning', 'mixer', 'bear']
}

# Move the vase and the tie and the fish from Box 4 to Box 2.
items_to_move = ['vase', 'tie', 'fish']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[2].append(item)

# Remove the wire from Box 4.
boxes[4].remove('wire')

# Replace the lightning and the shark and the bear with the toaster and the coral and the headphone in Box 7.
boxes[7].remove('lightning')
boxes[7].remove('shark')
boxes[7].remove('bear')
boxes[7].append('toaster')
boxes[7].append('coral')
boxes[7].append('headphone')

# Swap the key in Box 7 with the fork in Box 3.
boxes[7].remove('key')
boxes[3].remove('fork')
boxes[7].append('fork')
boxes[3].append('key')

# Remove the glove from Box 4.
boxes[4].remove('glove')

# Remove the pan and the ocean from Box 1.
boxes[1].remove('pan')
boxes[1].remove('ocean')

# Remove the book and the car and the key from Box 3.
boxes[3].remove('book')
boxes[3].remove('car')
boxes[3].remove('key')

# Replace the rock with the star in Box 1.
boxes[1].remove('rock')
boxes[1].append('star')

# Replace the star with the lipstick in Box 1.
boxes[1].remove('star')
boxes[1].append('lipstick')

# Replace the motorcycle with the dice in Box 6.
boxes[6].remove('motorcycle')
boxes[6].append('dice')

# Replace the lipstick with the bird in Box 1.
boxes[1].remove('lipstick')
boxes[1].append('bird')

# Replace the laptop with the clock in Box 3.
boxes[3].remove('laptop')
boxes[3].append('clock')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")