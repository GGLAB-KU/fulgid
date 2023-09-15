box_0 = ['dress', 'rain', 'comb', 'button']
box_1 = ['coin', 'sock', 'charger', 'whistle', 'rock']
box_2 = ['bag', 'pillow']
box_3 = ['perfume']
box_4 = ['crown', 'puzzle', 'shampoo', 'note', 'submarine']
box_5 = ['brush', 'necklace', 'lock']
box_6 = ['cup', 'vase', 'comet', 'telescope', 'train']
box_7 = []
box_8 = ['polish', 'watch', 'freezer', 'book', 'blender']

# Remove the sock and the rock from Box 1
box_1.remove('sock')
box_1.remove('rock')

# Remove the polish from Box 8
box_8.remove('polish')

# Swap the blender in Box 8 with the charger in Box 1
box_1.remove('charger')
box_8.append('charger')
box_8.remove('blender')
box_1.append('blender')

# Put the boot into Box 2
box_2.append('boot')

# Move the necklace from Box 5 to Box 1
box_5.remove('necklace')
box_1.append('necklace')

# Swap the comet in Box 6 with the pillow in Box 2
box_6.remove('comet')
box_2.remove('pillow')
box_6.append('pillow')
box_2.append('comet')

# Move the comb and the dress from Box 0 to Box 2
box_0.remove('comb')
box_0.remove('dress')
box_2.append('comb')
box_2.append('dress')

# Remove the submarine and the note and the puzzle from Box 4
box_4.remove('submarine')
box_4.remove('note')
box_4.remove('puzzle')

# Replace the lock with the thunder in Box 5
box_5.remove('lock')
box_5.append('thunder')

# Swap the freezer in Box 8 with the button in Box 0
box_0.remove('button')
box_0.append('freezer')
box_8.remove('freezer')
box_8.append('button')

# Swap the bag in Box 2 with the freezer in Box 0
box_0.remove('freezer')
box_0.append('bag')
box_2.remove('bag')
box_2.append('freezer')

# Move the rain and the bag from Box 0 to Box 6
box_0.remove('rain')
box_6.append('rain')
box_0.remove('bag')
box_6.append('bag')

# Move the blender and the whistle from Box 1 to Box 2
box_1.remove('blender')
box_2.append('blender')
box_1.remove('whistle')
box_2.append('whistle')

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