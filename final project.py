import os
import random
import time
from colorama import init, Fore, Style

init(autoreset=True)

os.environ['TERM'] = 'xterm'

def main_menu(bankroll):
    clearConsole()
    print(Fore.CYAN + Style.BRIGHT + "🔥🔥----[Welcome to the Python Casino!]----🔥🔥")
    print(Fore.YELLOW + "----[Select your game]----\n")

    print(Fore.RED + "[1] Roulette\n" + Fore.LIGHTYELLOW_EX +
                     "[2] Blackjack\n" + Fore.MAGENTA +
                     "[3] Slots\n")
    print(Fore.GREEN + "[4] Deposit Money \n" + Fore.LIGHTBLACK_EX +
                        "[5] Withdraw Money\n")

    print(Fore.CYAN + f"Wallet: ${bankroll}")
    choice = int(input(Fore.YELLOW + "\nPlease Select your game: "))

    if choice == 1:
        roulette(bankroll)
    elif choice == 2:
        blackjack(bankroll)
    elif choice == 3:
        slots(bankroll)
    elif choice == 4:
        depositFunds(bankroll)
    elif choice == 5:
        withdrawFunds(bankroll)
    else:
        print(Fore.RED + "Invalid selection. Try again.")
        time.sleep(2)
        main_menu(bankroll)


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)


def showWallet(bankroll):
    print(Fore.CYAN + f"\nWallet: ${bankroll}\n")


def betCheck(bankroll, bet):
    if bet == 0:
        main_menu(bankroll)

    if bankroll == 0:
        print(Fore.RED + "Sorry! Not enough funds!")
        time.sleep(3)
        main_menu(bankroll)

    if bet > bankroll:
        print(Fore.RED + "Not enough funds for that bet!")
        time.sleep(1.4)
        main_menu(bankroll)


def depositFunds(bankroll):
    clearConsole()
    print(Fore.GREEN + "----[Deposit Funds]----\n")
    deposit = int(input("How much would you like to deposit?: $"))

    bankroll += deposit

    print(Fore.GREEN + f"Successfully updated wallet with: ${deposit}")
    time.sleep(2)
    main_menu(bankroll)


def withdrawFunds(bankroll):
    clearConsole()
    print(Fore.RED + "----[Withdraw Funds]----\n")

    while True:
        try:
            withdrawal = int(input("How much would you like to withdraw?: $"))

            if withdrawal < 0:
                print(Fore.RED + "Invalid amount! Please enter a positive number.")
            elif withdrawal > bankroll:
                print(Fore.RED + f"Insufficient funds! You only have ${bankroll} available.")
            else:
                bankroll -= withdrawal
                print(Fore.GREEN + f"Successfully withdrew: ${withdrawal}")
                break

        except ValueError:
            print(Fore.RED + "Invalid input! Please enter a valid number.")

    time.sleep(2)
    main_menu(bankroll)

def roulette(bankroll):
    clearConsole()
    print(Fore.YELLOW + "🎰----[Now Playing Roulette]----🎰\n")
    showWallet(bankroll)

    print(Fore.YELLOW + "Betting Options:")
    print("[1] Bet on a Specific Number (0-36) - Pays 35 to 1")
    print("[2] Bet on Color (Red/Black) - Pays 1 to 1")
    print("[3] Bet on Even/Odd - Pays 1 to 1")
    print("[4] Bet on Dozen (1-12, 13-24, 25-36) - Pays 2 to 1\n")

    bet_type = input(Fore.YELLOW + "Select your bet type (1-4): ")

    if bet_type not in ['1', '2', '3', '4']:
        print(Fore.RED + "Invalid bet type. Returning to the main menu.")
        time.sleep(2)
        main_menu(bankroll)

    while True:
        try:
            bet = int(input(Fore.YELLOW + "\nPlease place your bet [USD]: "))
            betCheck(bankroll, bet)
            break
        except ValueError:
            print(Fore.RED + "Invalid input! Please enter a numerical value for your bet.")

    if bet_type == '1':
        while True:
            try:
                bet_number = int(input(Fore.YELLOW + "Enter the number you want to bet on (0-36): "))
                if 0 <= bet_number <= 36:
                    break
                else:
                    print(Fore.RED + "Invalid number! Please enter a number between 0 and 36.")
            except ValueError:
                print(Fore.RED + "Invalid input! Please enter a valid number.")

    elif bet_type == '2':
        bet_color = input(Fore.YELLOW + "Bet on Red or Black: ").lower()
        while bet_color not in ['red', 'black']:
            print(Fore.RED + "Invalid color! Please bet on Red or Black.")
            bet_color = input(Fore.YELLOW + "Bet on Red or Black: ").lower()

    elif bet_type == '3':
        bet_parity = input(Fore.YELLOW + "Bet on Even or Odd: ").lower()
        while bet_parity not in ['even', 'odd']:
            print(Fore.RED + "Invalid choice! Please bet on Even or Odd.")
            bet_parity = input(Fore.YELLOW + "Bet on Even or Odd: ").lower()

    elif bet_type == '4':
        bet_dozen = input(Fore.YELLOW + "Bet on Dozen (1-12, 13-24, 25-36): ")
        while bet_dozen not in ['1-12', '13-24', '25-36']:
            print(Fore.RED + "Invalid choice! Please bet on 1-12, 13-24, or 25-36.")
            bet_dozen = input(Fore.YELLOW + "Bet on Dozen (1-12, 13-24, 25-36): ")

    print(Fore.CYAN + "\nSpinning the wheel...")
    time.sleep(2)
    winning_number = random.randint(0, 36)
    winning_color = get_color(winning_number)
    print(Fore.GREEN + f"🎲 The winning number is {winning_number} ({winning_color})!")

    if bet_type == '1':
        if bet_number == winning_number:
            winnings = bet * 35
            print(Fore.GREEN + f"🎉 Congratulations! You won: ${winnings}")
            bankroll += winnings
        else:
            print(Fore.RED + "💥 You lost this round.")
            bankroll -= bet

    elif bet_type == '2':
        if bet_color == winning_color:
            winnings = bet * 2
            print(Fore.GREEN + f"🎉 Congratulations! You won: ${winnings}")
            bankroll += winnings
        else:
            print(Fore.RED + "💥 You lost this round.")
            bankroll -= bet

    elif bet_type == '3':
        if winning_number != 0 and ((bet_parity == 'even' and winning_number % 2 == 0) or
                                    (bet_parity == 'odd' and winning_number % 2 != 0)):
            winnings = bet * 2
            print(Fore.GREEN + f"🎉 Congratulations! You won: ${winnings}")
            bankroll += winnings
        else:
            print(Fore.RED + "💥 You lost this round.")
            bankroll -= bet

    elif bet_type == '4':
        if (bet_dozen == '1-12' and 1 <= winning_number <= 12) or \
           (bet_dozen == '13-24' and 13 <= winning_number <= 24) or \
           (bet_dozen == '25-36' and 25 <= winning_number <= 36):
            winnings = bet * 3
            print(Fore.GREEN + f"🎉 Congratulations! You won: ${winnings}")
            bankroll += winnings
        else:
            print(Fore.RED + "💥 You lost this round.")
            bankroll -= bet

    time.sleep(3)
    main_menu(bankroll)


def get_color(number):
    red_numbers = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    black_numbers = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
    if number == 0:
        return 'green'
    elif number in red_numbers:
        return 'red'
    else:
        return 'black'

def blackjack(bankroll):
    clearConsole()
    print(Fore.YELLOW + "----[Now Playing Blackjack]----\n")
    print(Fore.CYAN + "If you bet 0, you'll return to the main menu\n")

    showWallet(bankroll)
    bet = int(input(Fore.YELLOW + "Please place your bet [USD]: "))

    betCheck(bankroll, bet)

    player_hand = [draw_card(), draw_card()]
    dealer_hand = [draw_card(), draw_card()]

    print(Fore.CYAN + f"\nYour hand: {player_hand} (Total: {sum(player_hand)})")
    print(Fore.MAGENTA + f"Dealer shows: {dealer_hand[0]}")

    while sum(player_hand) < 21:
        action = input(Fore.YELLOW + "\nDo you want to [H]it or [S]tand? ").lower()
        if action == 'h':
            new_card = draw_card()
            player_hand.append(new_card)
            print(Fore.CYAN + f"You drew: {new_card} (Total: {sum(player_hand)})")
            if sum(player_hand) > 21:
                print(Fore.RED + "\nYou busted! Total:", sum(player_hand))
                bankroll -= bet
                time.sleep(2)
                main_menu(bankroll)
        elif action == 's':
            break
        else:
            print(Fore.RED + "Invalid input. Please enter 'H' to hit or 'S' to stand.")

    print(Fore.MAGENTA + f"\nDealer's hand: {dealer_hand} (Total: {sum(dealer_hand)})")
    while sum(dealer_hand) < 17:
        new_card = draw_card()
        dealer_hand.append(new_card)
        print(Fore.MAGENTA + f"Dealer drew: {new_card} (Total: {sum(dealer_hand)})")
        time.sleep(1)

    player_total = sum(player_hand)
    dealer_total = sum(dealer_hand)

    if dealer_total > 21 or player_total > dealer_total:
        print(Fore.GREEN + f"\nCongratulations! You won: ${bet * 2}")
        bankroll += bet * 2
    elif player_total == dealer_total:
        print(Fore.YELLOW + "\nIt's a push! Your bet is returned.")
    else:
        print(Fore.RED + "\nYou lost. Better luck next time!")
        bankroll -= bet

    time.sleep(3)
    main_menu(bankroll)


def draw_card():
    return random.randint(2, 11)
def slots(bankroll):
    clearConsole()
    print(Fore.YELLOW + "====[Welcome to Inferno Slots!]====\n")
    inferno_slots(bankroll)


def inferno_slots(bankroll):
    clearConsole()

    symbols = ['🔥 Dragon', '🔥 Phoenix', '🔥 Flame', '🔥 Fireball', '👑 Inferno Crown', '✨ Blazing Star']

    print(Fore.RED + "🔥🔥----[Now Playing Inferno Slots]----🔥🔥\n")
    print(Fore.YELLOW + "If you bet 0, you'll return to the main menu\n")

    showWallet(bankroll)
    bet = int(input(Fore.YELLOW + "\nPlease place your bet: $"))

    betCheck(bankroll, bet)

    print("Spinning the reels...")
    time.sleep(1)

    reel1 = random.choice(symbols)
    reel2 = random.choice(symbols)
    reel3 = random.choice(symbols)

    print(f"\n{Fore.RED}| {reel1} | {reel2} | {reel3} |")

    if reel1 == '👑 Inferno Crown' and reel2 == '👑 Inferno Crown' and reel3 == '👑 Inferno Crown':
        winnings = bet * 10000
        print(Fore.YELLOW + "\n🔥🔥 INFERNO JACKPOT! You won: $" + str(winnings))
        bankroll += winnings
    elif reel1 == reel2 == reel3:
        winnings = bet * 50
        print(Fore.GREEN + "\n🔥 TRIPLE MATCH! You won: $" + str(winnings))
        bankroll += winnings
    elif '✨ Blazing Star' in [reel1, reel2, reel3]:
        winnings = bet * 5
        print(Fore.CYAN + "\n✨ A Blazing Star! You won: $" + str(winnings))
        bankroll += winnings
    else:
        print(Fore.RED + "\n💥 You lost! Better luck next spin.")
        bankroll -= bet

    time.sleep(3)
    main_menu(bankroll)

def first_menu():
    clearConsole()
    print(Fore.CYAN + "🔥🔥----[Welcome to Casino Royale]----🔥🔥\n")
    bankroll = int(input(Fore.YELLOW + "Please deposit funds: $"))
    main_menu(bankroll)

first_menu()