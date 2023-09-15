box_0 = ['table', 'dress', 'card']
box_1 = ['sculpture']
box_2 = ['tape', 'fridge', 'oven']
box_3 = []
box_4 = []
box_5 = ['toaster', 'cup', 'violin', 'ship', 'bell']
box_6 = ['island', 'cow', 'speaker']
box_7 = ['toothpaste', 'dog']
box_8 = ['soap', 'towel', 'glove']
box_9 = ['branch']
box_10 = ['coral', 'camera']

# Remove the table, card, and dress from Box 0
box_0.remove('table')
box_0.remove('card')
box_0.remove('dress')

# Move the toothpaste from Box 7 to Box 8
toothpaste = box_7.pop()
box_8.append(toothpaste)

# Put the belt and the sun into Box 3
box_3.append('belt')
box_3.append('sun')

# Move the branch from Box 9 to Box 6
branch = box_9.pop()
box_6.append(branch)

# Remove the toothpaste and the glove from Box 8
box_8.remove('toothpaste')
box_8.remove('glove')

# Put the coin, glove, and helmet into Box 7
box_7.append('coin')
box_7.append('glove')
box_7.append('helmet')

# Swap the fridge in Box 2 with the cup in Box 5
fridge = box_2.pop(box_2.index('fridge'))
cup = box_5.pop(box_5.index('cup'))
box_2.append(cup)
box_5.append(fridge)

# Move the camera from Box 10 to Box 7
camera = box_10.pop()
box_7.append(camera)

# Put the mixer into Box 6
box_6.append('mixer')

# Put the glove, leaf, and river into Box 9
box_9.append('glove')
box_9.append('leaf')
box_9.append('river')

# Replace the camera and the dog with the piano and the keyboard in Box 7
box_7.remove('camera')
box_7.remove('dog')
box_7.append('piano')
box_7.append('keyboard')

# Remove the towel and the soap from Box 8
box_8.remove('towel')
box_8.remove('soap')

# Move the helmet, coin, and glove from Box 7 to Box 1
helmet = box_7.pop(box_7.index('helmet'))
coin = box_7.pop(box_7.index('coin'))
glove = box_7.pop(box_7.index('glove'))
box_1.append(helmet)
box_1.append(coin)
box_1.append(glove)

# Move the coral from Box 10 to Box 6
coral = box_10.pop()
box_6.append(coral)

# Remove the glove and the leaf from Box 9
box_9.remove('glove')
box_9.remove('leaf')

# Put the glove into Box 6
box_6.append('glove')

# Remove the river from Box 9
box_9.remove('river')

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