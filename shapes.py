# Helpful classes

import numpy as np

# Helper function for calculating dists
def dists(array):
  lens = []
  for i in range(len(array)):
    lens.append(np.linalg.norm(np.array(array[i][0])-
      np.array(array[i][1])))
  return lens


# I never remember if python needs getters & setters
# This is for the shape you want to cut
class Shape:
  def __init__(self, ls):
    self.edges = ls
    self.lengths = dists(ls)

  def get_edges(self):
    return self.edges

  def get_lengths(self):
    return self.lengths


# For the circles that are the point
class Circle:
  def __init__(self, vert, rad):
    self.vert = vert
    self.rad = rad

  def get_vertex(self):
    return self.vert

  def get_radius(self):
    return self.rad
