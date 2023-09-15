box_0 = []
box_1 = ['shelf', 'sculpture', 'violin']
box_2 = ['river', 'bag']
box_3 = ['tie', 'blender']
box_4 = ['shoes', 'elephant', 'table', 'necklace']
box_5 = ['butterfly', 'train', 'pot', 'storm', 'puzzle']
box_6 = ['button']
box_7 = ['glasses']
box_8 = ['polish', 'skirt', 'umbrella']
box_9 = ['dolphin']

# Swap the river in Box 2 with the elephant in Box 4
box_2.remove('river')
box_4.remove('elephant')
box_2.append('elephant')
box_4.append('river')

# Remove the dolphin from Box 9
box_9.remove('dolphin')

# Replace the puzzle and the pot with the sun and the dog in Box 5
box_5.remove('puzzle')
box_5.remove('pot')
box_5.append('sun')
box_5.append('dog')

# Swap the button in Box 6 with the glasses in Box 7
box_6.remove('button')
box_7.remove('glasses')
box_6.append('glasses')
box_7.append('button')

# Remove the shelf and the sculpture and the violin from Box 1
box_1.remove('shelf')
box_1.remove('sculpture')
box_1.remove('violin')

# Move the table from Box 4 to Box 0
box_4.remove('table')
box_0.append('table')

# Move the shoes and the necklace from Box 4 to Box 9
box_4.remove('shoes')
box_4.remove('necklace')
box_9.append('shoes')
box_9.append('necklace')

# Move the table from Box 0 to Box 8
box_0.remove('table')
box_8.append('table')

# Swap the blender in Box 3 with the necklace in Box 9
box_3.remove('blender')
box_9.remove('necklace')
box_3.append('necklace')
box_9.append('blender')

# Replace the elephant with the shampoo in Box 2
box_2.remove('elephant')
box_2.append('shampoo')

# Put the camera and the keyboard into Box 5
box_5.append('camera')
box_5.append('keyboard')

# Move the dog and the sun from Box 5 to Box 2
box_5.remove('dog')
box_5.remove('sun')
box_2.append('dog')
box_2.append('sun')

# Empty Box 3
box_3 = []

# Empty Box 4
box_4 = []

# Put the bird and the motorcycle into Box 0
box_0.append('bird')
box_0.append('motorcycle')

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