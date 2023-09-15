box_0 = ['freezer', 'zipper', 'ring']
box_1 = ['tree']
box_2 = []
box_3 = ['scarf', 'lock']
box_4 = ['wallet', 'lion', 'umbrella']
box_5 = ['plate', 'sandals', 'crown', 'starfish', 'dice']
box_6 = ['grinder', 'sock', 'speaker']
box_7 = ['rocket', 'keyboard', 'pot']
box_8 = ['ocean', 'button', 'cow']
box_9 = ['chair', 'lamp', 'sun', 'bracelet']
box_10 = ['glove', 'controller', 'paint', 'pillow', 'forest']
box_11 = []
box_12 = ['horse', 'shampoo', 'dress']

# Remove grinder, speaker, and sock from Box 6
box_6.remove('grinder')
box_6.remove('speaker')
box_6.remove('sock')

# Move tree from Box 1 to Box 3
box_3.append(box_1.pop(0))

# Empty Box 4
box_4.clear()

# Swap controller in Box 10 with zipper in Box 0
box_0.remove('zipper')
box_10.remove('controller')
box_0.append('controller')
box_10.append('zipper')

# Remove tree, scarf, and lock from Box 3
box_3.remove('tree')
box_3.remove('scarf')
box_3.remove('lock')

# Swap shampoo in Box 12 with ring in Box 0
box_0.remove('ring')
box_12.remove('shampoo')
box_0.append('shampoo')
box_12.append('ring')

# Remove chair, lamp, and bracelet from Box 9
box_9.remove('chair')
box_9.remove('lamp')
box_9.remove('bracelet')

# Put puzzle, dolphin, and tree into Box 2
box_2.extend(['puzzle', 'dolphin', 'tree'])

# Swap paint in Box 10 with sun in Box 9
box_9.remove('sun')
box_10.remove('paint')
box_9.append('paint')
box_10.append('sun')

# Swap freezer in Box 0 with sun in Box 10
box_0.remove('freezer')
box_10.remove('sun')
box_0.append('sun')
box_10.append('freezer')

# Swap dice in Box 5 with pot in Box 7
box_5.remove('dice')
box_7.remove('pot')
box_5.append('pot')
box_7.append('dice')

# Remove dice and rocket from Box 7
box_7.remove('dice')
box_7.remove('rocket')

# Replace puzzle with game in Box 2
box_2.remove('puzzle')
box_2.append('game')

# Move shampoo and sun from Box 0 to Box 3
box_3.append(box_0.pop(0))
box_3.append(box_0.pop(0))

# Put boot, rain, and lamp into Box 5
box_5.extend(['boot', 'rain', 'lamp'])

# Put crown and ring into Box 4
box_4.extend(['crown', 'ring'])

# Move keyboard from Box 7 to Box 8
box_8.append(box_7.pop(1))

# Remove paint from Box 9
box_9.remove('paint')

# Replace shampoo and sun with razor and dog in Box 3
box_3.remove('shampoo')
box_3.remove('sun')
box_3.extend(['razor', 'dog'])

# Print the contents of each box
for i, box in enumerate([box_0, box_1, box_2, box_3, box_4, box_5, box_6, box_7, box_8, box_9, box_10, box_11, box_12]):
    print(f"Box {i}: {box}")