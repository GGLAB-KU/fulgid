box_0 = ['zipper', 'blanket', 'coral', 'bag']
box_1 = ['basket', 'shoes']
box_2 = ['glasses', 'microscope']
box_3 = ['bus']
box_4 = []
box_5 = ['sculpture', 'hat', 'vase', 'shirt', 'mirror']
box_6 = []
box_7 = ['clock']
box_8 = ['tree', 'shark', 'lion']
box_9 = ['belt', 'scissors', 'desert', 'button', 'book']
box_10 = ['flower', 'coat', 'fork', 'ship']

# Move the zipper and the bag from Box 0 to Box 6
box_6.extend([box_0.pop(box_0.index('zipper')), box_0.pop(box_0.index('bag'))])

# Put the glasses and the starfish and the bus into Box 7
box_7.extend([box_2.pop(box_2.index('glasses')), box_3.pop(box_3.index('bus'))])

# Swap the coral in Box 0 with the basket in Box 1
box_0[box_0.index('coral')], box_1[box_1.index('basket')] = box_1[box_1.index('basket')], box_0[box_0.index('coral')]

# Swap the vase in Box 5 with the shark in Box 8
box_5[box_5.index('vase')], box_8[box_8.index('shark')] = box_8[box_8.index('shark')], box_5[box_5.index('vase')]

# Swap the bus in Box 3 with the tree in Box 8
box_3[box_3.index('bus')], box_8[box_8.index('tree')] = box_8[box_8.index('tree')], box_3[box_3.index('bus')]

# Replace the basket and the blanket with the branch and the lipstick in Box 0
box_0[box_0.index('basket')] = 'branch'
box_0[box_0.index('blanket')] = 'lipstick'

# Put the crown and the thunder and the thread into Box 3
box_3.extend(['crown', 'thunder', 'thread'])

# Replace the coral with the perfume in Box 1
box_1[box_1.index('coral')] = 'perfume'

# Swap the mirror in Box 5 with the ship in Box 10
box_5[box_5.index('mirror')], box_10[box_10.index('ship')] = box_10[box_10.index('ship')], box_5[box_5.index('mirror')]

# Put the bowl and the wallet into Box 10
box_10.extend(['bowl', 'wallet'])

# Replace the lion with the toy in Box 8
box_8[box_8.index('lion')] = 'toy'

# Swap the book in Box 9 with the perfume in Box 1
box_9[box_9.index('book')], box_1[box_1.index('perfume')] = box_1[box_1.index('perfume')], box_9[box_9.index('book')]

# Move the microscope from Box 2 to Box 3
box_3.append(box_2.pop(box_2.index('microscope')))

# Replace the mirror with the butterfly in Box 10
box_10[box_10.index('mirror')] = 'butterfly'

# Swap the clock in Box 7 with the tree in Box 3
box_7[box_7.index('clock')], box_3[box_3.index('tree')] = box_3[box_3.index('tree')], box_7[box_7.index('clock')]

# Replace the bus and the vase with the planet and the wig in Box 8
box_8[box_8.index('bus')] = 'planet'
box_8[box_8.index('vase')] = 'wig'

# Remove the wallet and the bowl from Box 10
box_10.remove('wallet')
box_10.remove('bowl')

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
print("Box 9:", box_9)
print("Box 10:", box_10)