import time

import atm as atm_library

if __name__ == "__main__":
    atm = atm_library.Atm()
    print(atm.deposit(100))
    print(atm.balance)

    time.sleep(1)
