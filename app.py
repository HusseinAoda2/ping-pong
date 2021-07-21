# استيراد وحدة السلاحف
import turtle

wind = turtle.Screen() #تهيئة الشاشة
wind.title("Ping Pong By Tech Makers") #عنوان النافذة
wind.bgcolor("black") #لون خلفية النافذة
wind.setup(width=800, height=600) #اضبط عرض النافذة وارتفاعها
wind.tracer(0) #توقف النافذة عن التحديث تلقائيًا

#madrab1
madrab1 = turtle.Turtle() # يميز جسم السلحفاة (الشكل) (shape)
madrab1.speed(0) # ضبط سرعة الحركة
madrab1.shape("square") # ضبط شكل الكائن
madrab1.color("blue") # ضبط لون الشكل
madrab1.shapesize(stretch_wid=5, stretch_len=1) # يمتد الشكل ليتناسب مع الحجم
madrab1.penup() # توقف الكائن عن رسم الخطوط
madrab1.goto(-350, 0) # ضبط موضع الكائن

#madrab2
madrab2 = turtle.Turtle()
madrab2.speed(0)
madrab2.shape("square")
madrab2.color("red")
madrab2.shapesize(stretch_wid=5, stretch_len=1)
madrab2.penup()
madrab2.goto(350, 0)

#ball 
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("#fff")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = 0.1

#score
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("#fff")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Player 1: 0 Player 2: 0", align="center", font=("Courier", 24, "normal"))

#functions
def madrab1_up():
    y = madrab1.ycor() #الحصول على إحداثيات (y) للمضرب1
    y += 20 #ضبط (y) لزيادة 20
    madrab1.sety(y) #ضبط (y) من المضرب1 على الإحداثيات (y) الجديد

def madrab1_down():
    y = madrab1.ycor()
    y -= 20 #ضبط (y) لإنقاص 20
    madrab1.sety(y)

def madrab2_up():
    y = madrab2.ycor()
    y += 20
    madrab2.sety(y)

def madrab2_down():
    y = madrab2.ycor()
    y -= 20
    madrab2.sety(y)

#keyboard bindings | الربط مع لوحة المفاتيح
wind.listen() #أخبر النافذة بتوقع إدخال لوحة المفاتيح
wind.onkeypress(madrab1_up, "w") #عند الضغط على (w) ، يتم استدعاء الوظيفة madrab1_up
wind.onkeypress(madrab1_down, "s")

wind.onkeypress(madrab2_up, "Up")
wind.onkeypress(madrab2_down, "Down")

#حلقة اللعبة الرئيسية
while True:
    wind.update() #يقوم بتحديث الشاشة في كل مرة يتم فيها تشغيل الحلقة

    #move the ball | حرك الكرة
    ball.setx(ball.xcor() + ball.dx) #ball starts at 0 and everytime loops run--- >+ 0.1 xaxis
    ball.sety(ball.ycor() + ball.dy) #ball starts at 0 and everytime loops run--- >+ 0.1 yaxis

    #border check , top border + 300px, bottom border - 300px, ball is 20px
    if ball.ycor() > 290: #if ball is at top border
        ball.sety(290) #set y coordinate + 20
        ball.dy *= -1 #reverse direction, making + 0.1--- >- 0.1

    if ball.ycor() < -290: #if ball is at bottom border
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390: #if ball is at right border
        ball.goto(0, 0) #return ball to center
        ball.dx *= -1 #reverse the x direction
        score1 += 1
        score.clear()
        score.write("Player 1: {} Player 2: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390: #if ball is at left border
        ball.goto(0, 0)
        ball.dx *= -1
        score2 += 1
        score.clear()
        score.write("Player 1: {} Player 2: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))

    #tasadom madrab and ball
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < madrab2.ycor() + 40 and ball.ycor() > madrab2.ycor() -40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < madrab1.ycor() + 40 and ball.ycor() > madrab1.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1








