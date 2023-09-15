box_0 = []
box_1 = ['horse', 'tree', 'soap']
box_2 = []
box_3 = ['shoe', 'candle']
box_4 = ['bag', 'chair', 'polish', 'branch', 'scarf']
box_5 = ['doll']
box_6 = ['puzzle', 'usb', 'bus']
box_7 = []
box_8 = ['wallet', 'beach', 'ship', 'wire', 'sandals', 'toy']
box_9 = ['shoes', 'battery']
box_10 = ['jungle', 'clock', 'telescope', 'console', 'spoon']

box_5.remove('boot')
box_2.remove('toothbrush')
box_9.append('toothbrush')
box_3.remove('candle')
box_3.remove('shoe')
box_8.extend(['candle', 'shoe'])
box_1 = ['belt', 'helmet']
box_1.remove('game')
box_1.remove('soap')
box_6.remove('zipper')
box_6.append('puzzle')
box_5.remove('skirt')
box_6.append('sock')
box_0.append('magnet')
box_6.remove('puzzle')
box_6.remove('usb')
box_6.remove('sock')
box_6.extend(['swimsuit', 'usb', 'bus'])
box_8.extend(['wire', 'sandals', 'toy'])
box_7.append('horn')
box_7.remove('horn')
box_6.extend(['wire', 'perfume'])
box_5.remove('skirt')

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