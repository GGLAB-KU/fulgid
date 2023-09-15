box_0 = ['towel', 'mixer', 'pen']
box_1 = ['speaker', 'lightning', 'battery', 'soap', 'shorts']
box_2 = []
box_3 = ['basket', 'button', 'charger', 'plane', 'elephant']
box_4 = ['makeup', 'belt']
box_5 = []
box_6 = []
box_7 = ['coral', 'bag', 'boat', 'chair']
box_8 = ['branch', 'dress', 'flower']
box_9 = ['bus', 'lock', 'note', 'vase']
box_10 = ['blanket', 'sun', 'desert']
box_11 = ['bird', 'spoon', 'shark', 'microwave', 'pan']

# Swap the belt in Box 4 with the note in Box 9
box_4.remove('belt')
box_9.remove('note')
box_4.append('note')
box_9.append('belt')

# Put the controller into Box 3
box_3.append('controller')

# Move the lock from Box 9 to Box 3
box_9.remove('lock')
box_3.append('lock')

# Put the star into Box 0
box_0.append('star')

# Move the desert and the blanket and the sun from Box 10 to Box 8
box_10.remove('desert')
box_10.remove('blanket')
box_10.remove('sun')
box_8.extend(['desert', 'blanket', 'sun'])

# Swap the pan in Box 11 with the bus in Box 9
box_11.remove('pan')
box_9.remove('bus')
box_11.append('bus')
box_9.append('pan')

# Put the helmet and the pants into Box 3
box_3.extend(['helmet', 'pants'])

# Remove the elephant and the pants and the controller from Box 3
box_3.remove('elephant')
box_3.remove('pants')
box_3.remove('controller')

# Replace the chair and the coral and the boat with the tree and the skirt and the cup in Box 7
box_7.remove('chair')
box_7.remove('coral')
box_7.remove('boat')
box_7.extend(['tree', 'skirt', 'cup'])

# Swap the branch in Box 8 with the pan in Box 9
box_8.remove('branch')
box_9.remove('pan')
box_8.append('pan')
box_9.append('branch')

# Move the makeup and the note from Box 4 to Box 2
box_4.remove('makeup')
box_4.remove('note')
box_2.extend(['makeup', 'note'])

# Replace the star and the pen and the mixer with the horn and the dog and the hat in Box 0
box_0.remove('star')
box_0.remove('pen')
box_0.remove('mixer')
box_0.extend(['horn', 'dog', 'hat'])

# Replace the pan and the sun with the gloves and the zipper in Box 8
box_8.remove('pan')
box_8.remove('sun')
box_8.extend(['gloves', 'zipper'])

# Remove the zipper and the desert from Box 8
box_8.remove('zipper')
box_8.remove('desert')

# Remove the makeup and the note from Box 2
box_2.remove('makeup')
box_2.remove('note')

# Remove the cup and the tree and the skirt from Box 7
box_7.remove('cup')
box_7.remove('tree')
box_7.remove('skirt')

# Put the shoes and the bicycle into Box 6
box_6.extend(['shoes', 'bicycle'])

# Swap the spoon in Box 11 with the shorts in Box 1
box_11.remove('spoon')
box_1.remove('shorts')
box_11.append('shorts')
box_1.append('spoon')

# Print the contents of each box
for i, box in enumerate([box_0, box_1, box_2, box_3, box_4, box_5, box_6, box_7, box_8, box_9, box_10, box_11]):
    print(f"Box {i}: {box}")