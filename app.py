import os
from rich import print; from rich.console import Console; cn = Console();
from rich.traceback import install
import requests
from PIL import Image
from tkinter import filedialog

R = '[bold red]'     # π΄| ΠΡΠ°ΡΠ½ΡΠΉ
Q = '[bold #E32636]' # π΄| Π―ΡΠΊΠΎ ΠΊΡΠ°ΡΠ½ΡΠΉ
G = '[bold green]'   # π’| ΠΠ΅Π»ΡΠ½ΡΠΉ
B = '[bold blue]'    # π΅| Π‘ΠΈΠ½ΠΈΠΉ
D = '[bold #00FF7F]' # π΅| ΠΠΎΠ»ΡΠ±ΠΎΠΉ
W = '[bold white]'   # βͺ| ΠΠ΅Π»ΡΠΉ
Y = '[bold #FFFF00]' # π‘| ΠΡΠ»ΡΡΠΉ
I = '[bold yellow]'  # π‘| Π‘Π²Π΅ΡΠ»ΠΎ ΠΆΡΠ»ΡΡΠΉ
E = '[bold #808080]' # βοΈ| Π‘Π΅ΡΠ²ΡΠΉ
O = '   '
A = 'βββ'

IA = '                         '
TAB ='    '
TAG1 = ['0+','6+','12+','16+','18+']
TAG2 = ['0', '6', '12', '16', '18']

print('   ')
cn.print(f'{R}βββ AledCreatik βββ', justify="center")

num = 0
Π€Π°ΠΉΠ»ΠΎΠ² = 1
for dirpath, dirnames, filenames in os.walk("./page"):
    for dirname in dirnames:
        num += 1
        Π€Π°ΠΉΠ»ΠΎΠ² += 1
nun = f'{num}      '

DIR = f'page/{Π€Π°ΠΉΠ»ΠΎΠ²}'
FILE = 'image.png'

class app:
    _1_Print  = f'{R}βββββββββββββββββββββββββββββββββββββ{A*3}{E} ΠΠ°Π½Π΅Π»Ρ ΡΠ°Π·ΡΠ°Π±ΠΎΡΡΠΊΠ° {R}β{R}β'
    _2_Print  = f'{R}β{W} ΠΠ°ΠΏΠΎΠΊ: {Y}{nun}                                           {O*2}{R}β'
    _3_Print  = f'{R}ββββββββββββββββββββββββββββββββββββββββββββββββββββββββββββββββ{A*1}{R}β'
    _4_Print  = f'{B} ΠΠ»Ρ Π½Π°ΡΠ°Π»Π° Π½Π°ΡΡΡΠΎΠΉΠΊΠΈ ΡΠ°ΠΉΡΠ°                          {Y}ΠΠ°ΠΆΠΌΠΈΡΠ΅: {D}Enter'
    _0_Input  = f''

    _11_Print = f'{R}βββββββββββββββββββββββββββββββββββββββββββββ{A*3}{E} ΠΠΎΠΌΠ΅Π½ΡΠ°ΡΠΈΠΉ {R}β{R}β'
    _12_Print = f'{R}β{I} ΠΠ½Π°ΡΠ΅Π½ΠΈΡ: {G}ΠΡΠ±ΠΎΠΉ ΡΠ΅ΠΊΡΡ                                   {O*3}{R}β'
    _13_Print = f'{R}β{E} β{Q} Π’ΡΠ΅Π±ΡΠ΅ΡΡΡ ΠΎΠ±ΡΠ·Π°ΡΠ΅Π»ΡΠ½ΠΎ!                                {O*3}{R}β'
    _14_Print = f'{R}ββββββββββββββββββββββββββββββββββββββββββββββββββββββββββββββββ{A*1}{R}β'
    _1_Name   = f'{IA}{B} ΠΠ°Π·Π²Π°Π½ΠΈΠ΅'
    _1_Input  = f'{IA}{E} β {I}ΠΠ½Π°ΡΠ΅Π½ΠΈΠ΅: '

    _21_Print = f'{R}βββββββββββββββββββββββββββββββββββββββββββββ{A*3}{E} ΠΠΎΠΌΠ΅Π½ΡΠ°ΡΠΈΠΉ {R}β{R}β'
    _22_Print = f'{R}β{I} Π·Π½Π°ΡΠ΅Π½ΠΈΡ: {G}0+, 6+, 12+, 16+, 18+                         {O*3}{R}β'
    _23_Print = f'{R}β{E} β{Y} ΠΠΎ ΡΠΌΠΎΠ»ΡΠ°Π½ΠΈΡ: {G}0+                                   {O*4}{R}β'
    _24_Print = f'{R}ββββββββββββββββββββββββββββββββββββββββββββββββββββββββββββββββ{A*1}{R}β'
    _2_Name   = f'{IA}{B} ΠΠΎΠ·ΡΠ°ΡΡΠ½ΠΎΠ΅ ΠΎΠ³ΡΠ°Π½ΠΈΡΠ΅Π½ΠΈΠ΅'
    _2_Input  = f'{IA}{E} β {I}ΠΠ½Π°ΡΠ΅Π½ΠΈΠ΅: '

    _31_Print = f'{R}βββββββββββββββββββββββββββββββββββββββββββββ{A*3}{E} ΠΠΎΠΌΠ΅Π½ΡΠ°ΡΠΈΠΉ {R}β{R}β'
    _32_Print = f'{R}β{I} ΠΠ½Π°ΡΠ΅Π½ΠΈΡ: {G}ΠΠΎΠΌΠ°Π½Π΄Π° {Q}file {W}ΠΈΠ»ΠΈ {G}https://example.com {O*6}{R}β'
    _33_Print = f'{R}β{E} β{Y} ΠΠΎ ΡΠΌΠΎΠ»ΡΠ°Π½ΠΈΡ: {G}ΠΠ΅Ρ                                  {O*4}{R}β'
    _34_Print = f'{R}ββββββββββββββββββββββββββββββββββββββββββββββββββββββββββββββββ{A*1}{R}β'
    _3_Name   = f'{IA}{B} ΠΠ·ΠΎΠ±ΡΠ°ΠΆΠ΅Π½ΠΈΠ΅'
    _3_Input  = f'{IA}{E} β {I}ΠΠ½Π°ΡΠ΅Π½ΠΈΠ΅: '
    _33_Input = f'{IA}{E}   β {I}URL ΠΠ·ΠΎΠ±ΡΠ°ΠΆΠ΅Π½ΠΈΡ: '

    _41_Print = f'{R}βββββββββββββββββββββββββββββββββββββββββββββ{A*3}{E} ΠΠΎΠΌΠ΅Π½ΡΠ°ΡΠΈΠΉ {R}β{R}β'
    _42_Print = f'{R}β{I} ΠΠ½Π°ΡΠ΅Π½ΠΈΡ: {G}https://example.com                           {O*3}{R}β'
    _43_Print = f'{R}β{E} β{Y} ΠΠΎ ΡΠΌΠΎΠ»ΡΠ°Π½ΠΈΡ: {G}ΠΠ΅Ρ                                  {O*4}{R}β'
    _44_Print = f'{R}ββββββββββββββββββββββββββββββββββββββββββββββββββββββββββββββββ{A*1}{R}β'
    _4_Name   = f'{IA}{B} URL ΠΠ½ΡΠΎΡΠΌΠ°ΡΠΈΡ'
    _4_Input  = f'{IA}{E} β {I}ΠΠ½Π°ΡΠ΅Π½ΠΈΠ΅: '

    _51_Print = f'{R}βββββββββββββββββββββββββββββββββββββββββββββ{A*3}{E} ΠΠΎΠΌΠ΅Π½ΡΠ°ΡΠΈΠΉ {R}β{R}β'
    _52_Print = f'{R}β{I} ΠΠ½Π°ΡΠ΅Π½ΠΈΡ: {G}https://example.com                           {O*3}{R}β'
    _53_Print = f'{R}β{E} β{Q} Π’ΡΠ΅Π±ΡΠ΅ΡΡΡ ΠΎΠ±ΡΠ·Π°ΡΠ΅Π»ΡΠ½ΠΎ!                                {O*3}{R}β'
    _54_Print = f'{R}ββββββββββββββββββββββββββββββββββββββββββββββββββββββββββββββββ{A*1}{R}β'
    _5_Name   = f'{IA}{B} URL ΠΠΈΠ΄Π΅ΠΎ'
    _5_Input  = f'{IA}{E} β {I}ΠΠ½Π°ΡΠ΅Π½ΠΈΠ΅: '

Π€ΠΎΡΠΌΠ°Ρ_App = (app._1_Print  + '\n' + app._2_Print  + '\n' + app._3_Print  + '\n' + app._4_Print)
Π€ΠΎΡΠΌΠ°Ρ_1   = (app._11_Print + '\n' + app._12_Print + '\n' + app._13_Print + '\n' + app._14_Print); ΠΠΌΡ = ''; ΠΠΌΡ1 = f'{B}-'
Π€ΠΎΡΠΌΠ°Ρ_2   = (app._21_Print + '\n' + app._22_Print + '\n' + app._23_Print + '\n' + app._24_Print); ΠΠΎΠ·ΡΠ°ΡΡ = ''; ΠΠΎΠ·ΡΠ°ΡΡ1 = f'{B}-'
Π€ΠΎΡΠΌΠ°Ρ_3   = (app._31_Print + '\n' + app._32_Print + '\n' + app._33_Print + '\n' + app._34_Print); ΠΠ·ΠΎΠ±ΡΠ°ΠΆΠ΅Π½ΠΈΠ΅ = ''; ΠΠ·ΠΎΠ±ΡΠ°ΠΆΠ΅Π½ΠΈΠ΅1 = f'{B}-'
Π€ΠΎΡΠΌΠ°Ρ_4   = (app._41_Print + '\n' + app._42_Print + '\n' + app._43_Print + '\n' + app._44_Print); ΠΠ½ΠΎΠΏΠΊΠ° = ''; ΠΠ½ΠΎΠΏΠΊΠ°1 = f'{B}-'; Button = ''
Π€ΠΎΡΠΌΠ°Ρ_5   = (app._51_Print + '\n' + app._52_Print + '\n' + app._53_Print + '\n' + app._54_Print); ΠΠΈΠ΄Π΅ΠΎ = ''; ΠΠΈΠ΄Π΅ΠΎ1 = f'{B}-'

cn.print(Π€ΠΎΡΠΌΠ°Ρ_App, justify="center")
cn.input(app._0_Input, password=True)
os.system('cls')
cn.print()
cn.print(f'{R}βββ ΠΠ°ΡΡΡΠΎΠΉΠΊΠ° ΡΠ°ΠΉΡΠ° βββ', justify="center")
cn.print()
cn.print(f'{E}   ΠΠ°Π·Π²Π°Π½ΠΈΠ΅ ΡΠΈΠ»ΡΠΌΠ°: {ΠΠΌΡ1}')
cn.print(f'{E}   ΠΠΎΠ·ΡΠ°ΡΡΠ½ΠΎΠ΅ ΠΎΠ³ΡΠ°Π½ΠΈΡΠ΅Π½ΠΈΠ΅: {ΠΠΎΠ·ΡΠ°ΡΡ1}')
cn.print()
cn.print(f'{E}   URL ΠΠ·ΠΎΠ±ΡΠ°ΠΆΠ΅Π½ΠΈΡ: {ΠΠ·ΠΎΠ±ΡΠ°ΠΆΠ΅Π½ΠΈΠ΅1}')
cn.print(f'{E}   URL ΠΠ½ΡΠΎΡΠΌΠ°ΡΠΈΡ: {ΠΠ½ΠΎΠΏΠΊΠ°1}')
cn.print(f'{E}   URL ΠΠΈΠ΄Π΅ΠΎ: {ΠΠΈΠ΄Π΅ΠΎ1}')
cn.print()
cn.print()
cn.print(Π€ΠΎΡΠΌΠ°Ρ_1, justify="center")
while ΠΠΌΡ in '':
    cn.print(app._1_Name)
    ΠΠΌΡ = cn.input(app._1_Input)
    if ΠΠΌΡ == '':
        cn.print(f'{IA}   {E}β {R}Π­ΡΠΎ ΠΏΠΎΠ»Π΅ ΠΎΠ±ΡΠ·Π°ΡΠ΅Π»ΡΠ½ΠΎ\n')
        pass
    else:
        ΠΠΌΡ1 = Y + ΠΠΌΡ
        break

os.system('cls')
cn.print()
cn.print(f'{R}βββ ΠΠ°ΡΡΡΠΎΠΉΠΊΠ° ΡΠ°ΠΉΡΠ° βββ', justify="center")
cn.print()
cn.print(f'{E}   ΠΠ°Π·Π²Π°Π½ΠΈΠ΅ ΡΠΈΠ»ΡΠΌΠ°: {ΠΠΌΡ1}')
cn.print(f'{E}   ΠΠΎΠ·ΡΠ°ΡΡΠ½ΠΎΠ΅ ΠΎΠ³ΡΠ°Π½ΠΈΡΠ΅Π½ΠΈΠ΅: {ΠΠΎΠ·ΡΠ°ΡΡ1}')
cn.print()
cn.print(f'{E}   URL ΠΠ·ΠΎΠ±ΡΠ°ΠΆΠ΅Π½ΠΈΡ: {ΠΠ·ΠΎΠ±ΡΠ°ΠΆΠ΅Π½ΠΈΠ΅1}')
cn.print(f'{E}   URL ΠΠ½ΡΠΎΡΠΌΠ°ΡΠΈΡ: {ΠΠ½ΠΎΠΏΠΊΠ°1}')
cn.print(f'{E}   URL ΠΠΈΠ΄Π΅ΠΎ: {ΠΠΈΠ΄Π΅ΠΎ1}')
cn.print()
cn.print()
cn.print(Π€ΠΎΡΠΌΠ°Ρ_2, justify="center")
while ΠΠΎΠ·ΡΠ°ΡΡ in '':
    cn.print(app._2_Name)
    ΠΠΎΠ·ΡΠ°ΡΡ = cn.input(app._2_Input)
    if ΠΠΎΠ·ΡΠ°ΡΡ == '':
        ΠΠΎΠ·ΡΠ°ΡΡ = '0+'
        ΠΠΎΠ·ΡΠ°ΡΡ1 = f'{R}{ΠΠΎΠ·ΡΠ°ΡΡ} {B}ΠΠΎ ΡΠΌΠΎΠ»ΡΠ°Π½ΠΈΡ'
        break
    elif ΠΠΎΠ·ΡΠ°ΡΡ in TAG1:
        ΠΠΎΠ·ΡΠ°ΡΡ = f'{ΠΠΎΠ·ΡΠ°ΡΡ}'
        ΠΠΎΠ·ΡΠ°ΡΡ1 = f'{R}{ΠΠΎΠ·ΡΠ°ΡΡ} {B}'
        break
    elif ΠΠΎΠ·ΡΠ°ΡΡ in TAG2:
        ΠΠΎΠ·ΡΠ°ΡΡ = f'{ΠΠΎΠ·ΡΠ°ΡΡ}+'
        ΠΠΎΠ·ΡΠ°ΡΡ1 = f'{R}{ΠΠΎΠ·ΡΠ°ΡΡ} {B}'
        break
    else:
        ΠΠΎΠ·ΡΠ°ΡΡ = '0+'
        ΠΠΎΠ·ΡΠ°ΡΡ1 = f'{R}{ΠΠΎΠ·ΡΠ°ΡΡ} {B}ΠΠΎ ΡΠΌΠΎΠ»ΡΠ°Π½ΠΈΡ'
        break

os.system('cls')
cn.print()
cn.print(f'{R}βββ ΠΠ°ΡΡΡΠΎΠΉΠΊΠ° ΡΠ°ΠΉΡΠ° βββ', justify="center")
cn.print()
cn.print(f'{E}   ΠΠ°Π·Π²Π°Π½ΠΈΠ΅ ΡΠΈΠ»ΡΠΌΠ°: {ΠΠΌΡ1}')
cn.print(f'{E}   ΠΠΎΠ·ΡΠ°ΡΡΠ½ΠΎΠ΅ ΠΎΠ³ΡΠ°Π½ΠΈΡΠ΅Π½ΠΈΠ΅: {ΠΠΎΠ·ΡΠ°ΡΡ1}')
cn.print()
cn.print(f'{E}   URL ΠΠ·ΠΎΠ±ΡΠ°ΠΆΠ΅Π½ΠΈΡ: {ΠΠ·ΠΎΠ±ΡΠ°ΠΆΠ΅Π½ΠΈΠ΅1}')
cn.print(f'{E}   URL ΠΠ½ΡΠΎΡΠΌΠ°ΡΠΈΡ: {ΠΠ½ΠΎΠΏΠΊΠ°1}')
cn.print(f'{E}   URL ΠΠΈΠ΄Π΅ΠΎ: {ΠΠΈΠ΄Π΅ΠΎ1}')
cn.print()
cn.print()
cn.print(Π€ΠΎΡΠΌΠ°Ρ_3, justify="center")
while True:
    cn.print(app._3_Name)
    ΠΠ·ΠΎΠ±ΡΠ°ΠΆΠ΅Π½ΠΈΠ΅ = cn.input(app._3_Input)
    if ΠΠ·ΠΎΠ±ΡΠ°ΠΆΠ΅Π½ΠΈΠ΅ in '':
        ΠΠ·ΠΎΠ±ΡΠ°ΠΆΠ΅Π½ΠΈΠ΅ = 'ΠΠ΅Ρ'
        ΠΠ·ΠΎΠ±ΡΠ°ΠΆΠ΅Π½ΠΈΠ΅1 = f'{D}Π€Π°ΠΉΠ» {B}ΠΠΎ ΡΠΌΠΎΠ»ΡΠ°Π½ΠΈΡ'
        imgLOG = '1'
        break
    if ΠΠ·ΠΎΠ±ΡΠ°ΠΆΠ΅Π½ΠΈΠ΅ in ['1', 'file', 'File', 'FILE']:
        try:
            ΠΠ·ΠΎΠ±ΡΠ°ΠΆΠ΅Π½ΠΈΠ΅ = filedialog.askopenfilename()
            FILE = Image.open(ΠΠ·ΠΎΠ±ΡΠ°ΠΆΠ΅Π½ΠΈΠ΅)  
            ΠΠ·ΠΎΠ±ΡΠ°ΠΆΠ΅Π½ΠΈΠ΅1 = f'{D}Π€Π°ΠΉΠ»'
            imgLOG = '2'
            break
        except:
            cn.print(f'{IA}   {E}β {R}Π€Π°ΠΉΠ» Π½Π΅ ΠΏΠΎΠ΄Π΄Π΅ΡΠΆΠΈΠ²Π°Π΅ΡΡΡ\n')
    else:
        try:
            ΠΠ°Π½Π½ΡΠ΅ = requests.get(ΠΠ·ΠΎΠ±ΡΠ°ΠΆΠ΅Π½ΠΈΠ΅).content
            ΠΠ·ΠΎΠ±ΡΠ°ΠΆΠ΅Π½ΠΈΠ΅1 = f'{D}Π‘ΡΡΠ»ΠΊΠ°'
            imgLOG = '3'
            break
        except:
            cn.print(f'{IA}   {E}β {R}Π‘ΡΡΠ»ΠΊΠ° ΡΠΊΠ°Π·Π°Π½Π° Π½Π΅ΠΊΠΎΡΠ΅ΠΊΡΠ½ΠΎ\n')

os.system('cls')
cn.print()
cn.print(f'{R}βββ ΠΠ°ΡΡΡΠΎΠΉΠΊΠ° ΡΠ°ΠΉΡΠ° βββ', justify="center")
cn.print()
cn.print(f'{E}   ΠΠ°Π·Π²Π°Π½ΠΈΠ΅ ΡΠΈΠ»ΡΠΌΠ°: {ΠΠΌΡ1}')
cn.print(f'{E}   ΠΠΎΠ·ΡΠ°ΡΡΠ½ΠΎΠ΅ ΠΎΠ³ΡΠ°Π½ΠΈΡΠ΅Π½ΠΈΠ΅: {ΠΠΎΠ·ΡΠ°ΡΡ1}')
cn.print()
cn.print(f'{E}   URL ΠΠ·ΠΎΠ±ΡΠ°ΠΆΠ΅Π½ΠΈΡ: {ΠΠ·ΠΎΠ±ΡΠ°ΠΆΠ΅Π½ΠΈΠ΅1}')
cn.print(f'{E}   URL ΠΠ½ΡΠΎΡΠΌΠ°ΡΠΈΡ: {ΠΠ½ΠΎΠΏΠΊΠ°1}')
cn.print(f'{E}   URL ΠΠΈΠ΄Π΅ΠΎ: {ΠΠΈΠ΄Π΅ΠΎ1}')
cn.print()
cn.print()
cn.print(Π€ΠΎΡΠΌΠ°Ρ_4, justify="center")
while ΠΠ½ΠΎΠΏΠΊΠ° in '':
    cn.print(app._4_Name)
    ΠΠ½ΠΎΠΏΠΊΠ° = cn.input(app._4_Input)
    if ΠΠ½ΠΎΠΏΠΊΠ° == '':
        button = ''
        ΠΠ½ΠΎΠΏΠΊΠ° = 'ΠΠ΅Ρ'
        ΠΠ½ΠΎΠΏΠΊΠ°1 = f'{Y}{ΠΠ½ΠΎΠΏΠΊΠ°} {B}'
    else:
        ΠΠ½ΠΎΠΏΠΊΠ°1 = f'{Y}{ΠΠ½ΠΎΠΏΠΊΠ°} {B}'
        Button = f'<a class="buttonn" href="{ΠΠ½ΠΎΠΏΠΊΠ°}" target="0">ΠΠ½ΡΠΎΡΠΌΠ°ΡΠΈΡ</a>'

os.system('cls')
cn.print()
cn.print(f'{R}βββ ΠΠ°ΡΡΡΠΎΠΉΠΊΠ° ΡΠ°ΠΉΡΠ° βββ', justify="center")
cn.print()
cn.print(f'{E}   ΠΠ°Π·Π²Π°Π½ΠΈΠ΅ ΡΠΈΠ»ΡΠΌΠ°: {ΠΠΌΡ1}')
cn.print(f'{E}   ΠΠΎΠ·ΡΠ°ΡΡΠ½ΠΎΠ΅ ΠΎΠ³ΡΠ°Π½ΠΈΡΠ΅Π½ΠΈΠ΅: {ΠΠΎΠ·ΡΠ°ΡΡ1}')
cn.print()
cn.print(f'{E}   URL ΠΠ·ΠΎΠ±ΡΠ°ΠΆΠ΅Π½ΠΈΡ: {ΠΠ·ΠΎΠ±ΡΠ°ΠΆΠ΅Π½ΠΈΠ΅1}')
cn.print(f'{E}   URL ΠΠ½ΡΠΎΡΠΌΠ°ΡΠΈΡ: {ΠΠ½ΠΎΠΏΠΊΠ°1}')
cn.print(f'{E}   URL ΠΠΈΠ΄Π΅ΠΎ: {ΠΠΈΠ΄Π΅ΠΎ1}')
cn.print()
cn.print()
cn.print(Π€ΠΎΡΠΌΠ°Ρ_5, justify="center")
while ΠΠΈΠ΄Π΅ΠΎ in '':
    cn.print(app._5_Name)
    ΠΠΈΠ΄Π΅ΠΎ = cn.input(app._5_Input)
    if ΠΠΈΠ΄Π΅ΠΎ == '':
        cn.print(f'{IA}   {E}β {R}Π­ΡΠΎ ΠΏΠΎΠ»Π΅ ΠΎΠ±ΡΠ·Π°ΡΠ΅Π»ΡΠ½ΠΎ\n')
    else:
        ΠΠΈΠ΄Π΅ΠΎ1 = f'{Y}{ΠΠΈΠ΄Π΅ΠΎ} {B}'

#    <style>:root{
#            --VName: 'Π£Π΄Π°ΡΠ°';
#            --VAge:  '6+';
#        }
#    </style> 

Π‘ΡΡΠ°Π½ΠΈΡΠ° = (   
f"""<!-- Π€ΠΎΡΠΌΠ°ΡΠΈΡΠΎΠ²Π°Π½ΠΈΠ΅ -->
<!DOCTYPE html>
<html lang="ru" class="no-js">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <head>
        <meta charset="utf-8">
        <meta name="yandex-verification" content="2d8c1dcb18ad48b7"/>
        
<!-- ΠΠ½ΡΠ΅Π³ΡΠ°ΡΠΈΡ Embed -->
<meta property="og:site_name" content="AledGG">
<link rel="shortcut icon" href="https://i.imgur.com/tPQs4ZD.png">
<meta property="og:image:width" content="170">
<meta property="og:image:height" content="250">
<meta name="theme-color" content="#26ade9">

<!-- CSS -->
<link rel="stylesheet" href="../../css/Page.css">        <!-- ΠΠΈΠ·Π°ΠΉΠ½ ΡΠΎΠ½Π° ΡΠ°ΠΉΡΠ° --> 
<link rel="stylesheet" href="../../css/Header.css">      <!-- ΠΠΈΠ·Π°ΠΉΠ½ ΡΠ°ΠΏΠΊΠΈ ΡΠ°ΠΉΡΠ° --> 
<link rel="stylesheet" href="../../css/ScrollBar.css">   <!-- ΠΠΎΠ»ΠΎΡΠ° ΠΏΡΠΎΠΊΡΡΡΠΊΠΈ -->
<link rel="stylesheet" href="../../css/SectionBox.css">  <!-- Π‘Π΅ΠΊΡΠΈΠΈ Π±Π»ΠΎΠΊΠΎΠ² -->
<link rel="stylesheet" href="../../css/VideoPlayer.css"> <!-- ΠΠΈΠ΄Π΅ΠΎ Π±Π»ΠΎΠΊ -->
<link rel="stylesheet" href="../../css/Animation.css">   <!-- ΠΠ½ΠΈΠΌΠ°ΡΠΈΠΈ -->

<link rel="stylesheet" href="../../css/Root.css">        <!-- ΠΠΎΠ½ΡΠΈΠ³ΡΡΠ°ΡΠΈΡ -->

<!-- JavasCript -->
<script src="../../index.js"></script>

<!-- Π¨Π°ΠΏΠΊΠ° ΡΡΡΠ°Π½ΠΈΡΡ -->
<div class="body-wrap">
    <header class="site-header">
        <div class="container">
            <div class="site-header-inner">
                <div class="brand header-brand">
                    <ul class="footer-links list-reset">
                        <h4 class="hero-title mt-0">
                            <a href="../../">
                                <span class="LogoBox"><ui class="LogoName"></span></a><ui class="LogoPage"><ui class="LogoVersion"></ui></h4>
                            </head>
                        </header>

<!-- ΠΊΠ°ΡΠ°Π»ΠΎΠ³ ΡΠΈΠ»ΡΠΌΠΎΠ² -->
<section class="hero2"></section>

<section class="hero1"><div class="container"><div class="hero-inner"><div class="hero-copy"><div class="film">
    <div class="name">{ΠΠΌΡ}<p class="number">{ΠΠΎΠ·ΡΠ°ΡΡ}</p></div></div><div class="im">
    <img src="image.png" class="image" onerror="this.style.visibility = 'hidden'" width="170px" height = "250px"><div class="hero-cta">
    {Button}</section><section class="hero1"><div class="container"><p class="buttonns"><p>
    <iframe class="fonv" src="{ΠΠΈΠ΄Π΅ΠΎ}" frameborder="0" allowfullscreen></iframe></div></div></div>       
    <meta property="og:title" content="{ΠΠΌΡ}">
    <title>ALED | {ΠΠΌΡ}</title>
</section>

</html>""")

os.system('cls')
print('   ')
cn.print(f'{R}βββ AledCreatik βββ', justify="center")
num = 0
for dirpath, dirnames, filenames in os.walk("./page"):
    for dirname in dirnames:
        num += 1
        pass
nun = f'{num}      '
num += 1
cn.print(Π€ΠΎΡΠΌΠ°Ρ_App, justify="center")

____________________ΠΠΌΡ = F'{ΠΠΌΡ}                                                       '
________________ΠΠΎΠ·ΡΠ°ΡΡ = F'{ΠΠΎΠ·ΡΠ°ΡΡ}                                                   '
cn.print(f'{G}βββ Π€ΠΈΠ»ΡΠΌ ΡΠ³Π΅Π½Π΅ΡΠΈΡΠΎΠ²Π°Π½ βββ', justify="center")
cn.print(f'{E}ββββββββββββββββββββββββββββββββββββββββββββββββββββββββββ{E}{E}{E}{E}{E}β', justify="center")
cn.print(f'{E}β{W} ΠΠ°Π·Π²Π°Π½ΠΈΠ΅: {R}{R}{R}{R}{R}{____________________ΠΠΌΡ[:45]} {Y}{Y}{Y}{E}β', justify="center")
cn.print(f'{E}β{W} ΠΠΎΠ·ΡΠ°ΡΠ½ΠΎΠ΅ ΠΎΠ³ΡΠ°Π½ΠΈΠ΅Π½ΠΈΠ΅: {R}{________________ΠΠΎΠ·ΡΠ°ΡΡ[:33]} {Y}{Y}{Y}{E}β', justify="center")
cn.print(f'{E}ββββββββββββββββββββββββββββββββββββββββββββββββ{Y} ID: {num} {E}β{E}{E}β', justify="center")
cn.print()
cn.print(f'{W}   URL ΠΠ½ΡΠΎΡΠΌΠ°ΡΠΈΡ: {B}{ΠΠ½ΠΎΠΏΠΊΠ°}')
cn.print(f'{W}   URL ΠΠΈΠ΄Π΅ΠΎ: {B}{ΠΠΈΠ΄Π΅ΠΎ}')
cn.print()
cn.print()

# Π‘ΠΎΠ·Π΄Π°ΡΡ ΠΏΠ°ΠΏΠΊΡ Π΄Π»Ρ ΡΠΈΠ»ΡΠΌΠ°
if not os.path.exists(f'./{DIR}'): 
    os.makedirs(f'./{DIR}')

# ΠΠ·ΠΌΠ΅Π½Π΅Π½ΠΈΠ΅ ΠΊΠ°ΡΠ°Π»ΠΎΠ³Π°
with open('./index.html', 'r', encoding='utf8') as Π€Π°ΠΉΠ»:
    lines = Π€Π°ΠΉΠ».readlines()
lines.insert(50, f'''
<section class="hero1"><div class="container"><div class="hero-inner"><div class="hero-copy"><div class="film">
    <h1 class="name">{ΠΠΌΡ}
    <p class="number">{ΠΠΎΠ·ΡΠ°ΡΡ}</p></h1></div>
    <div class="im"><img src="page/{num}/image.png" class="image" onerror="this.style.visibility = 'hidden'" width="170px" height = "250px"><div class="hero-cta">
    <a class="buttonn"  href="page/{num}/">Π‘ΠΌΠΎΡΡΠ΅ΡΡ</a>
</section>
''')
Π€Π°ΠΉΠ» = open('./index.html', 'w+', encoding='utf8')
Π€Π°ΠΉΠ».writelines(lines)

# Π‘ΠΎΠ·Π΄Π°Π½ΠΈΠ΅ ΠΈΠ·ΠΎΠ±ΡΠ°ΠΆΠ΅Π½ΠΈΡ
if imgLOG in '1':
    FILE = Image.open('icon/image.png')
    FILE = FILE.save(f'./{DIR}/image.png')
if imgLOG in '2':
    FILE = Image.open(ΠΠ·ΠΎΠ±ΡΠ°ΠΆΠ΅Π½ΠΈΠ΅)  
    FILE = FILE.save(F'./{DIR}/image.png')
if imgLOG in '3':
    FILE = open(f'./{DIR}/{FILE}', 'wb')
    FILE.write(ΠΠ°Π½Π½ΡΠ΅)
    FILE.close()

# Π‘ΡΡΠ°Π½ΠΈΡΠ° ΡΠΈΠ»ΡΠΌΠ°
Π€ΠΈΠ»ΡΠΌ = open(F"./{DIR}/index.html", "w+", encoding='utf8')
Π€ΠΈΠ»ΡΠΌ.write(Π‘ΡΡΠ°Π½ΠΈΡΠ°)
Π€ΠΈΠ»ΡΠΌ.close()