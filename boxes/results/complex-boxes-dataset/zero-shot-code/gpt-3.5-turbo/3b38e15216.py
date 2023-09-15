box_0 = ['camera']
box_1 = ['sock', 'brush', 'beach', 'thunder']
box_2 = ['tie', 'dice', 'fridge', 'bell']
box_3 = ['microscope', 'star', 'doll', 'console', 'storm']
box_4 = ['scarf', 'keyboard', 'mirror']
box_5 = ['shampoo', 'bus', 'pen']
box_6 = []
box_7 = ['lamp', 'needle', 'zipper']
box_8 = ['shoe', 'motorcycle', 'mountain']
box_9 = ['cow', 'watch']
box_10 = ['wig', 'scissors', 'key', 'thread', 'blender']
box_11 = ['bag', 'towel']
box_12 = ['lipstick', 'tree']

box_6.extend(['lamp', 'motorcycle', 'earring'])
box_4.remove('keyboard')
box_4.remove('mirror')
box_4.remove('scarf')
box_6.remove('earring')
box_10.remove('wig')
box_6.append('wig')
box_5.extend(['mirror', 'sun'])
box_8.remove('shoe')
box_8.remove('motorcycle')
box_8.append('toaster')
box_8.append('bag')
box_12.remove('lipstick')
box_12.remove('tree')
box_12.append('bus')
box_12.append('horse')
box_0_index = box_0.index('camera')
box_10_index = box_10.index('blender')
box_0[box_0_index], box_10[box_10_index] = box_10[box_10_index], box_0[box_0_index]
box_4.extend(['razor', 'card'])
box_4_index = box_4.index('card')
box_1_index = box_1.index('beach')
box_4[box_4_index], box_1[box_1_index] = box_1[box_1_index], box_4[box_4_index]
box_4_index = box_4.index('beach')
box_3_index = box_3.index('microscope')
box_4[box_4_index], box_3[box_3_index] = box_3[box_3_index], box_4[box_4_index]
box_11_index = box_11.index('towel')
box_10_index = box_10.index('camera')
box_11[box_11_index], box_10[box_10_index] = box_10[box_10_index], box_11[box_11_index]
box_12.remove('bus')
box_12.remove('horse')
box_12.append('whistle')
box_12.append('vase')
box_6_index = box_6.index('wig')
box_4_index = box_4.index('microscope')
box_6[box_6_index], box_4[box_4_index] = box_4[box_4_index], box_6[box_6_index]
box_12.append('bag')
box_7.remove('lamp')
box_11_index = box_11.index('bag')
box_3.extend([box_11.pop(), box_0.pop()])
box_6.remove('lamp')
box_1_index = box_1.index('brush')
box_5_index = box_5.index('bus')
box_1.remove('bus')
box_1.remove('sock')
box_1.remove('card')
box_12.remove('whistle')

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