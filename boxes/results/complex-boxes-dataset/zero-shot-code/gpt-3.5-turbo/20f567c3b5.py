box_0 = ['train', 'bus', 'pan', 'bell']
box_1 = ['doll', 'umbrella', 'meteor']
box_2 = []
box_3 = ['island']
box_4 = []
box_5 = ['basket', 'harmonica', 'pot', 'glove']

print("Initial State:")
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)

box_2.append('bear')
box_0.remove('bear')

box_0.extend(['harmonica', 'basket', 'glove'])
box_5.remove('harmonica')
box_5.remove('basket')
box_5.remove('glove')

box_1.extend(['coin', 'controller', 'sock'])

box_2.extend(['bus', 'pan', 'train'])
box_0.remove('bus')
box_0.remove('pan')
box_0.remove('train')

box_5.append('moon')

box_2.clear()

box_5[box_5.index('pot')], box_0[box_0.index('bell')] = box_0[box_0.index('bell')], box_5[box_5.index('pot')]

box_5[box_5.index('bell')], box_1[box_1.index('meteor')] = box_1[box_1.index('meteor')], box_5[box_5.index('bell')]

box_5[box_5.index('moon')], box_3[0] = box_3[0], box_5[box_5.index('moon')]

print("\nFinal State:")
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)