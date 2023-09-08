# Initial state of boxes
boxes = {
    0: ['river', 'flute', 'game', 'drum'],
    1: ['ring', 'needle', 'headphone', 'charger'],
    2: ['magnet', 'rock', 'butterfly', 'vase'],
    3: ['piano', 'battery'],
    4: ['car', 'pen'],
    5: ['comb', 'shirt'],
    6: ['oven', 'tree'],
    7: ['dress', 'moon', 'sandals'],
    8: ['branch', 'bus', 'book', 'shoe', 'coin'],
    9: ['pants', 'desert', 'pot'],
    10: ['belt', 'plane', 'toothpaste', 'towel']
}

# Put the rocket and the toaster into Box 9.
boxes[9].append('rocket')
boxes[9].append('toaster')

# Move the shoe and the branch from Box 8 to Box 10.
boxes[8].remove('shoe')
boxes[8].remove('branch')
boxes[10].append('shoe')
boxes[10].append('branch')

# Move the book and the coin and the bus from Box 8 to Box 0.
items_to_move = ['book', 'coin', 'bus']
for item in items_to_move:
    boxes[8].remove(item)
    boxes[0].append(item)

# Put the piano and the cat and the coral into Box 10.
boxes[10].append('piano')
boxes[10].append('cat')
boxes[10].append('coral')

# Remove the battery from Box 3.
boxes[3].remove('battery')

# Replace the pen and the car with the puzzle and the bowl in Box 4.
boxes[4].remove('pen')
boxes[4].remove('car')
boxes[4].append('puzzle')
boxes[4].append('bowl')

# Put the fish into Box 1.
boxes[1].append('fish')

# Remove the shirt from Box 5.
boxes[5].remove('shirt')

# Replace the branch and the cat with the zipper and the toaster in Box 10.
boxes[10].remove('branch')
boxes[10].remove('cat')
boxes[10].append('zipper')
boxes[10].append('toaster')

# Put the lipstick and the book and the sculpture into Box 8.
boxes[8].append('lipstick')
boxes[8].append('book')
boxes[8].append('sculpture')

# Remove the headphone and the fish and the charger from Box 1.
boxes[1].remove('headphone')
boxes[1].remove('fish')
boxes[1].remove('charger')

# Move the sculpture and the lipstick and the book from Box 8 to Box 2.
items_to_move = ['sculpture', 'lipstick', 'book']
for item in items_to_move:
    boxes[8].remove(item)
    boxes[2].append(item)

# Move the game from Box 0 to Box 7.
boxes[0].remove('game')
boxes[7].append('game')

# Remove the shoe and the toothpaste and the towel from Box 10.
boxes[10].remove('shoe')
boxes[10].remove('toothpaste')
boxes[10].remove('towel')

# Swap the pot in Box 9 with the comb in Box 5.
boxes[9].remove('pot')
boxes[5].remove('comb')
boxes[9].append('comb')
boxes[5].append('pot')

# Move the lipstick and the sculpture and the magnet from Box 2 to Box 9.
items_to_move = ['lipstick', 'sculpture', 'magnet']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[9].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")