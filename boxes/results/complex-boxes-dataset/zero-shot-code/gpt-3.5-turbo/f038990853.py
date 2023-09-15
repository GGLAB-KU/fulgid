box_0 = ['crown']
box_1 = ['harmonica', 'seaweed', 'grass']
box_2 = ['helmet']
box_3 = ['rain', 'wallet']
box_4 = ['usb', 'bicycle', 'clock', 'dice', 'cat']
box_5 = ['chair', 'tiger', 'lightning', 'zipper']

# Remove chair and lightning from Box 5
box_5.remove('chair')
box_5.remove('lightning')

# Put fork and usb into Box 2
box_2.append('fork')
box_2.append('usb')

# Swap rain in Box 3 with zipper in Box 5
box_3.remove('rain')
box_5.remove('zipper')
box_3.append('zipper')
box_5.append('rain')

# Put towel and book into Box 0
box_0.append('towel')
box_0.append('book')

# Remove wallet and zipper from Box 3
box_3.remove('wallet')
box_3.remove('zipper')

# Move helmet from Box 2 to Box 3
box_2.remove('helmet')
box_3.append('helmet')

# Swap seaweed in Box 1 with cat in Box 4
box_1.remove('seaweed')
box_4.remove('cat')
box_1.append('cat')
box_4.append('seaweed')

# Swap book in Box 0 with helmet in Box 3
box_0.remove('book')
box_3.remove('helmet')
box_0.append('helmet')
box_3.append('book')

# Swap bicycle in Box 4 with grass in Box 1
box_4.remove('bicycle')
box_1.remove('grass')
box_4.append('grass')
box_1.append('bicycle')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)