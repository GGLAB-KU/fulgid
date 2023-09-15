box_0 = ['skirt', 'desert', 'phone', 'flower']
box_1 = ['truck', 'sandals', 'telescope', 'zipper']
box_2 = ['pot', 'razor', 'blender', 'jacket', 'towel']
box_3 = ['helmet', 'camera', 'scarf']
box_4 = ['perfume']
box_5 = ['usb', 'lamp']

# Remove the scarf from Box 3
box_3.remove('scarf')

# Replace the usb and the lamp with the guitar and the cat in Box 5
box_5.remove('usb')
box_5.remove('lamp')
box_5.extend(['guitar', 'cat'])

# Move the guitar from Box 5 to Box 3
box_5.remove('guitar')
box_3.append('guitar')

# Move the guitar and the camera from Box 3 to Box 4
box_3.remove('guitar')
box_3.remove('camera')
box_4.extend(['guitar', 'camera'])

# Remove the telescope and the sandals and the zipper from Box 1
box_1.remove('telescope')
box_1.remove('sandals')
box_1.remove('zipper')

# Move the skirt from Box 0 to Box 5
box_0.remove('skirt')
box_5.append('skirt')

# Remove the cat and the skirt from Box 5
box_5.remove('cat')
box_5.remove('skirt')

# Replace the desert with the toaster in Box 0
box_0.remove('desert')
box_0.append('toaster')

# Swap the razor in Box 2 with the truck in Box 1
box_2.remove('razor')
box_1.remove('truck')
box_2.append('truck')
box_1.append('razor')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)