box_0 = ['shorts', 'lion']
box_1 = ['shoes', 'perfume', 'sculpture', 'towel', 'branch']
box_2 = ['magnet', 'key']
box_3 = ['scarf']
box_4 = []
box_5 = ['rain']
box_6 = []
box_7 = ['button', 'rock', 'piano', 'toy', 'wig']
box_8 = ['glasses', 'toothpaste', 'bell', 'pot']
box_9 = []
box_10 = ['glove', 'bird', 'book', 'guitar']
box_11 = ['tape', 'ocean', 'bag', 'sandals']
box_12 = ['shark']
box_13 = ['flower', 'shoe', 'thread']

box_11.remove('bag')
box_11.remove('sandals')
box_11.remove('ocean')
box_11.remove('tape')

box_8.remove('glasses')
box_8.remove('toothpaste')
box_10.append('glasses')
box_10.append('toothpaste')

box_0.remove('lion')
box_0.remove('shorts')
box_9.append('lion')
box_9.append('shorts')

box_12.remove('shark')

box_1.remove('shoes')
box_1.remove('perfume')
box_1.remove('sculpture')
box_9.append('shoes')
box_9.append('perfume')
box_9.append('sculpture')

box_4.extend(['jacket', 'spoon', 'shirt'])

box_4.remove('jacket')
box_4.remove('shirt')
box_4.append('bell')
box_4.append('candle')

box_10.remove('book')
box_10.append('mask')

box_5.remove('keyboard')
box_5.append('scissors')

box_5.remove('scissors')
box_9.append('scissors')

box_2.extend(['oven', 'toothpaste'])

box_4.remove('shirt')
box_4.remove('jacket')
box_4.append('bell')
box_4.append('candle')

box_10.remove('book')
box_10.append('mask')

box_5.remove('keyboard')
box_5.append('scissors')

box_5.remove('scissors')
box_9.append('scissors')

box_2.clear()

box_1.append('bowl')

box_1.remove('bowl')
box_5.append('bowl')

box_10.remove('guitar')
box_10.remove('glasses')
box_8.append('guitar')
box_8.append('glasses')

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