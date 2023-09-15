box_0 = []
box_1 = ['toy', 'cat', 'laptop', 'charger']
box_2 = ['key', 'oven', 'pen', 'pillow', 'razor']
box_3 = ['grass', 'shoe', 'needle', 'jungle', 'mask']
box_4 = ['beach', 'telescope', 'blanket', 'gloves']
box_5 = ['usb']
box_6 = []
box_7 = ['star', 'lightning']
box_8 = ['bracelet', 'car', 'rain', 'sock', 'umbrella']
box_9 = ['comb']
box_10 = []
box_11 = []
box_12 = []
box_13 = ['drum', 'coin']

box_8.remove('bracelet')
box_8.remove('rain')
box_13.remove('coin')

box_3[1], box_7[0] = box_7[0], box_3[1]

box_1.remove('cat')
box_1.remove('laptop')
box_1.remove('charger')

box_13.remove('drum')
box_4.remove('telescope')

box_6.append('blender')

box_2[1] = 'puzzle'

box_4.extend(['piano', 'grinder', 'speaker'])

box_3[3], box_7[0], box_3[4] = 'jacket', 'tie', 'harmonica'

box_5.remove('usb')

box_1.append('blender')

box_2[2], box_2[3], box_2[4] = 'hat', 'console', 'lion'

box_8[4], box_2[4] = box_2[4], box_8[4]

box_1.extend(['chair', 'soap'])

box_4[1], box_4[2], box_4[3] = 'skirt', 'shirt', 'coat'

box_8.remove('sock')

box_4.extend(['forest', 'motorcycle'])

box_9[0], box_1[0] = box_1[0], box_9[0]

box_7.remove('lightning')
box_10.append('shoe')
box_10.append('lightning')

box_4.remove('shirt')

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