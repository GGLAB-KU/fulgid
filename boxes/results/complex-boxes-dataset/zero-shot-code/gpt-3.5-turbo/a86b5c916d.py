box_0 = ['grass', 'basket']
box_1 = []
box_2 = ['earring', 'desert', 'keyboard', 'rain', 'coat']
box_3 = ['button', 'coral', 'doll', 'wig']
box_4 = ['freezer', 'frame', 'whistle', 'lock', 'belt']
box_5 = ['watch', 'plane', 'moon', 'flower']
box_6 = ['cat', 'sculpture', 'dice', 'elephant']
box_7 = ['glasses', 'dog']
box_8 = []
box_9 = ['seaweed', 'train', 'book']
box_10 = ['bag', 'submarine', 'clock']
box_11 = ['truck', 'pants', 'octopus', 'flute']
box_12 = []
box_13 = ['boat', 'puzzle']

box_13.remove('boat')
box_13.remove('puzzle')
box_9.remove('book')
box_9.append('sandals')
box_7.remove('glasses')
box_7.append('shorts')
box_7.remove('shorts')
box_7.remove('dog')
box_4.append(box_0.pop(0))
box_4.append(box_0.pop(0))
box_5.remove('flower')
box_5.remove('plane')
box_12.append('flower')
box_12.append('plane')
box_9.remove('sandals')
box_9.remove('train')
box_3[1], box_10[1] = box_10[1], box_3[1]
box_11.extend(['leaf', 'soap'])
box_4.remove('belt')
box_4.remove('frame')
box_10.append('belt')
box_10.append('frame')
box_12.remove('flower')
box_12.remove('plane')
box_8.append('flower')
box_8.append('plane')
box_0.extend(['horn', 'wig', 'island'])
box_8.extend(['skirt', 'pen', 'bus'])
box_11.remove('truck')
box_2.remove('keyboard')
box_1.append('keyboard')
box_3.remove('wig')
box_3.append('usb')
box_11.remove('octopus')
box_11.append('shorts')
box_8.remove('pen')
box_8.remove('skirt')
box_3.remove('usb')
box_3.remove('button')
box_3.remove('submarine')
box_10.extend(['pen', 'key', 'shark'])
box_10.remove('bag')
box_10.remove('clock')
box_10.remove('frame')
box_6.append('keyboard')

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