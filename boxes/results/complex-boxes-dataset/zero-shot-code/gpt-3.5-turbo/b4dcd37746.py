box_0 = []
box_1 = ['grinder']
box_2 = ['shelf']
box_3 = ['dress', 'swimsuit']
box_4 = []
box_5 = ['button', 'piano', 'boat']
box_6 = ['glasses', 'glove', 'bear', 'belt']
box_7 = ['shoe', 'polish', 'umbrella', 'camera']
box_8 = ['cup', 'perfume', 'wire', 'card']
box_9 = ['shark', 'grass', 'toy', 'usb', 'microscope']
box_10 = ['scissors', 'vase']

box_9.extend(['whistle', 'oven'])
box_9.remove('usb')
box_7[2], box_8[0] = box_8[0], box_7[2]
box_8.remove('perfume')
box_8.remove('card')
box_3 = ['rock', 'laptop']
box_6 = ['toothbrush', 'paint', 'star', 'sandals']
box_3.extend(['microwave', 'river'])
box_8[2], box_8[3] = box_8[3], box_8[2]
box_7.extend(['train', 'camera'])
box_7.extend(box_3)
box_7.remove('shoe')
box_1.remove('grinder')
box_10.extend(['pants', 'starfish'])
box_9[2], box_5[2] = box_5[2], box_9[2]
box_2.remove('shelf')
box_6.remove('paint')
box_6.remove('star')
box_6.remove('sandals')
box_8.extend(['flute', 'bell'])

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