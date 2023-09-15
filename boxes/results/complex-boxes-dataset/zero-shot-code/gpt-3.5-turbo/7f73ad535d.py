box_0 = ['moon']
box_1 = ['umbrella', 'fork', 'belt', 'pan']
box_2 = ['seaweed', 'mixer']
box_3 = ['soap', 'rock', 'whistle', 'leaf', 'necklace']
box_4 = ['wire', 'usb']
box_5 = ['wallet', 'piano', 'ocean']

# Move the necklace from Box 3 to Box 5
box_5.append(box_3.pop(box_3.index('necklace')))

# Move the moon from Box 0 to Box 4
box_4.append(box_0.pop())

# Remove the seaweed and the mixer from Box 2
box_2.remove('seaweed')
box_2.remove('mixer')

# Replace the usb and the moon with the toaster and the boot in Box 4
box_4.remove('usb')
box_4.append('toaster')
box_4.remove('moon')
box_4.append('boot')

# Replace the umbrella with the doll in Box 1
box_1.remove('umbrella')
box_1.append('doll')

# Remove the wire and the boot from Box 4
box_4.remove('wire')
box_4.remove('boot')

# Put the harmonica into Box 5
box_5.append('harmonica')

# Move the toaster from Box 4 to Box 0
box_0.append(box_4.pop(box_4.index('toaster')))

# Put the sun and the glasses and the lock into Box 4
box_4.append('sun')
box_4.append('glasses')
box_4.append('lock')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)