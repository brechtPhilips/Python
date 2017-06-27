import  time
import os
from datetime import datetime as dt


# --Window users--
# if you want the file to run when the pc starts
#  change .py to .pyw and add it to timescheduler,


#--Mac users--
# open terminal and enter sudo crontab -e
# add this line to the file: @reboot python3 "the path to this file without the quotes"



# Look which system is being used
if os.name == 'nt':
    # Define path windows to hosts file
    host_path = r"C:Windows\System32\drivers\etc\hosts"
else:
    # Define path mac/linux to hosts file
    host_path = "/etc/hosts"

# Define redirect ip adress
redirect = "127.0.0.1"

# Setup a list of websites u want to block
websites_list = ["www.facebook.com", "facebook.com", "www.youtube.com", "youtube.com"]
while True:
    if 8 < dt.now().hour < 16:
        print("Working hours...")
        with open(host_path, 'r+') as file:
            content = file.read()
            for website in websites_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
    else:
        print("Fun hours...")
        with open(host_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in websites_list):
                    file.write(line)
            file.truncate()

    time.sleep(5)
