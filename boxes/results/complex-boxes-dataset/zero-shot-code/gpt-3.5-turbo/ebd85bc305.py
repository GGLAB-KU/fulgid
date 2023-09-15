box_0 = ['bird', 'button', 'microscope', 'thunder', 'horse']
box_1 = ['console', 'toothbrush', 'controller', 'storm']
box_2 = ['belt', 'snow', 'leaf', 'hat']
box_3 = ['river', 'guitar', 'magnet', 'perfume', 'cow']
box_4 = ['watch']
box_5 = ['mirror', 'key', 'pants', 'grinder', 'car']
box_6 = []
box_7 = []
box_8 = ['desert', 'planet', 'whistle']

# Move toothbrush and storm from Box 1 to Box 4
box_4.extend([box_1.pop(box_1.index('toothbrush')), box_1.pop(box_1.index('storm'))])

# Remove button, bird, and thunder from Box 0
box_0.remove('button')
box_0.remove('bird')
box_0.remove('thunder')

# Replace controller and console with ship and thread in Box 1
box_1.remove('controller')
box_1.remove('console')
box_1.extend(['ship', 'thread'])

# Remove ship and thread from Box 1
box_1.remove('ship')
box_1.remove('thread')

# Put cow and cloud into Box 7
box_7.extend(['cow', 'cloud'])

# Swap key in Box 5 with cloud in Box 7
box_5[box_5.index('key')] = box_7.pop(box_7.index('cloud'))

# Replace leaf, snow, and belt with pot, freezer, and key in Box 2
box_2.remove('leaf')
box_2.remove('snow')
box_2.remove('belt')
box_2.extend(['pot', 'freezer', 'key'])

# Put motorcycle into Box 5
box_5.append('motorcycle')

# Remove key and cow from Box 7
box_7.remove('key')
box_7.remove('cow')

# Remove whistle, desert, and planet from Box 8
box_8.remove('whistle')
box_8.remove('desert')
box_8.remove('planet')

# Put truck and bag into Box 2
box_2.extend(['truck', 'bag'])

# Move watch and storm from Box 4 to Box 7
box_7.extend([box_4.pop(box_4.index('watch')), box_4.pop(box_4.index('storm'))])

# Move toothbrush from Box 4 to Box 6
box_6.append(box_4.pop(box_4.index('toothbrush')))

# Move freezer, pot, and hat from Box 2 to Box 5
box_5.extend([box_2.pop(box_2.index('freezer')), box_2.pop(box_2.index('pot')), box_2.pop(box_2.index('hat'))])

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)
print("Box 8:", box_8)