#

set key samplen 2
set xlabel "i{/Symbol w}_n [eV]"
set ylabel "Im {/Symbol S}(i{/Symbol w}_n) [eV]"

p \
'/home/dmft-user/Prog/dmft_input/bethe/Sigma.dat' u 1:3 w lp lt 2 lw 4 lc 7 ti 'reference', \
'Sigma.dat'                                       u 1:3 w lp lt 1 lw 3 lc 1 ti 'DMFT'
