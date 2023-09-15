box_0 = ['bowl', 'table', 'piano', 'tree', 'pillow']
box_1 = ['thread', 'paint', 'ring', 'umbrella', 'cloud']
box_2 = ['truck', 'submarine']
box_3 = ['plane', 'controller']
box_4 = []
box_5 = ['bracelet', 'dress', 'boot']
box_6 = []
box_7 = ['apple', 'jacket', 'pants', 'helmet', 'dog']
box_8 = ['train', 'swimsuit', 'necklace', 'makeup', 'phone']
box_9 = ['book']
box_10 = ['bag']
box_11 = ['comb', 'whistle', 'tiger', 'beach', 'clock']
box_12 = []
box_13 = []

# Swap the umbrella in Box 1 with the table in Box 0
box_0[1], box_1[3] = box_1[3], box_0[1]

# Put the book and the forest and the mixer into Box 13
box_13.extend(['book', 'forest', 'mixer'])

# Replace the tree and the bowl with the butterfly and the sandals in Box 0
box_0[0] = 'butterfly'
box_0.append('sandals')

# Remove the truck and the submarine from Box 2
box_2.clear()

# Swap the bag in Box 10 with the apple in Box 7
box_10[0], box_7[0] = box_7[0], box_10[0]

# Replace the phone and the makeup and the train with the river and the camera and the glove in Box 8
box_8[3] = 'river'
box_8[4] = 'camera'
box_8[0] = 'glove'

# Replace the tiger with the towel in Box 11
box_11[2] = 'towel'

# Move the paint and the table from Box 1 to Box 7
box_7.extend([box_1[1], box_1[0]])
box_1.remove('paint')
box_1.remove('table')

# Put the towel and the grass into Box 8
box_8.extend(['towel', 'grass'])

# Swap the plane in Box 3 with the swimsuit in Box 8
box_3[0], box_8[1] = box_8[1], box_3[0]

# Swap the book in Box 13 with the bracelet in Box 5
box_13[0], box_5[0] = box_5[0], box_13[0]

# Remove the book from Box 9
box_9.clear()

# Move the mixer and the forest from Box 13 to Box 2
box_2.extend([box_13[1], box_13[2]])
box_13.remove('mixer')
box_13.remove('forest')

# Put the microscope and the paint and the bear into Box 4
box_4.extend(['microscope', 'paint', 'bear'])

# Move the cloud and the thread and the ring from Box 1 to Box 0
box_0.extend([box_1[4], box_1[0], box_1[2]])
box_1.remove('cloud')
box_1.remove('thread')
box_1.remove('ring')

# Move the swimsuit and the controller from Box 3 to Box 9
box_9.extend([box_3[1], box_3[0]])
box_3.remove('swimsuit')
box_3.remove('controller')

# Move the pillow and the butterfly and the thread from Box 0 to Box 13
box_13.extend([box_0[4], box_0[0], box_0[3]])
box_0.remove('pillow')
box_0.remove('butterfly')
box_0.remove('thread')

# Remove the mixer from Box 2
box_2.clear()

# Put the mirror and the star into Box 7
box_7.extend(['mirror', 'star'])

# Remove the butterfly and the bracelet and the thread from Box 13
box_13.remove('butterfly')
box_13.remove('bracelet')
box_13.remove('thread')

# Move the beach and the whistle from Box 11 to Box 0
box_0.extend([box_11[3], box_11[1]])
box_11.remove('beach')
box_11.remove('whistle')

# Print the contents of each box
for i, box in enumerate([box_0, box_1, box_2, box_3, box_4, box_5, box_6, box_7, box_8, box_9, box_10, box_11, box_12, box_13]):
    print(f"Box {i}: {box}")