box0 = []
box1 = ['planet', 'rocket', 'toy', 'mountain', 'harmonica']
box2 = ['rock']
box3 = ['bag', 'shoes', 'gloves', 'bus', 'boot']

# Put the tiger into Box 2
box2.append('tiger')

# Replace the tiger with the scarf in Box 2
box2.remove('tiger')
box2.append('scarf')

# Move the toy and the rocket from Box 1 to Box 2
box2.extend(box1[2:4])
box1 = box1[:2] + box1[4:]

# Put the button and the bear into Box 0
box0.extend(['button', 'bear'])

# Put the shorts and the clock and the horse into Box 0
box0.extend(['shorts', 'clock', 'horse'])

# Put the grass and the battery into Box 3
box3.extend(['grass', 'battery'])

print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)