box_0 = ['horn', 'fish']
box_1 = ['brush', 'cow', 'guitar', 'coin', 'star']
box_2 = ['card', 'grinder', 'basket']
box_3 = ['fork', 'soap', 'bicycle', 'storm', 'cup']
box_4 = ['wallet', 'plane', 'camera', 'pillow', 'toaster']
box_5 = ['microwave']
box_6 = ['octopus', 'sock', 'book', 'coat']
box_7 = ['belt', 'car', 'violin', 'river']
box_8 = ['lightning', 'pan', 'scissors']
box_9 = ['meteor']
box_10 = ['blender', 'telescope', 'keyboard']

# Swap the grinder in Box 2 with the fork in Box 3
box_2[1], box_3[0] = box_3[0], box_2[1]

# Move the coin and the cow from Box 1 to Box 0
box_0.extend([box_1.pop(box_1.index('coin')), box_1.pop(box_1.index('cow'))])

# Replace the basket and the card and the fork with the polish and the towel and the lamp in Box 2
box_2 = ['polish', 'towel', 'lamp']

# Move the river and the belt and the car from Box 7 to Box 8
box_8.extend([box_7.pop(box_7.index('river')), box_7.pop(box_7.index('belt')), box_7.pop(box_7.index('car'))])

# Put the apple into Box 6
box_6.append('apple')

# Replace the pan with the sock in Box 8
box_8[1] = 'sock'

# Put the doll into Box 5
box_5.append('doll')

# Remove the towel from Box 2
box_2.remove('towel')

# Swap the pillow in Box 4 with the keyboard in Box 10
box_4[3], box_10[2] = box_10[2], box_4[3]

# Put the plane into Box 8
box_8.append('plane')

# Move the cup and the grinder and the soap from Box 3 to Box 2
box_2.extend([box_3.pop(box_3.index('cup')), box_3.pop(box_3.index('grinder')), box_3.pop(box_3.index('soap'))])

# Replace the star and the guitar with the submarine and the shark in Box 1
box_1 = ['submarine', 'shark']

# Move the coat and the apple and the book from Box 6 to Box 2
box_2.extend([box_6.pop(box_6.index('coat')), box_6.pop(box_6.index('apple')), box_6.pop(box_6.index('book'))])

# Remove the violin from Box 7
box_7.remove('violin')

# Put the ship and the butterfly into Box 7
box_7.extend(['ship', 'butterfly'])

# Move the cup and the grinder from Box 2 to Box 0
box_0.extend([box_2.pop(box_2.index('cup')), box_2.pop(box_2.index('grinder'))])

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