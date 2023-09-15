box_0 = ['soap', 'mirror', 'seaweed', 'dog']
box_1 = ['lightning', 'sun', 'island']
box_2 = []
box_3 = ['bus', 'harmonica', 'skirt', 'tiger']
box_4 = ['planet', 'key', 'microscope']
box_5 = []
box_6 = ['train', 'snow', 'fridge']
box_7 = ['ship', 'hat', 'butterfly', 'comet']
box_8 = []

# Replace the skirt with the wire in Box 3
box_3.remove('skirt')
box_3.append('wire')

# Swap the butterfly in Box 7 with the soap in Box 0
box_0.remove('soap')
box_7.remove('butterfly')
box_0.append('butterfly')
box_7.append('soap')

# Move the butterfly and the mirror from Box 0 to Box 2
box_0.remove('butterfly')
box_0.remove('mirror')
box_2.append('butterfly')
box_2.append('mirror')

# Move the fridge from Box 6 to Box 7
box_6.remove('fridge')
box_7.append('fridge')

# Remove the harmonica from Box 3
box_3.remove('harmonica')

# Replace the bus with the brush in Box 3
box_3.remove('bus')
box_3.append('brush')

# Swap the wire in Box 3 with the butterfly in Box 2
box_3.remove('wire')
box_2.remove('butterfly')
box_3.append('butterfly')
box_2.append('wire')

# Move the mirror from Box 2 to Box 8
box_2.remove('mirror')
box_8.append('mirror')

# Remove the train from Box 6
box_6.remove('train')

# Empty Box 1
box_1 = []

# Swap the butterfly in Box 3 with the snow in Box 6
box_3.remove('butterfly')
box_6.remove('snow')
box_3.append('snow')
box_6.append('butterfly')

# Move the mirror from Box 8 to Box 3
box_8.remove('mirror')
box_3.append('mirror')

# Put the lightning into Box 0
box_0.append('lightning')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)
print("Box 8:", box_8)