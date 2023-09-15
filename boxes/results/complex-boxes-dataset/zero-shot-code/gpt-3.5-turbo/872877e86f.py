box_0 = ['jacket', 'plane']
box_1 = ['sock', 'gloves', 'branch', 'fish']
box_2 = ['blender', 'truck', 'dog', 'mask']
box_3 = ['glasses']
box_4 = ['puzzle', 'river']
box_5 = []
box_6 = ['swimsuit', 'pot', 'helmet', 'speaker', 'pen']

# Move the speaker and the swimsuit from Box 6 to Box 4
box_4.extend([box_6.pop(box_6.index('speaker')), box_6.pop(box_6.index('swimsuit'))])

# Replace the jacket with the necklace in Box 0
box_0[box_0.index('jacket')] = 'necklace'

# Put the hat and the tree into Box 0
box_0.extend(['hat', 'tree'])

# Remove the necklace from Box 0
box_0.remove('necklace')

# Move the sock and the branch from Box 1 to Box 3
box_3.extend([box_1.pop(box_1.index('sock')), box_1.pop(box_1.index('branch'))])

# Swap the swimsuit in Box 4 with the branch in Box 3
box_4[box_4.index('swimsuit')], box_3[box_3.index('branch')] = box_3[box_3.index('branch')], box_4[box_4.index('swimsuit')]

# Replace the tree and the plane and the hat with the helmet and the crown and the violin in Box 0
box_0 = ['helmet', 'crown', 'violin']

# Swap the blender in Box 2 with the glasses in Box 3
box_2[box_2.index('blender')], box_3[box_3.index('glasses')] = box_3[box_3.index('glasses')], box_2[box_2.index('blender')]

# Move the glasses from Box 2 to Box 3
box_3.append(box_2.pop(box_2.index('glasses')))

# Put the star into Box 6
box_6.append('star')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)