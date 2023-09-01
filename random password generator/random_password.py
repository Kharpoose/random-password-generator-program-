import random
import string


characters = list(string.ascii_letters + string.digits + "!@%&^()*") 


def password_generator():
      password_lenght = int(input("How long would you like your password to be ? "))
      
      random.shuffle(characters)
      
      password = []
      
      for x in range(password_lenght):
          password.append(random.choice(characters))
          
      random.shuffle(password)
      
      
      password = "".join(password)
      
      print(password)      
      
                        
            
y = input("Are you want to create new password? yes/no ").lower()

if y == "yes":
      password_generator()
                        
elif y == "no":
      print("ok good bye") 
      quit()                       
else:
      print("Invalid input detected viyu viyu viyu eror eror !!!")
      quit()