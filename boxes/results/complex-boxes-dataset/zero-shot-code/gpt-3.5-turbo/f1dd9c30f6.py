box_0 = ['plate', 'truck', 'wig']
box_1 = ['tape', 'microwave', 'key', 'ring', 'cup']
box_2 = []
box_3 = ['ocean']
box_4 = ['rain', 'toothpaste', 'bicycle', 'cow']
box_5 = ['book', 'lipstick', 'whistle', 'coral']
box_6 = ['fork', 'starfish', 'bird', 'violin', 'planet']
box_7 = []
box_8 = ['thread']
box_9 = ['magnet', 'jacket', 'towel']
box_10 = ['tiger', 'seaweed']

# Replace items in Box 6
box_6 = ['toaster', 'forest', 'dress']

# Move plate from Box 0 to Box 5
box_5.append('plate')
box_0.remove('plate')

# Put shoes into Box 5
box_5.append('shoes')

# Put scissors, sun, and bird into Box 9
box_9.extend(['scissors', 'sun', 'bird'])

# Remove truck and wig from Box 0
box_0.remove('truck')
box_0.remove('wig')

# Move seaweed from Box 10 to Box 9
box_9.append(box_10.pop(box_10.index('seaweed')))

# Put leaf, rocket, and sock into Box 8
box_8.extend(['leaf', 'rocket', 'sock'])

# Swap shoes in Box 5 with tiger in Box 10
box_5.remove('shoes')
box_10.remove('tiger')
box_5.append('tiger')
box_10.append('shoes')

# Replace cup and key with gloves and tape in Box 1
box_1.remove('cup')
box_1.remove('key')
box_1.extend(['gloves', 'tape'])

# Remove microwave and gloves from Box 1
box_1.remove('microwave')
box_1.remove('gloves')

# Remove tape from Box 1
box_1.remove('tape')

# Empty Box 10
box_10 = []

# Swap toaster in Box 6 with ocean in Box 3
box_6.remove('toaster')
box_3.remove('ocean')
box_6.append('ocean')
box_3.append('toaster')

# Put brush, coin, and seaweed into Box 5
box_5.extend(['brush', 'coin', 'seaweed'])

# Move book from Box 5 to Box 1
box_1.append(box_5.pop(box_5.index('book')))

# Remove rain, toothpaste, and cow from Box 4
box_4.remove('rain')
box_4.remove('toothpaste')
box_4.remove('cow')

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