from turtle import *
begin_fill()
color('red', 'yellow')
shape ("turtle")
speed (1)
i = 2 
while i < 7:
   i = i+1
   a = 180- (( i - 2 ) * 180 / i)
   for j in range ( i):
      forward (100)
      left (a)
end_fill()
done ()