box_0 = ['speaker', 'ship']
box_1 = ['headphone', 'shorts', 'fish', 'wig', 'microscope']
box_2 = ['lipstick', 'spoon', 'phone', 'shark', 'octopus']
box_3 = ['frame', 'bowl', 'violin']
box_4 = ['blanket', 'scissors', 'necklace', 'magnet', 'book']

box_2.remove('shark')
box_1.append('spoon')
box_4.extend(['mixer', 'clock', 'magnet'])
box_4.remove('clock')
box_2[box_2.index('octopus')], box_3[box_3.index('bowl')] = box_3[box_3.index('bowl')], box_2[box_2.index('octopus')]
box_1.remove('spoon')
box_1.remove('fish')
box_4[box_4.index('book')] = 'freezer'
box_3.remove('octopus')

print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)