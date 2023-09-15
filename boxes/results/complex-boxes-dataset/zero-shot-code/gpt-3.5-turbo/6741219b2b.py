box_0 = ['desert', 'octopus', 'drum', 'key', 'tie']
box_1 = ['bear', 'telescope', 'flower']
box_2 = []
box_3 = ['pen', 'starfish', 'candle', 'battery']
box_4 = []
box_5 = ['scarf', 'oven', 'paint']
box_6 = ['bracelet', 'flute', 'shoes', 'swimsuit']
box_7 = ['usb', 'bowl', 'harmonica']
box_8 = ['tape', 'hat', 'keyboard']

box_8.remove('hat')
box_6.extend(['bus', 'keyboard'])
box_7.extend(['pillow', 'shoe', 'console'])
box_5[box_5.index('scarf')], box_7[box_7.index('harmonica')] = box_7[box_7.index('harmonica')], box_5[box_5.index('scarf')]
box_3[box_3.index('candle')], box_3[box_3.index('battery')] = 'pants', 'button'
box_0[box_0.index('drum')], box_0[box_0.index('tie')], box_0[box_0.index('octopus')] = 'microscope', 'pot', 'sculpture'
box_2.extend(['bell', 'shelf', 'bicycle'])
box_8.remove('tape')
box_2.extend(['coin', 'watch', 'scissors'])
box_5[box_5.index('paint')] = 'candle'
box_5.remove('candle')
box_6[box_6.index('bus')] = 'skirt'
box_0[box_0.index('sculpture')], box_7[box_7.index('shoe')] = box_7[box_7.index('shoe')], box_0[box_0.index('sculpture')]
box_5[box_5.index('oven')], box_6[box_6.index('bracelet')] = box_6[box_6.index('bracelet')], box_5[box_5.index('oven')]

print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)
print("Box 8:", box_8)