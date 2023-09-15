box_0 = ['bell', 'coat', 'toaster', 'lamp']
box_1 = ['meteor']
box_2 = ['usb', 'ship']
box_3 = ['jacket', 'puzzle', 'scissors', 'island', 'bracelet']
box_4 = ['flute', 'microscope']
box_5 = []
box_6 = ['plate']

# Replace microscope and flute with bear and tape in Box 4
box_4.remove('microscope')
box_4.remove('flute')
box_4.append('bear')
box_4.append('tape')

# Move bell, coat, and lamp from Box 0 to Box 2
box_0.remove('bell')
box_0.remove('coat')
box_0.remove('lamp')
box_2.append('bell')
box_2.append('coat')
box_2.append('lamp')

# Swap meteor in Box 1 with plate in Box 6
box_1.remove('meteor')
box_6.remove('plate')
box_1.append('plate')
box_6.append('meteor')

# Remove meteor from Box 6
box_6.remove('meteor')

# Put leaf into Box 4
box_4.append('leaf')

# Replace plate with dress in Box 1
box_1.remove('plate')
box_1.append('dress')

# Put needle into Box 4
box_4.append('needle')

# Replace island with train in Box 3
box_3.remove('island')
box_3.append('train')

# Swap toaster in Box 0 with needle in Box 4
box_0.remove('toaster')
box_4.remove('needle')
box_0.append('needle')
box_4.append('toaster')

# Replace usb and ship with submarine and lock in Box 2
box_2.remove('usb')
box_2.remove('ship')
box_2.append('submarine')
box_2.append('lock')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)