# Initial state of boxes
boxes = {
    0: ['tape', 'mixer', 'paint'],
    1: ['lightning', 'apple', 'rain'],
    2: [],
    3: ['dress', 'pan'],
    4: ['cow', 'umbrella', 'lock', 'phone'],
    5: ['butterfly', 'watch'],
    6: [],
    7: ['game', 'table', 'freezer'],
    8: [],
    9: ['perfume', 'charger'],
    10: ['vase', 'shorts', 'polish', 'forest'],
    11: ['toaster', 'controller', 'doll', 'tree', 'lamp'],
    12: [],
    13: ['violin', 'chair', 'belt', 'coral', 'dolphin'],
    14: ['toothbrush', 'needle', 'coin']
}

# Replace the toothbrush and the coin and the needle with the puzzle and the microscope and the controller in Box 14.
boxes[14].remove('toothbrush')
boxes[14].remove('needle')
boxes[14].remove('coin')
boxes[14].append('puzzle')
boxes[14].append('microscope')
boxes[14].append('controller')

# Remove the toaster and the tree and the lamp from Box 11.
boxes[11].remove('toaster')
boxes[11].remove('tree')
boxes[11].remove('lamp')

# Swap the apple in Box 1 with the dress in Box 3.
boxes[1].remove('apple')
boxes[3].remove('dress')
boxes[1].append('dress')
boxes[3].append('apple')

# Remove the controller from Box 11.
boxes[11].remove('controller')

# Swap the pan in Box 3 with the shorts in Box 10.
boxes[3].remove('pan')
boxes[10].remove('shorts')
boxes[3].append('shorts')
boxes[10].append('pan')

# Move the shorts from Box 3 to Box 5.
boxes[3].remove('shorts')
boxes[5].append('shorts')

# Put the vase into Box 8.
boxes[10].remove('vase')
boxes[8].append('vase')

# Put the polish and the dolphin into Box 6.
boxes[10].remove('polish')
boxes[13].remove('dolphin')
boxes[6].append('polish')
boxes[6].append('dolphin')

# Remove the apple from Box 3.
boxes[3].remove('apple')

# Move the phone and the umbrella and the lock from Box 4 to Box 10.
items_to_move = ['phone', 'umbrella', 'lock']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[10].append(item)

# Swap the forest in Box 10 with the vase in Box 8.
boxes[10].remove('forest')
boxes[8].remove('vase')
boxes[10].append('vase')
boxes[8].append('forest')

# Replace the butterfly with the elephant in Box 5.
boxes[5].remove('butterfly')
boxes[5].append('elephant')

# Swap the rain in Box 1 with the mixer in Box 0.
boxes[1].remove('rain')
boxes[0].remove('mixer')
boxes[1].append('mixer')
boxes[0].append('rain')

# Move the perfume and the charger from Box 9 to Box 1.
items_to_move = ['perfume', 'charger']
for item in items_to_move:
    boxes[9].remove(item)
    boxes[1].append(item)

# Put the bell and the snow into Box 3.
boxes[3].append('bell')
boxes[3].append('snow')

# Move the doll from Box 11 to Box 4.
boxes[11].remove('doll')
boxes[4].append('doll')

# Swap the violin in Box 13 with the pan in Box 10.
boxes[13].remove('violin')
boxes[10].remove('pan')
boxes[13].append('pan')
boxes[10].append('violin')

# Swap the table in Box 7 with the shorts in Box 5.
boxes[7].remove('table')
boxes[5].remove('shorts')
boxes[7].append('shorts')
boxes[5].append('table')

# Replace the paint and the tape with the pants and the sock in Box 0.
boxes[0].remove('paint')
boxes[0].remove('tape')
boxes[0].append('pants')
boxes[0].append('sock')

# Remove the dolphin from Box 6.
boxes[6].remove('dolphin')

# Put the keyboard and the dolphin and the river into Box 12.
boxes[12].append('keyboard')
boxes[13].remove('dolphin')
boxes[12].append('dolphin')
boxes[12].append('river')

# Move the phone from Box 10 to Box 12.
boxes[10].remove('phone')
boxes[12].append('phone')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")