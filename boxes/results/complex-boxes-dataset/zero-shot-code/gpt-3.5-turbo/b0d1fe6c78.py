box_0 = []
box_1 = []
box_2 = []
box_3 = []
box_4 = []
box_5 = []
box_6 = []
box_7 = []

box_1.append('fish')
box_2.append('sandals')
box_1.extend(['cloud', 'basket', 'guitar'])
box_4.append('makeup')
box_5.append('drum')
box_4.extend(['horn', 'dog'])
box_3.extend(['zipper', 'belt', 'cat'])
box_5.remove('drum')
box_6.extend(['drum', 'horn', 'dog'])
box_2.remove('sandals')
box_3.extend(['ring', 'plane', 'bicycle'])
box_1.remove('cloud')
box_1.remove('guitar')
box_1.extend(['toothbrush', 'sandals'])
box_2.remove('fish')
box_3.extend(['tiger', 'fish'])
box_1.remove('toothbrush')
box_1.remove('sandals')
box_1.extend(['shark', 'ship', 'desert'])
box_6.remove('dog')
box_6.remove('horn')
box_6.remove('drum')
box_2.remove('flute')
box_3.append('ring')
box_1.remove('shark')
box_1.extend(['candle'])

print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)