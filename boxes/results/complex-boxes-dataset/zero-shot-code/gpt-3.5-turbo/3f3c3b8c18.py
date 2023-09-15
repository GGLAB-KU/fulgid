box_0 = ['microwave']
box_1 = []
box_2 = ['ring', 'soap', 'glove', 'piano', 'wallet']
box_3 = []
box_4 = []
box_5 = ['cow', 'bear', 'console', 'towel']
box_6 = ['rock', 'shoes', 'sun', 'makeup', 'bird']

box_3.extend(['freezer', 'zipper', 'sock'])
box_3.remove('zipper')
box_3.remove('freezer')
box_3.remove('sock')

box_0.append('swimsuit')
box_1.append('bus')
box_1.remove('bus')
box_1.append('planet')

box_0_index = box_0.index('microwave')
box_6_index = box_6.index('sun')
box_0[box_0_index], box_6[box_6_index] = box_6[box_6_index], box_0[box_0_index]

box_2.append(box_0.pop(box_0_index))
box_5.append('boot')

box_1_index = box_1.index('planet')
box_2.append(box_1.pop(box_1_index))

box_0_index = box_0.index('microwave')
box_0[box_0_index] = 'controller'

box_6.append('cup')

print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)