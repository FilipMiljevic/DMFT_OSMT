#

set key samplen 2
set xlabel "i{/Symbol w}_n [eV]"
set ylabel "Im G(i{/Symbol w}_n) [1/eV]"

p \
'Gloc.dat'        u 1:3 w lp lt 1 lw 3 lc 1 ti 'G_{loc}', \
'Gimp.dat'        u 1:3 w lp lt 1 lw 3 lc 2 ti 'G_{imp}'
