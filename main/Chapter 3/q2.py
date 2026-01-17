letter = '''Dear <|Name|>, 
            You are selected! 
            <|Date|>''' 
name = input("enter your name: ")
date = input("enter the today's date: ")
print(letter.replace("<|Name|>",name).replace("<|Date|>",date))