#@Author : Sudip Mitra
def replace_email(email, old_domain, new_domain):
  if "@" + old_domain in email :
    i = email.index("@" + old_domain)
    updated_mail = email[:i] + "@" + new_domain
    return updated_mail

old_domain = input("Enter old domain : ")
new_domain = input("Enter new domain : ")
for i in range(int(input("Test Cases : "))):
  email = input("Enter email : ")
  print(replace_email(email, old_domain, new_domain))
