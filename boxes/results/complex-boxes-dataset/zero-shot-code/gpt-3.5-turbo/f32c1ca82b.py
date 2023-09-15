box_0 = ['horn']
box_1 = ['octopus']
box_2 = ['fish', 'microwave']
box_3 = ['ocean', 'candle', 'needle']
box_4 = ['rain', 'makeup', 'cat']
box_5 = ['tie', 'book', 'boat']
box_6 = ['dolphin', 'microscope', 'towel', 'piano']
box_7 = ['mask', 'soap']
box_8 = ['river', 'dog', 'vase']
box_9 = ['coat', 'watch', 'blanket']
box_10 = ['leaf', 'fork', 'elephant']
box_11 = ['guitar', 'harmonica', 'apple', 'bear']
box_12 = ['table', 'belt', 'shorts', 'planet']
box_13 = ['pan', 'pen', 'helmet', 'crown', 'battery']
box_14 = ['freezer', 'laptop', 'spoon', 'grinder', 'boot']

box_14.extend(['boot', 'pot'])
box_5.remove('book')
box_12.remove('table')
box_12.remove('belt')
box_6.remove('piano')
box_6.extend(['telescope', 'scarf', 'console'])
box_7.extend(['key', 'game', 'desert'])
box_6.remove('telescope')
box_6.remove('console')
box_6.extend(['ship', 'meteor'])
box_7.remove('desert')
box_12.remove('planet')
box_0.remove('horn')
box_1.append('horn')
box_11.append('flower')
box_7.remove('game')
box_9.append('game')
box_3.remove('candle')
box_3.remove('ocean')
box_3.remove('needle')
box_11.remove('guitar')
box_14.remove('freezer')
box_14.append('guitar')
box_3.extend(['planet', 'key', 'soap'])
box_9.remove('coat')
box_9.remove('blanket')
box_2.remove('fish')
box_4.remove('rain')
box_12.append('planet')
box_12.append('soap')
box_2.append('microwave')
box_14.remove('mask')
box_7.append('oven')
box_12.extend(['rock', 'controller', 'island'])
box_12.extend(['hat', 'pen', 'branch'])
box_7.remove('oven')

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