box_0 = ['helmet', 'sandals']
box_1 = []
box_2 = ['tiger', 'key', 'train', 'spoon']
box_3 = []
box_4 = ['soap', 'forest', 'bus', 'submarine']
box_5 = []
box_6 = ['pan', 'oven', 'butterfly']
box_7 = ['scissors', 'dice', 'toy', 'motorcycle']
box_8 = ['brush', 'drum', 'pillow', 'mountain', 'tape']
box_9 = ['meteor', 'button', 'keyboard', 'jacket', 'phone']
box_10 = ['mirror', 'coat']

# Remove the forest, soap, and bus from Box 4
box_4.remove('forest')
box_4.remove('soap')
box_4.remove('bus')

# Swap the submarine in Box 4 with the brush in Box 8
submarine = box_4.pop()
brush = box_8.pop()
box_4.append(brush)
box_8.append(submarine)

# Replace the scissors, motorcycle, and toy with the sculpture, bear, and rocket in Box 7
scissors = box_7.pop(0)
motorcycle = box_7.pop()
toy = box_7.pop()
box_7.extend(['sculpture', 'bear', 'rocket'])

# Move the submarine from Box 8 to Box 0
submarine = box_8.pop()
box_0.append(submarine)

# Move the sculpture and dice from Box 7 to Box 4
sculpture = box_7.pop(0)
dice = box_7.pop(0)
box_4.extend([sculpture, dice])

# Swap the oven in Box 6 with the jacket in Box 9
oven = box_6.pop(1)
jacket = box_9.pop(3)
box_6.append(jacket)
box_9.append(oven)

# Replace the jacket, pan, and butterfly with the shoe, comet, and coin in Box 6
jacket = box_6.pop(1)
pan = box_6.pop(1)
butterfly = box_6.pop()
box_6.extend(['shoe', 'comet', 'coin'])

# Remove the spoon, key, and train from Box 2
box_2.remove('spoon')
box_2.remove('key')
box_2.remove('train')

# Move the mirror from Box 10 to Box 2
mirror = box_10.pop(0)
box_2.append(mirror)

# Swap the mirror in Box 2 with the coat in Box 10
mirror = box_2.pop()
coat = box_10.pop()
box_2.append(coat)
box_10.append(mirror)

# Replace the phone with the ocean in Box 9
phone = box_9.pop(3)
box_9.append('ocean')

# Put the comet and vase into Box 1
comet = box_1.pop()
vase = box_1.pop()
box_1.extend(['comet', 'vase'])

# Replace the comet and vase with the rock and tree in Box 1
comet = box_1.pop(0)
vase = box_1.pop(0)
box_1.extend(['rock', 'tree'])

# Move the button and keyboard from Box 9 to Box 1
button = box_9.pop(1)
keyboard = box_9.pop(1)
box_1.extend(['button', 'keyboard'])

# Move the meteor from Box 9 to Box 0
meteor = box_9.pop(0)
box_0.append(meteor)

# Remove the tiger and coat from Box 2
box_2.remove('tiger')
box_2.remove('coat')

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