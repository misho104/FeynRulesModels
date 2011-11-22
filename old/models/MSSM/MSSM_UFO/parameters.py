# This file was automatically created by FeynRules $Revision: 634 $
# Mathematica version: 7.0 for Linux x86 (32-bit) (April 23, 2009)
# Date: Tue 22 Nov 2011 02:10:01



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# User-defined parameters.
RRd11 = Parameter(name = 'RRd11',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = '\\text{RRd11}',
                  lhablock = 'DSQMIX',
                  lhacode = [ 1, 1 ])

RRd22 = Parameter(name = 'RRd22',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = '\\text{RRd22}',
                  lhablock = 'DSQMIX',
                  lhacode = [ 2, 2 ])

RRd33 = Parameter(name = 'RRd33',
                  nature = 'external',
                  type = 'real',
                  value = 0.938737896,
                  texname = '\\text{RRd33}',
                  lhablock = 'DSQMIX',
                  lhacode = [ 3, 3 ])

RRd36 = Parameter(name = 'RRd36',
                  nature = 'external',
                  type = 'real',
                  value = 0.344631925,
                  texname = '\\text{RRd36}',
                  lhablock = 'DSQMIX',
                  lhacode = [ 3, 6 ])

RRd44 = Parameter(name = 'RRd44',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = '\\text{RRd44}',
                  lhablock = 'DSQMIX',
                  lhacode = [ 4, 4 ])

RRd55 = Parameter(name = 'RRd55',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = '\\text{RRd55}',
                  lhablock = 'DSQMIX',
                  lhacode = [ 5, 5 ])

RRd63 = Parameter(name = 'RRd63',
                  nature = 'external',
                  type = 'real',
                  value = -0.344631925,
                  texname = '\\text{RRd63}',
                  lhablock = 'DSQMIX',
                  lhacode = [ 6, 3 ])

RRd66 = Parameter(name = 'RRd66',
                  nature = 'external',
                  type = 'real',
                  value = 0.938737896,
                  texname = '\\text{RRd66}',
                  lhablock = 'DSQMIX',
                  lhacode = [ 6, 6 ])

alp = Parameter(name = 'alp',
                nature = 'external',
                type = 'real',
                value = -0.11382521,
                texname = '\\alpha ',
                lhablock = 'FRALPHA',
                lhacode = [ 1 ])

RMUH = Parameter(name = 'RMUH',
                 nature = 'external',
                 type = 'real',
                 value = 357.680977,
                 texname = '\\text{RMUH}',
                 lhablock = 'HMIX',
                 lhacode = [ 1 ])

tb = Parameter(name = 'tb',
               nature = 'external',
               type = 'real',
               value = 9.74862403,
               texname = 't_b',
               lhablock = 'HMIX',
               lhacode = [ 2 ])

MA2 = Parameter(name = 'MA2',
                nature = 'external',
                type = 'real',
                value = 166439.065,
                texname = 'm_A^2',
                lhablock = 'HMIX',
                lhacode = [ 4 ])

RmD211 = Parameter(name = 'RmD211',
                   nature = 'external',
                   type = 'real',
                   value = 273684.674,
                   texname = '\\text{RmD211}',
                   lhablock = 'MSD2',
                   lhacode = [ 1, 1 ])

RmD222 = Parameter(name = 'RmD222',
                   nature = 'external',
                   type = 'real',
                   value = 273684.674,
                   texname = '\\text{RmD222}',
                   lhablock = 'MSD2',
                   lhacode = [ 2, 2 ])

RmD233 = Parameter(name = 'RmD233',
                   nature = 'external',
                   type = 'real',
                   value = 270261.969,
                   texname = '\\text{RmD233}',
                   lhablock = 'MSD2',
                   lhacode = [ 3, 3 ])

RmE211 = Parameter(name = 'RmE211',
                   nature = 'external',
                   type = 'real',
                   value = 18630.6287,
                   texname = '\\text{RmE211}',
                   lhablock = 'MSE2',
                   lhacode = [ 1, 1 ])

RmE222 = Parameter(name = 'RmE222',
                   nature = 'external',
                   type = 'real',
                   value = 18630.6287,
                   texname = '\\text{RmE222}',
                   lhablock = 'MSE2',
                   lhacode = [ 2, 2 ])

RmE233 = Parameter(name = 'RmE233',
                   nature = 'external',
                   type = 'real',
                   value = 17967.6406,
                   texname = '\\text{RmE233}',
                   lhablock = 'MSE2',
                   lhacode = [ 3, 3 ])

RmL211 = Parameter(name = 'RmL211',
                   nature = 'external',
                   type = 'real',
                   value = 38155.67,
                   texname = '\\text{RmL211}',
                   lhablock = 'MSL2',
                   lhacode = [ 1, 1 ])

RmL222 = Parameter(name = 'RmL222',
                   nature = 'external',
                   type = 'real',
                   value = 38155.67,
                   texname = '\\text{RmL222}',
                   lhablock = 'MSL2',
                   lhacode = [ 2, 2 ])

RmL233 = Parameter(name = 'RmL233',
                   nature = 'external',
                   type = 'real',
                   value = 37828.6769,
                   texname = '\\text{RmL233}',
                   lhablock = 'MSL2',
                   lhacode = [ 3, 3 ])

RMx1 = Parameter(name = 'RMx1',
                 nature = 'external',
                 type = 'real',
                 value = 101.396534,
                 texname = '\\text{RMx1}',
                 lhablock = 'MSOFT',
                 lhacode = [ 1 ])

RMx2 = Parameter(name = 'RMx2',
                 nature = 'external',
                 type = 'real',
                 value = 191.504241,
                 texname = '\\text{RMx2}',
                 lhablock = 'MSOFT',
                 lhacode = [ 2 ])

RMx3 = Parameter(name = 'RMx3',
                 nature = 'external',
                 type = 'real',
                 value = 588.263031,
                 texname = '\\text{RMx3}',
                 lhablock = 'MSOFT',
                 lhacode = [ 3 ])

mHu2 = Parameter(name = 'mHu2',
                 nature = 'external',
                 type = 'real',
                 value = 32337.4943,
                 texname = 'm_{H_u}^2',
                 lhablock = 'MSOFT',
                 lhacode = [ 21 ])

mHd2 = Parameter(name = 'mHd2',
                 nature = 'external',
                 type = 'real',
                 value = -128800.134,
                 texname = 'm_{H_d}^2',
                 lhablock = 'MSOFT',
                 lhacode = [ 22 ])

RmQ211 = Parameter(name = 'RmQ211',
                   nature = 'external',
                   type = 'real',
                   value = 299836.701,
                   texname = '\\text{RmQ211}',
                   lhablock = 'MSQ2',
                   lhacode = [ 1, 1 ])

RmQ222 = Parameter(name = 'RmQ222',
                   nature = 'external',
                   type = 'real',
                   value = 299836.701,
                   texname = '\\text{RmQ222}',
                   lhablock = 'MSQ2',
                   lhacode = [ 2, 2 ])

RmQ233 = Parameter(name = 'RmQ233',
                   nature = 'external',
                   type = 'real',
                   value = 248765.367,
                   texname = '\\text{RmQ233}',
                   lhablock = 'MSQ2',
                   lhacode = [ 3, 3 ])

RmU211 = Parameter(name = 'RmU211',
                   nature = 'external',
                   type = 'real',
                   value = 280382.106,
                   texname = '\\text{RmU211}',
                   lhablock = 'MSU2',
                   lhacode = [ 1, 1 ])

RmU222 = Parameter(name = 'RmU222',
                   nature = 'external',
                   type = 'real',
                   value = 280382.106,
                   texname = '\\text{RmU222}',
                   lhablock = 'MSU2',
                   lhacode = [ 2, 2 ])

RmU233 = Parameter(name = 'RmU233',
                   nature = 'external',
                   type = 'real',
                   value = 179137.072,
                   texname = '\\text{RmU233}',
                   lhablock = 'MSU2',
                   lhacode = [ 3, 3 ])

RNN11 = Parameter(name = 'RNN11',
                  nature = 'external',
                  type = 'real',
                  value = 0.98636443,
                  texname = '\\text{RNN11}',
                  lhablock = 'NMIX',
                  lhacode = [ 1, 1 ])

RNN12 = Parameter(name = 'RNN12',
                  nature = 'external',
                  type = 'real',
                  value = -0.0531103553,
                  texname = '\\text{RNN12}',
                  lhablock = 'NMIX',
                  lhacode = [ 1, 2 ])

RNN13 = Parameter(name = 'RNN13',
                  nature = 'external',
                  type = 'real',
                  value = 0.146433995,
                  texname = '\\text{RNN13}',
                  lhablock = 'NMIX',
                  lhacode = [ 1, 3 ])

RNN14 = Parameter(name = 'RNN14',
                  nature = 'external',
                  type = 'real',
                  value = -0.0531186117,
                  texname = '\\text{RNN14}',
                  lhablock = 'NMIX',
                  lhacode = [ 1, 4 ])

RNN21 = Parameter(name = 'RNN21',
                  nature = 'external',
                  type = 'real',
                  value = 0.0993505358,
                  texname = '\\text{RNN21}',
                  lhablock = 'NMIX',
                  lhacode = [ 2, 1 ])

RNN22 = Parameter(name = 'RNN22',
                  nature = 'external',
                  type = 'real',
                  value = 0.944949299,
                  texname = '\\text{RNN22}',
                  lhablock = 'NMIX',
                  lhacode = [ 2, 2 ])

RNN23 = Parameter(name = 'RNN23',
                  nature = 'external',
                  type = 'real',
                  value = -0.26984672,
                  texname = '\\text{RNN23}',
                  lhablock = 'NMIX',
                  lhacode = [ 2, 3 ])

RNN24 = Parameter(name = 'RNN24',
                  nature = 'external',
                  type = 'real',
                  value = 0.156150698,
                  texname = '\\text{RNN24}',
                  lhablock = 'NMIX',
                  lhacode = [ 2, 4 ])

RNN31 = Parameter(name = 'RNN31',
                  nature = 'external',
                  type = 'real',
                  value = -0.0603388002,
                  texname = '\\text{RNN31}',
                  lhablock = 'NMIX',
                  lhacode = [ 3, 1 ])

RNN32 = Parameter(name = 'RNN32',
                  nature = 'external',
                  type = 'real',
                  value = 0.0877004854,
                  texname = '\\text{RNN32}',
                  lhablock = 'NMIX',
                  lhacode = [ 3, 2 ])

RNN33 = Parameter(name = 'RNN33',
                  nature = 'external',
                  type = 'real',
                  value = 0.695877493,
                  texname = '\\text{RNN33}',
                  lhablock = 'NMIX',
                  lhacode = [ 3, 3 ])

RNN34 = Parameter(name = 'RNN34',
                  nature = 'external',
                  type = 'real',
                  value = 0.710226984,
                  texname = '\\text{RNN34}',
                  lhablock = 'NMIX',
                  lhacode = [ 3, 4 ])

RNN41 = Parameter(name = 'RNN41',
                  nature = 'external',
                  type = 'real',
                  value = -0.116507132,
                  texname = '\\text{RNN41}',
                  lhablock = 'NMIX',
                  lhacode = [ 4, 1 ])

RNN42 = Parameter(name = 'RNN42',
                  nature = 'external',
                  type = 'real',
                  value = 0.310739017,
                  texname = '\\text{RNN42}',
                  lhablock = 'NMIX',
                  lhacode = [ 4, 2 ])

RNN43 = Parameter(name = 'RNN43',
                  nature = 'external',
                  type = 'real',
                  value = 0.64922596,
                  texname = '\\text{RNN43}',
                  lhablock = 'NMIX',
                  lhacode = [ 4, 3 ])

RNN44 = Parameter(name = 'RNN44',
                  nature = 'external',
                  type = 'real',
                  value = -0.684377823,
                  texname = '\\text{RNN44}',
                  lhablock = 'NMIX',
                  lhacode = [ 4, 4 ])

RRl11 = Parameter(name = 'RRl11',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = '\\text{RRl11}',
                  lhablock = 'SELMIX',
                  lhacode = [ 1, 1 ])

RRl22 = Parameter(name = 'RRl22',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = '\\text{RRl22}',
                  lhablock = 'SELMIX',
                  lhacode = [ 2, 2 ])

RRl33 = Parameter(name = 'RRl33',
                  nature = 'external',
                  type = 'real',
                  value = 0.28248719,
                  texname = '\\text{RRl33}',
                  lhablock = 'SELMIX',
                  lhacode = [ 3, 3 ])

RRl36 = Parameter(name = 'RRl36',
                  nature = 'external',
                  type = 'real',
                  value = 0.959271071,
                  texname = '\\text{RRl36}',
                  lhablock = 'SELMIX',
                  lhacode = [ 3, 6 ])

RRl44 = Parameter(name = 'RRl44',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = '\\text{RRl44}',
                  lhablock = 'SELMIX',
                  lhacode = [ 4, 4 ])

RRl55 = Parameter(name = 'RRl55',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = '\\text{RRl55}',
                  lhablock = 'SELMIX',
                  lhacode = [ 5, 5 ])

RRl63 = Parameter(name = 'RRl63',
                  nature = 'external',
                  type = 'real',
                  value = 0.959271071,
                  texname = '\\text{RRl63}',
                  lhablock = 'SELMIX',
                  lhacode = [ 6, 3 ])

RRl66 = Parameter(name = 'RRl66',
                  nature = 'external',
                  type = 'real',
                  value = -0.28248719,
                  texname = '\\text{RRl66}',
                  lhablock = 'SELMIX',
                  lhacode = [ 6, 6 ])

aEWM1 = Parameter(name = 'aEWM1',
                  nature = 'external',
                  type = 'real',
                  value = 127.934,
                  texname = '\\alpha _w^{-1}',
                  lhablock = 'SMINPUTS',
                  lhacode = [ 1 ])

aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.118,
               texname = '\\alpha _s',
               lhablock = 'SMINPUTS',
               lhacode = [ 3 ])

RRn11 = Parameter(name = 'RRn11',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = '\\text{RRn11}',
                  lhablock = 'SNUMIX',
                  lhacode = [ 1, 1 ])

RRn22 = Parameter(name = 'RRn22',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = '\\text{RRn22}',
                  lhablock = 'SNUMIX',
                  lhacode = [ 2, 2 ])

RRn33 = Parameter(name = 'RRn33',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = '\\text{RRn33}',
                  lhablock = 'SNUMIX',
                  lhacode = [ 3, 3 ])

Rtd33 = Parameter(name = 'Rtd33',
                  nature = 'external',
                  type = 'real',
                  value = -110.693742,
                  texname = '\\text{Rtd33}',
                  lhablock = 'TD',
                  lhacode = [ 3, 3 ])

Rte33 = Parameter(name = 'Rte33',
                  nature = 'external',
                  type = 'real',
                  value = -25.4019727,
                  texname = '\\text{Rte33}',
                  lhablock = 'TE',
                  lhacode = [ 3, 3 ])

Rtu33 = Parameter(name = 'Rtu33',
                  nature = 'external',
                  type = 'real',
                  value = -444.752457,
                  texname = '\\text{Rtu33}',
                  lhablock = 'TU',
                  lhacode = [ 3, 3 ])

RUU11 = Parameter(name = 'RUU11',
                  nature = 'external',
                  type = 'real',
                  value = 0.916834859,
                  texname = '\\text{RUU11}',
                  lhablock = 'UMIX',
                  lhacode = [ 1, 1 ])

RUU12 = Parameter(name = 'RUU12',
                  nature = 'external',
                  type = 'real',
                  value = -0.399266629,
                  texname = '\\text{RUU12}',
                  lhablock = 'UMIX',
                  lhacode = [ 1, 2 ])

RUU21 = Parameter(name = 'RUU21',
                  nature = 'external',
                  type = 'real',
                  value = 0.399266629,
                  texname = '\\text{RUU21}',
                  lhablock = 'UMIX',
                  lhacode = [ 2, 1 ])

RUU22 = Parameter(name = 'RUU22',
                  nature = 'external',
                  type = 'real',
                  value = 0.916834859,
                  texname = '\\text{RUU22}',
                  lhablock = 'UMIX',
                  lhacode = [ 2, 2 ])

RMNS11 = Parameter(name = 'RMNS11',
                   nature = 'external',
                   type = 'real',
                   value = 1.,
                   texname = '\\text{RMNS11}',
                   lhablock = 'UPMNS',
                   lhacode = [ 1, 1 ])

RMNS22 = Parameter(name = 'RMNS22',
                   nature = 'external',
                   type = 'real',
                   value = 1.,
                   texname = '\\text{RMNS22}',
                   lhablock = 'UPMNS',
                   lhacode = [ 2, 2 ])

RMNS33 = Parameter(name = 'RMNS33',
                   nature = 'external',
                   type = 'real',
                   value = 1.,
                   texname = '\\text{RMNS33}',
                   lhablock = 'UPMNS',
                   lhacode = [ 3, 3 ])

RRu11 = Parameter(name = 'RRu11',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = '\\text{RRu11}',
                  lhablock = 'USQMIX',
                  lhacode = [ 1, 1 ])

RRu22 = Parameter(name = 'RRu22',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = '\\text{RRu22}',
                  lhablock = 'USQMIX',
                  lhacode = [ 2, 2 ])

RRu33 = Parameter(name = 'RRu33',
                  nature = 'external',
                  type = 'real',
                  value = 0.55364496,
                  texname = '\\text{RRu33}',
                  lhablock = 'USQMIX',
                  lhacode = [ 3, 3 ])

RRu36 = Parameter(name = 'RRu36',
                  nature = 'external',
                  type = 'real',
                  value = 0.83275282,
                  texname = '\\text{RRu36}',
                  lhablock = 'USQMIX',
                  lhacode = [ 3, 6 ])

RRu44 = Parameter(name = 'RRu44',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = '\\text{RRu44}',
                  lhablock = 'USQMIX',
                  lhacode = [ 4, 4 ])

RRu55 = Parameter(name = 'RRu55',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = '\\text{RRu55}',
                  lhablock = 'USQMIX',
                  lhacode = [ 5, 5 ])

RRu63 = Parameter(name = 'RRu63',
                  nature = 'external',
                  type = 'real',
                  value = 0.83275282,
                  texname = '\\text{RRu63}',
                  lhablock = 'USQMIX',
                  lhacode = [ 6, 3 ])

RRu66 = Parameter(name = 'RRu66',
                  nature = 'external',
                  type = 'real',
                  value = -0.55364496,
                  texname = '\\text{RRu66}',
                  lhablock = 'USQMIX',
                  lhacode = [ 6, 6 ])

RCKM11 = Parameter(name = 'RCKM11',
                   nature = 'external',
                   type = 'real',
                   value = 1.,
                   texname = '\\text{RCKM11}',
                   lhablock = 'VCKM',
                   lhacode = [ 1, 1 ])

RCKM22 = Parameter(name = 'RCKM22',
                   nature = 'external',
                   type = 'real',
                   value = 1.,
                   texname = '\\text{RCKM22}',
                   lhablock = 'VCKM',
                   lhacode = [ 2, 2 ])

RCKM33 = Parameter(name = 'RCKM33',
                   nature = 'external',
                   type = 'real',
                   value = 1.,
                   texname = '\\text{RCKM33}',
                   lhablock = 'VCKM',
                   lhacode = [ 3, 3 ])

RVV11 = Parameter(name = 'RVV11',
                  nature = 'external',
                  type = 'real',
                  value = 0.972557835,
                  texname = '\\text{RVV11}',
                  lhablock = 'VMIX',
                  lhacode = [ 1, 1 ])

RVV12 = Parameter(name = 'RVV12',
                  nature = 'external',
                  type = 'real',
                  value = -0.232661249,
                  texname = '\\text{RVV12}',
                  lhablock = 'VMIX',
                  lhacode = [ 1, 2 ])

RVV21 = Parameter(name = 'RVV21',
                  nature = 'external',
                  type = 'real',
                  value = 0.232661249,
                  texname = '\\text{RVV21}',
                  lhablock = 'VMIX',
                  lhacode = [ 2, 1 ])

RVV22 = Parameter(name = 'RVV22',
                  nature = 'external',
                  type = 'real',
                  value = 0.972557835,
                  texname = '\\text{RVV22}',
                  lhablock = 'VMIX',
                  lhacode = [ 2, 2 ])

Ryd33 = Parameter(name = 'Ryd33',
                  nature = 'external',
                  type = 'real',
                  value = 0.138840206,
                  texname = '\\text{Ryd33}',
                  lhablock = 'YD',
                  lhacode = [ 3, 3 ])

Rye33 = Parameter(name = 'Rye33',
                  nature = 'external',
                  type = 'real',
                  value = 0.10089081,
                  texname = '\\text{Rye33}',
                  lhablock = 'YE',
                  lhacode = [ 3, 3 ])

Ryu33 = Parameter(name = 'Ryu33',
                  nature = 'external',
                  type = 'real',
                  value = 0.89284455,
                  texname = '\\text{Ryu33}',
                  lhablock = 'YU',
                  lhacode = [ 3, 3 ])

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.1876,
               texname = '\\text{MZ}',
               lhablock = 'MASS',
               lhacode = [ 23 ])

MW = Parameter(name = 'MW',
               nature = 'external',
               type = 'real',
               value = 79.8290131,
               texname = '\\text{MW}',
               lhablock = 'MASS',
               lhacode = [ 24 ])

Mneu1 = Parameter(name = 'Mneu1',
                  nature = 'external',
                  type = 'real',
                  value = 96.6880686,
                  texname = '\\text{Mneu1}',
                  lhablock = 'MASS',
                  lhacode = [ 1000022 ])

Mneu2 = Parameter(name = 'Mneu2',
                  nature = 'external',
                  type = 'real',
                  value = 181.088157,
                  texname = '\\text{Mneu2}',
                  lhablock = 'MASS',
                  lhacode = [ 1000023 ])

Mneu3 = Parameter(name = 'Mneu3',
                  nature = 'external',
                  type = 'real',
                  value = -363.756027,
                  texname = '\\text{Mneu3}',
                  lhablock = 'MASS',
                  lhacode = [ 1000025 ])

Mneu4 = Parameter(name = 'Mneu4',
                  nature = 'external',
                  type = 'real',
                  value = 381.729382,
                  texname = '\\text{Mneu4}',
                  lhablock = 'MASS',
                  lhacode = [ 1000035 ])

Mch1 = Parameter(name = 'Mch1',
                 nature = 'external',
                 type = 'real',
                 value = 181.696474,
                 texname = '\\text{Mch1}',
                 lhablock = 'MASS',
                 lhacode = [ 1000024 ])

Mch2 = Parameter(name = 'Mch2',
                 nature = 'external',
                 type = 'real',
                 value = 379.93932,
                 texname = '\\text{Mch2}',
                 lhablock = 'MASS',
                 lhacode = [ 1000037 ])

Mgo = Parameter(name = 'Mgo',
                nature = 'external',
                type = 'real',
                value = 607.713704,
                texname = '\\text{Mgo}',
                lhablock = 'MASS',
                lhacode = [ 1000021 ])

MH01 = Parameter(name = 'MH01',
                 nature = 'external',
                 type = 'real',
                 value = 110.899057,
                 texname = '\\text{MH01}',
                 lhablock = 'MASS',
                 lhacode = [ 25 ])

MH02 = Parameter(name = 'MH02',
                 nature = 'external',
                 type = 'real',
                 value = 399.960116,
                 texname = '\\text{MH02}',
                 lhablock = 'MASS',
                 lhacode = [ 35 ])

MA0 = Parameter(name = 'MA0',
                nature = 'external',
                type = 'real',
                value = 399.583917,
                texname = '\\text{MA0}',
                lhablock = 'MASS',
                lhacode = [ 36 ])

MH = Parameter(name = 'MH',
               nature = 'external',
               type = 'real',
               value = 407.879012,
               texname = '\\text{MH}',
               lhablock = 'MASS',
               lhacode = [ 37 ])

Mta = Parameter(name = 'Mta',
                nature = 'external',
                type = 'real',
                value = 1.777,
                texname = '\\text{Mta}',
                lhablock = 'MASS',
                lhacode = [ 15 ])

MT = Parameter(name = 'MT',
               nature = 'external',
               type = 'real',
               value = 175.,
               texname = '\\text{MT}',
               lhablock = 'MASS',
               lhacode = [ 6 ])

MB = Parameter(name = 'MB',
               nature = 'external',
               type = 'real',
               value = 4.88991651,
               texname = '\\text{MB}',
               lhablock = 'MASS',
               lhacode = [ 5 ])

Msn1 = Parameter(name = 'Msn1',
                 nature = 'external',
                 type = 'real',
                 value = 185.258326,
                 texname = '\\text{Msn1}',
                 lhablock = 'MASS',
                 lhacode = [ 1000012 ])

Msn2 = Parameter(name = 'Msn2',
                 nature = 'external',
                 type = 'real',
                 value = 185.258326,
                 texname = '\\text{Msn2}',
                 lhablock = 'MASS',
                 lhacode = [ 1000014 ])

Msn3 = Parameter(name = 'Msn3',
                 nature = 'external',
                 type = 'real',
                 value = 184.708464,
                 texname = '\\text{Msn3}',
                 lhablock = 'MASS',
                 lhacode = [ 1000016 ])

Msl1 = Parameter(name = 'Msl1',
                 nature = 'external',
                 type = 'real',
                 value = 202.91569,
                 texname = '\\text{Msl1}',
                 lhablock = 'MASS',
                 lhacode = [ 1000011 ])

Msl2 = Parameter(name = 'Msl2',
                 nature = 'external',
                 type = 'real',
                 value = 202.91569,
                 texname = '\\text{Msl2}',
                 lhablock = 'MASS',
                 lhacode = [ 1000013 ])

Msl3 = Parameter(name = 'Msl3',
                 nature = 'external',
                 type = 'real',
                 value = 134.490864,
                 texname = '\\text{Msl3}',
                 lhablock = 'MASS',
                 lhacode = [ 1000015 ])

Msl4 = Parameter(name = 'Msl4',
                 nature = 'external',
                 type = 'real',
                 value = 144.102799,
                 texname = '\\text{Msl4}',
                 lhablock = 'MASS',
                 lhacode = [ 2000011 ])

Msl5 = Parameter(name = 'Msl5',
                 nature = 'external',
                 type = 'real',
                 value = 144.102799,
                 texname = '\\text{Msl5}',
                 lhablock = 'MASS',
                 lhacode = [ 2000013 ])

Msl6 = Parameter(name = 'Msl6',
                 nature = 'external',
                 type = 'real',
                 value = 206.867805,
                 texname = '\\text{Msl6}',
                 lhablock = 'MASS',
                 lhacode = [ 2000015 ])

Msu1 = Parameter(name = 'Msu1',
                 nature = 'external',
                 type = 'real',
                 value = 561.119014,
                 texname = '\\text{Msu1}',
                 lhablock = 'MASS',
                 lhacode = [ 1000002 ])

Msu2 = Parameter(name = 'Msu2',
                 nature = 'external',
                 type = 'real',
                 value = 561.119014,
                 texname = '\\text{Msu2}',
                 lhablock = 'MASS',
                 lhacode = [ 1000004 ])

Msu3 = Parameter(name = 'Msu3',
                 nature = 'external',
                 type = 'real',
                 value = 399.668493,
                 texname = '\\text{Msu3}',
                 lhablock = 'MASS',
                 lhacode = [ 1000006 ])

Msu4 = Parameter(name = 'Msu4',
                 nature = 'external',
                 type = 'real',
                 value = 549.259265,
                 texname = '\\text{Msu4}',
                 lhablock = 'MASS',
                 lhacode = [ 2000002 ])

Msu5 = Parameter(name = 'Msu5',
                 nature = 'external',
                 type = 'real',
                 value = 549.259265,
                 texname = '\\text{Msu5}',
                 lhablock = 'MASS',
                 lhacode = [ 2000004 ])

Msu6 = Parameter(name = 'Msu6',
                 nature = 'external',
                 type = 'real',
                 value = 585.785818,
                 texname = '\\text{Msu6}',
                 lhablock = 'MASS',
                 lhacode = [ 2000006 ])

Msd1 = Parameter(name = 'Msd1',
                 nature = 'external',
                 type = 'real',
                 value = 568.441109,
                 texname = '\\text{Msd1}',
                 lhablock = 'MASS',
                 lhacode = [ 1000001 ])

Msd2 = Parameter(name = 'Msd2',
                 nature = 'external',
                 type = 'real',
                 value = 568.441109,
                 texname = '\\text{Msd2}',
                 lhablock = 'MASS',
                 lhacode = [ 1000003 ])

Msd3 = Parameter(name = 'Msd3',
                 nature = 'external',
                 type = 'real',
                 value = 513.065179,
                 texname = '\\text{Msd3}',
                 lhablock = 'MASS',
                 lhacode = [ 1000005 ])

Msd4 = Parameter(name = 'Msd4',
                 nature = 'external',
                 type = 'real',
                 value = 545.228462,
                 texname = '\\text{Msd4}',
                 lhablock = 'MASS',
                 lhacode = [ 2000001 ])

Msd5 = Parameter(name = 'Msd5',
                 nature = 'external',
                 type = 'real',
                 value = 545.228462,
                 texname = '\\text{Msd5}',
                 lhablock = 'MASS',
                 lhacode = [ 2000003 ])

Msd6 = Parameter(name = 'Msd6',
                 nature = 'external',
                 type = 'real',
                 value = 543.726676,
                 texname = '\\text{Msd6}',
                 lhablock = 'MASS',
                 lhacode = [ 2000005 ])

WZ = Parameter(name = 'WZ',
               nature = 'external',
               type = 'real',
               value = 2.41143316,
               texname = '\\text{WZ}',
               lhablock = 'DECAY',
               lhacode = [ 23 ])

WW = Parameter(name = 'WW',
               nature = 'external',
               type = 'real',
               value = 2.00282196,
               texname = '\\text{WW}',
               lhablock = 'DECAY',
               lhacode = [ 24 ])

Wneu2 = Parameter(name = 'Wneu2',
                  nature = 'external',
                  type = 'real',
                  value = 0.0207770048,
                  texname = '\\text{Wneu2}',
                  lhablock = 'DECAY',
                  lhacode = [ 1000023 ])

Wneu3 = Parameter(name = 'Wneu3',
                  nature = 'external',
                  type = 'real',
                  value = 1.91598495,
                  texname = '\\text{Wneu3}',
                  lhablock = 'DECAY',
                  lhacode = [ 1000025 ])

Wneu4 = Parameter(name = 'Wneu4',
                  nature = 'external',
                  type = 'real',
                  value = 2.58585079,
                  texname = '\\text{Wneu4}',
                  lhablock = 'DECAY',
                  lhacode = [ 1000035 ])

Wch1 = Parameter(name = 'Wch1',
                 nature = 'external',
                 type = 'real',
                 value = 0.0170414503,
                 texname = '\\text{Wch1}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000024 ])

Wch2 = Parameter(name = 'Wch2',
                 nature = 'external',
                 type = 'real',
                 value = 2.4868951,
                 texname = '\\text{Wch2}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000037 ])

Wgo = Parameter(name = 'Wgo',
                nature = 'external',
                type = 'real',
                value = 5.50675438,
                texname = '\\text{Wgo}',
                lhablock = 'DECAY',
                lhacode = [ 1000021 ])

WH01 = Parameter(name = 'WH01',
                 nature = 'external',
                 type = 'real',
                 value = 0.00198610799,
                 texname = '\\text{WH01}',
                 lhablock = 'DECAY',
                 lhacode = [ 25 ])

WH02 = Parameter(name = 'WH02',
                 nature = 'external',
                 type = 'real',
                 value = 0.574801389,
                 texname = '\\text{WH02}',
                 lhablock = 'DECAY',
                 lhacode = [ 35 ])

WA0 = Parameter(name = 'WA0',
                nature = 'external',
                type = 'real',
                value = 0.632178488,
                texname = '\\text{WA0}',
                lhablock = 'DECAY',
                lhacode = [ 36 ])

WH = Parameter(name = 'WH',
               nature = 'external',
               type = 'real',
               value = 0.546962813,
               texname = '\\text{WH}',
               lhablock = 'DECAY',
               lhacode = [ 37 ])

WT = Parameter(name = 'WT',
               nature = 'external',
               type = 'real',
               value = 1.56194983,
               texname = '\\text{WT}',
               lhablock = 'DECAY',
               lhacode = [ 6 ])

Wsn1 = Parameter(name = 'Wsn1',
                 nature = 'external',
                 type = 'real',
                 value = 0.149881634,
                 texname = '\\text{Wsn1}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000012 ])

Wsn2 = Parameter(name = 'Wsn2',
                 nature = 'external',
                 type = 'real',
                 value = 0.149881634,
                 texname = '\\text{Wsn2}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000014 ])

Wsn3 = Parameter(name = 'Wsn3',
                 nature = 'external',
                 type = 'real',
                 value = 0.147518977,
                 texname = '\\text{Wsn3}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000016 ])

Wsl1 = Parameter(name = 'Wsl1',
                 nature = 'external',
                 type = 'real',
                 value = 0.213682161,
                 texname = '\\text{Wsl1}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000011 ])

Wsl2 = Parameter(name = 'Wsl2',
                 nature = 'external',
                 type = 'real',
                 value = 0.213682161,
                 texname = '\\text{Wsl2}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000013 ])

Wsl3 = Parameter(name = 'Wsl3',
                 nature = 'external',
                 type = 'real',
                 value = 0.148327268,
                 texname = '\\text{Wsl3}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000015 ])

Wsl4 = Parameter(name = 'Wsl4',
                 nature = 'external',
                 type = 'real',
                 value = 0.216121626,
                 texname = '\\text{Wsl4}',
                 lhablock = 'DECAY',
                 lhacode = [ 2000011 ])

Wsl5 = Parameter(name = 'Wsl5',
                 nature = 'external',
                 type = 'real',
                 value = 0.216121626,
                 texname = '\\text{Wsl5}',
                 lhablock = 'DECAY',
                 lhacode = [ 2000013 ])

Wsl6 = Parameter(name = 'Wsl6',
                 nature = 'external',
                 type = 'real',
                 value = 0.269906096,
                 texname = '\\text{Wsl6}',
                 lhablock = 'DECAY',
                 lhacode = [ 2000015 ])

Wsu1 = Parameter(name = 'Wsu1',
                 nature = 'external',
                 type = 'real',
                 value = 5.47719539,
                 texname = '\\text{Wsu1}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000002 ])

Wsu2 = Parameter(name = 'Wsu2',
                 nature = 'external',
                 type = 'real',
                 value = 5.47719539,
                 texname = '\\text{Wsu2}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000004 ])

Wsu3 = Parameter(name = 'Wsu3',
                 nature = 'external',
                 type = 'real',
                 value = 2.02159578,
                 texname = '\\text{Wsu3}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000006 ])

Wsu4 = Parameter(name = 'Wsu4',
                 nature = 'external',
                 type = 'real',
                 value = 1.15297292,
                 texname = '\\text{Wsu4}',
                 lhablock = 'DECAY',
                 lhacode = [ 2000002 ])

Wsu5 = Parameter(name = 'Wsu5',
                 nature = 'external',
                 type = 'real',
                 value = 1.15297292,
                 texname = '\\text{Wsu5}',
                 lhablock = 'DECAY',
                 lhacode = [ 2000004 ])

Wsu6 = Parameter(name = 'Wsu6',
                 nature = 'external',
                 type = 'real',
                 value = 7.37313275,
                 texname = '\\text{Wsu6}',
                 lhablock = 'DECAY',
                 lhacode = [ 2000006 ])

Wsd1 = Parameter(name = 'Wsd1',
                 nature = 'external',
                 type = 'real',
                 value = 5.31278772,
                 texname = '\\text{Wsd1}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000001 ])

Wsd2 = Parameter(name = 'Wsd2',
                 nature = 'external',
                 type = 'real',
                 value = 5.31278772,
                 texname = '\\text{Wsd2}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000003 ])

Wsd3 = Parameter(name = 'Wsd3',
                 nature = 'external',
                 type = 'real',
                 value = 3.73627601,
                 texname = '\\text{Wsd3}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000005 ])

Wsd4 = Parameter(name = 'Wsd4',
                 nature = 'external',
                 type = 'real',
                 value = 0.285812308,
                 texname = '\\text{Wsd4}',
                 lhablock = 'DECAY',
                 lhacode = [ 2000001 ])

Wsd5 = Parameter(name = 'Wsd5',
                 nature = 'external',
                 type = 'real',
                 value = 0.285812308,
                 texname = '\\text{Wsd5}',
                 lhablock = 'DECAY',
                 lhacode = [ 2000003 ])

Wsd6 = Parameter(name = 'Wsd6',
                 nature = 'external',
                 type = 'real',
                 value = 0.801566294,
                 texname = '\\text{Wsd6}',
                 lhablock = 'DECAY',
                 lhacode = [ 2000005 ])

beta = Parameter(name = 'beta',
                 nature = 'internal',
                 type = 'real',
                 value = 'cmath.atan(tb)',
                 texname = '\\beta ')

CKM11 = Parameter(name = 'CKM11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RCKM11',
                  texname = '\\text{CKM11}')

CKM22 = Parameter(name = 'CKM22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RCKM22',
                  texname = '\\text{CKM22}')

CKM33 = Parameter(name = 'CKM33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RCKM33',
                  texname = '\\text{CKM33}')

cw = Parameter(name = 'cw',
               nature = 'internal',
               type = 'real',
               value = 'MW/MZ',
               texname = 'c_w')

mD211 = Parameter(name = 'mD211',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RmD211',
                  texname = '\\text{mD211}')

mD222 = Parameter(name = 'mD222',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RmD222',
                  texname = '\\text{mD222}')

mD233 = Parameter(name = 'mD233',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RmD233',
                  texname = '\\text{mD233}')

mE211 = Parameter(name = 'mE211',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RmE211',
                  texname = '\\text{mE211}')

mE222 = Parameter(name = 'mE222',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RmE222',
                  texname = '\\text{mE222}')

mE233 = Parameter(name = 'mE233',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RmE233',
                  texname = '\\text{mE233}')

mL211 = Parameter(name = 'mL211',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RmL211',
                  texname = '\\text{mL211}')

mL222 = Parameter(name = 'mL222',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RmL222',
                  texname = '\\text{mL222}')

mL233 = Parameter(name = 'mL233',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RmL233',
                  texname = '\\text{mL233}')

mQ211 = Parameter(name = 'mQ211',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RmQ211',
                  texname = '\\text{mQ211}')

mQ222 = Parameter(name = 'mQ222',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RmQ222',
                  texname = '\\text{mQ222}')

mQ233 = Parameter(name = 'mQ233',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RmQ233',
                  texname = '\\text{mQ233}')

mU211 = Parameter(name = 'mU211',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RmU211',
                  texname = '\\text{mU211}')

mU222 = Parameter(name = 'mU222',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RmU222',
                  texname = '\\text{mU222}')

mU233 = Parameter(name = 'mU233',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RmU233',
                  texname = '\\text{mU233}')

MUH = Parameter(name = 'MUH',
                nature = 'internal',
                type = 'complex',
                value = 'RMUH',
                texname = '\\mu ')

Mx1 = Parameter(name = 'Mx1',
                nature = 'internal',
                type = 'complex',
                value = 'RMx1',
                texname = 'M_1')

Mx2 = Parameter(name = 'Mx2',
                nature = 'internal',
                type = 'complex',
                value = 'RMx2',
                texname = 'M_2')

Mx3 = Parameter(name = 'Mx3',
                nature = 'internal',
                type = 'complex',
                value = 'RMx3',
                texname = 'M_3')

NN11 = Parameter(name = 'NN11',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RNN11',
                 texname = '\\text{NN11}')

NN12 = Parameter(name = 'NN12',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RNN12',
                 texname = '\\text{NN12}')

NN13 = Parameter(name = 'NN13',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RNN13',
                 texname = '\\text{NN13}')

NN14 = Parameter(name = 'NN14',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RNN14',
                 texname = '\\text{NN14}')

NN21 = Parameter(name = 'NN21',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RNN21',
                 texname = '\\text{NN21}')

NN22 = Parameter(name = 'NN22',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RNN22',
                 texname = '\\text{NN22}')

NN23 = Parameter(name = 'NN23',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RNN23',
                 texname = '\\text{NN23}')

NN24 = Parameter(name = 'NN24',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RNN24',
                 texname = '\\text{NN24}')

NN31 = Parameter(name = 'NN31',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RNN31',
                 texname = '\\text{NN31}')

NN32 = Parameter(name = 'NN32',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RNN32',
                 texname = '\\text{NN32}')

NN33 = Parameter(name = 'NN33',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RNN33',
                 texname = '\\text{NN33}')

NN34 = Parameter(name = 'NN34',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RNN34',
                 texname = '\\text{NN34}')

NN41 = Parameter(name = 'NN41',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RNN41',
                 texname = '\\text{NN41}')

NN42 = Parameter(name = 'NN42',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RNN42',
                 texname = '\\text{NN42}')

NN43 = Parameter(name = 'NN43',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RNN43',
                 texname = '\\text{NN43}')

NN44 = Parameter(name = 'NN44',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RNN44',
                 texname = '\\text{NN44}')

Rd11 = Parameter(name = 'Rd11',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RRd11',
                 texname = '\\text{Rd11}')

Rd22 = Parameter(name = 'Rd22',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RRd22',
                 texname = '\\text{Rd22}')

Rd33 = Parameter(name = 'Rd33',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RRd33',
                 texname = '\\text{Rd33}')

Rd36 = Parameter(name = 'Rd36',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RRd36',
                 texname = '\\text{Rd36}')

Rd44 = Parameter(name = 'Rd44',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RRd44',
                 texname = '\\text{Rd44}')

Rd55 = Parameter(name = 'Rd55',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RRd55',
                 texname = '\\text{Rd55}')

Rd63 = Parameter(name = 'Rd63',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RRd63',
                 texname = '\\text{Rd63}')

Rd66 = Parameter(name = 'Rd66',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RRd66',
                 texname = '\\text{Rd66}')

Rl11 = Parameter(name = 'Rl11',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RRl11',
                 texname = '\\text{Rl11}')

Rl22 = Parameter(name = 'Rl22',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RRl22',
                 texname = '\\text{Rl22}')

Rl33 = Parameter(name = 'Rl33',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RRl33',
                 texname = '\\text{Rl33}')

Rl36 = Parameter(name = 'Rl36',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RRl36',
                 texname = '\\text{Rl36}')

Rl44 = Parameter(name = 'Rl44',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RRl44',
                 texname = '\\text{Rl44}')

Rl55 = Parameter(name = 'Rl55',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RRl55',
                 texname = '\\text{Rl55}')

Rl63 = Parameter(name = 'Rl63',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RRl63',
                 texname = '\\text{Rl63}')

Rl66 = Parameter(name = 'Rl66',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RRl66',
                 texname = '\\text{Rl66}')

Rn11 = Parameter(name = 'Rn11',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RRn11',
                 texname = '\\text{Rn11}')

Rn22 = Parameter(name = 'Rn22',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RRn22',
                 texname = '\\text{Rn22}')

Rn33 = Parameter(name = 'Rn33',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RRn33',
                 texname = '\\text{Rn33}')

Ru11 = Parameter(name = 'Ru11',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RRu11',
                 texname = '\\text{Ru11}')

Ru22 = Parameter(name = 'Ru22',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RRu22',
                 texname = '\\text{Ru22}')

Ru33 = Parameter(name = 'Ru33',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RRu33',
                 texname = '\\text{Ru33}')

Ru36 = Parameter(name = 'Ru36',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RRu36',
                 texname = '\\text{Ru36}')

Ru44 = Parameter(name = 'Ru44',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RRu44',
                 texname = '\\text{Ru44}')

Ru55 = Parameter(name = 'Ru55',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RRu55',
                 texname = '\\text{Ru55}')

Ru63 = Parameter(name = 'Ru63',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RRu63',
                 texname = '\\text{Ru63}')

Ru66 = Parameter(name = 'Ru66',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RRu66',
                 texname = '\\text{Ru66}')

UU11 = Parameter(name = 'UU11',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RUU11',
                 texname = '\\text{UU11}')

UU12 = Parameter(name = 'UU12',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RUU12',
                 texname = '\\text{UU12}')

UU21 = Parameter(name = 'UU21',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RUU21',
                 texname = '\\text{UU21}')

UU22 = Parameter(name = 'UU22',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RUU22',
                 texname = '\\text{UU22}')

VV11 = Parameter(name = 'VV11',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RVV11',
                 texname = '\\text{VV11}')

VV12 = Parameter(name = 'VV12',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RVV12',
                 texname = '\\text{VV12}')

VV21 = Parameter(name = 'VV21',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RVV21',
                 texname = '\\text{VV21}')

VV22 = Parameter(name = 'VV22',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RVV22',
                 texname = '\\text{VV22}')

ee = Parameter(name = 'ee',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(1/aEWM1)*cmath.sqrt(cmath.pi)',
               texname = 'e')

G = Parameter(name = 'G',
              nature = 'internal',
              type = 'real',
              value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
              texname = 'G')

gp = Parameter(name = 'gp',
               nature = 'internal',
               type = 'real',
               value = '1',
               texname = 'g\'')

gw = Parameter(name = 'gw',
               nature = 'internal',
               type = 'real',
               value = '1',
               texname = 'g_w')

td33 = Parameter(name = 'td33',
                 nature = 'internal',
                 type = 'complex',
                 value = 'Rtd33',
                 texname = '\\text{td33}')

te33 = Parameter(name = 'te33',
                 nature = 'internal',
                 type = 'complex',
                 value = 'Rte33',
                 texname = '\\text{te33}')

tu33 = Parameter(name = 'tu33',
                 nature = 'internal',
                 type = 'complex',
                 value = 'Rtu33',
                 texname = '\\text{tu33}')

yd33 = Parameter(name = 'yd33',
                 nature = 'internal',
                 type = 'complex',
                 value = 'Ryd33',
                 texname = '\\text{yd33}')

ye33 = Parameter(name = 'ye33',
                 nature = 'internal',
                 type = 'complex',
                 value = 'Rye33',
                 texname = '\\text{ye33}')

yu33 = Parameter(name = 'yu33',
                 nature = 'internal',
                 type = 'complex',
                 value = 'Ryu33',
                 texname = '\\text{yu33}')

bb = Parameter(name = 'bb',
               nature = 'internal',
               type = 'complex',
               value = '((-mHd2 + mHu2 - MZ**2*cmath.cos(2*beta))*cmath.tan(2*beta))/2.',
               texname = 'b')

sw = Parameter(name = 'sw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1 - cw**2)',
               texname = 's_w')

vev = Parameter(name = 'vev',
                nature = 'internal',
                type = 'real',
                value = '(2*cw*MZ*sw)/ee',
                texname = 'v')

vd = Parameter(name = 'vd',
               nature = 'internal',
               type = 'real',
               value = 'vev*cmath.cos(beta)',
               texname = 'v_d')

vu = Parameter(name = 'vu',
               nature = 'internal',
               type = 'real',
               value = 'vev*cmath.sin(beta)',
               texname = 'v_u')

I133 = Parameter(name = 'I133',
                 nature = 'internal',
                 type = 'complex',
                 value = 'complexconjugate(CKM33)*complexconjugate(yu33)',
                 texname = '\\text{I133}')

I1033 = Parameter(name = 'I1033',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd33*complexconjugate(yd33)',
                  texname = '\\text{I1033}')

I1036 = Parameter(name = 'I1036',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd63*complexconjugate(yd33)',
                  texname = '\\text{I1036}')

I10033 = Parameter(name = 'I10033',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn33*complexconjugate(Rl36)*complexconjugate(te33)',
                   texname = '\\text{I10033}')

I10036 = Parameter(name = 'I10036',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn33*complexconjugate(Rl66)*complexconjugate(te33)',
                   texname = '\\text{I10036}')

I10133 = Parameter(name = 'I10133',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn33*ye33*complexconjugate(Rl33)*complexconjugate(ye33)',
                   texname = '\\text{I10133}')

I10136 = Parameter(name = 'I10136',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn33*ye33*complexconjugate(Rl63)*complexconjugate(ye33)',
                   texname = '\\text{I10136}')

I10211 = Parameter(name = 'I10211',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn11*complexconjugate(Rl11)',
                   texname = '\\text{I10211}')

I10222 = Parameter(name = 'I10222',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn22*complexconjugate(Rl22)',
                   texname = '\\text{I10222}')

I10233 = Parameter(name = 'I10233',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn33*complexconjugate(Rl33)',
                   texname = '\\text{I10233}')

I10236 = Parameter(name = 'I10236',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn33*complexconjugate(Rl63)',
                   texname = '\\text{I10236}')

I10333 = Parameter(name = 'I10333',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn33*ye33*complexconjugate(Rl33)*complexconjugate(ye33)',
                   texname = '\\text{I10333}')

I10336 = Parameter(name = 'I10336',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn33*ye33*complexconjugate(Rl63)*complexconjugate(ye33)',
                   texname = '\\text{I10336}')

I10433 = Parameter(name = 'I10433',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn33*ye33*complexconjugate(Rn33)*complexconjugate(ye33)',
                   texname = '\\text{I10433}')

I10511 = Parameter(name = 'I10511',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl11*complexconjugate(Rl11)',
                   texname = '\\text{I10511}')

I10522 = Parameter(name = 'I10522',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl22*complexconjugate(Rl22)',
                   texname = '\\text{I10522}')

I10533 = Parameter(name = 'I10533',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl33*complexconjugate(Rl33)',
                   texname = '\\text{I10533}')

I10536 = Parameter(name = 'I10536',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl63*complexconjugate(Rl33)',
                   texname = '\\text{I10536}')

I10563 = Parameter(name = 'I10563',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl33*complexconjugate(Rl63)',
                   texname = '\\text{I10563}')

I10566 = Parameter(name = 'I10566',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl63*complexconjugate(Rl63)',
                   texname = '\\text{I10566}')

I10633 = Parameter(name = 'I10633',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl36*complexconjugate(Rl36)',
                   texname = '\\text{I10633}')

I10636 = Parameter(name = 'I10636',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl66*complexconjugate(Rl36)',
                   texname = '\\text{I10636}')

I10644 = Parameter(name = 'I10644',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl44*complexconjugate(Rl44)',
                   texname = '\\text{I10644}')

I10655 = Parameter(name = 'I10655',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl55*complexconjugate(Rl55)',
                   texname = '\\text{I10655}')

I10663 = Parameter(name = 'I10663',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl36*complexconjugate(Rl66)',
                   texname = '\\text{I10663}')

I10666 = Parameter(name = 'I10666',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl66*complexconjugate(Rl66)',
                   texname = '\\text{I10666}')

I10711 = Parameter(name = 'I10711',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl11*complexconjugate(Rn11)',
                   texname = '\\text{I10711}')

I10722 = Parameter(name = 'I10722',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl22*complexconjugate(Rn22)',
                   texname = '\\text{I10722}')

I10733 = Parameter(name = 'I10733',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl33*complexconjugate(Rn33)',
                   texname = '\\text{I10733}')

I10736 = Parameter(name = 'I10736',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl63*complexconjugate(Rn33)',
                   texname = '\\text{I10736}')

I10811 = Parameter(name = 'I10811',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn11*complexconjugate(Rl11)',
                   texname = '\\text{I10811}')

I10822 = Parameter(name = 'I10822',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn22*complexconjugate(Rl22)',
                   texname = '\\text{I10822}')

I10833 = Parameter(name = 'I10833',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn33*complexconjugate(Rl33)',
                   texname = '\\text{I10833}')

I10836 = Parameter(name = 'I10836',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn33*complexconjugate(Rl63)',
                   texname = '\\text{I10836}')

I10933 = Parameter(name = 'I10933',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn33*complexconjugate(Rl36)*complexconjugate(ye33)',
                   texname = '\\text{I10933}')

I10936 = Parameter(name = 'I10936',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn33*complexconjugate(Rl66)*complexconjugate(ye33)',
                   texname = '\\text{I10936}')

I1133 = Parameter(name = 'I1133',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd36*yd33',
                  texname = '\\text{I1133}')

I1136 = Parameter(name = 'I1136',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd66*yd33',
                  texname = '\\text{I1136}')

I11033 = Parameter(name = 'I11033',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl36*ye33*complexconjugate(Rn33)',
                   texname = '\\text{I11033}')

I11036 = Parameter(name = 'I11036',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl66*ye33*complexconjugate(Rn33)',
                   texname = '\\text{I11036}')

I11133 = Parameter(name = 'I11133',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(Ru36)*complexconjugate(yu33)',
                   texname = '\\text{I11133}')

I11136 = Parameter(name = 'I11136',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(Ru66)*complexconjugate(yu33)',
                   texname = '\\text{I11136}')

I11233 = Parameter(name = 'I11233',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yu33*complexconjugate(Ru33)',
                   texname = '\\text{I11233}')

I11236 = Parameter(name = 'I11236',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yu33*complexconjugate(Ru63)',
                   texname = '\\text{I11236}')

I11311 = Parameter(name = 'I11311',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru11*complexconjugate(Ru11)',
                   texname = '\\text{I11311}')

I11322 = Parameter(name = 'I11322',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru22*complexconjugate(Ru22)',
                   texname = '\\text{I11322}')

I11333 = Parameter(name = 'I11333',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru33*complexconjugate(Ru33)',
                   texname = '\\text{I11333}')

I11336 = Parameter(name = 'I11336',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru63*complexconjugate(Ru33)',
                   texname = '\\text{I11336}')

I11363 = Parameter(name = 'I11363',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru33*complexconjugate(Ru63)',
                   texname = '\\text{I11363}')

I11366 = Parameter(name = 'I11366',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru63*complexconjugate(Ru63)',
                   texname = '\\text{I11366}')

I11433 = Parameter(name = 'I11433',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru36*complexconjugate(Ru36)',
                   texname = '\\text{I11433}')

I11436 = Parameter(name = 'I11436',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru66*complexconjugate(Ru36)',
                   texname = '\\text{I11436}')

I11444 = Parameter(name = 'I11444',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru44*complexconjugate(Ru44)',
                   texname = '\\text{I11444}')

I11455 = Parameter(name = 'I11455',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru55*complexconjugate(Ru55)',
                   texname = '\\text{I11455}')

I11463 = Parameter(name = 'I11463',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru36*complexconjugate(Ru66)',
                   texname = '\\text{I11463}')

I11466 = Parameter(name = 'I11466',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru66*complexconjugate(Ru66)',
                   texname = '\\text{I11466}')

I11511 = Parameter(name = 'I11511',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd11*complexconjugate(CKM11)*complexconjugate(Ru11)',
                   texname = '\\text{I11511}')

I11522 = Parameter(name = 'I11522',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd22*complexconjugate(CKM22)*complexconjugate(Ru22)',
                   texname = '\\text{I11522}')

I11533 = Parameter(name = 'I11533',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd33*complexconjugate(CKM33)*complexconjugate(Ru33)',
                   texname = '\\text{I11533}')

I11536 = Parameter(name = 'I11536',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd33*complexconjugate(CKM33)*complexconjugate(Ru63)',
                   texname = '\\text{I11536}')

I11563 = Parameter(name = 'I11563',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd63*complexconjugate(CKM33)*complexconjugate(Ru33)',
                   texname = '\\text{I11563}')

I11566 = Parameter(name = 'I11566',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd63*complexconjugate(CKM33)*complexconjugate(Ru63)',
                   texname = '\\text{I11566}')

I11633 = Parameter(name = 'I11633',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd33*complexconjugate(CKM33)*complexconjugate(Ru36)*complexconjugate(tu33)',
                   texname = '\\text{I11633}')

I11636 = Parameter(name = 'I11636',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd33*complexconjugate(CKM33)*complexconjugate(Ru66)*complexconjugate(tu33)',
                   texname = '\\text{I11636}')

I11663 = Parameter(name = 'I11663',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd63*complexconjugate(CKM33)*complexconjugate(Ru36)*complexconjugate(tu33)',
                   texname = '\\text{I11663}')

I11666 = Parameter(name = 'I11666',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd63*complexconjugate(CKM33)*complexconjugate(Ru66)*complexconjugate(tu33)',
                   texname = '\\text{I11666}')

I11733 = Parameter(name = 'I11733',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd33*complexconjugate(CKM33)*complexconjugate(Ru36)*complexconjugate(yu33)',
                   texname = '\\text{I11733}')

I11736 = Parameter(name = 'I11736',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd33*complexconjugate(CKM33)*complexconjugate(Ru66)*complexconjugate(yu33)',
                   texname = '\\text{I11736}')

I11763 = Parameter(name = 'I11763',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd63*complexconjugate(CKM33)*complexconjugate(Ru36)*complexconjugate(yu33)',
                   texname = '\\text{I11763}')

I11766 = Parameter(name = 'I11766',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd63*complexconjugate(CKM33)*complexconjugate(Ru66)*complexconjugate(yu33)',
                   texname = '\\text{I11766}')

I11833 = Parameter(name = 'I11833',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd36*td33*complexconjugate(CKM33)*complexconjugate(Ru33)',
                   texname = '\\text{I11833}')

I11836 = Parameter(name = 'I11836',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd36*td33*complexconjugate(CKM33)*complexconjugate(Ru63)',
                   texname = '\\text{I11836}')

I11863 = Parameter(name = 'I11863',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd66*td33*complexconjugate(CKM33)*complexconjugate(Ru33)',
                   texname = '\\text{I11863}')

I11866 = Parameter(name = 'I11866',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd66*td33*complexconjugate(CKM33)*complexconjugate(Ru63)',
                   texname = '\\text{I11866}')

I11933 = Parameter(name = 'I11933',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd33*yd33*complexconjugate(CKM33)*complexconjugate(Ru33)*complexconjugate(yd33)',
                   texname = '\\text{I11933}')

I11936 = Parameter(name = 'I11936',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd33*yd33*complexconjugate(CKM33)*complexconjugate(Ru63)*complexconjugate(yd33)',
                   texname = '\\text{I11936}')

I11963 = Parameter(name = 'I11963',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd63*yd33*complexconjugate(CKM33)*complexconjugate(Ru33)*complexconjugate(yd33)',
                   texname = '\\text{I11963}')

I11966 = Parameter(name = 'I11966',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd63*yd33*complexconjugate(CKM33)*complexconjugate(Ru63)*complexconjugate(yd33)',
                   texname = '\\text{I11966}')

I1211 = Parameter(name = 'I1211',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd11*complexconjugate(Rd11)',
                  texname = '\\text{I1211}')

I1222 = Parameter(name = 'I1222',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd22*complexconjugate(Rd22)',
                  texname = '\\text{I1222}')

I1233 = Parameter(name = 'I1233',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd33*complexconjugate(Rd33)',
                  texname = '\\text{I1233}')

I1236 = Parameter(name = 'I1236',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd63*complexconjugate(Rd33)',
                  texname = '\\text{I1236}')

I1263 = Parameter(name = 'I1263',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd33*complexconjugate(Rd63)',
                  texname = '\\text{I1263}')

I1266 = Parameter(name = 'I1266',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd63*complexconjugate(Rd63)',
                  texname = '\\text{I1266}')

I12033 = Parameter(name = 'I12033',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd36*yd33*complexconjugate(CKM33)*complexconjugate(Ru33)',
                   texname = '\\text{I12033}')

I12036 = Parameter(name = 'I12036',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd36*yd33*complexconjugate(CKM33)*complexconjugate(Ru63)',
                   texname = '\\text{I12036}')

I12063 = Parameter(name = 'I12063',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd66*yd33*complexconjugate(CKM33)*complexconjugate(Ru33)',
                   texname = '\\text{I12063}')

I12066 = Parameter(name = 'I12066',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd66*yd33*complexconjugate(CKM33)*complexconjugate(Ru63)',
                   texname = '\\text{I12066}')

I12133 = Parameter(name = 'I12133',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd36*yd33*complexconjugate(CKM33)*complexconjugate(Ru36)*complexconjugate(yu33)',
                   texname = '\\text{I12133}')

I12136 = Parameter(name = 'I12136',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd36*yd33*complexconjugate(CKM33)*complexconjugate(Ru66)*complexconjugate(yu33)',
                   texname = '\\text{I12136}')

I12163 = Parameter(name = 'I12163',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd66*yd33*complexconjugate(CKM33)*complexconjugate(Ru36)*complexconjugate(yu33)',
                   texname = '\\text{I12163}')

I12166 = Parameter(name = 'I12166',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd66*yd33*complexconjugate(CKM33)*complexconjugate(Ru66)*complexconjugate(yu33)',
                   texname = '\\text{I12166}')

I12233 = Parameter(name = 'I12233',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd33*yu33*complexconjugate(CKM33)*complexconjugate(Ru33)*complexconjugate(yu33)',
                   texname = '\\text{I12233}')

I12236 = Parameter(name = 'I12236',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd33*yu33*complexconjugate(CKM33)*complexconjugate(Ru63)*complexconjugate(yu33)',
                   texname = '\\text{I12236}')

I12263 = Parameter(name = 'I12263',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd63*yu33*complexconjugate(CKM33)*complexconjugate(Ru33)*complexconjugate(yu33)',
                   texname = '\\text{I12263}')

I12266 = Parameter(name = 'I12266',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd63*yu33*complexconjugate(CKM33)*complexconjugate(Ru63)*complexconjugate(yu33)',
                   texname = '\\text{I12266}')

I12311 = Parameter(name = 'I12311',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd11*complexconjugate(CKM11)*complexconjugate(Ru11)',
                   texname = '\\text{I12311}')

I12322 = Parameter(name = 'I12322',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd22*complexconjugate(CKM22)*complexconjugate(Ru22)',
                   texname = '\\text{I12322}')

I12333 = Parameter(name = 'I12333',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd33*complexconjugate(CKM33)*complexconjugate(Ru33)',
                   texname = '\\text{I12333}')

I12336 = Parameter(name = 'I12336',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd33*complexconjugate(CKM33)*complexconjugate(Ru63)',
                   texname = '\\text{I12336}')

I12363 = Parameter(name = 'I12363',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd63*complexconjugate(CKM33)*complexconjugate(Ru33)',
                   texname = '\\text{I12363}')

I12366 = Parameter(name = 'I12366',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd63*complexconjugate(CKM33)*complexconjugate(Ru63)',
                   texname = '\\text{I12366}')

I12433 = Parameter(name = 'I12433',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd36*yd33*complexconjugate(CKM33)*complexconjugate(Ru36)*complexconjugate(yu33)',
                   texname = '\\text{I12433}')

I12436 = Parameter(name = 'I12436',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd36*yd33*complexconjugate(CKM33)*complexconjugate(Ru66)*complexconjugate(yu33)',
                   texname = '\\text{I12436}')

I12463 = Parameter(name = 'I12463',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd66*yd33*complexconjugate(CKM33)*complexconjugate(Ru36)*complexconjugate(yu33)',
                   texname = '\\text{I12463}')

I12466 = Parameter(name = 'I12466',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd66*yd33*complexconjugate(CKM33)*complexconjugate(Ru66)*complexconjugate(yu33)',
                   texname = '\\text{I12466}')

I12533 = Parameter(name = 'I12533',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd33*yd33*complexconjugate(CKM33)*complexconjugate(Ru33)*complexconjugate(yd33)',
                   texname = '\\text{I12533}')

I12536 = Parameter(name = 'I12536',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd33*yd33*complexconjugate(CKM33)*complexconjugate(Ru63)*complexconjugate(yd33)',
                   texname = '\\text{I12536}')

I12563 = Parameter(name = 'I12563',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd63*yd33*complexconjugate(CKM33)*complexconjugate(Ru33)*complexconjugate(yd33)',
                   texname = '\\text{I12563}')

I12566 = Parameter(name = 'I12566',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd63*yd33*complexconjugate(CKM33)*complexconjugate(Ru63)*complexconjugate(yd33)',
                   texname = '\\text{I12566}')

I12633 = Parameter(name = 'I12633',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd33*yu33*complexconjugate(CKM33)*complexconjugate(Ru33)*complexconjugate(yu33)',
                   texname = '\\text{I12633}')

I12636 = Parameter(name = 'I12636',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd33*yu33*complexconjugate(CKM33)*complexconjugate(Ru63)*complexconjugate(yu33)',
                   texname = '\\text{I12636}')

I12663 = Parameter(name = 'I12663',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd63*yu33*complexconjugate(CKM33)*complexconjugate(Ru33)*complexconjugate(yu33)',
                   texname = '\\text{I12663}')

I12666 = Parameter(name = 'I12666',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd63*yu33*complexconjugate(CKM33)*complexconjugate(Ru63)*complexconjugate(yu33)',
                   texname = '\\text{I12666}')

I12711 = Parameter(name = 'I12711',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd11*complexconjugate(CKM11)*complexconjugate(Ru11)',
                   texname = '\\text{I12711}')

I12722 = Parameter(name = 'I12722',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd22*complexconjugate(CKM22)*complexconjugate(Ru22)',
                   texname = '\\text{I12722}')

I12733 = Parameter(name = 'I12733',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd33*complexconjugate(CKM33)*complexconjugate(Ru33)',
                   texname = '\\text{I12733}')

I12736 = Parameter(name = 'I12736',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd33*complexconjugate(CKM33)*complexconjugate(Ru63)',
                   texname = '\\text{I12736}')

I12763 = Parameter(name = 'I12763',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd63*complexconjugate(CKM33)*complexconjugate(Ru33)',
                   texname = '\\text{I12763}')

I12766 = Parameter(name = 'I12766',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd63*complexconjugate(CKM33)*complexconjugate(Ru63)',
                   texname = '\\text{I12766}')

I12811 = Parameter(name = 'I12811',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn11*complexconjugate(Rl11)',
                   texname = '\\text{I12811}')

I12822 = Parameter(name = 'I12822',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn22*complexconjugate(Rl22)',
                   texname = '\\text{I12822}')

I12833 = Parameter(name = 'I12833',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn33*complexconjugate(Rl33)',
                   texname = '\\text{I12833}')

I12836 = Parameter(name = 'I12836',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn33*complexconjugate(Rl63)',
                   texname = '\\text{I12836}')

I12933 = Parameter(name = 'I12933',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn33*complexconjugate(Rl36)*complexconjugate(ye33)',
                   texname = '\\text{I12933}')

I12936 = Parameter(name = 'I12936',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn33*complexconjugate(Rl66)*complexconjugate(ye33)',
                   texname = '\\text{I12936}')

I1333 = Parameter(name = 'I1333',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd36*complexconjugate(Rd36)',
                  texname = '\\text{I1333}')

I1336 = Parameter(name = 'I1336',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd66*complexconjugate(Rd36)',
                  texname = '\\text{I1336}')

I1344 = Parameter(name = 'I1344',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd44*complexconjugate(Rd44)',
                  texname = '\\text{I1344}')

I1355 = Parameter(name = 'I1355',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd55*complexconjugate(Rd55)',
                  texname = '\\text{I1355}')

I1363 = Parameter(name = 'I1363',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd36*complexconjugate(Rd66)',
                  texname = '\\text{I1363}')

I1366 = Parameter(name = 'I1366',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd66*complexconjugate(Rd66)',
                  texname = '\\text{I1366}')

I13033 = Parameter(name = 'I13033',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd36*yd33*complexconjugate(CKM33)*complexconjugate(Ru33)',
                   texname = '\\text{I13033}')

I13036 = Parameter(name = 'I13036',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd36*yd33*complexconjugate(CKM33)*complexconjugate(Ru63)',
                   texname = '\\text{I13036}')

I13063 = Parameter(name = 'I13063',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd66*yd33*complexconjugate(CKM33)*complexconjugate(Ru33)',
                   texname = '\\text{I13063}')

I13066 = Parameter(name = 'I13066',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd66*yd33*complexconjugate(CKM33)*complexconjugate(Ru63)',
                   texname = '\\text{I13066}')

I13133 = Parameter(name = 'I13133',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru33*complexconjugate(yu33)',
                   texname = '\\text{I13133}')

I13136 = Parameter(name = 'I13136',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru63*complexconjugate(yu33)',
                   texname = '\\text{I13136}')

I13233 = Parameter(name = 'I13233',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru36*yu33',
                   texname = '\\text{I13233}')

I13236 = Parameter(name = 'I13236',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru66*yu33',
                   texname = '\\text{I13236}')

I13311 = Parameter(name = 'I13311',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM11*Ru11',
                   texname = '\\text{I13311}')

I13322 = Parameter(name = 'I13322',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM22*Ru22',
                   texname = '\\text{I13322}')

I13333 = Parameter(name = 'I13333',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*Ru33',
                   texname = '\\text{I13333}')

I13336 = Parameter(name = 'I13336',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*Ru63',
                   texname = '\\text{I13336}')

I13433 = Parameter(name = 'I13433',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*Ru33*complexconjugate(yd33)',
                   texname = '\\text{I13433}')

I13436 = Parameter(name = 'I13436',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*Ru63*complexconjugate(yd33)',
                   texname = '\\text{I13436}')

I13533 = Parameter(name = 'I13533',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*Ru36*yu33',
                   texname = '\\text{I13533}')

I13536 = Parameter(name = 'I13536',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*Ru66*yu33',
                   texname = '\\text{I13536}')

I13611 = Parameter(name = 'I13611',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM11*Ru11*complexconjugate(Rd11)',
                   texname = '\\text{I13611}')

I13622 = Parameter(name = 'I13622',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM22*Ru22*complexconjugate(Rd22)',
                   texname = '\\text{I13622}')

I13633 = Parameter(name = 'I13633',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*Ru33*complexconjugate(Rd33)',
                   texname = '\\text{I13633}')

I13636 = Parameter(name = 'I13636',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*Ru63*complexconjugate(Rd33)',
                   texname = '\\text{I13636}')

I13663 = Parameter(name = 'I13663',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*Ru33*complexconjugate(Rd63)',
                   texname = '\\text{I13663}')

I13666 = Parameter(name = 'I13666',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*Ru63*complexconjugate(Rd63)',
                   texname = '\\text{I13666}')

I13733 = Parameter(name = 'I13733',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*Ru33*complexconjugate(Rd36)*complexconjugate(yd33)',
                   texname = '\\text{I13733}')

I13736 = Parameter(name = 'I13736',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*Ru63*complexconjugate(Rd36)*complexconjugate(yd33)',
                   texname = '\\text{I13736}')

I13763 = Parameter(name = 'I13763',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*Ru33*complexconjugate(Rd66)*complexconjugate(yd33)',
                   texname = '\\text{I13763}')

I13766 = Parameter(name = 'I13766',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*Ru63*complexconjugate(Rd66)*complexconjugate(yd33)',
                   texname = '\\text{I13766}')

I13833 = Parameter(name = 'I13833',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*Ru33*complexconjugate(Rd36)*complexconjugate(td33)',
                   texname = '\\text{I13833}')

I13836 = Parameter(name = 'I13836',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*Ru63*complexconjugate(Rd36)*complexconjugate(td33)',
                   texname = '\\text{I13836}')

I13863 = Parameter(name = 'I13863',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*Ru33*complexconjugate(Rd66)*complexconjugate(td33)',
                   texname = '\\text{I13863}')

I13866 = Parameter(name = 'I13866',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*Ru63*complexconjugate(Rd66)*complexconjugate(td33)',
                   texname = '\\text{I13866}')

I13933 = Parameter(name = 'I13933',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*Ru36*tu33*complexconjugate(Rd33)',
                   texname = '\\text{I13933}')

I13936 = Parameter(name = 'I13936',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*Ru66*tu33*complexconjugate(Rd33)',
                   texname = '\\text{I13936}')

I13963 = Parameter(name = 'I13963',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*Ru36*tu33*complexconjugate(Rd63)',
                   texname = '\\text{I13963}')

I13966 = Parameter(name = 'I13966',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*Ru66*tu33*complexconjugate(Rd63)',
                   texname = '\\text{I13966}')

I1433 = Parameter(name = 'I1433',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd33*complexconjugate(Rd36)*complexconjugate(td33)',
                  texname = '\\text{I1433}')

I1436 = Parameter(name = 'I1436',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd63*complexconjugate(Rd36)*complexconjugate(td33)',
                  texname = '\\text{I1436}')

I1463 = Parameter(name = 'I1463',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd33*complexconjugate(Rd66)*complexconjugate(td33)',
                  texname = '\\text{I1463}')

I1466 = Parameter(name = 'I1466',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd63*complexconjugate(Rd66)*complexconjugate(td33)',
                  texname = '\\text{I1466}')

I14033 = Parameter(name = 'I14033',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*Ru33*yd33*complexconjugate(Rd33)*complexconjugate(yd33)',
                   texname = '\\text{I14033}')

I14036 = Parameter(name = 'I14036',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*Ru63*yd33*complexconjugate(Rd33)*complexconjugate(yd33)',
                   texname = '\\text{I14036}')

I14063 = Parameter(name = 'I14063',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*Ru33*yd33*complexconjugate(Rd63)*complexconjugate(yd33)',
                   texname = '\\text{I14063}')

I14066 = Parameter(name = 'I14066',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*Ru63*yd33*complexconjugate(Rd63)*complexconjugate(yd33)',
                   texname = '\\text{I14066}')

I14133 = Parameter(name = 'I14133',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*Ru36*yu33*complexconjugate(Rd36)*complexconjugate(yd33)',
                   texname = '\\text{I14133}')

I14136 = Parameter(name = 'I14136',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*Ru66*yu33*complexconjugate(Rd36)*complexconjugate(yd33)',
                   texname = '\\text{I14136}')

I14163 = Parameter(name = 'I14163',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*Ru36*yu33*complexconjugate(Rd66)*complexconjugate(yd33)',
                   texname = '\\text{I14163}')

I14166 = Parameter(name = 'I14166',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*Ru66*yu33*complexconjugate(Rd66)*complexconjugate(yd33)',
                   texname = '\\text{I14166}')

I14233 = Parameter(name = 'I14233',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*Ru33*yu33*complexconjugate(Rd33)*complexconjugate(yu33)',
                   texname = '\\text{I14233}')

I14236 = Parameter(name = 'I14236',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*Ru63*yu33*complexconjugate(Rd33)*complexconjugate(yu33)',
                   texname = '\\text{I14236}')

I14263 = Parameter(name = 'I14263',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*Ru33*yu33*complexconjugate(Rd63)*complexconjugate(yu33)',
                   texname = '\\text{I14263}')

I14266 = Parameter(name = 'I14266',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*Ru63*yu33*complexconjugate(Rd63)*complexconjugate(yu33)',
                   texname = '\\text{I14266}')

I14333 = Parameter(name = 'I14333',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*Ru36*yu33*complexconjugate(Rd33)',
                   texname = '\\text{I14333}')

I14336 = Parameter(name = 'I14336',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*Ru66*yu33*complexconjugate(Rd33)',
                   texname = '\\text{I14336}')

I14363 = Parameter(name = 'I14363',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*Ru36*yu33*complexconjugate(Rd63)',
                   texname = '\\text{I14363}')

I14366 = Parameter(name = 'I14366',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*Ru66*yu33*complexconjugate(Rd63)',
                   texname = '\\text{I14366}')

I14411 = Parameter(name = 'I14411',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM11*Ru11*complexconjugate(Rd11)',
                   texname = '\\text{I14411}')

I14422 = Parameter(name = 'I14422',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM22*Ru22*complexconjugate(Rd22)',
                   texname = '\\text{I14422}')

I14433 = Parameter(name = 'I14433',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*Ru33*complexconjugate(Rd33)',
                   texname = '\\text{I14433}')

I14436 = Parameter(name = 'I14436',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*Ru63*complexconjugate(Rd33)',
                   texname = '\\text{I14436}')

I14463 = Parameter(name = 'I14463',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*Ru33*complexconjugate(Rd63)',
                   texname = '\\text{I14463}')

I14466 = Parameter(name = 'I14466',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*Ru63*complexconjugate(Rd63)',
                   texname = '\\text{I14466}')

I14533 = Parameter(name = 'I14533',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*Ru33*yd33*complexconjugate(Rd33)*complexconjugate(yd33)',
                   texname = '\\text{I14533}')

I14536 = Parameter(name = 'I14536',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*Ru63*yd33*complexconjugate(Rd33)*complexconjugate(yd33)',
                   texname = '\\text{I14536}')

I14563 = Parameter(name = 'I14563',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*Ru33*yd33*complexconjugate(Rd63)*complexconjugate(yd33)',
                   texname = '\\text{I14563}')

I14566 = Parameter(name = 'I14566',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*Ru63*yd33*complexconjugate(Rd63)*complexconjugate(yd33)',
                   texname = '\\text{I14566}')

I14633 = Parameter(name = 'I14633',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*Ru33*yu33*complexconjugate(Rd33)*complexconjugate(yu33)',
                   texname = '\\text{I14633}')

I14636 = Parameter(name = 'I14636',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*Ru63*yu33*complexconjugate(Rd33)*complexconjugate(yu33)',
                   texname = '\\text{I14636}')

I14663 = Parameter(name = 'I14663',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*Ru33*yu33*complexconjugate(Rd63)*complexconjugate(yu33)',
                   texname = '\\text{I14663}')

I14666 = Parameter(name = 'I14666',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*Ru63*yu33*complexconjugate(Rd63)*complexconjugate(yu33)',
                   texname = '\\text{I14666}')

I14733 = Parameter(name = 'I14733',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*Ru36*yu33*complexconjugate(Rd36)*complexconjugate(yd33)',
                   texname = '\\text{I14733}')

I14736 = Parameter(name = 'I14736',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*Ru66*yu33*complexconjugate(Rd36)*complexconjugate(yd33)',
                   texname = '\\text{I14736}')

I14763 = Parameter(name = 'I14763',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*Ru36*yu33*complexconjugate(Rd66)*complexconjugate(yd33)',
                   texname = '\\text{I14763}')

I14766 = Parameter(name = 'I14766',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*Ru66*yu33*complexconjugate(Rd66)*complexconjugate(yd33)',
                   texname = '\\text{I14766}')

I14811 = Parameter(name = 'I14811',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru11*complexconjugate(Ru11)',
                   texname = '\\text{I14811}')

I14822 = Parameter(name = 'I14822',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru22*complexconjugate(Ru22)',
                   texname = '\\text{I14822}')

I14833 = Parameter(name = 'I14833',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru33*complexconjugate(Ru33)',
                   texname = '\\text{I14833}')

I14836 = Parameter(name = 'I14836',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru63*complexconjugate(Ru33)',
                   texname = '\\text{I14836}')

I14863 = Parameter(name = 'I14863',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru33*complexconjugate(Ru63)',
                   texname = '\\text{I14863}')

I14866 = Parameter(name = 'I14866',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru63*complexconjugate(Ru63)',
                   texname = '\\text{I14866}')

I14933 = Parameter(name = 'I14933',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru36*complexconjugate(Ru36)',
                   texname = '\\text{I14933}')

I14936 = Parameter(name = 'I14936',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru66*complexconjugate(Ru36)',
                   texname = '\\text{I14936}')

I14944 = Parameter(name = 'I14944',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru44*complexconjugate(Ru44)',
                   texname = '\\text{I14944}')

I14955 = Parameter(name = 'I14955',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru55*complexconjugate(Ru55)',
                   texname = '\\text{I14955}')

I14963 = Parameter(name = 'I14963',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru36*complexconjugate(Ru66)',
                   texname = '\\text{I14963}')

I14966 = Parameter(name = 'I14966',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru66*complexconjugate(Ru66)',
                   texname = '\\text{I14966}')

I1533 = Parameter(name = 'I1533',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd33*complexconjugate(Rd36)*complexconjugate(yd33)',
                  texname = '\\text{I1533}')

I1536 = Parameter(name = 'I1536',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd63*complexconjugate(Rd36)*complexconjugate(yd33)',
                  texname = '\\text{I1536}')

I1563 = Parameter(name = 'I1563',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd33*complexconjugate(Rd66)*complexconjugate(yd33)',
                  texname = '\\text{I1563}')

I1566 = Parameter(name = 'I1566',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd63*complexconjugate(Rd66)*complexconjugate(yd33)',
                  texname = '\\text{I1566}')

I15033 = Parameter(name = 'I15033',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru33*complexconjugate(Ru36)*complexconjugate(yu33)',
                   texname = '\\text{I15033}')

I15036 = Parameter(name = 'I15036',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru63*complexconjugate(Ru36)*complexconjugate(yu33)',
                   texname = '\\text{I15036}')

I15063 = Parameter(name = 'I15063',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru33*complexconjugate(Ru66)*complexconjugate(yu33)',
                   texname = '\\text{I15063}')

I15066 = Parameter(name = 'I15066',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru63*complexconjugate(Ru66)*complexconjugate(yu33)',
                   texname = '\\text{I15066}')

I15133 = Parameter(name = 'I15133',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru33*complexconjugate(Ru36)*complexconjugate(tu33)',
                   texname = '\\text{I15133}')

I15136 = Parameter(name = 'I15136',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru63*complexconjugate(Ru36)*complexconjugate(tu33)',
                   texname = '\\text{I15136}')

I15163 = Parameter(name = 'I15163',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru33*complexconjugate(Ru66)*complexconjugate(tu33)',
                   texname = '\\text{I15163}')

I15166 = Parameter(name = 'I15166',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru63*complexconjugate(Ru66)*complexconjugate(tu33)',
                   texname = '\\text{I15166}')

I15233 = Parameter(name = 'I15233',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru36*tu33*complexconjugate(Ru33)',
                   texname = '\\text{I15233}')

I15236 = Parameter(name = 'I15236',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru66*tu33*complexconjugate(Ru33)',
                   texname = '\\text{I15236}')

I15263 = Parameter(name = 'I15263',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru36*tu33*complexconjugate(Ru63)',
                   texname = '\\text{I15263}')

I15266 = Parameter(name = 'I15266',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru66*tu33*complexconjugate(Ru63)',
                   texname = '\\text{I15266}')

I15333 = Parameter(name = 'I15333',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru36*yu33*complexconjugate(Ru33)',
                   texname = '\\text{I15333}')

I15336 = Parameter(name = 'I15336',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru66*yu33*complexconjugate(Ru33)',
                   texname = '\\text{I15336}')

I15363 = Parameter(name = 'I15363',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru36*yu33*complexconjugate(Ru63)',
                   texname = '\\text{I15363}')

I15366 = Parameter(name = 'I15366',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru66*yu33*complexconjugate(Ru63)',
                   texname = '\\text{I15366}')

I15433 = Parameter(name = 'I15433',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru33*yu33*complexconjugate(Ru33)*complexconjugate(yu33)',
                   texname = '\\text{I15433}')

I15436 = Parameter(name = 'I15436',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru63*yu33*complexconjugate(Ru33)*complexconjugate(yu33)',
                   texname = '\\text{I15436}')

I15463 = Parameter(name = 'I15463',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru33*yu33*complexconjugate(Ru63)*complexconjugate(yu33)',
                   texname = '\\text{I15463}')

I15466 = Parameter(name = 'I15466',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru63*yu33*complexconjugate(Ru63)*complexconjugate(yu33)',
                   texname = '\\text{I15466}')

I15533 = Parameter(name = 'I15533',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru36*yu33*complexconjugate(Ru36)*complexconjugate(yu33)',
                   texname = '\\text{I15533}')

I15536 = Parameter(name = 'I15536',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru66*yu33*complexconjugate(Ru36)*complexconjugate(yu33)',
                   texname = '\\text{I15536}')

I15563 = Parameter(name = 'I15563',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru36*yu33*complexconjugate(Ru66)*complexconjugate(yu33)',
                   texname = '\\text{I15563}')

I15566 = Parameter(name = 'I15566',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru66*yu33*complexconjugate(Ru66)*complexconjugate(yu33)',
                   texname = '\\text{I15566}')

I15633 = Parameter(name = 'I15633',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru33*yu33*complexconjugate(Ru33)*complexconjugate(yu33)',
                   texname = '\\text{I15633}')

I15636 = Parameter(name = 'I15636',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru63*yu33*complexconjugate(Ru33)*complexconjugate(yu33)',
                   texname = '\\text{I15636}')

I15663 = Parameter(name = 'I15663',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru33*yu33*complexconjugate(Ru63)*complexconjugate(yu33)',
                   texname = '\\text{I15663}')

I15666 = Parameter(name = 'I15666',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru63*yu33*complexconjugate(Ru63)*complexconjugate(yu33)',
                   texname = '\\text{I15666}')

I15733 = Parameter(name = 'I15733',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru36*yu33*complexconjugate(Ru36)*complexconjugate(yu33)',
                   texname = '\\text{I15733}')

I15736 = Parameter(name = 'I15736',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru66*yu33*complexconjugate(Ru36)*complexconjugate(yu33)',
                   texname = '\\text{I15736}')

I15763 = Parameter(name = 'I15763',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru36*yu33*complexconjugate(Ru66)*complexconjugate(yu33)',
                   texname = '\\text{I15763}')

I15766 = Parameter(name = 'I15766',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru66*yu33*complexconjugate(Ru66)*complexconjugate(yu33)',
                   texname = '\\text{I15766}')

I15833 = Parameter(name = 'I15833',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*Ru33*yd33*complexconjugate(CKM33)*complexconjugate(Ru33)*complexconjugate(yd33)',
                   texname = '\\text{I15833}')

I15836 = Parameter(name = 'I15836',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*Ru63*yd33*complexconjugate(CKM33)*complexconjugate(Ru33)*complexconjugate(yd33)',
                   texname = '\\text{I15836}')

I15863 = Parameter(name = 'I15863',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*Ru33*yd33*complexconjugate(CKM33)*complexconjugate(Ru63)*complexconjugate(yd33)',
                   texname = '\\text{I15863}')

I15866 = Parameter(name = 'I15866',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*Ru63*yd33*complexconjugate(CKM33)*complexconjugate(Ru63)*complexconjugate(yd33)',
                   texname = '\\text{I15866}')

I15911 = Parameter(name = 'I15911',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM11*Ru11*complexconjugate(Rd11)',
                   texname = '\\text{I15911}')

I15922 = Parameter(name = 'I15922',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM22*Ru22*complexconjugate(Rd22)',
                   texname = '\\text{I15922}')

I15933 = Parameter(name = 'I15933',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*Ru33*complexconjugate(Rd33)',
                   texname = '\\text{I15933}')

I15936 = Parameter(name = 'I15936',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*Ru63*complexconjugate(Rd33)',
                   texname = '\\text{I15936}')

I15963 = Parameter(name = 'I15963',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*Ru33*complexconjugate(Rd63)',
                   texname = '\\text{I15963}')

I15966 = Parameter(name = 'I15966',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*Ru63*complexconjugate(Rd63)',
                   texname = '\\text{I15966}')

I1633 = Parameter(name = 'I1633',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd36*td33*complexconjugate(Rd33)',
                  texname = '\\text{I1633}')

I1636 = Parameter(name = 'I1636',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd66*td33*complexconjugate(Rd33)',
                  texname = '\\text{I1636}')

I1663 = Parameter(name = 'I1663',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd36*td33*complexconjugate(Rd63)',
                  texname = '\\text{I1663}')

I1666 = Parameter(name = 'I1666',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd66*td33*complexconjugate(Rd63)',
                  texname = '\\text{I1666}')

I16033 = Parameter(name = 'I16033',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*Ru33*complexconjugate(Rd36)*complexconjugate(yd33)',
                   texname = '\\text{I16033}')

I16036 = Parameter(name = 'I16036',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*Ru63*complexconjugate(Rd36)*complexconjugate(yd33)',
                   texname = '\\text{I16036}')

I16063 = Parameter(name = 'I16063',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*Ru33*complexconjugate(Rd66)*complexconjugate(yd33)',
                   texname = '\\text{I16063}')

I16066 = Parameter(name = 'I16066',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*Ru63*complexconjugate(Rd66)*complexconjugate(yd33)',
                   texname = '\\text{I16066}')

I16111 = Parameter(name = 'I16111',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru11*complexconjugate(Ru11)',
                   texname = '\\text{I16111}')

I16122 = Parameter(name = 'I16122',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru22*complexconjugate(Ru22)',
                   texname = '\\text{I16122}')

I16133 = Parameter(name = 'I16133',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru33*complexconjugate(Ru33)',
                   texname = '\\text{I16133}')

I16136 = Parameter(name = 'I16136',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru63*complexconjugate(Ru33)',
                   texname = '\\text{I16136}')

I16163 = Parameter(name = 'I16163',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru33*complexconjugate(Ru63)',
                   texname = '\\text{I16163}')

I16166 = Parameter(name = 'I16166',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru63*complexconjugate(Ru63)',
                   texname = '\\text{I16166}')

I16233 = Parameter(name = 'I16233',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru36*complexconjugate(Ru36)',
                   texname = '\\text{I16233}')

I16236 = Parameter(name = 'I16236',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru66*complexconjugate(Ru36)',
                   texname = '\\text{I16236}')

I16244 = Parameter(name = 'I16244',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru44*complexconjugate(Ru44)',
                   texname = '\\text{I16244}')

I16255 = Parameter(name = 'I16255',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru55*complexconjugate(Ru55)',
                   texname = '\\text{I16255}')

I16263 = Parameter(name = 'I16263',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru36*complexconjugate(Ru66)',
                   texname = '\\text{I16263}')

I16266 = Parameter(name = 'I16266',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru66*complexconjugate(Ru66)',
                   texname = '\\text{I16266}')

I16311 = Parameter(name = 'I16311',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd11*complexconjugate(CKM11)*complexconjugate(Ru11)',
                   texname = '\\text{I16311}')

I16322 = Parameter(name = 'I16322',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd22*complexconjugate(CKM22)*complexconjugate(Ru22)',
                   texname = '\\text{I16322}')

I16333 = Parameter(name = 'I16333',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd33*complexconjugate(CKM33)*complexconjugate(Ru33)',
                   texname = '\\text{I16333}')

I16336 = Parameter(name = 'I16336',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd33*complexconjugate(CKM33)*complexconjugate(Ru63)',
                   texname = '\\text{I16336}')

I16363 = Parameter(name = 'I16363',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd63*complexconjugate(CKM33)*complexconjugate(Ru33)',
                   texname = '\\text{I16363}')

I16366 = Parameter(name = 'I16366',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd63*complexconjugate(CKM33)*complexconjugate(Ru63)',
                   texname = '\\text{I16366}')

I16433 = Parameter(name = 'I16433',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*Ru33*complexconjugate(Rd36)*complexconjugate(yd33)',
                   texname = '\\text{I16433}')

I16436 = Parameter(name = 'I16436',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*Ru63*complexconjugate(Rd36)*complexconjugate(yd33)',
                   texname = '\\text{I16436}')

I16463 = Parameter(name = 'I16463',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*Ru33*complexconjugate(Rd66)*complexconjugate(yd33)',
                   texname = '\\text{I16463}')

I16466 = Parameter(name = 'I16466',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*Ru63*complexconjugate(Rd66)*complexconjugate(yd33)',
                   texname = '\\text{I16466}')

I16533 = Parameter(name = 'I16533',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd36*yd33*complexconjugate(CKM33)*complexconjugate(Ru33)',
                   texname = '\\text{I16533}')

I16536 = Parameter(name = 'I16536',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd36*yd33*complexconjugate(CKM33)*complexconjugate(Ru63)',
                   texname = '\\text{I16536}')

I16563 = Parameter(name = 'I16563',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd66*yd33*complexconjugate(CKM33)*complexconjugate(Ru33)',
                   texname = '\\text{I16563}')

I16566 = Parameter(name = 'I16566',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd66*yd33*complexconjugate(CKM33)*complexconjugate(Ru63)',
                   texname = '\\text{I16566}')

I16633 = Parameter(name = 'I16633',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd33*complexconjugate(CKM33)*complexconjugate(Ru36)*complexconjugate(yu33)',
                   texname = '\\text{I16633}')

I16636 = Parameter(name = 'I16636',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd33*complexconjugate(CKM33)*complexconjugate(Ru66)*complexconjugate(yu33)',
                   texname = '\\text{I16636}')

I16663 = Parameter(name = 'I16663',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd63*complexconjugate(CKM33)*complexconjugate(Ru36)*complexconjugate(yu33)',
                   texname = '\\text{I16663}')

I16666 = Parameter(name = 'I16666',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd63*complexconjugate(CKM33)*complexconjugate(Ru66)*complexconjugate(yu33)',
                   texname = '\\text{I16666}')

I16733 = Parameter(name = 'I16733',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*Ru36*yu33*complexconjugate(Rd33)',
                   texname = '\\text{I16733}')

I16736 = Parameter(name = 'I16736',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*Ru66*yu33*complexconjugate(Rd33)',
                   texname = '\\text{I16736}')

I16763 = Parameter(name = 'I16763',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*Ru36*yu33*complexconjugate(Rd63)',
                   texname = '\\text{I16763}')

I16766 = Parameter(name = 'I16766',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*Ru66*yu33*complexconjugate(Rd63)',
                   texname = '\\text{I16766}')

I16811 = Parameter(name = 'I16811',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru11*complexconjugate(Ru11)',
                   texname = '\\text{I16811}')

I16822 = Parameter(name = 'I16822',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru22*complexconjugate(Ru22)',
                   texname = '\\text{I16822}')

I16833 = Parameter(name = 'I16833',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru33*complexconjugate(Ru33)',
                   texname = '\\text{I16833}')

I16836 = Parameter(name = 'I16836',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru63*complexconjugate(Ru33)',
                   texname = '\\text{I16836}')

I16863 = Parameter(name = 'I16863',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru33*complexconjugate(Ru63)',
                   texname = '\\text{I16863}')

I16866 = Parameter(name = 'I16866',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru63*complexconjugate(Ru63)',
                   texname = '\\text{I16866}')

I16911 = Parameter(name = 'I16911',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru11*complexconjugate(Ru11)',
                   texname = '\\text{I16911}')

I16922 = Parameter(name = 'I16922',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru22*complexconjugate(Ru22)',
                   texname = '\\text{I16922}')

I16933 = Parameter(name = 'I16933',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru33*complexconjugate(Ru33)',
                   texname = '\\text{I16933}')

I16936 = Parameter(name = 'I16936',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru63*complexconjugate(Ru33)',
                   texname = '\\text{I16936}')

I16963 = Parameter(name = 'I16963',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru33*complexconjugate(Ru63)',
                   texname = '\\text{I16963}')

I16966 = Parameter(name = 'I16966',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru63*complexconjugate(Ru63)',
                   texname = '\\text{I16966}')

I1733 = Parameter(name = 'I1733',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd36*yd33*complexconjugate(Rd33)',
                  texname = '\\text{I1733}')

I1736 = Parameter(name = 'I1736',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd66*yd33*complexconjugate(Rd33)',
                  texname = '\\text{I1736}')

I1763 = Parameter(name = 'I1763',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd36*yd33*complexconjugate(Rd63)',
                  texname = '\\text{I1763}')

I1766 = Parameter(name = 'I1766',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd66*yd33*complexconjugate(Rd63)',
                  texname = '\\text{I1766}')

I17011 = Parameter(name = 'I17011',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru11*complexconjugate(Ru11)',
                   texname = '\\text{I17011}')

I17022 = Parameter(name = 'I17022',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru22*complexconjugate(Ru22)',
                   texname = '\\text{I17022}')

I17033 = Parameter(name = 'I17033',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru33*complexconjugate(Ru33)',
                   texname = '\\text{I17033}')

I17036 = Parameter(name = 'I17036',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru63*complexconjugate(Ru33)',
                   texname = '\\text{I17036}')

I17063 = Parameter(name = 'I17063',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru33*complexconjugate(Ru63)',
                   texname = '\\text{I17063}')

I17066 = Parameter(name = 'I17066',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru63*complexconjugate(Ru63)',
                   texname = '\\text{I17066}')

I17111 = Parameter(name = 'I17111',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru11*complexconjugate(Ru11)',
                   texname = '\\text{I17111}')

I17122 = Parameter(name = 'I17122',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru22*complexconjugate(Ru22)',
                   texname = '\\text{I17122}')

I17133 = Parameter(name = 'I17133',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru33*complexconjugate(Ru33)',
                   texname = '\\text{I17133}')

I17136 = Parameter(name = 'I17136',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru63*complexconjugate(Ru33)',
                   texname = '\\text{I17136}')

I17163 = Parameter(name = 'I17163',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru33*complexconjugate(Ru63)',
                   texname = '\\text{I17163}')

I17166 = Parameter(name = 'I17166',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru63*complexconjugate(Ru63)',
                   texname = '\\text{I17166}')

I17233 = Parameter(name = 'I17233',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru36*complexconjugate(Ru36)',
                   texname = '\\text{I17233}')

I17236 = Parameter(name = 'I17236',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru66*complexconjugate(Ru36)',
                   texname = '\\text{I17236}')

I17244 = Parameter(name = 'I17244',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru44*complexconjugate(Ru44)',
                   texname = '\\text{I17244}')

I17255 = Parameter(name = 'I17255',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru55*complexconjugate(Ru55)',
                   texname = '\\text{I17255}')

I17263 = Parameter(name = 'I17263',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru36*complexconjugate(Ru66)',
                   texname = '\\text{I17263}')

I17266 = Parameter(name = 'I17266',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru66*complexconjugate(Ru66)',
                   texname = '\\text{I17266}')

I17311 = Parameter(name = 'I17311',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru11*complexconjugate(Ru11)',
                   texname = '\\text{I17311}')

I17322 = Parameter(name = 'I17322',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru22*complexconjugate(Ru22)',
                   texname = '\\text{I17322}')

I17333 = Parameter(name = 'I17333',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru33*complexconjugate(Ru33)',
                   texname = '\\text{I17333}')

I17336 = Parameter(name = 'I17336',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru63*complexconjugate(Ru33)',
                   texname = '\\text{I17336}')

I17363 = Parameter(name = 'I17363',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru33*complexconjugate(Ru63)',
                   texname = '\\text{I17363}')

I17366 = Parameter(name = 'I17366',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru63*complexconjugate(Ru63)',
                   texname = '\\text{I17366}')

I17433 = Parameter(name = 'I17433',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru36*complexconjugate(Ru36)',
                   texname = '\\text{I17433}')

I17436 = Parameter(name = 'I17436',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru66*complexconjugate(Ru36)',
                   texname = '\\text{I17436}')

I17444 = Parameter(name = 'I17444',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru44*complexconjugate(Ru44)',
                   texname = '\\text{I17444}')

I17455 = Parameter(name = 'I17455',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru55*complexconjugate(Ru55)',
                   texname = '\\text{I17455}')

I17463 = Parameter(name = 'I17463',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru36*complexconjugate(Ru66)',
                   texname = '\\text{I17463}')

I17466 = Parameter(name = 'I17466',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru66*complexconjugate(Ru66)',
                   texname = '\\text{I17466}')

I17533 = Parameter(name = 'I17533',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru36*complexconjugate(Ru36)',
                   texname = '\\text{I17533}')

I17536 = Parameter(name = 'I17536',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru66*complexconjugate(Ru36)',
                   texname = '\\text{I17536}')

I17544 = Parameter(name = 'I17544',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru44*complexconjugate(Ru44)',
                   texname = '\\text{I17544}')

I17555 = Parameter(name = 'I17555',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru55*complexconjugate(Ru55)',
                   texname = '\\text{I17555}')

I17563 = Parameter(name = 'I17563',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru36*complexconjugate(Ru66)',
                   texname = '\\text{I17563}')

I17566 = Parameter(name = 'I17566',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru66*complexconjugate(Ru66)',
                   texname = '\\text{I17566}')

I17633 = Parameter(name = 'I17633',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru36*complexconjugate(Ru36)',
                   texname = '\\text{I17633}')

I17636 = Parameter(name = 'I17636',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru66*complexconjugate(Ru36)',
                   texname = '\\text{I17636}')

I17644 = Parameter(name = 'I17644',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru44*complexconjugate(Ru44)',
                   texname = '\\text{I17644}')

I17655 = Parameter(name = 'I17655',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru55*complexconjugate(Ru55)',
                   texname = '\\text{I17655}')

I17663 = Parameter(name = 'I17663',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru36*complexconjugate(Ru66)',
                   texname = '\\text{I17663}')

I17666 = Parameter(name = 'I17666',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru66*complexconjugate(Ru66)',
                   texname = '\\text{I17666}')

I17733 = Parameter(name = 'I17733',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru36*complexconjugate(Ru36)',
                   texname = '\\text{I17733}')

I17736 = Parameter(name = 'I17736',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru66*complexconjugate(Ru36)',
                   texname = '\\text{I17736}')

I17744 = Parameter(name = 'I17744',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru44*complexconjugate(Ru44)',
                   texname = '\\text{I17744}')

I17755 = Parameter(name = 'I17755',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru55*complexconjugate(Ru55)',
                   texname = '\\text{I17755}')

I17763 = Parameter(name = 'I17763',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru36*complexconjugate(Ru66)',
                   texname = '\\text{I17763}')

I17766 = Parameter(name = 'I17766',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru66*complexconjugate(Ru66)',
                   texname = '\\text{I17766}')

I17833 = Parameter(name = 'I17833',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru36*complexconjugate(Ru36)',
                   texname = '\\text{I17833}')

I17836 = Parameter(name = 'I17836',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru66*complexconjugate(Ru36)',
                   texname = '\\text{I17836}')

I17844 = Parameter(name = 'I17844',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru44*complexconjugate(Ru44)',
                   texname = '\\text{I17844}')

I17855 = Parameter(name = 'I17855',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru55*complexconjugate(Ru55)',
                   texname = '\\text{I17855}')

I17863 = Parameter(name = 'I17863',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru36*complexconjugate(Ru66)',
                   texname = '\\text{I17863}')

I17866 = Parameter(name = 'I17866',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru66*complexconjugate(Ru66)',
                   texname = '\\text{I17866}')

I17933 = Parameter(name = 'I17933',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru33*complexconjugate(Ru36)*complexconjugate(yu33)',
                   texname = '\\text{I17933}')

I17936 = Parameter(name = 'I17936',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru63*complexconjugate(Ru36)*complexconjugate(yu33)',
                   texname = '\\text{I17936}')

I17963 = Parameter(name = 'I17963',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru33*complexconjugate(Ru66)*complexconjugate(yu33)',
                   texname = '\\text{I17963}')

I17966 = Parameter(name = 'I17966',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru63*complexconjugate(Ru66)*complexconjugate(yu33)',
                   texname = '\\text{I17966}')

I1833 = Parameter(name = 'I1833',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd36*yd33*complexconjugate(Rd36)*complexconjugate(yd33)',
                  texname = '\\text{I1833}')

I1836 = Parameter(name = 'I1836',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd66*yd33*complexconjugate(Rd36)*complexconjugate(yd33)',
                  texname = '\\text{I1836}')

I1863 = Parameter(name = 'I1863',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd36*yd33*complexconjugate(Rd66)*complexconjugate(yd33)',
                  texname = '\\text{I1863}')

I1866 = Parameter(name = 'I1866',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd66*yd33*complexconjugate(Rd66)*complexconjugate(yd33)',
                  texname = '\\text{I1866}')

I18033 = Parameter(name = 'I18033',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru36*yu33*complexconjugate(Ru33)',
                   texname = '\\text{I18033}')

I18036 = Parameter(name = 'I18036',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru66*yu33*complexconjugate(Ru33)',
                   texname = '\\text{I18036}')

I18063 = Parameter(name = 'I18063',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru36*yu33*complexconjugate(Ru63)',
                   texname = '\\text{I18063}')

I18066 = Parameter(name = 'I18066',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru66*yu33*complexconjugate(Ru63)',
                   texname = '\\text{I18066}')

I18133 = Parameter(name = 'I18133',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru33*complexconjugate(Ru36)*complexconjugate(yu33)',
                   texname = '\\text{I18133}')

I18136 = Parameter(name = 'I18136',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru63*complexconjugate(Ru36)*complexconjugate(yu33)',
                   texname = '\\text{I18136}')

I18163 = Parameter(name = 'I18163',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru33*complexconjugate(Ru66)*complexconjugate(yu33)',
                   texname = '\\text{I18163}')

I18166 = Parameter(name = 'I18166',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru63*complexconjugate(Ru66)*complexconjugate(yu33)',
                   texname = '\\text{I18166}')

I18233 = Parameter(name = 'I18233',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru36*yu33*complexconjugate(Ru33)',
                   texname = '\\text{I18233}')

I18236 = Parameter(name = 'I18236',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru66*yu33*complexconjugate(Ru33)',
                   texname = '\\text{I18236}')

I18263 = Parameter(name = 'I18263',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru36*yu33*complexconjugate(Ru63)',
                   texname = '\\text{I18263}')

I18266 = Parameter(name = 'I18266',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru66*yu33*complexconjugate(Ru63)',
                   texname = '\\text{I18266}')

I18333 = Parameter(name = 'I18333',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru33*complexconjugate(Ru36)*complexconjugate(yu33)',
                   texname = '\\text{I18333}')

I18336 = Parameter(name = 'I18336',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru63*complexconjugate(Ru36)*complexconjugate(yu33)',
                   texname = '\\text{I18336}')

I18363 = Parameter(name = 'I18363',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru33*complexconjugate(Ru66)*complexconjugate(yu33)',
                   texname = '\\text{I18363}')

I18366 = Parameter(name = 'I18366',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru63*complexconjugate(Ru66)*complexconjugate(yu33)',
                   texname = '\\text{I18366}')

I18433 = Parameter(name = 'I18433',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru36*yu33*complexconjugate(Ru33)',
                   texname = '\\text{I18433}')

I18436 = Parameter(name = 'I18436',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru66*yu33*complexconjugate(Ru33)',
                   texname = '\\text{I18436}')

I18463 = Parameter(name = 'I18463',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru36*yu33*complexconjugate(Ru63)',
                   texname = '\\text{I18463}')

I18466 = Parameter(name = 'I18466',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru66*yu33*complexconjugate(Ru63)',
                   texname = '\\text{I18466}')

I18533 = Parameter(name = 'I18533',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru33*complexconjugate(Ru36)*complexconjugate(yu33)',
                   texname = '\\text{I18533}')

I18536 = Parameter(name = 'I18536',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru63*complexconjugate(Ru36)*complexconjugate(yu33)',
                   texname = '\\text{I18536}')

I18563 = Parameter(name = 'I18563',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru33*complexconjugate(Ru66)*complexconjugate(yu33)',
                   texname = '\\text{I18563}')

I18566 = Parameter(name = 'I18566',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru63*complexconjugate(Ru66)*complexconjugate(yu33)',
                   texname = '\\text{I18566}')

I18633 = Parameter(name = 'I18633',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru36*yu33*complexconjugate(Ru33)',
                   texname = '\\text{I18633}')

I18636 = Parameter(name = 'I18636',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru66*yu33*complexconjugate(Ru33)',
                   texname = '\\text{I18636}')

I18663 = Parameter(name = 'I18663',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru36*yu33*complexconjugate(Ru63)',
                   texname = '\\text{I18663}')

I18666 = Parameter(name = 'I18666',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru66*yu33*complexconjugate(Ru63)',
                   texname = '\\text{I18666}')

I18711 = Parameter(name = 'I18711',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM11*complexconjugate(Rd11)',
                   texname = '\\text{I18711}')

I18722 = Parameter(name = 'I18722',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM22*complexconjugate(Rd22)',
                   texname = '\\text{I18722}')

I18733 = Parameter(name = 'I18733',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*complexconjugate(Rd33)',
                   texname = '\\text{I18733}')

I18736 = Parameter(name = 'I18736',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*complexconjugate(Rd63)',
                   texname = '\\text{I18736}')

I18833 = Parameter(name = 'I18833',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*complexconjugate(Rd36)*complexconjugate(yd33)',
                   texname = '\\text{I18833}')

I18836 = Parameter(name = 'I18836',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*complexconjugate(Rd66)*complexconjugate(yd33)',
                   texname = '\\text{I18836}')

I18933 = Parameter(name = 'I18933',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*yu33*complexconjugate(Rd33)',
                   texname = '\\text{I18933}')

I18936 = Parameter(name = 'I18936',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*yu33*complexconjugate(Rd63)',
                   texname = '\\text{I18936}')

I1933 = Parameter(name = 'I1933',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd33*yd33*complexconjugate(Rd33)*complexconjugate(yd33)',
                  texname = '\\text{I1933}')

I1936 = Parameter(name = 'I1936',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd63*yd33*complexconjugate(Rd33)*complexconjugate(yd33)',
                  texname = '\\text{I1936}')

I1963 = Parameter(name = 'I1963',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd33*yd33*complexconjugate(Rd63)*complexconjugate(yd33)',
                  texname = '\\text{I1963}')

I1966 = Parameter(name = 'I1966',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd63*yd33*complexconjugate(Rd63)*complexconjugate(yd33)',
                  texname = '\\text{I1966}')

I19011 = Parameter(name = 'I19011',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(Rl11)',
                   texname = '\\text{I19011}')

I19022 = Parameter(name = 'I19022',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(Rl22)',
                   texname = '\\text{I19022}')

I19033 = Parameter(name = 'I19033',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(Rl33)',
                   texname = '\\text{I19033}')

I19036 = Parameter(name = 'I19036',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(Rl63)',
                   texname = '\\text{I19036}')

I19133 = Parameter(name = 'I19133',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(Rl36)*complexconjugate(ye33)',
                   texname = '\\text{I19133}')

I19136 = Parameter(name = 'I19136',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(Rl66)*complexconjugate(ye33)',
                   texname = '\\text{I19136}')

I19211 = Parameter(name = 'I19211',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(Rn11)',
                   texname = '\\text{I19211}')

I19222 = Parameter(name = 'I19222',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(Rn22)',
                   texname = '\\text{I19222}')

I19233 = Parameter(name = 'I19233',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(Rn33)',
                   texname = '\\text{I19233}')

I19333 = Parameter(name = 'I19333',
                   nature = 'internal',
                   type = 'complex',
                   value = 'ye33*complexconjugate(Rn33)',
                   texname = '\\text{I19333}')

I19411 = Parameter(name = 'I19411',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(CKM11)*complexconjugate(Ru11)',
                   texname = '\\text{I19411}')

I19422 = Parameter(name = 'I19422',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(CKM22)*complexconjugate(Ru22)',
                   texname = '\\text{I19422}')

I19433 = Parameter(name = 'I19433',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(CKM33)*complexconjugate(Ru33)',
                   texname = '\\text{I19433}')

I19436 = Parameter(name = 'I19436',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(CKM33)*complexconjugate(Ru63)',
                   texname = '\\text{I19436}')

I19533 = Parameter(name = 'I19533',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(CKM33)*complexconjugate(Ru36)*complexconjugate(yu33)',
                   texname = '\\text{I19533}')

I19536 = Parameter(name = 'I19536',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(CKM33)*complexconjugate(Ru66)*complexconjugate(yu33)',
                   texname = '\\text{I19536}')

I19633 = Parameter(name = 'I19633',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yd33*complexconjugate(CKM33)*complexconjugate(Ru33)',
                   texname = '\\text{I19633}')

I19636 = Parameter(name = 'I19636',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yd33*complexconjugate(CKM33)*complexconjugate(Ru63)',
                   texname = '\\text{I19636}')

I19711 = Parameter(name = 'I19711',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM11*Ru11*complexconjugate(Rd11)',
                   texname = '\\text{I19711}')

I19722 = Parameter(name = 'I19722',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM22*Ru22*complexconjugate(Rd22)',
                   texname = '\\text{I19722}')

I19733 = Parameter(name = 'I19733',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*Ru33*complexconjugate(Rd33)',
                   texname = '\\text{I19733}')

I19736 = Parameter(name = 'I19736',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*Ru63*complexconjugate(Rd33)',
                   texname = '\\text{I19736}')

I19763 = Parameter(name = 'I19763',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*Ru33*complexconjugate(Rd63)',
                   texname = '\\text{I19763}')

I19766 = Parameter(name = 'I19766',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*Ru63*complexconjugate(Rd63)',
                   texname = '\\text{I19766}')

I19811 = Parameter(name = 'I19811',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn11*complexconjugate(Rl11)',
                   texname = '\\text{I19811}')

I19822 = Parameter(name = 'I19822',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn22*complexconjugate(Rl22)',
                   texname = '\\text{I19822}')

I19833 = Parameter(name = 'I19833',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn33*complexconjugate(Rl33)',
                   texname = '\\text{I19833}')

I19836 = Parameter(name = 'I19836',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn33*complexconjugate(Rl63)',
                   texname = '\\text{I19836}')

I19911 = Parameter(name = 'I19911',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd11*complexconjugate(CKM11)*complexconjugate(Ru11)',
                   texname = '\\text{I19911}')

I19922 = Parameter(name = 'I19922',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd22*complexconjugate(CKM22)*complexconjugate(Ru22)',
                   texname = '\\text{I19922}')

I19933 = Parameter(name = 'I19933',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd33*complexconjugate(CKM33)*complexconjugate(Ru33)',
                   texname = '\\text{I19933}')

I19936 = Parameter(name = 'I19936',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd33*complexconjugate(CKM33)*complexconjugate(Ru63)',
                   texname = '\\text{I19936}')

I19963 = Parameter(name = 'I19963',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd63*complexconjugate(CKM33)*complexconjugate(Ru33)',
                   texname = '\\text{I19963}')

I19966 = Parameter(name = 'I19966',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd63*complexconjugate(CKM33)*complexconjugate(Ru63)',
                   texname = '\\text{I19966}')

I233 = Parameter(name = 'I233',
                 nature = 'internal',
                 type = 'complex',
                 value = 'yd33*complexconjugate(CKM33)',
                 texname = '\\text{I233}')

I2033 = Parameter(name = 'I2033',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd36*yd33*complexconjugate(Rd36)*complexconjugate(yd33)',
                  texname = '\\text{I2033}')

I2036 = Parameter(name = 'I2036',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd66*yd33*complexconjugate(Rd36)*complexconjugate(yd33)',
                  texname = '\\text{I2036}')

I2063 = Parameter(name = 'I2063',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd36*yd33*complexconjugate(Rd66)*complexconjugate(yd33)',
                  texname = '\\text{I2063}')

I2066 = Parameter(name = 'I2066',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd66*yd33*complexconjugate(Rd66)*complexconjugate(yd33)',
                  texname = '\\text{I2066}')

I20011 = Parameter(name = 'I20011',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl11*complexconjugate(Rn11)',
                   texname = '\\text{I20011}')

I20022 = Parameter(name = 'I20022',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl22*complexconjugate(Rn22)',
                   texname = '\\text{I20022}')

I20033 = Parameter(name = 'I20033',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl33*complexconjugate(Rn33)',
                   texname = '\\text{I20033}')

I20036 = Parameter(name = 'I20036',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl63*complexconjugate(Rn33)',
                   texname = '\\text{I20036}')

I20111 = Parameter(name = 'I20111',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru11*complexconjugate(Ru11)',
                   texname = '\\text{I20111}')

I20122 = Parameter(name = 'I20122',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru22*complexconjugate(Ru22)',
                   texname = '\\text{I20122}')

I20133 = Parameter(name = 'I20133',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru33*complexconjugate(Ru33)',
                   texname = '\\text{I20133}')

I20136 = Parameter(name = 'I20136',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru63*complexconjugate(Ru33)',
                   texname = '\\text{I20136}')

I20163 = Parameter(name = 'I20163',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru33*complexconjugate(Ru63)',
                   texname = '\\text{I20163}')

I20166 = Parameter(name = 'I20166',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru63*complexconjugate(Ru63)',
                   texname = '\\text{I20166}')

I20233 = Parameter(name = 'I20233',
                   nature = 'internal',
                   type = 'complex',
                   value = 'ye33',
                   texname = '\\text{I20233}')

I20333 = Parameter(name = 'I20333',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru36*complexconjugate(Ru36)',
                   texname = '\\text{I20333}')

I20336 = Parameter(name = 'I20336',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru66*complexconjugate(Ru36)',
                   texname = '\\text{I20336}')

I20344 = Parameter(name = 'I20344',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru44*complexconjugate(Ru44)',
                   texname = '\\text{I20344}')

I20355 = Parameter(name = 'I20355',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru55*complexconjugate(Ru55)',
                   texname = '\\text{I20355}')

I20363 = Parameter(name = 'I20363',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru36*complexconjugate(Ru66)',
                   texname = '\\text{I20363}')

I20366 = Parameter(name = 'I20366',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru66*complexconjugate(Ru66)',
                   texname = '\\text{I20366}')

I2133 = Parameter(name = 'I2133',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd33*yd33*complexconjugate(Rd33)*complexconjugate(yd33)',
                  texname = '\\text{I2133}')

I2136 = Parameter(name = 'I2136',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd63*yd33*complexconjugate(Rd33)*complexconjugate(yd33)',
                  texname = '\\text{I2136}')

I2163 = Parameter(name = 'I2163',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd33*yd33*complexconjugate(Rd63)*complexconjugate(yd33)',
                  texname = '\\text{I2163}')

I2166 = Parameter(name = 'I2166',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd63*yd33*complexconjugate(Rd63)*complexconjugate(yd33)',
                  texname = '\\text{I2166}')

I2233 = Parameter(name = 'I2233',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM33*Rd33*yu33*complexconjugate(CKM33)*complexconjugate(Rd33)*complexconjugate(yu33)',
                  texname = '\\text{I2233}')

I2236 = Parameter(name = 'I2236',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM33*Rd63*yu33*complexconjugate(CKM33)*complexconjugate(Rd33)*complexconjugate(yu33)',
                  texname = '\\text{I2236}')

I2263 = Parameter(name = 'I2263',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM33*Rd33*yu33*complexconjugate(CKM33)*complexconjugate(Rd63)*complexconjugate(yu33)',
                  texname = '\\text{I2263}')

I2266 = Parameter(name = 'I2266',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM33*Rd63*yu33*complexconjugate(CKM33)*complexconjugate(Rd63)*complexconjugate(yu33)',
                  texname = '\\text{I2266}')

I2311 = Parameter(name = 'I2311',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd11*complexconjugate(Rd11)',
                  texname = '\\text{I2311}')

I2322 = Parameter(name = 'I2322',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd22*complexconjugate(Rd22)',
                  texname = '\\text{I2322}')

I2333 = Parameter(name = 'I2333',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd33*complexconjugate(Rd33)',
                  texname = '\\text{I2333}')

I2336 = Parameter(name = 'I2336',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd63*complexconjugate(Rd33)',
                  texname = '\\text{I2336}')

I2363 = Parameter(name = 'I2363',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd33*complexconjugate(Rd63)',
                  texname = '\\text{I2363}')

I2366 = Parameter(name = 'I2366',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd63*complexconjugate(Rd63)',
                  texname = '\\text{I2366}')

I2411 = Parameter(name = 'I2411',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd11*complexconjugate(Rd11)',
                  texname = '\\text{I2411}')

I2422 = Parameter(name = 'I2422',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd22*complexconjugate(Rd22)',
                  texname = '\\text{I2422}')

I2433 = Parameter(name = 'I2433',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd33*complexconjugate(Rd33)',
                  texname = '\\text{I2433}')

I2436 = Parameter(name = 'I2436',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd63*complexconjugate(Rd33)',
                  texname = '\\text{I2436}')

I2463 = Parameter(name = 'I2463',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd33*complexconjugate(Rd63)',
                  texname = '\\text{I2463}')

I2466 = Parameter(name = 'I2466',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd63*complexconjugate(Rd63)',
                  texname = '\\text{I2466}')

I2511 = Parameter(name = 'I2511',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd11*complexconjugate(Rd11)',
                  texname = '\\text{I2511}')

I2522 = Parameter(name = 'I2522',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd22*complexconjugate(Rd22)',
                  texname = '\\text{I2522}')

I2533 = Parameter(name = 'I2533',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd33*complexconjugate(Rd33)',
                  texname = '\\text{I2533}')

I2536 = Parameter(name = 'I2536',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd63*complexconjugate(Rd33)',
                  texname = '\\text{I2536}')

I2563 = Parameter(name = 'I2563',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd33*complexconjugate(Rd63)',
                  texname = '\\text{I2563}')

I2566 = Parameter(name = 'I2566',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd63*complexconjugate(Rd63)',
                  texname = '\\text{I2566}')

I2611 = Parameter(name = 'I2611',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd11*complexconjugate(Rd11)',
                  texname = '\\text{I2611}')

I2622 = Parameter(name = 'I2622',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd22*complexconjugate(Rd22)',
                  texname = '\\text{I2622}')

I2633 = Parameter(name = 'I2633',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd33*complexconjugate(Rd33)',
                  texname = '\\text{I2633}')

I2636 = Parameter(name = 'I2636',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd63*complexconjugate(Rd33)',
                  texname = '\\text{I2636}')

I2663 = Parameter(name = 'I2663',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd33*complexconjugate(Rd63)',
                  texname = '\\text{I2663}')

I2666 = Parameter(name = 'I2666',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd63*complexconjugate(Rd63)',
                  texname = '\\text{I2666}')

I2733 = Parameter(name = 'I2733',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd36*complexconjugate(Rd36)',
                  texname = '\\text{I2733}')

I2736 = Parameter(name = 'I2736',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd66*complexconjugate(Rd36)',
                  texname = '\\text{I2736}')

I2744 = Parameter(name = 'I2744',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd44*complexconjugate(Rd44)',
                  texname = '\\text{I2744}')

I2755 = Parameter(name = 'I2755',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd55*complexconjugate(Rd55)',
                  texname = '\\text{I2755}')

I2763 = Parameter(name = 'I2763',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd36*complexconjugate(Rd66)',
                  texname = '\\text{I2763}')

I2766 = Parameter(name = 'I2766',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd66*complexconjugate(Rd66)',
                  texname = '\\text{I2766}')

I2811 = Parameter(name = 'I2811',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd11*complexconjugate(Rd11)',
                  texname = '\\text{I2811}')

I2822 = Parameter(name = 'I2822',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd22*complexconjugate(Rd22)',
                  texname = '\\text{I2822}')

I2833 = Parameter(name = 'I2833',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd33*complexconjugate(Rd33)',
                  texname = '\\text{I2833}')

I2836 = Parameter(name = 'I2836',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd63*complexconjugate(Rd33)',
                  texname = '\\text{I2836}')

I2863 = Parameter(name = 'I2863',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd33*complexconjugate(Rd63)',
                  texname = '\\text{I2863}')

I2866 = Parameter(name = 'I2866',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd63*complexconjugate(Rd63)',
                  texname = '\\text{I2866}')

I2933 = Parameter(name = 'I2933',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd36*complexconjugate(Rd36)',
                  texname = '\\text{I2933}')

I2936 = Parameter(name = 'I2936',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd66*complexconjugate(Rd36)',
                  texname = '\\text{I2936}')

I2944 = Parameter(name = 'I2944',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd44*complexconjugate(Rd44)',
                  texname = '\\text{I2944}')

I2955 = Parameter(name = 'I2955',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd55*complexconjugate(Rd55)',
                  texname = '\\text{I2955}')

I2963 = Parameter(name = 'I2963',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd36*complexconjugate(Rd66)',
                  texname = '\\text{I2963}')

I2966 = Parameter(name = 'I2966',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd66*complexconjugate(Rd66)',
                  texname = '\\text{I2966}')

I333 = Parameter(name = 'I333',
                 nature = 'internal',
                 type = 'complex',
                 value = 'complexconjugate(Rd36)*complexconjugate(yd33)',
                 texname = '\\text{I333}')

I336 = Parameter(name = 'I336',
                 nature = 'internal',
                 type = 'complex',
                 value = 'complexconjugate(Rd66)*complexconjugate(yd33)',
                 texname = '\\text{I336}')

I3033 = Parameter(name = 'I3033',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd36*complexconjugate(Rd36)',
                  texname = '\\text{I3033}')

I3036 = Parameter(name = 'I3036',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd66*complexconjugate(Rd36)',
                  texname = '\\text{I3036}')

I3044 = Parameter(name = 'I3044',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd44*complexconjugate(Rd44)',
                  texname = '\\text{I3044}')

I3055 = Parameter(name = 'I3055',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd55*complexconjugate(Rd55)',
                  texname = '\\text{I3055}')

I3063 = Parameter(name = 'I3063',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd36*complexconjugate(Rd66)',
                  texname = '\\text{I3063}')

I3066 = Parameter(name = 'I3066',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd66*complexconjugate(Rd66)',
                  texname = '\\text{I3066}')

I3133 = Parameter(name = 'I3133',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd36*complexconjugate(Rd36)',
                  texname = '\\text{I3133}')

I3136 = Parameter(name = 'I3136',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd66*complexconjugate(Rd36)',
                  texname = '\\text{I3136}')

I3144 = Parameter(name = 'I3144',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd44*complexconjugate(Rd44)',
                  texname = '\\text{I3144}')

I3155 = Parameter(name = 'I3155',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd55*complexconjugate(Rd55)',
                  texname = '\\text{I3155}')

I3163 = Parameter(name = 'I3163',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd36*complexconjugate(Rd66)',
                  texname = '\\text{I3163}')

I3166 = Parameter(name = 'I3166',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd66*complexconjugate(Rd66)',
                  texname = '\\text{I3166}')

I3233 = Parameter(name = 'I3233',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd36*complexconjugate(Rd36)',
                  texname = '\\text{I3233}')

I3236 = Parameter(name = 'I3236',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd66*complexconjugate(Rd36)',
                  texname = '\\text{I3236}')

I3244 = Parameter(name = 'I3244',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd44*complexconjugate(Rd44)',
                  texname = '\\text{I3244}')

I3255 = Parameter(name = 'I3255',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd55*complexconjugate(Rd55)',
                  texname = '\\text{I3255}')

I3263 = Parameter(name = 'I3263',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd36*complexconjugate(Rd66)',
                  texname = '\\text{I3263}')

I3266 = Parameter(name = 'I3266',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd66*complexconjugate(Rd66)',
                  texname = '\\text{I3266}')

I3333 = Parameter(name = 'I3333',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd36*complexconjugate(Rd36)',
                  texname = '\\text{I3333}')

I3336 = Parameter(name = 'I3336',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd66*complexconjugate(Rd36)',
                  texname = '\\text{I3336}')

I3344 = Parameter(name = 'I3344',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd44*complexconjugate(Rd44)',
                  texname = '\\text{I3344}')

I3355 = Parameter(name = 'I3355',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd55*complexconjugate(Rd55)',
                  texname = '\\text{I3355}')

I3363 = Parameter(name = 'I3363',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd36*complexconjugate(Rd66)',
                  texname = '\\text{I3363}')

I3366 = Parameter(name = 'I3366',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd66*complexconjugate(Rd66)',
                  texname = '\\text{I3366}')

I3433 = Parameter(name = 'I3433',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd33*complexconjugate(Rd36)*complexconjugate(yd33)',
                  texname = '\\text{I3433}')

I3436 = Parameter(name = 'I3436',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd63*complexconjugate(Rd36)*complexconjugate(yd33)',
                  texname = '\\text{I3436}')

I3463 = Parameter(name = 'I3463',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd33*complexconjugate(Rd66)*complexconjugate(yd33)',
                  texname = '\\text{I3463}')

I3466 = Parameter(name = 'I3466',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd63*complexconjugate(Rd66)*complexconjugate(yd33)',
                  texname = '\\text{I3466}')

I3533 = Parameter(name = 'I3533',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd36*yd33*complexconjugate(Rd33)',
                  texname = '\\text{I3533}')

I3536 = Parameter(name = 'I3536',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd66*yd33*complexconjugate(Rd33)',
                  texname = '\\text{I3536}')

I3563 = Parameter(name = 'I3563',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd36*yd33*complexconjugate(Rd63)',
                  texname = '\\text{I3563}')

I3566 = Parameter(name = 'I3566',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd66*yd33*complexconjugate(Rd63)',
                  texname = '\\text{I3566}')

I3633 = Parameter(name = 'I3633',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd33*complexconjugate(Rd36)*complexconjugate(yd33)',
                  texname = '\\text{I3633}')

I3636 = Parameter(name = 'I3636',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd63*complexconjugate(Rd36)*complexconjugate(yd33)',
                  texname = '\\text{I3636}')

I3663 = Parameter(name = 'I3663',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd33*complexconjugate(Rd66)*complexconjugate(yd33)',
                  texname = '\\text{I3663}')

I3666 = Parameter(name = 'I3666',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd63*complexconjugate(Rd66)*complexconjugate(yd33)',
                  texname = '\\text{I3666}')

I3733 = Parameter(name = 'I3733',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd36*yd33*complexconjugate(Rd33)',
                  texname = '\\text{I3733}')

I3736 = Parameter(name = 'I3736',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd66*yd33*complexconjugate(Rd33)',
                  texname = '\\text{I3736}')

I3763 = Parameter(name = 'I3763',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd36*yd33*complexconjugate(Rd63)',
                  texname = '\\text{I3763}')

I3766 = Parameter(name = 'I3766',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd66*yd33*complexconjugate(Rd63)',
                  texname = '\\text{I3766}')

I3833 = Parameter(name = 'I3833',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd33*complexconjugate(Rd36)*complexconjugate(yd33)',
                  texname = '\\text{I3833}')

I3836 = Parameter(name = 'I3836',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd63*complexconjugate(Rd36)*complexconjugate(yd33)',
                  texname = '\\text{I3836}')

I3863 = Parameter(name = 'I3863',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd33*complexconjugate(Rd66)*complexconjugate(yd33)',
                  texname = '\\text{I3863}')

I3866 = Parameter(name = 'I3866',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd63*complexconjugate(Rd66)*complexconjugate(yd33)',
                  texname = '\\text{I3866}')

I3933 = Parameter(name = 'I3933',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd36*yd33*complexconjugate(Rd33)',
                  texname = '\\text{I3933}')

I3936 = Parameter(name = 'I3936',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd66*yd33*complexconjugate(Rd33)',
                  texname = '\\text{I3936}')

I3963 = Parameter(name = 'I3963',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd36*yd33*complexconjugate(Rd63)',
                  texname = '\\text{I3963}')

I3966 = Parameter(name = 'I3966',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd66*yd33*complexconjugate(Rd63)',
                  texname = '\\text{I3966}')

I433 = Parameter(name = 'I433',
                 nature = 'internal',
                 type = 'complex',
                 value = 'yd33*complexconjugate(Rd33)',
                 texname = '\\text{I433}')

I436 = Parameter(name = 'I436',
                 nature = 'internal',
                 type = 'complex',
                 value = 'yd33*complexconjugate(Rd63)',
                 texname = '\\text{I436}')

I4033 = Parameter(name = 'I4033',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd33*complexconjugate(Rd36)*complexconjugate(yd33)',
                  texname = '\\text{I4033}')

I4036 = Parameter(name = 'I4036',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd63*complexconjugate(Rd36)*complexconjugate(yd33)',
                  texname = '\\text{I4036}')

I4063 = Parameter(name = 'I4063',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd33*complexconjugate(Rd66)*complexconjugate(yd33)',
                  texname = '\\text{I4063}')

I4066 = Parameter(name = 'I4066',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd63*complexconjugate(Rd66)*complexconjugate(yd33)',
                  texname = '\\text{I4066}')

I4133 = Parameter(name = 'I4133',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd36*yd33*complexconjugate(Rd33)',
                  texname = '\\text{I4133}')

I4136 = Parameter(name = 'I4136',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd66*yd33*complexconjugate(Rd33)',
                  texname = '\\text{I4136}')

I4163 = Parameter(name = 'I4163',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd36*yd33*complexconjugate(Rd63)',
                  texname = '\\text{I4163}')

I4166 = Parameter(name = 'I4166',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd66*yd33*complexconjugate(Rd63)',
                  texname = '\\text{I4166}')

I4233 = Parameter(name = 'I4233',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM33*complexconjugate(yd33)',
                  texname = '\\text{I4233}')

I4333 = Parameter(name = 'I4333',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM33*yu33',
                  texname = '\\text{I4333}')

I4433 = Parameter(name = 'I4433',
                  nature = 'internal',
                  type = 'complex',
                  value = 'complexconjugate(ye33)',
                  texname = '\\text{I4433}')

I4533 = Parameter(name = 'I4533',
                  nature = 'internal',
                  type = 'complex',
                  value = 'complexconjugate(Rl36)*complexconjugate(ye33)',
                  texname = '\\text{I4533}')

I4536 = Parameter(name = 'I4536',
                  nature = 'internal',
                  type = 'complex',
                  value = 'complexconjugate(Rl66)*complexconjugate(ye33)',
                  texname = '\\text{I4536}')

I4633 = Parameter(name = 'I4633',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ye33*complexconjugate(Rl33)',
                  texname = '\\text{I4633}')

I4636 = Parameter(name = 'I4636',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ye33*complexconjugate(Rl63)',
                  texname = '\\text{I4636}')

I4711 = Parameter(name = 'I4711',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl11*complexconjugate(Rl11)',
                  texname = '\\text{I4711}')

I4722 = Parameter(name = 'I4722',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl22*complexconjugate(Rl22)',
                  texname = '\\text{I4722}')

I4733 = Parameter(name = 'I4733',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl33*complexconjugate(Rl33)',
                  texname = '\\text{I4733}')

I4736 = Parameter(name = 'I4736',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl63*complexconjugate(Rl33)',
                  texname = '\\text{I4736}')

I4763 = Parameter(name = 'I4763',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl33*complexconjugate(Rl63)',
                  texname = '\\text{I4763}')

I4766 = Parameter(name = 'I4766',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl63*complexconjugate(Rl63)',
                  texname = '\\text{I4766}')

I4833 = Parameter(name = 'I4833',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl36*complexconjugate(Rl36)',
                  texname = '\\text{I4833}')

I4836 = Parameter(name = 'I4836',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl66*complexconjugate(Rl36)',
                  texname = '\\text{I4836}')

I4844 = Parameter(name = 'I4844',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl44*complexconjugate(Rl44)',
                  texname = '\\text{I4844}')

I4855 = Parameter(name = 'I4855',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl55*complexconjugate(Rl55)',
                  texname = '\\text{I4855}')

I4863 = Parameter(name = 'I4863',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl36*complexconjugate(Rl66)',
                  texname = '\\text{I4863}')

I4866 = Parameter(name = 'I4866',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl66*complexconjugate(Rl66)',
                  texname = '\\text{I4866}')

I4933 = Parameter(name = 'I4933',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl33*complexconjugate(ye33)',
                  texname = '\\text{I4933}')

I4936 = Parameter(name = 'I4936',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl63*complexconjugate(ye33)',
                  texname = '\\text{I4936}')

I511 = Parameter(name = 'I511',
                 nature = 'internal',
                 type = 'complex',
                 value = 'Rd11*complexconjugate(Rd11)',
                 texname = '\\text{I511}')

I522 = Parameter(name = 'I522',
                 nature = 'internal',
                 type = 'complex',
                 value = 'Rd22*complexconjugate(Rd22)',
                 texname = '\\text{I522}')

I533 = Parameter(name = 'I533',
                 nature = 'internal',
                 type = 'complex',
                 value = 'Rd33*complexconjugate(Rd33)',
                 texname = '\\text{I533}')

I536 = Parameter(name = 'I536',
                 nature = 'internal',
                 type = 'complex',
                 value = 'Rd63*complexconjugate(Rd33)',
                 texname = '\\text{I536}')

I563 = Parameter(name = 'I563',
                 nature = 'internal',
                 type = 'complex',
                 value = 'Rd33*complexconjugate(Rd63)',
                 texname = '\\text{I563}')

I566 = Parameter(name = 'I566',
                 nature = 'internal',
                 type = 'complex',
                 value = 'Rd63*complexconjugate(Rd63)',
                 texname = '\\text{I566}')

I5033 = Parameter(name = 'I5033',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl36*ye33',
                  texname = '\\text{I5033}')

I5036 = Parameter(name = 'I5036',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl66*ye33',
                  texname = '\\text{I5036}')

I5111 = Parameter(name = 'I5111',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl11',
                  texname = '\\text{I5111}')

I5122 = Parameter(name = 'I5122',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl22',
                  texname = '\\text{I5122}')

I5133 = Parameter(name = 'I5133',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl33',
                  texname = '\\text{I5133}')

I5136 = Parameter(name = 'I5136',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl63',
                  texname = '\\text{I5136}')

I5233 = Parameter(name = 'I5233',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl36*ye33',
                  texname = '\\text{I5233}')

I5236 = Parameter(name = 'I5236',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl66*ye33',
                  texname = '\\text{I5236}')

I5311 = Parameter(name = 'I5311',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl11*complexconjugate(Rl11)',
                  texname = '\\text{I5311}')

I5322 = Parameter(name = 'I5322',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl22*complexconjugate(Rl22)',
                  texname = '\\text{I5322}')

I5333 = Parameter(name = 'I5333',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl33*complexconjugate(Rl33)',
                  texname = '\\text{I5333}')

I5336 = Parameter(name = 'I5336',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl63*complexconjugate(Rl33)',
                  texname = '\\text{I5336}')

I5363 = Parameter(name = 'I5363',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl33*complexconjugate(Rl63)',
                  texname = '\\text{I5363}')

I5366 = Parameter(name = 'I5366',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl63*complexconjugate(Rl63)',
                  texname = '\\text{I5366}')

I5433 = Parameter(name = 'I5433',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl36*complexconjugate(Rl36)',
                  texname = '\\text{I5433}')

I5436 = Parameter(name = 'I5436',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl66*complexconjugate(Rl36)',
                  texname = '\\text{I5436}')

I5444 = Parameter(name = 'I5444',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl44*complexconjugate(Rl44)',
                  texname = '\\text{I5444}')

I5455 = Parameter(name = 'I5455',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl55*complexconjugate(Rl55)',
                  texname = '\\text{I5455}')

I5463 = Parameter(name = 'I5463',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl36*complexconjugate(Rl66)',
                  texname = '\\text{I5463}')

I5466 = Parameter(name = 'I5466',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl66*complexconjugate(Rl66)',
                  texname = '\\text{I5466}')

I5533 = Parameter(name = 'I5533',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl33*complexconjugate(Rl36)*complexconjugate(te33)',
                  texname = '\\text{I5533}')

I5536 = Parameter(name = 'I5536',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl63*complexconjugate(Rl36)*complexconjugate(te33)',
                  texname = '\\text{I5536}')

I5563 = Parameter(name = 'I5563',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl33*complexconjugate(Rl66)*complexconjugate(te33)',
                  texname = '\\text{I5563}')

I5566 = Parameter(name = 'I5566',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl63*complexconjugate(Rl66)*complexconjugate(te33)',
                  texname = '\\text{I5566}')

I5633 = Parameter(name = 'I5633',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl33*complexconjugate(Rl36)*complexconjugate(ye33)',
                  texname = '\\text{I5633}')

I5636 = Parameter(name = 'I5636',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl63*complexconjugate(Rl36)*complexconjugate(ye33)',
                  texname = '\\text{I5636}')

I5663 = Parameter(name = 'I5663',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl33*complexconjugate(Rl66)*complexconjugate(ye33)',
                  texname = '\\text{I5663}')

I5666 = Parameter(name = 'I5666',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl63*complexconjugate(Rl66)*complexconjugate(ye33)',
                  texname = '\\text{I5666}')

I5733 = Parameter(name = 'I5733',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl36*te33*complexconjugate(Rl33)',
                  texname = '\\text{I5733}')

I5736 = Parameter(name = 'I5736',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl66*te33*complexconjugate(Rl33)',
                  texname = '\\text{I5736}')

I5763 = Parameter(name = 'I5763',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl36*te33*complexconjugate(Rl63)',
                  texname = '\\text{I5763}')

I5766 = Parameter(name = 'I5766',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl66*te33*complexconjugate(Rl63)',
                  texname = '\\text{I5766}')

I5833 = Parameter(name = 'I5833',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl33*ye33*complexconjugate(Rl33)*complexconjugate(ye33)',
                  texname = '\\text{I5833}')

I5836 = Parameter(name = 'I5836',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl63*ye33*complexconjugate(Rl33)*complexconjugate(ye33)',
                  texname = '\\text{I5836}')

I5863 = Parameter(name = 'I5863',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl33*ye33*complexconjugate(Rl63)*complexconjugate(ye33)',
                  texname = '\\text{I5863}')

I5866 = Parameter(name = 'I5866',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl63*ye33*complexconjugate(Rl63)*complexconjugate(ye33)',
                  texname = '\\text{I5866}')

I5933 = Parameter(name = 'I5933',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl36*ye33*complexconjugate(Rl33)',
                  texname = '\\text{I5933}')

I5936 = Parameter(name = 'I5936',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl66*ye33*complexconjugate(Rl33)',
                  texname = '\\text{I5936}')

I5963 = Parameter(name = 'I5963',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl36*ye33*complexconjugate(Rl63)',
                  texname = '\\text{I5963}')

I5966 = Parameter(name = 'I5966',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl66*ye33*complexconjugate(Rl63)',
                  texname = '\\text{I5966}')

I633 = Parameter(name = 'I633',
                 nature = 'internal',
                 type = 'complex',
                 value = 'Rd36*complexconjugate(Rd36)',
                 texname = '\\text{I633}')

I636 = Parameter(name = 'I636',
                 nature = 'internal',
                 type = 'complex',
                 value = 'Rd66*complexconjugate(Rd36)',
                 texname = '\\text{I636}')

I644 = Parameter(name = 'I644',
                 nature = 'internal',
                 type = 'complex',
                 value = 'Rd44*complexconjugate(Rd44)',
                 texname = '\\text{I644}')

I655 = Parameter(name = 'I655',
                 nature = 'internal',
                 type = 'complex',
                 value = 'Rd55*complexconjugate(Rd55)',
                 texname = '\\text{I655}')

I663 = Parameter(name = 'I663',
                 nature = 'internal',
                 type = 'complex',
                 value = 'Rd36*complexconjugate(Rd66)',
                 texname = '\\text{I663}')

I666 = Parameter(name = 'I666',
                 nature = 'internal',
                 type = 'complex',
                 value = 'Rd66*complexconjugate(Rd66)',
                 texname = '\\text{I666}')

I6033 = Parameter(name = 'I6033',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl36*ye33*complexconjugate(Rl36)*complexconjugate(ye33)',
                  texname = '\\text{I6033}')

I6036 = Parameter(name = 'I6036',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl66*ye33*complexconjugate(Rl36)*complexconjugate(ye33)',
                  texname = '\\text{I6036}')

I6063 = Parameter(name = 'I6063',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl36*ye33*complexconjugate(Rl66)*complexconjugate(ye33)',
                  texname = '\\text{I6063}')

I6066 = Parameter(name = 'I6066',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl66*ye33*complexconjugate(Rl66)*complexconjugate(ye33)',
                  texname = '\\text{I6066}')

I6133 = Parameter(name = 'I6133',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl33*ye33*complexconjugate(Rl33)*complexconjugate(ye33)',
                  texname = '\\text{I6133}')

I6136 = Parameter(name = 'I6136',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl63*ye33*complexconjugate(Rl33)*complexconjugate(ye33)',
                  texname = '\\text{I6136}')

I6163 = Parameter(name = 'I6163',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl33*ye33*complexconjugate(Rl63)*complexconjugate(ye33)',
                  texname = '\\text{I6163}')

I6166 = Parameter(name = 'I6166',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl63*ye33*complexconjugate(Rl63)*complexconjugate(ye33)',
                  texname = '\\text{I6166}')

I6233 = Parameter(name = 'I6233',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl36*ye33*complexconjugate(Rl36)*complexconjugate(ye33)',
                  texname = '\\text{I6233}')

I6236 = Parameter(name = 'I6236',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl66*ye33*complexconjugate(Rl36)*complexconjugate(ye33)',
                  texname = '\\text{I6236}')

I6263 = Parameter(name = 'I6263',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl36*ye33*complexconjugate(Rl66)*complexconjugate(ye33)',
                  texname = '\\text{I6263}')

I6266 = Parameter(name = 'I6266',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl66*ye33*complexconjugate(Rl66)*complexconjugate(ye33)',
                  texname = '\\text{I6266}')

I6333 = Parameter(name = 'I6333',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd36*complexconjugate(Rd36)',
                  texname = '\\text{I6333}')

I6336 = Parameter(name = 'I6336',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd66*complexconjugate(Rd36)',
                  texname = '\\text{I6336}')

I6344 = Parameter(name = 'I6344',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd44*complexconjugate(Rd44)',
                  texname = '\\text{I6344}')

I6355 = Parameter(name = 'I6355',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd55*complexconjugate(Rd55)',
                  texname = '\\text{I6355}')

I6363 = Parameter(name = 'I6363',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd36*complexconjugate(Rd66)',
                  texname = '\\text{I6363}')

I6366 = Parameter(name = 'I6366',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd66*complexconjugate(Rd66)',
                  texname = '\\text{I6366}')

I6411 = Parameter(name = 'I6411',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl11*complexconjugate(Rl11)',
                  texname = '\\text{I6411}')

I6422 = Parameter(name = 'I6422',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl22*complexconjugate(Rl22)',
                  texname = '\\text{I6422}')

I6433 = Parameter(name = 'I6433',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl33*complexconjugate(Rl33)',
                  texname = '\\text{I6433}')

I6436 = Parameter(name = 'I6436',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl63*complexconjugate(Rl33)',
                  texname = '\\text{I6436}')

I6463 = Parameter(name = 'I6463',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl33*complexconjugate(Rl63)',
                  texname = '\\text{I6463}')

I6466 = Parameter(name = 'I6466',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl63*complexconjugate(Rl63)',
                  texname = '\\text{I6466}')

I6511 = Parameter(name = 'I6511',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd11*complexconjugate(Rd11)',
                  texname = '\\text{I6511}')

I6522 = Parameter(name = 'I6522',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd22*complexconjugate(Rd22)',
                  texname = '\\text{I6522}')

I6533 = Parameter(name = 'I6533',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd33*complexconjugate(Rd33)',
                  texname = '\\text{I6533}')

I6536 = Parameter(name = 'I6536',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd63*complexconjugate(Rd33)',
                  texname = '\\text{I6536}')

I6563 = Parameter(name = 'I6563',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd33*complexconjugate(Rd63)',
                  texname = '\\text{I6563}')

I6566 = Parameter(name = 'I6566',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd63*complexconjugate(Rd63)',
                  texname = '\\text{I6566}')

I6633 = Parameter(name = 'I6633',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl36*complexconjugate(Rl36)',
                  texname = '\\text{I6633}')

I6636 = Parameter(name = 'I6636',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl66*complexconjugate(Rl36)',
                  texname = '\\text{I6636}')

I6644 = Parameter(name = 'I6644',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl44*complexconjugate(Rl44)',
                  texname = '\\text{I6644}')

I6655 = Parameter(name = 'I6655',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl55*complexconjugate(Rl55)',
                  texname = '\\text{I6655}')

I6663 = Parameter(name = 'I6663',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl36*complexconjugate(Rl66)',
                  texname = '\\text{I6663}')

I6666 = Parameter(name = 'I6666',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl66*complexconjugate(Rl66)',
                  texname = '\\text{I6666}')

I6733 = Parameter(name = 'I6733',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl33*complexconjugate(Rl36)*complexconjugate(ye33)',
                  texname = '\\text{I6733}')

I6736 = Parameter(name = 'I6736',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl63*complexconjugate(Rl36)*complexconjugate(ye33)',
                  texname = '\\text{I6736}')

I6763 = Parameter(name = 'I6763',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl33*complexconjugate(Rl66)*complexconjugate(ye33)',
                  texname = '\\text{I6763}')

I6766 = Parameter(name = 'I6766',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl63*complexconjugate(Rl66)*complexconjugate(ye33)',
                  texname = '\\text{I6766}')

I6833 = Parameter(name = 'I6833',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd36*yd33*complexconjugate(Rd33)',
                  texname = '\\text{I6833}')

I6836 = Parameter(name = 'I6836',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd66*yd33*complexconjugate(Rd33)',
                  texname = '\\text{I6836}')

I6863 = Parameter(name = 'I6863',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd36*yd33*complexconjugate(Rd63)',
                  texname = '\\text{I6863}')

I6866 = Parameter(name = 'I6866',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd66*yd33*complexconjugate(Rd63)',
                  texname = '\\text{I6866}')

I6933 = Parameter(name = 'I6933',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd33*complexconjugate(Rd36)*complexconjugate(yd33)',
                  texname = '\\text{I6933}')

I6936 = Parameter(name = 'I6936',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd63*complexconjugate(Rd36)*complexconjugate(yd33)',
                  texname = '\\text{I6936}')

I6963 = Parameter(name = 'I6963',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd33*complexconjugate(Rd66)*complexconjugate(yd33)',
                  texname = '\\text{I6963}')

I6966 = Parameter(name = 'I6966',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd63*complexconjugate(Rd66)*complexconjugate(yd33)',
                  texname = '\\text{I6966}')

I711 = Parameter(name = 'I711',
                 nature = 'internal',
                 type = 'complex',
                 value = 'Rd11*complexconjugate(CKM11)',
                 texname = '\\text{I711}')

I722 = Parameter(name = 'I722',
                 nature = 'internal',
                 type = 'complex',
                 value = 'Rd22*complexconjugate(CKM22)',
                 texname = '\\text{I722}')

I733 = Parameter(name = 'I733',
                 nature = 'internal',
                 type = 'complex',
                 value = 'Rd33*complexconjugate(CKM33)',
                 texname = '\\text{I733}')

I736 = Parameter(name = 'I736',
                 nature = 'internal',
                 type = 'complex',
                 value = 'Rd63*complexconjugate(CKM33)',
                 texname = '\\text{I736}')

I7033 = Parameter(name = 'I7033',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl36*ye33*complexconjugate(Rl33)',
                  texname = '\\text{I7033}')

I7036 = Parameter(name = 'I7036',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl66*ye33*complexconjugate(Rl33)',
                  texname = '\\text{I7036}')

I7063 = Parameter(name = 'I7063',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl36*ye33*complexconjugate(Rl63)',
                  texname = '\\text{I7063}')

I7066 = Parameter(name = 'I7066',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl66*ye33*complexconjugate(Rl63)',
                  texname = '\\text{I7066}')

I7111 = Parameter(name = 'I7111',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl11*complexconjugate(Rl11)',
                  texname = '\\text{I7111}')

I7122 = Parameter(name = 'I7122',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl22*complexconjugate(Rl22)',
                  texname = '\\text{I7122}')

I7133 = Parameter(name = 'I7133',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl33*complexconjugate(Rl33)',
                  texname = '\\text{I7133}')

I7136 = Parameter(name = 'I7136',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl63*complexconjugate(Rl33)',
                  texname = '\\text{I7136}')

I7163 = Parameter(name = 'I7163',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl33*complexconjugate(Rl63)',
                  texname = '\\text{I7163}')

I7166 = Parameter(name = 'I7166',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl63*complexconjugate(Rl63)',
                  texname = '\\text{I7166}')

I7211 = Parameter(name = 'I7211',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl11*complexconjugate(Rl11)',
                  texname = '\\text{I7211}')

I7222 = Parameter(name = 'I7222',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl22*complexconjugate(Rl22)',
                  texname = '\\text{I7222}')

I7233 = Parameter(name = 'I7233',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl33*complexconjugate(Rl33)',
                  texname = '\\text{I7233}')

I7236 = Parameter(name = 'I7236',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl63*complexconjugate(Rl33)',
                  texname = '\\text{I7236}')

I7263 = Parameter(name = 'I7263',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl33*complexconjugate(Rl63)',
                  texname = '\\text{I7263}')

I7266 = Parameter(name = 'I7266',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl63*complexconjugate(Rl63)',
                  texname = '\\text{I7266}')

I7311 = Parameter(name = 'I7311',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl11*complexconjugate(Rl11)',
                  texname = '\\text{I7311}')

I7322 = Parameter(name = 'I7322',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl22*complexconjugate(Rl22)',
                  texname = '\\text{I7322}')

I7333 = Parameter(name = 'I7333',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl33*complexconjugate(Rl33)',
                  texname = '\\text{I7333}')

I7336 = Parameter(name = 'I7336',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl63*complexconjugate(Rl33)',
                  texname = '\\text{I7336}')

I7363 = Parameter(name = 'I7363',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl33*complexconjugate(Rl63)',
                  texname = '\\text{I7363}')

I7366 = Parameter(name = 'I7366',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl63*complexconjugate(Rl63)',
                  texname = '\\text{I7366}')

I7411 = Parameter(name = 'I7411',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl11*complexconjugate(Rl11)',
                  texname = '\\text{I7411}')

I7422 = Parameter(name = 'I7422',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl22*complexconjugate(Rl22)',
                  texname = '\\text{I7422}')

I7433 = Parameter(name = 'I7433',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl33*complexconjugate(Rl33)',
                  texname = '\\text{I7433}')

I7436 = Parameter(name = 'I7436',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl63*complexconjugate(Rl33)',
                  texname = '\\text{I7436}')

I7463 = Parameter(name = 'I7463',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl33*complexconjugate(Rl63)',
                  texname = '\\text{I7463}')

I7466 = Parameter(name = 'I7466',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl63*complexconjugate(Rl63)',
                  texname = '\\text{I7466}')

I7511 = Parameter(name = 'I7511',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl11*complexconjugate(Rl11)',
                  texname = '\\text{I7511}')

I7522 = Parameter(name = 'I7522',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl22*complexconjugate(Rl22)',
                  texname = '\\text{I7522}')

I7533 = Parameter(name = 'I7533',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl33*complexconjugate(Rl33)',
                  texname = '\\text{I7533}')

I7536 = Parameter(name = 'I7536',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl63*complexconjugate(Rl33)',
                  texname = '\\text{I7536}')

I7563 = Parameter(name = 'I7563',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl33*complexconjugate(Rl63)',
                  texname = '\\text{I7563}')

I7566 = Parameter(name = 'I7566',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl63*complexconjugate(Rl63)',
                  texname = '\\text{I7566}')

I7633 = Parameter(name = 'I7633',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl36*complexconjugate(Rl36)',
                  texname = '\\text{I7633}')

I7636 = Parameter(name = 'I7636',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl66*complexconjugate(Rl36)',
                  texname = '\\text{I7636}')

I7644 = Parameter(name = 'I7644',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl44*complexconjugate(Rl44)',
                  texname = '\\text{I7644}')

I7655 = Parameter(name = 'I7655',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl55*complexconjugate(Rl55)',
                  texname = '\\text{I7655}')

I7663 = Parameter(name = 'I7663',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl36*complexconjugate(Rl66)',
                  texname = '\\text{I7663}')

I7666 = Parameter(name = 'I7666',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl66*complexconjugate(Rl66)',
                  texname = '\\text{I7666}')

I7733 = Parameter(name = 'I7733',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl36*complexconjugate(Rl36)',
                  texname = '\\text{I7733}')

I7736 = Parameter(name = 'I7736',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl66*complexconjugate(Rl36)',
                  texname = '\\text{I7736}')

I7744 = Parameter(name = 'I7744',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl44*complexconjugate(Rl44)',
                  texname = '\\text{I7744}')

I7755 = Parameter(name = 'I7755',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl55*complexconjugate(Rl55)',
                  texname = '\\text{I7755}')

I7763 = Parameter(name = 'I7763',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl36*complexconjugate(Rl66)',
                  texname = '\\text{I7763}')

I7766 = Parameter(name = 'I7766',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl66*complexconjugate(Rl66)',
                  texname = '\\text{I7766}')

I7833 = Parameter(name = 'I7833',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl36*complexconjugate(Rl36)',
                  texname = '\\text{I7833}')

I7836 = Parameter(name = 'I7836',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl66*complexconjugate(Rl36)',
                  texname = '\\text{I7836}')

I7844 = Parameter(name = 'I7844',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl44*complexconjugate(Rl44)',
                  texname = '\\text{I7844}')

I7855 = Parameter(name = 'I7855',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl55*complexconjugate(Rl55)',
                  texname = '\\text{I7855}')

I7863 = Parameter(name = 'I7863',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl36*complexconjugate(Rl66)',
                  texname = '\\text{I7863}')

I7866 = Parameter(name = 'I7866',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl66*complexconjugate(Rl66)',
                  texname = '\\text{I7866}')

I7933 = Parameter(name = 'I7933',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl36*complexconjugate(Rl36)',
                  texname = '\\text{I7933}')

I7936 = Parameter(name = 'I7936',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl66*complexconjugate(Rl36)',
                  texname = '\\text{I7936}')

I7944 = Parameter(name = 'I7944',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl44*complexconjugate(Rl44)',
                  texname = '\\text{I7944}')

I7955 = Parameter(name = 'I7955',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl55*complexconjugate(Rl55)',
                  texname = '\\text{I7955}')

I7963 = Parameter(name = 'I7963',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl36*complexconjugate(Rl66)',
                  texname = '\\text{I7963}')

I7966 = Parameter(name = 'I7966',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl66*complexconjugate(Rl66)',
                  texname = '\\text{I7966}')

I833 = Parameter(name = 'I833',
                 nature = 'internal',
                 type = 'complex',
                 value = 'Rd33*complexconjugate(CKM33)*complexconjugate(yu33)',
                 texname = '\\text{I833}')

I836 = Parameter(name = 'I836',
                 nature = 'internal',
                 type = 'complex',
                 value = 'Rd63*complexconjugate(CKM33)*complexconjugate(yu33)',
                 texname = '\\text{I836}')

I8033 = Parameter(name = 'I8033',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl36*complexconjugate(Rl36)',
                  texname = '\\text{I8033}')

I8036 = Parameter(name = 'I8036',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl66*complexconjugate(Rl36)',
                  texname = '\\text{I8036}')

I8044 = Parameter(name = 'I8044',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl44*complexconjugate(Rl44)',
                  texname = '\\text{I8044}')

I8055 = Parameter(name = 'I8055',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl55*complexconjugate(Rl55)',
                  texname = '\\text{I8055}')

I8063 = Parameter(name = 'I8063',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl36*complexconjugate(Rl66)',
                  texname = '\\text{I8063}')

I8066 = Parameter(name = 'I8066',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl66*complexconjugate(Rl66)',
                  texname = '\\text{I8066}')

I8133 = Parameter(name = 'I8133',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl36*complexconjugate(Rl36)',
                  texname = '\\text{I8133}')

I8136 = Parameter(name = 'I8136',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl66*complexconjugate(Rl36)',
                  texname = '\\text{I8136}')

I8144 = Parameter(name = 'I8144',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl44*complexconjugate(Rl44)',
                  texname = '\\text{I8144}')

I8155 = Parameter(name = 'I8155',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl55*complexconjugate(Rl55)',
                  texname = '\\text{I8155}')

I8163 = Parameter(name = 'I8163',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl36*complexconjugate(Rl66)',
                  texname = '\\text{I8163}')

I8166 = Parameter(name = 'I8166',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl66*complexconjugate(Rl66)',
                  texname = '\\text{I8166}')

I8233 = Parameter(name = 'I8233',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl33*complexconjugate(Rl36)*complexconjugate(ye33)',
                  texname = '\\text{I8233}')

I8236 = Parameter(name = 'I8236',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl63*complexconjugate(Rl36)*complexconjugate(ye33)',
                  texname = '\\text{I8236}')

I8263 = Parameter(name = 'I8263',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl33*complexconjugate(Rl66)*complexconjugate(ye33)',
                  texname = '\\text{I8263}')

I8266 = Parameter(name = 'I8266',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl63*complexconjugate(Rl66)*complexconjugate(ye33)',
                  texname = '\\text{I8266}')

I8333 = Parameter(name = 'I8333',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl36*ye33*complexconjugate(Rl33)',
                  texname = '\\text{I8333}')

I8336 = Parameter(name = 'I8336',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl66*ye33*complexconjugate(Rl33)',
                  texname = '\\text{I8336}')

I8363 = Parameter(name = 'I8363',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl36*ye33*complexconjugate(Rl63)',
                  texname = '\\text{I8363}')

I8366 = Parameter(name = 'I8366',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl66*ye33*complexconjugate(Rl63)',
                  texname = '\\text{I8366}')

I8433 = Parameter(name = 'I8433',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl33*complexconjugate(Rl36)*complexconjugate(ye33)',
                  texname = '\\text{I8433}')

I8436 = Parameter(name = 'I8436',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl63*complexconjugate(Rl36)*complexconjugate(ye33)',
                  texname = '\\text{I8436}')

I8463 = Parameter(name = 'I8463',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl33*complexconjugate(Rl66)*complexconjugate(ye33)',
                  texname = '\\text{I8463}')

I8466 = Parameter(name = 'I8466',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl63*complexconjugate(Rl66)*complexconjugate(ye33)',
                  texname = '\\text{I8466}')

I8533 = Parameter(name = 'I8533',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl36*ye33*complexconjugate(Rl33)',
                  texname = '\\text{I8533}')

I8536 = Parameter(name = 'I8536',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl66*ye33*complexconjugate(Rl33)',
                  texname = '\\text{I8536}')

I8563 = Parameter(name = 'I8563',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl36*ye33*complexconjugate(Rl63)',
                  texname = '\\text{I8563}')

I8566 = Parameter(name = 'I8566',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl66*ye33*complexconjugate(Rl63)',
                  texname = '\\text{I8566}')

I8633 = Parameter(name = 'I8633',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl33*complexconjugate(Rl36)*complexconjugate(ye33)',
                  texname = '\\text{I8633}')

I8636 = Parameter(name = 'I8636',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl63*complexconjugate(Rl36)*complexconjugate(ye33)',
                  texname = '\\text{I8636}')

I8663 = Parameter(name = 'I8663',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl33*complexconjugate(Rl66)*complexconjugate(ye33)',
                  texname = '\\text{I8663}')

I8666 = Parameter(name = 'I8666',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl63*complexconjugate(Rl66)*complexconjugate(ye33)',
                  texname = '\\text{I8666}')

I8733 = Parameter(name = 'I8733',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl36*ye33*complexconjugate(Rl33)',
                  texname = '\\text{I8733}')

I8736 = Parameter(name = 'I8736',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl66*ye33*complexconjugate(Rl33)',
                  texname = '\\text{I8736}')

I8763 = Parameter(name = 'I8763',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl36*ye33*complexconjugate(Rl63)',
                  texname = '\\text{I8763}')

I8766 = Parameter(name = 'I8766',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl66*ye33*complexconjugate(Rl63)',
                  texname = '\\text{I8766}')

I8833 = Parameter(name = 'I8833',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl33*complexconjugate(Rl36)*complexconjugate(ye33)',
                  texname = '\\text{I8833}')

I8836 = Parameter(name = 'I8836',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl63*complexconjugate(Rl36)*complexconjugate(ye33)',
                  texname = '\\text{I8836}')

I8863 = Parameter(name = 'I8863',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl33*complexconjugate(Rl66)*complexconjugate(ye33)',
                  texname = '\\text{I8863}')

I8866 = Parameter(name = 'I8866',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl63*complexconjugate(Rl66)*complexconjugate(ye33)',
                  texname = '\\text{I8866}')

I8933 = Parameter(name = 'I8933',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl36*ye33*complexconjugate(Rl33)',
                  texname = '\\text{I8933}')

I8936 = Parameter(name = 'I8936',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl66*ye33*complexconjugate(Rl33)',
                  texname = '\\text{I8936}')

I8963 = Parameter(name = 'I8963',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl36*ye33*complexconjugate(Rl63)',
                  texname = '\\text{I8963}')

I8966 = Parameter(name = 'I8966',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl66*ye33*complexconjugate(Rl63)',
                  texname = '\\text{I8966}')

I933 = Parameter(name = 'I933',
                 nature = 'internal',
                 type = 'complex',
                 value = 'Rd36*yd33*complexconjugate(CKM33)',
                 texname = '\\text{I933}')

I936 = Parameter(name = 'I936',
                 nature = 'internal',
                 type = 'complex',
                 value = 'Rd66*yd33*complexconjugate(CKM33)',
                 texname = '\\text{I936}')

I9011 = Parameter(name = 'I9011',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl11*complexconjugate(Rn11)',
                  texname = '\\text{I9011}')

I9022 = Parameter(name = 'I9022',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl22*complexconjugate(Rn22)',
                  texname = '\\text{I9022}')

I9033 = Parameter(name = 'I9033',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl33*complexconjugate(Rn33)',
                  texname = '\\text{I9033}')

I9036 = Parameter(name = 'I9036',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl63*complexconjugate(Rn33)',
                  texname = '\\text{I9036}')

I9133 = Parameter(name = 'I9133',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl36*te33*complexconjugate(Rn33)',
                  texname = '\\text{I9133}')

I9136 = Parameter(name = 'I9136',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl66*te33*complexconjugate(Rn33)',
                  texname = '\\text{I9136}')

I9233 = Parameter(name = 'I9233',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl33*ye33*complexconjugate(Rn33)*complexconjugate(ye33)',
                  texname = '\\text{I9233}')

I9236 = Parameter(name = 'I9236',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl63*ye33*complexconjugate(Rn33)*complexconjugate(ye33)',
                  texname = '\\text{I9236}')

I9333 = Parameter(name = 'I9333',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl36*ye33*complexconjugate(Rn33)',
                  texname = '\\text{I9333}')

I9336 = Parameter(name = 'I9336',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl66*ye33*complexconjugate(Rn33)',
                  texname = '\\text{I9336}')

I9411 = Parameter(name = 'I9411',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl11*complexconjugate(Rn11)',
                  texname = '\\text{I9411}')

I9422 = Parameter(name = 'I9422',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl22*complexconjugate(Rn22)',
                  texname = '\\text{I9422}')

I9433 = Parameter(name = 'I9433',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl33*complexconjugate(Rn33)',
                  texname = '\\text{I9433}')

I9436 = Parameter(name = 'I9436',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl63*complexconjugate(Rn33)',
                  texname = '\\text{I9436}')

I9533 = Parameter(name = 'I9533',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl33*ye33*complexconjugate(Rn33)*complexconjugate(ye33)',
                  texname = '\\text{I9533}')

I9536 = Parameter(name = 'I9536',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl63*ye33*complexconjugate(Rn33)*complexconjugate(ye33)',
                  texname = '\\text{I9536}')

I9611 = Parameter(name = 'I9611',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rn11',
                  texname = '\\text{I9611}')

I9622 = Parameter(name = 'I9622',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rn22',
                  texname = '\\text{I9622}')

I9633 = Parameter(name = 'I9633',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rn33',
                  texname = '\\text{I9633}')

I9733 = Parameter(name = 'I9733',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rn33*complexconjugate(ye33)',
                  texname = '\\text{I9733}')

I9811 = Parameter(name = 'I9811',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rn11*complexconjugate(Rl11)',
                  texname = '\\text{I9811}')

I9822 = Parameter(name = 'I9822',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rn22*complexconjugate(Rl22)',
                  texname = '\\text{I9822}')

I9833 = Parameter(name = 'I9833',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rn33*complexconjugate(Rl33)',
                  texname = '\\text{I9833}')

I9836 = Parameter(name = 'I9836',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rn33*complexconjugate(Rl63)',
                  texname = '\\text{I9836}')

I9933 = Parameter(name = 'I9933',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rn33*complexconjugate(Rl36)*complexconjugate(ye33)',
                  texname = '\\text{I9933}')

I9936 = Parameter(name = 'I9936',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rn33*complexconjugate(Rl66)*complexconjugate(ye33)',
                  texname = '\\text{I9936}')

