from openai import OpenAI
import os
import subprocess
client = OpenAI()

#asking user for a linux command

print ("""
 ██████╗  ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗██████╗    
 ██╔════╝ ██╔═══██╗████╗ ████║██╔══██╗████╗  ██║██╔══██╗    
 ██║  ███╗██║   ██║██╔████╔██║███████║██╔██╗ ██║██║  ██║ 
 ██║   ██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║██║  ██║ 
 ╚██████╔╝╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║██████╔╝ 
  ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝   
"""
)
print (f"""
Select your operation system(Input the number):
 1. Linux\MacOS
 2. Windows
       """)
Operation_System = input("Enter the number: ")

if Operation_System == "1":
    Operation_System = "Linux"
elif Operation_System == "2":
    Operation_System = "Windows"
else:
    print("Invalid input, please enter 1 for Linux or 2 for Windows")



command = input("Please describe the command you want: ")


#asking gpt to generate a linux command


completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": f"""
         
         From now on your a {Operation_System} command generator,
          do not answer with any more data but the command (please dont add the bash\powershell\cmd in the begginning)
        
          """},
        {"role": "user", "content": command},
    ]
)


answer = completion.choices[0].message.content

#run cmd command
print (answer)

user_approval = input("Do you want to run the command? (yes/no): ")
if user_approval == "yes":
    os.system(answer)
elif user_approval == "no":
    print("Ok, I will not run the command")
else:
    subprocess.run(["echo", "Invalid input, please enter yes or no"])
