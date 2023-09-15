box_0 = ['wire', 'fridge']
box_1 = []
box_2 = []
box_3 = []
box_4 = []
box_5 = ['piano', 'cloud', 'car']
box_6 = []
box_7 = ['dolphin', 'butterfly', 'oven', 'guitar', 'lightning']
box_8 = ['pan', 'coat', 'comet', 'harmonica', 'desert']
box_9 = ['horn', 'bear', 'seaweed']

# Swap the butterfly in Box 7 with the bear in Box 9
box_7[1], box_9[1] = box_9[1], box_7[1]

# Put the book and the island and the moon into Box 7
box_7.extend(['book', 'island', 'moon'])

# Empty Box 7
box_7 = []

# Swap the fridge in Box 0 with the coat in Box 8
box_0[1], box_8[1] = box_8[1], box_0[1]

# Move the fridge from Box 8 to Box 6
box_6.append(box_8.pop(1))

# Swap the cloud in Box 5 with the butterfly in Box 9
box_5[1], box_9[1] = box_9[1], box_5[1]

# Replace the comet and the harmonica with the plane and the basket in Box 8
box_8[2:4] = ['plane', 'basket']

# Replace the wire and the coat with the lion and the earring in Box 0
box_0 = ['lion', 'earring']

# Replace the fridge with the cloud in Box 6
box_6[0] = 'cloud'

# Swap the desert in Box 8 with the earring in Box 0
box_8[3], box_0[1] = box_0[1], box_8[3]

# Put the coat and the glasses into Box 5
box_5.extend(['coat', 'glasses'])

# Move the plane and the pan from Box 8 to Box 1
box_1.extend(box_8[2:4])
box_8[2:4] = []

# Put the comb into Box 7
box_7.append('comb')

# Replace the comb with the pen in Box 7
box_7[0] = 'pen'

# Replace the cloud with the pot in Box 6
box_6[0] = 'pot'

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
print("Box 9:", box_9)