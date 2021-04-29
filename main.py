#BookmyMovie.com (By Kanishka)

import Colour_Functions as cf   #Importing the file to add colours to the statements

class bookmymovie:
    head = "Welcome to BookmyMovie.com"
    head2 = "We hope you are safe!"
    cf.prRed(head.center(150))
    cf.prRed(head2.center(150))       #Printing the heading with colour RED and center position


    def menu(self):     #Function for displaying menu to the user
        ans = True
        while ans:      #Loop will run until ans is True, else it will stop.
            cf.prPurple("\nEnter the number corresponding to you want to choose :")
            self.choice = int(input("\n1. Show the seats\n2. Buy a Ticket\n3. Statistics\n4. Show booked ticket's user info\n0. Exit\n"))
            # while(self.choice!=0):
            if self.choice == 1:
                self.show_seats()
            elif self.choice == 2:
                self.buy()
            elif self.choice == 3:
                self.stats()
            elif self.choice == 4:
                self.info()
            elif self.choice == 0:
                ans = False
                self.ex()
            else:
                print("\nNot Valid Choice Try again")


    def __init__(self):
        self.row = int(input("Enter the number of rows\n"))
        self.col = int(input("Enter the number of seats in each row\n"))
        self.no_of_seats = self.row * self.col              #Calculating number of seats in the theater
        self.matrix = []                                    #Matrix for the theater seats (2-D)
        self.seat_count = 0                                 #to count number of seats booked
        self.current_income = 0                             #to calculate current income
        self.total_income = 0                               #to calculate possible income
        self.u_details = {}                                 #to store details of users who booked the seat

        for i in range(self.row):                           #Loop to append initial values to Matrix[]
            a = []
            for j in range(self.col):
                a.append("S")
            self.matrix.append(a)
        print(end="  ")

    def show_seats(self):           #Function used to show seats to the user (will be called by pressing 1)
        print("\nCinema :\n")
        a = 0
        b = 0
        print(end="  ")
        for j in range(1, self.col + 1):        #Loop for printing updates matrix
            b = b + 1
            print(b, end=" ")
        print()
        for i in self.matrix:
            a = a + 1
            print(a, end=" ")
            print(" ".join(i), sep=",")


    def buy(self):              #Function for Buying a Ticket(By pressing 2)
        a = int(input("Enter the row you want to book\n"))
        b = int(input("Enter the column you want to book\n"))
        if self.matrix[a-1][b-1] == "B":                        #Check statement whether ticket is booked or not
            print("This seat is already booked")
            self.menu()
        elif self.no_of_seats < 60:                #Will calculate price and ask for permission for booking the ticket
            self.price = 10
            print("Ticket per person is $10, do you want to proceed ahead? Press Y/y")
        elif a < self.row / 2:
            self.price = 10
            print("Ticket per person is $10, do you want to proceed ahead? Press Y/y")
        elif a > self.row / 2:
            self.price = 8
            print("Ticket per person is $8, do you want to proceed ahead? Press Y/y")
        self.pr = input()

        if self.pr == 'Y' or self.pr == 'y':                #If the user confirms the booking, take the user_details
            u_dict = {}
            Uname = input("For Booking, Enter your name\n")
            Ugen = input("Enter your gender\n")
            UAge = input("Enter your age\n")
            Ucn = input("Enter your Contact Number\n")
            self.row1 = a - 1
            self.col1 = b - 1
            self.matrix[self.row1][self.col1] = "B"             #Mark the seat as "B"
            self.seat_count = self.seat_count + 1               #Increase seat count by 1
            self.current_income = self.current_income + self.price          #Calculate current income till now
            # Store the user_details in a dict with rown,coln as key and values as the details
            u_dict[(self.row1+1), (self.col1+1)] = list((Uname, Ugen, UAge, Ucn, self.price))
            self.u_details.update(u_dict)
            print("Booked successfully !!\n")           #print confirmation message
        else:
            print("Booking couldn't be processed!\n")   #print terminated message


    # function for returning total possible revenue that could be earned if all the seats are booked
    def total_revenue(self):
        if self.no_of_seats < 60:
            self.total_income = self.no_of_seats * 10
        elif self.no_of_seats >= 60:
            for i in range(0,int(self.row / 2)):
                c =  int(self.row / 2)* self.col * 10
            for j in range(int(self.row / 2), self.row):
                d = int(self.row / 2)* self.col * 8
            self.total_income = c + d
        return self.total_income


    def stats(self):                    #Function for displaying statistics(By pressing 3)
        print("Number of purchased tickets : ", self.seat_count)
        self.percentage = (self.seat_count / self.no_of_seats) * 100
        print("Percentage of Tickets Booked : ", "{:.2f}".format(self.percentage),"%")
        print("Current Income : $", self.current_income)
        k=self.total_revenue()
        print("Total Income : $", k)


    def info(self):             #Function for printing the user details based on the row,col they booked(By pressing 4)
        self.check_a = int(input("Enter the row you booked\n"))
        self.check_b = int(input("Enter the column you booked\n"))
        if self.matrix[self.check_a-1][self.check_b-1] == 'B':
            c=self.u_details[(self.check_a, self.check_b)]
            print('Name:',c[0])
            print('Gender:',c[1])
            print('Age:',c[2])
            print('Phone no.:',c[3])
        else:                       #If the seat is not booked, displaying "Not booked yet"
            print("This seat is not booked yet!")


    def ex(self):                   #Function for extiting from the program (By pressing 0)
        return None


bmm_obj = bookmymovie()
bmm_obj.menu()
