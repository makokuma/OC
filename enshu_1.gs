*演習１
*reinit process
'reinit'
*'set display color white'
'c'
'set grads off'

*get args
*png name

outpng = subwrd(args, 1)

if (outpng = '')
  outpng = 'enshu1_rainarea.png'
endif

*setting map option
'set mpdset hires'


*open RRJ-Conv file
'open /mnt/hail1/RRJ-Conv/sfc/2020/fcst_sfc_LL.ctl'

*setting time
'set time 09z04Jul2020'

*set area
'set lat 34 38'
'set lon 135 140'

*setting drawing
'set gxout shaded'
'd apcpsfc'

'cbarn'

*save as png
*'printim enshu1.png'
'printim 'outpng' png white'

'quit'
