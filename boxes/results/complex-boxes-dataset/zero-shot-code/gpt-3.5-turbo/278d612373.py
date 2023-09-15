box_0 = []
box_1 = ['table', 'zipper', 'blender']
box_2 = []
box_3 = ['shampoo', 'skirt', 'usb']
box_4 = ['shoes']
box_5 = ['comet', 'fork']
box_6 = ['boat', 'charger', 'pants', 'hat']
box_7 = ['branch', 'cloud', 'pen', 'whistle']
box_8 = ['jungle', 'watch', 'pot']
box_9 = []
box_10 = ['meteor', 'battery', 'grinder', 'rain', 'freezer']
box_11 = []
box_12 = ['console', 'piano', 'clock', 'shark', 'bell']
box_13 = ['toy', 'game']
box_14 = ['drum']

box_8.remove('pot')
box_8.remove('watch')
box_8.remove('jungle')

box_7.remove('pen')
box_7.remove('cloud')
box_7.remove('branch')
box_7.append('puzzle')
box_7.append('note')
box_7.append('drum')

box_4.remove('shoes')
box_4.append('blender')

box_7.append('charger')

box_6.remove('pants')
box_6.remove('hat')
box_11.append('pants')
box_11.append('hat')

box_14.remove('drum')
box_14.append('clock')

box_4.remove('blender')
box_4.append('toy')

box_5.remove('comet')
box_5.append('toy')

box_7.remove('charger')
box_7.append('rain')

box_5.remove('fork')
box_10.append('fork')

box_3.remove('shampoo')
box_3.remove('skirt')
box_3.remove('usb')

box_11.remove('hat')
box_6.remove('boat')
box_6.append('hat')

box_14.remove('clock')

box_5.remove('toy')
box_5.append('shoe')

box_5.remove('shoe')
box_7.append('shoe')

box_1.extend(['camera', 'swimsuit', 'lamp'])

box_6.remove('charger')
box_6.remove('hat')

box_10.remove('battery')
box_4.append('battery')

box_10.remove('meteor')
box_4.append('meteor')

box_5.remove('drum')
box_5.append('bird')

box_13.remove('game')
box_10.append('game')

box_4.remove('meteor')
box_10.append('meteor')

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