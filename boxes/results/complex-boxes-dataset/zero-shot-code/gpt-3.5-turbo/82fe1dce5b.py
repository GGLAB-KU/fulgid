box_0 = ['charger', 'brush', 'star', 'wig', 'wire']
box_1 = ['speaker', 'pen', 'harmonica']
box_2 = ['jacket', 'grinder']
box_3 = ['snow', 'glasses', 'seaweed', 'sandals', 'shelf']
box_4 = ['earring', 'clock', 'towel', 'battery']
box_5 = ['crown']
box_6 = []
box_7 = ['mask', 'zipper', 'rain', 'river']
box_8 = ['gloves', 'thread', 'headphone']

# Remove items from Box 7
box_7.remove('mask')
box_7.remove('zipper')
box_7.remove('rain')
box_7.remove('river')

# Add items to Box 1
box_1.append('bowl')
box_1.append('microwave')
box_1.append('ring')

# Swap items between Box 1 and Box 2
box_1.remove('microwave')
box_2.remove('grinder')
box_1.append('grinder')
box_2.append('microwave')

# Swap items between Box 3 and Box 1
box_3.remove('glasses')
box_1.remove('ring')
box_3.append('ring')
box_1.append('glasses')

# Remove items from Box 8
box_8.remove('headphone')
box_8.remove('gloves')

# Move item from Box 1 to Box 6
box_6.append(box_1.pop(box_1.index('speaker')))

# Remove items from Box 0
box_0.remove('wire')
box_0.remove('brush')
box_0.remove('wig')

# Add items to Box 6
box_6.append('bracelet')
box_6.append('pen')
box_6.append('pot')

# Add items to Box 7
box_7.append('drum')
box_7.append('horse')
box_7.append('ship')

# Replace items in Box 7
box_7.remove('horse')
box_7.remove('rain')
box_7.append('sock')
box_7.append('shampoo')

# Remove items from Box 7
box_7.remove('ship')
box_7.remove('drum')
box_7.remove('shampoo')

# Add item to Box 6
box_6.append('candle')

# Remove items from Box 1
box_1.remove('grinder')
box_1.remove('pen')
box_1.remove('glasses')

# Swap items between Box 2 and Box 0
box_2.remove('jacket')
box_0.remove('charger')
box_2.append('charger')
box_0.append('jacket')

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