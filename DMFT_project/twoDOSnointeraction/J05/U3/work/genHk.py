import numpy as np
np.set_printoptions(precision=4,suppress=True)
# Generate the Hamiltonian in k-space (only 2-dimensions)

nkx = 40    # Number of k-points along kx
nky = 40    # Number of k-points along ky
no_orb = 2  # number of orbitals

# Define the Hamiltonian matrix at each k and spin
def Hk(s,kx,ky):
	H = np.zeros((no_orb,no_orb),dtype=complex)

	if (s==0):
		H[0,0] = -2*np.cos(kx) -2*np.cos(ky)
		H[1,1] = -2*np.cos(kx) -2*np.cos(ky) + 0.5
	else:
		H[0,0] = -2*np.cos(kx) -2*np.cos(ky)
		H[1,1] = -2*np.cos(kx) -2*np.cos(ky) + 0.5

	return H

outf = open('Hk.dat','w')
outf.write( str(nkx) + '\t' + str(nky) + '\n' )
Hloc = np.zeros((2,no_orb,no_orb),dtype=complex)
for ikx in range(nkx):
	for iky in range(nky):
		kx = ikx*2*np.pi/nkx
		ky = iky*2*np.pi/nky
		outf.write( str(kx) + '\t' + str(ky) + '\t' )

		for s in range(2):
			H = Hk(s,kx,ky)
			for m1 in range(no_orb):
				for m2 in range(no_orb):
					outf.write( str(H[m1,m2].real) + '\t' + str(H[m1,m2].imag) + '\t' )
			Hloc[s,:,:] += H/(nkx*nky)
		outf.write('\n')
outf.close()

for s in range(2):
	print 'Your local Hamiltonian for spin=',s,':\n',Hloc[s,:,:]

	nondiag = 0
	for m1 in range(no_orb):
		for m2 in range(no_orb):
			if ( m1!=m2 and  abs(Hloc[s,m1,m2])>0.001 ):
				nondiag = 1
	if (nondiag==1):
		print 'WARNING: Your local Hamiltonian is not diagonal! Is this what you want?'


