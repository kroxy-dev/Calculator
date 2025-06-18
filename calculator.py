from pytest import raises
def main():
    operations=['add','subtract','multiply','divide']
    a=get_a()
    b=get_b()
    while True:
        operation=input('select your operation')
        if operation in operations:
            break
    if operation=='add':
        add(a,b)
    elif operation=='subtract':
        subtract(a,b)
    elif operation=='multiply':
        multiply(a,b)
    elif operation=='divide':
        divide(a,b)


#adds a to b
def add(a,b):
    return a+b

#subtracts b from a
def subtract(a,b):
    return a-b 

#multiplies a by b
def multiply(a,b):
    return a*b 

#divides a by b
def divide (a,b):
    if b==0:
        raise ZeroDivisionError("You can't divide by 0")
    return a/b 

#gets user input for a
def get_a():
    while True:
        try :
            a=int(input('type a'))
        except:
            pass
        else:
            break 

#gets user input for b
def get_b():
    while True:
        try :
            b=int(input('type b'))
        except:
            pass
        else:
            break 

if __name__=='__main__ ':
    main()
