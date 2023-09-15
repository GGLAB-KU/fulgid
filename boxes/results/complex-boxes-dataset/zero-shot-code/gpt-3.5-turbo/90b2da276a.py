box_0 = ['blanket', 'pillow', 'controller', 'drum', 'tape']
box_1 = ['polish', 'cup', 'ocean']
box_2 = ['watch', 'pants']
box_3 = ['forest', 'sculpture', 'umbrella', 'whistle', 'horn']
box_4 = ['bag']
box_5 = ['clock', 'thunder', 'leaf']
box_6 = ['mountain', 'microscope', 'oven']

box_3.extend(['battery', 'bell'])
box_2.remove('pants')
box_2.remove('watch')
box_4.clear()
box_1.remove('polish')
box_1.remove('ocean')
box_1.remove('cup')
box_5[0] = 'apple'
box_5[1] = 'wallet'
box_5[2] = 'sandals'
box_0.remove('pillow')
box_0.remove('blanket')
box_0.remove('tape')
box_6.remove('mountain')
box_5.remove('sandals')
box_6.extend(['shampoo', 'brush', 'cup'])

print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)