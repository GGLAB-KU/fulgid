box0 = ['leaf', 'fridge', 'mixer']
box1 = ['shelf', 'snow']
box2 = ['bowl']
box3 = ['violin', 'crown', 'submarine', 'table', 'flower']
box4 = ['horse', 'controller', 'bear']
box5 = ['umbrella', 'whistle', 'ring', 'coral', 'puzzle']

# Remove coral from Box 5
box5.remove('coral')

# Remove submarine from Box 3
box3.remove('submarine')

# Move violin, crown, and flower from Box 3 to Box 4
box4.extend(['violin', 'crown', 'flower'])
box3.remove('violin')
box3.remove('crown')
box3.remove('flower')

# Swap mixer in Box 0 with puzzle in Box 5
box0.remove('mixer')
box5.remove('puzzle')
box0.append('puzzle')
box5.append('mixer')

# Put magnet, watch, and seaweed into Box 1
box1.extend(['magnet', 'watch', 'seaweed'])

# Remove table from Box 3
box3.remove('table')

# Remove whistle from Box 5
box5.remove('whistle')

# Remove fridge, puzzle, and leaf from Box 0
box0.remove('fridge')
box0.remove('puzzle')
box0.remove('leaf')

# Swap bowl in Box 2 with violin in Box 4
box2.remove('bowl')
box4.remove('violin')
box2.append('violin')
box4.append('bowl')

# Print the contents of each box
print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)
print("Box 4:", box4)
print("Box 5:", box5)