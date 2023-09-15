box_0 = []
box_1 = ['usb', 'flute', 'pen', 'sandals', 'violin']
box_2 = ['ocean', 'table', 'leaf', 'toaster', 'clock']
box_3 = ['flute', 'pen', 'sock']
box_4 = ['camera', 'elephant', 'oven', 'star']
box_5 = ['glasses', 'mixer', 'ring', 'bird', 'swimsuit']
box_6 = ['meteor', 'horn', 'jungle', 'moon']
box_7 = ['wig', 'perfume', 'car', 'horse', 'guitar']
box_8 = ['charger', 'jacket', 'doll', 'horn']
box_9 = ['lightning', 'crown', 'controller']
box_10 = ['card', 'harmonica', 'laptop', 'toothpaste']
box_11 = ['hat', 'pot']
box_12 = ['leaf', 'belt', 'spoon']
box_13 = ['blender', 'toothbrush', 'piano']
box_14 = ['coin']

box_3.remove('polish')
box_14.append('book')
box_2.extend(['leaf', 'toaster', 'clock'])
box_1.remove('flute')
box_1.remove('pen')
box_1.extend(['sock', 'thread'])
box_7.remove('horse')
box_7.remove('wig')
box_2.extend(['star', 'elephant', 'oven'])
box_8.extend(['charger', 'jacket', 'doll'])
box_14.append('coin')
box_11.append('watch')
box_0.extend(['sandals', 'usb'])
box_4.remove('camera')
box_5.remove('swimsuit')
box_5.remove('mixer')
box_5.remove('bird')
box_6.remove('tiger')
box_6.extend(['meteor', 'horn', 'jungle', 'moon'])
box_8.remove('charger')
box_8.remove('doll')
box_2.remove('oven')
box_8.append('horn')
box_1.extend(['book', 'coin'])
box_11.extend(['hat', 'pot'])
box_1.remove('thread')
box_1.remove('book')
box_1.remove('sock')

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