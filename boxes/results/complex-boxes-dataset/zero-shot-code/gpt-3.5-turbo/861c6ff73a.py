box_0 = []
box_1 = []
box_2 = []
box_3 = ['sandals', 'lamp']
box_4 = ['comet', 'coral']
box_5 = ['necklace', 'lock', 'card', 'comb']
box_6 = ['butterfly', 'magnet']
box_7 = ['telescope', 'grass', 'mask', 'sculpture', 'makeup']
box_8 = ['planet', 'cloud', 'thunder']
box_9 = ['earring']
box_10 = ['plate', 'pants', 'seaweed', 'pillow', 'frame']
box_11 = ['note']

box_8.extend(['mirror', 'shoe', 'pants'])
box_9.extend(['zipper', 'mountain'])
box_6[box_6.index('magnet')] = 'coral'
box_4[box_4.index('coral')] = 'magnet'
box_4.append(box_11.pop())
box_3.extend(['flute', 'forest', 'snow'])
box_2.append(box_8.pop(box_8.index('thunder')))
box_1.extend(['book', 'storm', 'thread'])
box_7.extend(['makeup', 'charger'])
box_6[box_6.index('coral')] = 'thunder'
box_8.remove('cloud')
box_8[box_8.index('planet')] = 'storm'
box_4.append(box_8.pop(box_8.index('thunder')))
box_4.extend(['lion', 'dress', 'shelf'])
box_10[box_10.index('seaweed')] = 'blender'
box_10[box_10.index('plate')] = 'mask'
box_10[box_10.index('pillow')] = 'cow'
box_6.remove('telescope')
box_11.append('car')
box_8.clear()

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