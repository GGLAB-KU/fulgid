class AirlineReservation:
    def __init__(self):
        self.passenger = None
        self.luggage = None
        self.boarding_pass = None
        self.destination = None

class Passenger:
    def __init__(self, name, identification):
        self.name = name
        self.identification = identification
        self.airline_reservation = None
        self.boarding_pass = None
        self.destination = None
    
    def make_reservation(self, airline_reservation):
        self.airline_reservation = airline_reservation
    
    def check_in(self):
        self.boarding_pass = self.airline_reservation.boarding_pass
        self.destination = self.airline_reservation.destination
    
    def board_plane(self):
        pass
    
    def get_off_plane(self):
        pass

class Luggage:
    def __init__(self, weight, size):
        self.weight = weight
        self.size = size
        self.airline_reservation = None
    
    def check_in(self, airline_reservation):
        self.airline_reservation = airline_reservation

class Airport:
    def __init__(self):
        self.passengers = []
    
    def add_passenger(self, passenger):
        self.passengers.append(passenger)
    
    def check_luggage(self, luggage):
        pass
    
    def issue_boarding_pass(self, passenger):
        passenger.airline_reservation.boarding_pass = 'Boarding Pass'

class Plane:
    def __init__(self):
        self.passengers = []
    
    def add_passenger(self, passenger):
        self.passengers.append(passenger)
    
    def arrive_at_destination(self):
        for passenger in self.passengers:
            passenger.airline_reservation.destination = 'Destination'

# Main
airline_reservation = AirlineReservation()
passenger = Passenger('John', '12345')
luggage = Luggage(20, 'large')

passenger.make_reservation(airline_reservation)
luggage.check_in(airline_reservation)

airport = Airport()
airport.add_passenger(passenger)
airport.check_luggage(luggage)
airport.issue_boarding_pass(passenger)

passenger.check_in()

plane = Plane()
plane.add_passenger(passenger)
plane.arrive_at_destination()

passenger.board_plane()
passenger.get_off_plane()