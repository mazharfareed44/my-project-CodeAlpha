# Here we are to creat a sipmle chatbot
#   we will create function
def chatbot():
    print("Welcome to Chatbot")
# Now we will use while loop  to take user input help user to ask again and again
    while True:
     user_input=input("You: ").capitalize()
# Here conditions are given to make decision
     if user_input=="Hello":
        print("Bot: HI")
     elif user_input=="How are you":
        print("Bot: Fine and You ?")
     elif user_input=="At which institute are you doing your intership":
        print("Bot: at CodeAlpha")
     elif user_input=="In which program":
        print("Bot: Pyhton Programming")
     elif user_input=="OK Thanks ,Bye":
        print("Bot ok bye")
# here  is used break function  to stop loop
        break
     else:
        print("Bot: Sorry I dont uderstand") #When given condition out of scope
#Function is called
chatbot()
