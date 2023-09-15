box0 = ['river', 'bag', 'watch', 'cow']
box1 = ['coat', 'pen', 'train', 'lightning']
box2 = []
box3 = ['glasses', 'rocket', 'plane', 'makeup', 'wallet']
box4 = []

# Swap wallet in Box 3 with coat in Box 1
box3[box3.index('wallet')], box1[box1.index('coat')] = box1[box1.index('coat')], box3[box3.index('wallet')]

# Move makeup and glasses from Box 3 to Box 4
box4.extend([box3.pop(box3.index('makeup')), box3.pop(box3.index('glasses'))])

# Remove bag from Box 0
box0.remove('bag')

# Move river, watch, and cow from Box 0 to Box 4
box4.extend([box0.pop(box0.index('river')), box0.pop(box0.index('watch')), box0.pop(box0.index('cow'))])

# Replace rocket and plane with toaster and toy in Box 3
box3[box3.index('rocket')] = 'toaster'
box3[box3.index('plane')] = 'toy'

# Move cow and makeup from Box 4 to Box 3
box3.extend([box4.pop(box4.index('cow')), box4.pop(box4.index('makeup'))])

# Remove train and pen from Box 1
box1.remove('train')
box1.remove('pen')

# Swap river in Box 4 with makeup in Box 3
box4[box4.index('river')], box3[box3.index('makeup')] = box3[box3.index('makeup')], box4[box4.index('river')]

print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)
print("Box 4:", box4)