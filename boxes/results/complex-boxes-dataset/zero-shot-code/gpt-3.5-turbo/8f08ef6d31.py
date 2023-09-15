box_0 = ['moon', 'vase', 'watch']
box_1 = ['microscope', 'telescope']
box_2 = ['keyboard', 'shirt', 'horn', 'mirror']
box_3 = ['sandals', 'horse', 'bag', 'spoon', 'octopus']
box_4 = ['freezer']
box_5 = []
box_6 = ['harmonica']
box_7 = ['card', 'comet', 'apple', 'oven']
box_8 = ['ocean', 'starfish', 'lion']
box_9 = ['sock', 'pen', 'towel', 'mask']
box_10 = []
box_11 = ['train', 'shorts', 'candle', 'elephant']
box_12 = ['usb']

# Remove the harmonica from Box 6
box_6.remove('harmonica')

# Remove the moon and the vase and the watch from Box 0
box_0.remove('moon')
box_0.remove('vase')
box_0.remove('watch')

# Swap the telescope in Box 1 with the freezer in Box 4
box_1.remove('telescope')
box_4.remove('freezer')
box_1.append('freezer')
box_4.append('telescope')

# Move the elephant from Box 11 to Box 9
box_11.remove('elephant')
box_9.append('elephant')

# Swap the microscope in Box 1 with the telescope in Box 4
box_1.remove('microscope')
box_4.remove('telescope')
box_1.append('telescope')
box_4.append('microscope')

# Swap the sock in Box 9 with the ocean in Box 8
box_9.remove('sock')
box_8.remove('ocean')
box_9.append('ocean')
box_8.append('sock')

# Move the ocean from Box 9 to Box 8
box_9.remove('ocean')
box_8.append('ocean')

# Move the mirror from Box 2 to Box 1
box_2.remove('mirror')
box_1.append('mirror')

# Replace the elephant and the mask and the towel with the glove and the bag and the tie in Box 9
box_9.remove('elephant')
box_9.remove('mask')
box_9.remove('towel')
box_9.append('glove')
box_9.append('bag')
box_9.append('tie')

# Swap the sandals in Box 3 with the keyboard in Box 2
box_3.remove('sandals')
box_2.remove('keyboard')
box_3.append('keyboard')
box_2.append('sandals')

# Put the tiger and the grinder and the sandals into Box 0
box_0.append('tiger')
box_0.append('grinder')
box_0.append('sandals')

# Replace the tie and the bag and the glove with the plane and the fish and the controller in Box 9
box_9.remove('tie')
box_9.remove('bag')
box_9.remove('glove')
box_9.append('plane')
box_9.append('fish')
box_9.append('controller')

# Replace the train and the candle and the shorts with the blanket and the comb and the basket in Box 11
box_11.remove('train')
box_11.remove('candle')
box_11.remove('shorts')
box_11.append('blanket')
box_11.append('comb')
box_11.append('basket')

# Remove the sandals from Box 0
box_0.remove('sandals')

# Replace the oven and the apple and the card with the pillow and the wire and the bell in Box 7
box_7.remove('oven')
box_7.remove('apple')
box_7.remove('card')
box_7.append('pillow')
box_7.append('wire')
box_7.append('bell')

# Remove the basket and the blanket and the comb from Box 11
box_11.remove('basket')
box_11.remove('blanket')
box_11.remove('comb')

# Empty Box 3
box_3.clear()

# Swap the freezer in Box 1 with the controller in Box 9
box_1.remove('freezer')
box_9.remove('controller')
box_1.append('controller')
box_9.append('freezer')

# Move the fish and the plane from Box 9 to Box 12
box_9.remove('fish')
box_9.remove('plane')
box_12.append('fish')
box_12.append('plane')

# Remove the plane from Box 12
box_12.remove('plane')

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
print("Box 11:", box_11)
print("Box 12:", box_12)