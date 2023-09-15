box_0 = ['star', 'mixer']
box_1 = []
box_2 = []
box_3 = ['toothbrush', 'lightning', 'freezer', 'gloves']
box_4 = []
box_5 = ['shampoo', 'bird']
box_6 = ['horse']
box_7 = ['harmonica', 'helmet', 'shoes', 'apple']
box_8 = ['razor', 'comb', 'controller']

box_1.extend(['belt', 'oven', 'bell'])
box_0.remove('star')
box_0.append('coin')
box_1.remove('bell')
box_1.extend(['lamp', 'forest', 'fridge'])
box_0, box_5 = box_5, box_0
box_3.append(box_7.pop(box_7.index('shoes')))
box_0.remove('shampoo')
box_0.remove('coin')
box_7, box_6 = box_6, box_7
box_5.extend([box_7.pop(box_7.index('apple')), box_7.pop(box_7.index('harmonica'))])
box_3.clear()
box_6[box_6.index('helmet')] = 'shorts'
box_7.remove('horse')
box_0.append(box_6.pop(box_6.index('shorts')))
box_4.extend(['flute', 'clock', 'drum'])

print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)
print("Box 8:", box_8)