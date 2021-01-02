

def fizzBuzz(n):
    black = []
    if  (n%3 == 0) and  (n%5 != 0):
        black = black.append("Fizz")
    elif  (n%5 == 0) and  (n%3 != 0):
        black = black.append("Buzz")
    elif  (n%3 == 0) and  (n%5 == 0):
        black = black.append("FizzBuzz")
    else:
        black = black.append(f"{i}")
    return black

if __name__ == '__main__':
    p = int(input().strip())
    i = 1
    
    while i <= p:
        fizzBuzz(i)
        i += 1
    
