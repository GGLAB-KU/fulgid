box_0 = ['tape', 'branch', 'needle']
box_1 = ['plate', 'pillow']
box_2 = ['boot', 'dog', 'book', 'grinder']
box_3 = []
box_4 = ['moon', 'truck']
box_5 = ['leaf']
box_6 = ['snow', 'pants', 'soap', 'usb', 'wire']

# Swap the dog in Box 2 with the leaf in Box 5
box_2.remove('dog')
box_5.remove('leaf')
box_2.append('leaf')
box_5.append('dog')

# Move the moon from Box 4 to Box 1
box_4.remove('moon')
box_1.append('moon')

# Put the fridge and the freezer and the tiger into Box 1
box_1.extend(['fridge', 'freezer', 'tiger'])

# Move the book and the grinder from Box 2 to Box 3
box_2.remove('book')
box_2.remove('grinder')
box_3.extend(['book', 'grinder'])

# Move the dog from Box 5 to Box 0
box_5.remove('dog')
box_0.append('dog')

# Replace the leaf and the boot with the key and the soap in Box 2
box_2.remove('leaf')
box_2.remove('boot')
box_2.extend(['key', 'soap'])

# Put the chair and the shirt into Box 4
box_4.extend(['chair', 'shirt'])

# Put the toothpaste and the frame and the truck into Box 6
box_6.extend(['toothpaste', 'frame', 'truck'])

# Empty Box 2
box_2.clear()

# Remove the toothpaste and the wire and the pants from Box 6
box_6.remove('toothpaste')
box_6.remove('wire')
box_6.remove('pants')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)