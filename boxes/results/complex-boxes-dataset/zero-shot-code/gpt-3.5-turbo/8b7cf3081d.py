box_0 = ['thunder', 'plane', 'shark', 'flute', 'microscope']
box_1 = ['grass', 'swimsuit', 'headphone', 'elephant']
box_2 = ['mountain', 'pillow', 'dice']
box_3 = ['flower', 'tape', 'mirror', 'pen']
box_4 = []
box_5 = ['planet', 'grinder', 'comet', 'submarine', 'gloves']
box_6 = ['moon', 'wallet', 'oven']
box_7 = []
box_8 = ['cloud']
box_9 = ['battery']
box_10 = ['beach', 'earring', 'helmet']
box_11 = ['candle', 'mask']
box_12 = ['sculpture', 'bus']

box_9.remove('battery')
box_12[box_12.index('bus')], box_3[box_3.index('mirror')] = box_3[box_3.index('mirror')], box_12[box_12.index('bus')]
box_10[box_10.index('earring')], box_8[box_8.index('cloud')] = box_8[box_8.index('cloud')], box_10[box_10.index('earring')]
box_12[box_12.index('mirror')], box_0[box_0.index('flute')] = box_0[box_0.index('flute')], box_12[box_12.index('mirror')]
box_11.append(box_12.pop(box_12.index('sculpture')))
box_0.extend(['perfume', 'planet', 'pants'])
box_1[box_1.index('headphone')], box_1[box_1.index('grass')] = 'polish', 'towel'
box_12.append('snow')
box_12.append('chair')
box_12.append('basket')
box_12.remove('snow')
box_0.append('pillow')
box_10.extend(['swimsuit', 'zipper', 'wig'])
box_6.clear()
box_11[box_11.index('candle')], box_12[box_12.index('basket')] = box_12[box_12.index('basket')], box_11[box_11.index('candle')]
box_0.extend(['skirt', 'shoe', 'bracelet'])
box_2.clear()
box_1[box_1.index('swimsuit')], box_1[box_1.index('fridge')] = 'sun', 'brush'
box_3[box_3.index('tape')], box_1[box_1.index('brush')] = box_1[box_1.index('brush')], box_3[box_3.index('tape')]

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