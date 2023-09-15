box_0 = ['toy']
box_1 = ['necklace', 'jungle', 'bowl', 'coin']
box_2 = []
box_3 = ['wig', 'star', 'horn', 'drum']
box_4 = ['cow', 'shoes']
box_5 = ['lipstick', 'snow', 'ocean', 'rocket']
box_6 = ['elephant', 'shoe', 'umbrella']
box_7 = ['shorts', 'butterfly']
box_8 = ['game', 'doll', 'belt']

box_4.extend(['helmet', 'bird'])
box_0.remove('toy')
box_7.remove('shorts')
box_3[1], box_5[1] = box_5[1], box_3[1]
box_5.remove('rocket')
box_6.append(box_7.pop())
box_8[0], box_1[1] = box_1[1], box_8[0]
box_4.extend([box_1.pop(1), box_8.pop(2)])
box_3[1:4] = ['speaker', 'octopus', 'wire']
box_4[0:3] = ['swimsuit', 'rock', 'battery']
box_5.remove('star')
box_8[1] = 'button'
box_4[1], box_6[2] = box_6[2], box_4[1]

print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)
print("Box 8:", box_8)