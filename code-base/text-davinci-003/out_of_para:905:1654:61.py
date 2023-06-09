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

class Intestines(Participant):
    def __init__(self, name):
        super().__init__(name)
    
    def complete_digestion(self):
        print(f'{self.name} moves the food into the intestines to complete digestion.')

saliva = Saliva('Saliva')
tongue = Tongue('Tongue')
esophagus = Esophagus('Esophagus')
stomach = Stomach('Stomach')
intestines = Intestines('Intestines')

saliva.break_down_chemicals()
tongue.push_food()
esophagus.move_food()
stomach.break_down_food()
intestines.complete_digestion()