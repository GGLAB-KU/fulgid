# Initial state of boxes
boxes = {
    0: ['mountain', 'phone', 'thunder', 'bag'],
    1: ['toaster', 'bicycle', 'umbrella'],
    2: ['bracelet', 'lion'],
    3: ['harmonica', 'skirt', 'car', 'comet', 'tape'],
    4: ['flower', 'cloud', 'shampoo', 'pants', 'guitar'],
    5: ['card', 'dog', 'horn', 'comb', 'keyboard'],
    6: ['piano', 'pan', 'towel'],
    7: ['usb', 'brush', 'rock', 'butterfly', 'sun'],
    8: ['frame'],
    9: ['scarf', 'lamp', 'soap', 'beach', 'boat'],
    10: ['shark'],
    11: ['wig', 'branch', 'lipstick', 'battery'],
    12: ['blanket', 'microwave', 'river', 'train', 'book'],
    13: ['toothbrush', 'mirror', 'swimsuit', 'tie'],
    14: ['bear']
}

# Move the umbrella and the toaster from Box 1 to Box 3.
boxes[1].remove('umbrella')
boxes[1].remove('toaster')
boxes[3].append('umbrella')
boxes[3].append('toaster')

# Put the pan and the sculpture into Box 0.
boxes[0].append('pan')
boxes[0].append('sculpture')

# Replace the tie with the bell in Box 13.
boxes[13].remove('tie')
boxes[13].append('bell')

# Empty Box 11.
boxes[11] = []

# Move the horn and the card from Box 5 to Box 11.
boxes[5].remove('horn')
boxes[5].remove('card')
boxes[11].append('horn')
boxes[11].append('card')

# Replace the phone and the sculpture and the thunder with the submarine and the wire and the cup in Box 0.
boxes[0].remove('phone')
boxes[0].remove('sculpture')
boxes[0].remove('thunder')
boxes[0].append('submarine')
boxes[0].append('wire')
boxes[0].append('cup')

# Swap the boat in Box 9 with the bear in Box 14.
boxes[9].remove('boat')
boxes[14].remove('bear')
boxes[9].append('bear')
boxes[14].append('boat')

# Move the shark from Box 10 to Box 9.
boxes[10].remove('shark')
boxes[9].append('shark')

# Put the flower into Box 14.
boxes[4].remove('flower')
boxes[14].append('flower')

# Move the pants and the flower and the cloud from Box 4 to Box 11.
boxes[4].remove('pants')
boxes[4].remove('flower')
boxes[4].remove('cloud')
boxes[11].append('pants')
boxes[11].append('flower')
boxes[11].append('cloud')

# Move the microwave and the book and the train from Box 12 to Box 1.
boxes[12].remove('microwave')
boxes[12].remove('book')
boxes[12].remove('train')
boxes[1].append('microwave')
boxes[1].append('book')
boxes[1].append('train')

# Put the desert into Box 4.
boxes[4].append('desert')

# Replace the flower with the shark in Box 14.
boxes[14].remove('flower')
boxes[14].append('shark')

# Replace the desert with the dress in Box 4.
boxes[4].remove('desert')
boxes[4].append('dress')

# Replace the piano with the chair in Box 6.
boxes[6].remove('piano')
boxes[6].append('chair')

# Swap the mirror in Box 13 with the pan in Box 6.
boxes[13].remove('mirror')
boxes[6].remove('pan')
boxes[13].append('pan')
boxes[6].append('mirror')

# Remove the keyboard from Box 5.
boxes[5].remove('keyboard')

# Remove the soap and the beach and the bear from Box 9.
boxes[9].remove('soap')
boxes[9].remove('beach')
boxes[9].remove('bear')

# Move the bracelet from Box 2 to Box 11.
boxes[2].remove('bracelet')
boxes[11].append('bracelet')

# Swap the frame in Box 8 with the lamp in Box 9.
boxes[8].remove('frame')
boxes[9].remove('lamp')
boxes[8].append('lamp')
boxes[9].append('frame')

# Replace the microwave with the glove in Box 1.
boxes[1].remove('microwave')
boxes[1].append('glove')

# Swap the mirror in Box 6 with the dress in Box 4.
boxes[6].remove('mirror')
boxes[4].remove('dress')
boxes[6].append('dress')
boxes[4].append('mirror')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")