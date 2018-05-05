import turtle
#wn = turtle.Screen()
alex = turtle.Turtle()

def star(turtle):
    s = 4

    s0 = 4
    s1 = 360/(s0 * 2)

    for i in range(s0 * 2):
        turtle.left(s1)
        turtle.forward(s)
        turtle.backward(s)

    #turtle.forward(s)
    
    return ;

#star(alex);

def box(turtle, l):
    r = round(l/10)
    for i in range(4):
        for s in range(r):
            star(turtle);
            
            turtle.up();
            turtle.forward(10);
            turtle.down();
        
        turtle.left(90)
        
    return ;

def triangle(turtle, l):
    for i in range(l*l):
        turtle.up();
        turtle.forward(10);
        turtle.down();
        star(turtle);

    turtle.left(90 + 90/2);
    for i in range(l*l + 2):
        turtle.up();
        turtle.forward(10);
        turtle.down();
        star(turtle);

    turtle.left(90 + 90/2);
    for i in range(l*l - 1):
        turtle.up();
        turtle.forward(10);
        turtle.down();
        star(turtle);
    return ;

triangle(alex, 3);
