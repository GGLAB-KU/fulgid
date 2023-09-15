box_0 = []
box_1 = []
box_2 = ['butterfly', 'table']
box_3 = ['bracelet', 'makeup']
box_4 = ['beach']

box_1.append('pillow')
box_1.remove('pillow')
box_1.append('vase')
box_4.remove('beach')
box_1.append('snow')
box_3.extend(['pen', 'shirt'])
box_2[0], box_3[1] = box_3[1], box_2[0]
box_2.remove('shirt')

print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)