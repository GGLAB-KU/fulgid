box_0 = ['dice', 'grass', 'glasses']
box_1 = ['leaf', 'basket']
box_2 = ['bear', 'phone', 'laptop', 'plane', 'violin']
box_3 = ['zipper', 'jungle', 'dress']
box_4 = ['comb']
box_5 = ['headphone', 'cow']
box_6 = []

# Swap the grass in Box 0 with the plane in Box 2
box_0[1], box_2[3] = box_2[3], box_0[1]

# Replace the grass with the mountain in Box 2
box_2[1] = 'mountain'

# Swap the jungle in Box 3 with the glasses in Box 0
box_0[2], box_3[1] = box_3[1], box_0[2]

# Remove the laptop from Box 2
box_2.remove('laptop')

# Swap the plane in Box 0 with the phone in Box 2
box_0[1], box_2[1] = box_2[1], box_0[1]

# Remove the glasses and the zipper from Box 3
box_3.remove('glasses')
box_3.remove('zipper')

# Replace the violin with the thunder in Box 2
box_2[4] = 'thunder'

# Remove the comb from Box 4
box_4.remove('comb')

# Swap the dice in Box 0 with the headphone in Box 5
box_0[0], box_5[0] = box_5[0], box_0[0]

# Remove the leaf from Box 1
box_1.remove('leaf')

# Put the usb and the skirt and the violin into Box 1
box_1.extend(['usb', 'skirt', 'violin'])

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)