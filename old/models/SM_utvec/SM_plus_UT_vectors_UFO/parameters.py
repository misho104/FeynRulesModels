# This file was automatically created by FeynRules 1.6.6
# Mathematica version: 8.0 for Microsoft Windows (32-bit) (December 7, 2010)
# Date: Wed 27 Jun 2012 18:38:15



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
               texname = '\\alpha _s',
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
                 value = 0.00255,
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
                value = 172,
                texname = '\\text{ymt}',
                lhablock = 'YUKAWA',
                lhacode = [ 6 ])

yme = Parameter(name = 'yme',
                nature = 'external',
                type = 'real',
                value = 0.000511,
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

MxW = Parameter(name = 'MxW',
                nature = 'external',
                type = 'real',
                value = 200,
                texname = '\\text{M}_{\\text{W}\'}',
                lhablock = 'FRBlock',
                lhacode = [ 1 ])

WxW = Parameter(name = 'WxW',
                nature = 'external',
                type = 'real',
                value = 0,
                texname = '\\text{W}_{\\text{W}\'}',
                lhablock = 'FRBlock',
                lhacode = [ 2 ])

MxZ = Parameter(name = 'MxZ',
                nature = 'external',
                type = 'real',
                value = 200,
                texname = '\\text{M}_{\\text{Z}\'}',
                lhablock = 'FRBlock',
                lhacode = [ 3 ])

WxZ = Parameter(name = 'WxZ',
                nature = 'external',
                type = 'real',
                value = 0,
                texname = '\\text{W}_{\\text{Z}\'}',
                lhablock = 'FRBlock',
                lhacode = [ 4 ])

gWprimeL = Parameter(name = 'gWprimeL',
                     nature = 'external',
                     type = 'real',
                     value = 1.,
                     texname = '\\text{g}_{\\text{L} \\text{W}\'}',
                     lhablock = 'FRBlock',
                     lhacode = [ 5 ])

gWprimeR = Parameter(name = 'gWprimeR',
                     nature = 'external',
                     type = 'real',
                     value = 1.,
                     texname = '\\text{g}_{\\text{R} \\text{W}\'}',
                     lhablock = 'FRBlock',
                     lhacode = [ 6 ])

gZprimeUT = Parameter(name = 'gZprimeUT',
                      nature = 'external',
                      type = 'real',
                      value = 1.,
                      texname = '\\text{g}_{\\text{UT} \\text{Z}\'}',
                      lhablock = 'FRBlock',
                      lhacode = [ 7 ])

gZprimeUU = Parameter(name = 'gZprimeUU',
                      nature = 'external',
                      type = 'real',
                      value = 1.,
                      texname = '\\text{g}_{\\text{UU} \\text{Z}\'}',
                      lhablock = 'FRBlock',
                      lhacode = [ 8 ])

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.1876,
               texname = '\\text{MZ}',
               lhablock = 'MASS',
               lhacode = [ 23 ])

Me = Parameter(name = 'Me',
               nature = 'external',
               type = 'real',
               value = 0.000511,
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
               value = 0.00255,
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
               value = 172,
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

MH = Parameter(name = 'MH',
               nature = 'external',
               type = 'real',
               value = 120,
               texname = '\\text{MH}',
               lhablock = 'MASS',
               lhacode = [ 25 ])

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

WT = Parameter(name = 'WT',
               nature = 'external',
               type = 'real',
               value = 1.50833649,
               texname = '\\text{WT}',
               lhablock = 'DECAY',
               lhacode = [ 6 ])

WH = Parameter(name = 'WH',
               nature = 'external',
               type = 'real',
               value = 0.00575308848,
               texname = '\\text{WH}',
               lhablock = 'DECAY',
               lhacode = [ 25 ])

aEW = Parameter(name = 'aEW',
                nature = 'internal',
                type = 'real',
                value = '1/aEWM1',
                texname = '\\alpha _{\\text{EW}}')

gw = Parameter(name = 'gw',
               nature = 'internal',
               type = 'real',
               value = '1',
               texname = 'g_w')

g1 = Parameter(name = 'g1',
               nature = 'internal',
               type = 'real',
               value = '1',
               texname = 'g_1')

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

vev = Parameter(name = 'vev',
                nature = 'internal',
                type = 'real',
                value = '(2*MW*sw)/ee',
                texname = '\\text{vev}')

lam = Parameter(name = 'lam',
                nature = 'internal',
                type = 'real',
                value = 'MH**2/(2.*vev**2)',
                texname = '\\text{lam}')

yb = Parameter(name = 'yb',
               nature = 'internal',
               type = 'real',
               value = '(ymb*cmath.sqrt(2))/vev',
               texname = '\\text{yb}')

yc = Parameter(name = 'yc',
               nature = 'internal',
               type = 'real',
               value = '(ymc*cmath.sqrt(2))/vev',
               texname = '\\text{yc}')

ydo = Parameter(name = 'ydo',
                nature = 'internal',
                type = 'real',
                value = '(ymdo*cmath.sqrt(2))/vev',
                texname = '\\text{ydo}')

ye = Parameter(name = 'ye',
               nature = 'internal',
               type = 'real',
               value = '(yme*cmath.sqrt(2))/vev',
               texname = '\\text{ye}')

ym = Parameter(name = 'ym',
               nature = 'internal',
               type = 'real',
               value = '(ymm*cmath.sqrt(2))/vev',
               texname = '\\text{ym}')

ys = Parameter(name = 'ys',
               nature = 'internal',
               type = 'real',
               value = '(yms*cmath.sqrt(2))/vev',
               texname = '\\text{ys}')

yt = Parameter(name = 'yt',
               nature = 'internal',
               type = 'real',
               value = '(ymt*cmath.sqrt(2))/vev',
               texname = '\\text{yt}')

ytau = Parameter(name = 'ytau',
                 nature = 'internal',
                 type = 'real',
                 value = '(ymtau*cmath.sqrt(2))/vev',
                 texname = '\\text{ytau}')

yup = Parameter(name = 'yup',
                nature = 'internal',
                type = 'real',
                value = '(ymup*cmath.sqrt(2))/vev',
                texname = '\\text{yup}')

muH = Parameter(name = 'muH',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(lam*vev**2)',
                texname = '\\mu')

I1x11 = Parameter(name = 'I1x11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ydo*complexconjugate(CKM11)',
                  texname = '\\text{I1x11}')

I1x12 = Parameter(name = 'I1x12',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ydo*complexconjugate(CKM21)',
                  texname = '\\text{I1x12}')

I1x13 = Parameter(name = 'I1x13',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ydo*complexconjugate(CKM31)',
                  texname = '\\text{I1x13}')

I1x21 = Parameter(name = 'I1x21',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ys*complexconjugate(CKM12)',
                  texname = '\\text{I1x21}')

I1x22 = Parameter(name = 'I1x22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ys*complexconjugate(CKM22)',
                  texname = '\\text{I1x22}')

I1x23 = Parameter(name = 'I1x23',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ys*complexconjugate(CKM32)',
                  texname = '\\text{I1x23}')

I1x31 = Parameter(name = 'I1x31',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yb*complexconjugate(CKM13)',
                  texname = '\\text{I1x31}')

I1x32 = Parameter(name = 'I1x32',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yb*complexconjugate(CKM23)',
                  texname = '\\text{I1x32}')

I1x33 = Parameter(name = 'I1x33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yb*complexconjugate(CKM33)',
                  texname = '\\text{I1x33}')

I2x11 = Parameter(name = 'I2x11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yup*complexconjugate(CKM11)',
                  texname = '\\text{I2x11}')

I2x12 = Parameter(name = 'I2x12',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yc*complexconjugate(CKM21)',
                  texname = '\\text{I2x12}')

I2x13 = Parameter(name = 'I2x13',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yt*complexconjugate(CKM31)',
                  texname = '\\text{I2x13}')

I2x21 = Parameter(name = 'I2x21',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yup*complexconjugate(CKM12)',
                  texname = '\\text{I2x21}')

I2x22 = Parameter(name = 'I2x22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yc*complexconjugate(CKM22)',
                  texname = '\\text{I2x22}')

I2x23 = Parameter(name = 'I2x23',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yt*complexconjugate(CKM32)',
                  texname = '\\text{I2x23}')

I2x31 = Parameter(name = 'I2x31',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yup*complexconjugate(CKM13)',
                  texname = '\\text{I2x31}')

I2x32 = Parameter(name = 'I2x32',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yc*complexconjugate(CKM23)',
                  texname = '\\text{I2x32}')

I2x33 = Parameter(name = 'I2x33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yt*complexconjugate(CKM33)',
                  texname = '\\text{I2x33}')

I3x11 = Parameter(name = 'I3x11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM11*yup',
                  texname = '\\text{I3x11}')

I3x12 = Parameter(name = 'I3x12',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM21*yc',
                  texname = '\\text{I3x12}')

I3x13 = Parameter(name = 'I3x13',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM31*yt',
                  texname = '\\text{I3x13}')

I3x21 = Parameter(name = 'I3x21',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM12*yup',
                  texname = '\\text{I3x21}')

I3x22 = Parameter(name = 'I3x22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM22*yc',
                  texname = '\\text{I3x22}')

I3x23 = Parameter(name = 'I3x23',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM32*yt',
                  texname = '\\text{I3x23}')

I3x31 = Parameter(name = 'I3x31',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM13*yup',
                  texname = '\\text{I3x31}')

I3x32 = Parameter(name = 'I3x32',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM23*yc',
                  texname = '\\text{I3x32}')

I3x33 = Parameter(name = 'I3x33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM33*yt',
                  texname = '\\text{I3x33}')

I4x11 = Parameter(name = 'I4x11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM11*ydo',
                  texname = '\\text{I4x11}')

I4x12 = Parameter(name = 'I4x12',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM21*ydo',
                  texname = '\\text{I4x12}')

I4x13 = Parameter(name = 'I4x13',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM31*ydo',
                  texname = '\\text{I4x13}')

I4x21 = Parameter(name = 'I4x21',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM12*ys',
                  texname = '\\text{I4x21}')

I4x22 = Parameter(name = 'I4x22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM22*ys',
                  texname = '\\text{I4x22}')

I4x23 = Parameter(name = 'I4x23',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM32*ys',
                  texname = '\\text{I4x23}')

I4x31 = Parameter(name = 'I4x31',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM13*yb',
                  texname = '\\text{I4x31}')

I4x32 = Parameter(name = 'I4x32',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM23*yb',
                  texname = '\\text{I4x32}')

I4x33 = Parameter(name = 'I4x33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM33*yb',
                  texname = '\\text{I4x33}')

