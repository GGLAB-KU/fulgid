box_0 = []
box_1 = []
box_2 = []
box_3 = ['cat', 'chair', 'fish']
box_4 = ['fridge', 'shorts', 'toaster', 'island']
box_5 = ['headphone', 'lion', 'wig']
box_6 = ['bus', 'mirror', 'gloves', 'piano']
box_7 = ['snow', 'soap', 'bear']
box_8 = ['toothbrush']
box_9 = ['razor', 'car']
box_10 = ['thread', 'pan']
box_11 = ['storm', 'shirt', 'dog', 'bird']

box_6.extend(['lion', 'planet', 'button'])
box_2.extend(box_6.remove('piano'))
box_2.extend(box_6.remove('gloves'))
box_2.extend(box_6.remove('button'))
box_8 = []
box_2.extend(box_10.remove('thread'))
box_2.remove('piano')
box_9.extend(['sun', 'plate'])
box_11 = ['seaweed', 'mixer', 'sculpture']
box_11 = ['bell', 'mask', 'basket']
box_11 = ['coin', 'grinder', 'basket']
box_5.extend(box_7.remove('snow'))
box_5.extend(box_7.remove('soap'))
box_5.extend(box_7.remove('bear'))
box_3, box_5 = box_5, box_3
box_6 = []
box_5.extend(box_4.remove('island'))
box_5.extend(box_4.remove('toaster'))
box_9, box_11 = box_11, box_9
box_0.extend(box_2.remove('gloves'))
box_0.extend(box_2.remove('button'))
box_0.extend(box_2.remove('thread'))
box_9, box_3 = box_3, box_9
box_6.extend(['keyboard', 'bracelet', 'seaweed'])

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