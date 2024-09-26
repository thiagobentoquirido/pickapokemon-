import random 
pokemons = [
        'xarizard','arceus','pikachu']
for pokemons in pokemons:
    
    pkch = input('escolha seu pokemon:\n')
    while True:
        if pkch != pokemons:
            print('este pokemon nao existe/nao esta na lista disponivel')
        elif pkch == 'xarizard':
            print(f'[{pokemons}] tem 100 de vida e 300 de ataque')
        elif pkch == 'arceus':
            print(f'[{pokemons}] tem 444 de vida e 222 de ataque')
        elif pkch == 'pikachu':
            print(f'[{pokemons}] tem 667 de vida e 846 de ataque')
    
        else: 
         print('pokemon invalido!')
        break
