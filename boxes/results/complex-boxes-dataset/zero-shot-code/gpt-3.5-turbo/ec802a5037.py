box0 = ['dog', 'game', 'razor', 'starfish']
box1 = []
box2 = ['dice']
box3 = ['shirt']
box4 = ['shorts', 'polish', 'blender']
box5 = ['pan', 'note', 'jacket', 'lock', 'planet']
box6 = ['zipper', 'fridge', 'apple', 'cloud']

# Move the polish, blender, and shorts from Box 4 to Box 2
box2.extend([box4.pop(box4.index('polish')), box4.pop(box4.index('blender')), box4.pop(box4.index('shorts'))])

# Move the game and razor from Box 0 to Box 2
box2.extend([box0.pop(box0.index('game')), box0.pop(box0.index('razor'))])

# Replace the jacket with the coat in Box 5
box5[box5.index('jacket')] = 'coat'

# Put the brush, ship, and clock into Box 4
box4.extend(['brush', 'ship', 'clock'])

# Replace the fridge and cloud with the console and wallet in Box 6
box6[box6.index('fridge')] = 'console'
box6[box6.index('cloud')] = 'wallet'

# Replace the starfish with the makeup in Box 0
box0[box0.index('starfish')] = 'makeup'

# Put the console, towel, and comet into Box 6
box6.extend(['console', 'towel', 'comet'])

# Remove the makeup from Box 0
box0.remove('makeup')

# Empty Box 0
box0 = []

# Remove the ship, brush, and clock from Box 4
box4.remove('ship')
box4.remove('brush')
box4.remove('clock')

# Print the contents of each box
print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)
print("Box 4:", box4)
print("Box 5:", box5)
print("Box 6:", box6)