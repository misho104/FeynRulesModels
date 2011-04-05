# This file was automatically created by FeynRules $Revision: 535 $
# Mathematica version: 7.0 for Microsoft Windows (32-bit) (April 23, 2009)
# Date: Wed 6 Apr 2011 01:53:58



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# User-defined parameters.
cabi = Parameter(name = 'cabi',
                 nature = 'external',
                 type = 'real',
                 value = 0.227736,
                 texname = '\\theta _c',
                 lhablock = 'CKMBLOCK',
                 lhacode = [ 1 ])

aEWM1 = Parameter(name = 'aEWM1',
                  nature = 'external',
                  type = 'real',
                  value = 127.9,
                  texname = '\\text{aEWM1}',
                  lhablock = 'SMINPUTS',
                  lhacode = [ 1 ])

Gf = Parameter(name = 'Gf',
               nature = 'external',
               type = 'real',
               value = 0.0000116637,
               texname = 'G_f',
               lhablock = 'SMINPUTS',
               lhacode = [ 2 ])

aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.1184,
               texname = '\\text{aS}',
               lhablock = 'SMINPUTS',
               lhacode = [ 3 ])

ymdo = Parameter(name = 'ymdo',
                 nature = 'external',
                 type = 'real',
                 value = 0.00504,
                 texname = '\\text{ymdo}',
                 lhablock = 'YUKAWA',
                 lhacode = [ 1 ])

ymup = Parameter(name = 'ymup',
                 nature = 'external',
                 type = 'real',
                 value = 0.0025499999999999997,
                 texname = '\\text{ymup}',
                 lhablock = 'YUKAWA',
                 lhacode = [ 2 ])

yms = Parameter(name = 'yms',
                nature = 'external',
                type = 'real',
                value = 0.101,
                texname = '\\text{yms}',
                lhablock = 'YUKAWA',
                lhacode = [ 3 ])

ymc = Parameter(name = 'ymc',
                nature = 'external',
                type = 'real',
                value = 1.27,
                texname = '\\text{ymc}',
                lhablock = 'YUKAWA',
                lhacode = [ 4 ])

ymb = Parameter(name = 'ymb',
                nature = 'external',
                type = 'real',
                value = 4.7,
                texname = '\\text{ymb}',
                lhablock = 'YUKAWA',
                lhacode = [ 5 ])

ymt = Parameter(name = 'ymt',
                nature = 'external',
                type = 'real',
                value = 172.,
                texname = '\\text{ymt}',
                lhablock = 'YUKAWA',
                lhacode = [ 6 ])

yme = Parameter(name = 'yme',
                nature = 'external',
                type = 'real',
                value = 0.0005110000000000001,
                texname = '\\text{yme}',
                lhablock = 'YUKAWA',
                lhacode = [ 11 ])

ymm = Parameter(name = 'ymm',
                nature = 'external',
                type = 'real',
                value = 0.10566,
                texname = '\\text{ymm}',
                lhablock = 'YUKAWA',
                lhacode = [ 13 ])

ymtau = Parameter(name = 'ymtau',
                  nature = 'external',
                  type = 'real',
                  value = 1.777,
                  texname = '\\text{ymtau}',
                  lhablock = 'YUKAWA',
                  lhacode = [ 15 ])

Msq = Parameter(name = 'Msq',
                nature = 'external',
                type = 'real',
                value = 200,
                texname = 'M_{\\text{sq}}',
                lhablock = 'FRBlock',
                lhacode = [ 1 ])

Wsq = Parameter(name = 'Wsq',
                nature = 'external',
                type = 'real',
                value = 0,
                texname = 'W_{\\text{sq}}',
                lhablock = 'FRBlock',
                lhacode = [ 2 ])

UDD312 = Parameter(name = 'UDD312',
                   nature = 'external',
                   type = 'real',
                   value = 1.,
                   texname = '\\lambda _{312}^{\\prime\\prime }',
                   lhablock = 'FRBlock',
                   lhacode = [ 3 ])

UDD313 = Parameter(name = 'UDD313',
                   nature = 'external',
                   type = 'real',
                   value = 1.,
                   texname = '\\lambda _{313}^{\\prime\\prime }',
                   lhablock = 'FRBlock',
                   lhacode = [ 4 ])

Me = Parameter(name = 'Me',
               nature = 'external',
               type = 'real',
               value = 0.0005110000000000001,
               texname = '\\text{Me}',
               lhablock = 'MASS',
               lhacode = [ 11 ])

MM = Parameter(name = 'MM',
               nature = 'external',
               type = 'real',
               value = 0.10566,
               texname = '\\text{MM}',
               lhablock = 'MASS',
               lhacode = [ 13 ])

MTA = Parameter(name = 'MTA',
                nature = 'external',
                type = 'real',
                value = 1.777,
                texname = '\\text{MTA}',
                lhablock = 'MASS',
                lhacode = [ 15 ])

MU = Parameter(name = 'MU',
               nature = 'external',
               type = 'real',
               value = 0.0025499999999999997,
               texname = 'M',
               lhablock = 'MASS',
               lhacode = [ 2 ])

MC = Parameter(name = 'MC',
               nature = 'external',
               type = 'real',
               value = 1.27,
               texname = '\\text{MC}',
               lhablock = 'MASS',
               lhacode = [ 4 ])

MT = Parameter(name = 'MT',
               nature = 'external',
               type = 'real',
               value = 172.,
               texname = '\\text{MT}',
               lhablock = 'MASS',
               lhacode = [ 6 ])

MD = Parameter(name = 'MD',
               nature = 'external',
               type = 'real',
               value = 0.00504,
               texname = '\\text{MD}',
               lhablock = 'MASS',
               lhacode = [ 1 ])

MS = Parameter(name = 'MS',
               nature = 'external',
               type = 'real',
               value = 0.101,
               texname = '\\text{MS}',
               lhablock = 'MASS',
               lhacode = [ 3 ])

MB = Parameter(name = 'MB',
               nature = 'external',
               type = 'real',
               value = 4.7,
               texname = '\\text{MB}',
               lhablock = 'MASS',
               lhacode = [ 5 ])

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.1876,
               texname = '\\text{MZ}',
               lhablock = 'MASS',
               lhacode = [ 23 ])

MH = Parameter(name = 'MH',
               nature = 'external',
               type = 'real',
               value = 120,
               texname = '\\text{MH}',
               lhablock = 'MASS',
               lhacode = [ 25 ])

MsuL = Parameter(name = 'MsuL',
                 nature = 'external',
                 type = 'real',
                 value = Msq,
                 texname = '\\text{MsuL}',
                 lhablock = 'MASS',
                 lhacode = [ 1000002 ])

MscL = Parameter(name = 'MscL',
                 nature = 'external',
                 type = 'real',
                 value = Msq,
                 texname = '\\text{MscL}',
                 lhablock = 'MASS',
                 lhacode = [ 1000004 ])

MstL = Parameter(name = 'MstL',
                 nature = 'external',
                 type = 'real',
                 value = Msq,
                 texname = '\\text{MstL}',
                 lhablock = 'MASS',
                 lhacode = [ 1000006 ])

MsuR = Parameter(name = 'MsuR',
                 nature = 'external',
                 type = 'real',
                 value = Msq,
                 texname = '\\text{MsuR}',
                 lhablock = 'MASS',
                 lhacode = [ 2000002 ])

MscR = Parameter(name = 'MscR',
                 nature = 'external',
                 type = 'real',
                 value = Msq,
                 texname = '\\text{MscR}',
                 lhablock = 'MASS',
                 lhacode = [ 2000004 ])

MstR = Parameter(name = 'MstR',
                 nature = 'external',
                 type = 'real',
                 value = Msq,
                 texname = '\\text{MstR}',
                 lhablock = 'MASS',
                 lhacode = [ 2000006 ])

MsdL = Parameter(name = 'MsdL',
                 nature = 'external',
                 type = 'real',
                 value = Msq,
                 texname = '\\text{MsdL}',
                 lhablock = 'MASS',
                 lhacode = [ 1000001 ])

MssL = Parameter(name = 'MssL',
                 nature = 'external',
                 type = 'real',
                 value = Msq,
                 texname = '\\text{MssL}',
                 lhablock = 'MASS',
                 lhacode = [ 1000003 ])

MsbL = Parameter(name = 'MsbL',
                 nature = 'external',
                 type = 'real',
                 value = Msq,
                 texname = '\\text{MsbL}',
                 lhablock = 'MASS',
                 lhacode = [ 1000005 ])

MsdR = Parameter(name = 'MsdR',
                 nature = 'external',
                 type = 'real',
                 value = Msq,
                 texname = '\\text{MsdR}',
                 lhablock = 'MASS',
                 lhacode = [ 2000001 ])

MssR = Parameter(name = 'MssR',
                 nature = 'external',
                 type = 'real',
                 value = Msq,
                 texname = '\\text{MssR}',
                 lhablock = 'MASS',
                 lhacode = [ 2000003 ])

MsbR = Parameter(name = 'MsbR',
                 nature = 'external',
                 type = 'real',
                 value = Msq,
                 texname = '\\text{MsbR}',
                 lhablock = 'MASS',
                 lhacode = [ 2000005 ])

WT = Parameter(name = 'WT',
               nature = 'external',
               type = 'real',
               value = 1.50833649,
               texname = '\\text{WT}',
               lhablock = 'DECAY',
               lhacode = [ 6 ])

WZ = Parameter(name = 'WZ',
               nature = 'external',
               type = 'real',
               value = 2.4952,
               texname = '\\text{WZ}',
               lhablock = 'DECAY',
               lhacode = [ 23 ])

WW = Parameter(name = 'WW',
               nature = 'external',
               type = 'real',
               value = 2.085,
               texname = '\\text{WW}',
               lhablock = 'DECAY',
               lhacode = [ 24 ])

WH = Parameter(name = 'WH',
               nature = 'external',
               type = 'real',
               value = 0.00575308848,
               texname = '\\text{WH}',
               lhablock = 'DECAY',
               lhacode = [ 25 ])

WsuL = Parameter(name = 'WsuL',
                 nature = 'external',
                 type = 'real',
                 value = Wsq,
                 texname = '\\text{WsuL}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000002 ])

WscL = Parameter(name = 'WscL',
                 nature = 'external',
                 type = 'real',
                 value = Wsq,
                 texname = '\\text{WscL}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000004 ])

WstL = Parameter(name = 'WstL',
                 nature = 'external',
                 type = 'real',
                 value = Wsq,
                 texname = '\\text{WstL}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000006 ])

WsuR = Parameter(name = 'WsuR',
                 nature = 'external',
                 type = 'real',
                 value = Wsq,
                 texname = '\\text{WsuR}',
                 lhablock = 'DECAY',
                 lhacode = [ 2000002 ])

WscR = Parameter(name = 'WscR',
                 nature = 'external',
                 type = 'real',
                 value = Wsq,
                 texname = '\\text{WscR}',
                 lhablock = 'DECAY',
                 lhacode = [ 2000004 ])

WstR = Parameter(name = 'WstR',
                 nature = 'external',
                 type = 'real',
                 value = Wsq,
                 texname = '\\text{WstR}',
                 lhablock = 'DECAY',
                 lhacode = [ 2000006 ])

WsdL = Parameter(name = 'WsdL',
                 nature = 'external',
                 type = 'real',
                 value = Wsq,
                 texname = '\\text{WsdL}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000001 ])

WssL = Parameter(name = 'WssL',
                 nature = 'external',
                 type = 'real',
                 value = Wsq,
                 texname = '\\text{WssL}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000003 ])

WsbL = Parameter(name = 'WsbL',
                 nature = 'external',
                 type = 'real',
                 value = Wsq,
                 texname = '\\text{WsbL}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000005 ])

WsdR = Parameter(name = 'WsdR',
                 nature = 'external',
                 type = 'real',
                 value = Wsq,
                 texname = '\\text{WsdR}',
                 lhablock = 'DECAY',
                 lhacode = [ 2000001 ])

WssR = Parameter(name = 'WssR',
                 nature = 'external',
                 type = 'real',
                 value = Wsq,
                 texname = '\\text{WssR}',
                 lhablock = 'DECAY',
                 lhacode = [ 2000003 ])

WsbR = Parameter(name = 'WsbR',
                 nature = 'external',
                 type = 'real',
                 value = Wsq,
                 texname = '\\text{WsbR}',
                 lhablock = 'DECAY',
                 lhacode = [ 2000005 ])

aEW = Parameter(name = 'aEW',
                nature = 'internal',
                type = 'real',
                value = '1/aEWM1',
                texname = '\\text{aEW}')

G = Parameter(name = 'G',
              nature = 'internal',
              type = 'real',
              value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
              texname = 'G')

CKM11 = Parameter(name = 'CKM11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'cmath.cos(cabi)',
                  texname = '\\text{CKM11}')

CKM12 = Parameter(name = 'CKM12',
                  nature = 'internal',
                  type = 'complex',
                  value = 'cmath.sin(cabi)',
                  texname = '\\text{CKM12}')

CKM13 = Parameter(name = 'CKM13',
                  nature = 'internal',
                  type = 'complex',
                  value = '0',
                  texname = '\\text{CKM13}')

CKM21 = Parameter(name = 'CKM21',
                  nature = 'internal',
                  type = 'complex',
                  value = '-cmath.sin(cabi)',
                  texname = '\\text{CKM21}')

CKM22 = Parameter(name = 'CKM22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'cmath.cos(cabi)',
                  texname = '\\text{CKM22}')

CKM23 = Parameter(name = 'CKM23',
                  nature = 'internal',
                  type = 'complex',
                  value = '0',
                  texname = '\\text{CKM23}')

CKM31 = Parameter(name = 'CKM31',
                  nature = 'internal',
                  type = 'complex',
                  value = '0',
                  texname = '\\text{CKM31}')

CKM32 = Parameter(name = 'CKM32',
                  nature = 'internal',
                  type = 'complex',
                  value = '0',
                  texname = '\\text{CKM32}')

CKM33 = Parameter(name = 'CKM33',
                  nature = 'internal',
                  type = 'complex',
                  value = '1',
                  texname = '\\text{CKM33}')

MW = Parameter(name = 'MW',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(MZ**2/2. + cmath.sqrt(MZ**4/4. - (aEW*cmath.pi*MZ**2)/(Gf*cmath.sqrt(2))))',
               texname = 'M_W')

ee = Parameter(name = 'ee',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(aEW)*cmath.sqrt(cmath.pi)',
               texname = 'e')

sw2 = Parameter(name = 'sw2',
                nature = 'internal',
                type = 'real',
                value = '1 - MW**2/MZ**2',
                texname = '\\text{sw2}')

cw = Parameter(name = 'cw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1 - sw2)',
               texname = 'c_w')

sw = Parameter(name = 'sw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(sw2)',
               texname = 's_w')

g1 = Parameter(name = 'g1',
               nature = 'internal',
               type = 'real',
               value = 'ee/cw',
               texname = 'g_1')

gw = Parameter(name = 'gw',
               nature = 'internal',
               type = 'real',
               value = 'ee/sw',
               texname = 'g_w')

v = Parameter(name = 'v',
              nature = 'internal',
              type = 'real',
              value = '(2*MW*sw)/ee',
              texname = 'v')

lam = Parameter(name = 'lam',
                nature = 'internal',
                type = 'real',
                value = 'MH**2/(2.*v**2)',
                texname = '\\text{lam}')

yb = Parameter(name = 'yb',
               nature = 'internal',
               type = 'real',
               value = '(ymb*cmath.sqrt(2))/v',
               texname = '\\text{yb}')

yc = Parameter(name = 'yc',
               nature = 'internal',
               type = 'real',
               value = '(ymc*cmath.sqrt(2))/v',
               texname = '\\text{yc}')

ydo = Parameter(name = 'ydo',
                nature = 'internal',
                type = 'real',
                value = '(ymdo*cmath.sqrt(2))/v',
                texname = '\\text{ydo}')

ye = Parameter(name = 'ye',
               nature = 'internal',
               type = 'real',
               value = '(yme*cmath.sqrt(2))/v',
               texname = '\\text{ye}')

ym = Parameter(name = 'ym',
               nature = 'internal',
               type = 'real',
               value = '(ymm*cmath.sqrt(2))/v',
               texname = '\\text{ym}')

ys = Parameter(name = 'ys',
               nature = 'internal',
               type = 'real',
               value = '(yms*cmath.sqrt(2))/v',
               texname = '\\text{ys}')

yt = Parameter(name = 'yt',
               nature = 'internal',
               type = 'real',
               value = '(ymt*cmath.sqrt(2))/v',
               texname = '\\text{yt}')

ytau = Parameter(name = 'ytau',
                 nature = 'internal',
                 type = 'real',
                 value = '(ymtau*cmath.sqrt(2))/v',
                 texname = '\\text{ytau}')

yup = Parameter(name = 'yup',
                nature = 'internal',
                type = 'real',
                value = '(ymup*cmath.sqrt(2))/v',
                texname = '\\text{yup}')

muH = Parameter(name = 'muH',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(lam*v**2)',
                texname = '\\mu ')

