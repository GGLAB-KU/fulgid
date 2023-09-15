box_0 = ['butterfly', 'tiger']
box_1 = ['necklace']
box_2 = ['bowl']
box_3 = ['needle']
box_4 = ['pillow', 'shampoo', 'phone']

# Put the piano and the needle into Box 3
box_3.append('piano')

# Move the bowl from Box 2 to Box 4
item = box_2.pop()
box_4.append(item)

# Replace the butterfly and the tiger with the bag and the keyboard in Box 0
box_0.remove('butterfly')
box_0.remove('tiger')
box_0.append('bag')
box_0.append('keyboard')

# Remove the keyboard from Box 0
box_0.remove('keyboard')

# Move the bag from Box 0 to Box 2
item = box_0.pop()
box_2.append(item)

# Remove the phone and the shampoo from Box 4
box_4.remove('phone')
box_4.remove('shampoo')

# Move the bag from Box 2 to Box 0
item = box_2.pop()
box_0.append(item)

# Print the final contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)