box_0 = ['desert', 'belt']
box_1 = ['phone', 'lamp']
box_2 = ['chair', 'moon']
box_3 = ['speaker', 'wallet']
box_4 = ['whistle', 'oven', 'toothbrush']
box_5 = ['island', 'butterfly', 'thread', 'fish', 'apple']
box_6 = ['jacket', 'boot', 'bicycle']
box_7 = ['controller']
box_8 = ['scarf']
box_9 = ['puzzle', 'coat']
box_10 = ['bracelet', 'headphone', 'seaweed']
box_11 = ['key', 'zipper']

# Move the key from Box 11 to Box 10
box_10.append(box_11.pop(box_11.index('key')))

# Swap the moon in Box 2 with the scarf in Box 8
box_2.append(box_8.pop(box_8.index('scarf')))
box_8.append(box_2.pop(box_2.index('moon')))

# Replace the moon with the comb in Box 8
box_8.append('comb')

# Put the swimsuit and the shelf and the helmet into Box 7
box_7.extend(['swimsuit', 'shelf', 'helmet'])

# Swap the seaweed in Box 10 with the thread in Box 5
box_10.append(box_5.pop(box_5.index('seaweed')))
box_5.append(box_10.pop(box_10.index('thread')))

# Remove the oven and the toothbrush and the whistle from Box 4
box_4.remove('oven')
box_4.remove('toothbrush')
box_4.remove('whistle')

# Move the key and the headphone from Box 10 to Box 5
box_5.extend([box_10.pop(box_10.index('key')), box_10.pop(box_10.index('headphone'))])

# Move the chair from Box 2 to Box 4
box_4.append(box_2.pop(box_2.index('chair')))

# Remove the puzzle from Box 9
box_9.remove('puzzle')

# Replace the island with the bracelet in Box 5
box_5.append('bracelet')
box_5.remove('island')

# Swap the desert in Box 0 with the chair in Box 4
box_0.append(box_4.pop(box_4.index('chair')))
box_4.append(box_0.pop(box_0.index('desert')))

# Empty Box 8
box_8 = []

# Swap the controller in Box 7 with the scarf in Box 2
box_7.append(box_2.pop(box_2.index('scarf')))
box_2.append(box_7.pop(box_7.index('controller')))

# Remove the coat from Box 9
box_9.remove('coat')

# Remove the wallet and the speaker from Box 3
box_3.remove('wallet')
box_3.remove('speaker')

# Replace the zipper with the book in Box 11
box_11.append('book')
box_11.remove('zipper')

# Swap the bracelet in Box 5 with the controller in Box 2
box_5.append(box_2.pop(box_2.index('controller')))
box_2.append(box_5.pop(box_5.index('bracelet')))

# Put the camera and the perfume into Box 5
box_5.extend(['camera', 'perfume'])

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