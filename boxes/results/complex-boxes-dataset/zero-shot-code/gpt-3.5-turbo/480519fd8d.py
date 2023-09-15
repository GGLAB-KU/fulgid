box_0 = ['ring', 'keyboard', 'tape']
box_1 = ['freezer', 'controller', 'frame']
box_2 = ['mask', 'charger']
box_3 = ['guitar', 'blender', 'forest', 'magnet']
box_4 = ['sock', 'book', 'watch', 'wig']
box_5 = ['blanket', 'lightning', 'necklace']
box_6 = ['wallet', 'river', 'branch', 'tiger']
box_7 = ['helmet']
box_8 = ['toaster', 'microwave', 'doll', 'starfish']

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

# Swap the wig in Box 4 with the guitar in Box 3
box_4.remove('wig')
box_3.remove('guitar')
box_4.append('guitar')
box_3.append('wig')

# Replace the charger with the jungle in Box 2
box_2.remove('charger')
box_2.append('jungle')

# Put the plate and the pot and the towel into Box 1
box_1.extend(['plate', 'pot', 'towel'])

# Put the wig and the harmonica and the shorts into Box 6
box_6.extend(['wig', 'harmonica', 'shorts'])

# Move the helmet from Box 7 to Box 1
box_7.remove('helmet')
box_1.append('helmet')

# Swap the jungle in Box 2 with the doll in Box 8
box_2.remove('jungle')
box_8.remove('doll')
box_2.append('doll')
box_8.append('jungle')

# Remove the sock from Box 4
box_4.remove('sock')

# Swap the frame in Box 1 with the wallet in Box 6
box_1.remove('frame')
box_6.remove('wallet')
box_1.append('wallet')
box_6.append('frame')

# Move the watch and the guitar from Box 4 to Box 7
box_4.remove('watch')
box_4.remove('guitar')
box_7.extend(['watch', 'guitar'])

# Swap the helmet in Box 1 with the mask in Box 2
box_1.remove('helmet')
box_2.remove('mask')
box_1.append('mask')
box_2.append('helmet')

# Remove the book from Box 4
box_4.remove('book')

# Put the plate and the polish and the fork into Box 3
box_3.extend(['plate', 'polish', 'fork'])

# Swap the plate in Box 3 with the blanket in Box 5
box_3.remove('plate')
box_5.remove('blanket')
box_3.append('blanket')
box_5.append('plate')

# Empty Box 8
box_8 = []

print_boxes()