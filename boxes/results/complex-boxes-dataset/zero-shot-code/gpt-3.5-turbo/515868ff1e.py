box0 = ['motorcycle', 'dolphin', 'tree']
box1 = ['grinder', 'usb']
box2 = ['microscope', 'blender']
box3 = ['coat']
box4 = ['keyboard', 'comb', 'pen']
box5 = ['necklace', 'planet']

box5.append('button')
box5.append('motorcycle')
box5.append('harmonica')

box0.remove('dolphin')
box0.append('tree')

box2.remove('blender')

box3.remove('coat')

box5.append('microscope')

box1[1], box5[2] = box5[2], box1[1]

box2.extend(box4[1:])
box4 = []

box1.extend(box0[:2])
box0 = []

box2.remove('comb')

boxes = [box0, box1, box2, box3, box4, box5]

for i, box in enumerate(boxes):
    print(f"Box {i}: {box}")