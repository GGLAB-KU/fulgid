# Initial state of boxes
boxes = {
    0: ['moon'],
    1: ['umbrella', 'fork', 'belt', 'pan'],
    2: ['seaweed', 'mixer'],
    3: ['soap', 'rock', 'whistle', 'leaf', 'necklace'],
    4: ['wire', 'usb'],
    5: ['wallet', 'piano', 'ocean']
}

# Move the necklace from Box 3 to Box 5.
boxes[3].remove('necklace')
boxes[5].append('necklace')

# Move the moon from Box 0 to Box 4.
boxes[0].remove('moon')
boxes[4].append('moon')

# Remove the seaweed and the mixer from Box 2.
boxes[2].remove('seaweed')
boxes[2].remove('mixer')

# Replace the usb and the moon with the toaster and the boot in Box 4.
boxes[4].remove('usb')
boxes[4].remove('moon')
boxes[4].append('toaster')
boxes[4].append('boot')

# Replace the umbrella with the doll in Box 1.
boxes[1].remove('umbrella')
boxes[1].append('doll')

# Remove the wire and the boot from Box 4.
boxes[4].remove('wire')
boxes[4].remove('boot')

# Put the harmonica into Box 5.
boxes[5].append('harmonica')

# Move the toaster from Box 4 to Box 0.
boxes[4].remove('toaster')
boxes[0].append('toaster')

# Put the sun and the glasses and the lock into Box 4.
items_to_add = ['sun', 'glasses', 'lock']
for item in items_to_add:
    boxes[4].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")