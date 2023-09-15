box_0 = []
box_1 = ['wire', 'bird', 'shoes', 'basket', 'card']
box_2 = []
box_3 = []
box_4 = ['note', 'button']
box_5 = ['blender', 'whistle', 'ring']
box_6 = ['spoon']
box_7 = ['needle']
box_8 = ['toy', 'fridge', 'book']

print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)
print("Box 8:", box_8)

# Move the needle from Box 7 to Box 6
box_6.append(box_7.pop())

# Put the razor and the beach and the river into Box 6
box_6.extend(['razor', 'beach', 'river'])

# Replace the button with the bicycle in Box 4
box_4.remove('button')
box_4.append('bicycle')

# Put the coral and the basket and the starfish into Box 1
box_1.extend(['coral', 'basket', 'starfish'])

# Remove the basket and the shoes and the card from Box 2
box_2.clear()

# Replace the coral with the microwave in Box 1
box_1.remove('coral')
box_1.append('microwave')

# Replace the wire and the basket and the microwave with the harmonica and the keyboard and the bell in Box 1
box_1.remove('wire')
box_1.remove('basket')
box_1.remove('microwave')
box_1.extend(['harmonica', 'keyboard', 'bell'])

# Move the river from Box 6 to Box 0
box_0.append(box_6.pop(box_6.index('river')))

# Move the book from Box 8 to Box 4
box_4.append(box_8.pop(box_8.index('book')))

# Swap the river in Box 0 with the beach in Box 6
box_0.append(box_6.pop(box_6.index('beach')))
box_6.append('river')

# Put the motorcycle into Box 5
box_5.append('motorcycle')

# Replace the fridge and the toy with the console and the zipper in Box 8
box_8.remove('fridge')
box_8.remove('toy')
box_8.extend(['console', 'zipper'])

# Remove the console from Box 8
box_8.remove('console')

print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)
print("Box 8:", box_8)