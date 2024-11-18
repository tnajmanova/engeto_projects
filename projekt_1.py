'''
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Tereza Najmanová
email: najmanova.tereza@gmail.com
'''

# Vstupní údaje:

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

ODDELOVAC = '-' * 40

registered_users = {
    'bob' : '123',
    'ann' : 'pass123',
    'mike' : 'password123',
    'liz' : 'pass123'
}

# Přihlášení uživatele, ověření, pozdrav, nabídka

print('$ python projekt1.py')
user = input('Your username: ')
password = input('Password: ')

if (user, password) in registered_users.items():
    print(ODDELOVAC, f'Welcome to the app, {user}', 'We have 3 texts to be analyzed.', ODDELOVAC, sep='\n')

else:
    print('unregistered user, terminating the program..', sep='\n')
    quit()


# Analýza textu:

volba_textu = int(input('Enter a number btw. 1 and 3 to select: '))
print(ODDELOVAC)

slovnik_texts = dict(enumerate(TEXTS, 1))

if not volba_textu in slovnik_texts.keys():
    print(f'no text with chosen number {volba_textu}', 'terminating the program..', sep='\n')
    quit()

else:
    slova = list(slovnik_texts[volba_textu].split())

# Celkový počet slov:

print(f'There are {len(slova)} words in the selected text.')

# Počet slov začínajících velkým písmem:

title_slova = [slovo for slovo in slova if slovo.istitle()]
print(f'There are {len(title_slova)} titlecase words.')

# Počet slov začínajících velkým písmem:

upper_slova = [slovo for slovo in slova if slovo.isupper() and slovo.isalpha()]
print(f'There are {len(upper_slova)} uppercase words.')

# Počet slov psaných malými písmeny:

lower_slova = [slovo for slovo in slova if slovo.islower()]
print(f'There are {len(lower_slova)} lowercase words.')

# Počet čísel (ne cifer):

num_slova = [cislo for cislo in slova if cislo.isnumeric()]
print(f'There are {len(num_slova)} numeric strings.')

# Suma všech čísel (ne cifer) v textu:

suma = [int(cislo) for cislo in slova if cislo.isnumeric()]
print(f'The sum of all the numbers {sum(suma)}')

# Sloupcový graf:

vycistena_slova = [slovo.strip(',.:;').lower() for slovo in slova]

delky_slov = [len(slovo) for slovo in vycistena_slova]
vyskyt_delek = {}

for delka in delky_slov:
    if delka in vyskyt_delek:
        vyskyt_delek[delka] += 1
    else:
        vyskyt_delek[delka] = 1

serazeny_vyskyt = dict(sorted(vyskyt_delek.items()))

print(ODDELOVAC, f'LEN|{'OCCURENCES': ^18}|NR.', ODDELOVAC, sep='\n')

for len, nr in serazeny_vyskyt.items():
    print(f'{len: >3}|{'*' * nr: <18}|{nr} ')

