# Initial state of boxes
boxes = {
    0: ['headphone', 'clock', 'ring', 'horse', 'cup'],
    1: ['brush'],
    2: ['fork'],
    3: ['shoe'],
    4: ['doll', 'branch', 'bell']
}

# Replace the shoe with the towel in Box 3.
boxes[3].remove('shoe')
boxes[3].append('towel')

# Empty Box 0.
boxes[0] = []

# Replace the brush with the car in Box 1.
boxes[1].remove('brush')
boxes[1].append('car')

# Swap the doll in Box 4 with the fork in Box 2.
boxes[4].remove('doll')
boxes[2].remove('fork')
boxes[4].append('fork')
boxes[2].append('doll')

# Swap the fork in Box 4 with the doll in Box 2.
boxes[4].remove('fork')
boxes[2].remove('doll')
boxes[4].append('doll')
boxes[2].append('fork')

# Replace the car with the mirror in Box 1.
boxes[1].remove('car')
boxes[1].append('mirror')

# Replace the towel with the puzzle in Box 3.
boxes[3].remove('towel')
boxes[3].append('puzzle')

# Move the puzzle from Box 3 to Box 1.
boxes[3].remove('puzzle')
boxes[1].append('puzzle')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")