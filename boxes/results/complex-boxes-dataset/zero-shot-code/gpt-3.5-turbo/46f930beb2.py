box0 = ['tape']
box1 = ['storm', 'umbrella', 'microscope', 'sock']
box2 = ['bicycle', 'pillow', 'fork', 'brush', 'shampoo']
box3 = ['perfume', 'coral']
box4 = ['controller', 'swimsuit']
box5 = ['wallet', 'magnet']

# Swap magnet in Box 5 with swimsuit in Box 4
box5.remove('magnet')
box4.remove('swimsuit')
box5.append('swimsuit')
box4.append('magnet')

# Put note, controller, and train into Box 3
box3.extend(['note', 'controller', 'train'])

# Replace note and perfume with tie and shorts in Box 3
box3.remove('note')
box3.remove('perfume')
box3.append('tie')
box3.append('shorts')

# Put swimsuit and headphone into Box 2
box2.append('swimsuit')
box2.append('headphone')

# Swap swimsuit in Box 5 with sock in Box 1
box5.remove('swimsuit')
box1.remove('sock')
box5.append('sock')
box1.append('swimsuit')

# Empty Box 5
box5 = []

# Remove fork and shampoo from Box 2
box2.remove('fork')
box2.remove('shampoo')

# Replace controller with necklace in Box 4
box4.remove('controller')
box4.append('necklace')

# Replace magnet with drum in Box 4
box4.remove('magnet')
box4.append('drum')

# Print the contents of each box
print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)
print("Box 4:", box4)
print("Box 5:", box5)