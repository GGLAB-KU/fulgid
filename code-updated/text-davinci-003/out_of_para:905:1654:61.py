class Participant:
    def __init__(self, name):
        self.name = name

class Saliva(Participant):
    def __init__(self, name):
        super().__init__(name)
    
    def break_down_chemicals(self):
        print(f'{self.name} breaks down the chemicals in the food.')

class Tongue(Participant):
    def __init__(self, name):
        super().__init__(name)
    
    def push_food(self):
        print(f'{self.name} pushes the food around while you chew with your teeth.')

class Esophagus(Participant):
    def __init__(self, name):
        super().__init__(name)
    
    def move_food(self):
        print(f'{self.name} moves food from the back of your throat to your stomach.')

class Stomach(Participant):
    def __init__(self, name):
        super().__init__(name)
    
    def break_down_food(self):
        print(f'Strong muscles in the walls of the {self.name} and gastric juices break down food in your stomach.')

    def move_to_intestines(self, intestines):
        print(f'{self.name} moves the food into the intestines to complete digestion.')
        intestines.receive_food()

class Intestines(Participant):
    def __init__(self, name):
        super().__init__(name)
        self.food_received = False
    
    def receive_food(self):
        self.food_received = True
    
    def complete_digestion(self):
        if self.food_received:
            print(f'{self.name} completes digestion of the food.')
        else:
            print(f'{self.name} has not received any food yet.')

class Kidneys(Participant):
    def __init__(self, name):
        super().__init__(name)
    
    def filter_blood(self):
        print(f'{self.name} filters the blood.')

class DigestiveSystem:
    def __init__(self):
        self.saliva = Saliva('Saliva')
        self.tongue = Tongue('Tongue')
        self.esophagus = Esophagus('Esophagus')
        self.stomach = Stomach('Stomach')
        self.intestines = Intestines('Intestines')
        self.kidneys = Kidneys('Kidneys')
    
    def start_digestion(self):
        self.saliva.break_down_chemicals()
        self.tongue.push_food()
        self.esophagus.move_food()
        self.stomach.break_down_food()
        self.stomach.move_to_intestines(self.intestines)
        self.intestines.complete_digestion()
    
    def filter_blood(self):
        self.kidneys.filter_blood()

digestive_system = DigestiveSystem()
digestive_system.start_digestion()

# Answering the question
print('If the blood is able to filter through the kidneys, how will it affect MORE digestion occuring?')
print('Valid options : ["more", "less", "no effect"]')
answer = input('Answer : ')

if answer == 'more':
    digestive_system.start_digestion()
elif answer == 'less':
    print('Digestion will be affected.')
else:
    print('No effect on digestion.')