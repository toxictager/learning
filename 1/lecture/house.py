name = input("what is your name? ")

match name:
    case "harry":
        print("Gryffindor")
    case "hermione":
        print("Griffindor")
    case "draco":
        print("Slytherin")
    case _:
        print("Who?")



match name:
    case "harry" | "hermione" | "ron":
        print("Gryffindor")
    case "draco":
        print("Slytherin")
    case _:
        print("Who?")
