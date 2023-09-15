box_0 = ['razor', 'river', 'sun', 'scarf']
box_1 = ['sock', 'pants', 'grass', 'leaf']
box_2 = ['candle', 'shampoo', 'cup', 'blanket']
box_3 = []
box_4 = ['scissors', 'paint', 'guitar', 'soap']
box_5 = ['train', 'boat', 'tape', 'controller', 'flower']
box_6 = []
box_7 = ['freezer', 'planet']
box_8 = ['toaster', 'dog', 'truck', 'butterfly']
box_9 = []
box_10 = []
box_11 = ['lock']
box_12 = []
box_13 = ['car', 'glove', 'thunder', 'skirt']

def print_box(box_index, box_items):
    print(f"Box {box_index}: {box_items}")

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

# Move the butterfly from Box 8 to Box 0
box_0.append(box_8.pop(box_8.index('butterfly')))

# Swap the toaster in Box 8 with the thunder in Box 13
box_8.append(box_13.pop(box_13.index('thunder')))
box_13.append(box_8.pop(box_8.index('toaster')))

# Replace the tape and the boat and the flower with the scissors and the card and the belt in Box 5
box_5.remove('tape')
box_5.remove('boat')
box_5.remove('flower')
box_5.append('scissors')
box_5.append('card')
box_5.append('belt')

# Put the makeup and the microscope and the shark into Box 11
box_11.append('makeup')
box_11.append('microscope')
box_11.append('shark')

# Replace the guitar and the soap and the scissors with the plate and the vase and the sock in Box 4
box_4.remove('guitar')
box_4.remove('soap')
box_4.remove('scissors')
box_4.append('plate')
box_4.append('vase')
box_4.append('sock')

# Replace the controller with the book in Box 5
box_5.remove('controller')
box_5.append('book')

# Remove the toaster and the skirt from Box 13
box_13.remove('toaster')
box_13.remove('skirt')

# Replace the glove with the note in Box 13
box_13.remove('glove')
box_13.append('note')

# Remove the shark and the microscope from Box 11
box_11.remove('shark')
box_11.remove('microscope')

# Swap the planet in Box 7 with the shampoo in Box 2
box_7.append(box_2.pop(box_2.index('planet')))
box_2.append(box_7.pop(box_7.index('shampoo')))

# Put the swimsuit and the meteor and the toy into Box 9
box_9.append('swimsuit')
box_9.append('meteor')
box_9.append('toy')

# Put the belt and the thread into Box 11
box_11.append('belt')
box_11.append('thread')

# Put the fridge and the mixer and the button into Box 1
box_1.append('fridge')
box_1.append('mixer')
box_1.append('button')

# Move the pants and the sock from Box 1 to Box 11
box_11.append(box_1.pop(box_1.index('pants')))
box_11.append(box_1.pop(box_1.index('sock')))

# Remove the shampoo from Box 7
box_7.remove('shampoo')

# Replace the belt and the card and the train with the keyboard and the oven and the brush in Box 5
box_5.remove('belt')
box_5.remove('card')
box_5.remove('train')
box_5.append('keyboard')
box_5.append('oven')
box_5.append('brush')

# Put the rocket into Box 4
box_4.append('rocket')

# Move the freezer from Box 7 to Box 0
box_0.append(box_7.pop(box_7.index('freezer')))

# Swap the blanket in Box 2 with the thunder in Box 8
box_2.append(box_8.pop(box_8.index('blanket')))
box_8.append(box_2.pop(box_2.index('thunder')))

# Move the cup and the candle from Box 2 to Box 5
box_5.append(box_2.pop(box_2.index('cup')))
box_5.append(box_2.pop(box_2.index('candle')))

# Remove the planet and the thunder from Box 2
box_2.remove('planet')
box_2.remove('thunder')

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