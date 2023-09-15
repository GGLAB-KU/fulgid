box_0 = ['puzzle', 'bicycle']
box_1 = ['violin', 'freezer', 'earring']
box_2 = ['polish', 'vase', 'brush']
box_3 = ['grinder', 'truck']
box_4 = ['note', 'butterfly', 'laptop', 'plate', 'lightning']
box_5 = ['starfish', 'apple', 'horn', 'wig']
box_6 = ['speaker', 'thunder', 'card', 'ocean']
box_7 = ['bowl']
box_8 = ['glasses']
box_9 = ['pan', 'telescope', 'dice', 'shoes']
box_10 = ['magnet', 'blanket', 'table', 'candle', 'fridge']
box_11 = ['fish', 'book', 'bracelet', 'microwave']

box_3.extend(['ship', 'console', 'rocket'])
box_0.remove('puzzle')
box_0.remove('bicycle')
box_3.extend(['puzzle', 'bicycle'])
box_10.remove('magnet')
box_2.remove('polish')
box_6.remove('ocean')
box_10 = []
box_6.append('butterfly')
box_1.remove('freezer')
box_1.remove('earring')
box_1.remove('violin')
box_6.remove('thunder')
box_4.remove('note')
box_3.extend(['keyboard', 'necklace'])
box_3.remove('ship')
box_3.remove('console')
box_3.append('fridge')
box_6.remove('speaker')
box_6.remove('note')
box_2.extend(['speaker', 'note'])
box_6.remove('butterfly')
box_6.append('whistle')
box_5.extend(['keyboard', 'ring'])
box_2.extend(['plane', 'bell'])
box_7.remove('bowl')
box_7.append('usb')
box_1.extend(['wallet', 'basket'])
box_4.remove('laptop')
box_6.remove('card')
box_4.append('card')
box_3.remove('fridge')
box_3.append('lamp')

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