box_0 = ['dice', 'seaweed', 'toaster', 'rocket']
box_1 = ['harmonica', 'island', 'car', 'bowl']
box_2 = ['flute']
box_3 = []
box_4 = ['mountain', 'rock', 'swimsuit', 'pan']

box_4.remove('swimsuit')
box_2.extend(['scissors', 'sock', 'sun'])
box_0.extend(['harmonica', 'island'])
box_2.extend(['pants', 'dolphin'])
box_3.append('train')
box_4 = ['bag', 'shirt', 'headphone']
box_2.append('bowl')
box_1, box_3 = box_3, box_1

print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)