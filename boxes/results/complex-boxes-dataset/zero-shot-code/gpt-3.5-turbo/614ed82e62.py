box_0 = []
box_1 = ['bowl']
box_2 = ['jacket', 'telescope']
box_3 = ['octopus', 'card', 'forest']
box_4 = ['table', 'fridge']
box_5 = ['thunder']
box_6 = ['shelf']
box_5 = ['branch']
box_1.append('island')
box_1.extend(['toothbrush', 'tree', 'umbrella'])
box_0 = []
box_2[0], box_3[1] = box_3[1], box_2[0]
box_3.remove('table')
box_3.remove('octopus')
box_1.append(box_6.pop())
box_6[0], box_4[0] = box_4[0], box_6[0]
box_4[0] = box_6.pop()
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)