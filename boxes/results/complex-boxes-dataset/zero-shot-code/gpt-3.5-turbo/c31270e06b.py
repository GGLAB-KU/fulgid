box_0 = []
box_1 = ['oven', 'microwave']
box_2 = ['shorts', 'bell', 'branch', 'ring', 'beach']
box_3 = ['shampoo', 'butterfly', 'ocean', 'perfume']
box_4 = ['moon', 'ship', 'bracelet', 'wallet']
box_5 = ['planet', 'starfish', 'grass', 'crown']

# Swap starfish in Box 5 with ocean in Box 3
box_5.remove('starfish')
box_3.remove('ocean')
box_5.append('ocean')
box_3.append('starfish')

# Remove bracelet, wallet, and ship from Box 4
box_4.remove('bracelet')
box_4.remove('wallet')
box_4.remove('ship')

# Remove moon from Box 4
box_4.remove('moon')

# Swap beach in Box 2 with perfume in Box 3
box_2.remove('beach')
box_3.remove('perfume')
box_2.append('perfume')
box_3.append('beach')

# Replace ocean and planet with star and tiger in Box 5
box_5.remove('ocean')
box_5.remove('planet')
box_5.append('star')
box_5.append('tiger')

# Swap oven in Box 1 with ring in Box 2
box_1.remove('oven')
box_2.remove('ring')
box_1.append('ring')
box_2.append('oven')

# Swap butterfly in Box 3 with branch in Box 2
box_3.remove('butterfly')
box_2.remove('branch')
box_3.append('branch')
box_2.append('butterfly')

# Remove microwave and ring from Box 1
box_1.remove('microwave')
box_1.remove('ring')

# Swap bell in Box 2 with shampoo in Box 3
box_2.remove('bell')
box_3.remove('shampoo')
box_2.append('shampoo')
box_3.append('bell')

print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)