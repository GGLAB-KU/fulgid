box_0 = ['puzzle', 'chair', 'moon', 'apple']
box_1 = ['candle', 'scarf']
box_2 = ['lamp']
box_3 = ['tape', 'blender', 'boot', 'lipstick']
box_4 = ['game', 'perfume', 'laptop']
box_5 = ['basket']
box_6 = []
box_7 = ['mask', 'ocean', 'magnet', 'storm', 'watch']
box_8 = []
box_9 = ['skirt']
box_10 = ['doll', 'shoe']

# Swap the ocean in Box 7 with the skirt in Box 9
box_7.remove('ocean')
box_9.remove('skirt')
box_7.append('skirt')
box_9.append('ocean')

# Swap the lamp in Box 2 with the perfume in Box 4
box_2.remove('lamp')
box_4.remove('perfume')
box_2.append('perfume')
box_4.append('lamp')

# Move the lamp and the laptop from Box 4 to Box 5
box_4.remove('lamp')
box_4.remove('laptop')
box_5.append('lamp')
box_5.append('laptop')

# Move the game from Box 4 to Box 1
box_4.remove('game')
box_1.append('game')

# Put the headphone into Box 7
box_7.append('headphone')

# Put the scarf into Box 10
box_10.append('scarf')

# Put the shampoo and the charger and the umbrella into Box 2
box_2.append('shampoo')
box_2.append('charger')
box_2.append('umbrella')

# Remove the skirt and the storm from Box 7
box_7.remove('skirt')
box_7.remove('storm')

# Move the moon from Box 0 to Box 10
box_0.remove('moon')
box_10.append('moon')

# Move the apple and the puzzle from Box 0 to Box 9
box_0.remove('apple')
box_0.remove('puzzle')
box_9.append('apple')
box_9.append('puzzle')

# Replace the perfume and the umbrella and the charger with the basket and the elephant and the keyboard in Box 2
box_2.remove('perfume')
box_2.remove('umbrella')
box_2.remove('charger')
box_2.append('basket')
box_2.append('elephant')
box_2.append('keyboard')

# Remove the headphone and the mask from Box 7
box_7.remove('headphone')
box_7.remove('mask')

# Move the apple and the puzzle from Box 9 to Box 10
box_9.remove('apple')
box_9.remove('puzzle')
box_10.append('apple')
box_10.append('puzzle')

# Empty Box 2
box_2 = []

# Move the game and the scarf from Box 1 to Box 2
box_1.remove('game')
box_1.remove('scarf')
box_2.append('game')
box_2.append('scarf')

# Move the doll from Box 10 to Box 4
box_10.remove('doll')
box_4.append('doll')

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