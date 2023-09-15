box_0 = ['console', 'cow', 'shoes', 'sun', 'toaster']
box_1 = ['rock', 'telescope', 'soap', 'snow', 'toothpaste']
box_2 = ['shorts', 'boot', 'tape', 'scarf']
box_3 = ['mixer', 'moon']
box_4 = []
box_5 = []
box_6 = ['note', 'branch', 'book', 'cloud']

print("Initial State:")
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)

box_1.append('hat')
box_1.append('toothbrush')
box_1.append('sculpture')

box_5.append(box_0.pop(box_0.index('cow')))

box_1.append(box_3.pop(box_3.index('moon')))

box_0.extend(box_6.pop(box_6.index('cloud')))
box_0.extend(box_6.pop(box_6.index('branch')))
box_0.extend(box_6.pop(box_6.index('note')))

box_6.append(box_1.pop(box_1.index('hat')))

box_3[0], box_6[box_6.index('hat')] = box_6[box_6.index('hat')], box_3[0]

box_6[box_6.index('book')] = 'bicycle'

box_6.remove('bicycle')
box_3.remove('mixer')

box_2[box_2.index('tape')] = 'mirror'
box_2[box_2.index('boot')] = 'oven'
box_2[box_2.index('shorts')] = 'moon'

print("\nFinal State:")
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)