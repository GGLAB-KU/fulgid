box_0 = []
box_1 = ['harmonica']
box_2 = ['belt', 'bicycle', 'speaker']
box_3 = ['lamp', 'watch', 'toaster', 'shelf']
box_4 = ['comb', 'crown', 'sculpture', 'branch', 'coral']
box_5 = ['soap', 'pot', 'tape', 'apple']
box_6 = ['doll', 'tree', 'dress', 'shirt']
box_7 = ['truck', 'usb', 'pants', 'motorcycle']
box_8 = ['frame', 'umbrella', 'lightning', 'table']
box_9 = ['guitar', 'pillow', 'island', 'controller']
box_10 = ['bag', 'spoon', 'puzzle', 'glove', 'lipstick']
box_11 = []
box_12 = ['note']

# Swap the controller in Box 9 with the bicycle in Box 2
box_9.remove('controller')
box_2.remove('bicycle')
box_9.append('bicycle')
box_2.append('controller')

# Remove the toaster and the watch and the shelf from Box 3
box_3.remove('toaster')
box_3.remove('watch')
box_3.remove('shelf')

# Remove the clock from Box 2
box_2.remove('clock')

# Swap the note in Box 12 with the umbrella in Box 8
box_12.remove('note')
box_8.remove('umbrella')
box_12.append('umbrella')
box_8.append('note')

# Replace the truck with the belt in Box 7
box_7.remove('truck')
box_7.append('belt')

# Swap the table in Box 8 with the spoon in Box 10
box_8.remove('table')
box_10.remove('spoon')
box_8.append('spoon')
box_10.append('table')

# Swap the harmonica in Box 1 with the note in Box 8
box_1.remove('harmonica')
box_8.remove('note')
box_1.append('note')
box_8.append('harmonica')

# Move the pants and the usb and the belt from Box 7 to Box 2
box_7.remove('pants')
box_7.remove('usb')
box_7.remove('belt')
box_2.append('pants')
box_2.append('usb')
box_2.append('belt')

# Replace the umbrella with the cat in Box 12
box_12.remove('umbrella')
box_12.append('cat')

# Replace the coral and the branch and the sculpture with the dolphin and the gloves and the sun in Box 4
box_4.remove('coral')
box_4.remove('branch')
box_4.remove('sculpture')
box_4.append('dolphin')
box_4.append('gloves')
box_4.append('sun')

# Put the violin and the battery and the usb into Box 7
box_7.append('violin')
box_7.append('battery')
box_7.append('usb')

# Move the guitar from Box 9 to Box 4
box_9.remove('guitar')
box_4.append('guitar')

# Put the shark and the pillow into Box 2
box_2.append('shark')
box_2.append('pillow')

# Swap the violin in Box 7 with the tape in Box 5
box_7.remove('violin')
box_5.remove('tape')
box_7.append('tape')
box_5.append('violin')

# Swap the lamp in Box 3 with the cat in Box 12
box_3.remove('lamp')
box_12.remove('cat')
box_3.append('cat')
box_12.append('lamp')

# Replace the controller and the belt with the dog and the phone in Box 2
box_2.remove('controller')
box_2.remove('belt')
box_2.append('dog')
box_2.append('phone')

# Put the pen into Box 10
box_10.append('pen')

# Move the cat from Box 3 to Box 2
box_3.remove('cat')
box_2.append('cat')

# Put the mountain into Box 4
box_4.append('mountain')

# Print the contents of each box
for i in range(13):
    print(f"Box {i}: {globals()[f'box_{i}']}")