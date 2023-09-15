box_0 = ['planet', 'paint']
box_1 = ['earring', 'comet', 'puzzle']
box_2 = ['leaf', 'needle']
box_3 = ['pillow', 'shelf']
box_4 = ['umbrella', 'wire', 'telescope', 'snow', 'speaker']
box_5 = ['shoe', 'mask']
box_6 = ['wallet', 'soap', 'scarf', 'watch', 'grass']
box_7 = []
box_8 = []
box_9 = ['polish', 'lamp', 'car', 'bell']
box_10 = ['button']
box_11 = ['bear']
box_12 = ['apple', 'microscope', 'rain', 'harmonica']

box_0.remove('planet')
box_0.append('perfume')

box_10.remove('button')

box_11.remove('bear')
box_11.append('scissors')

box_5.clear()

box_0, box_1 = box_1, box_0

box_3.remove('pillow')

box_6.remove('watch')
box_6.remove('scarf')
box_7.append('watch')
box_7.append('scarf')

box_2.clear()

box_3.remove('shelf')
box_6.append('shelf')

box_6.remove('grass')
box_6.remove('shelf')
box_6.remove('wallet')
box_3.append('grass')
box_3.append('shelf')
box_3.append('wallet')

box_12.remove('rain')
box_12.append('seaweed')

box_4.remove('wire')
box_4.remove('snow')
box_4.remove('umbrella')

box_9.remove('polish')
box_12.append('polish')

box_7.remove('scarf')
box_0, box_7 = box_7, box_0

box_12.remove('polish')
box_12.append('plate')

box_11.remove('scissors')
box_12.append('scissors')

box_4.append('basket')

box_4.remove('speaker')
box_7.append('speaker')

box_0.remove('scarf')

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