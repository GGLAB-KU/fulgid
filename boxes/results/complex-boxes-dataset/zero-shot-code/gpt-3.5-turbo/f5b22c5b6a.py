box_0 = ['sandals']
box_1 = ['comb', 'phone']
box_2 = []
box_3 = ['book', 'starfish', 'toothpaste', 'note', 'needle']
box_4 = ['clock', 'cup', 'coral', 'shoes']
box_5 = []

# Replace the sandals with the plane in Box 0
box_0.remove('sandals')
box_0.append('plane')

# Put the bowl into Box 4
box_4.append('bowl')

# Put the dress into Box 3
box_3.append('dress')

# Swap the clock in Box 4 with the plane in Box 0
box_0.remove('plane')
box_4.remove('clock')
box_0.append('clock')
box_4.append('plane')

# Remove the coral and the bowl from Box 4
box_4.remove('coral')
box_4.remove('bowl')

# Put the wire and the cat and the coat into Box 4
box_4.extend(['wire', 'cat', 'coat'])

# Move the clock from Box 0 to Box 4
box_0.remove('clock')
box_4.append('clock')

# Move the comb and the phone from Box 1 to Box 0
box_1.remove('comb')
box_1.remove('phone')
box_0.extend(['comb', 'phone'])

# Put the earring into Box 5
box_5.append('earring')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)