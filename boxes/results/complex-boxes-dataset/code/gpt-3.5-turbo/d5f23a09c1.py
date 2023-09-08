# Initial state of boxes
boxes = {
    0: ['card', 'oven', 'note', 'polish'],
    1: ['seaweed', 'rocket', 'butterfly', 'tree', 'umbrella'],
    2: ['planet', 'moon'],
    3: ['bicycle', 'pan'],
    4: ['car', 'shoes', 'fish', 'beach'],
    5: ['island', 'shoe', 'guitar', 'plane', 'bell'],
    6: ['spoon'],
    7: ['forest', 'vase', 'meteor', 'dog', 'desert'],
    8: ['coin', 'speaker', 'scarf', 'star'],
    9: ['toaster', 'helmet', 'lamp', 'pen'],
    10: [],
    11: [],
    12: []
}

# Replace the bicycle with the soap in Box 3.
boxes[3].remove('bicycle')
boxes[3].append('soap')

# Put the rain into Box 10.
boxes[10].append('rain')

# Remove the pen and the toaster and the lamp from Box 9.
items_to_remove = ['pen', 'toaster', 'lamp']
for item in items_to_remove:
    boxes[9].remove(item)

# Remove the spoon from Box 6.
boxes[6].remove('spoon')

# Put the makeup into Box 12.
boxes[12].append('makeup')

# Put the chair and the river into Box 4.
items_to_add = ['chair', 'river']
for item in items_to_add:
    boxes[4].append(item)

# Remove the pan and the soap from Box 3.
items_to_remove = ['pan', 'soap']
for item in items_to_remove:
    boxes[3].remove(item)

# Swap the star in Box 8 with the planet in Box 2.
boxes[8].remove('star')
boxes[2].remove('planet')
boxes[8].append('planet')
boxes[2].append('star')

# Remove the moon and the star from Box 2.
items_to_remove = ['moon', 'star']
for item in items_to_remove:
    boxes[2].remove(item)

# Move the guitar from Box 5 to Box 11.
boxes[5].remove('guitar')
boxes[11].append('guitar')

# Swap the shoe in Box 5 with the rain in Box 10.
boxes[5].remove('shoe')
boxes[10].remove('rain')
boxes[5].append('rain')
boxes[10].append('shoe')

# Move the shoe from Box 10 to Box 8.
boxes[10].remove('shoe')
boxes[8].append('shoe')

# Swap the makeup in Box 12 with the tree in Box 1.
boxes[12].remove('makeup')
boxes[1].remove('tree')
boxes[12].append('tree')
boxes[1].append('makeup')

# Remove the tree from Box 12.
boxes[12].remove('tree')

# Swap the rocket in Box 1 with the fish in Box 4.
boxes[1].remove('rocket')
boxes[4].remove('fish')
boxes[1].append('fish')
boxes[4].append('rocket')

# Remove the umbrella from Box 1.
boxes[1].remove('umbrella')

# Remove the seaweed and the butterfly and the makeup from Box 1.
items_to_remove = ['seaweed', 'butterfly', 'makeup']
for item in items_to_remove:
    boxes[1].remove(item)

# Put the horse into Box 4.
boxes[4].append('horse')

# Remove the dog and the desert from Box 7.
items_to_remove = ['dog', 'desert']
for item in items_to_remove:
    boxes[7].remove(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")