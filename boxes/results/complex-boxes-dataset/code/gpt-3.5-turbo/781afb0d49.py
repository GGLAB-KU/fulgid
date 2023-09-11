# Initial state of boxes
boxes = {
    0: ['razor', 'towel', 'shampoo', 'necklace'],
    1: ['shark', 'paint', 'book'],
    2: ['comet', 'pan', 'keyboard', 'car'],
    3: ['shoe', 'spoon', 'lipstick', 'frame', 'phone'],
    4: [],
    5: ['soap', 'flower', 'brush', 'shirt'],
    6: ['mirror', 'piano']
}

# Swap the flower in Box 5 with the piano in Box 6.
boxes[5].remove('flower')
boxes[6].remove('piano')
boxes[5].append('piano')
boxes[6].append('flower')

# Replace the shark and the book with the console and the dog in Box 1.
boxes[1].remove('shark')
boxes[1].remove('book')
boxes[1].append('console')
boxes[1].append('dog')

# Replace the shirt with the dog in Box 5.
boxes[5].remove('shirt')
boxes[5].append('dog')

# Put the elephant and the pan into Box 5.
boxes[5].append('elephant')
boxes[5].append('pan')

# Empty Box 6.
boxes[6] = []

# Remove the shampoo and the towel from Box 0.
boxes[0].remove('shampoo')
boxes[0].remove('towel')

# Move the dog and the paint and the console from Box 1 to Box 3.
items_to_move = ['dog', 'paint', 'console']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[3].append(item)

# Move the comet and the pan from Box 2 to Box 4.
items_to_move = ['comet', 'pan']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[4].append(item)

# Swap the brush in Box 5 with the comet in Box 4.
boxes[5].remove('brush')
boxes[4].remove('comet')
boxes[5].append('comet')
boxes[4].append('brush')

# Swap the keyboard in Box 2 with the razor in Box 0.
boxes[2].remove('keyboard')
boxes[0].remove('razor')
boxes[2].append('razor')
boxes[0].append('keyboard')

# Put the flute and the tiger and the motorcycle into Box 5.
boxes[5].append('flute')
boxes[5].append('tiger')
boxes[5].append('motorcycle')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")