class Bus:
    """Class the describes a Bus Object."""

    def __init__(self, fare: float, capacity: int):
        """
        Initialize an instance of an object called Bus.

        You need to initialize the parameters fare and float
        
        Also, create additional initializations of 
        passenger_count(integer) and distance_travelled(float)
        and set them to zero (or 0.0 respectively). 
        """
        # Your code goes here

    def go(self, distance: float):
        """
        Increase the total distance travelled by the current distance
        """
        # Your code goes here

    def accept_passenger(self):
        """Accept a passenger.

        If the bus has enough capacity, then
        the passenger count must increase by 1.

        """
        # Your code goes here

    def let_out_passenger(self):
        """On each stop, let a passenger out.
        
        You need to check if there are any passengers left on the bus. 
        If yes, remove a passenger. 
 
        """
        # Your code goes here


class Passenger:
    """This class describes a passenger."""

    def __init__(self, cash: float):
        """
        Initialize an instance of an object called Passenger.
        """
        # Your code goes here

    def can_I_get_on_the_bus(self, b: Bus):
        """This method checks if I, the passenger, can get on the bus b.
        
        You need to check if the cash for the passenger is greater than
        the fare cost. If yes, return True. Else, return False. 
        
        """
       # Your code goes here




############################################
############## RIDE SIMULATOR ##############
############################################


'''
Let's look at a simple example: a bus and a passenger

'''
b = Bus(2.75, 10)
p = Passenger(5.5)


# Bus fare is ${b.fare} and the Passenger has ${p.cash} 


if p.can_I_get_on_the_bus(b):
    b.accept_passenger()
    print(f"Passenger accepted! He now has ${p.cash} left!\n")
else:
    print(f"The passenger could not get on!" +
            f"He only had ${p.cash}, :(")









'''
Problem 1: a bus with 3 stops
'''


stops = [i for i in range(1, 4)]   
# this is equivalent to the list [1,2,3]
# we can assume that each stop is a mile apart.

b = Bus(2.75, 10)
p = Passenger(5.5)

'''
Bus fare is ${b.fare} and the Passenger has ${p.cash}

We want the passenger to get on at the 1st stop
and get off at the 3rd stop.
'''
        

for stop in stops:
    # make bus go to the next stop



    # Print a statement saying which stop the bus is at



    # If the bus is at stop one, check if the passenger can get on the bus
    # Use the 'can_I_get_on_the_bus(b)' function
    # Use the 'accept_passenger()' function
    # Display the total number of passengers now.





    # Else if the stop is at bus 3, let the passenger out
    # use the 'let_out_passenger()' function
    # Display how many passengers are on the bus. 








'''
Problem 2: A bus with 8 stops and 20 passengers


Assume every passenger wants to get off exactly 3 stops later. 
So if they got on at stop 1, they get off at stop 4. 
If they got on at stop 5, they get off at stop 8.
etc.

Info about the Bus:
    The Bus can hold 10 people at one time. 
    The fare for the bus is $2.25



Info about the passengers:
    Passenger1  -- Cash: $5.50, Pick-up: Stop 1
    Passenger2  -- Cash: $2.00, Pick-up: Stop 1
    Passenger3  -- Cash: $20.00, Pick-up: Stop 1
    Passenger4  -- Cash: $3.75, Pick-up: Stop 1
    Passenger5  -- Cash: $3.50, Pick-up: Stop 2
    Passenger6  -- Cash: $17.00, Pick-up: Stop 2
    Passenger7  -- Cash: $12.25, Pick-up: Stop 2
    Passenger8  -- Cash: $7.00, Pick-up: Stop 2
    Passenger9  -- Cash: $10.75, Pick-up: Stop 2
    Passenger10 -- Cash: $5.00, Pick-up: Stop 3
    Passenger11 -- Cash: $4.75, Pick-up: Stop 3
    Passenger12 -- Cash: $2.75, Pick-up: Stop 3
    Passenger13 -- Cash: $13.00, Pick-up: Stop 4
    Passenger14 -- Cash: $15.25, Pick-up: Stop 4
    Passenger15 -- Cash: $1.50, Pick-up: Stop 4
    Passenger16 -- Cash: $11.75, Pick-up: Stop 4
    Passenger17 -- Cash: $4.75, Pick-up: Stop 4
    Passenger18 -- Cash: $2.00, Pick-up: Stop 5
    Passenger19 -- Cash: $14.25, Pick-up: Stop 5
    Passenger20 -- Cash: $15.25, Pick-up: Stop 5





Using your knowledge from the previous problem,

Create a simulator that will pick up and drop off each passenger above
    at the appropriate spot. 

Determine if the bus has enough capicity for the passenger, as well as 
    if the passenger has enough cash. 

You should be keeping track of:
    who got on at what stop, 
    who got off at what stop,
    how much money each passenger has left, 
    as well as who couldn't get on the buys and why (too many ppl or not enough cash)

You should at the end of your program print out a summary of each passenger stating all 
     the items I asked you to keep track of.
     For example: "Passenger x got on at stop 1, off at stop 4, and now has $2.00 remaining.
                  "Passenger y could not get on at stop 2 becuase he did not have enough cash"
                  etc.


You should use the code we built above. But you are not limited to this code.
I expect you to use the clases that we built for a majority of the assignment, 
however, feel free to add more functions, methods, classes, etc to help you
in this assignment if you see necessary. 

'''




