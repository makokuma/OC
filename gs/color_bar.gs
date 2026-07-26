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
endif

if (plotkey = 'rain_accum_3h')
  'set gxout shaded'
  'set clevs 1 5 10 40 80 120 200 '

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
endif
if (plotkey = 'rain_accum_6h')
  'set gxout shaded'
  'set clevs 1 5 50 100 150 200 300 '

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
endif
if (plotkey = 'rain_accum_24h')
  'set gxout shaded'
  'set clevs 1 50 100 200 300 500 800 '

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
endif

if (plotkey = 'temp')
  'set gxout shaded'
  'set clevs -10 -5 0 5 10 15 20 25 30 35 40'

*color of JMA
  'set rgb 31 0 0 112'
  'set rgb 32 0 32 128'
  'set rgb 33 0 65 255'
  'set rgb 34 0 150 255'
  'set rgb 35 185 235 255'
  'set rgb 36 255 255 240'
  'set rgb 37 255 255 150'
  'set rgb 38 250 245 0'
  'set rgb 39 255 153 0'
  'set rgb 40 255 40 0'
  'set rgb 41 180 0 104'
  'set rgb 42 145 0 83'

  'set ccols 31 32 33 34 35 36 37 38 39 40 41 42 '
  return
endif

if (plotkey = 'prs')
  'set gxout shaded'
  'set clevs 960 970 980 990 1000 1010 1020 1030 1040 '

*RdYlBu (low=red, high=blue)
  'set rgb 31 165 0 38'
  'set rgb 32 215 48 39'
  'set rgb 33 244 109 67'
  'set rgb 34 253 174 97'
  'set rgb 35 254 224 144'
  'set rgb 36 224 243 248'
  'set rgb 37 171 217 233'
  'set rgb 38 116 173 209'
  'set rgb 39 69 117 180'
  'set rgb 40 49 54 149'

  'set ccols 31 32 33 34 35 36 37 38 39 40 '
  return
endif
