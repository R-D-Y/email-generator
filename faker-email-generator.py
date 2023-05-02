import random
from faker import Faker

# Définition des choix possibles pour le nombre d'emails à générer
nb_choices = [10, 25, 50, 100, "autre"]

# Définition des choix possibles pour le domaine à utiliser
domain_choices = ["gmail.com", "outlook.com", "hotmail.com", "icloud.com", "autre"]

domain_choices_dict = {"1": "gmail.com", "2": "outlook.com", "3": "hotmail.com", "4": "icloud.com"}

# Pose des questions à l'utilisateur
nb_emails = input("Combien d'email souhaitez-vous générer ? ({}) : ".format(", ".join(str(c) for c in nb_choices)))
while nb_emails not in map(str, nb_choices):
    nb_emails = input("Veuillez entrer un choix valide parmi {} : ".format(", ".join(str(c) for c in nb_choices)))

if nb_emails == "autre":
    nb_emails = input("Combien d'emails souhaitez-vous générer ? : ")
    while not nb_emails.isdigit():
        nb_emails = input("Seuls des chiffres sont requis ici. Combien d'emails souhaitez-vous générer ? : ")
    nb_emails = int(nb_emails)

domain = input("Quel domaine souhaitez-vous utiliser ? ([1]: gmail.com, [2]: outlook.com, [3]: hotmail.com, [4]: icloud.com, autre) : ")
while domain not in domain_choices_dict.keys() and domain not in domain_choices:
    domain = input("Veuillez entrer un choix valide parmi 1 (Gmail), 2 (Outlook), 3 (Hotmail), 4 (Icloud) ou autre : ".format(", ".join(domain_choices)))

if domain == "autre":
    domain = input("Quel nom de domaine souhaitez-vous utiliser ? : ")
    while "." not in domain:
        domain = input("Veuillez entrer un nom de domaine valide comportant un point : ")
elif domain in domain_choices_dict.keys():
    domain = domain_choices_dict[domain]

export_choice = input("Souhaitez-vous exporter la liste d'emails dans un fichier 'emails.txt' ? (oui/non) : ")
while export_choice.lower() not in ["oui", "non"]:
    export_choice = input("Vous ne pouvez répondre que par oui ou non. Souhaitez-vous exporter la liste d'emails dans un fichier 'emails.txt' ? (oui/non) : ")

# Génération des emails aléatoires
fake = Faker()
emails = []
if isinstance(nb_emails, int):
    for i in range(nb_emails):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = "{}.{}@{}".format(first_name.lower(), last_name.lower(), domain)
        emails.append(email)
else:
    while not nb_emails.isdigit():
        nb_emails = input("Veuillez entrer un nombre entier pour le nombre d'emails à générer : ")
    nb_emails = int(nb_emails)
    for i in range(nb_emails):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = "{}.{}@{}".format(first_name.lower(), last_name.lower(), domain)
        emails.append(email)

# Export des emails dans un fichier texte
if export_choice.lower() == "oui":
    with open("emails.txt", "w") as f:
        f.write("\n".join(emails))
else:
    # Affichage des emails dans le terminal
    print("\n".join(emails))

