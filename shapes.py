# Helpful classes

import numpy as np

# Helper function for calculating dists
def dists(array):
  lens = []
  for i in range(len(array)):
    lens.append(np.linalg.norm(np.array(array[i][0])-
      np.array(array[i][1])))
  return lens


# This is for the original shape you want to cut
class Shape:
  def __init__(self, ls):
    self.edges = np.array(ls)
    self.lengths = dists(ls)
    self.vertices = self.edges[:,0]


# For the circles that are the point
class Circle:
  def __init__(self, vert, rad):
    self.vert = vert
    self.rad = rad
