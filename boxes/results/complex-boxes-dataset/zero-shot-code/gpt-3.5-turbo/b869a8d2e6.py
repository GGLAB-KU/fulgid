box_0 = []
box_1 = ['magnet', 'comb', 'spoon', 'truck']
box_2 = ['headphone', 'star']
box_3 = ['charger', 'pen', 'usb', 'island', 'telescope']
box_4 = ['river', 'ring']
box_5 = []
box_6 = ['rocket', 'meteor', 'motorcycle', 'razor', 'battery']
box_7 = ['zipper', 'towel']
box_8 = ['piano', 'horse', 'jungle']
box_9 = ['perfume', 'bowl', 'pot']
box_10 = ['cow', 'horn']
box_11 = ['plate', 'wig']
box_12 = ['planet', 'cup']
box_13 = ['mixer', 'shirt', 'pan', 'flute']
box_14 = ['shoe', 'basket', 'lock', 'console', 'train']

box_5.append('doll')
box_9.remove('perfume')
box_9.remove('pot')
box_9.remove('bowl')
box_8.remove('piano')
box_8.remove('horse')
box_3[1], box_10[0] = box_10[0], box_3[1]
box_11.extend(['toothpaste', 'coin', 'pants'])
box_1[3], box_8[2] = box_8[2], box_1[3]
box_6[3], box_5[0] = box_5[0], box_6[3]
box_8.extend(['scissors', 'shoes', 'telescope'])
box_13[1], box_7[0] = box_7[0], box_13[1]
box_4.remove('river')
box_2.append('river')
box_11[1], box_10[1] = box_10[1], box_11[1]
box_1[3], box_8[2] = box_8[2], box_1[3]
box_10.clear()
box_10.extend(['perfume', 'helmet', 'glasses'])
box_13.extend(['battery', 'controller', 'necklace'])
box_11.remove('toothpaste')
box_11.remove('plate')
box_11.remove('horn')
box_5.extend(['boot', 'rain', 'comet'])
box_6[1], box_14[0] = box_14[0], box_6[1]
box_11[2], box_7[1] = box_7[1], box_11[2]
box_10.remove('perfume')
box_10.remove('helmet')
box_10.remove('glasses')
box_8.extend(['glasses', 'helmet', 'perfume'])
box_5.remove('comet')
box_4.append('comet')
box_12[1], box_5[2] = box_5[2], box_12[1]

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
print("Box 14:", box_14)