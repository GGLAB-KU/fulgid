box_0 = ['belt', 'dog']
box_1 = ['harmonica']
box_2 = ['rocket', 'glove', 'mask', 'controller']
box_3 = ['bracelet']
box_4 = ['guitar', 'mirror']
box_5 = ['candle', 'shirt', 'blanket', 'paint']
box_6 = []
box_7 = ['lamp', 'headphone']
box_8 = ['river', 'umbrella', 'brush']

print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)
print("Box 8:", box_8)

# Move the bracelet from Box 3 to Box 4
box_4.append(box_3.pop(0))

# Replace the glove and the rocket with the button and the planet in Box 2
box_2.remove('glove')
box_2.remove('rocket')
box_2.extend(['button', 'planet'])

# Move the harmonica from Box 1 to Box 5
box_5.append(box_1.pop(0))

# Move the belt and the dog from Box 0 to Box 3
box_3.extend(box_0)
box_0.clear()

# Put the lion and the sandals and the fish into Box 5
box_5.extend(['lion', 'sandals', 'fish'])

# Move the planet and the mask from Box 2 to Box 4
box_4.extend(['planet', 'mask'])
box_2.remove('planet')
box_2.remove('mask')

# Remove the planet and the mask and the mirror from Box 4
box_4.remove('planet')
box_4.remove('mask')
box_4.remove('mirror')

# Replace the belt and the dog with the bracelet and the coat in Box 3
box_3.remove('belt')
box_3.remove('dog')
box_3.extend(['bracelet', 'coat'])

# Move the headphone from Box 7 to Box 0
box_0.append(box_7.pop(1))

# Put the hat and the lightning and the phone into Box 7
box_7.extend(['hat', 'lightning', 'phone'])

# Move the brush from Box 8 to Box 1
box_1.append(box_8.pop(2))

# Swap the shirt in Box 5 with the guitar in Box 4
box_5.remove('shirt')
box_4.remove('guitar')
box_5.append('guitar')
box_4.append('shirt')

# Swap the headphone in Box 0 with the button in Box 2
box_0.remove('headphone')
box_2.remove('button')
box_0.append('button')
box_2.append('headphone')

print("\nAfter modifications:")
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)
print("Box 8:", box_8)