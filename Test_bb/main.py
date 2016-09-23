import Exampletest_dany_bb	#importo funzione delle bb
# from klampt import vis 
# from klampt.vis.glrobotprogram import *	#Per il simulatore
# from openmesh import *
from stl import mesh
import numpy as np

your_mesh = mesh.Mesh.from_file('banana.stl')
# point = np.array([[x[i], y[i], z[i]] for i in range(len(your_mesh.points))])
# print("points"), point
# for i in range(0,len(your_mesh.points)): 
# for i in range(0,3): 
# 	print("i"), i	
#  	print("point"), your_mesh.points[i]

# print("di nuovo"), your_mesh.points
print("len(your_mesh.points)"),len(your_mesh.points)

print("mesh.data x"),your_mesh.x #vettori di 3 elementi
print("mesh.data y"),your_mesh.y.size
print("mesh.data z"),your_mesh.z.size

box = Exampletest_dany_bb.Box(10)

# mesh = TriMesh()
# read_mesh(mesh, "poisson_mesh.stl")
# print("mesh n point"), mesh.Point

x = []; y= [] ; z = []
for i in range(0,len(your_mesh.points)):
	for j in range(0,3):
		x.append(your_mesh.x[i][j])
		y.append(your_mesh.y[i][j])
		z.append(your_mesh.z[i][j])

# box.SetPoint ( i, your_mesh.x[i][j], your_mesh.y[i][j], your_mesh.z[i][j] )
	# print("box"),box

