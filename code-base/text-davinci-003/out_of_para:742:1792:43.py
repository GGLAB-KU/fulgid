class Bat:
    def __init__(self):
        self.location = None
 
    def send_sound_waves(self):
        # code to send out sound waves
        pass
 
    def hear_echo(self):
        # code to hear the echo
        pass
 
    def find_object(self):
        # code to figure out where the object is located
        pass
 
class Object:
    def __init__(self):
        self.location = None
 
    def receive_sound_waves(self):
        # code to receive sound waves
        pass
 
    def produce_echo(self):
        # code to produce an echo
        pass
 
 
bat = Bat()
object = Object()
 
# The bat sends out sound waves from their mouth or nose
bat.send_sound_waves()
 
# The sound waves hit an object
object.receive_sound_waves()
 
# Echoes are produced
object.produce_echo()
 
# The echo returns to the bat's ears
bat.hear_echo()
 
# The bat can figure out where the object is located.
bat.find_object()