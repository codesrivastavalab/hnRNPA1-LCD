import numpy as np


# Dihedral angle calculation function
def dihed_angle(V,k):
	vec_1 = V[k+1] - V[k]
	vec_2 = V[k+2] - V[k+1]
	vec_3 = V[k+3] - V[k+2]
	
	# Calculate normals
	perp_1 = np.cross(vec_1,vec_2)
	perp_2 = np.cross(vec_2,vec_3)
    	
    	
	if np.linalg.norm(perp_1) == 0.0 or np.linalg.norm(perp_2) == 0.0:
		return(np.nan)
    		
    	# Calculate unit vector
	
	unv_1 = perp_1/np.linalg.norm(perp_1)
	unv_2 = perp_2/np.linalg.norm(perp_2)
    		
    		
    	# Calculating dot product and inverse to obtain the dihedral angle
     
	angle = np.dot(unv_1, unv_2)
	dhd = np.rad2deg(np.arccos(angle))
	
	
	
	if np.dot((-unv_1),vec_3)< 0.0:
		return(dhd)	
	else:
		dhd = -dhd
		if dhd == -180.0: dhd = 180.0
		return(dhd)	 
		
			
    	
# Data loading (User input)

# Load your protein trajectory consisting only C-alpha atoms
data_2 = np.genfromtxt("Only_C-alpha_coordinates.txt")

# Reshaping

# Shape of the array: (total numbe of amino acid residues times total number of trajectory frames, 3)
V = np.reshape(data_2, (710071,3))
   	
# Calling the function
f = open("C_alpha_dihedral_angles_list.txt",'w') # All the C-alpha dihedral angles get saved in this file

for i in range(0,10001,1): # Range: (0, total number of frames,1)
	for j in range(0,68,1): # Range: (0, total number of residues-3)
		k = 71*i + j # k = total number of residues*i + j	
		print(dihed_angle(V,k), end = " ", file=f)
	print("", file =f)
		
		    	
    	
    	
    	
    	
    	
    	
    		

