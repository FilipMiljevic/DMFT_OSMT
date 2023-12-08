#

set key samplen 2
set xlabel "{/Symbol w} [eV]"
set ylabel "A({/Symbol w})"
set yzeroaxis lt 1 lw 1 lc 7
set xrange [-7:7]

p \
'maxent_input.out.avspec.dat'                          u 1:2 w l lt 1 lw 3 lc 1 ti 'DMFT'
