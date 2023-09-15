box_0 = ['button', 'bird', 'island', 'pillow']
box_1 = ['lock', 'belt', 'usb', 'puzzle', 'microscope']
box_2 = []
box_3 = ['cloud', 'coin', 'ocean', 'key']
box_4 = ['starfish', 'controller', 'clock']
box_5 = ['bag']
box_6 = ['dog', 'sock', 'fork', 'watch', 'towel']
box_7 = ['submarine', 'camera', 'train', 'beach', 'car']
box_8 = ['shoe', 'desert']

print("Initial State:")
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)
print("Box 8:", box_8)

box_5.extend(box_4)
box_5.remove('starfish')
box_5.remove('controller')
box_5.remove('clock')

box_8.remove('shoe')
box_8.append('train')
box_8.remove('desert')

box_6.clear()
box_8.clear()

box_6.extend(box_5)
box_5.clear()

box_8.extend(['toothbrush', 'tape', 'horse'])

box_1.remove('puzzle')

box_5.clear()

box_3.append(box_1.pop(box_1.index('belt')))

box_8.remove('toothbrush')

box_1[box_1.index('usb')], box_7[box_7.index('car')] = box_7[box_7.index('car')], box_1[box_1.index('usb')]

box_6.append(box_7.pop(box_7.index('camera')))

print("\nFinal State:")
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)
print("Box 8:", box_8)