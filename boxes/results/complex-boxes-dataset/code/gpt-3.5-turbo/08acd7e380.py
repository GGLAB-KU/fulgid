# Initial state of boxes
boxes = {
    0: ['truck', 'shampoo'],
    1: ['tree'],
    2: [],
    3: ['motorcycle', 'dice', 'bell'],
    4: ['keyboard', 'shark'],
    5: ['razor'],
    6: ['submarine', 'beach'],
    7: ['thunder'],
    8: [],
    9: ['zipper', 'oven', 'console', 'dress', 'magnet'],
    10: ['violin', 'island', 'ship'],
    11: ['controller', 'cloud', 'rock', 'rain'],
    12: [],
    13: ['pan', 'boat', 'swimsuit']
}

# Move the magnet from Box 9 to Box 4.
boxes[9].remove('magnet')
boxes[4].append('magnet')

# Replace the shampoo and the truck with the glove and the boot in Box 0.
boxes[0].remove('shampoo')
boxes[0].remove('truck')
boxes[0].append('glove')
boxes[0].append('boot')

# Remove the oven and the console and the zipper from Box 9.
boxes[9].remove('oven')
boxes[9].remove('console')
boxes[9].remove('zipper')

# Put the submarine into Box 11.
boxes[11].append('submarine')

# Remove the razor from Box 5.
boxes[5].remove('razor')

# Move the dress from Box 9 to Box 1.
boxes[9].remove('dress')
boxes[1].append('dress')

# Remove the keyboard from Box 4.
boxes[4].remove('keyboard')

# Replace the dress with the lock in Box 1.
boxes[1].remove('dress')
boxes[1].append('lock')

# Replace the lock with the star in Box 1.
boxes[1].remove('lock')
boxes[1].append('star')

# Remove the controller and the cloud and the submarine from Box 11.
boxes[11].remove('controller')
boxes[11].remove('cloud')
boxes[11].remove('submarine')

# Move the star from Box 1 to Box 3.
boxes[1].remove('star')
boxes[3].append('star')

# Swap the ship in Box 10 with the dice in Box 3.
boxes[10].remove('ship')
boxes[3].remove('dice')
boxes[10].append('dice')
boxes[3].append('ship')

# Move the boot and the glove from Box 0 to Box 5.
boxes[0].remove('boot')
boxes[0].remove('glove')
boxes[5].append('boot')
boxes[5].append('glove')

# Replace the dice and the violin with the meteor and the bicycle in Box 10.
boxes[10].remove('dice')
boxes[10].remove('violin')
boxes[10].append('meteor')
boxes[10].append('bicycle')

# Swap the submarine in Box 6 with the tree in Box 1.
boxes[6].remove('submarine')
boxes[1].remove('tree')
boxes[6].append('tree')
boxes[1].append('submarine')

# Move the beach from Box 6 to Box 3.
boxes[6].remove('beach')
boxes[3].append('beach')

# Remove the glove from Box 5.
boxes[5].remove('glove')

# Remove the rock and the rain from Box 11.
boxes[11].remove('rock')
boxes[11].remove('rain')

# Move the ship and the motorcycle from Box 3 to Box 8.
boxes[3].remove('ship')
boxes[3].remove('motorcycle')
boxes[8].append('ship')
boxes[8].append('motorcycle')

# Move the bicycle and the island and the meteor from Box 10 to Box 3.
boxes[10].remove('bicycle')
boxes[10].remove('island')
boxes[10].remove('meteor')
boxes[3].append('bicycle')
boxes[3].append('island')
boxes[3].append('meteor')

# Put the shampoo into Box 12.
boxes[12].append('shampoo')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")