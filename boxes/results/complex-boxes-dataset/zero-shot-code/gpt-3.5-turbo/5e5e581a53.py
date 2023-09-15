box_0 = ['zipper', 'rock']
box_1 = []
box_2 = ['button', 'clock', 'spoon']
box_3 = ['horn', 'key', 'jacket']
box_4 = ['starfish', 'basket', 'island']
box_5 = ['tie']
box_6 = ['game', 'gloves', 'paint', 'tree']

box_1.append('star')
box_0.remove('rock')
box_0.remove('zipper')
box_2.append('dress')
box_2.append('meteor')
box_2.append('coral')
box_4.remove('basket')
box_6.append('basket')
box_4.remove('starfish')
box_6.append('starfish')
box_2.append('tie')
box_2.remove('coral')
box_2.remove('meteor')
box_6.remove('starfish')
box_1, box_3 = box_3, box_1

print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)