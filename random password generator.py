import random
sample_sp="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()_+?~1234567890"
len=int(input("enter the length of the password "))
password="".join(random.sample(sample_sp,len))
print("Your password is ",password)