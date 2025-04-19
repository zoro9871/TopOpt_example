import numpy as np
import trimesh
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

from skimage import measure


### load structure data using np.loadtxt
op_str = np.loadtxt('results/op_structure.txt')

### preprocessing the data

## 1. write down the purpose of the following sippet in your report
th = 0.5 # set the density threshold
op_str[0,op_str[0,:]>th]=th
op_str[-1,op_str[-1,:]>th]=th
op_str[op_str[:,0]>th,0]=th
op_str[op_str[:,-1]>th,-1]=th

## 2. write down the purpose of the following sippet in your report
op_str_bound = np.where(op_str > th, th, 0)
op_str_middle = np.tile(op_str[:,:,np.newaxis], (1,1,3))
op_str_3D = np.concatenate((op_str_bound[:,:,np.newaxis],op_str_middle,op_str_bound[:,:,np.newaxis]),axis=2)

## 3. write down the purpose of the following sippet in your report
verts, faces, normals, values = measure.marching_cubes(op_str_3D, th)

# Display resulting triangular mesh using Matplotlib. 
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')

mesh = Poly3DCollection(verts[faces])
mesh.set_edgecolor('k')
ax.add_collection3d(mesh)
ax.set_xlim(0, 30)  
ax.set_ylim(0, 90)  
ax.set_zlim(0, 5) 
ax.set_aspect('equal', adjustable='box')
plt.tight_layout()
plt.show()
fig.savefig("./results/final_structure_mesh.jpg")

mesh = trimesh.Trimesh(vertices=verts, faces=faces)
mesh.export("./results/final_structure.stl")
