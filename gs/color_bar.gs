*colorbar function
function main(args)

plotkey = subwrd(args, 1)

if (plotkey = 'rain')
  'set gxout shaded'
  'set clevs 1 5 10 20 30 50 80 '

*color of JMA
  'set rgb 31 242 242 255'
  'set rgb 32 160 210 255'
  'set rgb 33 33 140 255'
  'set rgb 34 0 65 255'
  'set rgb 35 250 245 0'
  'set rgb 36 255 153 0'
  'set rgb 37 255 40 0'
  'set rgb 38 180 0 104'

  'set ccols 31 32 33 34 35 36 37 38 '
  return
endif
