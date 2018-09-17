import random

def handle_rerolls():
    res = input('Would you like to reroll again? (y/n). ')
    res = res.lower()
    if type(res) != type(str):
        while type(res) != type(str) and (res != 'y' and res != 'n'):
            res = input("Invalid input! Please enter if you would like to reroll again (y/n). ")
            res = res.lower()
    if res == 'y':
        return True
    return False

if __name__ == "__main__":
    is_continue = True
    while is_continue:
        dice_num = random.randrange(1, 7)
        print("The dice number is:", dice_num)
        is_continue = handle_rerolls()