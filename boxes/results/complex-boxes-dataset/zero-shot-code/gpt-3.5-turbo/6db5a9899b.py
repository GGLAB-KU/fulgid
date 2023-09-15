box_0 = ['dress', 'plate']
box_1 = ['keyboard', 'planet', 'flower', 'dice', 'bracelet']
box_2 = ['camera', 'makeup', 'beach']
box_3 = ['coin', 'shorts']
box_4 = []
box_5 = ['train']
box_6 = ['violin', 'glasses', 'key', 'shoes', 'mixer']
box_7 = []
box_8 = []
box_9 = ['skirt']
box_10 = []

# Replace the skirt with the horse in Box 9
box_9.remove('skirt')
box_9.append('horse')

# Replace the makeup and the camera with the storm and the necklace in Box 2
box_2.remove('makeup')
box_2.remove('camera')
box_2.append('storm')
box_2.append('necklace')

# Remove the train from Box 5
box_5.remove('train')

# Remove the keyboard and the bracelet from Box 1
box_1.remove('keyboard')
box_1.remove('bracelet')

# Remove the flower and the dice from Box 1
box_1.remove('flower')
box_1.remove('dice')

# Swap the horse in Box 9 with the mixer in Box 6
box_6.remove('mixer')
box_6.append('horse')

# Move the violin and the glasses from Box 6 to Box 1
box_6.remove('violin')
box_6.remove('glasses')
box_1.append('violin')
box_1.append('glasses')

# Swap the planet in Box 1 with the shorts in Box 3
box_1.remove('planet')
box_3.remove('shorts')
box_1.append('shorts')
box_3.append('planet')

# Move the plate from Box 0 to Box 3
box_0.remove('plate')
box_3.append('plate')

# Replace the dress with the tiger in Box 0
box_0.remove('dress')
box_0.append('tiger')

# Put the seaweed into Box 5
box_5.append('seaweed')

# Replace the mixer with the table in Box 9
box_9.remove('mixer')
box_9.append('table')

# Put the keyboard and the pot into Box 8
box_8.append('keyboard')
box_8.append('pot')

# Move the tiger from Box 0 to Box 10
box_0.remove('tiger')
box_10.append('tiger')

# Replace the table with the rain in Box 9
box_9.remove('table')
box_9.append('rain')

# Remove the rain from Box 9
box_9.remove('rain')

# Replace the keyboard and the pot with the sandals and the horn in Box 8
box_8.remove('keyboard')
box_8.remove('pot')
box_8.append('sandals')
box_8.append('horn')

# Print the contents of each box
for i, box in enumerate([box_0, box_1, box_2, box_3, box_4, box_5, box_6, box_7, box_8, box_9, box_10]):
    print(f"Box {i}: {box}")