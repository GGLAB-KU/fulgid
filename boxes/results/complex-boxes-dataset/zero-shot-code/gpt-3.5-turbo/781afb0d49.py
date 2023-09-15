box_0 = ['razor', 'towel', 'shampoo', 'necklace']
box_1 = ['shark', 'paint', 'book']
box_2 = ['comet', 'pan', 'keyboard', 'car']
box_3 = ['shoe', 'spoon', 'lipstick', 'frame', 'phone']
box_4 = []
box_5 = ['soap', 'flower', 'brush', 'shirt']
box_6 = ['mirror', 'piano']

# Swap the flower in Box 5 with the piano in Box 6
box_5.remove('flower')
box_6.remove('piano')
box_5.append('piano')
box_6.append('flower')

# Replace the shark and the book with the console and the dog in Box 1
box_1.remove('shark')
box_1.remove('book')
box_1.append('console')
box_1.append('dog')

# Replace the shirt with the dog in Box 5
box_5.remove('shirt')
box_5.append('dog')

# Put the elephant and the pan into Box 5
box_5.append('elephant')
box_5.append('pan')

# Empty Box 6
box_6 = []

# Remove the shampoo and the towel from Box 0
box_0.remove('shampoo')
box_0.remove('towel')

# Move the dog and the paint and the console from Box 1 to Box 3
box_3.append('dog')
box_3.append('paint')
box_3.append('console')
box_1.remove('dog')
box_1.remove('paint')
box_1.remove('console')

# Move the comet and the pan from Box 2 to Box 4
box_4.append('comet')
box_4.append('pan')
box_2.remove('comet')
box_2.remove('pan')

# Swap the brush in Box 5 with the comet in Box 4
box_5.remove('brush')
box_4.remove('comet')
box_5.append('comet')
box_4.append('brush')

# Swap the keyboard in Box 2 with the razor in Box 0
box_2.remove('keyboard')
box_0.remove('razor')
box_2.append('razor')
box_0.append('keyboard')

# Put the flute and the tiger and the motorcycle into Box 5
box_5.append('flute')
box_5.append('tiger')
box_5.append('motorcycle')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)