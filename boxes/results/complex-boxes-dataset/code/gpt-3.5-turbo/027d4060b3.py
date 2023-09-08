# Initial state of boxes
boxes = {
    0: ['coral'],
    1: ['sun', 'guitar', 'microwave', 'planet'],
    2: ['boat', 'grass', 'bird', 'headphone', 'dice'],
    3: ['cat', 'scissors', 'coin', 'toy', 'tiger'],
    4: ['thread', 'ship'],
    5: ['umbrella', 'plane'],
    6: ['freezer'],
    7: ['meteor', 'table', 'bell', 'car', 'storm'],
    8: [],
    9: [],
    10: ['mask'],
    11: []
}

# Replace the umbrella and the plane with the tree and the dice in Box 5.
boxes[5].remove('umbrella')
boxes[5].remove('plane')
boxes[5].append('tree')
boxes[5].append('dice')

# Replace the planet and the guitar with the earring and the piano in Box 1.
boxes[1].remove('planet')
boxes[1].remove('guitar')
boxes[1].append('earring')
boxes[1].append('piano')

# Remove the freezer from Box 6.
boxes[6].remove('freezer')

# Remove the cat and the tiger and the scissors from Box 3.
boxes[3].remove('cat')
boxes[3].remove('tiger')
boxes[3].remove('scissors')

# Remove the meteor and the bell from Box 7.
boxes[7].remove('meteor')
boxes[7].remove('bell')

# Move the coral from Box 0 to Box 2.
boxes[0].remove('coral')
boxes[2].append('coral')

# Move the coin from Box 3 to Box 4.
boxes[3].remove('coin')
boxes[4].append('coin')

# Remove the mask from Box 10.
boxes[10].remove('mask')

# Swap the toy in Box 3 with the coral in Box 2.
boxes[2].remove('coral')
boxes[3].remove('toy')
boxes[2].append('toy')
boxes[3].append('coral')

# Replace the storm with the lamp in Box 7.
boxes[7].remove('storm')
boxes[7].append('lamp')

# Replace the coral with the wire in Box 3.
boxes[3].remove('coral')
boxes[3].append('wire')

# Remove the dice and the tree from Box 5.
boxes[5].remove('dice')
boxes[5].remove('tree')

# Remove the thread and the ship from Box 4.
boxes[4].remove('thread')
boxes[4].remove('ship')

# Put the horse into Box 0.
boxes[0].append('horse')

# Replace the car and the table with the camera and the cat in Box 7.
boxes[7].remove('car')
boxes[7].remove('table')
boxes[7].append('camera')
boxes[7].append('cat')

# Swap the coin in Box 4 with the piano in Box 1.
boxes[4].remove('coin')
boxes[1].remove('piano')
boxes[4].append('piano')
boxes[1].append('coin')

# Remove the horse from Box 0.
boxes[0].remove('horse')

# Put the lion and the charger and the flute into Box 6.
boxes[6].append('lion')
boxes[6].append('charger')
boxes[6].append('flute')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")