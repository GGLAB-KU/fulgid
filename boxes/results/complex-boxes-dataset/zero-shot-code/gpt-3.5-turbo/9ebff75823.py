box_0 = ['button', 'flute']
box_1 = ['shoe', 'console', 'clock', 'basket']
box_2 = ['bear', 'magnet', 'watch', 'river', 'candle']
box_3 = ['fork']
box_4 = []
box_5 = []
box_6 = []
box_7 = ['bowl', 'puzzle', 'microwave', 'doll', 'sun']
box_8 = []

# Swap the bowl in Box 7 with the button in Box 0
box_0.remove('button')
box_7.remove('bowl')
box_0.append('bowl')
box_7.append('button')

# Replace the button and the puzzle and the sun with the tie and the freezer and the fish in Box 7
box_7.remove('button')
box_7.remove('puzzle')
box_7.remove('sun')
box_7.append('tie')
box_7.append('freezer')
box_7.append('fish')

# Put the forest and the cup into Box 2
box_2.append('forest')
box_2.append('cup')

# Move the freezer and the tie and the fish from Box 7 to Box 1
box_1.append('freezer')
box_1.append('tie')
box_1.append('fish')
box_7.remove('freezer')
box_7.remove('tie')
box_7.remove('fish')

# Move the flute from Box 0 to Box 1
box_0.remove('flute')
box_1.append('flute')

# Put the river and the basket and the wire into Box 1
box_1.append('river')
box_1.append('basket')
box_1.append('wire')

# Remove the bowl from Box 0
box_0.remove('bowl')

# Move the console and the fish from Box 1 to Box 8
box_1.remove('console')
box_1.remove('fish')
box_8.append('console')
box_8.append('fish')

# Move the cup from Box 2 to Box 5
box_2.remove('cup')
box_5.append('cup')

# Put the perfume into Box 0
box_0.append('perfume')

# Replace the fork with the makeup in Box 3
box_3.remove('fork')
box_3.append('makeup')

# Replace the perfume with the elephant in Box 0
box_0.remove('perfume')
box_0.append('elephant')

# Put the blender and the fork into Box 5
box_5.append('blender')
box_5.append('fork')

# Swap the flute in Box 1 with the console in Box 8
box_1.remove('flute')
box_8.remove('console')
box_1.append('console')
box_8.append('flute')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)
print("Box 8:", box_8)