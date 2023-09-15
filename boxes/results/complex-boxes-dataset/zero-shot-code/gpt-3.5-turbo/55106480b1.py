box_0 = ['mixer', 'microwave', 'bracelet', 'key', 'book']
box_1 = ['truck', 'microscope']
box_2 = ['bag', 'horse', 'shorts', 'laptop', 'storm']
box_3 = ['note', 'river', 'bear']
box_4 = ['shampoo', 'razor', 'pants', 'mountain', 'helmet']
box_5 = ['mirror']
box_6 = ['bowl', 'sock', 'tape', 'console', 'soap']
box_7 = ['lion', 'candle', 'charger']

# Move the book, bracelet, and microwave from Box 0 to Box 1
box_1.extend(['book', 'bracelet', 'microwave'])
box_0.remove('book')
box_0.remove('bracelet')
box_0.remove('microwave')

# Remove the soap and tape from Box 6
box_6.remove('soap')
box_6.remove('tape')

# Empty Box 5
box_5 = []

# Put the piano, horse, and button into Box 1
box_1.extend(['piano', 'horse', 'button'])

# Replace the mixer and key with the crown and star in Box 0
box_0.remove('mixer')
box_0.remove('key')
box_0.extend(['crown', 'star'])

# Remove the helmet and razor from Box 4
box_4.remove('helmet')
box_4.remove('razor')

# Remove the shampoo and mountain from Box 4
box_4.remove('shampoo')
box_4.remove('mountain')

# Move the star from Box 0 to Box 1
box_1.append('star')
box_0.remove('star')

# Put the rain and sock into Box 0
box_0.extend(['rain', 'sock'])

# Move the rain and sock from Box 0 to Box 5
box_5.extend(['rain', 'sock'])
box_0.remove('rain')
box_0.remove('sock')

# Replace the bag and storm with the glove and grass in Box 2
box_2.remove('bag')
box_2.remove('storm')
box_2.extend(['glove', 'grass'])

# Put the bear into Box 5
box_5.append('bear')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)