box0 = []
box1 = ['necklace', 'violin']
box2 = []
box3 = ['fork', 'chair']
box4 = ['belt', 'blender', 'elephant']

# Swap the violin in Box 1 with the blender in Box 4
box1.remove('violin')
box4.remove('blender')
box1.append('blender')
box4.append('violin')

# Move the necklace and the blender from Box 1 to Box 3
box1.remove('necklace')
box1.remove('blender')
box3.extend(['necklace', 'blender'])

# Move the violin and the elephant and the belt from Box 4 to Box 1
box4.remove('violin')
box4.remove('elephant')
box4.remove('belt')
box1.extend(['violin', 'elephant', 'belt'])

# Remove the elephant from Box 1
box1.remove('elephant')

# Replace the violin and the belt with the rocket and the note in Box 1
box1.remove('violin')
box1.remove('belt')
box1.extend(['rocket', 'note'])

# Replace the chair and the fork with the island and the coin in Box 3
box3.remove('fork')
box3.remove('chair')
box3.extend(['island', 'coin'])

# Empty Box 3
box3 = []

# Replace the rocket with the makeup in Box 1
box1.remove('rocket')
box1.append('makeup')

print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)
print("Box 4:", box4)