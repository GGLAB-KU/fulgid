box_0 = []
box_1 = ['dolphin', 'telescope', 'mixer']
box_2 = ['pan', 'ring', 'blanket']
box_3 = []
box_4 = ['chair', 'camera']
box_5 = ['moon', 'plate', 'key', 'bag']
box_6 = ['earring', 'piano', 'toaster', 'tree', 'keyboard']
box_7 = ['comb']
box_8 = ['charger', 'bicycle', 'skirt', 'toothpaste']
box_9 = ['planet', 'comet', 'coin']
box_10 = ['forest', 'magnet']
box_11 = []
box_12 = ['wire', 'meteor', 'blender', 'flute', 'starfish']

# Move the bag and the moon from Box 5 to Box 9
box_9.extend([box_5.pop(box_5.index('bag')), box_5.pop(box_5.index('moon'))])

# Put the chair and the harmonica into Box 10
box_10.extend(['chair', 'harmonica'])

# Move the bicycle and the charger from Box 8 to Box 7
box_7.extend([box_8.pop(box_8.index('bicycle')), box_8.pop(box_8.index('charger'))])

# Swap the flute in Box 12 with the chair in Box 4
box_4[box_4.index('chair')], box_12[box_12.index('flute')] = box_12[box_12.index('flute')], box_4[box_4.index('chair')]

# Move the pan from Box 2 to Box 7
box_7.append(box_2.pop(box_2.index('pan')))

# Move the blender and the wire and the meteor from Box 12 to Box 6
box_6.extend([box_12.pop(box_12.index('blender')), box_12.pop(box_12.index('wire')), box_12.pop(box_12.index('meteor'))])

# Remove the starfish and the chair from Box 12
box_12.remove('starfish')
box_12.remove('chair')

# Move the keyboard and the meteor and the piano from Box 6 to Box 8
box_8.extend([box_6.pop(box_6.index('keyboard')), box_6.pop(box_6.index('meteor')), box_6.pop(box_6.index('piano'))])

# Remove the comb and the pan from Box 7
box_7.remove('comb')
box_7.remove('pan')

# Put the cup and the butterfly and the mask into Box 7
box_7.extend(['cup', 'butterfly', 'mask'])

# Move the bicycle from Box 7 to Box 6
box_6.append(box_7.pop(box_7.index('bicycle')))

# Remove the chair and the magnet from Box 10
box_10.remove('chair')
box_10.remove('magnet')

# Put the coin and the glasses into Box 7
box_7.extend(['coin', 'glasses'])

# Swap the planet in Box 9 with the flute in Box 4
box_9[box_9.index('planet')], box_4[box_4.index('flute')] = box_4[box_4.index('flute')], box_9[box_9.index('planet')]

# Empty Box 9
box_9 = []

# Remove the ring and the blanket from Box 2
box_2.remove('ring')
box_2.remove('blanket')

# Move the piano from Box 8 to Box 11
box_11.append(box_8.pop(box_8.index('piano')))

# Replace the plate with the river in Box 5
box_5[box_5.index('plate')] = 'river'

# Empty Box 4
box_4 = []

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