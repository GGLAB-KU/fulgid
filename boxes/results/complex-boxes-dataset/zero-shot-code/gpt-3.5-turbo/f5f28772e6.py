box_0 = ['branch', 'laptop', 'soap']
box_1 = ['card', 'perfume']
box_2 = []
box_3 = ['island', 'razor']
box_4 = []
box_5 = ['spoon', 'bell', 'grinder']
box_6 = ['guitar', 'grass', 'freezer', 'earring']
box_7 = ['lion', 'shark', 'belt']
box_8 = ['rocket', 'starfish', 'violin', 'motorcycle']

box_5 = []
box_8[box_8.index('motorcycle')], box_3[box_3.index('razor')] = box_3[box_3.index('razor')], box_8[box_8.index('motorcycle')]
box_8.remove('starfish')
box_8.remove('razor')
box_8.remove('rocket')
box_7.remove('shark')
box_7.remove('belt')
box_7.remove('lion')
box_6.remove('grass')
box_6.remove('earring')
box_6.remove('freezer')
box_0.remove('soap')
box_0.remove('branch')
box_2.append('fork')
box_6[box_6.index('guitar')], box_3[box_3.index('motorcycle')] = box_3[box_3.index('motorcycle')], box_6[box_6.index('guitar')]
box_3[box_3.index('island')] = 'fork'
box_1.append(box_3.pop())
box_2[0], box_3[box_3.index('guitar')] = box_3[box_3.index('guitar')], box_2[0]
box_3 = []
box_5.append('laptop')

print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)
print("Box 8:", box_8)