import time
def validate(password):
    pwd_rule = {'num': 0, 'upp': 0, 'low': 0, 'spe': 0}
    if password == '' or password == ' ':
        return False
    else:
        for x in password:
            if chr(32) < x < chr(128):
                if x.isalpha():
                    if x.islower():
                        pwd_rule['low'] += 1
                    elif x.isupper():
                        pwd_rule['upp'] += 1
                elif x.isdigit():
                    pwd_rule['num'] += 1
                else:
                    pwd_rule['spe'] += 1
        else:
            if not(0 in pwd_rule.values()):
                return True
        return False

print('# Password rules : \n-atleast one upper,\n-one lower,\n-one number and\n-one special character except space')
password = input('Enter the password : ')
t1 = time.perf_counter()
print(validate(password))
print(f'\nTime Taken : {time.perf_counter() - t1}')
