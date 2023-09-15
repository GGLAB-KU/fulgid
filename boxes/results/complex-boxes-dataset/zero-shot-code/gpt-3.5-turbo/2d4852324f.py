box0 = ['toothbrush', 'jungle']
box1 = []
box2 = []
box3 = ['camera', 'lamp', 'starfish', 'helmet', 'fish']
box4 = ['perfume', 'star', 'tree', 'ring']
box5 = ['zipper', 'scarf', 'ship', 'shirt']
box6 = ['coat', 'game', 'chair', 'planet']
box7 = ['hat', 'coral', 'cow', 'thunder']

# Move the chair from Box 6 to Box 2
box2.append(box6.pop(box6.index('chair')))

# Empty Box 4
box4 = []

# Remove the chair from Box 2
box2.remove('chair')

# Move the cow and the thunder and the coral from Box 7 to Box 0
box0.extend([box7.pop(box7.index('cow')), box7.pop(box7.index('thunder')), box7.pop(box7.index('coral'))])

# Swap the game in Box 6 with the camera in Box 3
box6[box6.index('game')], box3[box3.index('camera')] = box3[box3.index('camera')], box6[box6.index('game')]

# Remove the scarf and the ship and the shirt from Box 5
box5.remove('scarf')
box5.remove('ship')
box5.remove('shirt')

# Swap the camera in Box 6 with the zipper in Box 5
box6[box6.index('camera')], box5[box5.index('zipper')] = box5[box5.index('zipper')], box6[box6.index('camera')]

# Remove the hat from Box 7
box7.remove('hat')

# Put the lamp into Box 6
box6.append('lamp')

# Swap the lamp in Box 6 with the lamp in Box 3
box6[box6.index('lamp')], box3[box3.index('lamp')] = box3[box3.index('lamp')], box6[box6.index('lamp')]

# Put the book into Box 0
box0.append('book')

# Replace the planet and the zipper and the lamp with the shoes and the storm and the rain in Box 6
box6[box6.index('planet')] = 'shoes'
box6[box6.index('zipper')] = 'storm'
box6[box6.index('lamp')] = 'rain'

# Print the contents of each box
print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)
print("Box 4:", box4)
print("Box 5:", box5)
print("Box 6:", box6)
print("Box 7:", box7)