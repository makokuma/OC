*main plotting
function main(args)

*get args
ctlpath = subwrd(args, 1)
gtime   = subwrd(args, 2)
varname = subwrd(args, 3)
gxout   = subwrd(args, 4)
lat1    = subwrd(args, 5)
lat2    = subwrd(args, 6)
lon1    = subwrd(args, 7)
lon2    = subwrd(args, 8)
outpng  = subwrd(args, 9)

'reinit'
'c'
'set grads off'
'set mpdset hires'

'open 'ctlpath
'set time 'gtime
'set lat 'lat1' 'lat2
'set lon 'lon1' 'lon2
'set gxout 'gxout
'd 'varname
'cbarn'
'printim 'outpng' png white'
'quit'
