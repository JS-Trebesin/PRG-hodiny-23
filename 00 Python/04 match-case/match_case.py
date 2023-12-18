
pozdrav = "neee"

# if pozdrav == "Ahoj":
#     print("Ahoj")
# elif pozdrav == "Čau":
#      print("Čau")

match pozdrav:
    case "Ahoj" | "ahoj":
         print("Ahoj")
    case "Čau":
          print("Čau")
    case "Hi":
          print("Hi")
    case _:
          print("nebyl zvolen pozdrav")