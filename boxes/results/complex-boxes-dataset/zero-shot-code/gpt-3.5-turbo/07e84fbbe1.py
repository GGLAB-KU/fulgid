box_0 = ['sandals', 'lipstick', 'pan', 'cat']
box_1 = ['ocean', 'elephant', 'laptop', 'meteor']
box_2 = ['blanket']
box_3 = ['bus', 'tie', 'train']
box_4 = ['paint', 'whistle']
box_5 = ['makeup', 'lion', 'towel', 'fridge', 'violin']
box_6 = ['plane', 'sun', 'bowl']
box_7 = []
box_8 = ['dice']
box_9 = []
box_10 = ['razor', 'game', 'horn']
box_11 = []

# Move the towel from Box 5 to Box 4
box_4.append(box_5.pop(box_5.index('towel')))

# Remove the dice from Box 8
box_8.remove('dice')

# Remove the bus and the train and the tie from Box 3
box_3.remove('bus')
box_3.remove('tie')
box_3.remove('train')

# Move the plane from Box 6 to Box 10
box_10.append(box_6.pop(box_6.index('plane')))

# Put the skirt and the spoon into Box 8
box_8.extend(['skirt', 'spoon'])

# Put the towel and the grass into Box 5
box_5.extend(['towel', 'grass'])

# Replace the cat and the sandals with the needle and the pot in Box 0
box_0.remove('cat')
box_0.remove('sandals')
box_0.extend(['needle', 'pot'])

# Move the paint from Box 4 to Box 2
box_2.append(box_4.pop(box_4.index('paint')))

# Swap the whistle in Box 4 with the razor in Box 10
box_4.append(box_10.pop(box_10.index('razor')))
box_10.append('whistle')

# Put the thread into Box 0
box_0.append('thread')

# Move the makeup and the towel and the lion from Box 5 to Box 4
box_4.extend(['makeup', 'towel', 'lion'])
box_5.remove('makeup')
box_5.remove('towel')
box_5.remove('lion')

# Remove the elephant from Box 1
box_1.remove('elephant')

# Swap the spoon in Box 8 with the meteor in Box 1
box_1.append(box_8.pop(box_8.index('spoon')))
box_8.append('meteor')

# Remove the grass from Box 5
box_5.remove('grass')

# Replace the blanket and the paint with the ring and the button in Box 2
box_2.remove('blanket')
box_2.remove('paint')
box_2.extend(['ring', 'button'])

# Empty Box 10
box_10.clear()

# Remove the bowl and the sun from Box 6
box_6.remove('bowl')
box_6.remove('sun')

# Move the skirt from Box 8 to Box 9
box_9.append(box_8.pop(box_8.index('skirt')))

# Print the contents of each box
for i, box in enumerate([box_0, box_1, box_2, box_3, box_4, box_5, box_6, box_7, box_8, box_9, box_10, box_11]):
    print(f"Box {i}: {box}")