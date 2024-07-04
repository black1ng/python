import matplotlib.pyplot as mp
x = [a//10 for a in range(0, 200, 1)]
y = [1/(10 + a**3) for a in x]
mp.plot(x, y)
mp.xlabel('Ось х')
mp.ylabel('Ось y')
mp.title("y(x)=1/(10+x^3)")
mp.show()