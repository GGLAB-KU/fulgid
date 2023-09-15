box_0 = ['card', 'oven', 'note', 'polish']
box_1 = ['seaweed', 'rocket', 'butterfly', 'tree', 'umbrella']
box_2 = ['planet', 'moon']
box_3 = ['bicycle', 'pan']
box_4 = ['car', 'shoes', 'fish', 'beach']
box_5 = ['island', 'shoe', 'guitar', 'plane', 'bell']
box_6 = ['spoon']
box_7 = ['forest', 'vase', 'meteor', 'dog', 'desert']
box_8 = ['coin', 'speaker', 'scarf', 'star']
box_9 = ['toaster', 'helmet', 'lamp', 'pen']
box_10 = []
box_11 = []
box_12 = []

# Replace the bicycle with the soap in Box 3
box_3.remove('bicycle')
box_3.append('soap')

# Put the rain into Box 10
box_10.append('rain')

# Remove the pen and the toaster and the lamp from Box 9
box_9.remove('pen')
box_9.remove('toaster')
box_9.remove('lamp')

# Remove the spoon from Box 6
box_6.remove('spoon')

# Put the makeup into Box 12
box_12.append('makeup')

# Put the chair and the river into Box 4
box_4.append('chair')
box_4.append('river')

# Remove the pan and the soap from Box 3
box_3.remove('pan')
box_3.remove('soap')

# Swap the star in Box 8 with the planet in Box 2
box_8.remove('star')
box_2.remove('planet')
box_8.append('planet')
box_2.append('star')

# Remove the moon and the star from Box 2
box_2.remove('moon')
box_2.remove('star')

# Move the guitar from Box 5 to Box 11
box_5.remove('guitar')
box_11.append('guitar')

# Swap the shoe in Box 5 with the rain in Box 10
box_5.remove('shoe')
box_10.remove('rain')
box_5.append('rain')
box_10.append('shoe')

# Move the shoe from Box 10 to Box 8
box_10.remove('shoe')
box_8.append('shoe')

# Swap the makeup in Box 12 with the tree in Box 1
box_12.remove('makeup')
box_1.remove('tree')
box_12.append('tree')
box_1.append('makeup')

# Remove the tree from Box 12
box_12.remove('tree')

# Swap the rocket in Box 1 with the fish in Box 4
box_1.remove('rocket')
box_4.remove('fish')
box_1.append('fish')
box_4.append('rocket')

# Remove the umbrella from Box 1
box_1.remove('umbrella')

# Remove the seaweed and the butterfly and the makeup from Box 1
box_1.remove('seaweed')
box_1.remove('butterfly')
box_1.remove('makeup')

# Put the horse into Box 4
box_4.append('horse')

# Remove the dog and the desert from Box 7
box_7.remove('dog')
box_7.remove('desert')

# Print the contents of each box
for i, box in enumerate([box_0, box_1, box_2, box_3, box_4, box_5, box_6, box_7, box_8, box_9, box_10, box_11, box_12]):
    print(f"Box {i}: {box}")