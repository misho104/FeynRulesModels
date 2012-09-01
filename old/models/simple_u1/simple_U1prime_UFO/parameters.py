# This file was automatically created by FeynRules 1.6.7
# Mathematica version: 8.0 for Mac OS X x86 (64-bit) (October 14, 2011)
# Date: Sat 1 Sep 2012 17:46:10



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# User-defined parameters.
aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.1184,
               texname = '\\text{aS}',
               lhablock = 'SMINPUTS',
               lhacode = [ 3 ])

lam = Parameter(name = 'lam',
                nature = 'external',
                type = 'real',
                value = 0.1,
                texname = '\\text{lam}',
                lhablock = 'FRBlock',
                lhacode = [ 1 ])

gX = Parameter(name = 'gX',
               nature = 'external',
               type = 'real',
               value = 0.2,
               texname = '\\text{gX}',
               lhablock = 'FRBlock',
               lhacode = [ 2 ])

qXphi = Parameter(name = 'qXphi',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = '\\text{qXphi}',
                  lhablock = 'FRBlock',
                  lhacode = [ 3 ])

qXpsiL = Parameter(name = 'qXpsiL',
                   nature = 'external',
                   type = 'real',
                   value = 2.,
                   texname = '\\text{qXpsiL}',
                   lhablock = 'FRBlock',
                   lhacode = [ 4 ])

qXpsiR = Parameter(name = 'qXpsiR',
                   nature = 'external',
                   type = 'real',
                   value = 1.,
                   texname = '\\text{qXpsiR}',
                   lhablock = 'FRBlock',
                   lhacode = [ 5 ])

qXuL = Parameter(name = 'qXuL',
                 nature = 'external',
                 type = 'real',
                 value = 3.,
                 texname = '\\text{qXuL}',
                 lhablock = 'FRBlock',
                 lhacode = [ 6 ])

qXdL = Parameter(name = 'qXdL',
                 nature = 'external',
                 type = 'real',
                 value = 3.,
                 texname = '\\text{qXdL}',
                 lhablock = 'FRBlock',
                 lhacode = [ 7 ])

qXuR = Parameter(name = 'qXuR',
                 nature = 'external',
                 type = 'real',
                 value = 2.,
                 texname = '\\text{qXuR}',
                 lhablock = 'FRBlock',
                 lhacode = [ 8 ])

qXdR = Parameter(name = 'qXdR',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = '\\text{qXdR}',
                 lhablock = 'FRBlock',
                 lhacode = [ 9 ])

mZp = Parameter(name = 'mZp',
                nature = 'external',
                type = 'real',
                value = 600,
                texname = '\\text{mZp}',
                lhablock = 'FRBlock',
                lhacode = [ 10 ])

mphi = Parameter(name = 'mphi',
                 nature = 'external',
                 type = 'real',
                 value = 200,
                 texname = '\\text{mphi}',
                 lhablock = 'FRBlock',
                 lhacode = [ 11 ])

mpsi = Parameter(name = 'mpsi',
                 nature = 'external',
                 type = 'real',
                 value = 100,
                 texname = '\\text{mpsi}',
                 lhablock = 'FRBlock',
                 lhacode = [ 12 ])

wZp = Parameter(name = 'wZp',
                nature = 'external',
                type = 'real',
                value = 0.5,
                texname = '\\text{wZp}',
                lhablock = 'FRBlock',
                lhacode = [ 13 ])

wphi = Parameter(name = 'wphi',
                 nature = 'external',
                 type = 'real',
                 value = 0.4,
                 texname = '\\text{wphi}',
                 lhablock = 'FRBlock',
                 lhacode = [ 14 ])

wpsi = Parameter(name = 'wpsi',
                 nature = 'external',
                 type = 'real',
                 value = 0.3,
                 texname = '\\text{wpsi}',
                 lhablock = 'FRBlock',
                 lhacode = [ 15 ])

mZp = Parameter(name = 'mZp',
                nature = 'external',
                type = 'real',
                value = 200,
                texname = '\\text{mZp}',
                lhablock = 'MASS',
                lhacode = [ 9000001 ])

mphi = Parameter(name = 'mphi',
                 nature = 'external',
                 type = 'real',
                 value = 200,
                 texname = '\\text{mphi}',
                 lhablock = 'MASS',
                 lhacode = [ 9000004 ])

mpsi = Parameter(name = 'mpsi',
                 nature = 'external',
                 type = 'real',
                 value = 100,
                 texname = '\\text{mpsi}',
                 lhablock = 'MASS',
                 lhacode = [ 9000005 ])

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

wZp = Parameter(name = 'wZp',
                nature = 'external',
                type = 'real',
                value = 0.4,
                texname = '\\text{wZp}',
                lhablock = 'DECAY',
                lhacode = [ 9000001 ])

wphi = Parameter(name = 'wphi',
                 nature = 'external',
                 type = 'real',
                 value = 0.4,
                 texname = '\\text{wphi}',
                 lhablock = 'DECAY',
                 lhacode = [ 9000004 ])

wpsi = Parameter(name = 'wpsi',
                 nature = 'external',
                 type = 'real',
                 value = 0.3,
                 texname = '\\text{wpsi}',
                 lhablock = 'DECAY',
                 lhacode = [ 9000005 ])

WT = Parameter(name = 'WT',
               nature = 'external',
               type = 'real',
               value = 1.50833649,
               texname = '\\text{WT}',
               lhablock = 'DECAY',
               lhacode = [ 6 ])

gs = Parameter(name = 'gs',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
               texname = '\\text{gs}')

