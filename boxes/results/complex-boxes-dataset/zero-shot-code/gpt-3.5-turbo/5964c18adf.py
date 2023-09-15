box_0 = []
box_1 = []
box_2 = ['button', 'forest', 'motorcycle']
box_3 = ['sock', 'cloud', 'comet', 'bicycle']
box_4 = []
box_5 = ['battery', 'ship', 'towel', 'speaker', 'telescope']
box_6 = ['bus', 'coral', 'thread', 'blender', 'console']
box_7 = ['bird']
box_8 = []

# Put the lock and the chair and the horn into Box 3
box_3.extend(['lock', 'chair', 'horn'])

# Put the mixer and the scissors and the shampoo into Box 8
box_8.extend(['mixer', 'scissors', 'shampoo'])

# Swap the chair in Box 3 with the wallet in Box 0
box_0.append(box_3.pop(box_3.index('chair')))
box_3.append(box_0.pop(box_0.index('wallet')))

# Put the cloud and the button into Box 4
box_4.extend(['cloud', 'button'])

# Remove the bowl from Box 1
box_1.remove('bowl')

# Put the mirror and the cup and the fork into Box 1
box_1.extend(['mirror', 'cup', 'fork'])

# Remove the scissors and the mixer from Box 8
box_8.remove('scissors')
box_8.remove('mixer')

# Put the sandals into Box 8
box_8.append('sandals')

# Put the blanket into Box 0
box_0.append('blanket')

# Remove the shampoo from Box 8
box_8.remove('shampoo')

# Remove the sock and the horn and the lock from Box 3
box_3.remove('sock')
box_3.remove('horn')
box_3.remove('lock')

# Replace the ship and the battery with the watch and the cloud in Box 5
box_5.remove('ship')
box_5.remove('battery')
box_5.extend(['watch', 'cloud'])

# Empty Box 0
box_0.clear()

# Move the button from Box 4 to Box 0
box_0.append(box_4.pop(box_4.index('button')))

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