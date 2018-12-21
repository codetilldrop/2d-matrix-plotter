from parser import matrice_plot_data
import turtle
import Tkinter

pen = turtle.Pen()
pen.penup()
pen.fillcolor("black")
coordinates_to_plot = []

for matrix in matrice_plot_data:
  for coordinate_data in matrix:
    valid_coordinate = coordinate_data[0]
    coordinates = coordinate_data[1]
    
    if valid_coordinate == 1:
      x_val = coordinates[0] * 100
      y_val = coordinates[1] * 100
      coordinates_to_plot.append([x_val, y_val])

pen.fill(True)
pen.begin_fill()
start = coordinates_to_plot[0]
finish = coordinates_to_plot[-1]

coordinates_to_plot.pop(0)
coordinates_to_plot.pop(-1)

pen.setpos(start[0], start[1])
pen.pendown()

for coordinate in coordinates_to_plot:
  pen.setpos(coordinate[0], coordinate[1]) 
  pen.penup()
  pen.setpos(start[0], start[1])
  pen.pendown()


pen.penup()
pen.setpos(finish[0], finish[1])
pen.pendown()

for coordinate in coordinates_to_plot:
  pen.setpos(coordinate[0], coordinate[1]) 
  pen.penup()
  pen.setpos(finish[0], finish[1])
  pen.pendown()

pen.end_fill()



Tkinter.mainloop()
