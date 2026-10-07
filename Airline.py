class Passenger:
  def __init__(self,passenger_id,name):
    self.__passenger_id=passenger_id
    self.__name=name
  
  def get_id(self):
    return self.__passenger_id
  def get_name(self):
    return self.__name
  
class Flight:
  def __init__(self,flight_no,seats):
    self.flight_no=flight_no
    self.seats=seats
    
  def display_available_seats(self):
    print("\nAvailable Seats")
    
    for seat, status in self.seats.items():
      if status is None:
        print(seat)

class Reservation:
  def __init__(self,passenger,flight,seat_no):
    self.passenger=passenger
    self.flight=flight
    self.seat_no=seat_no
    
class AirlineSystem:
  def __init__(self):
    self.flight=Flight(
      "KQ101",
      {
        "A1":None,
        "A2":None,
        "A3":None,
        "A4":None,
        "A5":None,
        "A6":None
      }
    )
    self.reservations=[]
  
  def book_seat(self):
    pid=input("Passenger ID: ")
    name=input("Passenger Name: ")
    seat=input("Seat Number: ").upper()
    
    if seat not in self.flight.seats:
      print("Seat  Unavailable!.")
      return
    if self.flight.seats[seat] is not None:
      print("Seat already booked")
      return
    
    passenger=Passenger(pid,name)
    
    reservation=Reservation(passenger,self.flight,seat)
    
    self.flight.seats[seat]=passenger
    self.reservations.append(reservation)
    self.save_record(passenger,seat)
    print("Seat booked Succesfully")
  
  def cancel_booking(self):
    seat=input("Seat Number to cancel: ").upper()
    
    if seat in self.flight.seats:
      if self.flight.seats[seat] is not None:
        self.flight.seats[seat]=None
        print("Booking cancelled")
      else:
        print("Seat already empty!")
        
    else:
      print("Invalid seat!")
  
  def view_available_seats(self):
    self.flight.display_available_seats()
    
  def passenger_records(self):
    print("\n Passenger Records")
    
    for  reservation in self.reservations:
      print(reservation.passenger.get_id(),
            reservation.passenger.get_name(),
            reservation.seat_no)
  
  def save_record(self,passenger,seat):
    with open("reservations.txt", "a") as file:
      file.write(
        f"{passenger.get_id()},"
        f"{passenger.get_name()},"
        f"{seat}\n"
      )

system=AirlineSystem()
while True:
  print("\n======AIRLINE SYSTEM=======")
  print("1. Book Seat")
  print("2.Cancel Booking")
  print("3. View Available Seats")
  print("4. Passenger Records")
  print("5. Exit")
  
  choice=input("Enter choice: ")
  
  if choice=="1":
    system.book_seat()
  
  elif choice=="2":
    system.cancel_booking()
    
  elif choice=="3":
    system.view_available_seats()
    
  elif choice=="4":
    system.passenger_records()
    
  elif choice=="5":
    print("Thank you.")
    break
  
  else:
    print("Invalid choice.")     