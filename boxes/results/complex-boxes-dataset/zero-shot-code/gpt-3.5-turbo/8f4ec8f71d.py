box_0 = ['grinder', 'pillow', 'whistle', 'zipper', 'forest']
box_1 = ['pot']
box_2 = []
box_3 = ['leaf']
box_4 = ['controller', 'puzzle']
box_5 = ['flute', 'coral', 'pan', 'microscope', 'game']
box_6 = []

def print_boxes():
    print("Box 0:", box_0)
    print("Box 1:", box_1)
    print("Box 2:", box_2)
    print("Box 3:", box_3)
    print("Box 4:", box_4)
    print("Box 5:", box_5)
    print("Box 6:", box_6)

# Move the leaf from Box 3 to Box 4
box_4.append(box_3.pop(0))

# Put the jacket into Box 3
box_3.append('jacket')

# Replace the jacket with the guitar in Box 3
box_3.remove('jacket')
box_3.append('guitar')

# Replace the guitar with the cow in Box 3
box_3.remove('guitar')
box_3.append('cow')

# Put the comb into Box 3
box_3.append('comb')

# Swap the cow in Box 3 with the pot in Box 1
box_1.append(box_3.pop(0))
box_3.append(box_1.pop(0))

# Swap the comb in Box 3 with the cow in Box 1
box_1.append(box_3.pop(0))
box_3.append(box_1.pop(0))

# Put the swimsuit into Box 6
box_6.append('swimsuit')

# Swap the cow in Box 3 with the controller in Box 4
box_4.append(box_3.pop(0))
box_3.append(box_4.pop(0))

# Move the pot from Box 3 to Box 2
box_2.append(box_3.pop(0))

# Swap the pot in Box 2 with the pan in Box 5
box_5.append(box_2.pop(0))
box_2.append(box_5.pop(2))

# Print the final state of the boxes
print_boxes()