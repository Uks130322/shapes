import shape

sq1 = shape.Square(13)
sq2 = shape.Square(9)
t1 = shape.RightTriangle(2)
c1 = shape.Circle()
r1 = shape.Rectangle(9, 3)
r2 = shape.Rectangle(12, 7)
sq2.move(3, 4)
print(c1.radius)
print(shape.Square.total_area(), shape.Square.total_perimeter())
print(r2)
print(c1)
