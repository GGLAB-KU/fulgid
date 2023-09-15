box_0 = []
box_1 = ['oven', 'flower', 'pillow', 'umbrella', 'guitar']
box_2 = ['toothpaste', 'pen', 'polish', 'sun', 'blender']
box_3 = ['vase', 'shorts', 'plane', 'bird', 'thunder']
box_4 = ['swimsuit', 'river', 'dress', 'coat', 'forest']
box_5 = ['meteor', 'charger']
box_6 = ['controller']
box_7 = ['bag', 'card']
box_8 = ['mask', 'zipper', 'toaster', 'piano', 'shirt']

# Remove the bird from Box 3
box_3.remove('bird')

# Swap the coat in Box 4 with the charger in Box 5
box_4.remove('coat')
box_5.remove('charger')
box_4.append('charger')
box_5.append('coat')

# Swap the bag in Box 7 with the controller in Box 6
box_7.remove('bag')
box_6.remove('controller')
box_7.append('controller')
box_6.append('bag')

# Remove the bag from Box 6
box_6.remove('bag')

# Move the flower from Box 1 to Box 0
box_0.append(box_1.pop(box_1.index('flower')))

# Put the rock and the table into Box 4
box_4.extend(['rock', 'table'])

# Move the flower from Box 0 to Box 5
box_5.append(box_0.pop(box_0.index('flower')))

# Swap the toothpaste in Box 2 with the flower in Box 5
box_2.remove('toothpaste')
box_5.remove('flower')
box_2.append('flower')
box_5.append('toothpaste')

# Swap the pillow in Box 1 with the plane in Box 3
box_1.remove('pillow')
box_3.remove('plane')
box_1.append('plane')
box_3.append('pillow')

# Remove the sun and the polish from Box 2
box_2.remove('sun')
box_2.remove('polish')

# Move the controller and the card from Box 7 to Box 5
box_7.remove('card')
box_5.append('card')
box_7.remove('controller')
box_5.append('controller')

# Put the necklace into Box 7
box_7.append('necklace')

# Remove the necklace from Box 7
box_7.remove('necklace')

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