box_0 = ['thread', 'forest', 'zipper', 'toaster', 'soap']
box_1 = ['pants', 'bracelet', 'keyboard', 'table']
box_2 = ['bear', 'submarine', 'coat']
box_3 = ['beach', 'sock', 'sun']
box_4 = ['ring', 'mixer', 'key', 'brush', 'glasses']
box_5 = ['mask', 'car', 'dog', 'scissors', 'fish']
box_6 = []
box_7 = ['sculpture', 'elephant', 'helmet']
box_8 = ['oven', 'belt', 'seaweed', 'harmonica', 'pan']
box_9 = ['clock', 'cow', 'hat', 'phone', 'wallet']
box_10 = ['pot', 'charger', 'book', 'perfume']
box_11 = ['vase', 'usb', 'polish', 'blender', 'button']
box_12 = ['doll', 'planet', 'tree', 'cat']

# Put the swimsuit and the sun and the lamp into Box 2
box_2.extend(['swimsuit', 'sun', 'lamp'])

# Remove the sculpture and the helmet from Box 7
box_7.remove('sculpture')
box_7.remove('helmet')

# Replace the table with the cup in Box 1
box_1.remove('table')
box_1.append('cup')

# Move the elephant from Box 7 to Box 9
elephant = box_7.pop(1)
box_9.append(elephant)

# Replace the usb and the polish with the spoon and the shoe in Box 11
box_11.remove('usb')
box_11.remove('polish')
box_11.extend(['spoon', 'shoe'])

# Move the elephant and the wallet and the phone from Box 9 to Box 1
elephant = box_9.pop(1)
wallet = box_9.pop(2)
phone = box_9.pop(2)
box_1.extend([elephant, wallet, phone])

# Swap the cup in Box 1 with the coat in Box 2
cup = box_1.pop(2)
coat = box_2.pop(2)
box_1.append(coat)
box_2.append(cup)

# Put the flower and the rain and the whistle into Box 6
box_6.extend(['flower', 'rain', 'whistle'])

# Put the scissors and the freezer into Box 7
box_7.extend(['scissors', 'freezer'])

# Move the scissors and the freezer from Box 7 to Box 5
scissors = box_7.pop(0)
freezer = box_7.pop(0)
box_5.extend([scissors, freezer])

# Remove the key and the ring from Box 4
box_4.remove('key')
box_4.remove('ring')

# Swap the book in Box 10 with the glasses in Box 4
book = box_10.pop(2)
glasses = box_4.pop(3)
box_10.append(glasses)
box_4.append(book)

# Swap the bear in Box 2 with the toaster in Box 0
bear = box_2.pop(0)
toaster = box_0.pop(3)
box_2.append(toaster)
box_0.append(bear)

# Move the soap and the forest and the bear from Box 0 to Box 1
soap = box_0.pop(3)
forest = box_0.pop(2)
bear = box_0.pop(1)
box_1.extend([soap, forest, bear])

# Move the pan and the belt from Box 8 to Box 6
pan = box_8.pop(4)
belt = box_8.pop(1)
box_6.extend([pan, belt])

# Swap the pants in Box 1 with the doll in Box 12
pants = box_1.pop(0)
doll = box_12.pop(0)
box_1.append(doll)
box_12.append(pants)

# Replace the wallet with the whistle in Box 1
box_1.remove('wallet')
box_1.append('whistle')

# Move the sock and the beach from Box 3 to Box 0
sock = box_3.pop(1)
beach = box_3.pop(0)
box_0.extend([sock, beach])

# Move the book and the mixer and the brush from Box 4 to Box 9
book = box_4.pop(2)
mixer = box_4.pop(1)
brush = box_4.pop(1)
box_9.extend([book, mixer, brush])

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)
print("Box 8:", box_8)
print("Box 9:", box_9)
print("Box 10:", box_10)
print("Box 11:", box_11)
print("Box 12:", box_12)