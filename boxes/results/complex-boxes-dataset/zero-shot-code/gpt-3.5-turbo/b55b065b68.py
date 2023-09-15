box_0 = ['ocean']
box_1 = ['cat', 'moon', 'island', 'shirt', 'hat']
box_2 = []
box_3 = ['dog', 'blender']
box_4 = ['brush', 'star', 'bird', 'button']
box_5 = ['boat', 'planet', 'jungle', 'battery', 'umbrella']
box_6 = ['train', 'toy']
box_7 = []
box_8 = ['cow', 'cup', 'coral', 'toaster']
box_9 = ['frame', 'truck']
box_10 = ['mirror', 'violin', 'harmonica', 'pillow', 'towel']
box_11 = []
box_12 = []
box_13 = ['whistle', 'speaker', 'bicycle', 'toothpaste', 'card']

# Put the sandals and the toothpaste into Box 8
box_8.extend(['sandals', 'toothpaste'])

# Move the violin and the pillow from Box 10 to Box 1
box_1.extend([box_10.pop(box_10.index('violin')), box_10.pop(box_10.index('pillow'))])

# Put the grinder and the coral into Box 6
box_6.extend(['grinder', 'coral'])

# Swap the dog in Box 3 with the frame in Box 9
box_3[box_3.index('dog')], box_9[box_9.index('frame')] = box_9[box_9.index('frame')], box_3[box_3.index('dog')]

# Move the harmonica and the towel from Box 10 to Box 1
box_1.extend([box_10.pop(box_10.index('harmonica')), box_10.pop(box_10.index('towel'))])

# Put the paint and the watch and the mixer into Box 4
box_4.extend(['paint', 'watch', 'mixer'])

# Move the towel and the pillow from Box 1 to Box 10
box_10.extend([box_1.pop(box_1.index('towel')), box_1.pop(box_1.index('pillow'))])

# Replace the jungle with the candle in Box 5
box_5[box_5.index('jungle')] = 'candle'

# Replace the ocean with the mask in Box 0
box_0[0] = 'mask'

# Move the mirror from Box 10 to Box 2
box_2.append(box_10.pop(box_10.index('mirror')))

# Replace the mirror with the belt in Box 2
box_2[0] = 'belt'

# Replace the harmonica and the hat with the zipper and the puzzle in Box 1
box_1[box_1.index('harmonica')], box_1[box_1.index('hat')] = 'zipper', 'puzzle'

# Replace the blender and the frame with the perfume and the dog in Box 3
box_3[box_3.index('blender')], box_3[box_3.index('frame')] = 'perfume', 'dog'

# Empty Box 4
box_4.clear()

# Replace the toy and the train and the coral with the seaweed and the plane and the polish in Box 6
box_6[box_6.index('toy')], box_6[box_6.index('train')], box_6[box_6.index('coral')] = 'seaweed', 'plane', 'polish'

# Replace the mask with the meteor in Box 0
box_0[0] = 'meteor'

# Put the coat and the lock into Box 5
box_5.extend(['coat', 'lock'])

# Replace the toothpaste and the cup with the coat and the comb in Box 8
box_8[box_8.index('toothpaste')], box_8[box_8.index('cup')] = 'coat', 'comb'

# Swap the dog in Box 9 with the dog in Box 3
box_9[box_9.index('dog')], box_3[box_3.index('dog')] = box_3[box_3.index('dog')], box_9[box_9.index('dog')]

# Remove the meteor from Box 0
box_0.clear()

# Put the octopus and the note into Box 9
box_9.extend(['octopus', 'note'])

# Print the contents of each box
for i, box in enumerate([box_0, box_1, box_2, box_3, box_4, box_5, box_6, box_7, box_8, box_9, box_10, box_11, box_12, box_13]):
    print(f"Box {i}: {box}")