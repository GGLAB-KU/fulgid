box_0 = ['fork', 'toothpaste', 'toy', 'car', 'boat']
box_1 = ['blanket']
box_2 = ['candle', 'sandals']
box_3 = ['pants', 'bracelet', 'boot', 'battery', 'pot']
box_4 = []
box_5 = []
box_6 = []
box_7 = ['necklace', 'shoes', 'drum']
box_8 = ['mixer', 'key', 'sun', 'bicycle']
box_9 = ['brush', 'harmonica']
box_10 = ['doll', 'bus', 'table']

# Remove the candle and the sandals from Box 2
box_2.remove('candle')
box_2.remove('sandals')

# Move the brush from Box 9 to Box 7
brush = box_9.pop()
box_7.append(brush)

# Remove the necklace from Box 7
box_7.remove('necklace')

# Remove the drum and the shoes from Box 7
box_7.remove('drum')
box_7.remove('shoes')

# Swap the brush in Box 7 with the toothpaste in Box 0
toothpaste = box_0.pop(1)
box_0.append(brush)
box_7.append(toothpaste)

# Move the toothpaste from Box 7 to Box 2
toothpaste = box_7.pop()
box_2.append(toothpaste)

# Put the fork into Box 9
box_9.append('fork')

# Remove the blanket from Box 1
box_1.remove('blanket')

# Swap the doll in Box 10 with the brush in Box 0
doll = box_10.pop(0)
box_0[0] = doll

# Move the key and the bicycle from Box 8 to Box 0
key = box_8.pop(1)
bicycle = box_8.pop(1)
box_0.extend([key, bicycle])

# Replace the bicycle and the key with the bag and the zipper in Box 0
box_0.remove('bicycle')
box_0.remove('key')
box_0.extend(['bag', 'zipper'])

# Replace the table with the desert in Box 10
box_10[2] = 'desert'

# Move the boot and the bracelet from Box 3 to Box 5
boot = box_3.pop(2)
bracelet = box_3.pop(1)
box_5.extend([boot, bracelet])

# Move the mixer from Box 8 to Box 6
mixer = box_8.pop(0)
box_6.append(mixer)

# Remove the harmonica and the fork from Box 9
box_9.remove('harmonica')
box_9.remove('fork')

# Put the hat and the dog and the grass into Box 0
box_0.extend(['hat', 'dog', 'grass'])

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
print("Box 10:", box_10)