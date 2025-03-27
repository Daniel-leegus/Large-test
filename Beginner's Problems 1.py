def convert_min_to_sec(minutes):
    return f"{minutes * 60} seconds"

def jane_birthday_cards(cards):
    return f"Jane receives at least {cards * 2} cards."

def age_to_days(years):
    return f"You are {years * 365} days old."

def time_until_death(yars):
    return f"You are {yars * 365} days old. In {36500 - (yars * 365)} days you will be 100 years old!"

print(convert_min_to_sec(int(input())))
print(jane_birthday_cards(int(input())))
print(age_to_days(int(input("Enter your age in years: "))))
print(time_until_death(int(input("Enter your age in years: "))))
