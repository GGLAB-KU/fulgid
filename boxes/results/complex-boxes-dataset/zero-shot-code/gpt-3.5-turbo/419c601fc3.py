box_0 = ['snow']
box_1 = ['meteor', 'plate', 'glove', 'bear']
box_2 = ['starfish', 'island', 'comet', 'paint', 'bracelet']
box_3 = ['fork', 'bag', 'gloves', 'watch']
box_4 = ['shirt', 'tie', 'earring', 'tree', 'wig']
box_5 = []
box_6 = ['star', 'car']
box_7 = ['perfume']
box_8 = ['bus', 'shampoo', 'submarine', 'chair']
box_9 = ['coat']
box_10 = []
box_11 = ['vase', 'table']
box_12 = ['pants', 'storm']

box_4.remove('tree')
box_4.remove('earring')
box_4.remove('shirt')
box_4.append('flower')
box_4.append('lipstick')
box_4.append('soap')

box_7.remove('perfume')
box_11.remove('table')
box_11.append('perfume')
box_12.remove('vase')
box_12.append('storm')
box_11 = []

box_12.remove('pants')
box_12.append('whistle')
box_12.append('mixer')

box_3.remove('gloves')
box_5.append('gloves')

box_2.remove('bracelet')
box_2.remove('starfish')
box_4.append('bracelet')
box_4.append('starfish')

box_9.append('rock')
box_9.append('paint')
box_9.append('freezer')

box_9.remove('freezer')
box_9.remove('rock')
box_9.remove('paint')

box_4.remove('starfish')
box_4.remove('wig')
box_4.remove('bracelet')

box_10.append('wig')
box_10.append('pot')
box_10.append('mask')

box_7.remove('table')
box_3.append('table')

box_0.append('necklace')
box_0.append('camera')
box_0.append('bicycle')

box_12.remove('whistle')

box_1.remove('meteor')
box_1.remove('glove')
box_5.append('meteor')
box_5.append('glove')
box_5.remove('gloves')

box_5.append('submarine')
box_5.append('chair')
box_8.remove('submarine')
box_8.remove('chair')

box_0.append('cat')

box_5 = []
box_0 = []

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