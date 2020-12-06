#python 3.7
import voice_to_text as vt
#take in a passowrd and prompt a 2nd factor of verification
vt.voice_out("please create a password ")
new_pw = input("please create a password ")

vt.voice_out("New password created successfully")
print("New password created successfully")

vt.voice_out("Please create a security passphrase")
passphrase = input("Please create a security passphrase: ")

vt.voice_out("New passphrase created successfully")
print('New passphrase created successfully')
vt.voice_out("Please enter password")
pw = input("Please enter password: ")

vt.voice_out("Please follow instructions for two factor voice authentication")

if pw == new_pw:
    vt.do_stuff(passphrase)    