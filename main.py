# import time

# import atm as atm_library

# if __name__ == "__main__":
#     atm = atm_library.Atm()
#     # atm.read_card()    
#     # atm.start_session(atm._id, atm.card_number)
#     # atm.start_customer_console()
#     # atm.get_action()
#     # deposit_withdrawal_transfer()
#     time.sleep(1)

import customer
import time

if __name__ == "__main__":
    customer = customer.Customer("bob", 1234, 1234, "")
    time.sleep(1)
    customer.validate_card_id_pin(1234, 1234)
    print(customer.name)
    print(customer.pin)
    customer.logout()
    
