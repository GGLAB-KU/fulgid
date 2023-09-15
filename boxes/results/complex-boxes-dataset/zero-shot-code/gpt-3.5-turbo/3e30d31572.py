box_0 = ['planet', 'grass']
box_1 = ['flower', 'butterfly', 'button', 'starfish', 'toy']
box_2 = []
box_3 = ['card', 'plate', 'shampoo', 'wire', 'towel']
box_4 = []
box_5 = ['tree']
box_6 = ['perfume', 'shoe', 'brush', 'comb']
box_7 = ['magnet', 'lock']
box_8 = ['dress', 'soap', 'seaweed', 'necklace', 'flute']

# Swap wire in Box 3 with shoe in Box 6
box_3[3], box_6[1] = box_6[1], box_3[3]

# Replace brush, perfume, and comb with scarf, jungle, and jacket in Box 6
box_6[2:5] = ['scarf', 'jungle', 'jacket']

# Move tree from Box 5 to Box 3
box_3.append(box_5.pop())

# Swap lock in Box 7 with shoe in Box 3
box_7[1], box_3[3] = box_3[3], box_7[1]

# Move flower from Box 1 to Box 2
box_2.append(box_1.pop(0))

# Move dress, necklace, and flute from Box 8 to Box 6
box_6.extend(box_8[0:3])
del box_8[0:3]

# Move grass and planet from Box 0 to Box 3
box_3.extend(box_0)
del box_0[:]

# Put controller and pillow into Box 5
box_5.extend(['controller', 'pillow'])

# Put elephant, paint, and skirt into Box 3
box_3.extend(['elephant', 'paint', 'skirt'])

# Replace grass with pan in Box 3
box_3[box_3.index('grass')] = 'pan'

# Replace starfish with tape in Box 1
box_1[box_1.index('starfish')] = 'tape'

# Move pillow from Box 5 to Box 6
box_6.append(box_5.pop())

# Remove seaweed from Box 8
box_8.remove('seaweed')

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