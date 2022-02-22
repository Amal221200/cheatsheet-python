class Customer:
    def __init__(self, name, membership_type):
        self.name = name
        self.membership_type = membership_type
    
    def update_membership(self, new_membership):
        print("Calculating Cost")
        self.membership_type = new_membership

    def __str__(self):
        return self.name+" "+self.membership_type
    
    def print_all_customers(customers):
        for customer in customers:
            print(customer)
    
    # def __eq__(self, other):
    #     if self.name == other.name:
    #         return True
        
    #     return False
    
    # __hash__ = None

    # __repr__ = __str__


# c = Customer("Amal", "Gold")
customer = [Customer("Amal", "Gold"), Customer("Skillf", "Vibranium")]


print(c.name, c.membership_type)