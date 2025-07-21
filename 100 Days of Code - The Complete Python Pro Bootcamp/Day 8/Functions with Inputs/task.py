def life_in_weeks(age):
    weeks_for_90 = 52 * (90 - age)
    print(f"You have {weeks_for_90} weeks left")


life_in_weeks(56)


def calculate_love_score(name1, name2):
    name1 = name1.lower()
    name2 = name2.lower()
    score1 = 0
    score2 = 0
    true_test = ['t','r','u','e']
    love_test = ['l','o','v','e']
    for letter in name1:
        if letter in true_test:
            score1 += 1
        if letter in love_test:
            score2 += 1
    for letter in name2:
        if letter in true_test:
            score1 += 1
        if letter in love_test:
            score2 += 1
    print(score1,score2)


calculate_love_score("Kanye West", "Kim Kardashian")