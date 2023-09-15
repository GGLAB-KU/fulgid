box0 = ['crown', 'makeup', 'microscope']
box1 = []
box2 = ['pan', 'skirt', 'branch']
box3 = ['chair', 'dice', 'toothbrush']

# Replace items in Box 2
box2[0] = 'elephant'
box2[1] = 'brush'
box2[2] = 'toothbrush'

# Swap items between Box 0 and Box 3
box0[0], box3[0] = box3[0], box0[0]

# Remove items from Box 2 and Box 3
box2.remove('brush')
box2.remove('elephant')
box2.remove('toothbrush')
box3.remove('crown')
box3.remove('toothbrush')
box3.remove('dice')

# Replace items in Box 0
box0[0] = 'laptop'
box0[1] = 'pan'
box0[2] = 'ocean'

# Move pan from Box 0 to Box 1
box1.append(box0.pop(1))

# Print the contents of each box
print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)