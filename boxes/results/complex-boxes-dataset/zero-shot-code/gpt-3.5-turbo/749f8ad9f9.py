box_0 = []
box_1 = ['cat', 'shorts', 'submarine', 'headphone', 'bell']
box_2 = ['shampoo', 'sun', 'zipper', 'bird']
box_3 = ['star', 'desert', 'blanket', 'dress', 'basket']
box_4 = ['bracelet', 'spoon', 'lamp', 'charger']
box_5 = ['comb', 'toothbrush']
box_6 = ['fridge', 'fish', 'rocket', 'book', 'swimsuit']
box_7 = ['shelf', 'shoe', 'console', 'keyboard']
box_8 = ['leaf', 'pillow', 'freezer']
box_9 = []
box_10 = ['coin', 'paint']
box_11 = ['snow', 'phone', 'helmet']

# Remove items from Box 4
box_4.remove('lamp')
box_4.remove('charger')
box_4.remove('spoon')

# Add items to Box 2
box_2.append('controller')
box_2.append('paint')

# Add forest to Box 0
box_0.append('forest')

# Swap items between Box 1 and Box 4
box_1.remove('bell')
box_4.remove('bracelet')
box_1.append('bracelet')
box_4.append('bell')

# Swap items between Box 2 and Box 3
box_2.remove('zipper')
box_3.remove('desert')
box_2.append('desert')
box_3.append('zipper')

# Remove items from Box 8
box_8.remove('leaf')
box_8.remove('pillow')
box_8.remove('freezer')

# Move items from Box 7 to Box 1
box_1.append('shelf')
box_1.append('shoe')
box_1.append('console')
box_7.remove('shelf')
box_7.remove('shoe')
box_7.remove('console')

# Swap items between Box 2 and Box 4
box_2.remove('bird')
box_4.remove('bell')
box_2.append('bell')
box_4.append('bird')

# Move keyboard from Box 7 to Box 9
box_9.append('keyboard')
box_7.remove('keyboard')

# Add tiger to Box 9
box_9.append('tiger')

# Move blanket from Box 3 to Box 6
box_6.append('blanket')
box_3.remove('blanket')

# Move bird from Box 4 to Box 3
box_3.append('bird')
box_4.remove('bird')

# Remove helmet from Box 11
box_11.remove('helmet')

# Replace star with mixer in Box 3
box_3.remove('star')
box_3.append('mixer')

# Add ocean and tree to Box 4
box_4.append('ocean')
box_4.append('tree')

# Move ocean and tree from Box 4 to Box 6
box_6.append('ocean')
box_6.append('tree')
box_4.remove('ocean')
box_4.remove('tree')

# Remove comb from Box 5
box_5.remove('comb')

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