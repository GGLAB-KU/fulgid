box_0 = ['book', 'soap', 'planet', 'flower']
box_1 = ['tiger']
box_2 = []
box_3 = ['snow', 'shelf', 'bowl']
box_4 = ['motorcycle', 'candle', 'whistle']
box_5 = []
box_6 = ['basket', 'chair', 'towel']
box_7 = ['note', 'bell', 'dolphin', 'cat', 'flute']
box_8 = ['submarine']
box_9 = ['needle']
box_10 = ['doll', 'storm', 'mountain', 'plane']

# Move the planet, flower, and soap from Box 0 to Box 3
box_3.extend([box_0.pop(box_0.index('planet')), box_0.pop(box_0.index('flower')), box_0.pop(box_0.index('soap'))])

# Put the dress and lipstick into Box 3
box_3.extend(['dress', 'lipstick'])

# Put the coral, bowl, and tree into Box 7
box_7.extend(['coral', 'bowl', 'tree'])

# Empty Box 9
box_9 = []

# Put the bell and pants into Box 10
box_10.extend(['bell', 'pants'])

# Remove the storm from Box 10
box_10.remove('storm')

# Remove the dress and bowl from Box 3
box_3.remove('dress')
box_3.remove('bowl')

# Put the freezer, wig, and mixer into Box 5
box_5.extend(['freezer', 'wig', 'mixer'])

# Move the motorcycle, candle, and whistle from Box 4 to Box 8
box_8.extend([box_4.pop(box_4.index('motorcycle')), box_4.pop(box_4.index('candle')), box_4.pop(box_4.index('whistle'))])

# Replace the bowl with the snow in Box 7
box_7.remove('bowl')
box_7.append('snow')

# Swap the coral in Box 7 with the basket in Box 6
box_7.remove('coral')
box_6.remove('basket')
box_7.append('basket')
box_6.append('coral')

# Replace the towel and coral with the cup and shoes in Box 6
box_6.remove('towel')
box_6.remove('coral')
box_6.extend(['cup', 'shoes'])

# Move the soap, planet, and lipstick from Box 3 to Box 5
box_5.extend([box_3.pop(box_3.index('soap')), box_3.pop(box_3.index('planet')), box_3.pop(box_3.index('lipstick'))])

# Put the lamp and soap into Box 3
box_3.extend(['lamp', 'soap'])

# Replace the book with the horse in Box 0
box_0.remove('book')
box_0.append('horse')

# Empty Box 5
box_5 = []

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