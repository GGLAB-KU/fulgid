box_0 = ['headphone', 'comet', 'thunder']
box_1 = ['horn', 'skirt', 'sandals']
box_2 = []
box_3 = ['dolphin', 'branch']

box_3.remove('dolphin')
box_3.append('scissors')
box_3.remove('scissors')
box_3.append('sun')

box_2.extend(['puzzle', 'train', 'needle'])

box_0[box_0.index('thunder')] = 'sun'

box_2[box_2.index('puzzle')] = 'blender'

print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)