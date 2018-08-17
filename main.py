# I want to calculate and draw the circle version
# of the solution to the fold and cut theorem

# TODO: fix these assumptions:
  # User inputs valid edges
  # in a valid order

import numpy as np
import cv2 as cv
import networkx as nx
from shapes import *

def circles(shape):

  edges = shape.edges

  #### STEP ONE #######
  # Place a disk at each vertex v 
  # with radius 1/2 dist from v to nearest edge
  # of PR not incident to v
  #vertices = shape.vertices.append(

  # Create np array with apprpriate dimensions
  # for the "variables" part of the matrix eq
  # TODO: i think this is not quite right
  # TODO: please review
  mat = np.zeros((len(edges), len(edges)))
  for i in range(0, len(edges)):
    if (i + 1) > len(edges) - 1:
      n = 0
    else:
      n = i + 1
    mat[i, i] = 1
    mat[i, n] = 1
  print(mat)
  print(shape.lengths)

  # Solve the matrix eq
  radii = np.matmul(np.array(shape.lengths, 
      np.linalg.pinv(mat)))
  print(radii)
  
  # Create the (initial) disks
  circs = []
  for i in range(len(edges)):
    circs.append(Circle(edges[i][0], int(radii[i])))

  ##### STEP TWO #######
  # Place a new vertex at each intersection
  # of disk boundary and PR

  ##### STEP THREE #######
  # For edges of updated PR not covered:
  # calculate the disk where the edge is its diameter
  # While there is at least 1 crowded edge:
  # add midpoint of crowded edges
  # and update graph

  ##### STEP FOUR #########
  # the voronoi step
  # TODO: we'll get here later

  return circs 


def main():

  dim = 500
  
  # Initialize the image
  img = np.full((dim, dim, 3), 255, np.uint8)

  # TODO: get user input for shape
  shape = Shape([[(100,100), (100, 400)],
    [(100, 400), (400, 400)],
    [(400, 400), (400, 100)],
    [(400, 100), (100, 100)]])

  shape = Shape([[(200,250), (370, 450)],
    [(370, 450), (30, 300)],
    [(30, 300), (200, 250)]])

  print(shape.edges)
  print(shape.lengths)

  # Initialize the mathy graph part
  graph = nx.Graph()
  graph.add_edges_from(shape.edges)

  # Calculate circles
  circs = circles(shape)

  # Draw circles
  for i in range(len(circs)):
    img = cv.circle(img, circs[i].vertex,
        circs[i].radius,
        (0, 0, 255), 2)

  # TODO: Calculate folds
  # TODO: draw folds
  for i in range(len(circs)):
    for j in range(i + 1, len(circs)):
      if i == j:
        pass
      else:
        img = cv.line(img, circs[i].vertex,
            circs[j].vertex, (0, 255, 0), 2)

  # Print edges of desired shape
  edge = shape.edges
  for i in range(len(edge)):
    img = cv.line(img, edge[i][0], edge[i][1], (0, 0, 0), 2)

  # Show the image
  cv.imshow('Test', img)
  cv.waitKey(0)

main()
