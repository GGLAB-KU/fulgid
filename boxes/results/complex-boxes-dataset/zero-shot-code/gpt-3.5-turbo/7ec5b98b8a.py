box_0 = ['apple']
box_1 = ['octopus']
box_2 = ['makeup', 'bowl', 'camera']
box_3 = ['comb', 'shorts', 'grinder']
box_4 = ['coral', 'leaf', 'shoe', 'coat']
box_5 = ['motorcycle', 'pen', 'usb']
box_6 = ['whistle', 'pants', 'bus', 'freezer']
box_7 = ['lipstick', 'bird']
box_8 = []
box_9 = ['boot']
box_10 = []
box_11 = ['vase', 'moon', 'paint']
box_12 = ['fridge', 'candle', 'rain']
box_13 = ['dog', 'drum', 'cup', 'car']
box_14 = ['microwave', 'chair', 'horse', 'hat', 'dress']

# Move the motorcycle and the usb and the pen from Box 5 to Box 7
box_7.extend([box_5.pop(0), box_5.pop(0), box_5.pop(0)])

# Remove the drum and the car and the dog from Box 13
box_13.remove('drum')
box_13.remove('car')
box_13.remove('dog')

# Remove the octopus from Box 1
box_1.remove('octopus')

# Swap the cup in Box 13 with the apple in Box 0
box_0[0], box_13[2] = box_13[2], box_0[0]

# Move the comb and the shorts from Box 3 to Box 11
box_11.extend([box_3.pop(0), box_3.pop(0)])

# Remove the grinder from Box 3
box_3.remove('grinder')

# Put the harmonica and the river and the thread into Box 7
box_7.extend(['harmonica', 'river', 'thread'])

# Move the pants from Box 6 to Box 4
box_4.append(box_6.pop(1))

# Swap the apple in Box 13 with the cup in Box 0
box_0[0], box_13[2] = box_13[2], box_0[0]

# Move the shorts and the paint from Box 11 to Box 10
box_10.extend([box_11.pop(1), box_11.pop(1)])

# Replace the apple with the puzzle in Box 0
box_0[0] = 'puzzle'

# Move the leaf and the pants from Box 4 to Box 0
box_0.extend([box_4.pop(1), box_4.pop(1)])

# Move the comb and the moon and the vase from Box 11 to Box 13
box_13.extend([box_11.pop(0), box_11.pop(0), box_11.pop(0)])

# Move the moon from Box 13 to Box 12
box_12.append(box_13.pop(2))

# Replace the chair and the hat with the tie and the bicycle in Box 14
box_14.remove('chair')
box_14.remove('hat')
box_14.extend(['tie', 'bicycle'])

# Replace the leaf and the puzzle with the crown and the seaweed in Box 0
box_0.remove('leaf')
box_0.remove('puzzle')
box_0.extend(['crown', 'seaweed'])

# Remove the thread from Box 7
box_7.remove('thread')

# Move the boot from Box 9 to Box 4
box_4.append(box_9.pop(0))

# Remove the shoe and the coral and the coat from Box 4
box_4.remove('shoe')
box_4.remove('coral')
box_4.remove('coat')

# Remove the bicycle from Box 14
box_14.remove('bicycle')

# Remove the river and the motorcycle from Box 7
box_7.remove('river')
box_7.remove('motorcycle')

# Remove the paint and the shorts from Box 10
box_10.remove('paint')
box_10.remove('shorts')

# Print the contents of each box
for i, box in enumerate([box_0, box_1, box_2, box_3, box_4, box_5, box_6, box_7, box_8, box_9, box_10, box_11, box_12, box_13, box_14]):
    print(f"Box {i}: {box}")