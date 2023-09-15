box_0 = ['chair']
box_1 = []
box_2 = ['fish']
box_3 = ['meteor', 'dice', 'thread']
box_4 = ['razor', 'necklace']
box_5 = ['earring', 'needle', 'horse', 'makeup', 'comet']
box_6 = ['violin', 'umbrella', 'lamp']

box_6.append('shampoo')
box_6.remove('umbrella')
box_6.remove('violin')
box_6.remove('lamp')
box_6.extend(['snow', 'forest', 'spoon'])

box_5.remove('earring')
box_0.extend(['speaker', 'thunder'])

box_6.append(box_2.pop())

box_1.extend([box_5.pop(1), box_5.pop(2)])

box_0.remove('speaker')
box_1.clear()

box_4.remove('razor')
box_4.remove('necklace')
box_4.extend(['candle', 'laptop'])

box_3.append('mirror')

print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)