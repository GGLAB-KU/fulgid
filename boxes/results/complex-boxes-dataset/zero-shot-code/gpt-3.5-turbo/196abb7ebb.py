box0 = ['cow', 'planet']
box1 = ['microscope', 'glove', 'helmet']
box2 = ['bell', 'shoe', 'desert', 'card', 'basket']
box3 = ['note', 'jungle', 'seaweed', 'toaster']
box4 = []
box5 = ['tiger', 'coin', 'tree']
box6 = ['sock', 'lipstick', 'river']

# Remove sock, lipstick, and river from Box 6
box6.remove('sock')
box6.remove('lipstick')
box6.remove('river')

# Swap cow in Box 0 with desert in Box 2
box0[0], box2[2] = box2[2], box0[0]

# Put shirt and dolphin into Box 3
box3.append('shirt')
box3.append('dolphin')

# Swap toaster in Box 3 with glove in Box 1
box3[3], box1[1] = box1[1], box3[3]

# Remove note from Box 3
box3.remove('note')

# Replace planet with shampoo in Box 0
box0[1] = 'shampoo'

# Remove microscope, toaster, and helmet from Box 1
box1.remove('microscope')
box1.remove('toaster')
box1.remove('helmet')

# Move card from Box 2 to Box 3
box2.remove('card')
box3.append('card')

# Swap shampoo in Box 0 with coin in Box 5
box0[1], box5[1] = box5[1], box0[1]

# Remove shoe from Box 2
box2.remove('shoe')

# Swap cow in Box 2 with coin in Box 0
box2[0], box0[0] = box0[0], box2[0]

# Print the contents of each box
print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)
print("Box 4:", box4)
print("Box 5:", box5)
print("Box 6:", box6)