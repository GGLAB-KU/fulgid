box_0 = []
box_1 = ['glove']
box_2 = ['harmonica', 'magnet', 'lipstick', 'game']
box_3 = ['ocean', 'motorcycle', 'sculpture', 'jacket', 'butterfly']
box_4 = ['dolphin', 'microwave', 'doll', 'shoes']
box_5 = []
box_6 = ['moon', 'thunder', 'gloves']
box_7 = ['sun', 'key', 'paint']
box_8 = ['battery', 'rock', 'dog', 'charger', 'mask']

box_8.remove('rock')
box_8.remove('dog')

box_2.remove('harmonica')
box_2.remove('game')
box_2.append('bird')
box_2.append('truck')

box_4.remove('shoes')
box_4.remove('microwave')
box_4.remove('doll')
box_4.append('shampoo')
box_4.append('cloud')
box_4.append('bicycle')

box_5.extend(box_3)
box_3.clear()

box_2[box_2.index('bird')], box_6[box_6.index('thunder')] = box_6[box_6.index('thunder')], box_2[box_2.index('bird')]

box_5.append(box_8.pop(box_8.index('mask')))
box_5.append(box_8.pop(box_8.index('charger')))

box_2.append('swimsuit')
box_2.append('battery')

box_4.remove('cloud')
box_4.remove('bicycle')
box_4.remove('shampoo')
box_4.append('tie')
box_4.append('speaker')
box_4.append('watch')

box_2.remove('swimsuit')
box_2.remove('battery')

box_7.append('shirt')
box_7.append('submarine')

box_8.append(box_7.pop(box_7.index('key')))
box_8.append(box_7.pop(box_7.index('sun')))
box_8.append(box_7.pop(box_7.index('paint')))

box_2[box_2.index('battery')], box_8[box_8.index('battery')] = box_8[box_8.index('battery')], box_2[box_2.index('battery')]

box_2[box_2.index('glove')], box_1[box_1.index('thunder')] = box_1[box_1.index('thunder')], box_2[box_2.index('glove')]

box_1.append('magnet')
box_1.append('tie')

print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)
print("Box 8:", box_8)