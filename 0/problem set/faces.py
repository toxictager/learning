text = input("Please write anything with :) or :( ")

text = text.replace(":)", "🙂")
text = text.replace(":(", "🙁")
print(text)