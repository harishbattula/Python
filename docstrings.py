from turtle import Turtle


def hello():
    '''This function just prints hello world'''

    print("hello world")

# print(hello.__doc__)

class RoomBuddies:

    '''Class that lists all the friends in the room'''

    def __init__(self, Roomname = "IPDC"):
        '''
        Constructor in Roombuddies accepts one argument
        Roomname (string) : Either it can be KSC or IPDC
        default : IPDC
        '''

        # setting self object roomname property
        self.roomname = Roomname

        # members involved in both rooms
        self.Members = ["Kranthi", "Fayaz", "Imam", "Manikanta", "Khaleel", "Salman", "Chana", "Dinesh", "Pavan", "Siddik", "Rehman", "Guddu"]
    
    def Details(self):
        '''
        Provids details about the people in the room
        '''
        if self.roomname == "IPDC":
            self.Members.append(["Kiran", "Sairam", "Mahesh"])
        else:
            self.Members.append(["Roopsai"])

# print(RoomBuddies.__doc__)

help(RoomBuddies)
help(RoomBuddies.Details)

    
