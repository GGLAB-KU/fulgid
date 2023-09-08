# Initial state of boxes
boxes = {
    0: ['shoes', 'lightning', 'toothpaste', 'beach'],
    1: [],
    2: ['starfish', 'flute'],
    3: ['thunder', 'thread', 'charger', 'ring', 'book'],
    4: ['pan', 'towel', 'truck'],
    5: ['plane'],
    6: ['basket', 'river'],
    7: ['shoe', 'pot'],
    8: ['mixer'],
    9: ['scarf'],
    10: ['shorts', 'microwave'],
    11: ['comet', 'meteor', 'mountain'],
    12: ['clock', 'motorcycle'],
    13: ['polish', 'watch', 'swimsuit']
}

# Swap the plane in Box 5 with the scarf in Box 9.
boxes[5].remove('plane')
boxes[9].remove('scarf')
boxes[5].append('scarf')
boxes[9].append('plane')

# Remove the shoe and the pot from Box 7.
boxes[7].remove('shoe')
boxes[7].remove('pot')

# Put the lightning and the starfish into Box 5.
boxes[5].append('lightning')
boxes[5].append('starfish')

# Swap the flute in Box 2 with the microwave in Box 10.
boxes[2].remove('flute')
boxes[10].remove('microwave')
boxes[2].append('microwave')
boxes[10].append('flute')

# Move the book and the charger from Box 3 to Box 5.
items_to_move = ['book', 'charger']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[5].append(item)

# Replace the shorts and the flute with the tree and the bag in Box 10.
boxes[10].remove('shorts')
boxes[10].remove('flute')
boxes[10].append('tree')
boxes[10].append('bag')

# Empty Box 10.
boxes[10] = []

# Remove the swimsuit from Box 13.
boxes[13].remove('swimsuit')

# Empty Box 0.
boxes[0] = []

# Remove the thread from Box 3.
boxes[3].remove('thread')

# Put the camera and the fish into Box 13.
boxes[13].append('camera')
boxes[13].append('fish')

# Remove the river from Box 6.
boxes[6].remove('river')

# Replace the thunder and the ring with the microscope and the harmonica in Box 3.
boxes[3].remove('thunder')
boxes[3].remove('ring')
boxes[3].append('microscope')
boxes[3].append('harmonica')

# Put the sandals and the glove into Box 4.
boxes[4].append('sandals')
boxes[4].append('glove')

# Remove the scarf and the book and the lightning from Box 5.
boxes[5].remove('scarf')
boxes[5].remove('book')
boxes[5].remove('lightning')

# Remove the towel from Box 4.
boxes[4].remove('towel')

# Replace the clock and the motorcycle with the ring and the sun in Box 12.
boxes[12].remove('clock')
boxes[12].remove('motorcycle')
boxes[12].append('ring')
boxes[12].append('sun')

# Put the skirt and the starfish and the pants into Box 11.
boxes[11].append('skirt')
boxes[11].append('starfish')
boxes[11].append('pants')

# Remove the basket from Box 6.
boxes[6].remove('basket')

# Move the meteor and the pants from Box 11 to Box 9.
boxes[11].remove('meteor')
boxes[11].remove('pants')
boxes[9].append('meteor')
boxes[9].append('pants')

# Put the piano and the dog and the ship into Box 0.
boxes[0].append('piano')
boxes[0].append('dog')
boxes[0].append('ship')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")