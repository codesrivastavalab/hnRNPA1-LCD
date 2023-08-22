import numpy as np

# Reading secondary structure information obtained from DSSP analysis

f = open("DSSP_secondary_structure_information.dat") 
ss = f.readlines()

# Reading the C-alpha dihedral angles

dhd = np.genfromtxt("C-alpha_dihedral_angles_list.txt")

# Scanning the angles to classify

d = open('Beta_kink_classification.txt','w')
for i in range(0,10001,1): # Range: (0, total number of frames)
	for j in range(1,68,1): # Range: (1, total number of residues-3)
		if ss[i][j-1] == "E" and ss[i][j] == "E" and ss[i][j+1] == "E" and ss[i][j+2] == "E":
			if dhd[i][j-1] > -20.0 and dhd[i][j-1] < 20.0: 
				print("1", end ="", file = d) # 1 --> beta kink 1
			elif dhd[i][j-1] >= 20.0 and dhd[i][j-1] < 40.0: 
				print("2", end ="", file = d) # 2 --> beta kink 2
			elif dhd[i][j-1] <= -20.0 and dhd[i][j-1] > -40.0:
				print("2", end ="", file = d) # 2 --> beta kink 2
			elif dhd[i][j-1] >= 40.0 and dhd[i][j-1] < 60.0: 
				print("3", end ="", file = d) # 3 --> beta kink 3
			elif dhd[i][j-1] <= -40.0 and dhd[i][j-1] > -60.0: 
				print("3", end ="", file = d) # 3 --> beta kink 3
			elif dhd[i][j-1] >= 60.0 and dhd[i][j-1] < 90.0: 
				print("4", end ="", file = d) # 4 --> beta kink 4
			elif dhd[i][j-1] <= -60.0 and dhd[i][j-1] > -90.0: 
				print("4", end ="", file = d) # 4 --> beta kink 4
			elif dhd[i][j-1] >= 90.0 and dhd[i][j-1] < 150.0: 
				print("5", end ="", file = d) # 5 --> beta twist
			elif dhd[i][j-1] <= -90.0 and dhd[i][j-1] > -150.0: 
				print("5", end ="", file = d) # 5 --> beta twist
			elif dhd[i][j-1] >= 150.0 and dhd[i][j-1] <= 180.0: 
				print("6", end ="", file = d) # 6 --> beta sheet
			elif dhd[i][j-1] <= -150.0 and dhd[i][j-1] >= -180.0: 
				print("6", end ="", file = d) # 6 --> beta sheet
		elif ss[i][j] == "E" and ss[i][j+1] == "E" and ss[i][j+1] != ss[i][j+2]:	#(the line to check for two consecutive E and exclude them)
			print("0", end ="", file = d)	
		elif ss[i][j] == "E" and ss[i][j+1] == "E" and ss[i][j+2] == "E": 	#(the line to check for two consecutive E and exclude them)
			print("0", end ="", file = d)	
		else: 
			print("0", end ="", file = d)
									
	print("", file = d)			
				
				
				
					
					
		



