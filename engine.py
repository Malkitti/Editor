#/usr/bin/env python
# coding: utf-8
## engine.py


###############################################################################################
##					
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



'''' Engine: This is where the conversion get's done! '''


import string
from keymaps import keymap  ## load the keymaps



def mreplace(s, prv, nxt):
	if prv in s:
		s = s.replace(prv, nxt)
		return s
	else:
		return s
	

def roman2mal(intext):
		
	ans = ''
	
	## formating the input string to a suitable form for internal use!
	
	intext = mreplace(intext, 'aaY', 'w'); 

	
#	intext = mreplace(intext, 'tw', 'W'); 
	intext = mreplace(intext, 'ng', 'M');  
	intext = mreplace(intext, 'nG', 'G'); 
	intext = mreplace(intext, 'NG', 'J');  
	intext = mreplace(intext, 'NJ', 'J');   
	#intext = mreplace(intext, 'z', 'Y');   
	#intext = mreplace(intext, 'wri', 'X'); 
	#intext = mreplace(intext, 'wr', 'X');  
	#intext = mreplace(intext, '^', 'C');   
	#intext = mreplace(intext, 't`', 'W');  
	intext = mreplace(intext, 'Rh', 'Z');
	intext = mreplace(intext, 'cc', 'C');  
	
	#intext = mreplace(intext, '`', '`#');	
	
	intext = mreplace(intext, 'b ', 'ba ');
	intext = mreplace(intext, 'c ', 'ca ');
	intext = mreplace(intext, 'd ', 'da ');
	intext = mreplace(intext, 'f ', 'fa ');
	intext = mreplace(intext, 'g ', 'ga ');
	intext = mreplace(intext, 'h ', 'ha ');
	intext = mreplace(intext, 'j ', 'ja ');
	intext = mreplace(intext, 'k ', 'ka ');
	intext = mreplace(intext, 'K ', 'kha ');
	intext = mreplace(intext, 'l ', 'la ');
	intext = mreplace(intext, 'm ', 'ma ');
	intext = mreplace(intext, 'n ', 'na ');
	intext = mreplace(intext, 'p ', 'pa ');
	intext = mreplace(intext, 'r ', 'ra ');
	intext = mreplace(intext, 's ', 'sa ');
	intext = mreplace(intext, 't ', 'ta ');
	intext = mreplace(intext, 'v ', 'va ');
	intext = mreplace(intext, 'Y ', 'Ya ');
	intext = mreplace(intext, 'y ', 'ya ');
	intext = mreplace(intext, 'L ', 'La ');
	intext = mreplace(intext, 'w', 'wa');
	intext = mreplace(intext, 'q', 'q');
	intext = mreplace(intext, 'Q', 'Q');
	intext = mreplace(intext, 'z', 'z');	
	intext = mreplace(intext, 'N~', 'ൺ');
	intext = mreplace(intext, 'n~', 'ൻ');
	intext = mreplace(intext, 'r~', 'ർ');
	intext = mreplace(intext, 'l~', 'ൽ');
	intext = mreplace(intext, 'L~', 'ൾ');
	intext = mreplace(intext, 'M', 'ം');
	
	intext = mreplace(intext, '^', '്');
	intext = mreplace(intext, 'z ', 'za ');
	intext = mreplace(intext, 'R ', 'Ra ');
	

	intext = mreplace(intext, 'D ', 'Da ');
	intext = mreplace(intext, 'G ', 'Ga ');
	intext = mreplace(intext, 'J ', 'Ja ');
	intext = mreplace(intext, 'N ', 'Na ');
	intext = mreplace(intext, 'S ', 'Sa ');
	intext = mreplace(intext, 'T ', 'Ta ');
	intext = mreplace(intext, 'y ', 'ya ');
	intext = mreplace(intext, 'X', 'X');
	

	#intext = mreplace(intext, '. ', '.a ');
	

	
	
	if '|' in intext:
		intext = mreplace(intext, 'b|', 'ba|');
		intext = mreplace(intext, 'c|', 'ca|');
		intext = mreplace(intext, 'd|', 'da|');
		intext = mreplace(intext, 'f|', 'fa|');
		intext = mreplace(intext, 'g|', 'ga|');
		intext = mreplace(intext, 'h|', 'ha|');
		intext = mreplace(intext, 'j|', 'ja|');
		intext = mreplace(intext, 'k|', 'ka|');
		intext = mreplace(intext, 'K|', 'kha|');
		intext = mreplace(intext, 'l|', 'la|');
		#intext = mreplace(intext, 'v|', 'va|');
		intext = mreplace(intext, 'm|', 'ma|');
		intext = mreplace(intext, 'n|', 'na|');
		intext = mreplace(intext, 'p|', 'pa|');
		intext = mreplace(intext, 'r|', 'ra|');
		intext = mreplace(intext, 's|', 'sa|');
		intext = mreplace(intext, 't|', 'ta|');
		intext = mreplace(intext, 'v|', 'va|');
		intext = mreplace(intext, 'Y|', 'Ya|');
		intext = mreplace(intext, 'L|', 'La|');
		intext = mreplace(intext, 'w|', 'wa|');
		#intext = mreplace(intext, 'q|', 'ൗ');
		intext = mreplace(intext, 'D|', 'Da|');
		intext = mreplace(intext, 'G|', 'Ga|');
		intext = mreplace(intext, 'J|', 'Ja|');
		intext = mreplace(intext, 'N|', 'Na|');
		intext = mreplace(intext, 'S|', 'Sa|');
		intext = mreplace(intext, 'T|', 'Ta|');
		intext = mreplace(intext, 'y|', 'ya|');
		intext = mreplace(intext, 'z|', 'za|');
		
		intext = mreplace(intext, 'n~|', 'ൻ|');
		intext = mreplace(intext, 'N~|', 'ൺ|');
		intext = mreplace(intext, 'r~|', 'ർ|');
		intext = mreplace(intext, 'l~|', 'ൽ|');
		intext = mreplace(intext, 'l^~|', 'ൾ|');
		intext = mreplace(intext, '^|', '്|');
		intext = mreplace(intext, 'M|', 'ം|');
		intext = mreplace(intext, 'q|', 'q|');
		intext = mreplace(intext, 'Q|', 'Q|');
		
		intext = mreplace(intext, '.|', '.a|');
		
	intext = mreplace(intext, 'aa', 'A');
	intext = mreplace(intext, 'ii', 'I');
	intext = mreplace(intext, 'ee', 'E');
	intext = mreplace(intext, 'uu', 'U');
	intext = mreplace(intext, 'ai', 'E');
	#intext = mreplace(intext, 'au', 'AU');
	intext = mreplace(intext, 'oo', 'O');
	#intext = mreplace(intext, 'Ri', 'R');   ## needed ?

	#intext = mreplace(intext, 'chh', 'TMPUNIKSTR');
	#intext = mreplace(intext, 'ch', 'c');
	#intext = mreplace(intext, 'TMPUNIKSTR', 'ch');
	intext = mreplace(intext, 'GN', 'G');
	intext = mreplace(intext, 'JN', 'J');
	
	intext = mreplace(intext, 'Sh', 'S');
	
	
	#intext = mreplace(intext, '.n', 'M');
	#intext = mreplace(intext, '.N', 'C');
	#intext = mreplace(intext, '.Y', 'y');
	#intext = mreplace(intext, '.Dh', 'Z');
	#intext = mreplace(intext, '.D', 'X');
	#intext = mreplace(intext, 'Dh.', 'Z');
	#intext = mreplace(intext, 'D.', 'X');
	#intext = mreplace(intext, ':', 'H');

	intext = mreplace(intext, 'f', 'ph');
	#intext = mreplace(intext, 'v', 'va');

	intext = mreplace(intext, '_', '');
	
	
	
	## Main conversion to malayalam begins!
	i = 0
	#global len
	intext_len = len(intext)
	
	while i < intext_len:
		cur = intext[i]
		if i+1 < intext_len:
			next = intext[i+1]
		else:
			next = ''
			
		comb = cur + next
	
	## mainly the 'vowels'  list (first 12 are swarabarna which also acts as cihnam)
		list1 = ['a','A','i','I','u','U','e','E','o','O','M','H','^','|','#','`','x'] 
		## mainly the 'consonants' list
		list2 = ['k','g','G','c','C','j','J','t','d','n','T','D','N','p','b','m','s','h','Y','r','I','v','R','y','z','S','l','l~','^','L','w','W','Z','q','Q','P','F','K','V','B','X'] 


		if cur in list1 or (cur >= '0' and cur <= '9'):
			ans += keymap[cur]
			i += 1
		
		elif cur in list2:
			## more consonants list
			list3 = ['kh','gh','ch','jh','th','dh','Th','Dh','ph','bh','sh','au','C']

			if comb in list3:
				cur =  comb
				i +=1
				if i+1 < intext_len:
					next  = intext[i+1]
				else:
					next  = ''
	
			if next in list1[:17]: ## this lists the swarabarna / cihnam
				ans += (keymap[cur] + keymap[next+'cihnam'])
				i += 2
			#elif next != '':
			#	ans += (keymap[cur] + keymap['hasanta'])
			#	i += 1
			###### trying to remove trailing hasanta for words ending with 'a kaar' 
			else :
				ans += keymap[cur]
				i += 1
			
		else:
			ans += cur
			i += 1

	
	return ans 
