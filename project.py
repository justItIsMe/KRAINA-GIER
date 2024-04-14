while True:
    print("! KRAINA GIER, Autor: Patryk Wołoszyn 2BP !\n\n")
    print("1. Zgadnij liczbę\n")
    print("2. Szybki strzał\n")
    print("3. Kamień, papier, nożyce\n")

    choice = int(input("Wybierz grę (1 - 3): "))

    if choice == 1:
        import random

        def askForGuess():
            while True:
                guess = input('> ')

                if guess.isdecimal():
                    return int(guess)
                print('Proszę, podaj liczbę z zakresu od 1 do 100.')


        print('Odgadnij liczbę.')
        print()
        secretNumber = random.randint(1, 100)
        print('Mam na myśli liczbę z zakresu do 1 do 100.')

        for i in range(10):
            print('Masz jeszcze {} prób(y). Spróbuj odgadnąć liczbę.'.format(10 - i))

            guess = askForGuess()
            if guess == secretNumber:
                break  

            if guess < secretNumber:
                print('Podana przez Ciebie liczba jest za mała.')
            if guess > secretNumber:
                print('Podana przez Ciebie liczba jest za wysoka.')

        if guess == secretNumber:
            print('Hurra! Odgadłeś moją liczbę!')
        else:
            print('Koniec gry. Liczbą, o której myślałem, jest', secretNumber,'.')

    elif choice == 2:
        import random, sys, time

        print('Szybki strzał.')
        print()
        print('Czas sprawdzić swój refleks, by zobaczyć, czy jesteś najszybszym')
        print('strzelcem na Dzikim Zachodzie!')
        print('Gdy zobaczysz "STRZAŁ", masz 0.3 sekundy, by nacisnąć ENTER.')
        print('Jednak przegrasz, jeśli naciśniesz Enter, zanim pojawi się "STRZAŁ".')
        print()
        input('Naciśnij Enter, by rozpocząć...')

        while True:
            print()
            print('Samo południe...')
            time.sleep(random.randint(20, 50) / 10.0)
            print('STRZAŁ!')
            drawTime = time.time()
            input() 
            timeElapsed = time.time() - drawTime

            if timeElapsed < 0.01:
                print('Strzeliłeś przed pojawieniem się słowa "STRZAŁ"! Przegrałeś.')
            elif timeElapsed > 0.3:
                timeElapsed = round(timeElapsed, 4)
                print('Zajęło Ci', timeElapsed, 'sekundy, by strzelić. Za wolno!')
            else:
                timeElapsed = round(timeElapsed, 4)
                print('Zajęło Ci', timeElapsed, 'sekundy, by strzelić.')
                print('Jesteś najszybszym strzelcem na Dzikim Zachodzie! Wygrałeś!')

            print('Wpisz KONIEC, by zakończyć program, lub naciśnij Enter, by zagrać jeszcze raz.')
            response = input('> ').upper()
            if response == 'KONIEC':
                print('Dziękujemy za grę!')
                sys.exit()
    elif choice == 3:
        import random, time, sys

        print('''Papier, kamień, nożyce.
        - Kamień wygrywa z nożycami.
        - Papier wygrywa z kamieniem.
        - Nożyce wygrywają z papierem.
        ''')

        wins = 0
        losses = 0
        ties = 0

        while True: 
            while True:
                print('Wygrane: {}, Przegrane: {}, Remisy: {}'.format(wins, losses, ties))
                print('Podaj swój ruch: (K)amień (P)apier (N)ożyce lub (Z)akończ')
                playerMove = input('> ').upper()
                if playerMove == 'Z':
                    print('Dziękujemy za grę!')
                    sys.exit()

                if playerMove == 'K' or playerMove == 'P' or playerMove == 'N':
                    break
                else:
                    print('Podaj jedną z następujących liter: K, P, N lub Z.')

            if playerMove == 'K':
                print('KAMIEŃ kontra...')
                playerMove = 'KAMIEŃ'
            elif playerMove == 'P':
                print('PAPIER kontra...')
                playerMove = 'PAPIER'
            elif playerMove == 'N':
                print('NOŻYCE kontra...')
                playerMove = 'NOŻYCE'

            time.sleep(0.5)
            print('1...')
            time.sleep(0.25)
            print('2...')
            time.sleep(0.25)
            print('3...')
            time.sleep(0.25)

            randomNumber = random.randint(1, 3)
            if randomNumber == 1:
                computerMove = 'KAMIEŃ'
            elif randomNumber == 2:
                computerMove = 'PAPIER'
            elif randomNumber == 3:
                computerMove = 'NOŻYCE'
            print(computerMove)
            time.sleep(0.5)

            if playerMove == computerMove:
                print('Jest remis!')
                ties = ties + 1
            elif playerMove == 'KAMIEŃ' and computerMove == 'NOŻYCE':
                print('Wygrałeś!')
                wins = wins + 1
            elif playerMove == 'PAPIER' and computerMove == 'KAMIEŃ':
                print('Wygrałeś!')
                wins = wins + 1
            elif playerMove == 'NOŻYCE' and computerMove == 'PAPIER':
                print('Wygrałeś!')
                wins = wins + 1
            elif playerMove == 'KAMIEŃ' and computerMove == 'PAPIER':
                print('Przegrałeś!')
                losses = losses + 1
            elif playerMove == 'PAPIER' and computerMove == 'NOŻYCE':
                print('Przegrałeś!')
                losses = losses + 1
            elif playerMove == 'NOŻYCE' and computerMove == 'KAMIEŃ':
                print('Przegrałeś!')
                losses = losses + 1
    else:
        print("Nie ma takiej gry! Wybierz ponownie!")