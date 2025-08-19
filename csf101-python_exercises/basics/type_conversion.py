age = 18
age_str = str(age)
message = "I am " + age_str + " years old"
print (message)
#converting string to integer
num_str = "42"
num_int = int(num_str)
print (num_int)
#trying to convert non numeric string into integer
non_num_str = "hello"
try :
    non_num_int = int(non_num_str)
    print(non_num_int)
except ValueError as e:
    print(f"Error: {e}")