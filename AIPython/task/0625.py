# 성적
kor=70
eng=90
math=100
avg=(kor+eng+math)/3

print('-------------')
print('국어 = ', kor)
print('영어 = ', eng )
print('수학 = ', math)
print()
print('=> 평균 : ', avg)
print('-------------')


# 다각형
import turtle

pen = turtle.Turtle()
pen.shape('turtle')
pen.penup()
pen.goto(100, 200)
pen.pendown()

for n in range(3) :
    pen.forwaro(100)
    pen.right(120)


pen.penup()
pen.goto(-200, 200)
pen.pendown()

for n in range(5):
    pen.forward(130)
    pen.right(72)


#-------------------

pen2 = turtle.Turtle()
pen2.shape('circle')
pen2.color('red')

pen2.penup()
pen2.goto(200, -100)
pen2.pendown()

for n in range(5) :
    pen2.forward(100)
    pen2.right(144)
