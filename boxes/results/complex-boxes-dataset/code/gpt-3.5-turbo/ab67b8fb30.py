# Initial state of boxes
boxes = {
    0: ['skirt', 'fork', 'island'],
    1: ['sun', 'basket', 'tree', 'bowl', 'apple'],
    2: ['soap', 'meteor', 'pen', 'controller', 'desert'],
    3: ['planet'],
    4: ['mixer', 'river', 'pants', 'mask'],
    5: ['bicycle', 'toy'],
    6: ['cow'],
    7: ['telescope', 'watch'],
    8: ['shirt', 'forest', 'lipstick'],
    9: ['bag'],
    10: ['book', 'branch', 'train', 'bell'],
    11: ['bus', 'rocket']
}

# Swap the toy in Box 5 with the controller in Box 2.
boxes[2].remove('controller')
boxes[5].remove('toy')
boxes[2].append('toy')
boxes[5].append('controller')

# Put the shark and the plane and the pants into Box 9.
items_to_put = ['shark', 'plane', 'pants']
for item in items_to_put:
    boxes[9].append(item)

# Move the fork and the skirt and the island from Box 0 to Box 5.
items_to_move = ['fork', 'skirt', 'island']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[5].append(item)

# Replace the fork and the island and the bicycle with the pan and the boat and the laptop in Box 5.
boxes[5].remove('fork')
boxes[5].remove('island')
boxes[5].remove('bicycle')
boxes[5].append('pan')
boxes[5].append('boat')
boxes[5].append('laptop')

# Put the comb into Box 3.
boxes[3].append('comb')

# Remove the forest and the shirt and the lipstick from Box 8.
items_to_remove = ['forest', 'shirt', 'lipstick']
for item in items_to_remove:
    boxes[8].remove(item)

# Empty Box 11.
boxes[11] = []

# Put the star and the bus into Box 2.
boxes[2].append('star')
boxes[2].append('bus')

# Replace the controller and the pan and the boat with the tie and the earring and the mixer in Box 5.
boxes[5].remove('controller')
boxes[5].remove('pan')
boxes[5].remove('boat')
boxes[5].append('tie')
boxes[5].append('earring')
boxes[5].append('mixer')

# Empty Box 5.
boxes[5] = []

# Put the branch into Box 0.
boxes[0].append('branch')

# Remove the pants and the shark from Box 9.
boxes[9].remove('pants')
boxes[9].remove('shark')

# Replace the branch with the shoes in Box 10.
boxes[10].remove('branch')
boxes[10].append('shoes')

# Put the wallet and the lipstick and the vase into Box 2.
items_to_put = ['wallet', 'lipstick', 'vase']
for item in items_to_put:
    boxes[2].append(item)

# Empty Box 1.
boxes[1] = []

# Remove the train and the shoes from Box 10.
boxes[10].remove('train')
boxes[10].remove('shoes')

# Put the freezer into Box 3.
boxes[3].append('freezer')

# Replace the comb and the freezer and the planet with the key and the pan and the bus in Box 3.
boxes[3].remove('comb')
boxes[3].remove('freezer')
boxes[3].remove('planet')
boxes[3].append('key')
boxes[3].append('pan')
boxes[3].append('bus')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")