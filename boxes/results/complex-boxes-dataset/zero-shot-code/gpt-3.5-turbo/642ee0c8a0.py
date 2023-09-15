box_0 = []
box_1 = []
box_2 = ['key', 'jungle', 'battery', 'frame', 'drum']
box_3 = []
box_4 = ['pan', 'lipstick']
box_5 = ['crown', 'umbrella', 'leaf']
box_6 = []
box_7 = []
box_8 = ['beach', 'whistle']
box_9 = ['flower', 'pants', 'bowl', 'microwave']

# Swap beach and microwave
box_8, box_9 = box_9, box_8

# Remove flower from box 9
box_9.remove('flower')

# Move crown from box 5 to box 3
box_3.append(box_5.pop(box_5.index('crown')))

# Empty box 4 and box 9
box_4.clear()
box_9.clear()

# Move crown from box 3 to box 9
box_9.append(box_3.pop())

# Move microwave and whistle from box 8 to box 4
box_4.extend([box_8.pop(box_8.index('microwave')), box_8.pop(box_8.index('whistle'))])

# Move crown from box 9 to box 7
box_7.append(box_9.pop())

# Move crown from box 7 to box 1
box_1.append(box_7.pop())

# Remove leaf and umbrella from box 5
box_5.remove('leaf')
box_5.remove('umbrella')

# Empty box 2
box_2.clear()

# Swap crown in box 1 with whistle in box 4
box_1[0], box_4[box_4.index('whistle')] = box_4[box_4.index('whistle')], box_1[0]

# Replace whistle with vase in box 1
box_1[0] = 'vase'

# Remove vase from box 1
box_1.clear()

# Put hat, jacket, and towel into box 7
box_7.extend(['hat', 'jacket', 'towel'])

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