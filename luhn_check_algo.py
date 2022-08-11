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
    def check_sum(self, card: CreditCard) -> bool:
        digit_dict = {}
        digit_list = []
        for index in range(len(card.card_number)):
            digit = card.card_number[index]
            if index % 2 == 0:
                doubled_num = int(digit) * 2
                if len(str(doubled_num)) == 2:
                    sum_digit = doubled_num // 10 + doubled_num % 10
                    digit_dict[index] = sum_digit
                    digit_list.append(sum_digit)
                else:
                    digit_dict[index] = doubled_num
                    digit_list.append(doubled_num)
            else:
                digit_dict[index] = int(digit)
                digit_list.append(int(digit))
            print(digit_list)

        if sum(digit_list) % 10 == 0:
            return True
        else:
            return False
