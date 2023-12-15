sigma = 0.0007
inf = open('Gloc.dat','r')
no_orb = 1
useorb = 0

outf = open('gf.dat','w')
for line in inf:
	data = [float(x) for x in line.split()]
	orb_index=2*useorb*no_orb + 2*useorb
	outf.write( str(data[0])+ '\t' + str( (data[1+orb_index]) ) + '\t'  + str(sigma) + '\t' \
                                  + str( (data[2+orb_index]) ) + '\t'  + str(sigma) + '\n' )

outf.close()
inf.close()
