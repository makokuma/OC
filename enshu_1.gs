function main(args)

*演習１
*reinit process
'reinit'
*'set display color white'
'c'
'set grads off'

* get args
say 'DEBUG args = 'args

outpng = subwrd(args, 1)

say 'DEBUG outpng = 'outpng

if (outpng = '')
  outpng = 'enshu1_rainarea.png'
endif

say 'DEBUG final outpng = 'outpng

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
say 'DEBUG before printim'
say 'DEBUG printim command = printim 'outpng' png white'

'printim 'outpng' png white'

say 'DEBUG after printim'

'quit'
