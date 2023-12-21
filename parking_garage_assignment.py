class ParkingGarage():
    def __init__(self, total_tickets, total_parking_spaces):
        self.tickets = list(range(1, total_tickets + 1))
        self.parking_spaces = list(range(1, total_parking_spaces + 1))
        self.current_ticket = {}

    def takeTickets(self):
        if self.tickets:
            ticket = self.tickets.pop(0)
            space = self.parking_spaces.pop(0)
            self.current_ticket[ticket] = {"paid": False, "space": space}
            print(f"Ticket {ticket} issued. Park in space {space}.")
        else:
            print("Sorry, the garage is full. No more tickets available.")

    def payForParking(self):
        ticket = int(input("Enter your ticket number: "))
        if ticket in self.current_ticket and not self.current_ticket[ticket]["paid"]:
            payment = input("Enter the amount to pay: ")
            if payment:
                print("Ticket has been paid. You have 15 minutes to leave.")
                self.current_ticket[ticket]["paid"] = True
            else:
                print("Payment not provided. Ticket not paid.")
        else:
            print("Invalid ticket number or ticket already paid.")

    def leaveGarage(self):
        ticket = int(input("Enter your ticket: "))
        if ticket in self.current_ticket:
            if self.current_ticket[ticket]["paid"]:
                print("Thank you, have a nice day!")
                self.parking_spaces.append(self.current_ticket[ticket]["space"])
                self.tickets.append(ticket)
                del self.current_ticket[ticket]
            else:
                print("Ticket not paid. Please pay before leaving.")
        else:
            print("Invalid ticket number.")

if __name__ == "__main__":
    garage = ParkingGarage(total_tickets=10, total_parking_spaces=10)

    garage.takeTickets()
    garage.payForParking()
    garage.leaveGarage()
        