box_0 = ['mask', 'crown', 'sock', 'starfish']
box_1 = ['storm', 'gloves', 'mixer']
box_2 = ['wig', 'cup', 'swimsuit', 'violin', 'mirror']
box_3 = ['sandals', 'telescope', 'lock']
box_4 = ['camera', 'truck']
box_5 = ['magnet', 'jacket']

box_3.remove('sandals')
box_3.remove('telescope')
box_3.remove('lock')

box_2.clear()

box_4[box_4.index('camera')] = 'magnet'
box_5[box_5.index('magnet')] = 'camera'

box_1.extend(['elephant', 'clock'])

box_4[box_4.index('truck')] = 'fridge'

box_4[box_4.index('fridge')] = 'camera'
box_5[box_5.index('camera')] = 'fridge'

box_4[box_4.index('camera')] = 'jacket'
box_5[box_5.index('jacket')] = 'camera'

box_0[box_0.index('mask')] = 'jacket'
box_0.remove('jacket')

print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)