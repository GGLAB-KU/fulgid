box_0 = ['plane', 'usb', 'wire', 'star']
box_1 = ['gloves']
box_2 = ['submarine', 'speaker', 'shoe', 'pillow']
box_3 = ['camera', 'leaf']
box_4 = ['violin', 'cow', 'pants', 'lion', 'paint']
box_5 = ['necklace', 'boot']
box_6 = ['oven', 'lock', 'piano', 'phone']
box_7 = []
box_8 = []
box_9 = ['perfume', 'charger', 'plate']
box_10 = ['scissors']
box_11 = ['button', 'harmonica', 'planet', 'guitar', 'shampoo']
box_12 = ['towel', 'puzzle', 'scarf']
box_13 = ['game', 'fork', 'doll']
box_14 = ['dice', 'hat']

box_4.remove('cow')
box_3.extend(['boot', 'ship'])
box_4.remove('lion')
box_4.remove('paint')
box_13.extend(['lion', 'paint'])
box_6.extend(['puzzle', 'scarf'])
box_11.extend(['cow', 'bag', 'bracelet'])
box_12[box_12.index('star')] = 'towel'
box_13.remove('fork')
box_5.clear()
box_10[box_10.index('scissors')] = 'pillow'
box_0.remove('pants')
box_1.append('perfume')
box_14.extend(['plane', 'pants', 'wire'])
box_4[box_4.index('violin')] = 'shoe'
box_14.remove('hat')
box_6[box_6.index('phone')] = 'game'
box_2[box_2.index('submarine')] = 'sculpture'
box_9[box_9.index('charger')] = 'pillow'
box_2.clear()
box_10.remove('charger')
box_0.remove('usb')
box_1.extend(['towel', 'usb'])
box_13[box_13.index('doll')] = 'star'
box_9.extend(['zipper', 'pillow'])

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