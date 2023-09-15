box_0 = ['fish', 'whistle', 'submarine', 'train']
box_1 = ['bird']
box_2 = []
box_3 = ['sun', 'harmonica']
box_4 = ['beach']
box_5 = ['boat', 'candle']
box_6 = ['sock']

print("Initial Boxes:")
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)

box_5.append('hat')
box_5.append(box_1.pop(0))
box_4.append(box_0.pop(box_0.index('whistle')))
box_3.append('shark')
box_5.extend(['scarf', 'submarine', 'branch'])
box_4.extend(['bicycle', 'microwave'])
box_3.extend(['star', 'flute'])
box_2.append(box_3.pop(box_3.index('sun')))
box_2.extend(['horn', 'planet'])
box_2 = []
box_1, box_5 = box_5, box_1

print("\nFinal Boxes:")
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)