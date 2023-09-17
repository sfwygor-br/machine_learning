from matplotlib import pyplot as plt

def line(slope,intercept):
    x = [1,3,5]
    y = []
    for i in x:
        yy = slope*i + intercept
        y.append(yy)
    plt.plot(x,y)



line(2,100) #blue line
line(17,51) #orange 
line(4,28) # green
line(-180,90) #red
plt.plot(5, -10, 'o', color='purple');
plt.show()


