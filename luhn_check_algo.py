class CreditCard:
    """
    A credit card of the customer

    Keep track of the customer's credit card information

    Attribute:
        client_name: The name of the client on credit card
        card_number: The 16-digit number of the credit card
    """
    def __init__(self, client_name: str, card_number: str) -> None:
        """
        Initialize the credit card for the customer
        """
        self.client_name = client_name
        self.card_number = card_number

class Bank:
    """
    A bank that the customer registers for the credit card
    """
    def __init__(self, bank_name: str) -> None:
        """
        Initialize the bank 
        """
        self.bank_name = bank_name
<<<<<<< HEAD

=======
        
>>>>>>> 1f0d0afae8ec09912b99ff29738a37a2ce9094ba
    def check_sum(self, card: CreditCard) -> bool:
        """
        Verify the customer's credit card based on 16 digit number
        1) If the digit has an odd index, do nothing
        2) If the digit has an even index, double the digit. 
           If doubled digit has 2 digits, then split to two separate digit
        3) Sum every digit and check:
           - If sum is divisible by 10, then the credit card is valid
           - Otherwise, it is not valid
        """
        digit_list = []
        for index in range(len(card.card_number)):
            digit = card.card_number[index]
            if index % 2 == 0:
                doubled_num = int(digit) * 2
                if len(str(doubled_num)) == 2:
                    sum_digit = doubled_num // 10 + doubled_num % 10
                    digit_list.append(sum_digit)
                else:
                    digit_list.append(doubled_num)
            else:
                digit_list.append(int(digit))
            print(digit_list)

        if sum(digit_list) % 10 == 0:
            return True
        else:
            return False
