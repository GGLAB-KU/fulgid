box_0 = ['coral']
box_1 = ['sun', 'guitar', 'microwave', 'planet']
box_2 = ['boat', 'grass', 'bird', 'headphone', 'dice']
box_3 = ['cat', 'scissors', 'coin', 'toy', 'tiger']
box_4 = ['thread', 'ship']
box_5 = ['umbrella', 'plane']
box_6 = ['freezer']
box_7 = ['meteor', 'table', 'bell', 'car', 'storm']
box_8 = []
box_9 = []
box_10 = ['mask']
box_11 = []

# Replace the umbrella and the plane with the tree and the dice in Box 5
box_5.remove('umbrella')
box_5.remove('plane')
box_5.append('tree')
box_5.append('dice')

# Replace the planet and the guitar with the earring and the piano in Box 1
box_1.remove('planet')
box_1.remove('guitar')
box_1.append('earring')
box_1.append('piano')

# Remove the freezer from Box 6
box_6.remove('freezer')

# Remove the cat and the tiger and the scissors from Box 3
box_3.remove('cat')
box_3.remove('tiger')
box_3.remove('scissors')

# Remove the meteor and the bell from Box 7
box_7.remove('meteor')
box_7.remove('bell')

# Move the coral from Box 0 to Box 2
box_2.append(box_0.pop())

# Move the coin from Box 3 to Box 4
box_4.append(box_3.pop(box_3.index('coin')))

# Remove the mask from Box 10
box_10.remove('mask')

# Swap the toy in Box 3 with the coral in Box 2
box_2.append(box_3.pop(box_3.index('toy')))
box_3.append(box_2.pop(box_2.index('coral')))

# Replace the storm with the lamp in Box 7
box_7.remove('storm')
box_7.append('lamp')

# Replace the coral with the wire in Box 3
box_3.remove('coral')
box_3.append('wire')

# Remove the dice and the tree from Box 5
box_5.remove('dice')
box_5.remove('tree')

# Remove the thread and the ship from Box 4
box_4.remove('thread')
box_4.remove('ship')

# Put the horse into Box 0
box_0.append('horse')

# Replace the car and the table with the camera and the cat in Box 7
box_7.remove('car')
box_7.remove('table')
box_7.append('camera')
box_7.append('cat')

# Swap the coin in Box 4 with the piano in Box 1
box_1.append(box_4.pop(box_4.index('coin')))
box_4.append(box_1.pop(box_1.index('piano')))

# Remove the horse from Box 0
box_0.remove('horse')

# Put the lion and the charger and the flute into Box 6
box_6.append('lion')
box_6.append('charger')
box_6.append('flute')

# Print the contents of each box
for i, box in enumerate([box_0, box_1, box_2, box_3, box_4, box_5, box_6, box_7, box_8, box_9, box_10, box_11]):
    print(f"Box {i}: {box}")