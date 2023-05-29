import os
import jokehandler

def main():

    os.system('cls' if os.name == 'nt' else 'clear')
    print("\nEtt roligt skämt")

    url = f"https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw&type=single"

    nr = 1
    jokeopbj = jokehandler.Jokehandler(url)

    while True:

        t_joke = jokeopbj.get_joke()

        print("--------------------------")
        print(f"{t_joke}")
        print("--------------------------")

        nr += 1

        entill = input("En till? Ja/Nej")

        if entill == "Nej" or entill == "nej":
            break

main()