box_0 = []
box_1 = ['wig', 'horse', 'violin']
box_2 = ['coin', 'scarf', 'toaster', 'piano', 'note']
box_3 = ['moon']
box_4 = []
box_5 = ['forest', 'horn']
box_6 = ['game', 'boat']

box_4.append('blender')
box_5.extend(['apple', 'flower', 'freezer'])
box_2.clear()
box_2.extend(['apple', 'forest', 'freezer'])
box_4.remove('blender')
box_4.append('flower')
box_2[box_2.index('forest')], box_6[box_6.index('boat')] = box_6[box_6.index('boat')], box_2[box_2.index('forest')]
box_5[box_5.index('horn')] = 'zipper'
box_2.extend(box_1.pop(box_1.index('horse')))
box_2.extend(box_1.pop(box_1.index('violin')))
box_6[box_6.index('forest')], box_4[box_4.index('flower')] = box_4[box_4.index('flower')], box_6[box_6.index('forest')]
box_2.extend(box_4.pop(box_4.index('forest')))

print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)