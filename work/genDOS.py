#semicircular dos
import numpy as np

nx = 2000   # number of frequency/energy points
D1 = 1      # narrow band
D2 = 2      # wide band
no_orb = 2  # number of orbitals
D=np.array([D1,D2],dtype = 'float')

# a gaussian function
def Semicircle(x,D):
   if np.abs(x)<= D:
      return (2/(np.pi*D))*np.sqrt(1-(x/D)**2)
   else:
      return 0
# Create the dos as a function of frequency/energy and spin
def dos(x,D):

   return Semicircle(x,D)


dx = 4*np.max(D)/nx
outf = open('dos.dat','w')
outf.write( str(nx) + '\n' )
for n in range(nx):
	x = -2*np.max(D) + n*dx
	outf.write( str(x) + '\t')
	for s in range(2):
		for m in range(no_orb):
			d= dos(x,D[m])
			outf.write( str(d) + '\t' )
	outf.write('\n')


outf.close()
