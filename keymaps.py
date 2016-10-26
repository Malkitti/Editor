#/usr/bin/env python
# coding: utf-8
## keymaps.py


###############################################################################################
##					Copyright 2013 IITMK
##
##	This file is part of എഴുത്താണി  : A Malayalam Phonetic Text Editor for GNU/Linux Systems
##
##      എഴുത്താണി  is FREE software; you can redistribute it and/or modify
##      it under the terms of the GNU General Public License as published by
##      the Free Software Foundation; either version 3 of the License, or
##      (at your option) any later version.
##       
##      This program is distributed in the hope that it will be useful,
##      but WITHOUT ANY WARRANTY; without even the implied warranty of
##      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  
##      See the GNU General Public License for more details.
##       
##      You should have received a copy of the GNU General Public License
##      along with എഴുത്താണി . If not, see <http://www.gnu.org/licenses/>.
###############################################################################################


''' Keymaps: Lists the keymaps for use with engine.py '''


keymap = {}

keymap['0'] = '൦';
keymap['1'] = '൧';
keymap['2'] = '൨';
keymap['3'] = '൩';
keymap['4'] = 'ർ';
keymap['5'] = '൫';
keymap['6'] = '൬';
keymap['7'] = '൭';
keymap['8'] = '൮';
keymap['9'] = 'ൻ';

keymap['a'] = 'അ';
keymap['A'] = 'ആ';
keymap['i'] = 'ഇ';
keymap['I'] = 'ഈ';
keymap['u'] = 'ഉ';
keymap['U'] = 'ഊ';
keymap['e'] = 'എ';
keymap['E'] = 'ഏ';
keymap['z'] = 'ഐ';
keymap['o'] = 'ഒ';
keymap['O'] = 'ഓ';
keymap['Y'] = 'ഔ';
keymap['x'] = 'ഋ'; 


keymap['acihnam'] = '';
keymap['Acihnam'] = 'ാ';
keymap['icihnam'] = 'ി';
keymap['Icihnam'] = 'ീ';
keymap['ucihnam'] = 'ു';
keymap['Ucihnam'] = 'ൂ';
keymap['xcihnam'] = 'ൃ'
keymap['ecihnam'] = 'െ';
keymap['Ecihnam'] = 'േ';
keymap['ocihnam'] = 'ൊ';
keymap['Ocihnam'] = 'ോ';
keymap['q'] = 'ൗ';
keymap['Q']='ൈ';
keymap['M'] = 'ം';
keymap['H'] = 'ഃ'; 
#keymap['Xcihnam'] = 'ൃ';
#കഖഗഘങചഛജഝഞടഠഡഢണ
#keymap['hasanta'] = '্';

keymap['k'] = 'ക';
keymap['kh'] = 'ഖ';
keymap['g'] = 'ഗ';
keymap['gh'] = 'ഘ';
keymap['G'] = 'ങ';
keymap['c'] = 'ച';
keymap['ch'] = 'ഛ';
keymap['C'] = 'ഛ';
keymap['j'] = 'ജ';
keymap['jh'] = 'ഝ';
keymap['J'] = 'ഞ';
keymap['t'] = 'ട';
keymap['th'] = 'ഠ';
keymap['d'] = 'ഡ';
keymap['dh'] = 'ഢ';
keymap['n'] = 'ന';  
keymap['T'] = 'ത';     #തഥദധനപഫബഭമയരലവശഷസഹളഴറ
keymap['Th'] = 'ഥ';
keymap['D'] = 'ദ';
keymap['Dh'] = 'ധ';
keymap['N'] = 'ണ';
keymap['p'] = 'പ';
keymap['ph'] = 'ഫ';
keymap['b'] = 'ബ';
keymap['bh'] = 'ഭ';
keymap['m'] = 'മ';
keymap['y'] = 'യ';
keymap['r'] = 'ര';
keymap['l'] = 'ല';
keymap['v'] = 'വ';
keymap['sh'] = 'ഷ';
keymap['S'] = 'സ';
keymap['s'] = 'ശ';
keymap['h'] = 'ഹ';
keymap['L']='ള';
keymap['z']='ഴ';

keymap['^'] = '്';

keymap['N~'] = 'ൺ';    		#ൽൾർൺൻ
keymap['n~'] = 'ൻ';
keymap['r~'] = 'ർ';
keymap['l~'] = 'ൽ';
keymap['l^~'] = 'ൾ';

#keymap['q']='ൗ';

keymap['R'] = 'റ';

#keymap['Y']='';
keymap['W'] = ''
keymap['Z'] = ''
keymap['P'] = ''
keymap['F'] = ''
keymap['K'] = ''
keymap['V'] = ''
keymap['B'] = ''
keymap['X']=''
#keymap['Q']=''

keymap['|'] = '।'; # daanri
#keymap['.'] = '।'; # daanri
keymap['#'] = '‌'; # zero-width non-joiner ?
#keymap['`'] = '‌`'; # <same> Useful to 'force' a hasanta between letters
