
from klampt import *
#Klampt v0.6.x
#from klampt import visualization as vis
# from klampt import resource
#from klampt import robotcollide as collide
#from klampt.simulation import *
#from klampt.glrobotprogram import *
#Klampt v0.7.x
from klampt import vis 
from klampt.vis.glrobotprogram import *	#Per il simulatore
# from klampt.math import *
from klampt.model import collide
# from klampt.io import resource
from klampt.sim import *
# # from moving_base_control import *
import importlib
# import os
# import time
import sys
# import grasp_chose
#import an object dataset
from klampt.math import so3

world = WorldModel()
dataset = sys.argv[1] #which dataset will be use

# set di oggetti
objects_set = {
	'primo':['primo/poisson_mesh.stl']
	# 'secondo' : ['secondo/%n/poisson_mesh.stl']

	# 'ycb':['data/objects/ycb/%s/meshes/tsdf_mesh.stl','data/objects/ycb/%s/meshes/poisson_mesh.stl'],
	# 'apc2015':['data/objects/apc2015/%s/textured_meshes/optimized_tsdf_textured_mesh.ply']
}	

world.loadElement("terrains/plane.env")	#file che richiama la mesh del piano

# carico il robot
# moving_base_template_fn = 'moving_base_template.rob'
# robotname = "reflex_col"
# robot_files = {
# 	'reflex_col':'reflex_col.rob'
# }

# f = open(moving_base_template_fn,'r')
# pattern_2 = ''.join(f.readlines())
# f.close()
# f2 = open("temp.rob",'w')
# f2.write(pattern_2 % (robot_files[robotname],robotname))
# f2.close()
# world.loadElement("temp.rob")
world.loadElement("reflex_col.rob")
robot =  world.robot(world.numRobots()-1)
q = robot.getConfig()
q[0] = 2
q[1] = 2
q[2] = 2
q[3] = 0 #yaw
q[4] = 0 #pitch
q[5] = 180 #roll
robot.setConfig(q)


#now the simulation is launched
program = GLSimulationProgram(world)
sim = program.sim



for pattern in objects_set[dataset]:
	f = open(pattern,'r') #apro il file stl
	mesh_stl = [''.join(f.readlines())	]#leggi dentro. Ottengo tt i punti della mesh 
	f.close() #lo chiudo
	if world.loadElement(pattern) < 0:	#visualizzo mesh in simulazione
	 	print("no load")
	 	# continue
	# f2 = open('prova.txt','w')
	# f2.write(mesh_stl[0])
	# f2.close()


	

	#create a hand emulator from the given robot name
	module = importlib.import_module('plugins.'+robotname)
	#emulator takes the robot index (0), start link index (6), and start driver index (6)
	hand = module.HandEmulator(sim,0,6,6)
	sim.addEmulator(0,hand)
	import simple_controller
	R = so3.rotation([1,0,0],180*180/3.14)
	T = [0.1,0,0.2]
	print("make "), robot.link(5).getTransform() #fornisce rotazione e traslazione come se fosse un unico vettore

	p = (R,T) #concateno la matrice di rotazione e la traslazione creo s03
	print("p"), p

	# robot.link[5].setTransform(so3.rotation([1,0,0],180*180/3.14))
	sim.setController(robot,p )
























# #now the simulation is launched
# program = GLSimulationProgram(world)
# sim = program.sim




#this code manually updates the visualization
vis.add("world",world)
vis.show()
t0 = time.time()
while vis.shown():
	vis.lock()
	sim.simulate(0.01)
	sim.updateWorld()
	vis.unlock()
	t1 = time.time()
	time.sleep(max(0.01-(t1-t0),0.001))
	t0 = t1



