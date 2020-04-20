import time

import atm as atm_library

if __name__ == "__main__":
    atm = atm_library.Atm()
    atm.read_card()    
    atm.start_session(atm._id, atm.card_number)
    atm.start_customer_console()
    atm.get_action()
    time.sleep(1)
