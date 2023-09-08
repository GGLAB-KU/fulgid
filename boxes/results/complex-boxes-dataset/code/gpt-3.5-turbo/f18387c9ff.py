# Initial state of boxes
boxes = {
    0: ['skirt', 'desert', 'phone', 'flower'],
    1: ['truck', 'sandals', 'telescope', 'zipper'],
    2: ['pot', 'razor', 'blender', 'jacket', 'towel'],
    3: ['helmet', 'camera', 'scarf'],
    4: ['perfume'],
    5: ['usb', 'lamp']
}

# Remove the scarf from Box 3.
boxes[3].remove('scarf')

# Replace the usb and the lamp with the guitar and the cat in Box 5.
boxes[5].remove('usb')
boxes[5].remove('lamp')
boxes[5].append('guitar')
boxes[5].append('cat')

# Move the guitar from Box 5 to Box 3.
boxes[5].remove('guitar')
boxes[3].append('guitar')

# Move the guitar and the camera from Box 3 to Box 4.
boxes[3].remove('guitar')
boxes[3].remove('camera')
boxes[4].append('guitar')
boxes[4].append('camera')

# Remove the telescope and the sandals and the zipper from Box 1.
boxes[1].remove('telescope')
boxes[1].remove('sandals')
boxes[1].remove('zipper')

# Move the skirt from Box 0 to Box 5.
boxes[0].remove('skirt')
boxes[5].append('skirt')

# Remove the cat and the skirt from Box 5.
boxes[5].remove('cat')
boxes[5].remove('skirt')

# Replace the desert with the toaster in Box 0.
boxes[0].remove('desert')
boxes[0].append('toaster')

# Swap the razor in Box 2 with the truck in Box 1.
boxes[2].remove('razor')
boxes[1].remove('truck')
boxes[2].append('truck')
boxes[1].append('razor')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")