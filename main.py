# I want to calculate and draw the circle version
# of the solution to the fold and cut theorem
# (Not sure if it's even possible! but I'll try)
# TODO: turns out this whole thing is...
# significantly more complicated than originally anticipated
# For now I will try to solve it just for the very simple case.

# TODO: fix these assumptions:
  # User inputs valid edges
  # in a valid order

import numpy as np
import cv2 as cv
from shapes import *

def circles(shape):
  edges = shape.get_edges()

# Create np array with apprpriate dimensions
  # for the "variables" part of the matrix eq
  mat = np.zeros((len(edges), len(edges)))
  for i in range(0, len(edges)):
    if (i + 1) > len(edges) - 1:
      n = 0
    else:
      n = i + 1
    mat[i, i] = 1
    mat[i, n] = 1
  print(mat)
  print(shape.get_lengths())

  # Solve the matrix eq
  radii = np.matmul(np.array(shape.get_lengths()),
      np.linalg.pinv(mat))
  print(radii)
  
  # Create the circles
  circs = []
  for i in range(len(edges)):
    circs.append(Circle(edges[i][0], int(radii[i])))
  return circs 


def main():
  
  # Initialize the image
  img = np.full((500, 500, 3), 255, np.uint8)

  # TODO: get user input for shape
  shape = Shape([[(100,100), (100, 400)],
    [(100, 400), (400, 400)],
    [(400, 400), (400, 100)],
    [(400, 100), (100, 100)]])

  print(shape.get_edges())
  print(shape.get_lengths())

  # Calculate circles
  circs = circles(shape)

  # Draw circles
  for i in range(len(circs)):
    img = cv.circle(img, circs[i].get_vertex(),
        circs[i].get_radius(),
        (0, 0, 255), 2)

  # TODO: Calculate folds
  # TODO: draw folds
  for i in range(len(circs)):
    for j in range(i + 1, len(circs)):
      if i == j:
        pass
      else:
        img = cv.line(img, circs[i].get_vertex(), 
            circs[j].get_vertex(), (0, 255, 0), 2)

  # Print edges of desired shape
  edge = shape.get_edges()
  for i in range(len(edge)):
    img = cv.line(img, edge[i][0], edge[i][1], (0, 0, 0), 2)

  # Show the image
  cv.imshow('Test', img)
  cv.waitKey(0)

main()
