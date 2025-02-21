from openai import OpenAI
import os
import subprocess
client = OpenAI()

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
    exit()
command = input("Please describe the command you want: ")
command_amount = int(input("How many commands do you want to generate? (1-5): "))
if int(command_amount) > 5:
    print("Invalid input, please enter a number between 1 and 5")
    exit()
elif int(command_amount) < 1:
    print("Invalid input, please enter a number between 1 and 5")
    exit()

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": f"""
         
         From now on your a {Operation_System} command generator,
          do not answer with any more data but the command (please dont add the bash\powershell\cmd in the begginning)
          the amount of commands you want to generate is {command_amount}
          please generate the command in each line without adding any extra data or spaces between the commands
          """},
        {"role": "user", "content": command},
    ]
)


answer = completion.choices[0].message.content

commands = answer.split('\n')
print (f"Here are the commands that I have generated for you: {commands}")


user_approval = input("Do you want to run the command? (yes/no): ")

def Run_Command():
    if user_approval == "yes":
        os.system(commands[i])
    elif user_approval == "no":
        print("Ok, I will not run the command")
    else:
        print("Invalid input, please enter yes or no")
        exit()

i = 0
while i < command_amount:
    Run_Command()
    i += 1
    print(f"Command {i} has been executed")

    
