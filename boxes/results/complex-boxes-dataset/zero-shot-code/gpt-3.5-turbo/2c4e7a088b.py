box0 = []
box1 = ['paint', 'pillow']
box2 = []
box3 = ['pot', 'towel', 'freezer', 'whistle']

# Swap the pillow in Box 1 with the freezer in Box 3
box1.remove('pillow')
box3.remove('freezer')
box1.append('freezer')
box3.append('pillow')

# Move the towel and the pot and the whistle from Box 3 to Box 0
box0.extend(['towel', 'pot', 'whistle'])
box3.remove('towel')
box3.remove('pot')
box3.remove('whistle')

# Empty Box 0
box0 = []

# Move the pillow from Box 3 to Box 2
box3.remove('pillow')
box2.append('pillow')

# Remove the paint from Box 1
box1.remove('paint')

# Move the freezer from Box 1 to Box 2
box1.remove('freezer')
box2.append('freezer')

# Print the final state of the boxes
print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)