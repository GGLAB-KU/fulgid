box_0 = ['rain', 'scissors', 'mirror']
box_1 = ['guitar', 'scarf', 'starfish', 'puzzle']
box_2 = ['cat']
box_3 = ['sock', 'desert']
box_4 = ['fish', 'headphone', 'needle', 'planet', 'pot']
box_5 = ['jungle']
box_6 = ['shorts', 'beach', 'seaweed', 'book']

# Move items from Box 6 to Box 2
box_2.extend(box_6.pop(box_6.index('shorts')))
box_2.extend(box_6.pop(box_6.index('seaweed')))
box_2.extend(box_6.pop(box_6.index('book')))

# Swap items between Box 4 and Box 0
box_0.append(box_4.pop(box_4.index('mirror')))
box_4.append(box_0.pop(box_0.index('headphone')))

# Replace item in Box 5 with 'moon'
box_5[0] = 'moon'

# Put 'submarine' and 'snow' into Box 6
box_6.append('submarine')
box_6.append('snow')

# Swap 'snow' between Box 6 and Box 5
box_6.append(box_5.pop(box_5.index('snow')))
box_5.append(box_6.pop(box_6.index('snow')))

# Swap 'snow' with 'sock' in Box 3
box_3.append(box_5.pop(box_5.index('snow')))
box_5.append(box_3.pop(box_3.index('sock')))

# Put 'fork' into Box 6
box_6.append('fork')

# Put 'beach' and 'sock' into Box 1
box_1.append('beach')
box_1.append('sock')

# Replace 'scissors' and 'rain' with 'soap' and 'lamp' in Box 0
box_0.append('soap')
box_0.append('lamp')
box_0.remove('scissors')
box_0.remove('rain')

# Remove 'starfish' from Box 1
box_1.remove('starfish')

# Replace 'desert' with 'lipstick' in Box 3
box_3[0] = 'lipstick'

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)