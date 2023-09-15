box_0 = ['car', 'bowl', 'sun']
box_1 = ['key', 'usb', 'bag']
box_2 = ['oven', 'button']
box_3 = ['jacket', 'toaster', 'tape']
box_4 = ['boat', 'shorts', 'glasses', 'bicycle', 'train']
box_5 = ['ring', 'swimsuit']
box_6 = ['coin', 'rock']
box_7 = []
box_8 = ['telescope', 'mountain', 'lamp', 'bracelet', 'shampoo']
box_9 = ['rain', 'toy', 'pants']

print("Initial State:")
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

box_4.extend(['ocean', 'towel', 'candle'])
box_3[0] = 'storm'
box_9.extend(box_8[1:4])
box_1.remove('bag')
box_1.remove('usb')
box_1.remove('key')
box_6.append(box_9.pop(box_9.index('lamp')))
box_5.extend([box_2.pop(0), box_2.pop(0)])
box_8.clear()
box_6[box_6.index('lamp')] = box_9.pop(box_9.index('shampoo'))
box_6.remove('coin')
box_6.remove('rock')
box_4.remove('bicycle')
box_4.remove('shorts')
box_1.extend([box_0.pop(box_0.index('car')), box_0.pop(box_0.index('bowl'))])
box_4[box_4.index('ocean')] = 'sculpture'
box_4[box_4.index('towel')] = 'drum'
box_7.extend(['cloud', 'truck', 'wig'])
box_1[box_1.index('bowl')] = box_9.pop(box_9.index('toy'))
box_9.remove('pants')

print("\nFinal State:")
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