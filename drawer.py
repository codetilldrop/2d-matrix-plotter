from parser import matrice_plot_data
import turtle
import Tkinter

pen = turtle.Pen()
coordinates_to_plot = []

for matrix in matrice_plot_data:
  for coordinate_data in matrix:
    valid_coordinate = coordinate_data[0]
    coordinates = coordinate_data[1]
    
    if valid_coordinate == 1:
      x_val = coordinates[0] * 30
      y_val = coordinates[1] * 30
      coordinates_to_plot.append([x_val, y_val])

start = coordinates_to_plot[0]

right_side = coordinates_to_plot[len(coordinates_to_plot)//2:]
right_side = right_side[::-1]

coordinates_to_plot = coordinates_to_plot[:len(coordinates_to_plot)//2] + right_side
pen.penup()

for cooridinate in coordinates_to_plot:
  pen.setpos(cooridinate[0], cooridinate[1])
  pen.pendown()

pen.setpos(start[0], start[1])

Tkinter.mainloop()
