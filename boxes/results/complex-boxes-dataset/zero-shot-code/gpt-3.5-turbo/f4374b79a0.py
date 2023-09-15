box_0 = ['dress']
box_1 = ['swimsuit', 'toothbrush', 'towel', 'ocean', 'gloves']
box_2 = []
box_3 = ['glasses', 'snow']
box_4 = ['rock', 'seaweed']
box_5 = ['needle']
box_6 = ['game', 'coral', 'grass', 'wig']
box_7 = ['scarf', 'horn', 'octopus', 'razor']
box_8 = ['lion', 'freezer']
box_9 = ['boot']
box_10 = ['moon', 'earring', 'card', 'frame']
box_11 = ['motorcycle', 'bowl', 'magnet']
box_12 = ['mask']

box_2.append('sandals')
box_9.remove('boot')
box_6[0], box_10[1] = box_10[1], box_6[0]
box_11.append(box_1.pop(box_1.index('toothbrush')))
box_4.append('coral')
box_7.extend(['shoes', 'lock'])
box_8.append(box_5.pop(box_5.index('needle')))
box_4.append(box_1.pop(box_1.index('ocean')))
box_6[1:3] = ['sculpture', 'magnet']
box_4.extend(['shoe', 'lock'])
box_0[0], box_11[0] = box_11[0], box_0[0]
box_3[0], box_4[1] = box_4[1], box_3[0]
box_8.extend([box_7.pop(box_7.index('lion')), box_7.pop(box_7.index('needle'))])
box_4.append('butterfly')
box_8[0] = 'fridge'
box_11[1], box_12[0] = box_12[0], box_11[1]
box_9.append('console')
box_1.remove('swimsuit')
box_1.remove('towel')
box_1.remove('gloves')
box_9.append(box_0.pop(box_0.index('toothbrush')))

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