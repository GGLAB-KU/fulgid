box_0 = ['needle', 'grinder', 'ring']
box_1 = ['toy', 'crown', 'note']
box_2 = ['rain', 'tape', 'drum', 'key', 'thunder']
box_3 = ['coat', 'console', 'polish', 'battery', 'plane']
box_4 = ['shoes', 'scissors', 'jungle', 'paint', 'gloves']
box_5 = ['toothpaste', 'wallet', 'island', 'dice']
box_6 = ['tie', 'elephant', 'whistle', 'pot']
box_7 = ['star', 'usb']
box_8 = ['tiger', 'microscope', 'earring', 'lion', 'microwave']
box_9 = []

# Replace the toy, note, and crown in Box 1
box_1 = ['zipper', 'shoes', 'dolphin']

# Move the rain and drum from Box 2 to Box 8
box_8.extend(['rain', 'drum'])
box_2.remove('rain')
box_2.remove('drum')

# Swap the elephant in Box 6 with the tiger in Box 8
box_6.remove('elephant')
box_8.remove('tiger')
box_6.append('tiger')
box_8.append('elephant')

# Remove the whistle, pot, and tie from Box 6
box_6.remove('whistle')
box_6.remove('pot')
box_6.remove('tie')

# Move the key, thunder, and tape from Box 2 to Box 9
box_9.extend(['key', 'thunder', 'tape'])
box_2.remove('key')
box_2.remove('thunder')
box_2.remove('tape')

# Move the zipper, shoes, and dolphin from Box 1 to Box 5
box_5.extend(['zipper', 'shoes', 'dolphin'])
box_1.remove('zipper')
box_1.remove('shoes')
box_1.remove('dolphin')

# Replace the ring with the train in Box 0
box_0.remove('ring')
box_0.append('train')

# Replace the gloves with the glove in Box 4
box_4.remove('gloves')
box_4.append('glove')

# Put the shoe and bag into Box 5
box_5.extend(['shoe', 'bag'])

# Replace the tiger with the crown in Box 6
box_6.remove('tiger')
box_6.append('crown')

# Put the submarine and sculpture into Box 5
box_5.extend(['submarine', 'sculpture'])

# Replace the needle, train, and grinder with the island, leaf, and ocean in Box 0
box_0.remove('needle')
box_0.remove('train')
box_0.remove('grinder')
box_0.extend(['island', 'leaf', 'ocean'])

# Replace the crown with the ring in Box 6
box_6.remove('crown')
box_6.append('ring')

# Move the polish and battery from Box 3 to Box 8
box_8.extend(['polish', 'battery'])
box_3.remove('polish')
box_3.remove('battery')

# Replace the island, leaf, and ocean with the dog, mask, and thunder in Box 0
box_0.remove('island')
box_0.remove('leaf')
box_0.remove('ocean')
box_0.extend(['dog', 'mask', 'thunder'])

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