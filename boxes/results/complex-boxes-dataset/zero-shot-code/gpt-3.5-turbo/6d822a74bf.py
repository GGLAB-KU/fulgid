box_0 = ['key', 'cloud', 'beach', 'glasses']
box_1 = ['horse', 'card', 'blanket', 'truck', 'boot']
box_2 = ['needle', 'comb', 'soap', 'helmet']
box_3 = ['skirt', 'piano', 'shorts', 'bracelet']
box_4 = ['watch', 'note', 'game', 'plane']
box_5 = ['starfish', 'bowl', 'umbrella']
box_6 = ['dolphin', 'dice', 'console']
box_7 = ['telescope', 'puzzle', 'fish', 'thread', 'bird']
box_8 = ['lion', 'scissors', 'glove', 'microscope']
box_9 = ['ring', 'pot', 'speaker', 'paint', 'train']
box_10 = ['frame', 'boat', 'rocket']
box_11 = ['perfume', 'shoe', 'horn', 'shampoo']
box_12 = ['moon', 'sculpture', 'lightning']
box_13 = ['fork', 'freezer', 'cat', 'toothbrush', 'seaweed']
box_14 = []

# Replace the console with the train in Box 6
box_6.remove('console')
box_6.append('train')

# Swap the horn in Box 11 with the glove in Box 8
box_11.remove('horn')
box_11.append('glove')
box_8.remove('glove')
box_8.append('horn')

# Move the ring and the speaker and the pot from Box 9 to Box 11
box_9.remove('ring')
box_9.remove('speaker')
box_9.remove('pot')
box_11.append('ring')
box_11.append('speaker')
box_11.append('pot')

# Swap the shoe in Box 11 with the bowl in Box 5
box_11.remove('shoe')
box_11.append('bowl')
box_5.remove('bowl')
box_5.append('shoe')

# Replace the bracelet and the skirt with the blender and the seaweed in Box 3
box_3.remove('bracelet')
box_3.remove('skirt')
box_3.append('blender')
box_3.append('seaweed')

# Swap the sculpture in Box 12 with the horn in Box 8
box_12.remove('sculpture')
box_12.append('horn')
box_8.remove('horn')
box_8.append('sculpture')

# Swap the plane in Box 4 with the moon in Box 12
box_4.remove('plane')
box_4.append('moon')
box_12.remove('moon')
box_12.append('plane')

# Move the shorts and the blender from Box 3 to Box 9
box_3.remove('shorts')
box_3.remove('blender')
box_9.append('shorts')
box_9.append('blender')

# Swap the pot in Box 11 with the beach in Box 0
box_11.remove('pot')
box_11.append('beach')
box_0.remove('beach')
box_0.append('pot')

# Replace the piano and the seaweed with the battery and the towel in Box 3
box_3.remove('piano')
box_3.remove('seaweed')
box_3.append('battery')
box_3.append('towel')

# Move the train and the blender from Box 9 to Box 8
box_9.remove('train')
box_9.remove('blender')
box_8.append('train')
box_8.append('blender')

# Replace the battery and the towel with the lion and the bag in Box 3
box_3.remove('battery')
box_3.remove('towel')
box_3.append('lion')
box_3.append('bag')

# Replace the paint with the sandals in Box 9
box_9.remove('paint')
box_9.append('sandals')

# Move the cloud and the glasses from Box 0 to Box 12
box_0.remove('cloud')
box_0.remove('glasses')
box_12.append('cloud')
box_12.append('glasses')

# Remove the starfish from Box 5
box_5.remove('starfish')

# Put the laptop into Box 6
box_6.append('laptop')

# Move the freezer and the cat from Box 13 to Box 2
box_13.remove('freezer')
box_13.remove('cat')
box_2.append('freezer')
box_2.append('cat')

# Replace the soap with the vase in Box 2
box_2.remove('soap')
box_2.append('vase')

# Replace the pot with the shampoo in Box 0
box_0.remove('pot')
box_0.append('shampoo')

# Remove the horse and the card from Box 1
box_1.remove('horse')
box_1.remove('card')

# Swap the bowl in Box 11 with the train in Box 8
box_11.remove('bowl')
box_11.append('train')
box_8.remove('train')
box_8.append('bowl')

# Replace the boot and the truck with the clock and the leaf in Box 1
box_1.remove('boot')
box_1.remove('truck')
box_1.append('clock')
box_1.append('leaf')

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
print("Box 13:", box_13)
print("Box 14:", box_14)