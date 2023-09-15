box0 = ['comb', 'console', 'lion', 'submarine']
box1 = ['speaker']
box2 = ['river', 'controller']
box3 = ['flute', 'needle', 'shirt', 'cat', 'lipstick']
box4 = []
box5 = ['violin', 'ship', 'fork']
box6 = ['truck', 'coin', 'gloves', 'piano']

# Swap speaker in Box 1 with river in Box 2
box1.remove('speaker')
box2.remove('river')
box1.append('river')
box2.append('speaker')

# Swap cat in Box 3 with piano in Box 6
box3.remove('cat')
box6.remove('piano')
box3.append('piano')
box6.append('cat')

# Put necklace, toaster, and cup into Box 6
box6.extend(['necklace', 'toaster', 'cup'])

# Remove ship, violin, and fork from Box 5
box5.remove('ship')
box5.remove('violin')
box5.remove('fork')

# Move comb and submarine from Box 0 to Box 1
box0.remove('comb')
box0.remove('submarine')
box1.extend(['comb', 'submarine'])

# Put island into Box 0
box0.append('island')

# Move comb, river, and submarine from Box 1 to Box 2
box1.remove('comb')
box1.remove('river')
box1.remove('submarine')
box2.extend(['comb', 'river', 'submarine'])

# Swap truck in Box 6 with island in Box 0
box6.remove('truck')
box0.remove('island')
box6.append('island')
box0.append('truck')

# Remove gloves and coin from Box 6
box6.remove('gloves')
box6.remove('coin')

# Put toaster, speaker, and river into Box 5
box5.extend(['toaster', 'speaker', 'river'])

# Swap speaker in Box 5 with needle in Box 3
box5.remove('speaker')
box3.remove('needle')
box5.append('needle')
box3.append('speaker')

# Print the contents of each box
print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)
print("Box 4:", box4)
print("Box 5:", box5)
print("Box 6:", box6)