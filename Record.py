class Record():
    def __init__(self,people,payment,percentage_cost,max_cap,amount_paid):
        self.__people=people
        self.__payment=payment
        self.__percentage_cost=percentage_cost
        self.__max_cap=max_cap
        self.__amount_paid=amount_paid


    def get_people(self):
        return self.__people

    def get_payment(self):
        return self.__payment

    def get_percentage_cost(self):
        return self.__percentage_cost

    def get_max_cap(self):
        return self.__max_cap

    def get_amount_paid(self):
        return self.__amount_paid

    def set_people(self,people):
        self.__people=people

    def set_payment(self,payment):
        self.__payment=payment

    def set_percentage_cost(self,percentage_cost):
        self.__percentage_cost=percentage_cost

    def set_max_cap(self,max_cap):
        self.__max_cap=max_cap

    def set_amount_paid(self,amount_paid):
        self.__amount_paid=amount_paid