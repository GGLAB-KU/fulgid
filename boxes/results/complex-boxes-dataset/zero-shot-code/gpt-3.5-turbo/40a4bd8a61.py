box_0 = ['zipper', 'mirror', 'magnet', 'polish', 'vase']
box_1 = ['thread']
box_2 = ['camera', 'clock', 'guitar']
box_3 = ['battery', 'bowl', 'thunder', 'charger', 'earring']
box_4 = ['horn']
box_5 = ['lock', 'necklace', 'coin']
box_6 = []
box_7 = ['violin', 'boot']
box_8 = ['doll']
box_9 = ['fridge', 'star']
box_10 = ['perfume', 'starfish', 'cat', 'umbrella', 'blanket']

box_10.remove('perfume')
box_10.remove('starfish')
box_10.append('coin')
box_10.append('earring')

box_6.append('brush')

box_8.remove('doll')

box_4.remove('horn')
box_4.append('console')

box_1.append('magnet')
box_1.append('needle')

box_9.remove('fridge')
box_9.remove('star')
box_3.append('fridge')
box_3.append('star')

box_5.remove('necklace')
box_10.remove('blanket')
box_5.append('blanket')
box_10.append('necklace')

box_1.remove('magnet')
box_1.remove('needle')
box_6.append('magnet')
box_6.append('needle')

box_7.remove('violin')

box_3.remove('thunder')
box_4.remove('console')
box_3.append('console')
box_4.append('thunder')

box_2.append('submarine')
box_2.append('sculpture')

box_10.remove('cat')
box_10.remove('umbrella')
box_10.remove('earring')
box_10.append('plate')
box_10.append('battery')
box_10.append('thunder')

box_2.append('puzzle')
box_2.append('cat')
box_2.append('bowl')

box_2.remove('bowl')
box_3.remove('star')
box_2.append('star')

box_3.remove('charger')
box_4.remove('console')
box_3.append('ocean')
box_3.append('basket')

box_5.remove('blanket')
box_8.append('blanket')

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