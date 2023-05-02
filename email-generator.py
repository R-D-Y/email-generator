import random
from faker import Faker

# Defining possible choices for the number of emails to generate
nb_choices = [10, 25, 50, 100, "other"]

# Defining possible choices for the domain to use
domain_choices = ["gmail.com", "outlook.com", "hotmail.com", "icloud.com", "other"]

domain_choices_dict = {"1": "gmail.com", "2": "outlook.com", "3": "hotmail.com", "4": "icloud.com"}

# Asking questions to the user
nb_emails = input("How many emails do you want to generate? ({}) : ".format(", ".join(str(c) for c in nb_choices)))
while nb_emails not in map(str, nb_choices):
    nb_emails = input("Please enter a valid choice among {} : ".format(", ".join(str(c) for c in nb_choices)))

if nb_emails == "other":
    nb_emails = input("How many emails do you want to generate? : ")
    while not nb_emails.isdigit():
        nb_emails = input("Only numbers are required here. How many emails do you want to generate? : ")
    nb_emails = int(nb_emails)

domain = input("Which domain do you want to use? ([1]: gmail.com, [2]: outlook.com, [3]: hotmail.com, [4]: icloud.com, other) : ")
while domain not in domain_choices_dict.keys() and domain not in domain_choices:
    domain = input("Please enter a valid choice among 1 (Gmail), 2 (Outlook), 3 (Hotmail), 4 (Icloud), or other : ".format(", ".join(domain_choices)))

if domain == "other":
    domain = input("What domain name do you want to use? : ")
    while "." not in domain:
        domain = input("Please enter a valid domain name containing a dot : ")
elif domain in domain_choices_dict.keys():
    domain = domain_choices_dict[domain]

export_choice = input("Do you want to export the list of emails to a 'emails.txt' file? (yes/no) : ")
while export_choice.lower() not in ["yes", "no"]:
    export_choice = input("You can only answer with yes or no. Do you want to export the list of emails to a 'emails.txt' file? (yes/no) : ")

## Generating random emails
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
        nb_emails = input("Please enter an integer for the number of emails to generate : ")
    nb_emails = int(nb_emails)
    for i in range(nb_emails):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = "{}.{}@{}".format(first_name.lower(), last_name.lower(), domain)
        emails.append(email)

# Export the generated emails to a text file
if export_choice.lower() == "yes":
    with open("emails.txt", "w") as f:
        f.write("\n".join(emails))
else:
    # Console print
    print("\n".join(emails))

