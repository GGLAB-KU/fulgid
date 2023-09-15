box_0 = ['makeup', 'fish']
box_1 = ['microwave']
box_2 = ['seaweed', 'book', 'cloud', 'controller']
box_3 = ['pants', 'meteor', 'submarine', 'coral']
box_4 = ['hat', 'desert', 'blender', 'dress']
box_5 = ['key', 'phone', 'drum', 'fork', 'comet']
box_6 = ['grass', 'guitar', 'charger', 'river', 'branch']
box_7 = []
box_8 = []
box_9 = []

def print_boxes():
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

# Remove the microwave from Box 1
box_1.remove('microwave')

# Put the perfume into Box 8
box_8.append('perfume')

# Swap the submarine in Box 3 with the makeup in Box 0
box_0.remove('makeup')
box_3.remove('submarine')
box_0.append('submarine')
box_3.append('makeup')

# Remove the key from Box 5
box_5.remove('key')

# Remove the branch from Box 6
box_6.remove('branch')

# Remove the charger and the guitar from Box 6
box_6.remove('charger')
box_6.remove('guitar')

# Swap the perfume in Box 8 with the coral in Box 3
box_3.remove('coral')
box_8.remove('perfume')
box_3.append('perfume')
box_8.append('coral')

# Remove the cloud and the controller and the book from Box 2
box_2.remove('cloud')
box_2.remove('controller')
box_2.remove('book')

# Swap the river in Box 6 with the coral in Box 8
box_6.remove('river')
box_8.remove('coral')
box_6.append('coral')
box_8.append('river')

# Empty Box 8
box_8 = []

# Swap the pants in Box 3 with the desert in Box 4
box_3.remove('pants')
box_4.remove('desert')
box_3.append('desert')
box_4.append('pants')

# Remove the grass and the coral from Box 6
box_6.remove('grass')
box_6.remove('coral')

# Move the seaweed from Box 2 to Box 0
box_2.remove('seaweed')
box_0.append('seaweed')

# Move the makeup from Box 3 to Box 7
box_3.remove('makeup')
box_7.append('makeup')

# Remove the makeup from Box 7
box_7.remove('makeup')

# Print the final state of the boxes
print_boxes()