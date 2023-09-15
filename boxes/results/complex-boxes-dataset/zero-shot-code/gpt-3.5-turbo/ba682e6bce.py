box_0 = ['lock', 'crown']
box_1 = ['shark']
box_2 = []
box_3 = []
box_4 = ['keyboard', 'pan', 'skirt', 'apple']
box_5 = ['car', 'blanket', 'plane', 'bowl']
box_6 = ['moon', 'hat', 'fridge', 'sun', 'console']
box_7 = ['gloves', 'mountain', 'cat', 'cup', 'phone']
box_8 = ['wig', 'mask', 'meteor', 'soap']
box_9 = ['flower', 'octopus', 'rain', 'chair']
box_10 = ['bear']

box_1.remove('shark')
box_9.remove('flower')
box_10.extend(['fridge', 'moon'])
box_5.extend(['crown', 'lock'])
box_0.remove('fridge')
box_2.append('fridge')
box_5.clear()
box_3.extend(['bell', 'sun', 'earring'])
box_6.extend(['bracelet', 'bird', 'toy'])
box_1.extend(['mask', 'meteor', 'soap'])
box_3.remove('bell')
box_3.remove('earring')
box_3.extend(['bus', 'comb'])
box_8.extend(['fridge', 'flute'])
box_4.remove('pan')
box_7.extend(['gloves', 'flute'])
box_9.clear()

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