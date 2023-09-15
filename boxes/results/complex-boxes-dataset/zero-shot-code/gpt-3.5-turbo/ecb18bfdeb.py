box_0 = []
box_1 = []
box_2 = ['dog']
box_3 = ['bicycle', 'shirt']
box_4 = []
box_5 = ['coin', 'shampoo', 'guitar', 'comb']
box_6 = ['toothbrush', 'game', 'toothpaste']

print("Initial State:")
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)

# Move game, toothpaste, and toothbrush from Box 6 to Box 3
box_3.extend([box_6.pop(box_6.index('game')), box_6.pop(box_6.index('toothpaste')), box_6.pop(box_6.index('toothbrush'))])

# Replace game with lamp in Box 3
box_3[box_3.index('game')] = 'lamp'

# Empty Box 3
box_3 = []

# Move guitar and coin from Box 5 to Box 1
box_1.extend([box_5.pop(box_5.index('guitar')), box_5.pop(box_5.index('coin'))])

# Put gloves into Box 2
box_2.append('gloves')

# Swap dog in Box 2 with comb in Box 5
box_2[box_2.index('dog')], box_5[box_5.index('comb')] = box_5[box_5.index('comb')], box_2[box_2.index('dog')]

# Remove guitar and coin from Box 1
box_1.remove('guitar')
box_1.remove('coin')

# Put headphone and earring into Box 6
box_6.extend(['headphone', 'earring'])

# Swap headphone in Box 6 with gloves in Box 2
box_6[box_6.index('headphone')], box_2[box_2.index('gloves')] = box_2[box_2.index('gloves')], box_6[box_6.index('headphone')]

# Replace shampoo with necklace in Box 5
box_5[box_5.index('shampoo')] = 'necklace'

# Swap gloves in Box 6 with dog in Box 5
box_6[box_6.index('gloves')], box_5[box_5.index('dog')] = box_5[box_5.index('dog')], box_6[box_6.index('gloves')]

print("\nFinal State:")
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)