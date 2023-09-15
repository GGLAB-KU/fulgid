box_0 = []
box_1 = ['dress', 'bicycle', 'flute']
box_2 = ['polish', 'game', 'seaweed', 'table', 'meteor']
box_3 = []
box_4 = ['drum', 'cow', 'toaster', 'crown']
box_5 = []
box_6 = ['spoon', 'phone', 'glove', 'boot', 'bear', 'plane', 'flute']
box_7 = ['leaf', 'card', 'coin', 'button', 'towel', 'fish']
box_8 = ['dice', 'wig', 'boot', 'toothbrush']

box_1.remove('gloves')
box_1.remove('clock')
box_7.remove('shorts')
box_8.remove('dice')
box_4.remove('dice')
box_4.append('drum')
box_6.extend(['boot', 'bear'])
box_7.append('paint')
box_0.remove('bell')
box_6.extend(['cow', 'toaster', 'crown'])
box_6.extend(['plane', 'flute', 'spoon'])
box_8.extend(['wig', 'boot', 'toothbrush'])
box_5.remove('dice')
box_5.remove('sock')
box_4.append('flute')
box_7.remove('coin')
box_7.remove('elephant')
box_7.extend(['towel', 'fish'])
box_4.append('flute')

print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)
print("Box 8:", box_8)