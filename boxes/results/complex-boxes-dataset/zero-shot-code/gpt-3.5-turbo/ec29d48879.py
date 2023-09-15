box_0 = ['magnet', 'bell', 'mixer', 'moon']
box_1 = ['drum', 'keyboard', 'oven', 'lock']
box_2 = ['mirror', 'bowl', 'headphone', 'razor']
box_3 = ['table']
box_4 = ['forest', 'butterfly', 'frame', 'wig', 'lightning']
box_5 = []
box_6 = ['violin', 'button', 'controller']
box_7 = ['coat', 'bicycle', 'mask', 'pillow']
box_8 = ['car', 'dress']
box_9 = []
box_10 = ['phone']
box_11 = []
box_12 = ['earring', 'hat', 'meteor']
box_13 = []

box_8.remove('dress')
box_8.remove('car')
box_3.remove('table')
box_5.append(box_7.pop(box_7.index('bicycle')))
box_6.extend([box_4.pop(box_4.index('wig')), box_4.pop(box_4.index('lightning')), box_4.pop(box_4.index('forest'))])
box_5.remove('bicycle')
box_6.append(box_10.pop(box_10.index('phone')))
box_13.extend([box_1.pop(box_1.index('drum')), box_1.pop(box_1.index('lock')), box_1.pop(box_1.index('oven'))])
box_9.extend([box_0.pop(box_0.index('magnet')), box_0.pop(box_0.index('moon'))])
box_8.extend(['doll', 'watch'])
box_1[box_1.index('keyboard')] = 'controller'
box_8.append('train')
box_6.clear()
box_0.append(box_2.pop(box_2.index('mirror')))
box_9.extend(['watch', 'microwave'])
box_13.extend(['sock', 'leaf'])
box_11.extend(['car', 'gloves', 'shelf'])
box_0.clear()
box_13[box_13.index('sock')] = box_2.pop(box_2.index('razor'))
box_4.remove('frame')
box_4.remove('butterfly')
box_7[box_7.index('coat')] = 'zipper'
box_7[box_7.index('pillow')] = 'skirt'
box_12.remove('earring')

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