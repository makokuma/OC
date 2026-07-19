*plot overlay var

function main(args)

overlay = subwrd(args, 1)

if (overlay = 'slp_contour')
  'set gxout contour'
  'set ccolor 1'
  'set cthick 5'
  'set clab on'
  'set cint 4'
  'd PRMSLmsl/100'
  return
endif

if (overlay = 'wind_vector')
  'set gxout vector'
  'set ccolor 1'
  'set arrscl 0.5 10'
  'd skip(UGRD10m,20,20);VGRD10m'
  return
endif

say 'WARNING: unknown overlay = 'overlay
return
