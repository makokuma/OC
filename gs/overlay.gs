*plot overlay var

function main(args)

overlay = subwrd(args, 1)
MAXDEGREE = 30
INTNMIN = 4


if (overlay = 'slp_contour')
  'set gxout contour'
  'set ccolor 1'
  'set cthick 5'
  'set clab on'
  'set cint 4'
  'd PRMSLmsl/100'
*  say 'slp_contour'
  return
endif

if (overlay = 'wind_vector')
  'q dim'
  xline = sublin(result, 2)
  yline = sublin(result, 3)
  xmin  = subwrd(xline, 6)
  xmax  = subwrd(xline, 8)
  ymin  = subwrd(yline, 6)
  ymax  = subwrd(yline, 8)
  xrange = xmax - xmin
  yrange = ymax - ymin
  if (xrange > yrange)
    widerRange = xrange
  else
    widerRange = yrange
  endif
  vint = math_nint(25 * widerRange / MAXDEGREE)
  if (vint < INTNMIN)
    vint = INTNMIN
  endif
*  vint = MAXDEGREE
*  say 'wind_vector'
*  say 'XRANGE='xrange
*  say 'YRANGE='yrange
*  say 'WIDER_RANGE='widerRange
*  say 'VINT='vint

  'set gxout vector'
  'set ccolor 1'
  'set arrscl 0.5 10'
  'd skip(UGRD10m,'vint','vint');VGRD10m'
  return
endif

say 'WARNING: unknown overlay = 'overlay
return
