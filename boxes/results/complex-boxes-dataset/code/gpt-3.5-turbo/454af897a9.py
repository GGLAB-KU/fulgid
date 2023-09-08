# Initial state of boxes
boxes = {
    0: ['sun', 'console', 'wallet', 'helmet', 'tie'],
    1: ['mountain', 'shoe', 'planet', 'rocket'],
    2: [],
    3: ['earring', 'cow', 'charger', 'doll'],
    4: [],
    5: ['hat', 'dress'],
    6: ['keyboard', 'key', 'star', 'card'],
    7: [],
    8: [],
    9: ['microwave', 'grass'],
    10: [],
    11: [],
    12: ['violin', 'pan', 'bell', 'coin'],
    13: ['zipper', 'apple', 'shorts', 'wig']
}

# Swap the coin in Box 12 with the shoe in Box 1.
boxes[12].remove('coin')
boxes[1].remove('shoe')
boxes[12].append('shoe')
boxes[1].append('coin')

# Replace the wallet with the fish in Box 0.
boxes[0].remove('wallet')
boxes[0].append('fish')

# Swap the microwave in Box 9 with the sun in Box 0.
boxes[9].remove('microwave')
boxes[0].remove('sun')
boxes[9].append('sun')
boxes[0].append('microwave')

# Move the sun and the grass from Box 9 to Box 1.
items_to_move = ['sun', 'grass']
for item in items_to_move:
    boxes[9].remove(item)
    boxes[1].append(item)

# Empty Box 0.
boxes[0] = []

# Put the cat and the branch into Box 7.
boxes[7].append('cat')
boxes[7].append('branch')

# Put the ocean and the bicycle and the pan into Box 10.
boxes[10].append('ocean')
boxes[10].append('bicycle')
boxes[10].append('pan')

# Remove the hat and the dress from Box 5.
boxes[5].remove('hat')
boxes[5].remove('dress')

# Move the rocket and the coin and the grass from Box 1 to Box 6.
items_to_move = ['rocket', 'coin', 'grass']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[6].append(item)

# Swap the pan in Box 10 with the mountain in Box 1.
boxes[10].remove('pan')
boxes[1].remove('mountain')
boxes[10].append('mountain')
boxes[1].append('pan')

# Swap the branch in Box 7 with the zipper in Box 13.
boxes[7].remove('branch')
boxes[13].remove('zipper')
boxes[7].append('zipper')
boxes[13].append('branch')

# Put the seaweed and the pants into Box 7.
boxes[7].append('seaweed')
boxes[7].append('pants')

# Replace the card and the grass with the oven and the plate in Box 6.
boxes[6].remove('card')
boxes[6].remove('grass')
boxes[6].append('oven')
boxes[6].append('plate')

# Put the scissors and the flute and the doll into Box 10.
boxes[10].append('scissors')
boxes[10].append('flute')
boxes[10].append('doll')

# Empty Box 3.
boxes[3] = []

# Put the umbrella and the paint and the button into Box 4.
boxes[4].append('umbrella')
boxes[4].append('paint')
boxes[4].append('button')

# Swap the paint in Box 4 with the sun in Box 1.
boxes[4].remove('paint')
boxes[1].remove('sun')
boxes[4].append('sun')
boxes[1].append('paint')

# Replace the shoe and the violin and the bell with the thunder and the brush and the fish in Box 12.
boxes[12].remove('shoe')
boxes[12].remove('violin')
boxes[12].remove('bell')
boxes[12].append('thunder')
boxes[12].append('brush')
boxes[12].append('fish')

# Replace the umbrella and the button with the boot and the dice in Box 4.
boxes[4].remove('umbrella')
boxes[4].remove('button')
boxes[4].append('boot')
boxes[4].append('dice')

# Put the snow and the necklace into Box 1.
boxes[1].append('snow')
boxes[1].append('necklace')

# Empty Box 4.
boxes[4] = []

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")