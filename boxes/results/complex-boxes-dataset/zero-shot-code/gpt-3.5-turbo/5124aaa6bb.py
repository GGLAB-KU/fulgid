box_0 = []
box_1 = ['octopus']
box_2 = []
box_3 = []
box_4 = ['mountain', 'freezer', 'basket']
box_5 = ['cup', 'bird', 'gloves', 'forest']
box_6 = []
box_7 = ['fork', 'planet']
box_8 = ['leaf', 'usb', 'note', 'rocket', 'toothpaste']
box_9 = []
box_10 = ['motorcycle', 'hat', 'lion']
box_11 = []
box_12 = ['moon']
box_13 = ['spoon', 'zipper']

box_12.extend(['chair', 'plane', 'lamp'])
box_8 = ['mask', 'telescope', 'beach']
box_4.append('grass')
box_3.append(box_8.pop(0))
box_3.remove('mask')
box_13[1] = 'lock'
box_1[0] = 'sun'
box_12.extend(['headphone', 'razor', 'necklace'])
box_8[1] = box_5.pop(0)
box_12 = ['whistle', 'ocean']
box_8.remove('rocket')
box_7[1] = box_13.pop(1)
box_7.extend(['console', 'pants'])
box_0.append(box_1.pop(0))
box_1.extend([box_8.pop(0), box_5.pop(0), box_5.pop(0)])
box_13.remove('planet')
box_13.remove('spoon')
box_11.extend([box_10.pop(0), box_10.pop(0)])
box_10[1] = box_8.pop(1)
box_4.extend(['beach', 'blanket'])
box_1.extend(['horn', 'usb'])

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