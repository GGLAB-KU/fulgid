box_0 = ['boat', 'rain', 'toy', 'snow', 'fridge']
box_1 = []
box_2 = ['spoon', 'apple', 'beach', 'cup', 'lock']
box_3 = []
box_4 = ['harmonica', 'pants', 'candle']
box_5 = ['horse', 'camera', 'mirror', 'table', 'dress']
box_6 = ['toothpaste', 'toothbrush']
box_7 = ['elephant', 'controller', 'razor', 'microwave']
box_8 = ['necklace', 'sun']
box_9 = ['storm']
box_10 = ['zipper', 'freezer', 'thunder', 'phone', 'star']
box_11 = []

# Swap toothpaste in Box 6 with toy in Box 0
box_0[box_0.index('toy')], box_6[box_6.index('toothpaste')] = box_6[box_6.index('toothpaste')], box_0[box_0.index('toy')]

# Swap dress in Box 5 with storm in Box 9
box_5[box_5.index('dress')], box_9[box_9.index('storm')] = box_9[box_9.index('storm')], box_5[box_5.index('dress')]

# Remove toy from Box 6
box_6.remove('toy')

# Move microwave, controller, and razor from Box 7 to Box 10
box_10.extend(box_7[1:4])
box_7[1:4] = []

# Swap mirror in Box 5 with snow in Box 0
box_0[box_0.index('snow')], box_5[box_5.index('mirror')] = box_5[box_5.index('mirror')], box_0[box_0.index('snow')]

# Swap beach in Box 2 with elephant in Box 7
box_2[box_2.index('beach')], box_7[box_7.index('elephant')] = box_7[box_7.index('elephant')], box_2[box_2.index('beach')]

# Remove beach from Box 7
box_7.remove('beach')

# Remove toothbrush from Box 6
box_6.remove('toothbrush')

# Remove sun and necklace from Box 8
box_8.remove('sun')
box_8.remove('necklace')

# Remove cup, apple, and lock from Box 2
box_2.remove('cup')
box_2.remove('apple')
box_2.remove('lock')

# Move star, razor, and thunder from Box 10 to Box 8
box_8.extend(box_10[4:7])
box_10[4:7] = []

# Swap dress in Box 9 with horse in Box 5
box_5[box_5.index('dress')], box_9[box_9.index('horse')] = box_9[box_9.index('horse')], box_5[box_5.index('dress')]

# Remove horse from Box 9
box_9.remove('horse')

# Remove star from Box 8
box_8.remove('star')

# Replace controller, zipper, and phone with hat, sculpture, and paint in Box 10
box_10[box_10.index('controller')] = 'hat'
box_10[box_10.index('zipper')] = 'sculpture'
box_10[box_10.index('phone')] = 'paint'

# Replace pants with meteor in Box 4
box_4[box_4.index('pants')] = 'meteor'

# Replace elephant with perfume in Box 2
box_2[box_2.index('elephant')] = 'perfume'

# Swap freezer in Box 10 with perfume in Box 2
box_10[box_10.index('freezer')], box_2[box_2.index('perfume')] = box_2[box_2.index('perfume')], box_10[box_10.index('freezer')]

# Print the contents of each box
for i, box in enumerate([box_0, box_1, box_2, box_3, box_4, box_5, box_6, box_7, box_8, box_9, box_10, box_11]):
    print(f"Box {i}: {box}")