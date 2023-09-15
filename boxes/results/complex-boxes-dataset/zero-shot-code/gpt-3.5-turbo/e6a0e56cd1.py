box_0 = []
box_1 = ['battery', 'perfume', 'basket']
box_2 = ['clock', 'rain', 'shorts', 'vase', 'boat']
box_3 = ['butterfly']
box_4 = ['dog', 'bag', 'mountain']
box_5 = ['elephant', 'zipper', 'scissors', 'bird', 'shirt']
box_6 = ['phone']
box_7 = ['makeup', 'sun', 'dolphin']
box_8 = ['blender', 'piano', 'thunder']
box_9 = ['freezer', 'card', 'tiger']

# Swap butterfly and basket
box_1.remove('basket')
box_1.append('butterfly')
box_3.remove('butterfly')
box_3.append('basket')

# Remove freezer, tiger, and card
box_9.remove('freezer')
box_9.remove('card')
box_9.remove('tiger')

# Replace battery, perfume, and butterfly with apple, fork, and glasses
box_1.remove('battery')
box_1.remove('perfume')
box_1.remove('butterfly')
box_1.append('apple')
box_1.append('fork')
box_1.append('glasses')

# Remove blender, piano, and thunder
box_8.remove('blender')
box_8.remove('piano')
box_8.remove('thunder')

# Put pillow, ship, and flute into box 2
box_2.append('pillow')
box_2.append('ship')
box_2.append('flute')

# Replace mirror with phone in box 6
box_6.remove('phone')
box_6.append('mirror')

# Remove bird from box 5
box_5.remove('bird')

# Move flute from box 2 to box 8
box_2.remove('flute')
box_8.append('flute')

# Replace flute with scarf in box 8
box_8.remove('flute')
box_8.append('scarf')

# Remove dolphin, sun, and makeup from box 7
box_7.remove('dolphin')
box_7.remove('sun')
box_7.remove('makeup')

# Remove scarf from box 8
box_8.remove('scarf')

# Put plate into box 8
box_8.append('plate')

# Remove ship and shorts from box 2
box_2.remove('ship')
box_2.remove('shorts')

# Empty box 2
box_2 = []

# Put charger, book, and storm into box 3
box_3.append('charger')
box_3.append('book')
box_3.append('storm')

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