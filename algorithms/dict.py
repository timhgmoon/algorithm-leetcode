voted = {}
def check_voter(name):
  if voted.get(name):
    print("kick em out")
  else:
    voted[name] = True
    print("let them vote")

check_voter("tom")
check_voter("mike")
check_voter("mike")