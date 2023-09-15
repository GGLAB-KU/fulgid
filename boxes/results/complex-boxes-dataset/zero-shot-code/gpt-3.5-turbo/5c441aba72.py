box_0 = ['mountain', 'phone', 'thunder', 'bag']
box_1 = ['toaster', 'bicycle', 'umbrella']
box_2 = ['bracelet', 'lion']
box_3 = ['harmonica', 'skirt', 'car', 'comet', 'tape']
box_4 = ['flower', 'cloud', 'shampoo', 'pants', 'guitar']
box_5 = ['card', 'dog', 'horn', 'comb', 'keyboard']
box_6 = ['piano', 'pan', 'towel']
box_7 = ['usb', 'brush', 'rock', 'butterfly', 'sun']
box_8 = ['frame']
box_9 = ['scarf', 'lamp', 'soap', 'beach', 'boat']
box_10 = ['shark']
box_11 = ['wig', 'branch', 'lipstick', 'battery']
box_12 = ['blanket', 'microwave', 'river', 'train', 'book']
box_13 = ['toothbrush', 'mirror', 'swimsuit', 'tie']
box_14 = ['bear']

# Move the umbrella and the toaster from Box 1 to Box 3
box_3.extend([box_1.pop(box_1.index('umbrella')), box_1.pop(box_1.index('toaster'))])

# Put the pan and the sculpture into Box 0
box_0.extend(['pan', 'sculpture'])

# Replace the tie with the bell in Box 13
box_13[box_13.index('tie')] = 'bell'

# Empty Box 11
box_11.clear()

# Move the horn and the card from Box 5 to Box 11
box_11.extend([box_5.pop(box_5.index('horn')), box_5.pop(box_5.index('card'))])

# Replace the phone and the sculpture and the thunder with the submarine and the wire and the cup in Box 0
box_0[box_0.index('phone')] = 'submarine'
box_0[box_0.index('sculpture')] = 'wire'
box_0[box_0.index('thunder')] = 'cup'

# Swap the boat in Box 9 with the bear in Box 14
box_9[box_9.index('boat')], box_14[box_14.index('bear')] = box_14[box_14.index('bear')], box_9[box_9.index('boat')]

# Move the shark from Box 10 to Box 9
box_9.append(box_10.pop())

# Put the flower into Box 14
box_14.append(box_4.pop(box_4.index('flower')))

# Move the pants and the flower and the cloud from Box 4 to Box 11
box_11.extend([box_4.pop(box_4.index('pants')), box_4.pop(box_4.index('flower')), box_4.pop(box_4.index('cloud'))])

# Move the microwave and the book and the train from Box 12 to Box 1
box_1.extend([box_12.pop(box_12.index('microwave')), box_12.pop(box_12.index('book')), box_12.pop(box_12.index('train'))])

# Put the desert into Box 4
box_4.append('desert')

# Replace the flower with the shark in Box 14
box_14[box_14.index('flower')] = 'shark'

# Replace the desert with the dress in Box 4
box_4[box_4.index('desert')] = 'dress'

# Replace the piano with the chair in Box 6
box_6[box_6.index('piano')] = 'chair'

# Swap the mirror in Box 13 with the pan in Box 6
box_13[box_13.index('mirror')], box_6[box_6.index('pan')] = box_6[box_6.index('pan')], box_13[box_13.index('mirror')]

# Remove the keyboard from Box 5
box_5.remove('keyboard')

# Remove the soap and the beach and the bear from Box 9
box_9.remove('soap')
box_9.remove('beach')
box_9.remove('bear')

# Move the bracelet from Box 2 to Box 11
box_11.append(box_2.pop(box_2.index('bracelet')))

# Swap the frame in Box 8 with the lamp in Box 9
box_8[box_8.index('frame')], box_9[box_9.index('lamp')] = box_9[box_9.index('lamp')], box_8[box_8.index('frame')]

# Replace the microwave with the glove in Box 1
box_1[box_1.index('microwave')] = 'glove'

# Swap the mirror in Box 6 with the dress in Box 4
box_6[box_6.index('mirror')], box_4[box_4.index('dress')] = box_4[box_4.index('dress')], box_6[box_6.index('mirror')]

# Print the contents of each box
for i, box in enumerate([box_0, box_1, box_2, box_3, box_4, box_5, box_6, box_7, box_8, box_9, box_10, box_11, box_12, box_13, box_14]):
    print(f"Box {i}: {box}")