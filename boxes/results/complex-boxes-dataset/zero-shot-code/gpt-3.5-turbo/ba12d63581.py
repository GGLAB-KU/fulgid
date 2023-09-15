box_0 = ['desert', 'book', 'toothbrush', 'sculpture']
box_1 = ['microwave', 'flower', 'boat', 'magnet']
box_2 = ['seaweed', 'submarine']
box_3 = ['card']
box_4 = []
box_5 = ['butterfly', 'console', 'telescope']
box_6 = ['wig', 'helmet', 'fish']
box_7 = ['elephant', 'sandals', 'beach', 'necklace']
box_8 = ['mixer']
box_9 = ['ocean', 'lipstick', 'zipper', 'usb', 'soap']
box_10 = ['button', 'scissors', 'river', 'puzzle', 'oven']

box_7.remove('sandals')
box_7.remove('elephant')
box_7.append('puzzle')
box_7.append('pants')

box_7.remove('puzzle')
box_7.remove('beach')
box_7.remove('pants')

box_6.remove('fish')
box_9.remove('soap')
box_6.append('soap')

box_0.remove('sculpture')
box_0.remove('desert')
box_0.append('hat')
box_0.append('shirt')

box_1.append(box_0.pop(3))

box_5.append('flower')

box_0.remove('hat')
box_0.remove('shirt')
box_0.remove('book')
box_0.append('plane')

box_0, box_1 = box_1, box_0

box_7.extend(box_2.pop(0))
box_7.extend(box_2.pop(0))

box_9.append(box_0.pop(3))

box_6.remove('wig')

box_10.remove('puzzle')
box_10.append('beach')

box_0.append('wig')

box_8.extend(['table', 'crown'])

box_10.extend(box_1.pop(1))
box_10.extend(box_1.pop(1))
box_10.extend(box_1.pop(1))

box_10.remove('beach')
box_6.append('helmet')

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