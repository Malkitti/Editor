# Malayalam Phonetic Editor / മലയാളം ൊഫാൊണറിക് എഡിറർ


Ezhuthani is a simple Text Editor to enable Phonetic typing in the Malayalam
language for users of GNU/Linux systems. It is written in Python and uses the
Wxpython toolkit for the GUI. The encoding scheme used in the application is
Unicode 6.2.
It is very easy and totally intuitive to use Ezhuthani. You keep typing words using
your normal keyboard, and it will automatically be transliterated to Malayalam. No
need to remember complicated Malayalam Keyboard layouts.
e.g. 'aa' will become 'ആ'
The transliteration happens when the 'Space bar' is pressed. In order to know which
roman letter combination will produce the actual malayalam character press F1 or the
Help button in the toolbar to get the translitearation scheme.
How to Install Ezhuthani, Phonetic Text Editor for Malayalam
Install the dependencies
• Python 2.7.x (as wxPython doesn't have support for Python 3.x.x
versions it's recommended to use 2.x.x version preferebly 2.7.x)
• wxPython 2.8 or later (if a compatible version for your linux flavour is
not found you can install wxGlade which has wx in it)
• Download Meera font or any other malyalam font with unicode support.
The dependencies can be installed directly using the package manager in your linux
distro. The binaries for these programs can be downloaded from the links provided
below.
http://python.org/
http://wxpython.org/
http://malayalam.kerala.gov.in/index.php/Fonts
It is advised to install the dependenices before trying to run th installer script as it
doesn't check for dependencies, and the installer script will report errors.
After installing the dependencies, follow the instructions,
• Download the source tarball from http://
• Untar the tarball : tar -xvvf ezhuthani-0.1.tar.gz
• Go to the director: cd ezhuthani
• Execute the installer script as root: sudo ./installer
• Now type ezhuthani in the terminal and you'll get the interface of ezhuthani, in
case some error occurs or you can't see the menu or toolbar type, 'sudo
ezhuthani' instead of 'ezhuthani'.
• The installed files will be in the /usr/share/ezhuthani
• To run the program use the command 'ezhuthani' or 'sudo ezhuthani' from a
terminal. Instead you can copy 'ezhuthani_launcher.sh' into the home folder
and create a launcher in the desktop and select 'ezhuthani_launcher.sh' as the
command. Make sure you've selelcter the type of the launcher as 'Application
in Terminal'
Limitations
• Typing Malyalam and English together is not possible in this version of
Ezhuthani.
• Find and Replace is not available yet.
• Formattin will not be saved as the files are saved as plain text, but they are
useful if you want to copu the text from ezhuthani to other word processing
applications.
Transliteration Scheme
Ezhuthani uses a very intuitive trasliteration scheme which is given below,
Vowels
അ = a ആ = aa|A
ഇ = i ഈ = ii|I
ഉ = u ഊ = uu|U
ഋ = x
എ = e ഏ = ee|E
ഐ = z
ഒ= o ഓ = oo|O
ഔ = Y
അം = aM അഃ = aH
Consonants
ക = k|ka ച = c|ca ട = t|ta
ഖ = kh|kha ഛ = cc|cca|ch|cha ഠ = th|tha
ഗ = g|ga ജ = j|ja ഡ = d|da
ഘ = gh|gha ഝ = jh|jha ഢ = dh|dha
ങ = G|Ga ഞ = J|Ja ണ = N|Na
ത = T|Ta പ = p|pa
ഥ = Th|Tha ഫ = ph|pha
ദ = D|Da ബ = b|ba
ധ = Dh|Dha ഭ = bh|bha
ന = n|na മ = m|ma
യ = y|ya
ര = r|ra
ല = l|la
വ = v|va
ശ = s|sa
ഷ = sh|sha
സ = S|Sa
ഹ = h|ha
ള = L|La
ഴ = z|za
റ = R|Ra
Chillu
ൽ = l~
ൾ = L~
ർ = r~
ൻ = n~
ൺ = N~
Consonants with vowel symbols
ക് = ക + ്് = k^
ക = k|ka
കാ = ക + ്ാ = kaa|kA
കി = ക + ്ി = ki
കീ = ക + ്ീ = kii|kI
ക = ക + ്ു = ku
ക = ക + ്ൂ = kuu|kU
ക = ക + ്ൃ = kx
ൊക = ക + ൊ് = ke
േക = ക + േ് = kE
ൈക = ക + ൈ് = kQ
ൊകാ = ക + ൊ്ാ = ko
േകാ = ക + േ്ാ = koo|kO
കൗ = ക + ്ൗ = kq
കം = ക + ്ം = kM
കഃ = ക + ്ഃ = kH
Consonant Symbols
കയ = ക + ്് + യ = k^r|k^ra
കവ = ക + ്് + വ = k^v|k^va
ക = ക + ്് + ല = k^l|k^la
ക = ക + ്് + ര =k^r|k^ra
Numbers
1 = ൧
2 = ൨
3 = ൩
4 = ർ
5 = ൫
6 = ൬
7 = ൭
8 = ൮
9 = ൻ
0 = ൦
The combination of consonants can be produced using the chandrakala ്് which can
be invoked by the ^ on the keyboard.
For example
'ക' can be produced by k^sh | k^sha
