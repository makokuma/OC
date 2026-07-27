*main plotting

args = '/mnt/hail1/RRJ-Conv/sfc/2020/anl_sfc_LL.ctl'
args = args' 12Z29JUN2020'
args = args' prs'
args = args' pressfc'
args = args' shaded'
args = args' 34'
args = args' 36'
args = args' 122'
args = args' 126'
args = args' color_bar.gs'
args = args' test.png'
args = args' wind_vector'

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

LABNMAX = 6
LABNMIN = 3

GOODINT.1 = 5
GOODINT.2 = 4
GOODINT.3 = 2.5
GOODINT.4 = 2
GOODINT.5 = 1
GOODINT.6 = 0.5
GOODINT.7 = 0.25
GOODINT.8 = 0.2
GOODINT.9 = 0.1

i = 0
latRange = lat2 - lat1
yint = 5
while (i < 10)
  i = i + 1
  nl = latRange / GOODINT.i
  if (nl <= LABNMAX)
    if (nl >= LABNMIN)
      yint = GOODINT.i
      break
    endif
  endif
endwhile

i = 0
lonRange = lon2 - lon1
xint = 5
while (i < 10)
  i = i + 1
  nl = lonRange / GOODINT.i
  if (nl <= LABNMAX)
    if (nl >= LABNMIN)
      xint = GOODINT.i
      break
    endif
  endif
endwhile

say 'XINT='xint
say 'YINT='yint


'reinit'
'c'
'set grads off'
'set mpdset hires'
'set map 1 1 6'
'set grid off'
'set xlopts 1 3 0.14'
'set ylopts 1 3 0.14'
'set xlint 'xint
'set ylint 'yint

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

*main var(shaded)
'run 'colorgs' 'plotkey
'd pvar'
'cbarn'

*overlay var (position 12 onward, until an empty token)
i = 12
while (1)
  ov = subwrd(args, i)
  if (ov = '')
    break
  endif
  'run overlay.gs 'ov
  i = i + 1
endwhile

'printim 'outpng' png white -x 1600 -y 1200'
'quit'
