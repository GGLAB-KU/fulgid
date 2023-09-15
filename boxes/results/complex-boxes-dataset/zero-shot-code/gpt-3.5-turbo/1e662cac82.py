box_0 = []
box_1 = []
box_2 = ['sun', 'blanket']
box_3 = ['tie', 'ship', 'clock', 'tiger']
box_4 = ['dolphin', 'truck']
box_5 = ['plate', 'coat', 'speaker', 'wig']
box_6 = ['cow', 'usb', 'swimsuit']
box_7 = []
box_8 = []
box_9 = ['sandals']
box_10 = ['violin', 'charger', 'puzzle', 'keyboard', 'storm']
box_11 = []
box_12 = []
box_13 = ['necklace']
box_14 = ['crown', 'forest', 'button']

box_6.remove('usb')
box_6.remove('swimsuit')
box_6.extend(['ship', 'harmonica'])

box_14.remove('crown')
box_3.remove('tie')
box_14.append('tie')

box_5.extend(['cup', 'makeup', 'blender'])

box_13.remove('necklace')
box_9.remove('sandals')
box_13.append('sandals')

box_0 = []

box_13.append('rain')

box_14.append('submarine')

box_11.extend(['sun', 'blanket'])
box_2 = []

box_1.extend(['submarine', 'button'])
box_14.remove('submarine')
box_14.remove('button')

box_14.extend(['puzzle', 'violin'])
box_10 = []

box_6.remove('harmonica')
box_11.remove('sun')
box_11.remove('blanket')
box_1.extend(['blanket', 'harmonica'])

box_6 = []

box_13.extend(['dolphin', 'truck'])

box_5.extend(['horn', 'grass', 'harmonica'])

box_10.remove('charger')
box_10.append('hat')

box_9.extend(['boat', 'lock'])

box_14.remove('puzzle')
box_14.remove('violin')

box_3.remove('ship')
box_3.append('grinder')

box_10.remove('storm')
box_5.remove('cup')
box_10.append('cup')

box_3.extend(['glove', 'truck'])

box_10.remove('hat')
box_9.remove('boat')
box_10.append('boat')

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