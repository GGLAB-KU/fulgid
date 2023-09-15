box_0 = ['dolphin']
box_1 = ['jungle']
box_2 = ['makeup', 'tape', 'submarine', 'blender']
box_3 = ['bear']
box_4 = ['chair', 'leaf']
box_5 = ['speaker']
box_6 = ['bowl', 'elephant', 'towel', 'coin']
box_7 = ['book', 'spoon', 'shoe', 'magnet', 'forest']
box_8 = ['dice', 'necklace', 'puzzle', 'watch']
box_9 = ['moon', 'button', 'ocean']
box_10 = ['key', 'storm']
box_11 = ['zipper']

# Remove the jungle from Box 1
box_1.remove('jungle')

# Put the glasses into Box 7
box_7.append('glasses')

# Put the mirror and the watch and the lamp into Box 3
box_3.extend(['mirror', 'watch', 'lamp'])

# Move the dolphin from Box 0 to Box 4
box_4.append(box_0.pop())

# Put the polish and the star and the ship into Box 6
box_6.extend(['polish', 'star', 'ship'])

# Swap the magnet in Box 7 with the necklace in Box 8
box_7.remove('magnet')
box_8.remove('necklace')
box_7.append('necklace')
box_8.append('magnet')

# Move the magnet and the watch and the puzzle from Box 8 to Box 3
box_3.extend([box_8.pop(), box_8.pop(), box_8.pop()])

# Swap the moon in Box 9 with the speaker in Box 5
box_9.remove('moon')
box_5.remove('speaker')
box_9.append('speaker')
box_5.append('moon')

# Swap the moon in Box 5 with the book in Box 7
box_5.remove('moon')
box_7.remove('book')
box_5.append('book')
box_7.append('moon')

# Swap the leaf in Box 4 with the makeup in Box 2
box_4.remove('leaf')
box_2.remove('makeup')
box_4.append('makeup')
box_2.append('leaf')

# Replace the chair and the makeup with the shelf and the comet in Box 4
box_4.remove('chair')
box_4.remove('makeup')
box_4.append('shelf')
box_4.append('comet')

# Move the tape from Box 2 to Box 9
box_2.remove('tape')
box_9.append('tape')

# Move the dice from Box 8 to Box 2
box_8.remove('dice')
box_2.append('dice')

# Swap the tape in Box 9 with the book in Box 5
box_9.remove('tape')
box_5.remove('book')
box_9.append('book')
box_5.append('tape')

# Move the key and the storm from Box 10 to Box 7
box_10.remove('key')
box_10.remove('storm')
box_7.extend(['key', 'storm'])

# Move the button and the book from Box 9 to Box 4
box_9.remove('button')
box_9.remove('book')
box_4.extend(['button', 'book'])

# Replace the shelf with the butterfly in Box 4
box_4.remove('shelf')
box_4.append('butterfly')

# Remove the moon and the glasses and the key from Box 7
box_7.remove('moon')
box_7.remove('glasses')
box_7.remove('key')

# Print the contents of each box
for i, box in enumerate([box_0, box_1, box_2, box_3, box_4, box_5, box_6, box_7, box_8, box_9, box_10, box_11]):
    print(f"Box {i}: {box}")