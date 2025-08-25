# Python code
wa={
"who are you!":"i am not a filthy useless thing","do you know anything?":"nah i am a filthy thing","what can you do for me":"nothing and nothing"
}

while True:
   question=input("ask me     anything! or type exit").lower()

   if question=="exit":
     print("thanks")
     break
   if question in wa:
     print(wa[question])
   else:
     print("idk this you know!!!")
