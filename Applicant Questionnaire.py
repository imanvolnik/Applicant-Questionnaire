from os import system
import time
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
edu_certificate = int(input("Do you have a school education certificate (if yes enter 1, if no enter 0): "))
edu_presence = None

if edu_certificate == 0:
    edu_certificate = False
    print("Unfortunately, if you don't have a school education certificate it's impossible to enter to university")
else:
    ort_score = int(input("Enter your ORT score: "))
    eng_levels = {
        "1) Beginner / A1": 1,
        "2) Elementary / A2": 2,
        "3) Intermediate / B1": 3,
        "4) Upper-Intermediate / B2": 4,
        "5) Advanced / C1": 5,
        "6) Native / C2": 6
    }
    for key in eng_levels:
        print(key)
    lang_level = int(input("Enter your level of english (1 - 6):  "))
    system('cls')
    print("\n" * 111)

    faculties = {
        "1) Computer Engineering 2500$": 1,
        "2) Artificial Intelligence 2200$": 2,
        "3) Psychology 1900$": 3,
        "4) International Relations 2200$": 4,
        "5) Law 1800$": 5,
        "6) Management 2200$": 6,
        "7) Medicine 3300$": 7
    }
    discount = {
        "140-155: 5%": 5,
        "156-174: 10%": 10,
        "175-199: 25%": 25,
        "200-209: 50%": 50,
        "210-218: 75%": 75,
        "219-240: 100%": 100
    }
    if ort_score >= 110 and edu_certificate and lang_level >= 3:
        print("All requirements for admission to the university are satisfied!")
        for key in faculties:
            print(key)
        chosen_fac = int(input("Choose which faculty you want to apply: "))
        system('cls')
        print("\n" * 111)
        for key in discount:
            print(key)
        time.sleep(3)
        system('cls')
        print("\n" * 111)

        fac = " "

        if chosen_fac == 1:
            fac = "Computer Engineering"
            cost = 2500
        elif chosen_fac == 2:
            fac = "Artificial Intelligence"
            cost = 2200
        elif chosen_fac == 3:
            fac = "Psychology"
            cost = 1900
        elif chosen_fac == 4:
            fac = "International Relations"
            cost = 2200
        elif chosen_fac == 5:
            fac = "Law"
            cost = 1800
        elif chosen_fac == 6:
            fac = "Management"
            cost = 2200
        elif chosen_fac == 7:
            fac = "Medicine"
            cost = 3300
        else:
            fac = " "

        percentage = 0

        if 140 <= ort_score <= 155:
            percentage = 5
        elif 156 <= ort_score <= 174:
            percentage = 10
        elif 175 <= ort_score <= 199:
            percentage = 25
        elif 200 <= ort_score <= 209:
            percentage = 50
        elif 210 <= ort_score <= 218:
            percentage = 75
        elif 219 <= ort_score <= 245:
            percentage = 5
        else:
            percentage = 0

        if percentage == 0:
            print(f"""'Dear {first_name} {last_name}, we congratulate you!
You have been admitted to the {fac} program at Ala-Too International University.
The tuition fee will be {cost}$ per year.” 
            """)
        else:
            print(f"""'Dear {first_name} {last_name}, we congratulate you!
You have been admitted to the {fac} program at Ala-Too International University.
The cost of your tuition with a {percentage}% discount will be {cost - (cost * percentage / 100)}$ per year.” 
        """)

    elif ort_score >= 110 and edu_certificate and lang_level < 3:
        print("""We can offer you a one-year preparatory English language course 
(Foundation Course AIU) at the university.
Then next year, after completing that course, you will be able to enroll the university""")

    elif edu_certificate is False or ort_score < 110:
        print("You are not able to university without school education certificate or ort score below than 110")
