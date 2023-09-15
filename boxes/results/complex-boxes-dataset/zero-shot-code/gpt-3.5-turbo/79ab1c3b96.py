box_0 = ['shoes', 'lightning', 'toothpaste', 'beach']
box_1 = []
box_2 = ['starfish', 'flute']
box_3 = ['thunder', 'thread', 'charger', 'ring', 'book']
box_4 = ['pan', 'towel', 'truck']
box_5 = ['plane']
box_6 = ['basket', 'river']
box_7 = ['shoe', 'pot']
box_8 = ['mixer']
box_9 = ['scarf']
box_10 = ['shorts', 'microwave']
box_11 = ['comet', 'meteor', 'mountain']
box_12 = ['clock', 'motorcycle']
box_13 = ['polish', 'watch', 'swimsuit']

# Swap plane in Box 5 with scarf in Box 9
box_5.remove('plane')
box_9.remove('scarf')
box_5.append('scarf')
box_9.append('plane')

# Remove shoe and pot from Box 7
box_7.remove('shoe')
box_7.remove('pot')

# Put lightning and starfish into Box 5
box_5.append('lightning')
box_5.append('starfish')

# Swap flute in Box 2 with microwave in Box 10
box_2.remove('flute')
box_10.remove('microwave')
box_2.append('microwave')
box_10.append('flute')

# Move book and charger from Box 3 to Box 5
box_3.remove('book')
box_3.remove('charger')
box_5.append('book')
box_5.append('charger')

# Replace shorts and flute with tree and bag in Box 10
box_10.remove('shorts')
box_10.remove('flute')
box_10.append('tree')
box_10.append('bag')

# Empty Box 10
box_10 = []

# Remove swimsuit from Box 13
box_13.remove('swimsuit')

# Empty Box 0
box_0 = []

# Remove thread from Box 3
box_3.remove('thread')

# Put camera and fish into Box 13
box_13.append('camera')
box_13.append('fish')

# Remove river from Box 6
box_6.remove('river')

# Replace thunder and ring with microscope and harmonica in Box 3
box_3.remove('thunder')
box_3.remove('ring')
box_3.append('microscope')
box_3.append('harmonica')

# Put sandals and glove into Box 4
box_4.append('sandals')
box_4.append('glove')

# Remove scarf, book, and lightning from Box 5
box_5.remove('scarf')
box_5.remove('book')
box_5.remove('lightning')

# Remove towel from Box 4
box_4.remove('towel')

# Replace clock and motorcycle with ring and sun in Box 12
box_12.remove('clock')
box_12.remove('motorcycle')
box_12.append('ring')
box_12.append('sun')

# Put skirt, starfish, and pants into Box 11
box_11.append('skirt')
box_11.append('starfish')
box_11.append('pants')

# Remove basket from Box 6
box_6.remove('basket')

# Move meteor and pants from Box 11 to Box 9
box_11.remove('meteor')
box_11.remove('pants')
box_9.append('meteor')
box_9.append('pants')

# Put piano, dog, and ship into Box 0
box_0.append('piano')
box_0.append('dog')
box_0.append('ship')

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