# Initial state of boxes
boxes = {
    0: ['flower', 'dolphin'],
    1: ['rocket', 'dice', 'shorts', 'shoe'],
    2: ['wire', 'console', 'magnet', 'bus'],
    3: ['fridge'],
    4: ['bear', 'microwave', 'storm', 'ocean', 'glasses'],
    5: ['starfish', 'fish', 'sun', 'fork'],
    6: ['scissors', 'makeup'],
    7: ['toothbrush', 'mirror', 'piano', 'planet', 'horn'],
    8: [],
    9: ['rock', 'whistle', 'frame', 'oven', 'skirt'],
    10: [],
    11: ['belt', 'wig', 'brush', 'car'],
    12: ['jungle', 'headphone']
}

# Swap the planet in Box 7 with the flower in Box 0.
boxes[0].remove('flower')
boxes[7].remove('planet')
boxes[0].append('planet')
boxes[7].append('flower')

# Swap the fridge in Box 3 with the horn in Box 7.
boxes[3].remove('fridge')
boxes[7].remove('horn')
boxes[3].append('horn')
boxes[7].append('fridge')

# Move the horn from Box 3 to Box 5.
boxes[3].remove('horn')
boxes[5].append('horn')

# Move the fork from Box 5 to Box 7.
boxes[5].remove('fork')
boxes[7].append('fork')

# Replace the skirt and the whistle and the rock with the lion and the rain and the tiger in Box 9.
boxes[9].remove('skirt')
boxes[9].remove('whistle')
boxes[9].remove('rock')
boxes[9].append('lion')
boxes[9].append('rain')
boxes[9].append('tiger')

# Put the controller and the storm into Box 5.
boxes[5].append('controller')
boxes[5].append('storm')

# Remove the planet and the dolphin from Box 0.
boxes[0].remove('planet')
boxes[0].remove('dolphin')

# Put the dolphin into Box 2.
boxes[2].append('dolphin')

# Empty Box 5.
boxes[5] = []

# Empty Box 11.
boxes[11] = []

# Swap the shorts in Box 1 with the scissors in Box 6.
boxes[1].remove('shorts')
boxes[6].remove('scissors')
boxes[1].append('scissors')
boxes[6].append('shorts')

# Move the makeup from Box 6 to Box 5.
boxes[6].remove('makeup')
boxes[5].append('makeup')

# Put the sun and the desert into Box 11.
boxes[11].append('sun')
boxes[11].append('desert')

# Remove the glasses from Box 4.
boxes[4].remove('glasses')

# Remove the makeup from Box 5.
boxes[5].remove('makeup')

# Put the moon into Box 10.
boxes[10].append('moon')

# Replace the headphone with the clock in Box 12.
boxes[12].remove('headphone')
boxes[12].append('clock')

# Put the fish into Box 10.
boxes[10].append('fish')

# Move the desert and the sun from Box 11 to Box 7.
boxes[11].remove('desert')
boxes[11].remove('sun')
boxes[7].append('desert')
boxes[7].append('sun')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")