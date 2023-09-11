# Initial state of boxes
boxes = {
    0: ['crown', 'makeup', 'microscope'],
    1: [],
    2: ['pan', 'skirt', 'branch'],
    3: ['chair', 'dice', 'toothbrush']
}

# Replace the pan and the branch and the skirt with the elephant and the brush and the toothbrush in Box 2.
boxes[2].remove('pan')
boxes[2].remove('branch')
boxes[2].remove('skirt')
boxes[2].append('elephant')
boxes[2].append('brush')
boxes[2].append('toothbrush')

# Swap the crown in Box 0 with the chair in Box 3.
boxes[0].remove('crown')
boxes[3].remove('chair')
boxes[0].append('chair')
boxes[3].append('crown')

# Remove the brush and the elephant and the toothbrush from Box 2.
boxes[2].remove('brush')
boxes[2].remove('elephant')
boxes[2].remove('toothbrush')

# Remove the crown and the toothbrush and the dice from Box 3.
boxes[3].remove('crown')
boxes[3].remove('toothbrush')
boxes[3].remove('dice')

# Replace the makeup and the microscope and the chair with the laptop and the pan and the ocean in Box 0.
boxes[0].remove('makeup')
boxes[0].remove('microscope')
boxes[0].remove('chair')
boxes[0].append('laptop')
boxes[0].append('pan')
boxes[0].append('ocean')

# Move the pan from Box 0 to Box 1.
boxes[0].remove('pan')
boxes[1].append('pan')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")