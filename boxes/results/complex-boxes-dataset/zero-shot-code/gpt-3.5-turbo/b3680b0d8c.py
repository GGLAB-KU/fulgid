box_0 = []
box_1 = ['bracelet', 'desert', 'tiger']
box_2 = ['gloves', 'tape']
box_3 = ['scarf', 'frame']
box_4 = ['forest', 'elephant', 'plate', 'watch', 'umbrella']
box_5 = ['scissors', 'phone', 'cat', 'coin']
box_6 = []
box_7 = []
box_8 = []
box_9 = ['toaster']
box_10 = ['bear', 'clock', 'necklace', 'needle']

box_9 = ['toaster']
box_2, box_9 = box_9, box_2
box_10.extend(['battery', 'dolphin'])
box_0.append('dolphin')
box_1[2], box_5[0] = box_5[0], box_1[2]
box_1.remove('scissors')
box_4.extend(['flower', 'dolphin', 'telescope'])
box_3.append('seaweed')
box_3.remove('frame')
box_3.remove('scarf')
box_2, box_0 = box_0, box_2
box_4, box_1 = box_1, box_4
box_5[3], box_4[2] = box_4[2], box_5[3]
box_2.append('dolphin')
box_1.append('forest')
box_1.append('watch')
box_5[2], box_4[4] = box_4[4], box_5[2]
box_2.remove('dolphin')
box_0.append('fridge')
box_2, box_5 = box_5, box_2
box_0 = ['train']

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