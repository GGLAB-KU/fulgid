box_0 = ['flute', 'comb', 'card', 'cup']
box_1 = ['coin']
box_2 = ['bicycle', 'river', 'towel', 'lamp']
box_3 = []
box_4 = ['shoes', 'bracelet', 'thread', 'controller']
box_5 = ['planet', 'pants']
box_6 = []

# Remove the coin from Box 1
box_1.remove('coin')

# Move the river and the towel from Box 2 to Box 3
box_3.extend(box_2[1:3])
box_2 = box_2[:1] + box_2[3:]

# Replace the river with the sun in Box 3
box_3[0] = 'sun'

# Replace the lamp with the pen in Box 2
box_2[2] = 'pen'

# Swap the shoes in Box 4 with the towel in Box 3
box_4[0], box_3[1] = box_3[1], box_4[0]

# Put the keyboard and the headphone and the tiger into Box 4
box_4.extend(['keyboard', 'headphone', 'tiger'])

# Empty Box 0
box_0 = []

# Remove the thread from Box 4
box_4.remove('thread')

# Move the pants from Box 5 to Box 2
box_2.extend(box_5[1:])
box_5 = box_5[:1]

# Replace the bracelet and the tiger and the towel with the vase and the grinder and the headphone in Box 4
box_4[1:4] = ['vase', 'grinder', 'headphone']

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)