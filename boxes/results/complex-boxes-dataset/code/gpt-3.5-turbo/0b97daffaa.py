# Initial state of boxes
boxes = {
    0: ['shorts', 'lion'],
    1: ['shoes', 'perfume', 'sculpture', 'towel', 'branch'],
    2: ['magnet', 'key'],
    3: ['scarf'],
    4: [],
    5: ['rain'],
    6: [],
    7: ['button', 'rock', 'piano', 'toy', 'wig'],
    8: ['glasses', 'toothpaste', 'bell', 'pot'],
    9: [],
    10: ['glove', 'bird', 'book', 'guitar'],
    11: ['tape', 'ocean', 'bag', 'sandals'],
    12: ['shark'],
    13: ['flower', 'shoe', 'thread']
}

# Remove the bag and the sandals from Box 11.
boxes[11].remove('bag')
boxes[11].remove('sandals')

# Remove the ocean and the tape from Box 11.
boxes[11].remove('ocean')
boxes[11].remove('tape')

# Move the glasses and the toothpaste from Box 8 to Box 10.
boxes[8].remove('glasses')
boxes[8].remove('toothpaste')
boxes[10].append('glasses')
boxes[10].append('toothpaste')

# Move the lion and the shorts from Box 0 to Box 9.
boxes[0].remove('lion')
boxes[0].remove('shorts')
boxes[9].append('lion')
boxes[9].append('shorts')

# Remove the shark from Box 12.
boxes[12].remove('shark')

# Swap the shoes in Box 1 with the shoe in Box 13.
boxes[1].remove('shoes')
boxes[13].remove('shoe')
boxes[1].append('shoe')
boxes[13].append('shoes')

# Move the towel and the perfume and the sculpture from Box 1 to Box 9.
items_to_move = ['towel', 'perfume', 'sculpture']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[9].append(item)

# Put the jacket and the spoon and the shirt into Box 4.
items_to_put = ['jacket', 'spoon', 'shirt']
for item in items_to_put:
    boxes[4].append(item)

# Put the pen and the branch into Box 9.
boxes[9].append('pen')
boxes[9].append('branch')

# Empty Box 9.
boxes[9] = []

# Replace the rain with the keyboard in Box 5.
boxes[5].remove('rain')
boxes[5].append('keyboard')

# Move the shoe and the branch from Box 1 to Box 9.
boxes[1].remove('shoe')
boxes[1].remove('branch')
boxes[9].append('shoe')
boxes[9].append('branch')

# Put the oven and the toothpaste into Box 2.
boxes[2].append('oven')
boxes[2].append('toothpaste')

# Replace the shirt and the jacket with the bell and the candle in Box 4.
boxes[4].remove('shirt')
boxes[4].remove('jacket')
boxes[4].append('bell')
boxes[4].append('candle')

# Replace the book with the mask in Box 10.
boxes[10].remove('book')
boxes[10].append('mask')

# Replace the keyboard with the scissors in Box 5.
boxes[5].remove('keyboard')
boxes[5].append('scissors')

# Move the scissors from Box 5 to Box 9.
boxes[5].remove('scissors')
boxes[9].append('scissors')

# Empty Box 2.
boxes[2] = []

# Put the bowl into Box 1.
boxes[1].append('bowl')

# Move the bowl from Box 1 to Box 5.
boxes[1].remove('bowl')
boxes[5].append('bowl')

# Move the guitar and the glasses from Box 10 to Box 8.
boxes[10].remove('guitar')
boxes[10].remove('glasses')
boxes[8].append('guitar')
boxes[8].append('glasses')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")