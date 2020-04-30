import time

import atm as atm_library

if __name__ == "__main__":
    atm = atm_library.Atm()
    atm.log_in("1111111111", "1111")
    atm.deposit(100)
    print(atm.balance)
    print(vars(atm))
    print(vars(atm._account))
    print(atm.balance)

    time.sleep(1)
