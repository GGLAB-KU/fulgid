box0 = ['glove']
box1 = ['boot', 'forest', 'bell']
box2 = ['wig', 'motorcycle', 'scarf']
box3 = ['island']
box4 = ['ocean', 'vase', 'toy']

# Move rain and mountain to box2
box2.append('rain')
box2.append('mountain')

# Move rain, scarf, and mountain to box1
box1.append(box2.pop(box2.index('rain')))
box1.append(box2.pop(box2.index('scarf')))
box1.append(box2.pop(box2.index('mountain')))

# Move ocean and vase to box2
box2.append(box4.pop(box4.index('ocean')))
box2.append(box4.pop(box4.index('vase')))

# Remove glove from box0
box0.remove('glove')

# Replace toy with butterfly in box4
box4[box4.index('toy')] = 'butterfly'

# Put sock into box2
box2.append('sock')

# Replace island with earring in box3
box3[box3.index('island')] = 'earring'

# Print the contents of each box
print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)
print("Box 4:", box4)