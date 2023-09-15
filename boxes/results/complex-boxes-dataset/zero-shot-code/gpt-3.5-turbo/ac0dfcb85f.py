box_0 = ['cow', 'ship', 'pot', 'fish', 'towel']
box_1 = ['mirror']
box_2 = []
box_3 = ['bear', 'whistle']
box_4 = ['fork', 'grass', 'sun', 'tie', 'bird']
box_5 = ['charger', 'swimsuit', 'microwave']
box_6 = ['comb', 'coat', 'boot', 'battery']
box_7 = []
box_8 = ['branch', 'shark', 'bag']

box_8.extend(['apple', 'toothbrush', 'shampoo'])
box_8.remove('shampoo')
box_8.remove('toothbrush')
box_8.remove('branch')

box_4[box_4.index('grass')], box_3[box_3.index('bear')] = box_3[box_3.index('bear')], box_4[box_4.index('grass')]
box_3.clear()

box_0.remove('ship')
box_0[box_0.index('fish')], box_1[box_1.index('mirror')] = box_1[box_1.index('mirror')], box_0[box_0.index('fish')]
box_1.remove('mirror')

box_5[box_5.index('charger')], box_5[box_5.index('swimsuit')], box_5[box_5.index('microwave')] = 'umbrella', 'violin', 'coat'

box_8[box_8.index('apple')] = 'freezer'

box_1[box_1.index('fish')], box_4[box_4.index('fork')] = box_4[box_4.index('fork')], box_1[box_1.index('fish')]

box_8[box_8.index('bag')] = 'tie'

box_6.extend(['coat', 'tape'])

box_4[box_4.index('tie')], box_5[box_5.index('coat')] = box_5[box_5.index('coat')], box_4[box_4.index('tie')]

box_6[box_6.index('boot')], box_5[box_5.index('umbrella')] = box_5[box_5.index('umbrella')], box_6[box_6.index('boot')]

print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)
print("Box 8:", box_8)