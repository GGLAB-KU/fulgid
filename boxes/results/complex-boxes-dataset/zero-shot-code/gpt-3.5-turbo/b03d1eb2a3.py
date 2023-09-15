box_0 = ['bicycle', 'boat', 'horn', 'tie', 'toaster']
box_1 = ['sock', 'boot', 'coat', 'bear', 'gloves']
box_2 = ['coin', 'dolphin', 'plane']
box_3 = ['microwave']
box_4 = ['jacket']
box_5 = ['belt', 'rock']
box_6 = []
box_7 = ['wallet', 'harmonica', 'thunder']
box_8 = []

# Remove the boat from Box 0
box_0.remove('boat')

# Move the horn and the toaster from Box 0 to Box 4
box_4.extend(['horn', 'toaster'])
box_0.remove('horn')
box_0.remove('toaster')

# Empty Box 3
box_3.clear()

# Move the toaster from Box 4 to Box 8
box_8.append(box_4.pop())

# Put the grass into Box 6
box_6.append('grass')

# Replace the horn with the fork in Box 4
box_4.remove('horn')
box_4.append('fork')

# Put the scissors and the sandals into Box 0
box_0.extend(['scissors', 'sandals'])

# Move the dolphin from Box 2 to Box 8
box_8.append(box_2.pop(1))

# Put the jungle and the mountain into Box 4
box_4.extend(['jungle', 'mountain'])

# Move the boot and the coat and the sock from Box 1 to Box 2
box_2.extend(box_1[:3])
box_1 = box_1[3:]

# Move the rock from Box 5 to Box 7
box_7.append(box_5.pop())

# Put the fish and the pot into Box 2
box_2.extend(['fish', 'pot'])

# Replace the grass with the coat in Box 6
box_6.remove('grass')
box_6.append('coat')

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