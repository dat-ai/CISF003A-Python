import typing

class Test :
    def __init__(self):
        """

        """
        self.Answer = ""

    def print_answer(self)->None:
        """
        Just prints the Answer variable

        :return:
        """
        print(self.Answer)

    def test_me(self)->None:
        """

        :param self:
        :return:
        """
        print("leave me alone")


class BankAccount:
    def __init__(self, balance: float=0.0):
        """

        :param balance:
        """
        self.Account_number = -1
        self.Account_first_name = ""
        self.Account_last_name = ""
        self.Account_routing_numbers = []
        self.Account_balance = balance

    def print_balance(self):
        print("The account balance is: " + str(self.Account_balance))

    def double_my_money(self):
        self.Account_balance *=2

    def add_to_balance(self, add_to_balance:float):
        """
        Add money to the balance
        :param add_to_balance:
        :return:
        """
        if add_to_balance <0:
            print("excuse me, you have to put some real money please, no funny business!")
            return
        elif add_to_balance > 10**7 :
            print(" please speak to the bank manager we don't accept such large deposits!")
        else:
            self.Account_balance += add_to_balance

    def __str__(self)->str:
        str_rep =""
        str_rep += "The account number is: " + str(self.Account_number ) + "\n"
        str_rep += "For Account holder: " + str(self.Account_first_name) + " "+ str(self.Account_last_name) + "\n"
        str_rep += "The account balance is: " + str(self.Account_balance)
        return str_rep

    def __int__(self)->int:
        return self.Account_number

    def __add__(self, other):

        self.Account_balance += other.Account_balance
        return self

    def __mul__(self, other):
        self.Account_balance *= other.Account_balance
        return self

    def __truediv__(self, other):
        self.Account_balance /= other.Account_balance
        return self


# code entry point
if __name__ == "__main__":
    me = Test()
    second_me = Test()
    me.test_me()
    me.Answer= "Five"
    second_me.Answer = "Ten"
    me.print_answer()
    second_me.print_answer()

    ba = BankAccount()
    print(ba.Account_number)
    ba.print_balance()
    second_account = BankAccount(20)
    second_account.double_my_money()
    second_account.print_balance()
    second_account.add_to_balance(-50000)
    second_account.print_balance()
    second_account.add_to_balance(50000)
    second_account.print_balance()

    # print(str(second_account) )
    print(second_account)

    print(int(second_account) + 5)
    print("is this upper case?".upper())

    test_list = [3, 9, 5, 6, 4]
    test_list.append(20)
    test_int = 23
    print(test_list)
    ba.add_to_balance(500)
    print(second_account+ba)
    print(ba)
    print(second_account)
    print(second_account*ba)
    print(second_account/ba)
