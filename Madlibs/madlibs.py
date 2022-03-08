# concatenation de string (aka comment assembler des caine de caractere)
# supposons que nous voulions créer une chaîne qui dit "s'abonner à ______"
# youtuber = "IbacTV" # une variable string 

# #quelques façon de le faire
# print("subscribe to " + youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")

madlib = f"Computer programming is so {adj}! it makes me so excited all the time \
I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}"

print(madlib)