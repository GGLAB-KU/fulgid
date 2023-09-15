box_0 = ['chair']
box_1 = []
box_2 = ['doll', 'bicycle', 'violin', 'button']
box_3 = ['headphone', 'ring', 'shampoo', 'oven', 'shoes']
box_4 = ['submarine', 'shoe', 'lightning', 'octopus']
box_5 = ['dice', 'sandals', 'rain', 'comb']
box_6 = ['pot']
box_7 = ['meteor']
box_8 = ['truck']
box_9 = ['brush', 'cat', 'car', 'mirror', 'guitar']
box_10 = []
box_11 = ['swimsuit', 'butterfly']
box_12 = ['toaster', 'lock']
box_13 = ['polish', 'spoon', 'clock', 'keyboard', 'console']
box_14 = ['earring', 'pan', 'candle', 'zipper']

# Move the pot from Box 6 to Box 2
box_2.append(box_6.pop(0))

# Swap the shoe in Box 4 with the keyboard in Box 13
box_4[box_4.index('shoe')], box_13[box_13.index('keyboard')] = box_13[box_13.index('keyboard')], box_4[box_4.index('shoe')]

# Replace the lock and the toaster with the cow and the soap in Box 12
box_12[box_12.index('lock')] = 'cow'
box_12[box_12.index('toaster')] = 'soap'

# Remove the chair from Box 0
box_0.pop(0)

# Replace the car with the plane in Box 9
box_9[box_9.index('car')] = 'plane'

# Put the razor into Box 13
box_13.append('razor')

# Put the skirt into Box 1
box_1.append('skirt')

# Move the pot and the violin and the doll from Box 2 to Box 0
box_0.extend([box_2.pop(box_2.index('pot'))])
box_0.extend([box_2.pop(box_2.index('violin'))])
box_0.extend([box_2.pop(box_2.index('doll'))])

# Move the sandals from Box 5 to Box 8
box_8.extend([box_5.pop(box_5.index('sandals'))])

# Move the skirt from Box 1 to Box 8
box_8.extend([box_1.pop(box_1.index('skirt'))])

# Move the candle and the zipper from Box 14 to Box 7
box_7.extend([box_14.pop(box_14.index('candle'))])
box_7.extend([box_14.pop(box_14.index('zipper'))])

# Move the butterfly and the swimsuit from Box 11 to Box 7
box_7.extend([box_11.pop(box_11.index('butterfly'))])
box_7.extend([box_11.pop(box_11.index('swimsuit'))])

# Put the lion and the frame into Box 1
box_1.extend(['lion', 'frame'])

# Replace the pan with the zipper in Box 14
box_14[box_14.index('pan')] = 'zipper'

# Move the cow and the soap from Box 12 to Box 2
box_2.extend([box_12.pop(box_12.index('cow'))])
box_2.extend([box_12.pop(box_12.index('soap'))])

# Remove the lightning from Box 4
box_4.remove('lightning')

# Remove the violin from Box 0
box_0.remove('violin')

# Move the octopus from Box 4 to Box 7
box_7.extend([box_4.pop(box_4.index('octopus'))])

# Swap the submarine in Box 4 with the earring in Box 14
box_4[box_4.index('submarine')], box_14[box_14.index('earring')] = box_14[box_14.index('earring')], box_4[box_4.index('submarine')]

# Swap the pot in Box 0 with the console in Box 13
box_0[box_0.index('pot')], box_13[box_13.index('console')] = box_13[box_13.index('console')], box_0[box_0.index('pot')]

# Remove the spoon and the shoe and the pot from Box 13
box_13.remove('spoon')
box_13.remove('shoe')
box_13.remove('pot')

# Move the swimsuit and the meteor from Box 7 to Box 14
box_14.extend([box_7.pop(box_7.index('swimsuit'))])
box_14.extend([box_7.pop(box_7.index('meteor'))])

# Print the contents of each box
for i, box in enumerate([box_0, box_1, box_2, box_3, box_4, box_5, box_6, box_7, box_8, box_9, box_10, box_11, box_12, box_13, box_14]):
    print(f"Box {i}: {box}")