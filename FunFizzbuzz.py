z = input('What is my favorite number to FizzBuzz? ')

z = int(z)

for x in list(range(1,z)):
    output = ""
    if(x % 3 == 0):
        output += 'Fizz'
    if(x % 5 == 0):
        output += 'Buzz'
    if(output == ""):
        output += str(x)

    print(output)
