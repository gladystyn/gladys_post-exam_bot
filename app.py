print("Title of program: Post-exam bot")
print()
while True:
  description = input("Could you describe how you feel in a sentence?")

  list_of_words = description.split()

  feelings_list = []
  encouragement_list = []
  counter = 0
  
  for each_word in list_of_words:
    
    if each_word == "bored":
      feelings_list.append("bored")
      encouragement_list.append("you can always find something fun to do")
      counter += 1
    if each_word == "happy":
      feelings_list.append("happy")
      encouragement_list.append("you should not be overly-proud and must always work hard")
      counter += 1
    if each_word == "angry":
      feelings_list.append("angry")
      encouragement_list.append("you can always improve yourself as long as you believe in yourself")
      counter += 1
    if each_word == "sad":
      feelings_list.append("sad")
      encouragement_list.append("you don't have to worry, just try again")
      counter += 1    
    if each_word == "worried":
      feelings_list.append("worried")
      encouragement_list.append("there's always a tomorrow for you to work harder")
      counter += 1
  if counter == 0:
    
      output = "Sorry I don't really understand. Please use different words?"

  elif counter == 1:
    
      output = "It seems that you are feeling quite " + feelings_list[0] + ". However, do remember that "+ encouragement_list[0] + "! Hope you feel better :)"  

  else:

    feelings = ""    
    for i in range(len(feelings_list)-1):
      feelings += feelings_list[i] + ", "
    feelings += "and " + feelings_list[-1]
    
    encouragement = ""    
    for j in range(len(encouragement_list)-1):
      encouragement += encouragement_list[i] + ", "
    encouragement += "and " + encouragement_list[-1]

    output = "It seems that you are feeling quite " + feelings + ". Please always remember "+ encouragement + "! Hope you feel better :)"

  print()
  print(output)
  print()
