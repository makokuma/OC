*main plotting
function main(args)

*get args
ctlpath = subwrd(args, 1)
gtime   = subwrd(args, 2)
plotkey   = subwrd(args, 3)
varname = subwrd(args, 4)
gxout   = subwrd(args, 5)
lat1    = subwrd(args, 6)
lat2    = subwrd(args, 7)
lon1    = subwrd(args, 8)
lon2    = subwrd(args, 9)
colorgs    = subwrd(args, 10)
outpng  = subwrd(args, 11)

'reinit'
'c'
'set grads off'
'set mpdset hires'
'set map 1 1 6'
'set grid off'
'set xlopts 1 3 0.14'
'set ylopts 1 3 0.14'

'set parea 0.8 10.2 0.8 7.6'

'open 'ctlpath
'set time 'gtime
'set lat 'lat1' 'lat2
'set lon 'lon1' 'lon2
'set gxout 'gxout

*unit conversion (K->C, Pa->hPa)
if (plotkey = 'temp')
  'define pvar = 'varname'-273.15'
else

if (plotkey = 'prs')
  'define pvar = 'varname'/100'
else
*accum rein
if (plotkey = 'rain_accum_24h')
  'define pvar = sum('varname',t-23,t-0)'
else
  'define pvar = 'varname
endif
endif
endif

'run 'colorgs' 'plotkey
'd pvar'
'cbarn'
'printim 'outpng' png white -x 1600 -y 1200'
'quit'
