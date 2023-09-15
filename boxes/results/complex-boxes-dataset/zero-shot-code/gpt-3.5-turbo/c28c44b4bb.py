box_0 = ['watch', 'dolphin', 'shoes', 'bus', 'scissors']
box_1 = ['key']
box_2 = ['bicycle', 'bag', 'button', 'guitar', 'belt']
box_3 = ['game', 'sun', 'pants', 'freezer', 'mountain']
box_4 = ['lipstick', 'horn', 'table']
box_5 = ['spoon', 'crown', 'comb', 'pillow']
box_6 = ['violin']
box_7 = []
box_8 = ['blender']
box_9 = ['apple', 'helmet', 'shorts', 'car']
box_10 = ['shampoo']
box_11 = ['planet']
box_12 = []
box_13 = ['towel']
box_14 = ['octopus', 'ocean', 'puzzle', 'wig']

def print_box(box_index, box_items):
    print(f"Box {box_index}: {box_items}")

# Move the towel from Box 13 to Box 10
box_10.append(box_13.pop(box_13.index('towel')))

# Put the beach and the bell and the toy into Box 13
box_13.extend(['beach', 'bell', 'toy'])

# Put the guitar and the key into Box 5
box_5.extend(['guitar', 'key'])

# Replace the mountain and the sun with the scissors and the headphone in Box 3
box_3.remove('mountain')
box_3.remove('sun')
box_3.extend(['scissors', 'headphone'])

# Remove the puzzle from Box 14
box_14.remove('puzzle')

# Replace the helmet and the shorts with the shampoo and the necklace in Box 9
box_9.remove('helmet')
box_9.remove('shorts')
box_9.extend(['shampoo', 'necklace'])

# Put the makeup and the bicycle and the submarine into Box 11
box_11.extend(['makeup', 'bicycle', 'submarine'])

# Remove the necklace and the apple and the car from Box 9
box_9.remove('necklace')
box_9.remove('apple')
box_9.remove('car')

# Remove the towel from Box 10
box_10.remove('towel')

# Swap the blender in Box 8 with the shampoo in Box 9
box_8, box_9 = box_9, box_8

# Replace the shampoo with the necklace in Box 10
box_10.remove('shampoo')
box_10.append('necklace')

# Put the glove into Box 0
box_0.append('glove')

# Put the phone into Box 12
box_12.append('phone')

# Remove the submarine from Box 11
box_11.remove('submarine')

# Move the shoes and the scissors from Box 0 to Box 9
box_9.extend(['shoes', 'scissors'])
box_0.remove('shoes')
box_0.remove('scissors')

# Remove the violin from Box 6
box_6.remove('violin')

# Swap the horn in Box 4 with the scissors in Box 3
box_3.append('horn')
box_4.append('scissors')
box_3.remove('scissors')
box_4.remove('horn')

# Replace the horn and the game and the pants with the shirt and the train and the glasses in Box 3
box_3.remove('horn')
box_3.remove('game')
box_3.remove('pants')
box_3.extend(['shirt', 'train', 'glasses'])

# Remove the phone from Box 12
box_12.remove('phone')

# Put the cow and the usb into Box 10
box_10.extend(['cow', 'usb'])

# Replace the guitar and the spoon and the pillow with the bird and the towel and the oven in Box 5
box_5.remove('guitar')
box_5.remove('spoon')
box_5.remove('pillow')
box_5.extend(['bird', 'towel', 'oven'])

# Swap the scissors in Box 9 with the bicycle in Box 11
box_9.append('bicycle')
box_11.append('scissors')
box_9.remove('scissors')
box_11.remove('bicycle')

# Print the contents of each box
print_box(0, box_0)
print_box(1, box_1)
print_box(2, box_2)
print_box(3, box_3)
print_box(4, box_4)
print_box(5, box_5)
print_box(6, box_6)
print_box(7, box_7)
print_box(8, box_8)
print_box(9, box_9)
print_box(10, box_10)
print_box(11, box_11)
print_box(12, box_12)
print_box(13, box_13)
print_box(14, box_14)