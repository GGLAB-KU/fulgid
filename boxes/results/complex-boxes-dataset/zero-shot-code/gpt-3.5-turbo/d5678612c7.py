box_0 = []
box_1 = ['whistle']
box_2 = ['cow', 'watch']
box_3 = ['comb']
box_4 = ['fridge']
box_5 = ['dolphin', 'usb']
box_6 = ['rain', 'meteor', 'toothbrush']
box_7 = ['tape', 'magnet', 'motorcycle']
box_8 = ['branch']
box_9 = ['towel', 'phone']
box_10 = ['mirror', 'mask', 'controller', 'ship', 'wallet']
box_11 = ['bus']
box_12 = ['forest', 'snow']
box_13 = ['leaf']
box_14 = ['soap']

box_3.extend(['blanket', 'doll', 'clock'])
box_0 = box_11
box_7.remove('magnet')
box_4, box_10[0] = box_10[0], box_4
box_11.remove('bus')
box_3.remove('comb')
box_10.extend(['jungle', 'forest', 'soap'])
box_2.remove('watch')
box_7[0], box_5[0] = box_5[0], box_7[0]
box_13, box_2[0] = box_2[0], box_13[0]
box_4.remove('mirror')
box_3[-1] = 'hat'
box_5.append('toothbrush')
box_8.remove('branch')
box_0 = []
box_1.append('branch')
box_6[0], box_9[0] = box_9[0], box_6[0]
box_12.append('note')
box_7.append('zipper')
box_12.extend([box_7.pop(), box_7.pop()])
box_6[0], box_9[1] = box_9[1], box_6[0]

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