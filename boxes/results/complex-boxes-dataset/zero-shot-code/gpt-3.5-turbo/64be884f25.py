box_0 = ['plane', 'camera', 'bear']
box_1 = []
box_2 = []
box_3 = ['candle', 'island']
box_4 = ['coral', 'submarine']
box_5 = []
box_6 = ['planet']
box_7 = ['grass', 'cat']
box_8 = ['dress']
box_9 = ['drum', 'toothpaste', 'table']
box_10 = ['fork']
box_11 = ['sculpture', 'flute']
box_12 = ['doll', 'wig', 'motorcycle', 'octopus', 'fish']
box_13 = ['hat', 'violin', 'mixer']
box_14 = []

box_13 = []

box_12.remove('fish')
box_12.remove('octopus')
box_12.remove('motorcycle')
box_12.append('speaker')
box_12.append('bracelet')
box_12.append('rock')

box_12.remove('speaker')
box_12.remove('doll')
box_12.remove('bracelet')
box_12.append('mask')
box_12.append('plate')
box_12.append('dog')

box_10.extend(['plane', 'bear'])
box_10.remove('bear')
box_10.remove('plane')
box_10.remove('fork')

box_12.remove('mask')
box_12.append('lightning')

box_6.remove('planet')

box_0.remove('camera')

box_9.remove('drum')
box_9.remove('table')
box_9.remove('toothpaste')
box_9.append('spoon')
box_9.append('dog')
box_9.append('thunder')

box_11, box_3 = box_3, box_11

box_1.append('fish')

box_9, box_4 = box_4, box_9

box_11, box_4 = box_4, box_11

box_5.extend(['skirt', 'elephant', 'wallet'])

box_12.remove('lightning')

box_5, box_9 = box_9, box_5

box_5.remove('skirt')
box_5.append('rain')
box_5.append('frame')
box_5.append('puzzle')

box_8, box_5 = box_5, box_8

box_5.remove('rain')
box_5.append('dress')

box_1.remove('fish')

box_12.remove('wig')
box_12.append('cup')

box_9.remove('skirt')
box_9.remove('spoon')
box_9.append('grinder')
box_9.append('violin')

box_8, box_7 = box_7, box_8

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