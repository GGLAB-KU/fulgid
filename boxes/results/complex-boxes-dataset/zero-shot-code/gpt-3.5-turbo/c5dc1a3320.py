box_0 = ['shirt', 'rain', 'puzzle', 'wig']
box_1 = []
box_2 = []
box_3 = ['grass']
box_4 = ['octopus', 'wallet', 'moon', 'umbrella', 'cat']
box_5 = []
box_6 = ['flower', 'helmet', 'coral']
box_7 = ['bag', 'bell', 'toy']
box_8 = []
box_9 = []
box_10 = ['jungle', 'dress', 'perfume']
box_11 = ['drum']
box_12 = ['fridge', 'towel', 'shampoo', 'truck']
box_13 = ['usb']

box_13.append('card')
box_6[0] = 'perfume'
box_13[0] = 'comet'
box_10[0], box_6[1] = box_6[1], box_10[0]
box_0.append('hat')
box_6.append('shelf')
box_0.remove('wig')
box_0.remove('rain')
box_0.remove('hat')
box_8.extend(['wig', 'rain', 'hat'])
box_10.extend(['spoon', 'mask', 'mountain'])
box_10[0], box_11[0] = box_11[0], box_10[0]
box_3[0], box_11[0] = box_11[0], box_3[0]
box_4.extend(['lion', 'console', 'book'])
box_6[0] = 'lightning'
box_13[0], box_4[4] = box_4[4], box_13[0]
box_4[3], box_4[4] = box_4[4], box_4[3]
box_8.remove('wig')
box_8.remove('hat')
box_8.remove('rain')
box_3.extend(['wallet', 'comet', 'octopus'])
box_0.append('card')
box_10[1], box_10[0] = box_10[0], box_10[1]
box_10[0], box_11[0] = box_11[0], box_10[0]
box_4[2], box_3[0] = box_3[0], box_4[2]
box_4.remove('umbrella')
box_4.remove('lion')
box_4.extend(['needle', 'wig'])
box_4.remove('wallet')
box_4.remove('comet')
box_4.remove('octopus')
box_3.extend(['wallet', 'comet', 'octopus'])
box_8.remove('wig')
box_8.remove('hat')
box_8.remove('rain')
box_10[0], box_10[1] = box_10[1], box_10[0]
box_10[0], box_11[0] = box_11[0], box_10[0]
box_13.remove('card')
box_0[0], box_0[1] = box_0[1], box_0[0]
box_0[0], box_0[1] = box_0[1], box_0[0]
box_6.append('sun')
box_0[0], box_0[1] = box_0[1], box_0[0]

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
print("Box 13:", box_13)