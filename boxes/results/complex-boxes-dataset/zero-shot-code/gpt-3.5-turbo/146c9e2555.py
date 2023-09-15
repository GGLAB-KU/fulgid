box_0 = ['car', 'shirt', 'storm']
box_1 = ['fish', 'grinder', 'river', 'game', 'microwave']
box_2 = []
box_3 = ['wig', 'beach', 'jacket']
box_4 = ['console', 'bracelet', 'scarf', 'helmet', 'dolphin']
box_5 = ['chair']
box_6 = ['dress', 'elephant', 'desert', 'headphone', 'book']
box_7 = ['magnet', 'comet']
box_8 = ['crown', 'sculpture', 'hat']
box_9 = ['brush', 'watch']
box_10 = ['starfish', 'bus', 'gloves']
box_11 = ['umbrella', 'battery', 'sock']
box_12 = ['usb']
box_13 = ['doll']

# Replace the battery with the plane in Box 11
box_11.remove('battery')
box_11.append('plane')

# Swap the bus in Box 10 with the microwave in Box 1
box_10.remove('bus')
box_1.remove('microwave')
box_10.append('microwave')
box_1.append('bus')

# Move the sock from Box 11 to Box 4
box_11.remove('sock')
box_4.append('sock')

# Put the scissors and the coat and the planet into Box 4
box_4.extend(['scissors', 'coat', 'planet'])

# Replace the hat and the sculpture with the boot and the lion in Box 8
box_8.remove('hat')
box_8.remove('sculpture')
box_8.append('boot')
box_8.append('lion')

# Put the flower and the sun into Box 4
box_4.extend(['flower', 'sun'])

# Move the umbrella from Box 11 to Box 5
box_11.remove('umbrella')
box_5.append('umbrella')

# Swap the usb in Box 12 with the car in Box 0
box_12.remove('usb')
box_0.remove('car')
box_12.append('car')
box_0.append('usb')

# Replace the elephant and the book and the desert with the motorcycle and the keyboard and the sandals in Box 6
box_6.remove('elephant')
box_6.remove('book')
box_6.remove('desert')
box_6.append('motorcycle')
box_6.append('keyboard')
box_6.append('sandals')

# Put the train into Box 6
box_6.append('train')

# Put the dolphin and the tiger into Box 9
box_9.extend(['dolphin', 'tiger'])

# Replace the boot and the lion with the wire and the shirt in Box 8
box_8.remove('boot')
box_8.remove('lion')
box_8.append('wire')
box_8.append('shirt')

# Replace the starfish and the microwave and the gloves with the swimsuit and the console and the rocket in Box 10
box_10.remove('starfish')
box_10.remove('microwave')
box_10.remove('gloves')
box_10.append('swimsuit')
box_10.append('console')
box_10.append('rocket')

# Move the wig and the beach from Box 3 to Box 9
box_3.remove('wig')
box_3.remove('beach')
box_9.extend(['wig', 'beach'])

# Replace the umbrella and the chair with the toaster and the ship in Box 5
box_5.remove('umbrella')
box_5.remove('chair')
box_5.append('toaster')
box_5.append('ship')

# Replace the magnet and the comet with the apple and the grass in Box 7
box_7.remove('magnet')
box_7.remove('comet')
box_7.append('apple')
box_7.append('grass')

# Replace the shirt and the crown and the wire with the cup and the doll and the seaweed in Box 8
box_8.remove('shirt')
box_8.remove('crown')
box_8.remove('wire')
box_8.append('cup')
box_8.append('doll')
box_8.append('seaweed')

# Move the car from Box 12 to Box 6
box_12.remove('car')
box_6.append('car')

# Move the rocket and the swimsuit and the console from Box 10 to Box 6
box_10.remove('rocket')
box_10.remove('swimsuit')
box_10.remove('console')
box_6.extend(['rocket', 'swimsuit', 'console'])

# Replace the ship and the toaster with the cat and the toy in Box 5
box_5.remove('ship')
box_5.remove('toaster')
box_5.append('cat')
box_5.append('toy')

# Swap the apple in Box 7 with the doll in Box 13
box_7.remove('apple')
box_13.remove('doll')
box_7.append('doll')

# Print the contents of each box
for i, box in enumerate([box_0, box_1, box_2, box_3, box_4, box_5, box_6, box_7, box_8, box_9, box_10, box_11, box_12, box_13]):
    print(f"Box {i}: {box}")