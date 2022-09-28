
'''
opdracht: maak een pretty_print functie die de data uit een file leest en deze data mooi uitprint.

stap 1:  maak een functie die als een parameter de filename meekrijgt

        def pretty_print(filename):
            print(filename)


stap 2: open de file en lees de data uit, oftewel alle regels.

        def pretty_print(filename):
                file = open(filename, 'r')
                data = file.readlines()
                file.close()
                print(data)


stap 3: loop over de data zodat we regel voor regel de data mooi uit kunnen gaan printen.

        def pretty_print(filename):
                file = open(filename, 'r')
                data = file.readlines()
                file.close()
                for line in data:
                    print(line)


stap 4: split de regels zodat we het product en de prijs los van elkaar kunnen gaan gebruiken.
        let hier op dat:
        product, prijs = line.split(':')  een kortere en betere manier is van:
                                                                                 lst = line.split(':')
                                                                                 product = lst[0]
                                                                                 prijs   = lst[1]

            def pretty_print(filename):
                file = open(filename, 'r')
                data = file.readlines()
                file.close()
                for line in data:
                    product, prijs = line.split(':')
                    print(product)
                    print(prijs)


stap 5: print de regel uit als volgende 'product cost prijs euro'

            def pretty_print(filename):
                file = open(filename, 'r')
                data = file.readlines()
                file.close()
                for line in data:
                    product, prijs = line.split(':')
                    s = f'{product} cost {prijs} euro'
                    print(s)


stap 6: verwijder de \n van elke regel zodat elke line op een enkele regel wordt weergegeven.
        Dit kunnen we doen met de string.strip() functie die empty spaces en \n aan het begin en het eind van de string
        verwijderd

            def pretty_print(filename):
                file = open(filename, 'r')
                data = file.readlines()
                file.close()
                for line in data:
                    product, prijs = line.split(':')
                    s = f'{product} cost {prijs.strip()} euro'
                    print(s)

stap 7: maak de formatting nog mooier door de 'cost' en 'euro' onder elkaar te zetten. dit kunnen we doen door in de f'{}'
        :grootte toe te voegen. Dit maakt in het geval van f'{product:12}' dat de waarde van product in een
        gereserveerd blok van 12 characters breed wordt geplaatst. Is er niet genoeg gereserveerd dan wordt het gewoon in de string geplaatst
        en als het kleiner is dan het gereserveerde gedeelte dan wordt het opgevuld met spaties.

            def pretty_print(filename):
                file = open(filename, 'r')
                data = file.readlines()
                file.close()
                for line in data:
                    product, prijs = line.split(':')
                    s = f'{product:12} cost {prijs.strip():5} euro'
                    print(s)
'''





def pretty_print(filename):
    file = open(filename, 'r')
    data = file.readlines()
    file.close()
    for line in data:
        product, prijs = line.split(':')
        s = f'{product:12} cost {prijs.strip():5} euro'
        print(s)

#we kunnen nu onze pretty_print functie vaker gebruiken voor verschillende bestanden die data bevatten in de style  product:prijs
print('De data van de ah is: ')
pretty_print('ah.txt')

print('\n')

print('De data van de boni is: ')
pretty_print('boni.txt')

print('\n')

print('De data van de hoogvliet is: ')
pretty_print('hoogvliet.txt')