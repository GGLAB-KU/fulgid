box_0 = []
box_1 = ['mask', 'river', 'tie']
box_2 = ['lipstick', 'shark', 'dolphin', 'fish', 'rocket']
box_3 = ['octopus', 'pillow', 'perfume', 'controller', 'bag']
box_4 = ['phone', 'horse']
box_5 = ['makeup', 'harmonica', 'toothbrush']
box_6 = ['whistle', 'wig', 'desert', 'rock', 'chair']
box_7 = ['mixer', 'puzzle', 'moon', 'scarf']
box_8 = ['crown', 'glasses', 'flute']
box_9 = ['zipper']
box_10 = ['cloud', 'snow', 'guitar', 'bear']
box_11 = ['planet', 'shirt', 'pan', 'fridge']
box_12 = ['basket', 'umbrella', 'truck']

def print_box(box_name, box):
    print(f"Box {box_name}: {box}")

# Remove the snow and the guitar and the cloud from Box 10
box_10.remove('snow')
box_10.remove('guitar')
box_10.remove('cloud')

# Move the crown and the flute and the glasses from Box 8 to Box 1
box_1.extend(box_8)
box_8.clear()

# Put the bowl and the desert into Box 3
box_3.append('bowl')
box_3.append('desert')

# Empty Box 5
box_5.clear()

# Remove the whistle and the wig from Box 6
box_6.remove('whistle')
box_6.remove('wig')

# Replace the fish and the rocket with the dress and the guitar in Box 2
box_2.remove('fish')
box_2.remove('rocket')
box_2.append('dress')
box_2.append('guitar')

# Swap the bear in Box 10 with the guitar in Box 2
box_10.remove('bear')
box_2.remove('guitar')
box_10.append('guitar')
box_2.append('bear')

# Move the planet from Box 11 to Box 12
box_11.remove('planet')
box_12.append('planet')

# Move the chair from Box 6 to Box 12
box_6.remove('chair')
box_12.append('chair')

# Swap the shirt in Box 11 with the phone in Box 4
box_11.remove('shirt')
box_4.remove('phone')
box_11.append('phone')
box_4.append('shirt')

# Move the zipper from Box 9 to Box 5
box_9.remove('zipper')
box_5.append('zipper')

# Empty Box 1
box_1.clear()

# Put the frame and the vase into Box 5
box_5.append('frame')
box_5.append('vase')

# Remove the pillow and the bag from Box 3
box_3.remove('pillow')
box_3.remove('bag')

# Put the microwave into Box 8
box_8.append('microwave')

# Move the bear and the dress from Box 2 to Box 8
box_2.remove('bear')
box_2.remove('dress')
box_8.append('bear')
box_8.append('dress')

# Swap the dolphin in Box 2 with the zipper in Box 5
box_2.remove('dolphin')
box_5.remove('zipper')
box_2.append('zipper')
box_5.append('dolphin')

# Swap the rock in Box 6 with the guitar in Box 10
box_6.remove('rock')
box_10.remove('guitar')
box_6.append('guitar')
box_10.append('rock')

# Move the rock from Box 10 to Box 3
box_10.remove('rock')
box_3.append('rock')

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