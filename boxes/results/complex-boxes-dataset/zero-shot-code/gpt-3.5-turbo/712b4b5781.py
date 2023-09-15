box_0 = []
box_1 = ['mountain', 'zipper', 'rain']
box_2 = ['piano', 'comb', 'river']
box_3 = []
box_4 = ['leaf', 'charger', 'submarine']
box_5 = ['console', 'lamp']
box_6 = ['freezer']

# Put the scissors and the basket and the harmonica into Box 3
box_3.extend(['scissors', 'basket', 'harmonica'])

# Empty Box 2
box_2 = []

# Swap the lamp in Box 5 with the rain in Box 1
box_1.remove('rain')
box_5.remove('lamp')
box_1.append('lamp')
box_5.append('rain')

# Move the rain and the console from Box 5 to Box 3
box_5.remove('rain')
box_5.remove('console')
box_3.extend(['rain', 'console'])

# Move the charger and the submarine and the leaf from Box 4 to Box 2
box_4.remove('charger')
box_4.remove('submarine')
box_4.remove('leaf')
box_2.extend(['charger', 'submarine', 'leaf'])

# Remove the mountain and the lamp from Box 1
box_1.remove('mountain')
box_1.remove('lamp')

# Swap the charger in Box 2 with the zipper in Box 1
box_2.remove('charger')
box_1.remove('zipper')
box_2.append('zipper')
box_1.append('charger')

# Move the submarine and the zipper from Box 2 to Box 3
box_2.remove('submarine')
box_2.remove('zipper')
box_3.extend(['submarine', 'zipper'])

# Put the shorts into Box 5
box_5.append('shorts')

# Swap the freezer in Box 6 with the leaf in Box 2
box_6.remove('freezer')
box_2.remove('leaf')
box_6.append('leaf')
box_2.append('freezer')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)