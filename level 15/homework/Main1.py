luka=False
while luka==False:
    ask=input("how are You?")
    if ask=="Normal":
        print("Bot:I hope you will get better")
        luka=True
    elif ask=="Great":
        print("Bot:Good! Have a nice day")
        luka=True
    elif ask== 'sad' or ask=='super sad':
        print("Bot:It's sad")
        luka=True
    else:
        ask=input("Bot: Sorry, I didn't understand, repeat")
print("GoodBye")
    