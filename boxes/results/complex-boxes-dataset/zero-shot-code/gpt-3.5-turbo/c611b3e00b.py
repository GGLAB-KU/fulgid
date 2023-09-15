box_0 = ['plate', 'branch', 'starfish', 'chair']
box_1 = ['microscope', 'guitar', 'fridge']
box_2 = []
box_3 = ['button']
box_4 = ['soap']
box_5 = ['violin', 'laptop', 'dog', 'helmet']
box_6 = ['planet', 'telescope']
box_7 = ['toaster', 'table', 'dress', 'island', 'glove']
box_8 = []
box_9 = ['bell', 'pants', 'frame']
box_10 = ['bowl', 'fork', 'shorts', 'mountain', 'cup']
box_11 = ['gloves']

# Remove the fridge and the guitar from Box 1
box_1.remove('fridge')
box_1.remove('guitar')

# Swap the microscope in Box 1 with the soap in Box 4
box_1.append(box_4[0])
box_4[0] = 'microscope'

# Remove the button from Box 3
box_3.remove('button')

# Put the pillow and the helmet into Box 8
box_8.extend(['pillow', 'helmet'])

# Put the sandals and the crown and the clock into Box 8
box_8.extend(['sandals', 'crown', 'clock'])

# Empty Box 7
box_7.clear()

# Put the island into Box 0
box_0.append('island')

# Replace the frame and the pants with the microscope and the usb in Box 9
box_9.remove('frame')
box_9.remove('pants')
box_9.extend(['microscope', 'usb'])

# Put the octopus into Box 11
box_11.append('octopus')

# Move the gloves from Box 11 to Box 0
box_0.extend(box_11)
box_11.clear()

# Swap the mountain in Box 10 with the octopus in Box 11
box_10.remove('mountain')
box_11.append('mountain')

# Remove the mountain from Box 11
box_11.remove('mountain')

# Move the microscope from Box 4 to Box 6
box_6.append(box_4[0])
box_4.clear()

# Swap the soap in Box 1 with the chair in Box 0
box_0.append(box_1[0])
box_1[0] = 'soap'

# Move the dog from Box 5 to Box 9
box_9.append(box_5.pop(box_5.index('dog')))

# Replace the pillow and the crown with the basket and the sculpture in Box 8
box_8.remove('pillow')
box_8.remove('crown')
box_8.extend(['basket', 'sculpture'])

# Put the scarf and the charger and the whistle into Box 5
box_5.extend(['scarf', 'charger', 'whistle'])

# Swap the clock in Box 8 with the chair in Box 1
box_1.append(box_8.pop(box_8.index('chair')))
box_8.append('clock')

# Print the contents of each box
for i, box in enumerate([box_0, box_1, box_2, box_3, box_4, box_5, box_6, box_7, box_8, box_9, box_10, box_11]):
    print(f"Box {i}: {box}")