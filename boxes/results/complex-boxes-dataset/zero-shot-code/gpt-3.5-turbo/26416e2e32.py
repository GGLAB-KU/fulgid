box_0 = ['submarine', 'frame', 'helmet']
box_1 = ['branch', 'grinder']
box_2 = ['shark', 'plane', 'paint']
box_3 = []
box_4 = ['shoe', 'fish', 'dress', 'ship', 'puzzle']
box_5 = ['doll', 'table', 'hat']
box_6 = ['oven']
box_7 = []
box_8 = []
box_9 = []
box_10 = []
box_11 = ['earring', 'sock']
box_12 = ['truck', 'fork', 'planet', 'crown']

box_0.extend(['crown', 'dress', 'seaweed'])
box_0.extend(['beach', 'pillow', 'mixer'])
box_5.remove('table')
box_10.extend(['shirt', 'clock'])
box_11[0], box_10[0] = box_10[0], box_11[0]
box_5.extend(['wallet', 'pen'])
box_6 = ['skirt']
box_4.extend(['boot', 'basket', 'plate'])
box_1.remove('grinder')
box_1[0], box_10[1] = box_10[1], box_1[0]
box_1 = ['piano']
box_5.extend(['puzzle', 'shoe', 'fish'])
box_2.extend(['pen', 'hat'])
box_1[0], box_11[1] = box_11[1], box_1[0]
box_2[0], box_4[1] = box_4[1], box_2[0]
box_7.extend(['toothpaste', 'vase', 'island'])
box_10[0], box_10[1] = box_10[1], box_10[0]
box_6.remove('skirt')
box_2[0], box_2[1], box_4[2], box_4[3], box_4[4] = box_4[2], box_4[3], box_4[4], box_2[0], box_2[1]

print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)
print("Box 8:", box_8)
print("Box 9:", box_9)
print("Box 10:", box_10)
print("Box 11:", box_11)
print("Box 12:", box_12)