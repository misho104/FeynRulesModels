# This file was automatically created by FeynRules 1.6.18
# Mathematica version: 9.0 for Mac OS X x86 (64-bit) (January 28, 2013)
# Date: Wed 25 Sep 2013 05:34:07



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
                  value = 0.707106781,
                  texname = '\\text{RRd11}',
                  lhablock = 'DSQMIX',
                  lhacode = [ 1, 1 ])

RRd14 = Parameter(name = 'RRd14',
                  nature = 'external',
                  type = 'real',
                  value = 0.707106781,
                  texname = '\\text{RRd14}',
                  lhablock = 'DSQMIX',
                  lhacode = [ 1, 4 ])

RRd22 = Parameter(name = 'RRd22',
                  nature = 'external',
                  type = 'real',
                  value = 0.707106781,
                  texname = '\\text{RRd22}',
                  lhablock = 'DSQMIX',
                  lhacode = [ 2, 2 ])

RRd25 = Parameter(name = 'RRd25',
                  nature = 'external',
                  type = 'real',
                  value = 0.707106781,
                  texname = '\\text{RRd25}',
                  lhablock = 'DSQMIX',
                  lhacode = [ 2, 5 ])

RRd33 = Parameter(name = 'RRd33',
                  nature = 'external',
                  type = 'real',
                  value = 0.707106781,
                  texname = '\\text{RRd33}',
                  lhablock = 'DSQMIX',
                  lhacode = [ 3, 3 ])

RRd36 = Parameter(name = 'RRd36',
                  nature = 'external',
                  type = 'real',
                  value = 0.707106781,
                  texname = '\\text{RRd36}',
                  lhablock = 'DSQMIX',
                  lhacode = [ 3, 6 ])

RRd41 = Parameter(name = 'RRd41',
                  nature = 'external',
                  type = 'real',
                  value = -0.707106781,
                  texname = '\\text{RRd41}',
                  lhablock = 'DSQMIX',
                  lhacode = [ 4, 1 ])

RRd44 = Parameter(name = 'RRd44',
                  nature = 'external',
                  type = 'real',
                  value = 0.707106781,
                  texname = '\\text{RRd44}',
                  lhablock = 'DSQMIX',
                  lhacode = [ 4, 4 ])

RRd52 = Parameter(name = 'RRd52',
                  nature = 'external',
                  type = 'real',
                  value = -0.707106781,
                  texname = '\\text{RRd52}',
                  lhablock = 'DSQMIX',
                  lhacode = [ 5, 2 ])

RRd55 = Parameter(name = 'RRd55',
                  nature = 'external',
                  type = 'real',
                  value = 0.707106781,
                  texname = '\\text{RRd55}',
                  lhablock = 'DSQMIX',
                  lhacode = [ 5, 5 ])

RRd63 = Parameter(name = 'RRd63',
                  nature = 'external',
                  type = 'real',
                  value = -0.707106781,
                  texname = '\\text{RRd63}',
                  lhablock = 'DSQMIX',
                  lhacode = [ 6, 3 ])

RRd66 = Parameter(name = 'RRd66',
                  nature = 'external',
                  type = 'real',
                  value = 0.707106781,
                  texname = '\\text{RRd66}',
                  lhablock = 'DSQMIX',
                  lhacode = [ 6, 6 ])

alp = Parameter(name = 'alp',
                nature = 'external',
                type = 'real',
                value = -0.11382521,
                texname = '\\alpha',
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
                texname = '\\text{Subsuperscript}[m,A,2]',
                lhablock = 'HMIX',
                lhacode = [ 4 ])

RmD211 = Parameter(name = 'RmD211',
                   nature = 'external',
                   type = 'real',
                   value = 276684.674,
                   texname = '\\text{RmD211}',
                   lhablock = 'MSD2',
                   lhacode = [ 1, 1 ])

RmD222 = Parameter(name = 'RmD222',
                   nature = 'external',
                   type = 'real',
                   value = 275684.674,
                   texname = '\\text{RmD222}',
                   lhablock = 'MSD2',
                   lhacode = [ 2, 2 ])

RmD233 = Parameter(name = 'RmD233',
                   nature = 'external',
                   type = 'real',
                   value = 274261.969,
                   texname = '\\text{RmD233}',
                   lhablock = 'MSD2',
                   lhacode = [ 3, 3 ])

RmE211 = Parameter(name = 'RmE211',
                   nature = 'external',
                   type = 'real',
                   value = 18930.6287,
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
                   value = 38455.67,
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

mHd2 = Parameter(name = 'mHd2',
                 nature = 'external',
                 type = 'real',
                 value = 32337.4943,
                 texname = '\\text{Subsuperscript}\\left[m,H_d,2\\right]',
                 lhablock = 'MSOFT',
                 lhacode = [ 21 ])

mHu2 = Parameter(name = 'mHu2',
                 nature = 'external',
                 type = 'real',
                 value = -128800.134,
                 texname = '\\text{Subsuperscript}\\left[m,H_u,2\\right]',
                 lhablock = 'MSOFT',
                 lhacode = [ 22 ])

RmQ211 = Parameter(name = 'RmQ211',
                   nature = 'external',
                   type = 'real',
                   value = 309836.701,
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
                   value = 290382.106,
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
                  value = 0.707106781,
                  texname = '\\text{RRl11}',
                  lhablock = 'SELMIX',
                  lhacode = [ 1, 1 ])

RRl14 = Parameter(name = 'RRl14',
                  nature = 'external',
                  type = 'real',
                  value = 0.707106781,
                  texname = '\\text{RRl14}',
                  lhablock = 'SELMIX',
                  lhacode = [ 1, 4 ])

RRl22 = Parameter(name = 'RRl22',
                  nature = 'external',
                  type = 'real',
                  value = 0.707106781,
                  texname = '\\text{RRl22}',
                  lhablock = 'SELMIX',
                  lhacode = [ 2, 2 ])

RRl25 = Parameter(name = 'RRl25',
                  nature = 'external',
                  type = 'real',
                  value = 0.707106781,
                  texname = '\\text{RRl25}',
                  lhablock = 'SELMIX',
                  lhacode = [ 2, 5 ])

RRl33 = Parameter(name = 'RRl33',
                  nature = 'external',
                  type = 'real',
                  value = 0.707106781,
                  texname = '\\text{RRl33}',
                  lhablock = 'SELMIX',
                  lhacode = [ 3, 3 ])

RRl36 = Parameter(name = 'RRl36',
                  nature = 'external',
                  type = 'real',
                  value = 0.707106781,
                  texname = '\\text{RRl36}',
                  lhablock = 'SELMIX',
                  lhacode = [ 3, 6 ])

RRl41 = Parameter(name = 'RRl41',
                  nature = 'external',
                  type = 'real',
                  value = -0.707106781,
                  texname = '\\text{RRl41}',
                  lhablock = 'SELMIX',
                  lhacode = [ 4, 1 ])

RRl44 = Parameter(name = 'RRl44',
                  nature = 'external',
                  type = 'real',
                  value = 0.707106781,
                  texname = '\\text{RRl44}',
                  lhablock = 'SELMIX',
                  lhacode = [ 4, 4 ])

RRl52 = Parameter(name = 'RRl52',
                  nature = 'external',
                  type = 'real',
                  value = -0.707106781,
                  texname = '\\text{RRl52}',
                  lhablock = 'SELMIX',
                  lhacode = [ 5, 2 ])

RRl55 = Parameter(name = 'RRl55',
                  nature = 'external',
                  type = 'real',
                  value = 0.707106781,
                  texname = '\\text{RRl55}',
                  lhablock = 'SELMIX',
                  lhacode = [ 5, 5 ])

RRl63 = Parameter(name = 'RRl63',
                  nature = 'external',
                  type = 'real',
                  value = -0.707106781,
                  texname = '\\text{RRl63}',
                  lhablock = 'SELMIX',
                  lhacode = [ 6, 3 ])

RRl66 = Parameter(name = 'RRl66',
                  nature = 'external',
                  type = 'real',
                  value = 0.707106781,
                  texname = '\\text{RRl66}',
                  lhablock = 'SELMIX',
                  lhacode = [ 6, 6 ])

aEWM1 = Parameter(name = 'aEWM1',
                  nature = 'external',
                  type = 'real',
                  value = 127.934,
                  texname = '\\text{Subsuperscript}[\\alpha ,w,-1]',
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

Rtd11 = Parameter(name = 'Rtd11',
                  nature = 'external',
                  type = 'real',
                  value = -108.693742,
                  texname = '\\text{Rtd11}',
                  lhablock = 'TD',
                  lhacode = [ 1, 1 ])

Rtd22 = Parameter(name = 'Rtd22',
                  nature = 'external',
                  type = 'real',
                  value = -109.693742,
                  texname = '\\text{Rtd22}',
                  lhablock = 'TD',
                  lhacode = [ 2, 2 ])

Rtd33 = Parameter(name = 'Rtd33',
                  nature = 'external',
                  type = 'real',
                  value = -110.693742,
                  texname = '\\text{Rtd33}',
                  lhablock = 'TD',
                  lhacode = [ 3, 3 ])

Rte11 = Parameter(name = 'Rte11',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = '\\text{Rte11}',
                  lhablock = 'TE',
                  lhacode = [ 1, 1 ])

Rte22 = Parameter(name = 'Rte22',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = '\\text{Rte22}',
                  lhablock = 'TE',
                  lhacode = [ 2, 2 ])

Rte33 = Parameter(name = 'Rte33',
                  nature = 'external',
                  type = 'real',
                  value = -25.4019727,
                  texname = '\\text{Rte33}',
                  lhablock = 'TE',
                  lhacode = [ 3, 3 ])

Rtu11 = Parameter(name = 'Rtu11',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = '\\text{Rtu11}',
                  lhablock = 'TU',
                  lhacode = [ 1, 1 ])

Rtu22 = Parameter(name = 'Rtu22',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = '\\text{Rtu22}',
                  lhablock = 'TU',
                  lhacode = [ 2, 2 ])

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
                  value = 0.707106781,
                  texname = '\\text{RRu11}',
                  lhablock = 'USQMIX',
                  lhacode = [ 1, 1 ])

RRu14 = Parameter(name = 'RRu14',
                  nature = 'external',
                  type = 'real',
                  value = 0.707106781,
                  texname = '\\text{RRu14}',
                  lhablock = 'USQMIX',
                  lhacode = [ 1, 4 ])

RRu22 = Parameter(name = 'RRu22',
                  nature = 'external',
                  type = 'real',
                  value = 0.707106781,
                  texname = '\\text{RRu22}',
                  lhablock = 'USQMIX',
                  lhacode = [ 2, 2 ])

RRu25 = Parameter(name = 'RRu25',
                  nature = 'external',
                  type = 'real',
                  value = 0.707106781,
                  texname = '\\text{RRu25}',
                  lhablock = 'USQMIX',
                  lhacode = [ 2, 5 ])

RRu33 = Parameter(name = 'RRu33',
                  nature = 'external',
                  type = 'real',
                  value = 0.707106781,
                  texname = '\\text{RRu33}',
                  lhablock = 'USQMIX',
                  lhacode = [ 3, 3 ])

RRu36 = Parameter(name = 'RRu36',
                  nature = 'external',
                  type = 'real',
                  value = 0.707106781,
                  texname = '\\text{RRu36}',
                  lhablock = 'USQMIX',
                  lhacode = [ 3, 6 ])

RRu41 = Parameter(name = 'RRu41',
                  nature = 'external',
                  type = 'real',
                  value = -0.707106781,
                  texname = '\\text{RRu41}',
                  lhablock = 'USQMIX',
                  lhacode = [ 4, 1 ])

RRu44 = Parameter(name = 'RRu44',
                  nature = 'external',
                  type = 'real',
                  value = 0.707106781,
                  texname = '\\text{RRu44}',
                  lhablock = 'USQMIX',
                  lhacode = [ 4, 4 ])

RRu52 = Parameter(name = 'RRu52',
                  nature = 'external',
                  type = 'real',
                  value = -0.707106781,
                  texname = '\\text{RRu52}',
                  lhablock = 'USQMIX',
                  lhacode = [ 5, 2 ])

RRu55 = Parameter(name = 'RRu55',
                  nature = 'external',
                  type = 'real',
                  value = 0.707106781,
                  texname = '\\text{RRu55}',
                  lhablock = 'USQMIX',
                  lhacode = [ 5, 5 ])

RRu63 = Parameter(name = 'RRu63',
                  nature = 'external',
                  type = 'real',
                  value = -0.707106781,
                  texname = '\\text{RRu63}',
                  lhablock = 'USQMIX',
                  lhacode = [ 6, 3 ])

RRu66 = Parameter(name = 'RRu66',
                  nature = 'external',
                  type = 'real',
                  value = 0.707106781,
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

Ryd11 = Parameter(name = 'Ryd11',
                  nature = 'external',
                  type = 'real',
                  value = 0.00001,
                  texname = '\\text{Ryd11}',
                  lhablock = 'YD',
                  lhacode = [ 1, 1 ])

Ryd22 = Parameter(name = 'Ryd22',
                  nature = 'external',
                  type = 'real',
                  value = 0.001,
                  texname = '\\text{Ryd22}',
                  lhablock = 'YD',
                  lhacode = [ 2, 2 ])

Ryd33 = Parameter(name = 'Ryd33',
                  nature = 'external',
                  type = 'real',
                  value = 0.138840206,
                  texname = '\\text{Ryd33}',
                  lhablock = 'YD',
                  lhacode = [ 3, 3 ])

Rye11 = Parameter(name = 'Rye11',
                  nature = 'external',
                  type = 'real',
                  value = 0.00001,
                  texname = '\\text{Rye11}',
                  lhablock = 'YE',
                  lhacode = [ 1, 1 ])

Rye22 = Parameter(name = 'Rye22',
                  nature = 'external',
                  type = 'real',
                  value = 0.001,
                  texname = '\\text{Rye22}',
                  lhablock = 'YE',
                  lhacode = [ 2, 2 ])

Rye33 = Parameter(name = 'Rye33',
                  nature = 'external',
                  type = 'real',
                  value = 0.10089081,
                  texname = '\\text{Rye33}',
                  lhablock = 'YE',
                  lhacode = [ 3, 3 ])

Ryu11 = Parameter(name = 'Ryu11',
                  nature = 'external',
                  type = 'real',
                  value = 0.00001,
                  texname = '\\text{Ryu11}',
                  lhablock = 'YU',
                  lhacode = [ 1, 1 ])

Ryu22 = Parameter(name = 'Ryu22',
                  nature = 'external',
                  type = 'real',
                  value = 0.001,
                  texname = '\\text{Ryu22}',
                  lhablock = 'YU',
                  lhacode = [ 2, 2 ])

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

Me = Parameter(name = 'Me',
               nature = 'external',
               type = 'real',
               value = 0.0001,
               texname = '\\text{Me}',
               lhablock = 'MASS',
               lhacode = [ 11 ])

Mm = Parameter(name = 'Mm',
               nature = 'external',
               type = 'real',
               value = 0.1,
               texname = '\\text{Mm}',
               lhablock = 'MASS',
               lhacode = [ 13 ])

Mta = Parameter(name = 'Mta',
                nature = 'external',
                type = 'real',
                value = 1.777,
                texname = '\\text{Mta}',
                lhablock = 'MASS',
                lhacode = [ 15 ])

MU = Parameter(name = 'MU',
               nature = 'external',
               type = 'real',
               value = 0.001,
               texname = 'M',
               lhablock = 'MASS',
               lhacode = [ 2 ])

MC = Parameter(name = 'MC',
               nature = 'external',
               type = 'real',
               value = 1.,
               texname = '\\text{MC}',
               lhablock = 'MASS',
               lhacode = [ 4 ])

MT = Parameter(name = 'MT',
               nature = 'external',
               type = 'real',
               value = 175.,
               texname = '\\text{MT}',
               lhablock = 'MASS',
               lhacode = [ 6 ])

MD = Parameter(name = 'MD',
               nature = 'external',
               type = 'real',
               value = 0.001,
               texname = '\\text{MD}',
               lhablock = 'MASS',
               lhacode = [ 1 ])

MS = Parameter(name = 'MS',
               nature = 'external',
               type = 'real',
               value = 0.1,
               texname = '\\text{MS}',
               lhablock = 'MASS',
               lhacode = [ 3 ])

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
                 value = 182.258326,
                 texname = '\\text{Msn1}',
                 lhablock = 'MASS',
                 lhacode = [ 1000012 ])

Msn2 = Parameter(name = 'Msn2',
                 nature = 'external',
                 type = 'real',
                 value = 184.258326,
                 texname = '\\text{Msn2}',
                 lhablock = 'MASS',
                 lhacode = [ 1000014 ])

Msn3 = Parameter(name = 'Msn3',
                 nature = 'external',
                 type = 'real',
                 value = 186.708464,
                 texname = '\\text{Msn3}',
                 lhablock = 'MASS',
                 lhacode = [ 1000016 ])

Msl1 = Parameter(name = 'Msl1',
                 nature = 'external',
                 type = 'real',
                 value = 201.91569,
                 texname = '\\text{Msl1}',
                 lhablock = 'MASS',
                 lhacode = [ 1000011 ])

Msl2 = Parameter(name = 'Msl2',
                 nature = 'external',
                 type = 'real',
                 value = 203.91569,
                 texname = '\\text{Msl2}',
                 lhablock = 'MASS',
                 lhacode = [ 1000013 ])

Msl3 = Parameter(name = 'Msl3',
                 nature = 'external',
                 type = 'real',
                 value = 135.490864,
                 texname = '\\text{Msl3}',
                 lhablock = 'MASS',
                 lhacode = [ 1000015 ])

Msl4 = Parameter(name = 'Msl4',
                 nature = 'external',
                 type = 'real',
                 value = 141.102799,
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
                 value = 562.119014,
                 texname = '\\text{Msu1}',
                 lhablock = 'MASS',
                 lhacode = [ 1000002 ])

Msu2 = Parameter(name = 'Msu2',
                 nature = 'external',
                 type = 'real',
                 value = 564.119014,
                 texname = '\\text{Msu2}',
                 lhablock = 'MASS',
                 lhacode = [ 1000004 ])

Msu3 = Parameter(name = 'Msu3',
                 nature = 'external',
                 type = 'real',
                 value = 396.668493,
                 texname = '\\text{Msu3}',
                 lhablock = 'MASS',
                 lhacode = [ 1000006 ])

Msu4 = Parameter(name = 'Msu4',
                 nature = 'external',
                 type = 'real',
                 value = 542.259265,
                 texname = '\\text{Msu4}',
                 lhablock = 'MASS',
                 lhacode = [ 2000002 ])

Msu5 = Parameter(name = 'Msu5',
                 nature = 'external',
                 type = 'real',
                 value = 544.259265,
                 texname = '\\text{Msu5}',
                 lhablock = 'MASS',
                 lhacode = [ 2000004 ])

Msu6 = Parameter(name = 'Msu6',
                 nature = 'external',
                 type = 'real',
                 value = 586.785818,
                 texname = '\\text{Msu6}',
                 lhablock = 'MASS',
                 lhacode = [ 2000006 ])

Msd1 = Parameter(name = 'Msd1',
                 nature = 'external',
                 type = 'real',
                 value = 561.441109,
                 texname = '\\text{Msd1}',
                 lhablock = 'MASS',
                 lhacode = [ 1000001 ])

Msd2 = Parameter(name = 'Msd2',
                 nature = 'external',
                 type = 'real',
                 value = 563.441109,
                 texname = '\\text{Msd2}',
                 lhablock = 'MASS',
                 lhacode = [ 1000003 ])

Msd3 = Parameter(name = 'Msd3',
                 nature = 'external',
                 type = 'real',
                 value = 515.065179,
                 texname = '\\text{Msd3}',
                 lhablock = 'MASS',
                 lhacode = [ 1000005 ])

Msd4 = Parameter(name = 'Msd4',
                 nature = 'external',
                 type = 'real',
                 value = 541.228462,
                 texname = '\\text{Msd4}',
                 lhablock = 'MASS',
                 lhacode = [ 2000001 ])

Msd5 = Parameter(name = 'Msd5',
                 nature = 'external',
                 type = 'real',
                 value = 543.228462,
                 texname = '\\text{Msd5}',
                 lhablock = 'MASS',
                 lhacode = [ 2000003 ])

Msd6 = Parameter(name = 'Msd6',
                 nature = 'external',
                 type = 'real',
                 value = 545.726676,
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

Wneu1 = Parameter(name = 'Wneu1',
                  nature = 'external',
                  type = 'real',
                  value = 0.14,
                  texname = '\\text{Wneu1}',
                  lhablock = 'DECAY',
                  lhacode = [ 1000022 ])

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
                 texname = '\\beta')

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
                texname = '\\mu')

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

Rd14 = Parameter(name = 'Rd14',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RRd14',
                 texname = '\\text{Rd14}')

Rd22 = Parameter(name = 'Rd22',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RRd22',
                 texname = '\\text{Rd22}')

Rd25 = Parameter(name = 'Rd25',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RRd25',
                 texname = '\\text{Rd25}')

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

Rd41 = Parameter(name = 'Rd41',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RRd41',
                 texname = '\\text{Rd41}')

Rd44 = Parameter(name = 'Rd44',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RRd44',
                 texname = '\\text{Rd44}')

Rd52 = Parameter(name = 'Rd52',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RRd52',
                 texname = '\\text{Rd52}')

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

Rl14 = Parameter(name = 'Rl14',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RRl14',
                 texname = '\\text{Rl14}')

Rl22 = Parameter(name = 'Rl22',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RRl22',
                 texname = '\\text{Rl22}')

Rl25 = Parameter(name = 'Rl25',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RRl25',
                 texname = '\\text{Rl25}')

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

Rl41 = Parameter(name = 'Rl41',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RRl41',
                 texname = '\\text{Rl41}')

Rl44 = Parameter(name = 'Rl44',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RRl44',
                 texname = '\\text{Rl44}')

Rl52 = Parameter(name = 'Rl52',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RRl52',
                 texname = '\\text{Rl52}')

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

Ru14 = Parameter(name = 'Ru14',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RRu14',
                 texname = '\\text{Ru14}')

Ru22 = Parameter(name = 'Ru22',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RRu22',
                 texname = '\\text{Ru22}')

Ru25 = Parameter(name = 'Ru25',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RRu25',
                 texname = '\\text{Ru25}')

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

Ru41 = Parameter(name = 'Ru41',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RRu41',
                 texname = '\\text{Ru41}')

Ru44 = Parameter(name = 'Ru44',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RRu44',
                 texname = '\\text{Ru44}')

Ru52 = Parameter(name = 'Ru52',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RRu52',
                 texname = '\\text{Ru52}')

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

td11 = Parameter(name = 'td11',
                 nature = 'internal',
                 type = 'complex',
                 value = 'Rtd11',
                 texname = '\\text{td11}')

td22 = Parameter(name = 'td22',
                 nature = 'internal',
                 type = 'complex',
                 value = 'Rtd22',
                 texname = '\\text{td22}')

td33 = Parameter(name = 'td33',
                 nature = 'internal',
                 type = 'complex',
                 value = 'Rtd33',
                 texname = '\\text{td33}')

te11 = Parameter(name = 'te11',
                 nature = 'internal',
                 type = 'complex',
                 value = 'Rte11',
                 texname = '\\text{te11}')

te22 = Parameter(name = 'te22',
                 nature = 'internal',
                 type = 'complex',
                 value = 'Rte22',
                 texname = '\\text{te22}')

te33 = Parameter(name = 'te33',
                 nature = 'internal',
                 type = 'complex',
                 value = 'Rte33',
                 texname = '\\text{te33}')

tu11 = Parameter(name = 'tu11',
                 nature = 'internal',
                 type = 'complex',
                 value = 'Rtu11',
                 texname = '\\text{tu11}')

tu22 = Parameter(name = 'tu22',
                 nature = 'internal',
                 type = 'complex',
                 value = 'Rtu22',
                 texname = '\\text{tu22}')

tu33 = Parameter(name = 'tu33',
                 nature = 'internal',
                 type = 'complex',
                 value = 'Rtu33',
                 texname = '\\text{tu33}')

yd11 = Parameter(name = 'yd11',
                 nature = 'internal',
                 type = 'complex',
                 value = 'Ryd11',
                 texname = '\\text{yd11}')

yd22 = Parameter(name = 'yd22',
                 nature = 'internal',
                 type = 'complex',
                 value = 'Ryd22',
                 texname = '\\text{yd22}')

yd33 = Parameter(name = 'yd33',
                 nature = 'internal',
                 type = 'complex',
                 value = 'Ryd33',
                 texname = '\\text{yd33}')

ye11 = Parameter(name = 'ye11',
                 nature = 'internal',
                 type = 'complex',
                 value = 'Rye11',
                 texname = '\\text{ye11}')

ye22 = Parameter(name = 'ye22',
                 nature = 'internal',
                 type = 'complex',
                 value = 'Rye22',
                 texname = '\\text{ye22}')

ye33 = Parameter(name = 'ye33',
                 nature = 'internal',
                 type = 'complex',
                 value = 'Rye33',
                 texname = '\\text{ye33}')

yu11 = Parameter(name = 'yu11',
                 nature = 'internal',
                 type = 'complex',
                 value = 'Ryu11',
                 texname = '\\text{yu11}')

yu22 = Parameter(name = 'yu22',
                 nature = 'internal',
                 type = 'complex',
                 value = 'Ryu22',
                 texname = '\\text{yu22}')

yu33 = Parameter(name = 'yu33',
                 nature = 'internal',
                 type = 'complex',
                 value = 'Ryu33',
                 texname = '\\text{yu33}')

bb = Parameter(name = 'bb',
               nature = 'internal',
               type = 'complex',
               value = '((-mHd2 + mHu2)*cmath.tan(2*alp))/2. - MZ**2*(cmath.sin(2*beta)/2. + cmath.cos(2*beta)*cmath.tan(2*alp))',
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

I1x11 = Parameter(name = 'I1x11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'complexconjugate(CKM11)*complexconjugate(yu11)',
                  texname = '\\text{I1x11}')

I1x22 = Parameter(name = 'I1x22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'complexconjugate(CKM22)*complexconjugate(yu22)',
                  texname = '\\text{I1x22}')

I1x33 = Parameter(name = 'I1x33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'complexconjugate(CKM33)*complexconjugate(yu33)',
                  texname = '\\text{I1x33}')

I10x11 = Parameter(name = 'I10x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd11*complexconjugate(CKM11)',
                   texname = '\\text{I10x11}')

I10x14 = Parameter(name = 'I10x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd41*complexconjugate(CKM11)',
                   texname = '\\text{I10x14}')

I10x22 = Parameter(name = 'I10x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd22*complexconjugate(CKM22)',
                   texname = '\\text{I10x22}')

I10x25 = Parameter(name = 'I10x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd52*complexconjugate(CKM22)',
                   texname = '\\text{I10x25}')

I10x33 = Parameter(name = 'I10x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd33*complexconjugate(CKM33)',
                   texname = '\\text{I10x33}')

I10x36 = Parameter(name = 'I10x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd63*complexconjugate(CKM33)',
                   texname = '\\text{I10x36}')

I100x11 = Parameter(name = 'I100x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn11*complexconjugate(Rl14)*complexconjugate(ye11)',
                    texname = '\\text{I100x11}')

I100x14 = Parameter(name = 'I100x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn11*complexconjugate(Rl44)*complexconjugate(ye11)',
                    texname = '\\text{I100x14}')

I100x22 = Parameter(name = 'I100x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn22*complexconjugate(Rl25)*complexconjugate(ye22)',
                    texname = '\\text{I100x22}')

I100x25 = Parameter(name = 'I100x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn22*complexconjugate(Rl55)*complexconjugate(ye22)',
                    texname = '\\text{I100x25}')

I100x33 = Parameter(name = 'I100x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn33*complexconjugate(Rl36)*complexconjugate(ye33)',
                    texname = '\\text{I100x33}')

I100x36 = Parameter(name = 'I100x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn33*complexconjugate(Rl66)*complexconjugate(ye33)',
                    texname = '\\text{I100x36}')

I101x11 = Parameter(name = 'I101x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn11*ye11*complexconjugate(Rl11)*complexconjugate(ye11)',
                    texname = '\\text{I101x11}')

I101x14 = Parameter(name = 'I101x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn11*ye11*complexconjugate(Rl41)*complexconjugate(ye11)',
                    texname = '\\text{I101x14}')

I101x22 = Parameter(name = 'I101x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn22*ye22*complexconjugate(Rl22)*complexconjugate(ye22)',
                    texname = '\\text{I101x22}')

I101x25 = Parameter(name = 'I101x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn22*ye22*complexconjugate(Rl52)*complexconjugate(ye22)',
                    texname = '\\text{I101x25}')

I101x33 = Parameter(name = 'I101x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn33*ye33*complexconjugate(Rl33)*complexconjugate(ye33)',
                    texname = '\\text{I101x33}')

I101x36 = Parameter(name = 'I101x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn33*ye33*complexconjugate(Rl63)*complexconjugate(ye33)',
                    texname = '\\text{I101x36}')

I102x11 = Parameter(name = 'I102x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn11*complexconjugate(Rl11)',
                    texname = '\\text{I102x11}')

I102x14 = Parameter(name = 'I102x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn11*complexconjugate(Rl41)',
                    texname = '\\text{I102x14}')

I102x22 = Parameter(name = 'I102x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn22*complexconjugate(Rl22)',
                    texname = '\\text{I102x22}')

I102x25 = Parameter(name = 'I102x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn22*complexconjugate(Rl52)',
                    texname = '\\text{I102x25}')

I102x33 = Parameter(name = 'I102x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn33*complexconjugate(Rl33)',
                    texname = '\\text{I102x33}')

I102x36 = Parameter(name = 'I102x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn33*complexconjugate(Rl63)',
                    texname = '\\text{I102x36}')

I103x11 = Parameter(name = 'I103x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn11*ye11*complexconjugate(Rl11)*complexconjugate(ye11)',
                    texname = '\\text{I103x11}')

I103x14 = Parameter(name = 'I103x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn11*ye11*complexconjugate(Rl41)*complexconjugate(ye11)',
                    texname = '\\text{I103x14}')

I103x22 = Parameter(name = 'I103x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn22*ye22*complexconjugate(Rl22)*complexconjugate(ye22)',
                    texname = '\\text{I103x22}')

I103x25 = Parameter(name = 'I103x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn22*ye22*complexconjugate(Rl52)*complexconjugate(ye22)',
                    texname = '\\text{I103x25}')

I103x33 = Parameter(name = 'I103x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn33*ye33*complexconjugate(Rl33)*complexconjugate(ye33)',
                    texname = '\\text{I103x33}')

I103x36 = Parameter(name = 'I103x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn33*ye33*complexconjugate(Rl63)*complexconjugate(ye33)',
                    texname = '\\text{I103x36}')

I104x11 = Parameter(name = 'I104x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn11*ye11*complexconjugate(Rn11)*complexconjugate(ye11)',
                    texname = '\\text{I104x11}')

I104x22 = Parameter(name = 'I104x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn22*ye22*complexconjugate(Rn22)*complexconjugate(ye22)',
                    texname = '\\text{I104x22}')

I104x33 = Parameter(name = 'I104x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn33*ye33*complexconjugate(Rn33)*complexconjugate(ye33)',
                    texname = '\\text{I104x33}')

I105x11 = Parameter(name = 'I105x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl11*complexconjugate(Rl11)',
                    texname = '\\text{I105x11}')

I105x14 = Parameter(name = 'I105x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl41*complexconjugate(Rl11)',
                    texname = '\\text{I105x14}')

I105x22 = Parameter(name = 'I105x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl22*complexconjugate(Rl22)',
                    texname = '\\text{I105x22}')

I105x25 = Parameter(name = 'I105x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl52*complexconjugate(Rl22)',
                    texname = '\\text{I105x25}')

I105x33 = Parameter(name = 'I105x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl33*complexconjugate(Rl33)',
                    texname = '\\text{I105x33}')

I105x36 = Parameter(name = 'I105x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl63*complexconjugate(Rl33)',
                    texname = '\\text{I105x36}')

I105x41 = Parameter(name = 'I105x41',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl11*complexconjugate(Rl41)',
                    texname = '\\text{I105x41}')

I105x44 = Parameter(name = 'I105x44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl41*complexconjugate(Rl41)',
                    texname = '\\text{I105x44}')

I105x52 = Parameter(name = 'I105x52',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl22*complexconjugate(Rl52)',
                    texname = '\\text{I105x52}')

I105x55 = Parameter(name = 'I105x55',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl52*complexconjugate(Rl52)',
                    texname = '\\text{I105x55}')

I105x63 = Parameter(name = 'I105x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl33*complexconjugate(Rl63)',
                    texname = '\\text{I105x63}')

I105x66 = Parameter(name = 'I105x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl63*complexconjugate(Rl63)',
                    texname = '\\text{I105x66}')

I106x11 = Parameter(name = 'I106x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl14*complexconjugate(Rl14)',
                    texname = '\\text{I106x11}')

I106x14 = Parameter(name = 'I106x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl44*complexconjugate(Rl14)',
                    texname = '\\text{I106x14}')

I106x22 = Parameter(name = 'I106x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl25*complexconjugate(Rl25)',
                    texname = '\\text{I106x22}')

I106x25 = Parameter(name = 'I106x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl55*complexconjugate(Rl25)',
                    texname = '\\text{I106x25}')

I106x33 = Parameter(name = 'I106x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl36*complexconjugate(Rl36)',
                    texname = '\\text{I106x33}')

I106x36 = Parameter(name = 'I106x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl66*complexconjugate(Rl36)',
                    texname = '\\text{I106x36}')

I106x41 = Parameter(name = 'I106x41',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl14*complexconjugate(Rl44)',
                    texname = '\\text{I106x41}')

I106x44 = Parameter(name = 'I106x44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl44*complexconjugate(Rl44)',
                    texname = '\\text{I106x44}')

I106x52 = Parameter(name = 'I106x52',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl25*complexconjugate(Rl55)',
                    texname = '\\text{I106x52}')

I106x55 = Parameter(name = 'I106x55',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl55*complexconjugate(Rl55)',
                    texname = '\\text{I106x55}')

I106x63 = Parameter(name = 'I106x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl36*complexconjugate(Rl66)',
                    texname = '\\text{I106x63}')

I106x66 = Parameter(name = 'I106x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl66*complexconjugate(Rl66)',
                    texname = '\\text{I106x66}')

I107x11 = Parameter(name = 'I107x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl11*complexconjugate(Rn11)',
                    texname = '\\text{I107x11}')

I107x14 = Parameter(name = 'I107x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl41*complexconjugate(Rn11)',
                    texname = '\\text{I107x14}')

I107x22 = Parameter(name = 'I107x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl22*complexconjugate(Rn22)',
                    texname = '\\text{I107x22}')

I107x25 = Parameter(name = 'I107x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl52*complexconjugate(Rn22)',
                    texname = '\\text{I107x25}')

I107x33 = Parameter(name = 'I107x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl33*complexconjugate(Rn33)',
                    texname = '\\text{I107x33}')

I107x36 = Parameter(name = 'I107x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl63*complexconjugate(Rn33)',
                    texname = '\\text{I107x36}')

I108x11 = Parameter(name = 'I108x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn11*complexconjugate(Rl11)',
                    texname = '\\text{I108x11}')

I108x14 = Parameter(name = 'I108x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn11*complexconjugate(Rl41)',
                    texname = '\\text{I108x14}')

I108x22 = Parameter(name = 'I108x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn22*complexconjugate(Rl22)',
                    texname = '\\text{I108x22}')

I108x25 = Parameter(name = 'I108x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn22*complexconjugate(Rl52)',
                    texname = '\\text{I108x25}')

I108x33 = Parameter(name = 'I108x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn33*complexconjugate(Rl33)',
                    texname = '\\text{I108x33}')

I108x36 = Parameter(name = 'I108x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn33*complexconjugate(Rl63)',
                    texname = '\\text{I108x36}')

I109x11 = Parameter(name = 'I109x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn11*complexconjugate(Rl14)*complexconjugate(ye11)',
                    texname = '\\text{I109x11}')

I109x14 = Parameter(name = 'I109x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn11*complexconjugate(Rl44)*complexconjugate(ye11)',
                    texname = '\\text{I109x14}')

I109x22 = Parameter(name = 'I109x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn22*complexconjugate(Rl25)*complexconjugate(ye22)',
                    texname = '\\text{I109x22}')

I109x25 = Parameter(name = 'I109x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn22*complexconjugate(Rl55)*complexconjugate(ye22)',
                    texname = '\\text{I109x25}')

I109x33 = Parameter(name = 'I109x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn33*complexconjugate(Rl36)*complexconjugate(ye33)',
                    texname = '\\text{I109x33}')

I109x36 = Parameter(name = 'I109x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn33*complexconjugate(Rl66)*complexconjugate(ye33)',
                    texname = '\\text{I109x36}')

I11x11 = Parameter(name = 'I11x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd11*complexconjugate(CKM11)*complexconjugate(yu11)',
                   texname = '\\text{I11x11}')

I11x14 = Parameter(name = 'I11x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd41*complexconjugate(CKM11)*complexconjugate(yu11)',
                   texname = '\\text{I11x14}')

I11x22 = Parameter(name = 'I11x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd22*complexconjugate(CKM22)*complexconjugate(yu22)',
                   texname = '\\text{I11x22}')

I11x25 = Parameter(name = 'I11x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd52*complexconjugate(CKM22)*complexconjugate(yu22)',
                   texname = '\\text{I11x25}')

I11x33 = Parameter(name = 'I11x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd33*complexconjugate(CKM33)*complexconjugate(yu33)',
                   texname = '\\text{I11x33}')

I11x36 = Parameter(name = 'I11x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd63*complexconjugate(CKM33)*complexconjugate(yu33)',
                   texname = '\\text{I11x36}')

I110x11 = Parameter(name = 'I110x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl14*ye11*complexconjugate(Rn11)',
                    texname = '\\text{I110x11}')

I110x14 = Parameter(name = 'I110x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl44*ye11*complexconjugate(Rn11)',
                    texname = '\\text{I110x14}')

I110x22 = Parameter(name = 'I110x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl25*ye22*complexconjugate(Rn22)',
                    texname = '\\text{I110x22}')

I110x25 = Parameter(name = 'I110x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl55*ye22*complexconjugate(Rn22)',
                    texname = '\\text{I110x25}')

I110x33 = Parameter(name = 'I110x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl36*ye33*complexconjugate(Rn33)',
                    texname = '\\text{I110x33}')

I110x36 = Parameter(name = 'I110x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl66*ye33*complexconjugate(Rn33)',
                    texname = '\\text{I110x36}')

I111x11 = Parameter(name = 'I111x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(Ru14)*complexconjugate(yu11)',
                    texname = '\\text{I111x11}')

I111x14 = Parameter(name = 'I111x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(Ru44)*complexconjugate(yu11)',
                    texname = '\\text{I111x14}')

I111x22 = Parameter(name = 'I111x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(Ru25)*complexconjugate(yu22)',
                    texname = '\\text{I111x22}')

I111x25 = Parameter(name = 'I111x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(Ru55)*complexconjugate(yu22)',
                    texname = '\\text{I111x25}')

I111x33 = Parameter(name = 'I111x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(Ru36)*complexconjugate(yu33)',
                    texname = '\\text{I111x33}')

I111x36 = Parameter(name = 'I111x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(Ru66)*complexconjugate(yu33)',
                    texname = '\\text{I111x36}')

I112x11 = Parameter(name = 'I112x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'yu11*complexconjugate(Ru11)',
                    texname = '\\text{I112x11}')

I112x14 = Parameter(name = 'I112x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'yu11*complexconjugate(Ru41)',
                    texname = '\\text{I112x14}')

I112x22 = Parameter(name = 'I112x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'yu22*complexconjugate(Ru22)',
                    texname = '\\text{I112x22}')

I112x25 = Parameter(name = 'I112x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'yu22*complexconjugate(Ru52)',
                    texname = '\\text{I112x25}')

I112x33 = Parameter(name = 'I112x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'yu33*complexconjugate(Ru33)',
                    texname = '\\text{I112x33}')

I112x36 = Parameter(name = 'I112x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'yu33*complexconjugate(Ru63)',
                    texname = '\\text{I112x36}')

I113x11 = Parameter(name = 'I113x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru11*complexconjugate(Ru11)',
                    texname = '\\text{I113x11}')

I113x14 = Parameter(name = 'I113x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru41*complexconjugate(Ru11)',
                    texname = '\\text{I113x14}')

I113x22 = Parameter(name = 'I113x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru22*complexconjugate(Ru22)',
                    texname = '\\text{I113x22}')

I113x25 = Parameter(name = 'I113x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru52*complexconjugate(Ru22)',
                    texname = '\\text{I113x25}')

I113x33 = Parameter(name = 'I113x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru33*complexconjugate(Ru33)',
                    texname = '\\text{I113x33}')

I113x36 = Parameter(name = 'I113x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru63*complexconjugate(Ru33)',
                    texname = '\\text{I113x36}')

I113x41 = Parameter(name = 'I113x41',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru11*complexconjugate(Ru41)',
                    texname = '\\text{I113x41}')

I113x44 = Parameter(name = 'I113x44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru41*complexconjugate(Ru41)',
                    texname = '\\text{I113x44}')

I113x52 = Parameter(name = 'I113x52',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru22*complexconjugate(Ru52)',
                    texname = '\\text{I113x52}')

I113x55 = Parameter(name = 'I113x55',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru52*complexconjugate(Ru52)',
                    texname = '\\text{I113x55}')

I113x63 = Parameter(name = 'I113x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru33*complexconjugate(Ru63)',
                    texname = '\\text{I113x63}')

I113x66 = Parameter(name = 'I113x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru63*complexconjugate(Ru63)',
                    texname = '\\text{I113x66}')

I114x11 = Parameter(name = 'I114x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru14*complexconjugate(Ru14)',
                    texname = '\\text{I114x11}')

I114x14 = Parameter(name = 'I114x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru44*complexconjugate(Ru14)',
                    texname = '\\text{I114x14}')

I114x22 = Parameter(name = 'I114x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru25*complexconjugate(Ru25)',
                    texname = '\\text{I114x22}')

I114x25 = Parameter(name = 'I114x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru55*complexconjugate(Ru25)',
                    texname = '\\text{I114x25}')

I114x33 = Parameter(name = 'I114x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru36*complexconjugate(Ru36)',
                    texname = '\\text{I114x33}')

I114x36 = Parameter(name = 'I114x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru66*complexconjugate(Ru36)',
                    texname = '\\text{I114x36}')

I114x41 = Parameter(name = 'I114x41',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru14*complexconjugate(Ru44)',
                    texname = '\\text{I114x41}')

I114x44 = Parameter(name = 'I114x44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru44*complexconjugate(Ru44)',
                    texname = '\\text{I114x44}')

I114x52 = Parameter(name = 'I114x52',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru25*complexconjugate(Ru55)',
                    texname = '\\text{I114x52}')

I114x55 = Parameter(name = 'I114x55',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru55*complexconjugate(Ru55)',
                    texname = '\\text{I114x55}')

I114x63 = Parameter(name = 'I114x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru36*complexconjugate(Ru66)',
                    texname = '\\text{I114x63}')

I114x66 = Parameter(name = 'I114x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru66*complexconjugate(Ru66)',
                    texname = '\\text{I114x66}')

I115x11 = Parameter(name = 'I115x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd11*complexconjugate(CKM11)*complexconjugate(Ru11)',
                    texname = '\\text{I115x11}')

I115x14 = Parameter(name = 'I115x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd11*complexconjugate(CKM11)*complexconjugate(Ru41)',
                    texname = '\\text{I115x14}')

I115x22 = Parameter(name = 'I115x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd22*complexconjugate(CKM22)*complexconjugate(Ru22)',
                    texname = '\\text{I115x22}')

I115x25 = Parameter(name = 'I115x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd22*complexconjugate(CKM22)*complexconjugate(Ru52)',
                    texname = '\\text{I115x25}')

I115x33 = Parameter(name = 'I115x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd33*complexconjugate(CKM33)*complexconjugate(Ru33)',
                    texname = '\\text{I115x33}')

I115x36 = Parameter(name = 'I115x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd33*complexconjugate(CKM33)*complexconjugate(Ru63)',
                    texname = '\\text{I115x36}')

I115x41 = Parameter(name = 'I115x41',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd41*complexconjugate(CKM11)*complexconjugate(Ru11)',
                    texname = '\\text{I115x41}')

I115x44 = Parameter(name = 'I115x44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd41*complexconjugate(CKM11)*complexconjugate(Ru41)',
                    texname = '\\text{I115x44}')

I115x52 = Parameter(name = 'I115x52',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd52*complexconjugate(CKM22)*complexconjugate(Ru22)',
                    texname = '\\text{I115x52}')

I115x55 = Parameter(name = 'I115x55',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd52*complexconjugate(CKM22)*complexconjugate(Ru52)',
                    texname = '\\text{I115x55}')

I115x63 = Parameter(name = 'I115x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd63*complexconjugate(CKM33)*complexconjugate(Ru33)',
                    texname = '\\text{I115x63}')

I115x66 = Parameter(name = 'I115x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd63*complexconjugate(CKM33)*complexconjugate(Ru63)',
                    texname = '\\text{I115x66}')

I116x11 = Parameter(name = 'I116x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd11*complexconjugate(CKM11)*complexconjugate(Ru14)*complexconjugate(yu11)',
                    texname = '\\text{I116x11}')

I116x14 = Parameter(name = 'I116x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd11*complexconjugate(CKM11)*complexconjugate(Ru44)*complexconjugate(yu11)',
                    texname = '\\text{I116x14}')

I116x22 = Parameter(name = 'I116x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd22*complexconjugate(CKM22)*complexconjugate(Ru25)*complexconjugate(yu22)',
                    texname = '\\text{I116x22}')

I116x25 = Parameter(name = 'I116x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd22*complexconjugate(CKM22)*complexconjugate(Ru55)*complexconjugate(yu22)',
                    texname = '\\text{I116x25}')

I116x33 = Parameter(name = 'I116x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd33*complexconjugate(CKM33)*complexconjugate(Ru36)*complexconjugate(yu33)',
                    texname = '\\text{I116x33}')

I116x36 = Parameter(name = 'I116x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd33*complexconjugate(CKM33)*complexconjugate(Ru66)*complexconjugate(yu33)',
                    texname = '\\text{I116x36}')

I116x41 = Parameter(name = 'I116x41',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd41*complexconjugate(CKM11)*complexconjugate(Ru14)*complexconjugate(yu11)',
                    texname = '\\text{I116x41}')

I116x44 = Parameter(name = 'I116x44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd41*complexconjugate(CKM11)*complexconjugate(Ru44)*complexconjugate(yu11)',
                    texname = '\\text{I116x44}')

I116x52 = Parameter(name = 'I116x52',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd52*complexconjugate(CKM22)*complexconjugate(Ru25)*complexconjugate(yu22)',
                    texname = '\\text{I116x52}')

I116x55 = Parameter(name = 'I116x55',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd52*complexconjugate(CKM22)*complexconjugate(Ru55)*complexconjugate(yu22)',
                    texname = '\\text{I116x55}')

I116x63 = Parameter(name = 'I116x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd63*complexconjugate(CKM33)*complexconjugate(Ru36)*complexconjugate(yu33)',
                    texname = '\\text{I116x63}')

I116x66 = Parameter(name = 'I116x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd63*complexconjugate(CKM33)*complexconjugate(Ru66)*complexconjugate(yu33)',
                    texname = '\\text{I116x66}')

I117x11 = Parameter(name = 'I117x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd11*complexconjugate(CKM11)*complexconjugate(Ru14)*complexconjugate(tu11)',
                    texname = '\\text{I117x11}')

I117x14 = Parameter(name = 'I117x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd11*complexconjugate(CKM11)*complexconjugate(Ru44)*complexconjugate(tu11)',
                    texname = '\\text{I117x14}')

I117x22 = Parameter(name = 'I117x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd22*complexconjugate(CKM22)*complexconjugate(Ru25)*complexconjugate(tu22)',
                    texname = '\\text{I117x22}')

I117x25 = Parameter(name = 'I117x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd22*complexconjugate(CKM22)*complexconjugate(Ru55)*complexconjugate(tu22)',
                    texname = '\\text{I117x25}')

I117x33 = Parameter(name = 'I117x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd33*complexconjugate(CKM33)*complexconjugate(Ru36)*complexconjugate(tu33)',
                    texname = '\\text{I117x33}')

I117x36 = Parameter(name = 'I117x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd33*complexconjugate(CKM33)*complexconjugate(Ru66)*complexconjugate(tu33)',
                    texname = '\\text{I117x36}')

I117x41 = Parameter(name = 'I117x41',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd41*complexconjugate(CKM11)*complexconjugate(Ru14)*complexconjugate(tu11)',
                    texname = '\\text{I117x41}')

I117x44 = Parameter(name = 'I117x44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd41*complexconjugate(CKM11)*complexconjugate(Ru44)*complexconjugate(tu11)',
                    texname = '\\text{I117x44}')

I117x52 = Parameter(name = 'I117x52',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd52*complexconjugate(CKM22)*complexconjugate(Ru25)*complexconjugate(tu22)',
                    texname = '\\text{I117x52}')

I117x55 = Parameter(name = 'I117x55',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd52*complexconjugate(CKM22)*complexconjugate(Ru55)*complexconjugate(tu22)',
                    texname = '\\text{I117x55}')

I117x63 = Parameter(name = 'I117x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd63*complexconjugate(CKM33)*complexconjugate(Ru36)*complexconjugate(tu33)',
                    texname = '\\text{I117x63}')

I117x66 = Parameter(name = 'I117x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd63*complexconjugate(CKM33)*complexconjugate(Ru66)*complexconjugate(tu33)',
                    texname = '\\text{I117x66}')

I118x11 = Parameter(name = 'I118x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd14*td11*complexconjugate(CKM11)*complexconjugate(Ru11)',
                    texname = '\\text{I118x11}')

I118x14 = Parameter(name = 'I118x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd14*td11*complexconjugate(CKM11)*complexconjugate(Ru41)',
                    texname = '\\text{I118x14}')

I118x22 = Parameter(name = 'I118x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd25*td22*complexconjugate(CKM22)*complexconjugate(Ru22)',
                    texname = '\\text{I118x22}')

I118x25 = Parameter(name = 'I118x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd25*td22*complexconjugate(CKM22)*complexconjugate(Ru52)',
                    texname = '\\text{I118x25}')

I118x33 = Parameter(name = 'I118x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd36*td33*complexconjugate(CKM33)*complexconjugate(Ru33)',
                    texname = '\\text{I118x33}')

I118x36 = Parameter(name = 'I118x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd36*td33*complexconjugate(CKM33)*complexconjugate(Ru63)',
                    texname = '\\text{I118x36}')

I118x41 = Parameter(name = 'I118x41',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd44*td11*complexconjugate(CKM11)*complexconjugate(Ru11)',
                    texname = '\\text{I118x41}')

I118x44 = Parameter(name = 'I118x44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd44*td11*complexconjugate(CKM11)*complexconjugate(Ru41)',
                    texname = '\\text{I118x44}')

I118x52 = Parameter(name = 'I118x52',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd55*td22*complexconjugate(CKM22)*complexconjugate(Ru22)',
                    texname = '\\text{I118x52}')

I118x55 = Parameter(name = 'I118x55',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd55*td22*complexconjugate(CKM22)*complexconjugate(Ru52)',
                    texname = '\\text{I118x55}')

I118x63 = Parameter(name = 'I118x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd66*td33*complexconjugate(CKM33)*complexconjugate(Ru33)',
                    texname = '\\text{I118x63}')

I118x66 = Parameter(name = 'I118x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd66*td33*complexconjugate(CKM33)*complexconjugate(Ru63)',
                    texname = '\\text{I118x66}')

I119x11 = Parameter(name = 'I119x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd11*yd11*complexconjugate(CKM11)*complexconjugate(Ru11)*complexconjugate(yd11)',
                    texname = '\\text{I119x11}')

I119x14 = Parameter(name = 'I119x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd11*yd11*complexconjugate(CKM11)*complexconjugate(Ru41)*complexconjugate(yd11)',
                    texname = '\\text{I119x14}')

I119x22 = Parameter(name = 'I119x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd22*yd22*complexconjugate(CKM22)*complexconjugate(Ru22)*complexconjugate(yd22)',
                    texname = '\\text{I119x22}')

I119x25 = Parameter(name = 'I119x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd22*yd22*complexconjugate(CKM22)*complexconjugate(Ru52)*complexconjugate(yd22)',
                    texname = '\\text{I119x25}')

I119x33 = Parameter(name = 'I119x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd33*yd33*complexconjugate(CKM33)*complexconjugate(Ru33)*complexconjugate(yd33)',
                    texname = '\\text{I119x33}')

I119x36 = Parameter(name = 'I119x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd33*yd33*complexconjugate(CKM33)*complexconjugate(Ru63)*complexconjugate(yd33)',
                    texname = '\\text{I119x36}')

I119x41 = Parameter(name = 'I119x41',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd41*yd11*complexconjugate(CKM11)*complexconjugate(Ru11)*complexconjugate(yd11)',
                    texname = '\\text{I119x41}')

I119x44 = Parameter(name = 'I119x44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd41*yd11*complexconjugate(CKM11)*complexconjugate(Ru41)*complexconjugate(yd11)',
                    texname = '\\text{I119x44}')

I119x52 = Parameter(name = 'I119x52',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd52*yd22*complexconjugate(CKM22)*complexconjugate(Ru22)*complexconjugate(yd22)',
                    texname = '\\text{I119x52}')

I119x55 = Parameter(name = 'I119x55',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd52*yd22*complexconjugate(CKM22)*complexconjugate(Ru52)*complexconjugate(yd22)',
                    texname = '\\text{I119x55}')

I119x63 = Parameter(name = 'I119x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd63*yd33*complexconjugate(CKM33)*complexconjugate(Ru33)*complexconjugate(yd33)',
                    texname = '\\text{I119x63}')

I119x66 = Parameter(name = 'I119x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd63*yd33*complexconjugate(CKM33)*complexconjugate(Ru63)*complexconjugate(yd33)',
                    texname = '\\text{I119x66}')

I12x11 = Parameter(name = 'I12x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd14*yd11*complexconjugate(CKM11)',
                   texname = '\\text{I12x11}')

I12x14 = Parameter(name = 'I12x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd44*yd11*complexconjugate(CKM11)',
                   texname = '\\text{I12x14}')

I12x22 = Parameter(name = 'I12x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd25*yd22*complexconjugate(CKM22)',
                   texname = '\\text{I12x22}')

I12x25 = Parameter(name = 'I12x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd55*yd22*complexconjugate(CKM22)',
                   texname = '\\text{I12x25}')

I12x33 = Parameter(name = 'I12x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd36*yd33*complexconjugate(CKM33)',
                   texname = '\\text{I12x33}')

I12x36 = Parameter(name = 'I12x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd66*yd33*complexconjugate(CKM33)',
                   texname = '\\text{I12x36}')

I120x11 = Parameter(name = 'I120x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd14*yd11*complexconjugate(CKM11)*complexconjugate(Ru11)',
                    texname = '\\text{I120x11}')

I120x14 = Parameter(name = 'I120x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd14*yd11*complexconjugate(CKM11)*complexconjugate(Ru41)',
                    texname = '\\text{I120x14}')

I120x22 = Parameter(name = 'I120x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd25*yd22*complexconjugate(CKM22)*complexconjugate(Ru22)',
                    texname = '\\text{I120x22}')

I120x25 = Parameter(name = 'I120x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd25*yd22*complexconjugate(CKM22)*complexconjugate(Ru52)',
                    texname = '\\text{I120x25}')

I120x33 = Parameter(name = 'I120x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd36*yd33*complexconjugate(CKM33)*complexconjugate(Ru33)',
                    texname = '\\text{I120x33}')

I120x36 = Parameter(name = 'I120x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd36*yd33*complexconjugate(CKM33)*complexconjugate(Ru63)',
                    texname = '\\text{I120x36}')

I120x41 = Parameter(name = 'I120x41',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd44*yd11*complexconjugate(CKM11)*complexconjugate(Ru11)',
                    texname = '\\text{I120x41}')

I120x44 = Parameter(name = 'I120x44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd44*yd11*complexconjugate(CKM11)*complexconjugate(Ru41)',
                    texname = '\\text{I120x44}')

I120x52 = Parameter(name = 'I120x52',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd55*yd22*complexconjugate(CKM22)*complexconjugate(Ru22)',
                    texname = '\\text{I120x52}')

I120x55 = Parameter(name = 'I120x55',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd55*yd22*complexconjugate(CKM22)*complexconjugate(Ru52)',
                    texname = '\\text{I120x55}')

I120x63 = Parameter(name = 'I120x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd66*yd33*complexconjugate(CKM33)*complexconjugate(Ru33)',
                    texname = '\\text{I120x63}')

I120x66 = Parameter(name = 'I120x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd66*yd33*complexconjugate(CKM33)*complexconjugate(Ru63)',
                    texname = '\\text{I120x66}')

I121x11 = Parameter(name = 'I121x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd14*yd11*complexconjugate(CKM11)*complexconjugate(Ru14)*complexconjugate(yu11)',
                    texname = '\\text{I121x11}')

I121x14 = Parameter(name = 'I121x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd14*yd11*complexconjugate(CKM11)*complexconjugate(Ru44)*complexconjugate(yu11)',
                    texname = '\\text{I121x14}')

I121x22 = Parameter(name = 'I121x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd25*yd22*complexconjugate(CKM22)*complexconjugate(Ru25)*complexconjugate(yu22)',
                    texname = '\\text{I121x22}')

I121x25 = Parameter(name = 'I121x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd25*yd22*complexconjugate(CKM22)*complexconjugate(Ru55)*complexconjugate(yu22)',
                    texname = '\\text{I121x25}')

I121x33 = Parameter(name = 'I121x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd36*yd33*complexconjugate(CKM33)*complexconjugate(Ru36)*complexconjugate(yu33)',
                    texname = '\\text{I121x33}')

I121x36 = Parameter(name = 'I121x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd36*yd33*complexconjugate(CKM33)*complexconjugate(Ru66)*complexconjugate(yu33)',
                    texname = '\\text{I121x36}')

I121x41 = Parameter(name = 'I121x41',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd44*yd11*complexconjugate(CKM11)*complexconjugate(Ru14)*complexconjugate(yu11)',
                    texname = '\\text{I121x41}')

I121x44 = Parameter(name = 'I121x44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd44*yd11*complexconjugate(CKM11)*complexconjugate(Ru44)*complexconjugate(yu11)',
                    texname = '\\text{I121x44}')

I121x52 = Parameter(name = 'I121x52',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd55*yd22*complexconjugate(CKM22)*complexconjugate(Ru25)*complexconjugate(yu22)',
                    texname = '\\text{I121x52}')

I121x55 = Parameter(name = 'I121x55',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd55*yd22*complexconjugate(CKM22)*complexconjugate(Ru55)*complexconjugate(yu22)',
                    texname = '\\text{I121x55}')

I121x63 = Parameter(name = 'I121x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd66*yd33*complexconjugate(CKM33)*complexconjugate(Ru36)*complexconjugate(yu33)',
                    texname = '\\text{I121x63}')

I121x66 = Parameter(name = 'I121x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd66*yd33*complexconjugate(CKM33)*complexconjugate(Ru66)*complexconjugate(yu33)',
                    texname = '\\text{I121x66}')

I122x11 = Parameter(name = 'I122x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd11*yu11*complexconjugate(CKM11)*complexconjugate(Ru11)*complexconjugate(yu11)',
                    texname = '\\text{I122x11}')

I122x14 = Parameter(name = 'I122x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd11*yu11*complexconjugate(CKM11)*complexconjugate(Ru41)*complexconjugate(yu11)',
                    texname = '\\text{I122x14}')

I122x22 = Parameter(name = 'I122x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd22*yu22*complexconjugate(CKM22)*complexconjugate(Ru22)*complexconjugate(yu22)',
                    texname = '\\text{I122x22}')

I122x25 = Parameter(name = 'I122x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd22*yu22*complexconjugate(CKM22)*complexconjugate(Ru52)*complexconjugate(yu22)',
                    texname = '\\text{I122x25}')

I122x33 = Parameter(name = 'I122x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd33*yu33*complexconjugate(CKM33)*complexconjugate(Ru33)*complexconjugate(yu33)',
                    texname = '\\text{I122x33}')

I122x36 = Parameter(name = 'I122x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd33*yu33*complexconjugate(CKM33)*complexconjugate(Ru63)*complexconjugate(yu33)',
                    texname = '\\text{I122x36}')

I122x41 = Parameter(name = 'I122x41',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd41*yu11*complexconjugate(CKM11)*complexconjugate(Ru11)*complexconjugate(yu11)',
                    texname = '\\text{I122x41}')

I122x44 = Parameter(name = 'I122x44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd41*yu11*complexconjugate(CKM11)*complexconjugate(Ru41)*complexconjugate(yu11)',
                    texname = '\\text{I122x44}')

I122x52 = Parameter(name = 'I122x52',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd52*yu22*complexconjugate(CKM22)*complexconjugate(Ru22)*complexconjugate(yu22)',
                    texname = '\\text{I122x52}')

I122x55 = Parameter(name = 'I122x55',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd52*yu22*complexconjugate(CKM22)*complexconjugate(Ru52)*complexconjugate(yu22)',
                    texname = '\\text{I122x55}')

I122x63 = Parameter(name = 'I122x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd63*yu33*complexconjugate(CKM33)*complexconjugate(Ru33)*complexconjugate(yu33)',
                    texname = '\\text{I122x63}')

I122x66 = Parameter(name = 'I122x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd63*yu33*complexconjugate(CKM33)*complexconjugate(Ru63)*complexconjugate(yu33)',
                    texname = '\\text{I122x66}')

I123x11 = Parameter(name = 'I123x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd11*complexconjugate(CKM11)*complexconjugate(Ru11)',
                    texname = '\\text{I123x11}')

I123x14 = Parameter(name = 'I123x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd11*complexconjugate(CKM11)*complexconjugate(Ru41)',
                    texname = '\\text{I123x14}')

I123x22 = Parameter(name = 'I123x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd22*complexconjugate(CKM22)*complexconjugate(Ru22)',
                    texname = '\\text{I123x22}')

I123x25 = Parameter(name = 'I123x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd22*complexconjugate(CKM22)*complexconjugate(Ru52)',
                    texname = '\\text{I123x25}')

I123x33 = Parameter(name = 'I123x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd33*complexconjugate(CKM33)*complexconjugate(Ru33)',
                    texname = '\\text{I123x33}')

I123x36 = Parameter(name = 'I123x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd33*complexconjugate(CKM33)*complexconjugate(Ru63)',
                    texname = '\\text{I123x36}')

I123x41 = Parameter(name = 'I123x41',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd41*complexconjugate(CKM11)*complexconjugate(Ru11)',
                    texname = '\\text{I123x41}')

I123x44 = Parameter(name = 'I123x44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd41*complexconjugate(CKM11)*complexconjugate(Ru41)',
                    texname = '\\text{I123x44}')

I123x52 = Parameter(name = 'I123x52',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd52*complexconjugate(CKM22)*complexconjugate(Ru22)',
                    texname = '\\text{I123x52}')

I123x55 = Parameter(name = 'I123x55',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd52*complexconjugate(CKM22)*complexconjugate(Ru52)',
                    texname = '\\text{I123x55}')

I123x63 = Parameter(name = 'I123x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd63*complexconjugate(CKM33)*complexconjugate(Ru33)',
                    texname = '\\text{I123x63}')

I123x66 = Parameter(name = 'I123x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd63*complexconjugate(CKM33)*complexconjugate(Ru63)',
                    texname = '\\text{I123x66}')

I124x11 = Parameter(name = 'I124x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd11*yd11*complexconjugate(CKM11)*complexconjugate(Ru11)*complexconjugate(yd11)',
                    texname = '\\text{I124x11}')

I124x14 = Parameter(name = 'I124x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd11*yd11*complexconjugate(CKM11)*complexconjugate(Ru41)*complexconjugate(yd11)',
                    texname = '\\text{I124x14}')

I124x22 = Parameter(name = 'I124x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd22*yd22*complexconjugate(CKM22)*complexconjugate(Ru22)*complexconjugate(yd22)',
                    texname = '\\text{I124x22}')

I124x25 = Parameter(name = 'I124x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd22*yd22*complexconjugate(CKM22)*complexconjugate(Ru52)*complexconjugate(yd22)',
                    texname = '\\text{I124x25}')

I124x33 = Parameter(name = 'I124x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd33*yd33*complexconjugate(CKM33)*complexconjugate(Ru33)*complexconjugate(yd33)',
                    texname = '\\text{I124x33}')

I124x36 = Parameter(name = 'I124x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd33*yd33*complexconjugate(CKM33)*complexconjugate(Ru63)*complexconjugate(yd33)',
                    texname = '\\text{I124x36}')

I124x41 = Parameter(name = 'I124x41',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd41*yd11*complexconjugate(CKM11)*complexconjugate(Ru11)*complexconjugate(yd11)',
                    texname = '\\text{I124x41}')

I124x44 = Parameter(name = 'I124x44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd41*yd11*complexconjugate(CKM11)*complexconjugate(Ru41)*complexconjugate(yd11)',
                    texname = '\\text{I124x44}')

I124x52 = Parameter(name = 'I124x52',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd52*yd22*complexconjugate(CKM22)*complexconjugate(Ru22)*complexconjugate(yd22)',
                    texname = '\\text{I124x52}')

I124x55 = Parameter(name = 'I124x55',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd52*yd22*complexconjugate(CKM22)*complexconjugate(Ru52)*complexconjugate(yd22)',
                    texname = '\\text{I124x55}')

I124x63 = Parameter(name = 'I124x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd63*yd33*complexconjugate(CKM33)*complexconjugate(Ru33)*complexconjugate(yd33)',
                    texname = '\\text{I124x63}')

I124x66 = Parameter(name = 'I124x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd63*yd33*complexconjugate(CKM33)*complexconjugate(Ru63)*complexconjugate(yd33)',
                    texname = '\\text{I124x66}')

I125x11 = Parameter(name = 'I125x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd14*yd11*complexconjugate(CKM11)*complexconjugate(Ru14)*complexconjugate(yu11)',
                    texname = '\\text{I125x11}')

I125x14 = Parameter(name = 'I125x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd14*yd11*complexconjugate(CKM11)*complexconjugate(Ru44)*complexconjugate(yu11)',
                    texname = '\\text{I125x14}')

I125x22 = Parameter(name = 'I125x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd25*yd22*complexconjugate(CKM22)*complexconjugate(Ru25)*complexconjugate(yu22)',
                    texname = '\\text{I125x22}')

I125x25 = Parameter(name = 'I125x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd25*yd22*complexconjugate(CKM22)*complexconjugate(Ru55)*complexconjugate(yu22)',
                    texname = '\\text{I125x25}')

I125x33 = Parameter(name = 'I125x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd36*yd33*complexconjugate(CKM33)*complexconjugate(Ru36)*complexconjugate(yu33)',
                    texname = '\\text{I125x33}')

I125x36 = Parameter(name = 'I125x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd36*yd33*complexconjugate(CKM33)*complexconjugate(Ru66)*complexconjugate(yu33)',
                    texname = '\\text{I125x36}')

I125x41 = Parameter(name = 'I125x41',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd44*yd11*complexconjugate(CKM11)*complexconjugate(Ru14)*complexconjugate(yu11)',
                    texname = '\\text{I125x41}')

I125x44 = Parameter(name = 'I125x44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd44*yd11*complexconjugate(CKM11)*complexconjugate(Ru44)*complexconjugate(yu11)',
                    texname = '\\text{I125x44}')

I125x52 = Parameter(name = 'I125x52',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd55*yd22*complexconjugate(CKM22)*complexconjugate(Ru25)*complexconjugate(yu22)',
                    texname = '\\text{I125x52}')

I125x55 = Parameter(name = 'I125x55',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd55*yd22*complexconjugate(CKM22)*complexconjugate(Ru55)*complexconjugate(yu22)',
                    texname = '\\text{I125x55}')

I125x63 = Parameter(name = 'I125x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd66*yd33*complexconjugate(CKM33)*complexconjugate(Ru36)*complexconjugate(yu33)',
                    texname = '\\text{I125x63}')

I125x66 = Parameter(name = 'I125x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd66*yd33*complexconjugate(CKM33)*complexconjugate(Ru66)*complexconjugate(yu33)',
                    texname = '\\text{I125x66}')

I126x11 = Parameter(name = 'I126x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd11*yu11*complexconjugate(CKM11)*complexconjugate(Ru11)*complexconjugate(yu11)',
                    texname = '\\text{I126x11}')

I126x14 = Parameter(name = 'I126x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd11*yu11*complexconjugate(CKM11)*complexconjugate(Ru41)*complexconjugate(yu11)',
                    texname = '\\text{I126x14}')

I126x22 = Parameter(name = 'I126x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd22*yu22*complexconjugate(CKM22)*complexconjugate(Ru22)*complexconjugate(yu22)',
                    texname = '\\text{I126x22}')

I126x25 = Parameter(name = 'I126x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd22*yu22*complexconjugate(CKM22)*complexconjugate(Ru52)*complexconjugate(yu22)',
                    texname = '\\text{I126x25}')

I126x33 = Parameter(name = 'I126x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd33*yu33*complexconjugate(CKM33)*complexconjugate(Ru33)*complexconjugate(yu33)',
                    texname = '\\text{I126x33}')

I126x36 = Parameter(name = 'I126x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd33*yu33*complexconjugate(CKM33)*complexconjugate(Ru63)*complexconjugate(yu33)',
                    texname = '\\text{I126x36}')

I126x41 = Parameter(name = 'I126x41',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd41*yu11*complexconjugate(CKM11)*complexconjugate(Ru11)*complexconjugate(yu11)',
                    texname = '\\text{I126x41}')

I126x44 = Parameter(name = 'I126x44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd41*yu11*complexconjugate(CKM11)*complexconjugate(Ru41)*complexconjugate(yu11)',
                    texname = '\\text{I126x44}')

I126x52 = Parameter(name = 'I126x52',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd52*yu22*complexconjugate(CKM22)*complexconjugate(Ru22)*complexconjugate(yu22)',
                    texname = '\\text{I126x52}')

I126x55 = Parameter(name = 'I126x55',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd52*yu22*complexconjugate(CKM22)*complexconjugate(Ru52)*complexconjugate(yu22)',
                    texname = '\\text{I126x55}')

I126x63 = Parameter(name = 'I126x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd63*yu33*complexconjugate(CKM33)*complexconjugate(Ru33)*complexconjugate(yu33)',
                    texname = '\\text{I126x63}')

I126x66 = Parameter(name = 'I126x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd63*yu33*complexconjugate(CKM33)*complexconjugate(Ru63)*complexconjugate(yu33)',
                    texname = '\\text{I126x66}')

I127x11 = Parameter(name = 'I127x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd11*complexconjugate(CKM11)*complexconjugate(Ru11)',
                    texname = '\\text{I127x11}')

I127x14 = Parameter(name = 'I127x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd11*complexconjugate(CKM11)*complexconjugate(Ru41)',
                    texname = '\\text{I127x14}')

I127x22 = Parameter(name = 'I127x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd22*complexconjugate(CKM22)*complexconjugate(Ru22)',
                    texname = '\\text{I127x22}')

I127x25 = Parameter(name = 'I127x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd22*complexconjugate(CKM22)*complexconjugate(Ru52)',
                    texname = '\\text{I127x25}')

I127x33 = Parameter(name = 'I127x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd33*complexconjugate(CKM33)*complexconjugate(Ru33)',
                    texname = '\\text{I127x33}')

I127x36 = Parameter(name = 'I127x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd33*complexconjugate(CKM33)*complexconjugate(Ru63)',
                    texname = '\\text{I127x36}')

I127x41 = Parameter(name = 'I127x41',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd41*complexconjugate(CKM11)*complexconjugate(Ru11)',
                    texname = '\\text{I127x41}')

I127x44 = Parameter(name = 'I127x44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd41*complexconjugate(CKM11)*complexconjugate(Ru41)',
                    texname = '\\text{I127x44}')

I127x52 = Parameter(name = 'I127x52',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd52*complexconjugate(CKM22)*complexconjugate(Ru22)',
                    texname = '\\text{I127x52}')

I127x55 = Parameter(name = 'I127x55',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd52*complexconjugate(CKM22)*complexconjugate(Ru52)',
                    texname = '\\text{I127x55}')

I127x63 = Parameter(name = 'I127x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd63*complexconjugate(CKM33)*complexconjugate(Ru33)',
                    texname = '\\text{I127x63}')

I127x66 = Parameter(name = 'I127x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd63*complexconjugate(CKM33)*complexconjugate(Ru63)',
                    texname = '\\text{I127x66}')

I128x11 = Parameter(name = 'I128x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn11*complexconjugate(Rl11)',
                    texname = '\\text{I128x11}')

I128x14 = Parameter(name = 'I128x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn11*complexconjugate(Rl41)',
                    texname = '\\text{I128x14}')

I128x22 = Parameter(name = 'I128x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn22*complexconjugate(Rl22)',
                    texname = '\\text{I128x22}')

I128x25 = Parameter(name = 'I128x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn22*complexconjugate(Rl52)',
                    texname = '\\text{I128x25}')

I128x33 = Parameter(name = 'I128x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn33*complexconjugate(Rl33)',
                    texname = '\\text{I128x33}')

I128x36 = Parameter(name = 'I128x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn33*complexconjugate(Rl63)',
                    texname = '\\text{I128x36}')

I129x11 = Parameter(name = 'I129x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn11*complexconjugate(Rl14)*complexconjugate(ye11)',
                    texname = '\\text{I129x11}')

I129x14 = Parameter(name = 'I129x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn11*complexconjugate(Rl44)*complexconjugate(ye11)',
                    texname = '\\text{I129x14}')

I129x22 = Parameter(name = 'I129x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn22*complexconjugate(Rl25)*complexconjugate(ye22)',
                    texname = '\\text{I129x22}')

I129x25 = Parameter(name = 'I129x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn22*complexconjugate(Rl55)*complexconjugate(ye22)',
                    texname = '\\text{I129x25}')

I129x33 = Parameter(name = 'I129x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn33*complexconjugate(Rl36)*complexconjugate(ye33)',
                    texname = '\\text{I129x33}')

I129x36 = Parameter(name = 'I129x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn33*complexconjugate(Rl66)*complexconjugate(ye33)',
                    texname = '\\text{I129x36}')

I13x11 = Parameter(name = 'I13x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd11*complexconjugate(yd11)',
                   texname = '\\text{I13x11}')

I13x14 = Parameter(name = 'I13x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd41*complexconjugate(yd11)',
                   texname = '\\text{I13x14}')

I13x22 = Parameter(name = 'I13x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd22*complexconjugate(yd22)',
                   texname = '\\text{I13x22}')

I13x25 = Parameter(name = 'I13x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd52*complexconjugate(yd22)',
                   texname = '\\text{I13x25}')

I13x33 = Parameter(name = 'I13x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd33*complexconjugate(yd33)',
                   texname = '\\text{I13x33}')

I13x36 = Parameter(name = 'I13x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd63*complexconjugate(yd33)',
                   texname = '\\text{I13x36}')

I130x11 = Parameter(name = 'I130x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd14*yd11*complexconjugate(CKM11)*complexconjugate(Ru11)',
                    texname = '\\text{I130x11}')

I130x14 = Parameter(name = 'I130x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd14*yd11*complexconjugate(CKM11)*complexconjugate(Ru41)',
                    texname = '\\text{I130x14}')

I130x22 = Parameter(name = 'I130x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd25*yd22*complexconjugate(CKM22)*complexconjugate(Ru22)',
                    texname = '\\text{I130x22}')

I130x25 = Parameter(name = 'I130x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd25*yd22*complexconjugate(CKM22)*complexconjugate(Ru52)',
                    texname = '\\text{I130x25}')

I130x33 = Parameter(name = 'I130x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd36*yd33*complexconjugate(CKM33)*complexconjugate(Ru33)',
                    texname = '\\text{I130x33}')

I130x36 = Parameter(name = 'I130x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd36*yd33*complexconjugate(CKM33)*complexconjugate(Ru63)',
                    texname = '\\text{I130x36}')

I130x41 = Parameter(name = 'I130x41',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd44*yd11*complexconjugate(CKM11)*complexconjugate(Ru11)',
                    texname = '\\text{I130x41}')

I130x44 = Parameter(name = 'I130x44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd44*yd11*complexconjugate(CKM11)*complexconjugate(Ru41)',
                    texname = '\\text{I130x44}')

I130x52 = Parameter(name = 'I130x52',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd55*yd22*complexconjugate(CKM22)*complexconjugate(Ru22)',
                    texname = '\\text{I130x52}')

I130x55 = Parameter(name = 'I130x55',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd55*yd22*complexconjugate(CKM22)*complexconjugate(Ru52)',
                    texname = '\\text{I130x55}')

I130x63 = Parameter(name = 'I130x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd66*yd33*complexconjugate(CKM33)*complexconjugate(Ru33)',
                    texname = '\\text{I130x63}')

I130x66 = Parameter(name = 'I130x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd66*yd33*complexconjugate(CKM33)*complexconjugate(Ru63)',
                    texname = '\\text{I130x66}')

I131x11 = Parameter(name = 'I131x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru11*complexconjugate(yu11)',
                    texname = '\\text{I131x11}')

I131x14 = Parameter(name = 'I131x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru41*complexconjugate(yu11)',
                    texname = '\\text{I131x14}')

I131x22 = Parameter(name = 'I131x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru22*complexconjugate(yu22)',
                    texname = '\\text{I131x22}')

I131x25 = Parameter(name = 'I131x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru52*complexconjugate(yu22)',
                    texname = '\\text{I131x25}')

I131x33 = Parameter(name = 'I131x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru33*complexconjugate(yu33)',
                    texname = '\\text{I131x33}')

I131x36 = Parameter(name = 'I131x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru63*complexconjugate(yu33)',
                    texname = '\\text{I131x36}')

I132x11 = Parameter(name = 'I132x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru14*yu11',
                    texname = '\\text{I132x11}')

I132x14 = Parameter(name = 'I132x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru44*yu11',
                    texname = '\\text{I132x14}')

I132x22 = Parameter(name = 'I132x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru25*yu22',
                    texname = '\\text{I132x22}')

I132x25 = Parameter(name = 'I132x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru55*yu22',
                    texname = '\\text{I132x25}')

I132x33 = Parameter(name = 'I132x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru36*yu33',
                    texname = '\\text{I132x33}')

I132x36 = Parameter(name = 'I132x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru66*yu33',
                    texname = '\\text{I132x36}')

I133x11 = Parameter(name = 'I133x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM11*Ru11',
                    texname = '\\text{I133x11}')

I133x14 = Parameter(name = 'I133x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM11*Ru41',
                    texname = '\\text{I133x14}')

I133x22 = Parameter(name = 'I133x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM22*Ru22',
                    texname = '\\text{I133x22}')

I133x25 = Parameter(name = 'I133x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM22*Ru52',
                    texname = '\\text{I133x25}')

I133x33 = Parameter(name = 'I133x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM33*Ru33',
                    texname = '\\text{I133x33}')

I133x36 = Parameter(name = 'I133x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM33*Ru63',
                    texname = '\\text{I133x36}')

I134x11 = Parameter(name = 'I134x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM11*Ru11*complexconjugate(yd11)',
                    texname = '\\text{I134x11}')

I134x14 = Parameter(name = 'I134x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM11*Ru41*complexconjugate(yd11)',
                    texname = '\\text{I134x14}')

I134x22 = Parameter(name = 'I134x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM22*Ru22*complexconjugate(yd22)',
                    texname = '\\text{I134x22}')

I134x25 = Parameter(name = 'I134x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM22*Ru52*complexconjugate(yd22)',
                    texname = '\\text{I134x25}')

I134x33 = Parameter(name = 'I134x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM33*Ru33*complexconjugate(yd33)',
                    texname = '\\text{I134x33}')

I134x36 = Parameter(name = 'I134x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM33*Ru63*complexconjugate(yd33)',
                    texname = '\\text{I134x36}')

I135x11 = Parameter(name = 'I135x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM11*Ru14*yu11',
                    texname = '\\text{I135x11}')

I135x14 = Parameter(name = 'I135x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM11*Ru44*yu11',
                    texname = '\\text{I135x14}')

I135x22 = Parameter(name = 'I135x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM22*Ru25*yu22',
                    texname = '\\text{I135x22}')

I135x25 = Parameter(name = 'I135x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM22*Ru55*yu22',
                    texname = '\\text{I135x25}')

I135x33 = Parameter(name = 'I135x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM33*Ru36*yu33',
                    texname = '\\text{I135x33}')

I135x36 = Parameter(name = 'I135x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM33*Ru66*yu33',
                    texname = '\\text{I135x36}')

I136x11 = Parameter(name = 'I136x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM11*Ru11*complexconjugate(Rd11)',
                    texname = '\\text{I136x11}')

I136x14 = Parameter(name = 'I136x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM11*Ru41*complexconjugate(Rd11)',
                    texname = '\\text{I136x14}')

I136x22 = Parameter(name = 'I136x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM22*Ru22*complexconjugate(Rd22)',
                    texname = '\\text{I136x22}')

I136x25 = Parameter(name = 'I136x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM22*Ru52*complexconjugate(Rd22)',
                    texname = '\\text{I136x25}')

I136x33 = Parameter(name = 'I136x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM33*Ru33*complexconjugate(Rd33)',
                    texname = '\\text{I136x33}')

I136x36 = Parameter(name = 'I136x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM33*Ru63*complexconjugate(Rd33)',
                    texname = '\\text{I136x36}')

I136x41 = Parameter(name = 'I136x41',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM11*Ru11*complexconjugate(Rd41)',
                    texname = '\\text{I136x41}')

I136x44 = Parameter(name = 'I136x44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM11*Ru41*complexconjugate(Rd41)',
                    texname = '\\text{I136x44}')

I136x52 = Parameter(name = 'I136x52',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM22*Ru22*complexconjugate(Rd52)',
                    texname = '\\text{I136x52}')

I136x55 = Parameter(name = 'I136x55',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM22*Ru52*complexconjugate(Rd52)',
                    texname = '\\text{I136x55}')

I136x63 = Parameter(name = 'I136x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM33*Ru33*complexconjugate(Rd63)',
                    texname = '\\text{I136x63}')

I136x66 = Parameter(name = 'I136x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM33*Ru63*complexconjugate(Rd63)',
                    texname = '\\text{I136x66}')

I137x11 = Parameter(name = 'I137x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM11*Ru11*complexconjugate(Rd14)*complexconjugate(td11)',
                    texname = '\\text{I137x11}')

I137x14 = Parameter(name = 'I137x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM11*Ru41*complexconjugate(Rd14)*complexconjugate(td11)',
                    texname = '\\text{I137x14}')

I137x22 = Parameter(name = 'I137x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM22*Ru22*complexconjugate(Rd25)*complexconjugate(td22)',
                    texname = '\\text{I137x22}')

I137x25 = Parameter(name = 'I137x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM22*Ru52*complexconjugate(Rd25)*complexconjugate(td22)',
                    texname = '\\text{I137x25}')

I137x33 = Parameter(name = 'I137x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM33*Ru33*complexconjugate(Rd36)*complexconjugate(td33)',
                    texname = '\\text{I137x33}')

I137x36 = Parameter(name = 'I137x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM33*Ru63*complexconjugate(Rd36)*complexconjugate(td33)',
                    texname = '\\text{I137x36}')

I137x41 = Parameter(name = 'I137x41',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM11*Ru11*complexconjugate(Rd44)*complexconjugate(td11)',
                    texname = '\\text{I137x41}')

I137x44 = Parameter(name = 'I137x44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM11*Ru41*complexconjugate(Rd44)*complexconjugate(td11)',
                    texname = '\\text{I137x44}')

I137x52 = Parameter(name = 'I137x52',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM22*Ru22*complexconjugate(Rd55)*complexconjugate(td22)',
                    texname = '\\text{I137x52}')

I137x55 = Parameter(name = 'I137x55',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM22*Ru52*complexconjugate(Rd55)*complexconjugate(td22)',
                    texname = '\\text{I137x55}')

I137x63 = Parameter(name = 'I137x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM33*Ru33*complexconjugate(Rd66)*complexconjugate(td33)',
                    texname = '\\text{I137x63}')

I137x66 = Parameter(name = 'I137x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM33*Ru63*complexconjugate(Rd66)*complexconjugate(td33)',
                    texname = '\\text{I137x66}')

I138x11 = Parameter(name = 'I138x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM11*Ru11*complexconjugate(Rd14)*complexconjugate(yd11)',
                    texname = '\\text{I138x11}')

I138x14 = Parameter(name = 'I138x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM11*Ru41*complexconjugate(Rd14)*complexconjugate(yd11)',
                    texname = '\\text{I138x14}')

I138x22 = Parameter(name = 'I138x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM22*Ru22*complexconjugate(Rd25)*complexconjugate(yd22)',
                    texname = '\\text{I138x22}')

I138x25 = Parameter(name = 'I138x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM22*Ru52*complexconjugate(Rd25)*complexconjugate(yd22)',
                    texname = '\\text{I138x25}')

I138x33 = Parameter(name = 'I138x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM33*Ru33*complexconjugate(Rd36)*complexconjugate(yd33)',
                    texname = '\\text{I138x33}')

I138x36 = Parameter(name = 'I138x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM33*Ru63*complexconjugate(Rd36)*complexconjugate(yd33)',
                    texname = '\\text{I138x36}')

I138x41 = Parameter(name = 'I138x41',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM11*Ru11*complexconjugate(Rd44)*complexconjugate(yd11)',
                    texname = '\\text{I138x41}')

I138x44 = Parameter(name = 'I138x44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM11*Ru41*complexconjugate(Rd44)*complexconjugate(yd11)',
                    texname = '\\text{I138x44}')

I138x52 = Parameter(name = 'I138x52',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM22*Ru22*complexconjugate(Rd55)*complexconjugate(yd22)',
                    texname = '\\text{I138x52}')

I138x55 = Parameter(name = 'I138x55',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM22*Ru52*complexconjugate(Rd55)*complexconjugate(yd22)',
                    texname = '\\text{I138x55}')

I138x63 = Parameter(name = 'I138x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM33*Ru33*complexconjugate(Rd66)*complexconjugate(yd33)',
                    texname = '\\text{I138x63}')

I138x66 = Parameter(name = 'I138x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM33*Ru63*complexconjugate(Rd66)*complexconjugate(yd33)',
                    texname = '\\text{I138x66}')

I139x11 = Parameter(name = 'I139x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM11*Ru14*tu11*complexconjugate(Rd11)',
                    texname = '\\text{I139x11}')

I139x14 = Parameter(name = 'I139x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM11*Ru44*tu11*complexconjugate(Rd11)',
                    texname = '\\text{I139x14}')

I139x22 = Parameter(name = 'I139x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM22*Ru25*tu22*complexconjugate(Rd22)',
                    texname = '\\text{I139x22}')

I139x25 = Parameter(name = 'I139x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM22*Ru55*tu22*complexconjugate(Rd22)',
                    texname = '\\text{I139x25}')

I139x33 = Parameter(name = 'I139x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM33*Ru36*tu33*complexconjugate(Rd33)',
                    texname = '\\text{I139x33}')

I139x36 = Parameter(name = 'I139x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM33*Ru66*tu33*complexconjugate(Rd33)',
                    texname = '\\text{I139x36}')

I139x41 = Parameter(name = 'I139x41',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM11*Ru14*tu11*complexconjugate(Rd41)',
                    texname = '\\text{I139x41}')

I139x44 = Parameter(name = 'I139x44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM11*Ru44*tu11*complexconjugate(Rd41)',
                    texname = '\\text{I139x44}')

I139x52 = Parameter(name = 'I139x52',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM22*Ru25*tu22*complexconjugate(Rd52)',
                    texname = '\\text{I139x52}')

I139x55 = Parameter(name = 'I139x55',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM22*Ru55*tu22*complexconjugate(Rd52)',
                    texname = '\\text{I139x55}')

I139x63 = Parameter(name = 'I139x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM33*Ru36*tu33*complexconjugate(Rd63)',
                    texname = '\\text{I139x63}')

I139x66 = Parameter(name = 'I139x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM33*Ru66*tu33*complexconjugate(Rd63)',
                    texname = '\\text{I139x66}')

I14x11 = Parameter(name = 'I14x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd14*yd11',
                   texname = '\\text{I14x11}')

I14x14 = Parameter(name = 'I14x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd44*yd11',
                   texname = '\\text{I14x14}')

I14x22 = Parameter(name = 'I14x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd25*yd22',
                   texname = '\\text{I14x22}')

I14x25 = Parameter(name = 'I14x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd55*yd22',
                   texname = '\\text{I14x25}')

I14x33 = Parameter(name = 'I14x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd36*yd33',
                   texname = '\\text{I14x33}')

I14x36 = Parameter(name = 'I14x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd66*yd33',
                   texname = '\\text{I14x36}')

I140x11 = Parameter(name = 'I140x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM11*Ru11*yd11*complexconjugate(Rd11)*complexconjugate(yd11)',
                    texname = '\\text{I140x11}')

I140x14 = Parameter(name = 'I140x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM11*Ru41*yd11*complexconjugate(Rd11)*complexconjugate(yd11)',
                    texname = '\\text{I140x14}')

I140x22 = Parameter(name = 'I140x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM22*Ru22*yd22*complexconjugate(Rd22)*complexconjugate(yd22)',
                    texname = '\\text{I140x22}')

I140x25 = Parameter(name = 'I140x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM22*Ru52*yd22*complexconjugate(Rd22)*complexconjugate(yd22)',
                    texname = '\\text{I140x25}')

I140x33 = Parameter(name = 'I140x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM33*Ru33*yd33*complexconjugate(Rd33)*complexconjugate(yd33)',
                    texname = '\\text{I140x33}')

I140x36 = Parameter(name = 'I140x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM33*Ru63*yd33*complexconjugate(Rd33)*complexconjugate(yd33)',
                    texname = '\\text{I140x36}')

I140x41 = Parameter(name = 'I140x41',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM11*Ru11*yd11*complexconjugate(Rd41)*complexconjugate(yd11)',
                    texname = '\\text{I140x41}')

I140x44 = Parameter(name = 'I140x44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM11*Ru41*yd11*complexconjugate(Rd41)*complexconjugate(yd11)',
                    texname = '\\text{I140x44}')

I140x52 = Parameter(name = 'I140x52',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM22*Ru22*yd22*complexconjugate(Rd52)*complexconjugate(yd22)',
                    texname = '\\text{I140x52}')

I140x55 = Parameter(name = 'I140x55',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM22*Ru52*yd22*complexconjugate(Rd52)*complexconjugate(yd22)',
                    texname = '\\text{I140x55}')

I140x63 = Parameter(name = 'I140x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM33*Ru33*yd33*complexconjugate(Rd63)*complexconjugate(yd33)',
                    texname = '\\text{I140x63}')

I140x66 = Parameter(name = 'I140x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM33*Ru63*yd33*complexconjugate(Rd63)*complexconjugate(yd33)',
                    texname = '\\text{I140x66}')

I141x11 = Parameter(name = 'I141x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM11*Ru14*yu11*complexconjugate(Rd11)',
                    texname = '\\text{I141x11}')

I141x14 = Parameter(name = 'I141x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM11*Ru44*yu11*complexconjugate(Rd11)',
                    texname = '\\text{I141x14}')

I141x22 = Parameter(name = 'I141x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM22*Ru25*yu22*complexconjugate(Rd22)',
                    texname = '\\text{I141x22}')

I141x25 = Parameter(name = 'I141x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM22*Ru55*yu22*complexconjugate(Rd22)',
                    texname = '\\text{I141x25}')

I141x33 = Parameter(name = 'I141x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM33*Ru36*yu33*complexconjugate(Rd33)',
                    texname = '\\text{I141x33}')

I141x36 = Parameter(name = 'I141x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM33*Ru66*yu33*complexconjugate(Rd33)',
                    texname = '\\text{I141x36}')

I141x41 = Parameter(name = 'I141x41',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM11*Ru14*yu11*complexconjugate(Rd41)',
                    texname = '\\text{I141x41}')

I141x44 = Parameter(name = 'I141x44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM11*Ru44*yu11*complexconjugate(Rd41)',
                    texname = '\\text{I141x44}')

I141x52 = Parameter(name = 'I141x52',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM22*Ru25*yu22*complexconjugate(Rd52)',
                    texname = '\\text{I141x52}')

I141x55 = Parameter(name = 'I141x55',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM22*Ru55*yu22*complexconjugate(Rd52)',
                    texname = '\\text{I141x55}')

I141x63 = Parameter(name = 'I141x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM33*Ru36*yu33*complexconjugate(Rd63)',
                    texname = '\\text{I141x63}')

I141x66 = Parameter(name = 'I141x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM33*Ru66*yu33*complexconjugate(Rd63)',
                    texname = '\\text{I141x66}')

I142x11 = Parameter(name = 'I142x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM11*Ru11*yu11*complexconjugate(Rd11)*complexconjugate(yu11)',
                    texname = '\\text{I142x11}')

I142x14 = Parameter(name = 'I142x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM11*Ru41*yu11*complexconjugate(Rd11)*complexconjugate(yu11)',
                    texname = '\\text{I142x14}')

I142x22 = Parameter(name = 'I142x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM22*Ru22*yu22*complexconjugate(Rd22)*complexconjugate(yu22)',
                    texname = '\\text{I142x22}')

I142x25 = Parameter(name = 'I142x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM22*Ru52*yu22*complexconjugate(Rd22)*complexconjugate(yu22)',
                    texname = '\\text{I142x25}')

I142x33 = Parameter(name = 'I142x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM33*Ru33*yu33*complexconjugate(Rd33)*complexconjugate(yu33)',
                    texname = '\\text{I142x33}')

I142x36 = Parameter(name = 'I142x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM33*Ru63*yu33*complexconjugate(Rd33)*complexconjugate(yu33)',
                    texname = '\\text{I142x36}')

I142x41 = Parameter(name = 'I142x41',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM11*Ru11*yu11*complexconjugate(Rd41)*complexconjugate(yu11)',
                    texname = '\\text{I142x41}')

I142x44 = Parameter(name = 'I142x44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM11*Ru41*yu11*complexconjugate(Rd41)*complexconjugate(yu11)',
                    texname = '\\text{I142x44}')

I142x52 = Parameter(name = 'I142x52',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM22*Ru22*yu22*complexconjugate(Rd52)*complexconjugate(yu22)',
                    texname = '\\text{I142x52}')

I142x55 = Parameter(name = 'I142x55',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM22*Ru52*yu22*complexconjugate(Rd52)*complexconjugate(yu22)',
                    texname = '\\text{I142x55}')

I142x63 = Parameter(name = 'I142x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM33*Ru33*yu33*complexconjugate(Rd63)*complexconjugate(yu33)',
                    texname = '\\text{I142x63}')

I142x66 = Parameter(name = 'I142x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM33*Ru63*yu33*complexconjugate(Rd63)*complexconjugate(yu33)',
                    texname = '\\text{I142x66}')

I143x11 = Parameter(name = 'I143x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM11*Ru14*yu11*complexconjugate(Rd14)*complexconjugate(yd11)',
                    texname = '\\text{I143x11}')

I143x14 = Parameter(name = 'I143x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM11*Ru44*yu11*complexconjugate(Rd14)*complexconjugate(yd11)',
                    texname = '\\text{I143x14}')

I143x22 = Parameter(name = 'I143x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM22*Ru25*yu22*complexconjugate(Rd25)*complexconjugate(yd22)',
                    texname = '\\text{I143x22}')

I143x25 = Parameter(name = 'I143x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM22*Ru55*yu22*complexconjugate(Rd25)*complexconjugate(yd22)',
                    texname = '\\text{I143x25}')

I143x33 = Parameter(name = 'I143x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM33*Ru36*yu33*complexconjugate(Rd36)*complexconjugate(yd33)',
                    texname = '\\text{I143x33}')

I143x36 = Parameter(name = 'I143x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM33*Ru66*yu33*complexconjugate(Rd36)*complexconjugate(yd33)',
                    texname = '\\text{I143x36}')

I143x41 = Parameter(name = 'I143x41',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM11*Ru14*yu11*complexconjugate(Rd44)*complexconjugate(yd11)',
                    texname = '\\text{I143x41}')

I143x44 = Parameter(name = 'I143x44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM11*Ru44*yu11*complexconjugate(Rd44)*complexconjugate(yd11)',
                    texname = '\\text{I143x44}')

I143x52 = Parameter(name = 'I143x52',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM22*Ru25*yu22*complexconjugate(Rd55)*complexconjugate(yd22)',
                    texname = '\\text{I143x52}')

I143x55 = Parameter(name = 'I143x55',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM22*Ru55*yu22*complexconjugate(Rd55)*complexconjugate(yd22)',
                    texname = '\\text{I143x55}')

I143x63 = Parameter(name = 'I143x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM33*Ru36*yu33*complexconjugate(Rd66)*complexconjugate(yd33)',
                    texname = '\\text{I143x63}')

I143x66 = Parameter(name = 'I143x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM33*Ru66*yu33*complexconjugate(Rd66)*complexconjugate(yd33)',
                    texname = '\\text{I143x66}')

I144x11 = Parameter(name = 'I144x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM11*Ru11*complexconjugate(Rd11)',
                    texname = '\\text{I144x11}')

I144x14 = Parameter(name = 'I144x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM11*Ru41*complexconjugate(Rd11)',
                    texname = '\\text{I144x14}')

I144x22 = Parameter(name = 'I144x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM22*Ru22*complexconjugate(Rd22)',
                    texname = '\\text{I144x22}')

I144x25 = Parameter(name = 'I144x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM22*Ru52*complexconjugate(Rd22)',
                    texname = '\\text{I144x25}')

I144x33 = Parameter(name = 'I144x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM33*Ru33*complexconjugate(Rd33)',
                    texname = '\\text{I144x33}')

I144x36 = Parameter(name = 'I144x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM33*Ru63*complexconjugate(Rd33)',
                    texname = '\\text{I144x36}')

I144x41 = Parameter(name = 'I144x41',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM11*Ru11*complexconjugate(Rd41)',
                    texname = '\\text{I144x41}')

I144x44 = Parameter(name = 'I144x44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM11*Ru41*complexconjugate(Rd41)',
                    texname = '\\text{I144x44}')

I144x52 = Parameter(name = 'I144x52',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM22*Ru22*complexconjugate(Rd52)',
                    texname = '\\text{I144x52}')

I144x55 = Parameter(name = 'I144x55',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM22*Ru52*complexconjugate(Rd52)',
                    texname = '\\text{I144x55}')

I144x63 = Parameter(name = 'I144x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM33*Ru33*complexconjugate(Rd63)',
                    texname = '\\text{I144x63}')

I144x66 = Parameter(name = 'I144x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM33*Ru63*complexconjugate(Rd63)',
                    texname = '\\text{I144x66}')

I145x11 = Parameter(name = 'I145x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM11*Ru11*yd11*complexconjugate(Rd11)*complexconjugate(yd11)',
                    texname = '\\text{I145x11}')

I145x14 = Parameter(name = 'I145x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM11*Ru41*yd11*complexconjugate(Rd11)*complexconjugate(yd11)',
                    texname = '\\text{I145x14}')

I145x22 = Parameter(name = 'I145x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM22*Ru22*yd22*complexconjugate(Rd22)*complexconjugate(yd22)',
                    texname = '\\text{I145x22}')

I145x25 = Parameter(name = 'I145x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM22*Ru52*yd22*complexconjugate(Rd22)*complexconjugate(yd22)',
                    texname = '\\text{I145x25}')

I145x33 = Parameter(name = 'I145x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM33*Ru33*yd33*complexconjugate(Rd33)*complexconjugate(yd33)',
                    texname = '\\text{I145x33}')

I145x36 = Parameter(name = 'I145x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM33*Ru63*yd33*complexconjugate(Rd33)*complexconjugate(yd33)',
                    texname = '\\text{I145x36}')

I145x41 = Parameter(name = 'I145x41',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM11*Ru11*yd11*complexconjugate(Rd41)*complexconjugate(yd11)',
                    texname = '\\text{I145x41}')

I145x44 = Parameter(name = 'I145x44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM11*Ru41*yd11*complexconjugate(Rd41)*complexconjugate(yd11)',
                    texname = '\\text{I145x44}')

I145x52 = Parameter(name = 'I145x52',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM22*Ru22*yd22*complexconjugate(Rd52)*complexconjugate(yd22)',
                    texname = '\\text{I145x52}')

I145x55 = Parameter(name = 'I145x55',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM22*Ru52*yd22*complexconjugate(Rd52)*complexconjugate(yd22)',
                    texname = '\\text{I145x55}')

I145x63 = Parameter(name = 'I145x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM33*Ru33*yd33*complexconjugate(Rd63)*complexconjugate(yd33)',
                    texname = '\\text{I145x63}')

I145x66 = Parameter(name = 'I145x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM33*Ru63*yd33*complexconjugate(Rd63)*complexconjugate(yd33)',
                    texname = '\\text{I145x66}')

I146x11 = Parameter(name = 'I146x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM11*Ru11*yu11*complexconjugate(Rd11)*complexconjugate(yu11)',
                    texname = '\\text{I146x11}')

I146x14 = Parameter(name = 'I146x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM11*Ru41*yu11*complexconjugate(Rd11)*complexconjugate(yu11)',
                    texname = '\\text{I146x14}')

I146x22 = Parameter(name = 'I146x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM22*Ru22*yu22*complexconjugate(Rd22)*complexconjugate(yu22)',
                    texname = '\\text{I146x22}')

I146x25 = Parameter(name = 'I146x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM22*Ru52*yu22*complexconjugate(Rd22)*complexconjugate(yu22)',
                    texname = '\\text{I146x25}')

I146x33 = Parameter(name = 'I146x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM33*Ru33*yu33*complexconjugate(Rd33)*complexconjugate(yu33)',
                    texname = '\\text{I146x33}')

I146x36 = Parameter(name = 'I146x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM33*Ru63*yu33*complexconjugate(Rd33)*complexconjugate(yu33)',
                    texname = '\\text{I146x36}')

I146x41 = Parameter(name = 'I146x41',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM11*Ru11*yu11*complexconjugate(Rd41)*complexconjugate(yu11)',
                    texname = '\\text{I146x41}')

I146x44 = Parameter(name = 'I146x44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM11*Ru41*yu11*complexconjugate(Rd41)*complexconjugate(yu11)',
                    texname = '\\text{I146x44}')

I146x52 = Parameter(name = 'I146x52',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM22*Ru22*yu22*complexconjugate(Rd52)*complexconjugate(yu22)',
                    texname = '\\text{I146x52}')

I146x55 = Parameter(name = 'I146x55',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM22*Ru52*yu22*complexconjugate(Rd52)*complexconjugate(yu22)',
                    texname = '\\text{I146x55}')

I146x63 = Parameter(name = 'I146x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM33*Ru33*yu33*complexconjugate(Rd63)*complexconjugate(yu33)',
                    texname = '\\text{I146x63}')

I146x66 = Parameter(name = 'I146x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM33*Ru63*yu33*complexconjugate(Rd63)*complexconjugate(yu33)',
                    texname = '\\text{I146x66}')

I147x11 = Parameter(name = 'I147x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM11*Ru14*yu11*complexconjugate(Rd14)*complexconjugate(yd11)',
                    texname = '\\text{I147x11}')

I147x14 = Parameter(name = 'I147x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM11*Ru44*yu11*complexconjugate(Rd14)*complexconjugate(yd11)',
                    texname = '\\text{I147x14}')

I147x22 = Parameter(name = 'I147x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM22*Ru25*yu22*complexconjugate(Rd25)*complexconjugate(yd22)',
                    texname = '\\text{I147x22}')

I147x25 = Parameter(name = 'I147x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM22*Ru55*yu22*complexconjugate(Rd25)*complexconjugate(yd22)',
                    texname = '\\text{I147x25}')

I147x33 = Parameter(name = 'I147x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM33*Ru36*yu33*complexconjugate(Rd36)*complexconjugate(yd33)',
                    texname = '\\text{I147x33}')

I147x36 = Parameter(name = 'I147x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM33*Ru66*yu33*complexconjugate(Rd36)*complexconjugate(yd33)',
                    texname = '\\text{I147x36}')

I147x41 = Parameter(name = 'I147x41',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM11*Ru14*yu11*complexconjugate(Rd44)*complexconjugate(yd11)',
                    texname = '\\text{I147x41}')

I147x44 = Parameter(name = 'I147x44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM11*Ru44*yu11*complexconjugate(Rd44)*complexconjugate(yd11)',
                    texname = '\\text{I147x44}')

I147x52 = Parameter(name = 'I147x52',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM22*Ru25*yu22*complexconjugate(Rd55)*complexconjugate(yd22)',
                    texname = '\\text{I147x52}')

I147x55 = Parameter(name = 'I147x55',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM22*Ru55*yu22*complexconjugate(Rd55)*complexconjugate(yd22)',
                    texname = '\\text{I147x55}')

I147x63 = Parameter(name = 'I147x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM33*Ru36*yu33*complexconjugate(Rd66)*complexconjugate(yd33)',
                    texname = '\\text{I147x63}')

I147x66 = Parameter(name = 'I147x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM33*Ru66*yu33*complexconjugate(Rd66)*complexconjugate(yd33)',
                    texname = '\\text{I147x66}')

I148x11 = Parameter(name = 'I148x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru11*complexconjugate(Ru11)',
                    texname = '\\text{I148x11}')

I148x14 = Parameter(name = 'I148x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru41*complexconjugate(Ru11)',
                    texname = '\\text{I148x14}')

I148x22 = Parameter(name = 'I148x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru22*complexconjugate(Ru22)',
                    texname = '\\text{I148x22}')

I148x25 = Parameter(name = 'I148x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru52*complexconjugate(Ru22)',
                    texname = '\\text{I148x25}')

I148x33 = Parameter(name = 'I148x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru33*complexconjugate(Ru33)',
                    texname = '\\text{I148x33}')

I148x36 = Parameter(name = 'I148x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru63*complexconjugate(Ru33)',
                    texname = '\\text{I148x36}')

I148x41 = Parameter(name = 'I148x41',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru11*complexconjugate(Ru41)',
                    texname = '\\text{I148x41}')

I148x44 = Parameter(name = 'I148x44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru41*complexconjugate(Ru41)',
                    texname = '\\text{I148x44}')

I148x52 = Parameter(name = 'I148x52',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru22*complexconjugate(Ru52)',
                    texname = '\\text{I148x52}')

I148x55 = Parameter(name = 'I148x55',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru52*complexconjugate(Ru52)',
                    texname = '\\text{I148x55}')

I148x63 = Parameter(name = 'I148x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru33*complexconjugate(Ru63)',
                    texname = '\\text{I148x63}')

I148x66 = Parameter(name = 'I148x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru63*complexconjugate(Ru63)',
                    texname = '\\text{I148x66}')

I149x11 = Parameter(name = 'I149x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru14*complexconjugate(Ru14)',
                    texname = '\\text{I149x11}')

I149x14 = Parameter(name = 'I149x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru44*complexconjugate(Ru14)',
                    texname = '\\text{I149x14}')

I149x22 = Parameter(name = 'I149x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru25*complexconjugate(Ru25)',
                    texname = '\\text{I149x22}')

I149x25 = Parameter(name = 'I149x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru55*complexconjugate(Ru25)',
                    texname = '\\text{I149x25}')

I149x33 = Parameter(name = 'I149x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru36*complexconjugate(Ru36)',
                    texname = '\\text{I149x33}')

I149x36 = Parameter(name = 'I149x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru66*complexconjugate(Ru36)',
                    texname = '\\text{I149x36}')

I149x41 = Parameter(name = 'I149x41',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru14*complexconjugate(Ru44)',
                    texname = '\\text{I149x41}')

I149x44 = Parameter(name = 'I149x44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru44*complexconjugate(Ru44)',
                    texname = '\\text{I149x44}')

I149x52 = Parameter(name = 'I149x52',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru25*complexconjugate(Ru55)',
                    texname = '\\text{I149x52}')

I149x55 = Parameter(name = 'I149x55',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru55*complexconjugate(Ru55)',
                    texname = '\\text{I149x55}')

I149x63 = Parameter(name = 'I149x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru36*complexconjugate(Ru66)',
                    texname = '\\text{I149x63}')

I149x66 = Parameter(name = 'I149x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru66*complexconjugate(Ru66)',
                    texname = '\\text{I149x66}')

I15x11 = Parameter(name = 'I15x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd11*complexconjugate(Rd11)',
                   texname = '\\text{I15x11}')

I15x14 = Parameter(name = 'I15x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd41*complexconjugate(Rd11)',
                   texname = '\\text{I15x14}')

I15x22 = Parameter(name = 'I15x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd22*complexconjugate(Rd22)',
                   texname = '\\text{I15x22}')

I15x25 = Parameter(name = 'I15x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd52*complexconjugate(Rd22)',
                   texname = '\\text{I15x25}')

I15x33 = Parameter(name = 'I15x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd33*complexconjugate(Rd33)',
                   texname = '\\text{I15x33}')

I15x36 = Parameter(name = 'I15x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd63*complexconjugate(Rd33)',
                   texname = '\\text{I15x36}')

I15x41 = Parameter(name = 'I15x41',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd11*complexconjugate(Rd41)',
                   texname = '\\text{I15x41}')

I15x44 = Parameter(name = 'I15x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd41*complexconjugate(Rd41)',
                   texname = '\\text{I15x44}')

I15x52 = Parameter(name = 'I15x52',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd22*complexconjugate(Rd52)',
                   texname = '\\text{I15x52}')

I15x55 = Parameter(name = 'I15x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd52*complexconjugate(Rd52)',
                   texname = '\\text{I15x55}')

I15x63 = Parameter(name = 'I15x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd33*complexconjugate(Rd63)',
                   texname = '\\text{I15x63}')

I15x66 = Parameter(name = 'I15x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd63*complexconjugate(Rd63)',
                   texname = '\\text{I15x66}')

I150x11 = Parameter(name = 'I150x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru11*complexconjugate(Ru14)*complexconjugate(yu11)',
                    texname = '\\text{I150x11}')

I150x14 = Parameter(name = 'I150x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru41*complexconjugate(Ru14)*complexconjugate(yu11)',
                    texname = '\\text{I150x14}')

I150x22 = Parameter(name = 'I150x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru22*complexconjugate(Ru25)*complexconjugate(yu22)',
                    texname = '\\text{I150x22}')

I150x25 = Parameter(name = 'I150x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru52*complexconjugate(Ru25)*complexconjugate(yu22)',
                    texname = '\\text{I150x25}')

I150x33 = Parameter(name = 'I150x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru33*complexconjugate(Ru36)*complexconjugate(yu33)',
                    texname = '\\text{I150x33}')

I150x36 = Parameter(name = 'I150x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru63*complexconjugate(Ru36)*complexconjugate(yu33)',
                    texname = '\\text{I150x36}')

I150x41 = Parameter(name = 'I150x41',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru11*complexconjugate(Ru44)*complexconjugate(yu11)',
                    texname = '\\text{I150x41}')

I150x44 = Parameter(name = 'I150x44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru41*complexconjugate(Ru44)*complexconjugate(yu11)',
                    texname = '\\text{I150x44}')

I150x52 = Parameter(name = 'I150x52',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru22*complexconjugate(Ru55)*complexconjugate(yu22)',
                    texname = '\\text{I150x52}')

I150x55 = Parameter(name = 'I150x55',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru52*complexconjugate(Ru55)*complexconjugate(yu22)',
                    texname = '\\text{I150x55}')

I150x63 = Parameter(name = 'I150x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru33*complexconjugate(Ru66)*complexconjugate(yu33)',
                    texname = '\\text{I150x63}')

I150x66 = Parameter(name = 'I150x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru63*complexconjugate(Ru66)*complexconjugate(yu33)',
                    texname = '\\text{I150x66}')

I151x11 = Parameter(name = 'I151x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru11*complexconjugate(Ru14)*complexconjugate(tu11)',
                    texname = '\\text{I151x11}')

I151x14 = Parameter(name = 'I151x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru41*complexconjugate(Ru14)*complexconjugate(tu11)',
                    texname = '\\text{I151x14}')

I151x22 = Parameter(name = 'I151x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru22*complexconjugate(Ru25)*complexconjugate(tu22)',
                    texname = '\\text{I151x22}')

I151x25 = Parameter(name = 'I151x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru52*complexconjugate(Ru25)*complexconjugate(tu22)',
                    texname = '\\text{I151x25}')

I151x33 = Parameter(name = 'I151x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru33*complexconjugate(Ru36)*complexconjugate(tu33)',
                    texname = '\\text{I151x33}')

I151x36 = Parameter(name = 'I151x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru63*complexconjugate(Ru36)*complexconjugate(tu33)',
                    texname = '\\text{I151x36}')

I151x41 = Parameter(name = 'I151x41',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru11*complexconjugate(Ru44)*complexconjugate(tu11)',
                    texname = '\\text{I151x41}')

I151x44 = Parameter(name = 'I151x44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru41*complexconjugate(Ru44)*complexconjugate(tu11)',
                    texname = '\\text{I151x44}')

I151x52 = Parameter(name = 'I151x52',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru22*complexconjugate(Ru55)*complexconjugate(tu22)',
                    texname = '\\text{I151x52}')

I151x55 = Parameter(name = 'I151x55',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru52*complexconjugate(Ru55)*complexconjugate(tu22)',
                    texname = '\\text{I151x55}')

I151x63 = Parameter(name = 'I151x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru33*complexconjugate(Ru66)*complexconjugate(tu33)',
                    texname = '\\text{I151x63}')

I151x66 = Parameter(name = 'I151x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru63*complexconjugate(Ru66)*complexconjugate(tu33)',
                    texname = '\\text{I151x66}')

I152x11 = Parameter(name = 'I152x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru14*tu11*complexconjugate(Ru11)',
                    texname = '\\text{I152x11}')

I152x14 = Parameter(name = 'I152x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru44*tu11*complexconjugate(Ru11)',
                    texname = '\\text{I152x14}')

I152x22 = Parameter(name = 'I152x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru25*tu22*complexconjugate(Ru22)',
                    texname = '\\text{I152x22}')

I152x25 = Parameter(name = 'I152x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru55*tu22*complexconjugate(Ru22)',
                    texname = '\\text{I152x25}')

I152x33 = Parameter(name = 'I152x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru36*tu33*complexconjugate(Ru33)',
                    texname = '\\text{I152x33}')

I152x36 = Parameter(name = 'I152x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru66*tu33*complexconjugate(Ru33)',
                    texname = '\\text{I152x36}')

I152x41 = Parameter(name = 'I152x41',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru14*tu11*complexconjugate(Ru41)',
                    texname = '\\text{I152x41}')

I152x44 = Parameter(name = 'I152x44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru44*tu11*complexconjugate(Ru41)',
                    texname = '\\text{I152x44}')

I152x52 = Parameter(name = 'I152x52',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru25*tu22*complexconjugate(Ru52)',
                    texname = '\\text{I152x52}')

I152x55 = Parameter(name = 'I152x55',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru55*tu22*complexconjugate(Ru52)',
                    texname = '\\text{I152x55}')

I152x63 = Parameter(name = 'I152x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru36*tu33*complexconjugate(Ru63)',
                    texname = '\\text{I152x63}')

I152x66 = Parameter(name = 'I152x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru66*tu33*complexconjugate(Ru63)',
                    texname = '\\text{I152x66}')

I153x11 = Parameter(name = 'I153x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru14*yu11*complexconjugate(Ru11)',
                    texname = '\\text{I153x11}')

I153x14 = Parameter(name = 'I153x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru44*yu11*complexconjugate(Ru11)',
                    texname = '\\text{I153x14}')

I153x22 = Parameter(name = 'I153x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru25*yu22*complexconjugate(Ru22)',
                    texname = '\\text{I153x22}')

I153x25 = Parameter(name = 'I153x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru55*yu22*complexconjugate(Ru22)',
                    texname = '\\text{I153x25}')

I153x33 = Parameter(name = 'I153x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru36*yu33*complexconjugate(Ru33)',
                    texname = '\\text{I153x33}')

I153x36 = Parameter(name = 'I153x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru66*yu33*complexconjugate(Ru33)',
                    texname = '\\text{I153x36}')

I153x41 = Parameter(name = 'I153x41',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru14*yu11*complexconjugate(Ru41)',
                    texname = '\\text{I153x41}')

I153x44 = Parameter(name = 'I153x44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru44*yu11*complexconjugate(Ru41)',
                    texname = '\\text{I153x44}')

I153x52 = Parameter(name = 'I153x52',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru25*yu22*complexconjugate(Ru52)',
                    texname = '\\text{I153x52}')

I153x55 = Parameter(name = 'I153x55',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru55*yu22*complexconjugate(Ru52)',
                    texname = '\\text{I153x55}')

I153x63 = Parameter(name = 'I153x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru36*yu33*complexconjugate(Ru63)',
                    texname = '\\text{I153x63}')

I153x66 = Parameter(name = 'I153x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru66*yu33*complexconjugate(Ru63)',
                    texname = '\\text{I153x66}')

I154x11 = Parameter(name = 'I154x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru11*yu11*complexconjugate(Ru11)*complexconjugate(yu11)',
                    texname = '\\text{I154x11}')

I154x14 = Parameter(name = 'I154x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru41*yu11*complexconjugate(Ru11)*complexconjugate(yu11)',
                    texname = '\\text{I154x14}')

I154x22 = Parameter(name = 'I154x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru22*yu22*complexconjugate(Ru22)*complexconjugate(yu22)',
                    texname = '\\text{I154x22}')

I154x25 = Parameter(name = 'I154x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru52*yu22*complexconjugate(Ru22)*complexconjugate(yu22)',
                    texname = '\\text{I154x25}')

I154x33 = Parameter(name = 'I154x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru33*yu33*complexconjugate(Ru33)*complexconjugate(yu33)',
                    texname = '\\text{I154x33}')

I154x36 = Parameter(name = 'I154x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru63*yu33*complexconjugate(Ru33)*complexconjugate(yu33)',
                    texname = '\\text{I154x36}')

I154x41 = Parameter(name = 'I154x41',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru11*yu11*complexconjugate(Ru41)*complexconjugate(yu11)',
                    texname = '\\text{I154x41}')

I154x44 = Parameter(name = 'I154x44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru41*yu11*complexconjugate(Ru41)*complexconjugate(yu11)',
                    texname = '\\text{I154x44}')

I154x52 = Parameter(name = 'I154x52',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru22*yu22*complexconjugate(Ru52)*complexconjugate(yu22)',
                    texname = '\\text{I154x52}')

I154x55 = Parameter(name = 'I154x55',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru52*yu22*complexconjugate(Ru52)*complexconjugate(yu22)',
                    texname = '\\text{I154x55}')

I154x63 = Parameter(name = 'I154x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru33*yu33*complexconjugate(Ru63)*complexconjugate(yu33)',
                    texname = '\\text{I154x63}')

I154x66 = Parameter(name = 'I154x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru63*yu33*complexconjugate(Ru63)*complexconjugate(yu33)',
                    texname = '\\text{I154x66}')

I155x11 = Parameter(name = 'I155x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru14*yu11*complexconjugate(Ru14)*complexconjugate(yu11)',
                    texname = '\\text{I155x11}')

I155x14 = Parameter(name = 'I155x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru44*yu11*complexconjugate(Ru14)*complexconjugate(yu11)',
                    texname = '\\text{I155x14}')

I155x22 = Parameter(name = 'I155x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru25*yu22*complexconjugate(Ru25)*complexconjugate(yu22)',
                    texname = '\\text{I155x22}')

I155x25 = Parameter(name = 'I155x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru55*yu22*complexconjugate(Ru25)*complexconjugate(yu22)',
                    texname = '\\text{I155x25}')

I155x33 = Parameter(name = 'I155x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru36*yu33*complexconjugate(Ru36)*complexconjugate(yu33)',
                    texname = '\\text{I155x33}')

I155x36 = Parameter(name = 'I155x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru66*yu33*complexconjugate(Ru36)*complexconjugate(yu33)',
                    texname = '\\text{I155x36}')

I155x41 = Parameter(name = 'I155x41',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru14*yu11*complexconjugate(Ru44)*complexconjugate(yu11)',
                    texname = '\\text{I155x41}')

I155x44 = Parameter(name = 'I155x44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru44*yu11*complexconjugate(Ru44)*complexconjugate(yu11)',
                    texname = '\\text{I155x44}')

I155x52 = Parameter(name = 'I155x52',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru25*yu22*complexconjugate(Ru55)*complexconjugate(yu22)',
                    texname = '\\text{I155x52}')

I155x55 = Parameter(name = 'I155x55',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru55*yu22*complexconjugate(Ru55)*complexconjugate(yu22)',
                    texname = '\\text{I155x55}')

I155x63 = Parameter(name = 'I155x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru36*yu33*complexconjugate(Ru66)*complexconjugate(yu33)',
                    texname = '\\text{I155x63}')

I155x66 = Parameter(name = 'I155x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru66*yu33*complexconjugate(Ru66)*complexconjugate(yu33)',
                    texname = '\\text{I155x66}')

I156x11 = Parameter(name = 'I156x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru11*yu11*complexconjugate(Ru11)*complexconjugate(yu11)',
                    texname = '\\text{I156x11}')

I156x14 = Parameter(name = 'I156x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru41*yu11*complexconjugate(Ru11)*complexconjugate(yu11)',
                    texname = '\\text{I156x14}')

I156x22 = Parameter(name = 'I156x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru22*yu22*complexconjugate(Ru22)*complexconjugate(yu22)',
                    texname = '\\text{I156x22}')

I156x25 = Parameter(name = 'I156x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru52*yu22*complexconjugate(Ru22)*complexconjugate(yu22)',
                    texname = '\\text{I156x25}')

I156x33 = Parameter(name = 'I156x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru33*yu33*complexconjugate(Ru33)*complexconjugate(yu33)',
                    texname = '\\text{I156x33}')

I156x36 = Parameter(name = 'I156x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru63*yu33*complexconjugate(Ru33)*complexconjugate(yu33)',
                    texname = '\\text{I156x36}')

I156x41 = Parameter(name = 'I156x41',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru11*yu11*complexconjugate(Ru41)*complexconjugate(yu11)',
                    texname = '\\text{I156x41}')

I156x44 = Parameter(name = 'I156x44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru41*yu11*complexconjugate(Ru41)*complexconjugate(yu11)',
                    texname = '\\text{I156x44}')

I156x52 = Parameter(name = 'I156x52',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru22*yu22*complexconjugate(Ru52)*complexconjugate(yu22)',
                    texname = '\\text{I156x52}')

I156x55 = Parameter(name = 'I156x55',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru52*yu22*complexconjugate(Ru52)*complexconjugate(yu22)',
                    texname = '\\text{I156x55}')

I156x63 = Parameter(name = 'I156x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru33*yu33*complexconjugate(Ru63)*complexconjugate(yu33)',
                    texname = '\\text{I156x63}')

I156x66 = Parameter(name = 'I156x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru63*yu33*complexconjugate(Ru63)*complexconjugate(yu33)',
                    texname = '\\text{I156x66}')

I157x11 = Parameter(name = 'I157x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru14*yu11*complexconjugate(Ru14)*complexconjugate(yu11)',
                    texname = '\\text{I157x11}')

I157x14 = Parameter(name = 'I157x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru44*yu11*complexconjugate(Ru14)*complexconjugate(yu11)',
                    texname = '\\text{I157x14}')

I157x22 = Parameter(name = 'I157x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru25*yu22*complexconjugate(Ru25)*complexconjugate(yu22)',
                    texname = '\\text{I157x22}')

I157x25 = Parameter(name = 'I157x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru55*yu22*complexconjugate(Ru25)*complexconjugate(yu22)',
                    texname = '\\text{I157x25}')

I157x33 = Parameter(name = 'I157x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru36*yu33*complexconjugate(Ru36)*complexconjugate(yu33)',
                    texname = '\\text{I157x33}')

I157x36 = Parameter(name = 'I157x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru66*yu33*complexconjugate(Ru36)*complexconjugate(yu33)',
                    texname = '\\text{I157x36}')

I157x41 = Parameter(name = 'I157x41',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru14*yu11*complexconjugate(Ru44)*complexconjugate(yu11)',
                    texname = '\\text{I157x41}')

I157x44 = Parameter(name = 'I157x44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru44*yu11*complexconjugate(Ru44)*complexconjugate(yu11)',
                    texname = '\\text{I157x44}')

I157x52 = Parameter(name = 'I157x52',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru25*yu22*complexconjugate(Ru55)*complexconjugate(yu22)',
                    texname = '\\text{I157x52}')

I157x55 = Parameter(name = 'I157x55',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru55*yu22*complexconjugate(Ru55)*complexconjugate(yu22)',
                    texname = '\\text{I157x55}')

I157x63 = Parameter(name = 'I157x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru36*yu33*complexconjugate(Ru66)*complexconjugate(yu33)',
                    texname = '\\text{I157x63}')

I157x66 = Parameter(name = 'I157x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru66*yu33*complexconjugate(Ru66)*complexconjugate(yu33)',
                    texname = '\\text{I157x66}')

I158x11 = Parameter(name = 'I158x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM11*Ru11*yd11*complexconjugate(CKM11)*complexconjugate(Ru11)*complexconjugate(yd11)',
                    texname = '\\text{I158x11}')

I158x14 = Parameter(name = 'I158x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM11*Ru41*yd11*complexconjugate(CKM11)*complexconjugate(Ru11)*complexconjugate(yd11)',
                    texname = '\\text{I158x14}')

I158x22 = Parameter(name = 'I158x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM22*Ru22*yd22*complexconjugate(CKM22)*complexconjugate(Ru22)*complexconjugate(yd22)',
                    texname = '\\text{I158x22}')

I158x25 = Parameter(name = 'I158x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM22*Ru52*yd22*complexconjugate(CKM22)*complexconjugate(Ru22)*complexconjugate(yd22)',
                    texname = '\\text{I158x25}')

I158x33 = Parameter(name = 'I158x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM33*Ru33*yd33*complexconjugate(CKM33)*complexconjugate(Ru33)*complexconjugate(yd33)',
                    texname = '\\text{I158x33}')

I158x36 = Parameter(name = 'I158x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM33*Ru63*yd33*complexconjugate(CKM33)*complexconjugate(Ru33)*complexconjugate(yd33)',
                    texname = '\\text{I158x36}')

I158x41 = Parameter(name = 'I158x41',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM11*Ru11*yd11*complexconjugate(CKM11)*complexconjugate(Ru41)*complexconjugate(yd11)',
                    texname = '\\text{I158x41}')

I158x44 = Parameter(name = 'I158x44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM11*Ru41*yd11*complexconjugate(CKM11)*complexconjugate(Ru41)*complexconjugate(yd11)',
                    texname = '\\text{I158x44}')

I158x52 = Parameter(name = 'I158x52',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM22*Ru22*yd22*complexconjugate(CKM22)*complexconjugate(Ru52)*complexconjugate(yd22)',
                    texname = '\\text{I158x52}')

I158x55 = Parameter(name = 'I158x55',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM22*Ru52*yd22*complexconjugate(CKM22)*complexconjugate(Ru52)*complexconjugate(yd22)',
                    texname = '\\text{I158x55}')

I158x63 = Parameter(name = 'I158x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM33*Ru33*yd33*complexconjugate(CKM33)*complexconjugate(Ru63)*complexconjugate(yd33)',
                    texname = '\\text{I158x63}')

I158x66 = Parameter(name = 'I158x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM33*Ru63*yd33*complexconjugate(CKM33)*complexconjugate(Ru63)*complexconjugate(yd33)',
                    texname = '\\text{I158x66}')

I159x11 = Parameter(name = 'I159x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM11*Ru11*complexconjugate(Rd11)',
                    texname = '\\text{I159x11}')

I159x14 = Parameter(name = 'I159x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM11*Ru41*complexconjugate(Rd11)',
                    texname = '\\text{I159x14}')

I159x22 = Parameter(name = 'I159x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM22*Ru22*complexconjugate(Rd22)',
                    texname = '\\text{I159x22}')

I159x25 = Parameter(name = 'I159x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM22*Ru52*complexconjugate(Rd22)',
                    texname = '\\text{I159x25}')

I159x33 = Parameter(name = 'I159x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM33*Ru33*complexconjugate(Rd33)',
                    texname = '\\text{I159x33}')

I159x36 = Parameter(name = 'I159x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM33*Ru63*complexconjugate(Rd33)',
                    texname = '\\text{I159x36}')

I159x41 = Parameter(name = 'I159x41',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM11*Ru11*complexconjugate(Rd41)',
                    texname = '\\text{I159x41}')

I159x44 = Parameter(name = 'I159x44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM11*Ru41*complexconjugate(Rd41)',
                    texname = '\\text{I159x44}')

I159x52 = Parameter(name = 'I159x52',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM22*Ru22*complexconjugate(Rd52)',
                    texname = '\\text{I159x52}')

I159x55 = Parameter(name = 'I159x55',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM22*Ru52*complexconjugate(Rd52)',
                    texname = '\\text{I159x55}')

I159x63 = Parameter(name = 'I159x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM33*Ru33*complexconjugate(Rd63)',
                    texname = '\\text{I159x63}')

I159x66 = Parameter(name = 'I159x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM33*Ru63*complexconjugate(Rd63)',
                    texname = '\\text{I159x66}')

I16x11 = Parameter(name = 'I16x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd14*complexconjugate(Rd14)',
                   texname = '\\text{I16x11}')

I16x14 = Parameter(name = 'I16x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd44*complexconjugate(Rd14)',
                   texname = '\\text{I16x14}')

I16x22 = Parameter(name = 'I16x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd25*complexconjugate(Rd25)',
                   texname = '\\text{I16x22}')

I16x25 = Parameter(name = 'I16x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd55*complexconjugate(Rd25)',
                   texname = '\\text{I16x25}')

I16x33 = Parameter(name = 'I16x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd36*complexconjugate(Rd36)',
                   texname = '\\text{I16x33}')

I16x36 = Parameter(name = 'I16x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd66*complexconjugate(Rd36)',
                   texname = '\\text{I16x36}')

I16x41 = Parameter(name = 'I16x41',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd14*complexconjugate(Rd44)',
                   texname = '\\text{I16x41}')

I16x44 = Parameter(name = 'I16x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd44*complexconjugate(Rd44)',
                   texname = '\\text{I16x44}')

I16x52 = Parameter(name = 'I16x52',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd25*complexconjugate(Rd55)',
                   texname = '\\text{I16x52}')

I16x55 = Parameter(name = 'I16x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd55*complexconjugate(Rd55)',
                   texname = '\\text{I16x55}')

I16x63 = Parameter(name = 'I16x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd36*complexconjugate(Rd66)',
                   texname = '\\text{I16x63}')

I16x66 = Parameter(name = 'I16x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd66*complexconjugate(Rd66)',
                   texname = '\\text{I16x66}')

I160x11 = Parameter(name = 'I160x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM11*Ru11*complexconjugate(Rd14)*complexconjugate(yd11)',
                    texname = '\\text{I160x11}')

I160x14 = Parameter(name = 'I160x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM11*Ru41*complexconjugate(Rd14)*complexconjugate(yd11)',
                    texname = '\\text{I160x14}')

I160x22 = Parameter(name = 'I160x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM22*Ru22*complexconjugate(Rd25)*complexconjugate(yd22)',
                    texname = '\\text{I160x22}')

I160x25 = Parameter(name = 'I160x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM22*Ru52*complexconjugate(Rd25)*complexconjugate(yd22)',
                    texname = '\\text{I160x25}')

I160x33 = Parameter(name = 'I160x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM33*Ru33*complexconjugate(Rd36)*complexconjugate(yd33)',
                    texname = '\\text{I160x33}')

I160x36 = Parameter(name = 'I160x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM33*Ru63*complexconjugate(Rd36)*complexconjugate(yd33)',
                    texname = '\\text{I160x36}')

I160x41 = Parameter(name = 'I160x41',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM11*Ru11*complexconjugate(Rd44)*complexconjugate(yd11)',
                    texname = '\\text{I160x41}')

I160x44 = Parameter(name = 'I160x44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM11*Ru41*complexconjugate(Rd44)*complexconjugate(yd11)',
                    texname = '\\text{I160x44}')

I160x52 = Parameter(name = 'I160x52',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM22*Ru22*complexconjugate(Rd55)*complexconjugate(yd22)',
                    texname = '\\text{I160x52}')

I160x55 = Parameter(name = 'I160x55',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM22*Ru52*complexconjugate(Rd55)*complexconjugate(yd22)',
                    texname = '\\text{I160x55}')

I160x63 = Parameter(name = 'I160x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM33*Ru33*complexconjugate(Rd66)*complexconjugate(yd33)',
                    texname = '\\text{I160x63}')

I160x66 = Parameter(name = 'I160x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM33*Ru63*complexconjugate(Rd66)*complexconjugate(yd33)',
                    texname = '\\text{I160x66}')

I161x11 = Parameter(name = 'I161x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru11*complexconjugate(Ru11)',
                    texname = '\\text{I161x11}')

I161x14 = Parameter(name = 'I161x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru41*complexconjugate(Ru11)',
                    texname = '\\text{I161x14}')

I161x22 = Parameter(name = 'I161x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru22*complexconjugate(Ru22)',
                    texname = '\\text{I161x22}')

I161x25 = Parameter(name = 'I161x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru52*complexconjugate(Ru22)',
                    texname = '\\text{I161x25}')

I161x33 = Parameter(name = 'I161x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru33*complexconjugate(Ru33)',
                    texname = '\\text{I161x33}')

I161x36 = Parameter(name = 'I161x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru63*complexconjugate(Ru33)',
                    texname = '\\text{I161x36}')

I161x41 = Parameter(name = 'I161x41',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru11*complexconjugate(Ru41)',
                    texname = '\\text{I161x41}')

I161x44 = Parameter(name = 'I161x44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru41*complexconjugate(Ru41)',
                    texname = '\\text{I161x44}')

I161x52 = Parameter(name = 'I161x52',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru22*complexconjugate(Ru52)',
                    texname = '\\text{I161x52}')

I161x55 = Parameter(name = 'I161x55',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru52*complexconjugate(Ru52)',
                    texname = '\\text{I161x55}')

I161x63 = Parameter(name = 'I161x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru33*complexconjugate(Ru63)',
                    texname = '\\text{I161x63}')

I161x66 = Parameter(name = 'I161x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru63*complexconjugate(Ru63)',
                    texname = '\\text{I161x66}')

I162x11 = Parameter(name = 'I162x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru14*complexconjugate(Ru14)',
                    texname = '\\text{I162x11}')

I162x14 = Parameter(name = 'I162x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru44*complexconjugate(Ru14)',
                    texname = '\\text{I162x14}')

I162x22 = Parameter(name = 'I162x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru25*complexconjugate(Ru25)',
                    texname = '\\text{I162x22}')

I162x25 = Parameter(name = 'I162x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru55*complexconjugate(Ru25)',
                    texname = '\\text{I162x25}')

I162x33 = Parameter(name = 'I162x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru36*complexconjugate(Ru36)',
                    texname = '\\text{I162x33}')

I162x36 = Parameter(name = 'I162x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru66*complexconjugate(Ru36)',
                    texname = '\\text{I162x36}')

I162x41 = Parameter(name = 'I162x41',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru14*complexconjugate(Ru44)',
                    texname = '\\text{I162x41}')

I162x44 = Parameter(name = 'I162x44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru44*complexconjugate(Ru44)',
                    texname = '\\text{I162x44}')

I162x52 = Parameter(name = 'I162x52',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru25*complexconjugate(Ru55)',
                    texname = '\\text{I162x52}')

I162x55 = Parameter(name = 'I162x55',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru55*complexconjugate(Ru55)',
                    texname = '\\text{I162x55}')

I162x63 = Parameter(name = 'I162x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru36*complexconjugate(Ru66)',
                    texname = '\\text{I162x63}')

I162x66 = Parameter(name = 'I162x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru66*complexconjugate(Ru66)',
                    texname = '\\text{I162x66}')

I163x11 = Parameter(name = 'I163x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd11*complexconjugate(CKM11)*complexconjugate(Ru11)',
                    texname = '\\text{I163x11}')

I163x14 = Parameter(name = 'I163x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd11*complexconjugate(CKM11)*complexconjugate(Ru41)',
                    texname = '\\text{I163x14}')

I163x22 = Parameter(name = 'I163x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd22*complexconjugate(CKM22)*complexconjugate(Ru22)',
                    texname = '\\text{I163x22}')

I163x25 = Parameter(name = 'I163x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd22*complexconjugate(CKM22)*complexconjugate(Ru52)',
                    texname = '\\text{I163x25}')

I163x33 = Parameter(name = 'I163x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd33*complexconjugate(CKM33)*complexconjugate(Ru33)',
                    texname = '\\text{I163x33}')

I163x36 = Parameter(name = 'I163x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd33*complexconjugate(CKM33)*complexconjugate(Ru63)',
                    texname = '\\text{I163x36}')

I163x41 = Parameter(name = 'I163x41',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd41*complexconjugate(CKM11)*complexconjugate(Ru11)',
                    texname = '\\text{I163x41}')

I163x44 = Parameter(name = 'I163x44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd41*complexconjugate(CKM11)*complexconjugate(Ru41)',
                    texname = '\\text{I163x44}')

I163x52 = Parameter(name = 'I163x52',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd52*complexconjugate(CKM22)*complexconjugate(Ru22)',
                    texname = '\\text{I163x52}')

I163x55 = Parameter(name = 'I163x55',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd52*complexconjugate(CKM22)*complexconjugate(Ru52)',
                    texname = '\\text{I163x55}')

I163x63 = Parameter(name = 'I163x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd63*complexconjugate(CKM33)*complexconjugate(Ru33)',
                    texname = '\\text{I163x63}')

I163x66 = Parameter(name = 'I163x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd63*complexconjugate(CKM33)*complexconjugate(Ru63)',
                    texname = '\\text{I163x66}')

I164x11 = Parameter(name = 'I164x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM11*Ru11*complexconjugate(Rd14)*complexconjugate(yd11)',
                    texname = '\\text{I164x11}')

I164x14 = Parameter(name = 'I164x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM11*Ru41*complexconjugate(Rd14)*complexconjugate(yd11)',
                    texname = '\\text{I164x14}')

I164x22 = Parameter(name = 'I164x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM22*Ru22*complexconjugate(Rd25)*complexconjugate(yd22)',
                    texname = '\\text{I164x22}')

I164x25 = Parameter(name = 'I164x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM22*Ru52*complexconjugate(Rd25)*complexconjugate(yd22)',
                    texname = '\\text{I164x25}')

I164x33 = Parameter(name = 'I164x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM33*Ru33*complexconjugate(Rd36)*complexconjugate(yd33)',
                    texname = '\\text{I164x33}')

I164x36 = Parameter(name = 'I164x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM33*Ru63*complexconjugate(Rd36)*complexconjugate(yd33)',
                    texname = '\\text{I164x36}')

I164x41 = Parameter(name = 'I164x41',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM11*Ru11*complexconjugate(Rd44)*complexconjugate(yd11)',
                    texname = '\\text{I164x41}')

I164x44 = Parameter(name = 'I164x44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM11*Ru41*complexconjugate(Rd44)*complexconjugate(yd11)',
                    texname = '\\text{I164x44}')

I164x52 = Parameter(name = 'I164x52',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM22*Ru22*complexconjugate(Rd55)*complexconjugate(yd22)',
                    texname = '\\text{I164x52}')

I164x55 = Parameter(name = 'I164x55',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM22*Ru52*complexconjugate(Rd55)*complexconjugate(yd22)',
                    texname = '\\text{I164x55}')

I164x63 = Parameter(name = 'I164x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM33*Ru33*complexconjugate(Rd66)*complexconjugate(yd33)',
                    texname = '\\text{I164x63}')

I164x66 = Parameter(name = 'I164x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM33*Ru63*complexconjugate(Rd66)*complexconjugate(yd33)',
                    texname = '\\text{I164x66}')

I165x11 = Parameter(name = 'I165x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd14*yd11*complexconjugate(CKM11)*complexconjugate(Ru11)',
                    texname = '\\text{I165x11}')

I165x14 = Parameter(name = 'I165x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd14*yd11*complexconjugate(CKM11)*complexconjugate(Ru41)',
                    texname = '\\text{I165x14}')

I165x22 = Parameter(name = 'I165x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd25*yd22*complexconjugate(CKM22)*complexconjugate(Ru22)',
                    texname = '\\text{I165x22}')

I165x25 = Parameter(name = 'I165x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd25*yd22*complexconjugate(CKM22)*complexconjugate(Ru52)',
                    texname = '\\text{I165x25}')

I165x33 = Parameter(name = 'I165x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd36*yd33*complexconjugate(CKM33)*complexconjugate(Ru33)',
                    texname = '\\text{I165x33}')

I165x36 = Parameter(name = 'I165x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd36*yd33*complexconjugate(CKM33)*complexconjugate(Ru63)',
                    texname = '\\text{I165x36}')

I165x41 = Parameter(name = 'I165x41',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd44*yd11*complexconjugate(CKM11)*complexconjugate(Ru11)',
                    texname = '\\text{I165x41}')

I165x44 = Parameter(name = 'I165x44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd44*yd11*complexconjugate(CKM11)*complexconjugate(Ru41)',
                    texname = '\\text{I165x44}')

I165x52 = Parameter(name = 'I165x52',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd55*yd22*complexconjugate(CKM22)*complexconjugate(Ru22)',
                    texname = '\\text{I165x52}')

I165x55 = Parameter(name = 'I165x55',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd55*yd22*complexconjugate(CKM22)*complexconjugate(Ru52)',
                    texname = '\\text{I165x55}')

I165x63 = Parameter(name = 'I165x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd66*yd33*complexconjugate(CKM33)*complexconjugate(Ru33)',
                    texname = '\\text{I165x63}')

I165x66 = Parameter(name = 'I165x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd66*yd33*complexconjugate(CKM33)*complexconjugate(Ru63)',
                    texname = '\\text{I165x66}')

I166x11 = Parameter(name = 'I166x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd11*complexconjugate(CKM11)*complexconjugate(Ru14)*complexconjugate(yu11)',
                    texname = '\\text{I166x11}')

I166x14 = Parameter(name = 'I166x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd11*complexconjugate(CKM11)*complexconjugate(Ru44)*complexconjugate(yu11)',
                    texname = '\\text{I166x14}')

I166x22 = Parameter(name = 'I166x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd22*complexconjugate(CKM22)*complexconjugate(Ru25)*complexconjugate(yu22)',
                    texname = '\\text{I166x22}')

I166x25 = Parameter(name = 'I166x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd22*complexconjugate(CKM22)*complexconjugate(Ru55)*complexconjugate(yu22)',
                    texname = '\\text{I166x25}')

I166x33 = Parameter(name = 'I166x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd33*complexconjugate(CKM33)*complexconjugate(Ru36)*complexconjugate(yu33)',
                    texname = '\\text{I166x33}')

I166x36 = Parameter(name = 'I166x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd33*complexconjugate(CKM33)*complexconjugate(Ru66)*complexconjugate(yu33)',
                    texname = '\\text{I166x36}')

I166x41 = Parameter(name = 'I166x41',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd41*complexconjugate(CKM11)*complexconjugate(Ru14)*complexconjugate(yu11)',
                    texname = '\\text{I166x41}')

I166x44 = Parameter(name = 'I166x44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd41*complexconjugate(CKM11)*complexconjugate(Ru44)*complexconjugate(yu11)',
                    texname = '\\text{I166x44}')

I166x52 = Parameter(name = 'I166x52',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd52*complexconjugate(CKM22)*complexconjugate(Ru25)*complexconjugate(yu22)',
                    texname = '\\text{I166x52}')

I166x55 = Parameter(name = 'I166x55',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd52*complexconjugate(CKM22)*complexconjugate(Ru55)*complexconjugate(yu22)',
                    texname = '\\text{I166x55}')

I166x63 = Parameter(name = 'I166x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd63*complexconjugate(CKM33)*complexconjugate(Ru36)*complexconjugate(yu33)',
                    texname = '\\text{I166x63}')

I166x66 = Parameter(name = 'I166x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd63*complexconjugate(CKM33)*complexconjugate(Ru66)*complexconjugate(yu33)',
                    texname = '\\text{I166x66}')

I167x11 = Parameter(name = 'I167x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM11*Ru14*yu11*complexconjugate(Rd11)',
                    texname = '\\text{I167x11}')

I167x14 = Parameter(name = 'I167x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM11*Ru44*yu11*complexconjugate(Rd11)',
                    texname = '\\text{I167x14}')

I167x22 = Parameter(name = 'I167x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM22*Ru25*yu22*complexconjugate(Rd22)',
                    texname = '\\text{I167x22}')

I167x25 = Parameter(name = 'I167x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM22*Ru55*yu22*complexconjugate(Rd22)',
                    texname = '\\text{I167x25}')

I167x33 = Parameter(name = 'I167x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM33*Ru36*yu33*complexconjugate(Rd33)',
                    texname = '\\text{I167x33}')

I167x36 = Parameter(name = 'I167x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM33*Ru66*yu33*complexconjugate(Rd33)',
                    texname = '\\text{I167x36}')

I167x41 = Parameter(name = 'I167x41',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM11*Ru14*yu11*complexconjugate(Rd41)',
                    texname = '\\text{I167x41}')

I167x44 = Parameter(name = 'I167x44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM11*Ru44*yu11*complexconjugate(Rd41)',
                    texname = '\\text{I167x44}')

I167x52 = Parameter(name = 'I167x52',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM22*Ru25*yu22*complexconjugate(Rd52)',
                    texname = '\\text{I167x52}')

I167x55 = Parameter(name = 'I167x55',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM22*Ru55*yu22*complexconjugate(Rd52)',
                    texname = '\\text{I167x55}')

I167x63 = Parameter(name = 'I167x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM33*Ru36*yu33*complexconjugate(Rd63)',
                    texname = '\\text{I167x63}')

I167x66 = Parameter(name = 'I167x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM33*Ru66*yu33*complexconjugate(Rd63)',
                    texname = '\\text{I167x66}')

I168x11 = Parameter(name = 'I168x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru11*complexconjugate(Ru11)',
                    texname = '\\text{I168x11}')

I168x14 = Parameter(name = 'I168x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru41*complexconjugate(Ru11)',
                    texname = '\\text{I168x14}')

I168x22 = Parameter(name = 'I168x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru22*complexconjugate(Ru22)',
                    texname = '\\text{I168x22}')

I168x25 = Parameter(name = 'I168x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru52*complexconjugate(Ru22)',
                    texname = '\\text{I168x25}')

I168x33 = Parameter(name = 'I168x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru33*complexconjugate(Ru33)',
                    texname = '\\text{I168x33}')

I168x36 = Parameter(name = 'I168x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru63*complexconjugate(Ru33)',
                    texname = '\\text{I168x36}')

I168x41 = Parameter(name = 'I168x41',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru11*complexconjugate(Ru41)',
                    texname = '\\text{I168x41}')

I168x44 = Parameter(name = 'I168x44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru41*complexconjugate(Ru41)',
                    texname = '\\text{I168x44}')

I168x52 = Parameter(name = 'I168x52',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru22*complexconjugate(Ru52)',
                    texname = '\\text{I168x52}')

I168x55 = Parameter(name = 'I168x55',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru52*complexconjugate(Ru52)',
                    texname = '\\text{I168x55}')

I168x63 = Parameter(name = 'I168x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru33*complexconjugate(Ru63)',
                    texname = '\\text{I168x63}')

I168x66 = Parameter(name = 'I168x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru63*complexconjugate(Ru63)',
                    texname = '\\text{I168x66}')

I169x11 = Parameter(name = 'I169x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru11*complexconjugate(Ru11)',
                    texname = '\\text{I169x11}')

I169x14 = Parameter(name = 'I169x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru41*complexconjugate(Ru11)',
                    texname = '\\text{I169x14}')

I169x22 = Parameter(name = 'I169x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru22*complexconjugate(Ru22)',
                    texname = '\\text{I169x22}')

I169x25 = Parameter(name = 'I169x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru52*complexconjugate(Ru22)',
                    texname = '\\text{I169x25}')

I169x33 = Parameter(name = 'I169x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru33*complexconjugate(Ru33)',
                    texname = '\\text{I169x33}')

I169x36 = Parameter(name = 'I169x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru63*complexconjugate(Ru33)',
                    texname = '\\text{I169x36}')

I169x41 = Parameter(name = 'I169x41',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru11*complexconjugate(Ru41)',
                    texname = '\\text{I169x41}')

I169x44 = Parameter(name = 'I169x44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru41*complexconjugate(Ru41)',
                    texname = '\\text{I169x44}')

I169x52 = Parameter(name = 'I169x52',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru22*complexconjugate(Ru52)',
                    texname = '\\text{I169x52}')

I169x55 = Parameter(name = 'I169x55',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru52*complexconjugate(Ru52)',
                    texname = '\\text{I169x55}')

I169x63 = Parameter(name = 'I169x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru33*complexconjugate(Ru63)',
                    texname = '\\text{I169x63}')

I169x66 = Parameter(name = 'I169x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru63*complexconjugate(Ru63)',
                    texname = '\\text{I169x66}')

I17x11 = Parameter(name = 'I17x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd11*complexconjugate(Rd14)*complexconjugate(td11)',
                   texname = '\\text{I17x11}')

I17x14 = Parameter(name = 'I17x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd41*complexconjugate(Rd14)*complexconjugate(td11)',
                   texname = '\\text{I17x14}')

I17x22 = Parameter(name = 'I17x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd22*complexconjugate(Rd25)*complexconjugate(td22)',
                   texname = '\\text{I17x22}')

I17x25 = Parameter(name = 'I17x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd52*complexconjugate(Rd25)*complexconjugate(td22)',
                   texname = '\\text{I17x25}')

I17x33 = Parameter(name = 'I17x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd33*complexconjugate(Rd36)*complexconjugate(td33)',
                   texname = '\\text{I17x33}')

I17x36 = Parameter(name = 'I17x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd63*complexconjugate(Rd36)*complexconjugate(td33)',
                   texname = '\\text{I17x36}')

I17x41 = Parameter(name = 'I17x41',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd11*complexconjugate(Rd44)*complexconjugate(td11)',
                   texname = '\\text{I17x41}')

I17x44 = Parameter(name = 'I17x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd41*complexconjugate(Rd44)*complexconjugate(td11)',
                   texname = '\\text{I17x44}')

I17x52 = Parameter(name = 'I17x52',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd22*complexconjugate(Rd55)*complexconjugate(td22)',
                   texname = '\\text{I17x52}')

I17x55 = Parameter(name = 'I17x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd52*complexconjugate(Rd55)*complexconjugate(td22)',
                   texname = '\\text{I17x55}')

I17x63 = Parameter(name = 'I17x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd33*complexconjugate(Rd66)*complexconjugate(td33)',
                   texname = '\\text{I17x63}')

I17x66 = Parameter(name = 'I17x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd63*complexconjugate(Rd66)*complexconjugate(td33)',
                   texname = '\\text{I17x66}')

I170x11 = Parameter(name = 'I170x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru11*complexconjugate(Ru11)',
                    texname = '\\text{I170x11}')

I170x14 = Parameter(name = 'I170x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru41*complexconjugate(Ru11)',
                    texname = '\\text{I170x14}')

I170x22 = Parameter(name = 'I170x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru22*complexconjugate(Ru22)',
                    texname = '\\text{I170x22}')

I170x25 = Parameter(name = 'I170x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru52*complexconjugate(Ru22)',
                    texname = '\\text{I170x25}')

I170x33 = Parameter(name = 'I170x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru33*complexconjugate(Ru33)',
                    texname = '\\text{I170x33}')

I170x36 = Parameter(name = 'I170x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru63*complexconjugate(Ru33)',
                    texname = '\\text{I170x36}')

I170x41 = Parameter(name = 'I170x41',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru11*complexconjugate(Ru41)',
                    texname = '\\text{I170x41}')

I170x44 = Parameter(name = 'I170x44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru41*complexconjugate(Ru41)',
                    texname = '\\text{I170x44}')

I170x52 = Parameter(name = 'I170x52',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru22*complexconjugate(Ru52)',
                    texname = '\\text{I170x52}')

I170x55 = Parameter(name = 'I170x55',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru52*complexconjugate(Ru52)',
                    texname = '\\text{I170x55}')

I170x63 = Parameter(name = 'I170x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru33*complexconjugate(Ru63)',
                    texname = '\\text{I170x63}')

I170x66 = Parameter(name = 'I170x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru63*complexconjugate(Ru63)',
                    texname = '\\text{I170x66}')

I171x11 = Parameter(name = 'I171x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru11*complexconjugate(Ru11)',
                    texname = '\\text{I171x11}')

I171x14 = Parameter(name = 'I171x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru41*complexconjugate(Ru11)',
                    texname = '\\text{I171x14}')

I171x22 = Parameter(name = 'I171x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru22*complexconjugate(Ru22)',
                    texname = '\\text{I171x22}')

I171x25 = Parameter(name = 'I171x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru52*complexconjugate(Ru22)',
                    texname = '\\text{I171x25}')

I171x33 = Parameter(name = 'I171x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru33*complexconjugate(Ru33)',
                    texname = '\\text{I171x33}')

I171x36 = Parameter(name = 'I171x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru63*complexconjugate(Ru33)',
                    texname = '\\text{I171x36}')

I171x41 = Parameter(name = 'I171x41',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru11*complexconjugate(Ru41)',
                    texname = '\\text{I171x41}')

I171x44 = Parameter(name = 'I171x44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru41*complexconjugate(Ru41)',
                    texname = '\\text{I171x44}')

I171x52 = Parameter(name = 'I171x52',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru22*complexconjugate(Ru52)',
                    texname = '\\text{I171x52}')

I171x55 = Parameter(name = 'I171x55',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru52*complexconjugate(Ru52)',
                    texname = '\\text{I171x55}')

I171x63 = Parameter(name = 'I171x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru33*complexconjugate(Ru63)',
                    texname = '\\text{I171x63}')

I171x66 = Parameter(name = 'I171x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru63*complexconjugate(Ru63)',
                    texname = '\\text{I171x66}')

I172x11 = Parameter(name = 'I172x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru14*complexconjugate(Ru14)',
                    texname = '\\text{I172x11}')

I172x14 = Parameter(name = 'I172x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru44*complexconjugate(Ru14)',
                    texname = '\\text{I172x14}')

I172x22 = Parameter(name = 'I172x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru25*complexconjugate(Ru25)',
                    texname = '\\text{I172x22}')

I172x25 = Parameter(name = 'I172x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru55*complexconjugate(Ru25)',
                    texname = '\\text{I172x25}')

I172x33 = Parameter(name = 'I172x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru36*complexconjugate(Ru36)',
                    texname = '\\text{I172x33}')

I172x36 = Parameter(name = 'I172x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru66*complexconjugate(Ru36)',
                    texname = '\\text{I172x36}')

I172x41 = Parameter(name = 'I172x41',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru14*complexconjugate(Ru44)',
                    texname = '\\text{I172x41}')

I172x44 = Parameter(name = 'I172x44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru44*complexconjugate(Ru44)',
                    texname = '\\text{I172x44}')

I172x52 = Parameter(name = 'I172x52',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru25*complexconjugate(Ru55)',
                    texname = '\\text{I172x52}')

I172x55 = Parameter(name = 'I172x55',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru55*complexconjugate(Ru55)',
                    texname = '\\text{I172x55}')

I172x63 = Parameter(name = 'I172x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru36*complexconjugate(Ru66)',
                    texname = '\\text{I172x63}')

I172x66 = Parameter(name = 'I172x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru66*complexconjugate(Ru66)',
                    texname = '\\text{I172x66}')

I173x11 = Parameter(name = 'I173x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru11*complexconjugate(Ru11)',
                    texname = '\\text{I173x11}')

I173x14 = Parameter(name = 'I173x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru41*complexconjugate(Ru11)',
                    texname = '\\text{I173x14}')

I173x22 = Parameter(name = 'I173x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru22*complexconjugate(Ru22)',
                    texname = '\\text{I173x22}')

I173x25 = Parameter(name = 'I173x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru52*complexconjugate(Ru22)',
                    texname = '\\text{I173x25}')

I173x33 = Parameter(name = 'I173x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru33*complexconjugate(Ru33)',
                    texname = '\\text{I173x33}')

I173x36 = Parameter(name = 'I173x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru63*complexconjugate(Ru33)',
                    texname = '\\text{I173x36}')

I173x41 = Parameter(name = 'I173x41',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru11*complexconjugate(Ru41)',
                    texname = '\\text{I173x41}')

I173x44 = Parameter(name = 'I173x44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru41*complexconjugate(Ru41)',
                    texname = '\\text{I173x44}')

I173x52 = Parameter(name = 'I173x52',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru22*complexconjugate(Ru52)',
                    texname = '\\text{I173x52}')

I173x55 = Parameter(name = 'I173x55',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru52*complexconjugate(Ru52)',
                    texname = '\\text{I173x55}')

I173x63 = Parameter(name = 'I173x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru33*complexconjugate(Ru63)',
                    texname = '\\text{I173x63}')

I173x66 = Parameter(name = 'I173x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru63*complexconjugate(Ru63)',
                    texname = '\\text{I173x66}')

I174x11 = Parameter(name = 'I174x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru14*complexconjugate(Ru14)',
                    texname = '\\text{I174x11}')

I174x14 = Parameter(name = 'I174x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru44*complexconjugate(Ru14)',
                    texname = '\\text{I174x14}')

I174x22 = Parameter(name = 'I174x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru25*complexconjugate(Ru25)',
                    texname = '\\text{I174x22}')

I174x25 = Parameter(name = 'I174x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru55*complexconjugate(Ru25)',
                    texname = '\\text{I174x25}')

I174x33 = Parameter(name = 'I174x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru36*complexconjugate(Ru36)',
                    texname = '\\text{I174x33}')

I174x36 = Parameter(name = 'I174x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru66*complexconjugate(Ru36)',
                    texname = '\\text{I174x36}')

I174x41 = Parameter(name = 'I174x41',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru14*complexconjugate(Ru44)',
                    texname = '\\text{I174x41}')

I174x44 = Parameter(name = 'I174x44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru44*complexconjugate(Ru44)',
                    texname = '\\text{I174x44}')

I174x52 = Parameter(name = 'I174x52',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru25*complexconjugate(Ru55)',
                    texname = '\\text{I174x52}')

I174x55 = Parameter(name = 'I174x55',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru55*complexconjugate(Ru55)',
                    texname = '\\text{I174x55}')

I174x63 = Parameter(name = 'I174x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru36*complexconjugate(Ru66)',
                    texname = '\\text{I174x63}')

I174x66 = Parameter(name = 'I174x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru66*complexconjugate(Ru66)',
                    texname = '\\text{I174x66}')

I175x11 = Parameter(name = 'I175x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru14*complexconjugate(Ru14)',
                    texname = '\\text{I175x11}')

I175x14 = Parameter(name = 'I175x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru44*complexconjugate(Ru14)',
                    texname = '\\text{I175x14}')

I175x22 = Parameter(name = 'I175x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru25*complexconjugate(Ru25)',
                    texname = '\\text{I175x22}')

I175x25 = Parameter(name = 'I175x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru55*complexconjugate(Ru25)',
                    texname = '\\text{I175x25}')

I175x33 = Parameter(name = 'I175x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru36*complexconjugate(Ru36)',
                    texname = '\\text{I175x33}')

I175x36 = Parameter(name = 'I175x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru66*complexconjugate(Ru36)',
                    texname = '\\text{I175x36}')

I175x41 = Parameter(name = 'I175x41',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru14*complexconjugate(Ru44)',
                    texname = '\\text{I175x41}')

I175x44 = Parameter(name = 'I175x44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru44*complexconjugate(Ru44)',
                    texname = '\\text{I175x44}')

I175x52 = Parameter(name = 'I175x52',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru25*complexconjugate(Ru55)',
                    texname = '\\text{I175x52}')

I175x55 = Parameter(name = 'I175x55',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru55*complexconjugate(Ru55)',
                    texname = '\\text{I175x55}')

I175x63 = Parameter(name = 'I175x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru36*complexconjugate(Ru66)',
                    texname = '\\text{I175x63}')

I175x66 = Parameter(name = 'I175x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru66*complexconjugate(Ru66)',
                    texname = '\\text{I175x66}')

I176x11 = Parameter(name = 'I176x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru14*complexconjugate(Ru14)',
                    texname = '\\text{I176x11}')

I176x14 = Parameter(name = 'I176x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru44*complexconjugate(Ru14)',
                    texname = '\\text{I176x14}')

I176x22 = Parameter(name = 'I176x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru25*complexconjugate(Ru25)',
                    texname = '\\text{I176x22}')

I176x25 = Parameter(name = 'I176x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru55*complexconjugate(Ru25)',
                    texname = '\\text{I176x25}')

I176x33 = Parameter(name = 'I176x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru36*complexconjugate(Ru36)',
                    texname = '\\text{I176x33}')

I176x36 = Parameter(name = 'I176x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru66*complexconjugate(Ru36)',
                    texname = '\\text{I176x36}')

I176x41 = Parameter(name = 'I176x41',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru14*complexconjugate(Ru44)',
                    texname = '\\text{I176x41}')

I176x44 = Parameter(name = 'I176x44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru44*complexconjugate(Ru44)',
                    texname = '\\text{I176x44}')

I176x52 = Parameter(name = 'I176x52',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru25*complexconjugate(Ru55)',
                    texname = '\\text{I176x52}')

I176x55 = Parameter(name = 'I176x55',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru55*complexconjugate(Ru55)',
                    texname = '\\text{I176x55}')

I176x63 = Parameter(name = 'I176x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru36*complexconjugate(Ru66)',
                    texname = '\\text{I176x63}')

I176x66 = Parameter(name = 'I176x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru66*complexconjugate(Ru66)',
                    texname = '\\text{I176x66}')

I177x11 = Parameter(name = 'I177x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru14*complexconjugate(Ru14)',
                    texname = '\\text{I177x11}')

I177x14 = Parameter(name = 'I177x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru44*complexconjugate(Ru14)',
                    texname = '\\text{I177x14}')

I177x22 = Parameter(name = 'I177x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru25*complexconjugate(Ru25)',
                    texname = '\\text{I177x22}')

I177x25 = Parameter(name = 'I177x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru55*complexconjugate(Ru25)',
                    texname = '\\text{I177x25}')

I177x33 = Parameter(name = 'I177x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru36*complexconjugate(Ru36)',
                    texname = '\\text{I177x33}')

I177x36 = Parameter(name = 'I177x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru66*complexconjugate(Ru36)',
                    texname = '\\text{I177x36}')

I177x41 = Parameter(name = 'I177x41',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru14*complexconjugate(Ru44)',
                    texname = '\\text{I177x41}')

I177x44 = Parameter(name = 'I177x44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru44*complexconjugate(Ru44)',
                    texname = '\\text{I177x44}')

I177x52 = Parameter(name = 'I177x52',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru25*complexconjugate(Ru55)',
                    texname = '\\text{I177x52}')

I177x55 = Parameter(name = 'I177x55',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru55*complexconjugate(Ru55)',
                    texname = '\\text{I177x55}')

I177x63 = Parameter(name = 'I177x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru36*complexconjugate(Ru66)',
                    texname = '\\text{I177x63}')

I177x66 = Parameter(name = 'I177x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru66*complexconjugate(Ru66)',
                    texname = '\\text{I177x66}')

I178x11 = Parameter(name = 'I178x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru14*complexconjugate(Ru14)',
                    texname = '\\text{I178x11}')

I178x14 = Parameter(name = 'I178x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru44*complexconjugate(Ru14)',
                    texname = '\\text{I178x14}')

I178x22 = Parameter(name = 'I178x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru25*complexconjugate(Ru25)',
                    texname = '\\text{I178x22}')

I178x25 = Parameter(name = 'I178x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru55*complexconjugate(Ru25)',
                    texname = '\\text{I178x25}')

I178x33 = Parameter(name = 'I178x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru36*complexconjugate(Ru36)',
                    texname = '\\text{I178x33}')

I178x36 = Parameter(name = 'I178x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru66*complexconjugate(Ru36)',
                    texname = '\\text{I178x36}')

I178x41 = Parameter(name = 'I178x41',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru14*complexconjugate(Ru44)',
                    texname = '\\text{I178x41}')

I178x44 = Parameter(name = 'I178x44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru44*complexconjugate(Ru44)',
                    texname = '\\text{I178x44}')

I178x52 = Parameter(name = 'I178x52',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru25*complexconjugate(Ru55)',
                    texname = '\\text{I178x52}')

I178x55 = Parameter(name = 'I178x55',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru55*complexconjugate(Ru55)',
                    texname = '\\text{I178x55}')

I178x63 = Parameter(name = 'I178x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru36*complexconjugate(Ru66)',
                    texname = '\\text{I178x63}')

I178x66 = Parameter(name = 'I178x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru66*complexconjugate(Ru66)',
                    texname = '\\text{I178x66}')

I179x11 = Parameter(name = 'I179x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru11*complexconjugate(Ru14)*complexconjugate(yu11)',
                    texname = '\\text{I179x11}')

I179x14 = Parameter(name = 'I179x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru41*complexconjugate(Ru14)*complexconjugate(yu11)',
                    texname = '\\text{I179x14}')

I179x22 = Parameter(name = 'I179x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru22*complexconjugate(Ru25)*complexconjugate(yu22)',
                    texname = '\\text{I179x22}')

I179x25 = Parameter(name = 'I179x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru52*complexconjugate(Ru25)*complexconjugate(yu22)',
                    texname = '\\text{I179x25}')

I179x33 = Parameter(name = 'I179x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru33*complexconjugate(Ru36)*complexconjugate(yu33)',
                    texname = '\\text{I179x33}')

I179x36 = Parameter(name = 'I179x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru63*complexconjugate(Ru36)*complexconjugate(yu33)',
                    texname = '\\text{I179x36}')

I179x41 = Parameter(name = 'I179x41',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru11*complexconjugate(Ru44)*complexconjugate(yu11)',
                    texname = '\\text{I179x41}')

I179x44 = Parameter(name = 'I179x44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru41*complexconjugate(Ru44)*complexconjugate(yu11)',
                    texname = '\\text{I179x44}')

I179x52 = Parameter(name = 'I179x52',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru22*complexconjugate(Ru55)*complexconjugate(yu22)',
                    texname = '\\text{I179x52}')

I179x55 = Parameter(name = 'I179x55',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru52*complexconjugate(Ru55)*complexconjugate(yu22)',
                    texname = '\\text{I179x55}')

I179x63 = Parameter(name = 'I179x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru33*complexconjugate(Ru66)*complexconjugate(yu33)',
                    texname = '\\text{I179x63}')

I179x66 = Parameter(name = 'I179x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru63*complexconjugate(Ru66)*complexconjugate(yu33)',
                    texname = '\\text{I179x66}')

I18x11 = Parameter(name = 'I18x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd11*complexconjugate(Rd14)*complexconjugate(yd11)',
                   texname = '\\text{I18x11}')

I18x14 = Parameter(name = 'I18x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd41*complexconjugate(Rd14)*complexconjugate(yd11)',
                   texname = '\\text{I18x14}')

I18x22 = Parameter(name = 'I18x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd22*complexconjugate(Rd25)*complexconjugate(yd22)',
                   texname = '\\text{I18x22}')

I18x25 = Parameter(name = 'I18x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd52*complexconjugate(Rd25)*complexconjugate(yd22)',
                   texname = '\\text{I18x25}')

I18x33 = Parameter(name = 'I18x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd33*complexconjugate(Rd36)*complexconjugate(yd33)',
                   texname = '\\text{I18x33}')

I18x36 = Parameter(name = 'I18x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd63*complexconjugate(Rd36)*complexconjugate(yd33)',
                   texname = '\\text{I18x36}')

I18x41 = Parameter(name = 'I18x41',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd11*complexconjugate(Rd44)*complexconjugate(yd11)',
                   texname = '\\text{I18x41}')

I18x44 = Parameter(name = 'I18x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd41*complexconjugate(Rd44)*complexconjugate(yd11)',
                   texname = '\\text{I18x44}')

I18x52 = Parameter(name = 'I18x52',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd22*complexconjugate(Rd55)*complexconjugate(yd22)',
                   texname = '\\text{I18x52}')

I18x55 = Parameter(name = 'I18x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd52*complexconjugate(Rd55)*complexconjugate(yd22)',
                   texname = '\\text{I18x55}')

I18x63 = Parameter(name = 'I18x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd33*complexconjugate(Rd66)*complexconjugate(yd33)',
                   texname = '\\text{I18x63}')

I18x66 = Parameter(name = 'I18x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd63*complexconjugate(Rd66)*complexconjugate(yd33)',
                   texname = '\\text{I18x66}')

I180x11 = Parameter(name = 'I180x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru14*yu11*complexconjugate(Ru11)',
                    texname = '\\text{I180x11}')

I180x14 = Parameter(name = 'I180x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru44*yu11*complexconjugate(Ru11)',
                    texname = '\\text{I180x14}')

I180x22 = Parameter(name = 'I180x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru25*yu22*complexconjugate(Ru22)',
                    texname = '\\text{I180x22}')

I180x25 = Parameter(name = 'I180x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru55*yu22*complexconjugate(Ru22)',
                    texname = '\\text{I180x25}')

I180x33 = Parameter(name = 'I180x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru36*yu33*complexconjugate(Ru33)',
                    texname = '\\text{I180x33}')

I180x36 = Parameter(name = 'I180x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru66*yu33*complexconjugate(Ru33)',
                    texname = '\\text{I180x36}')

I180x41 = Parameter(name = 'I180x41',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru14*yu11*complexconjugate(Ru41)',
                    texname = '\\text{I180x41}')

I180x44 = Parameter(name = 'I180x44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru44*yu11*complexconjugate(Ru41)',
                    texname = '\\text{I180x44}')

I180x52 = Parameter(name = 'I180x52',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru25*yu22*complexconjugate(Ru52)',
                    texname = '\\text{I180x52}')

I180x55 = Parameter(name = 'I180x55',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru55*yu22*complexconjugate(Ru52)',
                    texname = '\\text{I180x55}')

I180x63 = Parameter(name = 'I180x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru36*yu33*complexconjugate(Ru63)',
                    texname = '\\text{I180x63}')

I180x66 = Parameter(name = 'I180x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru66*yu33*complexconjugate(Ru63)',
                    texname = '\\text{I180x66}')

I181x11 = Parameter(name = 'I181x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru11*complexconjugate(Ru14)*complexconjugate(yu11)',
                    texname = '\\text{I181x11}')

I181x14 = Parameter(name = 'I181x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru41*complexconjugate(Ru14)*complexconjugate(yu11)',
                    texname = '\\text{I181x14}')

I181x22 = Parameter(name = 'I181x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru22*complexconjugate(Ru25)*complexconjugate(yu22)',
                    texname = '\\text{I181x22}')

I181x25 = Parameter(name = 'I181x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru52*complexconjugate(Ru25)*complexconjugate(yu22)',
                    texname = '\\text{I181x25}')

I181x33 = Parameter(name = 'I181x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru33*complexconjugate(Ru36)*complexconjugate(yu33)',
                    texname = '\\text{I181x33}')

I181x36 = Parameter(name = 'I181x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru63*complexconjugate(Ru36)*complexconjugate(yu33)',
                    texname = '\\text{I181x36}')

I181x41 = Parameter(name = 'I181x41',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru11*complexconjugate(Ru44)*complexconjugate(yu11)',
                    texname = '\\text{I181x41}')

I181x44 = Parameter(name = 'I181x44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru41*complexconjugate(Ru44)*complexconjugate(yu11)',
                    texname = '\\text{I181x44}')

I181x52 = Parameter(name = 'I181x52',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru22*complexconjugate(Ru55)*complexconjugate(yu22)',
                    texname = '\\text{I181x52}')

I181x55 = Parameter(name = 'I181x55',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru52*complexconjugate(Ru55)*complexconjugate(yu22)',
                    texname = '\\text{I181x55}')

I181x63 = Parameter(name = 'I181x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru33*complexconjugate(Ru66)*complexconjugate(yu33)',
                    texname = '\\text{I181x63}')

I181x66 = Parameter(name = 'I181x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru63*complexconjugate(Ru66)*complexconjugate(yu33)',
                    texname = '\\text{I181x66}')

I182x11 = Parameter(name = 'I182x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru14*yu11*complexconjugate(Ru11)',
                    texname = '\\text{I182x11}')

I182x14 = Parameter(name = 'I182x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru44*yu11*complexconjugate(Ru11)',
                    texname = '\\text{I182x14}')

I182x22 = Parameter(name = 'I182x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru25*yu22*complexconjugate(Ru22)',
                    texname = '\\text{I182x22}')

I182x25 = Parameter(name = 'I182x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru55*yu22*complexconjugate(Ru22)',
                    texname = '\\text{I182x25}')

I182x33 = Parameter(name = 'I182x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru36*yu33*complexconjugate(Ru33)',
                    texname = '\\text{I182x33}')

I182x36 = Parameter(name = 'I182x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru66*yu33*complexconjugate(Ru33)',
                    texname = '\\text{I182x36}')

I182x41 = Parameter(name = 'I182x41',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru14*yu11*complexconjugate(Ru41)',
                    texname = '\\text{I182x41}')

I182x44 = Parameter(name = 'I182x44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru44*yu11*complexconjugate(Ru41)',
                    texname = '\\text{I182x44}')

I182x52 = Parameter(name = 'I182x52',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru25*yu22*complexconjugate(Ru52)',
                    texname = '\\text{I182x52}')

I182x55 = Parameter(name = 'I182x55',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru55*yu22*complexconjugate(Ru52)',
                    texname = '\\text{I182x55}')

I182x63 = Parameter(name = 'I182x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru36*yu33*complexconjugate(Ru63)',
                    texname = '\\text{I182x63}')

I182x66 = Parameter(name = 'I182x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru66*yu33*complexconjugate(Ru63)',
                    texname = '\\text{I182x66}')

I183x11 = Parameter(name = 'I183x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru11*complexconjugate(Ru14)*complexconjugate(yu11)',
                    texname = '\\text{I183x11}')

I183x14 = Parameter(name = 'I183x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru41*complexconjugate(Ru14)*complexconjugate(yu11)',
                    texname = '\\text{I183x14}')

I183x22 = Parameter(name = 'I183x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru22*complexconjugate(Ru25)*complexconjugate(yu22)',
                    texname = '\\text{I183x22}')

I183x25 = Parameter(name = 'I183x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru52*complexconjugate(Ru25)*complexconjugate(yu22)',
                    texname = '\\text{I183x25}')

I183x33 = Parameter(name = 'I183x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru33*complexconjugate(Ru36)*complexconjugate(yu33)',
                    texname = '\\text{I183x33}')

I183x36 = Parameter(name = 'I183x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru63*complexconjugate(Ru36)*complexconjugate(yu33)',
                    texname = '\\text{I183x36}')

I183x41 = Parameter(name = 'I183x41',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru11*complexconjugate(Ru44)*complexconjugate(yu11)',
                    texname = '\\text{I183x41}')

I183x44 = Parameter(name = 'I183x44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru41*complexconjugate(Ru44)*complexconjugate(yu11)',
                    texname = '\\text{I183x44}')

I183x52 = Parameter(name = 'I183x52',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru22*complexconjugate(Ru55)*complexconjugate(yu22)',
                    texname = '\\text{I183x52}')

I183x55 = Parameter(name = 'I183x55',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru52*complexconjugate(Ru55)*complexconjugate(yu22)',
                    texname = '\\text{I183x55}')

I183x63 = Parameter(name = 'I183x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru33*complexconjugate(Ru66)*complexconjugate(yu33)',
                    texname = '\\text{I183x63}')

I183x66 = Parameter(name = 'I183x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru63*complexconjugate(Ru66)*complexconjugate(yu33)',
                    texname = '\\text{I183x66}')

I184x11 = Parameter(name = 'I184x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru14*yu11*complexconjugate(Ru11)',
                    texname = '\\text{I184x11}')

I184x14 = Parameter(name = 'I184x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru44*yu11*complexconjugate(Ru11)',
                    texname = '\\text{I184x14}')

I184x22 = Parameter(name = 'I184x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru25*yu22*complexconjugate(Ru22)',
                    texname = '\\text{I184x22}')

I184x25 = Parameter(name = 'I184x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru55*yu22*complexconjugate(Ru22)',
                    texname = '\\text{I184x25}')

I184x33 = Parameter(name = 'I184x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru36*yu33*complexconjugate(Ru33)',
                    texname = '\\text{I184x33}')

I184x36 = Parameter(name = 'I184x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru66*yu33*complexconjugate(Ru33)',
                    texname = '\\text{I184x36}')

I184x41 = Parameter(name = 'I184x41',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru14*yu11*complexconjugate(Ru41)',
                    texname = '\\text{I184x41}')

I184x44 = Parameter(name = 'I184x44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru44*yu11*complexconjugate(Ru41)',
                    texname = '\\text{I184x44}')

I184x52 = Parameter(name = 'I184x52',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru25*yu22*complexconjugate(Ru52)',
                    texname = '\\text{I184x52}')

I184x55 = Parameter(name = 'I184x55',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru55*yu22*complexconjugate(Ru52)',
                    texname = '\\text{I184x55}')

I184x63 = Parameter(name = 'I184x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru36*yu33*complexconjugate(Ru63)',
                    texname = '\\text{I184x63}')

I184x66 = Parameter(name = 'I184x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru66*yu33*complexconjugate(Ru63)',
                    texname = '\\text{I184x66}')

I185x11 = Parameter(name = 'I185x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru11*complexconjugate(Ru14)*complexconjugate(yu11)',
                    texname = '\\text{I185x11}')

I185x14 = Parameter(name = 'I185x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru41*complexconjugate(Ru14)*complexconjugate(yu11)',
                    texname = '\\text{I185x14}')

I185x22 = Parameter(name = 'I185x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru22*complexconjugate(Ru25)*complexconjugate(yu22)',
                    texname = '\\text{I185x22}')

I185x25 = Parameter(name = 'I185x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru52*complexconjugate(Ru25)*complexconjugate(yu22)',
                    texname = '\\text{I185x25}')

I185x33 = Parameter(name = 'I185x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru33*complexconjugate(Ru36)*complexconjugate(yu33)',
                    texname = '\\text{I185x33}')

I185x36 = Parameter(name = 'I185x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru63*complexconjugate(Ru36)*complexconjugate(yu33)',
                    texname = '\\text{I185x36}')

I185x41 = Parameter(name = 'I185x41',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru11*complexconjugate(Ru44)*complexconjugate(yu11)',
                    texname = '\\text{I185x41}')

I185x44 = Parameter(name = 'I185x44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru41*complexconjugate(Ru44)*complexconjugate(yu11)',
                    texname = '\\text{I185x44}')

I185x52 = Parameter(name = 'I185x52',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru22*complexconjugate(Ru55)*complexconjugate(yu22)',
                    texname = '\\text{I185x52}')

I185x55 = Parameter(name = 'I185x55',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru52*complexconjugate(Ru55)*complexconjugate(yu22)',
                    texname = '\\text{I185x55}')

I185x63 = Parameter(name = 'I185x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru33*complexconjugate(Ru66)*complexconjugate(yu33)',
                    texname = '\\text{I185x63}')

I185x66 = Parameter(name = 'I185x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru63*complexconjugate(Ru66)*complexconjugate(yu33)',
                    texname = '\\text{I185x66}')

I186x11 = Parameter(name = 'I186x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru14*yu11*complexconjugate(Ru11)',
                    texname = '\\text{I186x11}')

I186x14 = Parameter(name = 'I186x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru44*yu11*complexconjugate(Ru11)',
                    texname = '\\text{I186x14}')

I186x22 = Parameter(name = 'I186x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru25*yu22*complexconjugate(Ru22)',
                    texname = '\\text{I186x22}')

I186x25 = Parameter(name = 'I186x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru55*yu22*complexconjugate(Ru22)',
                    texname = '\\text{I186x25}')

I186x33 = Parameter(name = 'I186x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru36*yu33*complexconjugate(Ru33)',
                    texname = '\\text{I186x33}')

I186x36 = Parameter(name = 'I186x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru66*yu33*complexconjugate(Ru33)',
                    texname = '\\text{I186x36}')

I186x41 = Parameter(name = 'I186x41',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru14*yu11*complexconjugate(Ru41)',
                    texname = '\\text{I186x41}')

I186x44 = Parameter(name = 'I186x44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru44*yu11*complexconjugate(Ru41)',
                    texname = '\\text{I186x44}')

I186x52 = Parameter(name = 'I186x52',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru25*yu22*complexconjugate(Ru52)',
                    texname = '\\text{I186x52}')

I186x55 = Parameter(name = 'I186x55',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru55*yu22*complexconjugate(Ru52)',
                    texname = '\\text{I186x55}')

I186x63 = Parameter(name = 'I186x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru36*yu33*complexconjugate(Ru63)',
                    texname = '\\text{I186x63}')

I186x66 = Parameter(name = 'I186x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru66*yu33*complexconjugate(Ru63)',
                    texname = '\\text{I186x66}')

I187x11 = Parameter(name = 'I187x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM11*complexconjugate(Rd11)',
                    texname = '\\text{I187x11}')

I187x14 = Parameter(name = 'I187x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM11*complexconjugate(Rd41)',
                    texname = '\\text{I187x14}')

I187x22 = Parameter(name = 'I187x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM22*complexconjugate(Rd22)',
                    texname = '\\text{I187x22}')

I187x25 = Parameter(name = 'I187x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM22*complexconjugate(Rd52)',
                    texname = '\\text{I187x25}')

I187x33 = Parameter(name = 'I187x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM33*complexconjugate(Rd33)',
                    texname = '\\text{I187x33}')

I187x36 = Parameter(name = 'I187x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM33*complexconjugate(Rd63)',
                    texname = '\\text{I187x36}')

I188x11 = Parameter(name = 'I188x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM11*complexconjugate(Rd14)*complexconjugate(yd11)',
                    texname = '\\text{I188x11}')

I188x14 = Parameter(name = 'I188x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM11*complexconjugate(Rd44)*complexconjugate(yd11)',
                    texname = '\\text{I188x14}')

I188x22 = Parameter(name = 'I188x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM22*complexconjugate(Rd25)*complexconjugate(yd22)',
                    texname = '\\text{I188x22}')

I188x25 = Parameter(name = 'I188x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM22*complexconjugate(Rd55)*complexconjugate(yd22)',
                    texname = '\\text{I188x25}')

I188x33 = Parameter(name = 'I188x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM33*complexconjugate(Rd36)*complexconjugate(yd33)',
                    texname = '\\text{I188x33}')

I188x36 = Parameter(name = 'I188x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM33*complexconjugate(Rd66)*complexconjugate(yd33)',
                    texname = '\\text{I188x36}')

I189x11 = Parameter(name = 'I189x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM11*yu11*complexconjugate(Rd11)',
                    texname = '\\text{I189x11}')

I189x14 = Parameter(name = 'I189x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM11*yu11*complexconjugate(Rd41)',
                    texname = '\\text{I189x14}')

I189x22 = Parameter(name = 'I189x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM22*yu22*complexconjugate(Rd22)',
                    texname = '\\text{I189x22}')

I189x25 = Parameter(name = 'I189x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM22*yu22*complexconjugate(Rd52)',
                    texname = '\\text{I189x25}')

I189x33 = Parameter(name = 'I189x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM33*yu33*complexconjugate(Rd33)',
                    texname = '\\text{I189x33}')

I189x36 = Parameter(name = 'I189x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM33*yu33*complexconjugate(Rd63)',
                    texname = '\\text{I189x36}')

I19x11 = Parameter(name = 'I19x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd14*td11*complexconjugate(Rd11)',
                   texname = '\\text{I19x11}')

I19x14 = Parameter(name = 'I19x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd44*td11*complexconjugate(Rd11)',
                   texname = '\\text{I19x14}')

I19x22 = Parameter(name = 'I19x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd25*td22*complexconjugate(Rd22)',
                   texname = '\\text{I19x22}')

I19x25 = Parameter(name = 'I19x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd55*td22*complexconjugate(Rd22)',
                   texname = '\\text{I19x25}')

I19x33 = Parameter(name = 'I19x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd36*td33*complexconjugate(Rd33)',
                   texname = '\\text{I19x33}')

I19x36 = Parameter(name = 'I19x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd66*td33*complexconjugate(Rd33)',
                   texname = '\\text{I19x36}')

I19x41 = Parameter(name = 'I19x41',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd14*td11*complexconjugate(Rd41)',
                   texname = '\\text{I19x41}')

I19x44 = Parameter(name = 'I19x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd44*td11*complexconjugate(Rd41)',
                   texname = '\\text{I19x44}')

I19x52 = Parameter(name = 'I19x52',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd25*td22*complexconjugate(Rd52)',
                   texname = '\\text{I19x52}')

I19x55 = Parameter(name = 'I19x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd55*td22*complexconjugate(Rd52)',
                   texname = '\\text{I19x55}')

I19x63 = Parameter(name = 'I19x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd36*td33*complexconjugate(Rd63)',
                   texname = '\\text{I19x63}')

I19x66 = Parameter(name = 'I19x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd66*td33*complexconjugate(Rd63)',
                   texname = '\\text{I19x66}')

I190x11 = Parameter(name = 'I190x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(Rl11)',
                    texname = '\\text{I190x11}')

I190x14 = Parameter(name = 'I190x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(Rl41)',
                    texname = '\\text{I190x14}')

I190x22 = Parameter(name = 'I190x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(Rl22)',
                    texname = '\\text{I190x22}')

I190x25 = Parameter(name = 'I190x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(Rl52)',
                    texname = '\\text{I190x25}')

I190x33 = Parameter(name = 'I190x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(Rl33)',
                    texname = '\\text{I190x33}')

I190x36 = Parameter(name = 'I190x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(Rl63)',
                    texname = '\\text{I190x36}')

I191x11 = Parameter(name = 'I191x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(Rl14)*complexconjugate(ye11)',
                    texname = '\\text{I191x11}')

I191x14 = Parameter(name = 'I191x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(Rl44)*complexconjugate(ye11)',
                    texname = '\\text{I191x14}')

I191x22 = Parameter(name = 'I191x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(Rl25)*complexconjugate(ye22)',
                    texname = '\\text{I191x22}')

I191x25 = Parameter(name = 'I191x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(Rl55)*complexconjugate(ye22)',
                    texname = '\\text{I191x25}')

I191x33 = Parameter(name = 'I191x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(Rl36)*complexconjugate(ye33)',
                    texname = '\\text{I191x33}')

I191x36 = Parameter(name = 'I191x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(Rl66)*complexconjugate(ye33)',
                    texname = '\\text{I191x36}')

I192x11 = Parameter(name = 'I192x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(Rn11)',
                    texname = '\\text{I192x11}')

I192x22 = Parameter(name = 'I192x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(Rn22)',
                    texname = '\\text{I192x22}')

I192x33 = Parameter(name = 'I192x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(Rn33)',
                    texname = '\\text{I192x33}')

I193x11 = Parameter(name = 'I193x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'ye11*complexconjugate(Rn11)',
                    texname = '\\text{I193x11}')

I193x22 = Parameter(name = 'I193x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'ye22*complexconjugate(Rn22)',
                    texname = '\\text{I193x22}')

I193x33 = Parameter(name = 'I193x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'ye33*complexconjugate(Rn33)',
                    texname = '\\text{I193x33}')

I194x11 = Parameter(name = 'I194x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(CKM11)*complexconjugate(Ru11)',
                    texname = '\\text{I194x11}')

I194x14 = Parameter(name = 'I194x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(CKM11)*complexconjugate(Ru41)',
                    texname = '\\text{I194x14}')

I194x22 = Parameter(name = 'I194x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(CKM22)*complexconjugate(Ru22)',
                    texname = '\\text{I194x22}')

I194x25 = Parameter(name = 'I194x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(CKM22)*complexconjugate(Ru52)',
                    texname = '\\text{I194x25}')

I194x33 = Parameter(name = 'I194x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(CKM33)*complexconjugate(Ru33)',
                    texname = '\\text{I194x33}')

I194x36 = Parameter(name = 'I194x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(CKM33)*complexconjugate(Ru63)',
                    texname = '\\text{I194x36}')

I195x11 = Parameter(name = 'I195x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(CKM11)*complexconjugate(Ru14)*complexconjugate(yu11)',
                    texname = '\\text{I195x11}')

I195x14 = Parameter(name = 'I195x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(CKM11)*complexconjugate(Ru44)*complexconjugate(yu11)',
                    texname = '\\text{I195x14}')

I195x22 = Parameter(name = 'I195x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(CKM22)*complexconjugate(Ru25)*complexconjugate(yu22)',
                    texname = '\\text{I195x22}')

I195x25 = Parameter(name = 'I195x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(CKM22)*complexconjugate(Ru55)*complexconjugate(yu22)',
                    texname = '\\text{I195x25}')

I195x33 = Parameter(name = 'I195x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(CKM33)*complexconjugate(Ru36)*complexconjugate(yu33)',
                    texname = '\\text{I195x33}')

I195x36 = Parameter(name = 'I195x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(CKM33)*complexconjugate(Ru66)*complexconjugate(yu33)',
                    texname = '\\text{I195x36}')

I196x11 = Parameter(name = 'I196x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'yd11*complexconjugate(CKM11)*complexconjugate(Ru11)',
                    texname = '\\text{I196x11}')

I196x14 = Parameter(name = 'I196x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'yd11*complexconjugate(CKM11)*complexconjugate(Ru41)',
                    texname = '\\text{I196x14}')

I196x22 = Parameter(name = 'I196x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'yd22*complexconjugate(CKM22)*complexconjugate(Ru22)',
                    texname = '\\text{I196x22}')

I196x25 = Parameter(name = 'I196x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'yd22*complexconjugate(CKM22)*complexconjugate(Ru52)',
                    texname = '\\text{I196x25}')

I196x33 = Parameter(name = 'I196x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'yd33*complexconjugate(CKM33)*complexconjugate(Ru33)',
                    texname = '\\text{I196x33}')

I196x36 = Parameter(name = 'I196x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'yd33*complexconjugate(CKM33)*complexconjugate(Ru63)',
                    texname = '\\text{I196x36}')

I197x11 = Parameter(name = 'I197x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM11*Ru11*complexconjugate(Rd11)',
                    texname = '\\text{I197x11}')

I197x14 = Parameter(name = 'I197x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM11*Ru41*complexconjugate(Rd11)',
                    texname = '\\text{I197x14}')

I197x22 = Parameter(name = 'I197x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM22*Ru22*complexconjugate(Rd22)',
                    texname = '\\text{I197x22}')

I197x25 = Parameter(name = 'I197x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM22*Ru52*complexconjugate(Rd22)',
                    texname = '\\text{I197x25}')

I197x33 = Parameter(name = 'I197x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM33*Ru33*complexconjugate(Rd33)',
                    texname = '\\text{I197x33}')

I197x36 = Parameter(name = 'I197x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM33*Ru63*complexconjugate(Rd33)',
                    texname = '\\text{I197x36}')

I197x41 = Parameter(name = 'I197x41',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM11*Ru11*complexconjugate(Rd41)',
                    texname = '\\text{I197x41}')

I197x44 = Parameter(name = 'I197x44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM11*Ru41*complexconjugate(Rd41)',
                    texname = '\\text{I197x44}')

I197x52 = Parameter(name = 'I197x52',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM22*Ru22*complexconjugate(Rd52)',
                    texname = '\\text{I197x52}')

I197x55 = Parameter(name = 'I197x55',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM22*Ru52*complexconjugate(Rd52)',
                    texname = '\\text{I197x55}')

I197x63 = Parameter(name = 'I197x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM33*Ru33*complexconjugate(Rd63)',
                    texname = '\\text{I197x63}')

I197x66 = Parameter(name = 'I197x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM33*Ru63*complexconjugate(Rd63)',
                    texname = '\\text{I197x66}')

I198x11 = Parameter(name = 'I198x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn11*complexconjugate(Rl11)',
                    texname = '\\text{I198x11}')

I198x14 = Parameter(name = 'I198x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn11*complexconjugate(Rl41)',
                    texname = '\\text{I198x14}')

I198x22 = Parameter(name = 'I198x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn22*complexconjugate(Rl22)',
                    texname = '\\text{I198x22}')

I198x25 = Parameter(name = 'I198x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn22*complexconjugate(Rl52)',
                    texname = '\\text{I198x25}')

I198x33 = Parameter(name = 'I198x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn33*complexconjugate(Rl33)',
                    texname = '\\text{I198x33}')

I198x36 = Parameter(name = 'I198x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn33*complexconjugate(Rl63)',
                    texname = '\\text{I198x36}')

I199x11 = Parameter(name = 'I199x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd11*complexconjugate(CKM11)*complexconjugate(Ru11)',
                    texname = '\\text{I199x11}')

I199x14 = Parameter(name = 'I199x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd11*complexconjugate(CKM11)*complexconjugate(Ru41)',
                    texname = '\\text{I199x14}')

I199x22 = Parameter(name = 'I199x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd22*complexconjugate(CKM22)*complexconjugate(Ru22)',
                    texname = '\\text{I199x22}')

I199x25 = Parameter(name = 'I199x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd22*complexconjugate(CKM22)*complexconjugate(Ru52)',
                    texname = '\\text{I199x25}')

I199x33 = Parameter(name = 'I199x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd33*complexconjugate(CKM33)*complexconjugate(Ru33)',
                    texname = '\\text{I199x33}')

I199x36 = Parameter(name = 'I199x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd33*complexconjugate(CKM33)*complexconjugate(Ru63)',
                    texname = '\\text{I199x36}')

I199x41 = Parameter(name = 'I199x41',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd41*complexconjugate(CKM11)*complexconjugate(Ru11)',
                    texname = '\\text{I199x41}')

I199x44 = Parameter(name = 'I199x44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd41*complexconjugate(CKM11)*complexconjugate(Ru41)',
                    texname = '\\text{I199x44}')

I199x52 = Parameter(name = 'I199x52',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd52*complexconjugate(CKM22)*complexconjugate(Ru22)',
                    texname = '\\text{I199x52}')

I199x55 = Parameter(name = 'I199x55',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd52*complexconjugate(CKM22)*complexconjugate(Ru52)',
                    texname = '\\text{I199x55}')

I199x63 = Parameter(name = 'I199x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd63*complexconjugate(CKM33)*complexconjugate(Ru33)',
                    texname = '\\text{I199x63}')

I199x66 = Parameter(name = 'I199x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd63*complexconjugate(CKM33)*complexconjugate(Ru63)',
                    texname = '\\text{I199x66}')

I2x11 = Parameter(name = 'I2x11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yd11*complexconjugate(CKM11)',
                  texname = '\\text{I2x11}')

I2x22 = Parameter(name = 'I2x22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yd22*complexconjugate(CKM22)',
                  texname = '\\text{I2x22}')

I2x33 = Parameter(name = 'I2x33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yd33*complexconjugate(CKM33)',
                  texname = '\\text{I2x33}')

I20x11 = Parameter(name = 'I20x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd11*yd11*complexconjugate(Rd11)*complexconjugate(yd11)',
                   texname = '\\text{I20x11}')

I20x14 = Parameter(name = 'I20x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd41*yd11*complexconjugate(Rd11)*complexconjugate(yd11)',
                   texname = '\\text{I20x14}')

I20x22 = Parameter(name = 'I20x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd22*yd22*complexconjugate(Rd22)*complexconjugate(yd22)',
                   texname = '\\text{I20x22}')

I20x25 = Parameter(name = 'I20x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd52*yd22*complexconjugate(Rd22)*complexconjugate(yd22)',
                   texname = '\\text{I20x25}')

I20x33 = Parameter(name = 'I20x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd33*yd33*complexconjugate(Rd33)*complexconjugate(yd33)',
                   texname = '\\text{I20x33}')

I20x36 = Parameter(name = 'I20x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd63*yd33*complexconjugate(Rd33)*complexconjugate(yd33)',
                   texname = '\\text{I20x36}')

I20x41 = Parameter(name = 'I20x41',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd11*yd11*complexconjugate(Rd41)*complexconjugate(yd11)',
                   texname = '\\text{I20x41}')

I20x44 = Parameter(name = 'I20x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd41*yd11*complexconjugate(Rd41)*complexconjugate(yd11)',
                   texname = '\\text{I20x44}')

I20x52 = Parameter(name = 'I20x52',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd22*yd22*complexconjugate(Rd52)*complexconjugate(yd22)',
                   texname = '\\text{I20x52}')

I20x55 = Parameter(name = 'I20x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd52*yd22*complexconjugate(Rd52)*complexconjugate(yd22)',
                   texname = '\\text{I20x55}')

I20x63 = Parameter(name = 'I20x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd33*yd33*complexconjugate(Rd63)*complexconjugate(yd33)',
                   texname = '\\text{I20x63}')

I20x66 = Parameter(name = 'I20x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd63*yd33*complexconjugate(Rd63)*complexconjugate(yd33)',
                   texname = '\\text{I20x66}')

I200x11 = Parameter(name = 'I200x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl11*complexconjugate(Rn11)',
                    texname = '\\text{I200x11}')

I200x14 = Parameter(name = 'I200x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl41*complexconjugate(Rn11)',
                    texname = '\\text{I200x14}')

I200x22 = Parameter(name = 'I200x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl22*complexconjugate(Rn22)',
                    texname = '\\text{I200x22}')

I200x25 = Parameter(name = 'I200x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl52*complexconjugate(Rn22)',
                    texname = '\\text{I200x25}')

I200x33 = Parameter(name = 'I200x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl33*complexconjugate(Rn33)',
                    texname = '\\text{I200x33}')

I200x36 = Parameter(name = 'I200x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl63*complexconjugate(Rn33)',
                    texname = '\\text{I200x36}')

I201x11 = Parameter(name = 'I201x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru11*complexconjugate(Ru11)',
                    texname = '\\text{I201x11}')

I201x14 = Parameter(name = 'I201x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru41*complexconjugate(Ru11)',
                    texname = '\\text{I201x14}')

I201x22 = Parameter(name = 'I201x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru22*complexconjugate(Ru22)',
                    texname = '\\text{I201x22}')

I201x25 = Parameter(name = 'I201x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru52*complexconjugate(Ru22)',
                    texname = '\\text{I201x25}')

I201x33 = Parameter(name = 'I201x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru33*complexconjugate(Ru33)',
                    texname = '\\text{I201x33}')

I201x36 = Parameter(name = 'I201x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru63*complexconjugate(Ru33)',
                    texname = '\\text{I201x36}')

I201x41 = Parameter(name = 'I201x41',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru11*complexconjugate(Ru41)',
                    texname = '\\text{I201x41}')

I201x44 = Parameter(name = 'I201x44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru41*complexconjugate(Ru41)',
                    texname = '\\text{I201x44}')

I201x52 = Parameter(name = 'I201x52',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru22*complexconjugate(Ru52)',
                    texname = '\\text{I201x52}')

I201x55 = Parameter(name = 'I201x55',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru52*complexconjugate(Ru52)',
                    texname = '\\text{I201x55}')

I201x63 = Parameter(name = 'I201x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru33*complexconjugate(Ru63)',
                    texname = '\\text{I201x63}')

I201x66 = Parameter(name = 'I201x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru63*complexconjugate(Ru63)',
                    texname = '\\text{I201x66}')

I202x11 = Parameter(name = 'I202x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'ye11',
                    texname = '\\text{I202x11}')

I202x22 = Parameter(name = 'I202x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'ye22',
                    texname = '\\text{I202x22}')

I202x33 = Parameter(name = 'I202x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'ye33',
                    texname = '\\text{I202x33}')

I203x11 = Parameter(name = 'I203x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru14*complexconjugate(Ru14)',
                    texname = '\\text{I203x11}')

I203x14 = Parameter(name = 'I203x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru44*complexconjugate(Ru14)',
                    texname = '\\text{I203x14}')

I203x22 = Parameter(name = 'I203x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru25*complexconjugate(Ru25)',
                    texname = '\\text{I203x22}')

I203x25 = Parameter(name = 'I203x25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru55*complexconjugate(Ru25)',
                    texname = '\\text{I203x25}')

I203x33 = Parameter(name = 'I203x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru36*complexconjugate(Ru36)',
                    texname = '\\text{I203x33}')

I203x36 = Parameter(name = 'I203x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru66*complexconjugate(Ru36)',
                    texname = '\\text{I203x36}')

I203x41 = Parameter(name = 'I203x41',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru14*complexconjugate(Ru44)',
                    texname = '\\text{I203x41}')

I203x44 = Parameter(name = 'I203x44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru44*complexconjugate(Ru44)',
                    texname = '\\text{I203x44}')

I203x52 = Parameter(name = 'I203x52',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru25*complexconjugate(Ru55)',
                    texname = '\\text{I203x52}')

I203x55 = Parameter(name = 'I203x55',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru55*complexconjugate(Ru55)',
                    texname = '\\text{I203x55}')

I203x63 = Parameter(name = 'I203x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru36*complexconjugate(Ru66)',
                    texname = '\\text{I203x63}')

I203x66 = Parameter(name = 'I203x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru66*complexconjugate(Ru66)',
                    texname = '\\text{I203x66}')

I21x11 = Parameter(name = 'I21x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd14*yd11*complexconjugate(Rd11)',
                   texname = '\\text{I21x11}')

I21x14 = Parameter(name = 'I21x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd44*yd11*complexconjugate(Rd11)',
                   texname = '\\text{I21x14}')

I21x22 = Parameter(name = 'I21x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd25*yd22*complexconjugate(Rd22)',
                   texname = '\\text{I21x22}')

I21x25 = Parameter(name = 'I21x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd55*yd22*complexconjugate(Rd22)',
                   texname = '\\text{I21x25}')

I21x33 = Parameter(name = 'I21x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd36*yd33*complexconjugate(Rd33)',
                   texname = '\\text{I21x33}')

I21x36 = Parameter(name = 'I21x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd66*yd33*complexconjugate(Rd33)',
                   texname = '\\text{I21x36}')

I21x41 = Parameter(name = 'I21x41',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd14*yd11*complexconjugate(Rd41)',
                   texname = '\\text{I21x41}')

I21x44 = Parameter(name = 'I21x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd44*yd11*complexconjugate(Rd41)',
                   texname = '\\text{I21x44}')

I21x52 = Parameter(name = 'I21x52',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd25*yd22*complexconjugate(Rd52)',
                   texname = '\\text{I21x52}')

I21x55 = Parameter(name = 'I21x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd55*yd22*complexconjugate(Rd52)',
                   texname = '\\text{I21x55}')

I21x63 = Parameter(name = 'I21x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd36*yd33*complexconjugate(Rd63)',
                   texname = '\\text{I21x63}')

I21x66 = Parameter(name = 'I21x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd66*yd33*complexconjugate(Rd63)',
                   texname = '\\text{I21x66}')

I22x11 = Parameter(name = 'I22x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd14*yd11*complexconjugate(Rd14)*complexconjugate(yd11)',
                   texname = '\\text{I22x11}')

I22x14 = Parameter(name = 'I22x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd44*yd11*complexconjugate(Rd14)*complexconjugate(yd11)',
                   texname = '\\text{I22x14}')

I22x22 = Parameter(name = 'I22x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd25*yd22*complexconjugate(Rd25)*complexconjugate(yd22)',
                   texname = '\\text{I22x22}')

I22x25 = Parameter(name = 'I22x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd55*yd22*complexconjugate(Rd25)*complexconjugate(yd22)',
                   texname = '\\text{I22x25}')

I22x33 = Parameter(name = 'I22x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd36*yd33*complexconjugate(Rd36)*complexconjugate(yd33)',
                   texname = '\\text{I22x33}')

I22x36 = Parameter(name = 'I22x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd66*yd33*complexconjugate(Rd36)*complexconjugate(yd33)',
                   texname = '\\text{I22x36}')

I22x41 = Parameter(name = 'I22x41',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd14*yd11*complexconjugate(Rd44)*complexconjugate(yd11)',
                   texname = '\\text{I22x41}')

I22x44 = Parameter(name = 'I22x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd44*yd11*complexconjugate(Rd44)*complexconjugate(yd11)',
                   texname = '\\text{I22x44}')

I22x52 = Parameter(name = 'I22x52',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd25*yd22*complexconjugate(Rd55)*complexconjugate(yd22)',
                   texname = '\\text{I22x52}')

I22x55 = Parameter(name = 'I22x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd55*yd22*complexconjugate(Rd55)*complexconjugate(yd22)',
                   texname = '\\text{I22x55}')

I22x63 = Parameter(name = 'I22x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd36*yd33*complexconjugate(Rd66)*complexconjugate(yd33)',
                   texname = '\\text{I22x63}')

I22x66 = Parameter(name = 'I22x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd66*yd33*complexconjugate(Rd66)*complexconjugate(yd33)',
                   texname = '\\text{I22x66}')

I23x11 = Parameter(name = 'I23x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd11*yd11*complexconjugate(Rd11)*complexconjugate(yd11)',
                   texname = '\\text{I23x11}')

I23x14 = Parameter(name = 'I23x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd41*yd11*complexconjugate(Rd11)*complexconjugate(yd11)',
                   texname = '\\text{I23x14}')

I23x22 = Parameter(name = 'I23x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd22*yd22*complexconjugate(Rd22)*complexconjugate(yd22)',
                   texname = '\\text{I23x22}')

I23x25 = Parameter(name = 'I23x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd52*yd22*complexconjugate(Rd22)*complexconjugate(yd22)',
                   texname = '\\text{I23x25}')

I23x33 = Parameter(name = 'I23x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd33*yd33*complexconjugate(Rd33)*complexconjugate(yd33)',
                   texname = '\\text{I23x33}')

I23x36 = Parameter(name = 'I23x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd63*yd33*complexconjugate(Rd33)*complexconjugate(yd33)',
                   texname = '\\text{I23x36}')

I23x41 = Parameter(name = 'I23x41',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd11*yd11*complexconjugate(Rd41)*complexconjugate(yd11)',
                   texname = '\\text{I23x41}')

I23x44 = Parameter(name = 'I23x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd41*yd11*complexconjugate(Rd41)*complexconjugate(yd11)',
                   texname = '\\text{I23x44}')

I23x52 = Parameter(name = 'I23x52',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd22*yd22*complexconjugate(Rd52)*complexconjugate(yd22)',
                   texname = '\\text{I23x52}')

I23x55 = Parameter(name = 'I23x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd52*yd22*complexconjugate(Rd52)*complexconjugate(yd22)',
                   texname = '\\text{I23x55}')

I23x63 = Parameter(name = 'I23x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd33*yd33*complexconjugate(Rd63)*complexconjugate(yd33)',
                   texname = '\\text{I23x63}')

I23x66 = Parameter(name = 'I23x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd63*yd33*complexconjugate(Rd63)*complexconjugate(yd33)',
                   texname = '\\text{I23x66}')

I24x11 = Parameter(name = 'I24x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd14*yd11*complexconjugate(Rd14)*complexconjugate(yd11)',
                   texname = '\\text{I24x11}')

I24x14 = Parameter(name = 'I24x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd44*yd11*complexconjugate(Rd14)*complexconjugate(yd11)',
                   texname = '\\text{I24x14}')

I24x22 = Parameter(name = 'I24x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd25*yd22*complexconjugate(Rd25)*complexconjugate(yd22)',
                   texname = '\\text{I24x22}')

I24x25 = Parameter(name = 'I24x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd55*yd22*complexconjugate(Rd25)*complexconjugate(yd22)',
                   texname = '\\text{I24x25}')

I24x33 = Parameter(name = 'I24x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd36*yd33*complexconjugate(Rd36)*complexconjugate(yd33)',
                   texname = '\\text{I24x33}')

I24x36 = Parameter(name = 'I24x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd66*yd33*complexconjugate(Rd36)*complexconjugate(yd33)',
                   texname = '\\text{I24x36}')

I24x41 = Parameter(name = 'I24x41',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd14*yd11*complexconjugate(Rd44)*complexconjugate(yd11)',
                   texname = '\\text{I24x41}')

I24x44 = Parameter(name = 'I24x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd44*yd11*complexconjugate(Rd44)*complexconjugate(yd11)',
                   texname = '\\text{I24x44}')

I24x52 = Parameter(name = 'I24x52',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd25*yd22*complexconjugate(Rd55)*complexconjugate(yd22)',
                   texname = '\\text{I24x52}')

I24x55 = Parameter(name = 'I24x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd55*yd22*complexconjugate(Rd55)*complexconjugate(yd22)',
                   texname = '\\text{I24x55}')

I24x63 = Parameter(name = 'I24x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd36*yd33*complexconjugate(Rd66)*complexconjugate(yd33)',
                   texname = '\\text{I24x63}')

I24x66 = Parameter(name = 'I24x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd66*yd33*complexconjugate(Rd66)*complexconjugate(yd33)',
                   texname = '\\text{I24x66}')

I25x11 = Parameter(name = 'I25x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM11*Rd11*yu11*complexconjugate(CKM11)*complexconjugate(Rd11)*complexconjugate(yu11)',
                   texname = '\\text{I25x11}')

I25x14 = Parameter(name = 'I25x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM11*Rd41*yu11*complexconjugate(CKM11)*complexconjugate(Rd11)*complexconjugate(yu11)',
                   texname = '\\text{I25x14}')

I25x22 = Parameter(name = 'I25x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM22*Rd22*yu22*complexconjugate(CKM22)*complexconjugate(Rd22)*complexconjugate(yu22)',
                   texname = '\\text{I25x22}')

I25x25 = Parameter(name = 'I25x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM22*Rd52*yu22*complexconjugate(CKM22)*complexconjugate(Rd22)*complexconjugate(yu22)',
                   texname = '\\text{I25x25}')

I25x33 = Parameter(name = 'I25x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*Rd33*yu33*complexconjugate(CKM33)*complexconjugate(Rd33)*complexconjugate(yu33)',
                   texname = '\\text{I25x33}')

I25x36 = Parameter(name = 'I25x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*Rd63*yu33*complexconjugate(CKM33)*complexconjugate(Rd33)*complexconjugate(yu33)',
                   texname = '\\text{I25x36}')

I25x41 = Parameter(name = 'I25x41',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM11*Rd11*yu11*complexconjugate(CKM11)*complexconjugate(Rd41)*complexconjugate(yu11)',
                   texname = '\\text{I25x41}')

I25x44 = Parameter(name = 'I25x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM11*Rd41*yu11*complexconjugate(CKM11)*complexconjugate(Rd41)*complexconjugate(yu11)',
                   texname = '\\text{I25x44}')

I25x52 = Parameter(name = 'I25x52',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM22*Rd22*yu22*complexconjugate(CKM22)*complexconjugate(Rd52)*complexconjugate(yu22)',
                   texname = '\\text{I25x52}')

I25x55 = Parameter(name = 'I25x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM22*Rd52*yu22*complexconjugate(CKM22)*complexconjugate(Rd52)*complexconjugate(yu22)',
                   texname = '\\text{I25x55}')

I25x63 = Parameter(name = 'I25x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*Rd33*yu33*complexconjugate(CKM33)*complexconjugate(Rd63)*complexconjugate(yu33)',
                   texname = '\\text{I25x63}')

I25x66 = Parameter(name = 'I25x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM33*Rd63*yu33*complexconjugate(CKM33)*complexconjugate(Rd63)*complexconjugate(yu33)',
                   texname = '\\text{I25x66}')

I26x11 = Parameter(name = 'I26x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd11*complexconjugate(Rd11)',
                   texname = '\\text{I26x11}')

I26x14 = Parameter(name = 'I26x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd41*complexconjugate(Rd11)',
                   texname = '\\text{I26x14}')

I26x22 = Parameter(name = 'I26x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd22*complexconjugate(Rd22)',
                   texname = '\\text{I26x22}')

I26x25 = Parameter(name = 'I26x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd52*complexconjugate(Rd22)',
                   texname = '\\text{I26x25}')

I26x33 = Parameter(name = 'I26x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd33*complexconjugate(Rd33)',
                   texname = '\\text{I26x33}')

I26x36 = Parameter(name = 'I26x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd63*complexconjugate(Rd33)',
                   texname = '\\text{I26x36}')

I26x41 = Parameter(name = 'I26x41',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd11*complexconjugate(Rd41)',
                   texname = '\\text{I26x41}')

I26x44 = Parameter(name = 'I26x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd41*complexconjugate(Rd41)',
                   texname = '\\text{I26x44}')

I26x52 = Parameter(name = 'I26x52',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd22*complexconjugate(Rd52)',
                   texname = '\\text{I26x52}')

I26x55 = Parameter(name = 'I26x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd52*complexconjugate(Rd52)',
                   texname = '\\text{I26x55}')

I26x63 = Parameter(name = 'I26x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd33*complexconjugate(Rd63)',
                   texname = '\\text{I26x63}')

I26x66 = Parameter(name = 'I26x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd63*complexconjugate(Rd63)',
                   texname = '\\text{I26x66}')

I27x11 = Parameter(name = 'I27x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd11*complexconjugate(Rd11)',
                   texname = '\\text{I27x11}')

I27x14 = Parameter(name = 'I27x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd41*complexconjugate(Rd11)',
                   texname = '\\text{I27x14}')

I27x22 = Parameter(name = 'I27x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd22*complexconjugate(Rd22)',
                   texname = '\\text{I27x22}')

I27x25 = Parameter(name = 'I27x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd52*complexconjugate(Rd22)',
                   texname = '\\text{I27x25}')

I27x33 = Parameter(name = 'I27x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd33*complexconjugate(Rd33)',
                   texname = '\\text{I27x33}')

I27x36 = Parameter(name = 'I27x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd63*complexconjugate(Rd33)',
                   texname = '\\text{I27x36}')

I27x41 = Parameter(name = 'I27x41',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd11*complexconjugate(Rd41)',
                   texname = '\\text{I27x41}')

I27x44 = Parameter(name = 'I27x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd41*complexconjugate(Rd41)',
                   texname = '\\text{I27x44}')

I27x52 = Parameter(name = 'I27x52',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd22*complexconjugate(Rd52)',
                   texname = '\\text{I27x52}')

I27x55 = Parameter(name = 'I27x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd52*complexconjugate(Rd52)',
                   texname = '\\text{I27x55}')

I27x63 = Parameter(name = 'I27x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd33*complexconjugate(Rd63)',
                   texname = '\\text{I27x63}')

I27x66 = Parameter(name = 'I27x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd63*complexconjugate(Rd63)',
                   texname = '\\text{I27x66}')

I28x11 = Parameter(name = 'I28x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd11*complexconjugate(Rd11)',
                   texname = '\\text{I28x11}')

I28x14 = Parameter(name = 'I28x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd41*complexconjugate(Rd11)',
                   texname = '\\text{I28x14}')

I28x22 = Parameter(name = 'I28x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd22*complexconjugate(Rd22)',
                   texname = '\\text{I28x22}')

I28x25 = Parameter(name = 'I28x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd52*complexconjugate(Rd22)',
                   texname = '\\text{I28x25}')

I28x33 = Parameter(name = 'I28x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd33*complexconjugate(Rd33)',
                   texname = '\\text{I28x33}')

I28x36 = Parameter(name = 'I28x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd63*complexconjugate(Rd33)',
                   texname = '\\text{I28x36}')

I28x41 = Parameter(name = 'I28x41',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd11*complexconjugate(Rd41)',
                   texname = '\\text{I28x41}')

I28x44 = Parameter(name = 'I28x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd41*complexconjugate(Rd41)',
                   texname = '\\text{I28x44}')

I28x52 = Parameter(name = 'I28x52',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd22*complexconjugate(Rd52)',
                   texname = '\\text{I28x52}')

I28x55 = Parameter(name = 'I28x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd52*complexconjugate(Rd52)',
                   texname = '\\text{I28x55}')

I28x63 = Parameter(name = 'I28x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd33*complexconjugate(Rd63)',
                   texname = '\\text{I28x63}')

I28x66 = Parameter(name = 'I28x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd63*complexconjugate(Rd63)',
                   texname = '\\text{I28x66}')

I29x11 = Parameter(name = 'I29x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd11*complexconjugate(Rd11)',
                   texname = '\\text{I29x11}')

I29x14 = Parameter(name = 'I29x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd41*complexconjugate(Rd11)',
                   texname = '\\text{I29x14}')

I29x22 = Parameter(name = 'I29x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd22*complexconjugate(Rd22)',
                   texname = '\\text{I29x22}')

I29x25 = Parameter(name = 'I29x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd52*complexconjugate(Rd22)',
                   texname = '\\text{I29x25}')

I29x33 = Parameter(name = 'I29x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd33*complexconjugate(Rd33)',
                   texname = '\\text{I29x33}')

I29x36 = Parameter(name = 'I29x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd63*complexconjugate(Rd33)',
                   texname = '\\text{I29x36}')

I29x41 = Parameter(name = 'I29x41',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd11*complexconjugate(Rd41)',
                   texname = '\\text{I29x41}')

I29x44 = Parameter(name = 'I29x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd41*complexconjugate(Rd41)',
                   texname = '\\text{I29x44}')

I29x52 = Parameter(name = 'I29x52',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd22*complexconjugate(Rd52)',
                   texname = '\\text{I29x52}')

I29x55 = Parameter(name = 'I29x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd52*complexconjugate(Rd52)',
                   texname = '\\text{I29x55}')

I29x63 = Parameter(name = 'I29x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd33*complexconjugate(Rd63)',
                   texname = '\\text{I29x63}')

I29x66 = Parameter(name = 'I29x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd63*complexconjugate(Rd63)',
                   texname = '\\text{I29x66}')

I3x11 = Parameter(name = 'I3x11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM11*complexconjugate(yd11)',
                  texname = '\\text{I3x11}')

I3x22 = Parameter(name = 'I3x22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM22*complexconjugate(yd22)',
                  texname = '\\text{I3x22}')

I3x33 = Parameter(name = 'I3x33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM33*complexconjugate(yd33)',
                  texname = '\\text{I3x33}')

I30x11 = Parameter(name = 'I30x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd14*complexconjugate(Rd14)',
                   texname = '\\text{I30x11}')

I30x14 = Parameter(name = 'I30x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd44*complexconjugate(Rd14)',
                   texname = '\\text{I30x14}')

I30x22 = Parameter(name = 'I30x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd25*complexconjugate(Rd25)',
                   texname = '\\text{I30x22}')

I30x25 = Parameter(name = 'I30x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd55*complexconjugate(Rd25)',
                   texname = '\\text{I30x25}')

I30x33 = Parameter(name = 'I30x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd36*complexconjugate(Rd36)',
                   texname = '\\text{I30x33}')

I30x36 = Parameter(name = 'I30x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd66*complexconjugate(Rd36)',
                   texname = '\\text{I30x36}')

I30x41 = Parameter(name = 'I30x41',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd14*complexconjugate(Rd44)',
                   texname = '\\text{I30x41}')

I30x44 = Parameter(name = 'I30x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd44*complexconjugate(Rd44)',
                   texname = '\\text{I30x44}')

I30x52 = Parameter(name = 'I30x52',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd25*complexconjugate(Rd55)',
                   texname = '\\text{I30x52}')

I30x55 = Parameter(name = 'I30x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd55*complexconjugate(Rd55)',
                   texname = '\\text{I30x55}')

I30x63 = Parameter(name = 'I30x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd36*complexconjugate(Rd66)',
                   texname = '\\text{I30x63}')

I30x66 = Parameter(name = 'I30x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd66*complexconjugate(Rd66)',
                   texname = '\\text{I30x66}')

I31x11 = Parameter(name = 'I31x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd11*complexconjugate(Rd11)',
                   texname = '\\text{I31x11}')

I31x14 = Parameter(name = 'I31x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd41*complexconjugate(Rd11)',
                   texname = '\\text{I31x14}')

I31x22 = Parameter(name = 'I31x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd22*complexconjugate(Rd22)',
                   texname = '\\text{I31x22}')

I31x25 = Parameter(name = 'I31x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd52*complexconjugate(Rd22)',
                   texname = '\\text{I31x25}')

I31x33 = Parameter(name = 'I31x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd33*complexconjugate(Rd33)',
                   texname = '\\text{I31x33}')

I31x36 = Parameter(name = 'I31x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd63*complexconjugate(Rd33)',
                   texname = '\\text{I31x36}')

I31x41 = Parameter(name = 'I31x41',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd11*complexconjugate(Rd41)',
                   texname = '\\text{I31x41}')

I31x44 = Parameter(name = 'I31x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd41*complexconjugate(Rd41)',
                   texname = '\\text{I31x44}')

I31x52 = Parameter(name = 'I31x52',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd22*complexconjugate(Rd52)',
                   texname = '\\text{I31x52}')

I31x55 = Parameter(name = 'I31x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd52*complexconjugate(Rd52)',
                   texname = '\\text{I31x55}')

I31x63 = Parameter(name = 'I31x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd33*complexconjugate(Rd63)',
                   texname = '\\text{I31x63}')

I31x66 = Parameter(name = 'I31x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd63*complexconjugate(Rd63)',
                   texname = '\\text{I31x66}')

I32x11 = Parameter(name = 'I32x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd14*complexconjugate(Rd14)',
                   texname = '\\text{I32x11}')

I32x14 = Parameter(name = 'I32x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd44*complexconjugate(Rd14)',
                   texname = '\\text{I32x14}')

I32x22 = Parameter(name = 'I32x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd25*complexconjugate(Rd25)',
                   texname = '\\text{I32x22}')

I32x25 = Parameter(name = 'I32x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd55*complexconjugate(Rd25)',
                   texname = '\\text{I32x25}')

I32x33 = Parameter(name = 'I32x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd36*complexconjugate(Rd36)',
                   texname = '\\text{I32x33}')

I32x36 = Parameter(name = 'I32x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd66*complexconjugate(Rd36)',
                   texname = '\\text{I32x36}')

I32x41 = Parameter(name = 'I32x41',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd14*complexconjugate(Rd44)',
                   texname = '\\text{I32x41}')

I32x44 = Parameter(name = 'I32x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd44*complexconjugate(Rd44)',
                   texname = '\\text{I32x44}')

I32x52 = Parameter(name = 'I32x52',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd25*complexconjugate(Rd55)',
                   texname = '\\text{I32x52}')

I32x55 = Parameter(name = 'I32x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd55*complexconjugate(Rd55)',
                   texname = '\\text{I32x55}')

I32x63 = Parameter(name = 'I32x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd36*complexconjugate(Rd66)',
                   texname = '\\text{I32x63}')

I32x66 = Parameter(name = 'I32x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd66*complexconjugate(Rd66)',
                   texname = '\\text{I32x66}')

I33x11 = Parameter(name = 'I33x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd14*complexconjugate(Rd14)',
                   texname = '\\text{I33x11}')

I33x14 = Parameter(name = 'I33x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd44*complexconjugate(Rd14)',
                   texname = '\\text{I33x14}')

I33x22 = Parameter(name = 'I33x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd25*complexconjugate(Rd25)',
                   texname = '\\text{I33x22}')

I33x25 = Parameter(name = 'I33x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd55*complexconjugate(Rd25)',
                   texname = '\\text{I33x25}')

I33x33 = Parameter(name = 'I33x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd36*complexconjugate(Rd36)',
                   texname = '\\text{I33x33}')

I33x36 = Parameter(name = 'I33x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd66*complexconjugate(Rd36)',
                   texname = '\\text{I33x36}')

I33x41 = Parameter(name = 'I33x41',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd14*complexconjugate(Rd44)',
                   texname = '\\text{I33x41}')

I33x44 = Parameter(name = 'I33x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd44*complexconjugate(Rd44)',
                   texname = '\\text{I33x44}')

I33x52 = Parameter(name = 'I33x52',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd25*complexconjugate(Rd55)',
                   texname = '\\text{I33x52}')

I33x55 = Parameter(name = 'I33x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd55*complexconjugate(Rd55)',
                   texname = '\\text{I33x55}')

I33x63 = Parameter(name = 'I33x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd36*complexconjugate(Rd66)',
                   texname = '\\text{I33x63}')

I33x66 = Parameter(name = 'I33x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd66*complexconjugate(Rd66)',
                   texname = '\\text{I33x66}')

I34x11 = Parameter(name = 'I34x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd14*complexconjugate(Rd14)',
                   texname = '\\text{I34x11}')

I34x14 = Parameter(name = 'I34x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd44*complexconjugate(Rd14)',
                   texname = '\\text{I34x14}')

I34x22 = Parameter(name = 'I34x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd25*complexconjugate(Rd25)',
                   texname = '\\text{I34x22}')

I34x25 = Parameter(name = 'I34x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd55*complexconjugate(Rd25)',
                   texname = '\\text{I34x25}')

I34x33 = Parameter(name = 'I34x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd36*complexconjugate(Rd36)',
                   texname = '\\text{I34x33}')

I34x36 = Parameter(name = 'I34x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd66*complexconjugate(Rd36)',
                   texname = '\\text{I34x36}')

I34x41 = Parameter(name = 'I34x41',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd14*complexconjugate(Rd44)',
                   texname = '\\text{I34x41}')

I34x44 = Parameter(name = 'I34x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd44*complexconjugate(Rd44)',
                   texname = '\\text{I34x44}')

I34x52 = Parameter(name = 'I34x52',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd25*complexconjugate(Rd55)',
                   texname = '\\text{I34x52}')

I34x55 = Parameter(name = 'I34x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd55*complexconjugate(Rd55)',
                   texname = '\\text{I34x55}')

I34x63 = Parameter(name = 'I34x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd36*complexconjugate(Rd66)',
                   texname = '\\text{I34x63}')

I34x66 = Parameter(name = 'I34x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd66*complexconjugate(Rd66)',
                   texname = '\\text{I34x66}')

I35x11 = Parameter(name = 'I35x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd14*complexconjugate(Rd14)',
                   texname = '\\text{I35x11}')

I35x14 = Parameter(name = 'I35x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd44*complexconjugate(Rd14)',
                   texname = '\\text{I35x14}')

I35x22 = Parameter(name = 'I35x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd25*complexconjugate(Rd25)',
                   texname = '\\text{I35x22}')

I35x25 = Parameter(name = 'I35x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd55*complexconjugate(Rd25)',
                   texname = '\\text{I35x25}')

I35x33 = Parameter(name = 'I35x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd36*complexconjugate(Rd36)',
                   texname = '\\text{I35x33}')

I35x36 = Parameter(name = 'I35x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd66*complexconjugate(Rd36)',
                   texname = '\\text{I35x36}')

I35x41 = Parameter(name = 'I35x41',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd14*complexconjugate(Rd44)',
                   texname = '\\text{I35x41}')

I35x44 = Parameter(name = 'I35x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd44*complexconjugate(Rd44)',
                   texname = '\\text{I35x44}')

I35x52 = Parameter(name = 'I35x52',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd25*complexconjugate(Rd55)',
                   texname = '\\text{I35x52}')

I35x55 = Parameter(name = 'I35x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd55*complexconjugate(Rd55)',
                   texname = '\\text{I35x55}')

I35x63 = Parameter(name = 'I35x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd36*complexconjugate(Rd66)',
                   texname = '\\text{I35x63}')

I35x66 = Parameter(name = 'I35x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd66*complexconjugate(Rd66)',
                   texname = '\\text{I35x66}')

I36x11 = Parameter(name = 'I36x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd14*complexconjugate(Rd14)',
                   texname = '\\text{I36x11}')

I36x14 = Parameter(name = 'I36x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd44*complexconjugate(Rd14)',
                   texname = '\\text{I36x14}')

I36x22 = Parameter(name = 'I36x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd25*complexconjugate(Rd25)',
                   texname = '\\text{I36x22}')

I36x25 = Parameter(name = 'I36x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd55*complexconjugate(Rd25)',
                   texname = '\\text{I36x25}')

I36x33 = Parameter(name = 'I36x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd36*complexconjugate(Rd36)',
                   texname = '\\text{I36x33}')

I36x36 = Parameter(name = 'I36x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd66*complexconjugate(Rd36)',
                   texname = '\\text{I36x36}')

I36x41 = Parameter(name = 'I36x41',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd14*complexconjugate(Rd44)',
                   texname = '\\text{I36x41}')

I36x44 = Parameter(name = 'I36x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd44*complexconjugate(Rd44)',
                   texname = '\\text{I36x44}')

I36x52 = Parameter(name = 'I36x52',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd25*complexconjugate(Rd55)',
                   texname = '\\text{I36x52}')

I36x55 = Parameter(name = 'I36x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd55*complexconjugate(Rd55)',
                   texname = '\\text{I36x55}')

I36x63 = Parameter(name = 'I36x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd36*complexconjugate(Rd66)',
                   texname = '\\text{I36x63}')

I36x66 = Parameter(name = 'I36x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd66*complexconjugate(Rd66)',
                   texname = '\\text{I36x66}')

I37x11 = Parameter(name = 'I37x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd11*complexconjugate(Rd14)*complexconjugate(yd11)',
                   texname = '\\text{I37x11}')

I37x14 = Parameter(name = 'I37x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd41*complexconjugate(Rd14)*complexconjugate(yd11)',
                   texname = '\\text{I37x14}')

I37x22 = Parameter(name = 'I37x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd22*complexconjugate(Rd25)*complexconjugate(yd22)',
                   texname = '\\text{I37x22}')

I37x25 = Parameter(name = 'I37x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd52*complexconjugate(Rd25)*complexconjugate(yd22)',
                   texname = '\\text{I37x25}')

I37x33 = Parameter(name = 'I37x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd33*complexconjugate(Rd36)*complexconjugate(yd33)',
                   texname = '\\text{I37x33}')

I37x36 = Parameter(name = 'I37x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd63*complexconjugate(Rd36)*complexconjugate(yd33)',
                   texname = '\\text{I37x36}')

I37x41 = Parameter(name = 'I37x41',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd11*complexconjugate(Rd44)*complexconjugate(yd11)',
                   texname = '\\text{I37x41}')

I37x44 = Parameter(name = 'I37x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd41*complexconjugate(Rd44)*complexconjugate(yd11)',
                   texname = '\\text{I37x44}')

I37x52 = Parameter(name = 'I37x52',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd22*complexconjugate(Rd55)*complexconjugate(yd22)',
                   texname = '\\text{I37x52}')

I37x55 = Parameter(name = 'I37x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd52*complexconjugate(Rd55)*complexconjugate(yd22)',
                   texname = '\\text{I37x55}')

I37x63 = Parameter(name = 'I37x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd33*complexconjugate(Rd66)*complexconjugate(yd33)',
                   texname = '\\text{I37x63}')

I37x66 = Parameter(name = 'I37x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd63*complexconjugate(Rd66)*complexconjugate(yd33)',
                   texname = '\\text{I37x66}')

I38x11 = Parameter(name = 'I38x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd14*yd11*complexconjugate(Rd11)',
                   texname = '\\text{I38x11}')

I38x14 = Parameter(name = 'I38x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd44*yd11*complexconjugate(Rd11)',
                   texname = '\\text{I38x14}')

I38x22 = Parameter(name = 'I38x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd25*yd22*complexconjugate(Rd22)',
                   texname = '\\text{I38x22}')

I38x25 = Parameter(name = 'I38x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd55*yd22*complexconjugate(Rd22)',
                   texname = '\\text{I38x25}')

I38x33 = Parameter(name = 'I38x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd36*yd33*complexconjugate(Rd33)',
                   texname = '\\text{I38x33}')

I38x36 = Parameter(name = 'I38x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd66*yd33*complexconjugate(Rd33)',
                   texname = '\\text{I38x36}')

I38x41 = Parameter(name = 'I38x41',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd14*yd11*complexconjugate(Rd41)',
                   texname = '\\text{I38x41}')

I38x44 = Parameter(name = 'I38x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd44*yd11*complexconjugate(Rd41)',
                   texname = '\\text{I38x44}')

I38x52 = Parameter(name = 'I38x52',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd25*yd22*complexconjugate(Rd52)',
                   texname = '\\text{I38x52}')

I38x55 = Parameter(name = 'I38x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd55*yd22*complexconjugate(Rd52)',
                   texname = '\\text{I38x55}')

I38x63 = Parameter(name = 'I38x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd36*yd33*complexconjugate(Rd63)',
                   texname = '\\text{I38x63}')

I38x66 = Parameter(name = 'I38x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd66*yd33*complexconjugate(Rd63)',
                   texname = '\\text{I38x66}')

I39x11 = Parameter(name = 'I39x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd11*complexconjugate(Rd14)*complexconjugate(yd11)',
                   texname = '\\text{I39x11}')

I39x14 = Parameter(name = 'I39x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd41*complexconjugate(Rd14)*complexconjugate(yd11)',
                   texname = '\\text{I39x14}')

I39x22 = Parameter(name = 'I39x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd22*complexconjugate(Rd25)*complexconjugate(yd22)',
                   texname = '\\text{I39x22}')

I39x25 = Parameter(name = 'I39x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd52*complexconjugate(Rd25)*complexconjugate(yd22)',
                   texname = '\\text{I39x25}')

I39x33 = Parameter(name = 'I39x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd33*complexconjugate(Rd36)*complexconjugate(yd33)',
                   texname = '\\text{I39x33}')

I39x36 = Parameter(name = 'I39x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd63*complexconjugate(Rd36)*complexconjugate(yd33)',
                   texname = '\\text{I39x36}')

I39x41 = Parameter(name = 'I39x41',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd11*complexconjugate(Rd44)*complexconjugate(yd11)',
                   texname = '\\text{I39x41}')

I39x44 = Parameter(name = 'I39x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd41*complexconjugate(Rd44)*complexconjugate(yd11)',
                   texname = '\\text{I39x44}')

I39x52 = Parameter(name = 'I39x52',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd22*complexconjugate(Rd55)*complexconjugate(yd22)',
                   texname = '\\text{I39x52}')

I39x55 = Parameter(name = 'I39x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd52*complexconjugate(Rd55)*complexconjugate(yd22)',
                   texname = '\\text{I39x55}')

I39x63 = Parameter(name = 'I39x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd33*complexconjugate(Rd66)*complexconjugate(yd33)',
                   texname = '\\text{I39x63}')

I39x66 = Parameter(name = 'I39x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd63*complexconjugate(Rd66)*complexconjugate(yd33)',
                   texname = '\\text{I39x66}')

I4x11 = Parameter(name = 'I4x11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM11*yu11',
                  texname = '\\text{I4x11}')

I4x22 = Parameter(name = 'I4x22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM22*yu22',
                  texname = '\\text{I4x22}')

I4x33 = Parameter(name = 'I4x33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM33*yu33',
                  texname = '\\text{I4x33}')

I40x11 = Parameter(name = 'I40x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd14*yd11*complexconjugate(Rd11)',
                   texname = '\\text{I40x11}')

I40x14 = Parameter(name = 'I40x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd44*yd11*complexconjugate(Rd11)',
                   texname = '\\text{I40x14}')

I40x22 = Parameter(name = 'I40x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd25*yd22*complexconjugate(Rd22)',
                   texname = '\\text{I40x22}')

I40x25 = Parameter(name = 'I40x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd55*yd22*complexconjugate(Rd22)',
                   texname = '\\text{I40x25}')

I40x33 = Parameter(name = 'I40x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd36*yd33*complexconjugate(Rd33)',
                   texname = '\\text{I40x33}')

I40x36 = Parameter(name = 'I40x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd66*yd33*complexconjugate(Rd33)',
                   texname = '\\text{I40x36}')

I40x41 = Parameter(name = 'I40x41',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd14*yd11*complexconjugate(Rd41)',
                   texname = '\\text{I40x41}')

I40x44 = Parameter(name = 'I40x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd44*yd11*complexconjugate(Rd41)',
                   texname = '\\text{I40x44}')

I40x52 = Parameter(name = 'I40x52',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd25*yd22*complexconjugate(Rd52)',
                   texname = '\\text{I40x52}')

I40x55 = Parameter(name = 'I40x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd55*yd22*complexconjugate(Rd52)',
                   texname = '\\text{I40x55}')

I40x63 = Parameter(name = 'I40x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd36*yd33*complexconjugate(Rd63)',
                   texname = '\\text{I40x63}')

I40x66 = Parameter(name = 'I40x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd66*yd33*complexconjugate(Rd63)',
                   texname = '\\text{I40x66}')

I41x11 = Parameter(name = 'I41x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd11*complexconjugate(Rd14)*complexconjugate(yd11)',
                   texname = '\\text{I41x11}')

I41x14 = Parameter(name = 'I41x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd41*complexconjugate(Rd14)*complexconjugate(yd11)',
                   texname = '\\text{I41x14}')

I41x22 = Parameter(name = 'I41x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd22*complexconjugate(Rd25)*complexconjugate(yd22)',
                   texname = '\\text{I41x22}')

I41x25 = Parameter(name = 'I41x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd52*complexconjugate(Rd25)*complexconjugate(yd22)',
                   texname = '\\text{I41x25}')

I41x33 = Parameter(name = 'I41x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd33*complexconjugate(Rd36)*complexconjugate(yd33)',
                   texname = '\\text{I41x33}')

I41x36 = Parameter(name = 'I41x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd63*complexconjugate(Rd36)*complexconjugate(yd33)',
                   texname = '\\text{I41x36}')

I41x41 = Parameter(name = 'I41x41',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd11*complexconjugate(Rd44)*complexconjugate(yd11)',
                   texname = '\\text{I41x41}')

I41x44 = Parameter(name = 'I41x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd41*complexconjugate(Rd44)*complexconjugate(yd11)',
                   texname = '\\text{I41x44}')

I41x52 = Parameter(name = 'I41x52',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd22*complexconjugate(Rd55)*complexconjugate(yd22)',
                   texname = '\\text{I41x52}')

I41x55 = Parameter(name = 'I41x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd52*complexconjugate(Rd55)*complexconjugate(yd22)',
                   texname = '\\text{I41x55}')

I41x63 = Parameter(name = 'I41x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd33*complexconjugate(Rd66)*complexconjugate(yd33)',
                   texname = '\\text{I41x63}')

I41x66 = Parameter(name = 'I41x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd63*complexconjugate(Rd66)*complexconjugate(yd33)',
                   texname = '\\text{I41x66}')

I42x11 = Parameter(name = 'I42x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd14*yd11*complexconjugate(Rd11)',
                   texname = '\\text{I42x11}')

I42x14 = Parameter(name = 'I42x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd44*yd11*complexconjugate(Rd11)',
                   texname = '\\text{I42x14}')

I42x22 = Parameter(name = 'I42x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd25*yd22*complexconjugate(Rd22)',
                   texname = '\\text{I42x22}')

I42x25 = Parameter(name = 'I42x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd55*yd22*complexconjugate(Rd22)',
                   texname = '\\text{I42x25}')

I42x33 = Parameter(name = 'I42x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd36*yd33*complexconjugate(Rd33)',
                   texname = '\\text{I42x33}')

I42x36 = Parameter(name = 'I42x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd66*yd33*complexconjugate(Rd33)',
                   texname = '\\text{I42x36}')

I42x41 = Parameter(name = 'I42x41',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd14*yd11*complexconjugate(Rd41)',
                   texname = '\\text{I42x41}')

I42x44 = Parameter(name = 'I42x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd44*yd11*complexconjugate(Rd41)',
                   texname = '\\text{I42x44}')

I42x52 = Parameter(name = 'I42x52',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd25*yd22*complexconjugate(Rd52)',
                   texname = '\\text{I42x52}')

I42x55 = Parameter(name = 'I42x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd55*yd22*complexconjugate(Rd52)',
                   texname = '\\text{I42x55}')

I42x63 = Parameter(name = 'I42x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd36*yd33*complexconjugate(Rd63)',
                   texname = '\\text{I42x63}')

I42x66 = Parameter(name = 'I42x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd66*yd33*complexconjugate(Rd63)',
                   texname = '\\text{I42x66}')

I43x11 = Parameter(name = 'I43x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd11*complexconjugate(Rd14)*complexconjugate(yd11)',
                   texname = '\\text{I43x11}')

I43x14 = Parameter(name = 'I43x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd41*complexconjugate(Rd14)*complexconjugate(yd11)',
                   texname = '\\text{I43x14}')

I43x22 = Parameter(name = 'I43x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd22*complexconjugate(Rd25)*complexconjugate(yd22)',
                   texname = '\\text{I43x22}')

I43x25 = Parameter(name = 'I43x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd52*complexconjugate(Rd25)*complexconjugate(yd22)',
                   texname = '\\text{I43x25}')

I43x33 = Parameter(name = 'I43x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd33*complexconjugate(Rd36)*complexconjugate(yd33)',
                   texname = '\\text{I43x33}')

I43x36 = Parameter(name = 'I43x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd63*complexconjugate(Rd36)*complexconjugate(yd33)',
                   texname = '\\text{I43x36}')

I43x41 = Parameter(name = 'I43x41',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd11*complexconjugate(Rd44)*complexconjugate(yd11)',
                   texname = '\\text{I43x41}')

I43x44 = Parameter(name = 'I43x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd41*complexconjugate(Rd44)*complexconjugate(yd11)',
                   texname = '\\text{I43x44}')

I43x52 = Parameter(name = 'I43x52',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd22*complexconjugate(Rd55)*complexconjugate(yd22)',
                   texname = '\\text{I43x52}')

I43x55 = Parameter(name = 'I43x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd52*complexconjugate(Rd55)*complexconjugate(yd22)',
                   texname = '\\text{I43x55}')

I43x63 = Parameter(name = 'I43x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd33*complexconjugate(Rd66)*complexconjugate(yd33)',
                   texname = '\\text{I43x63}')

I43x66 = Parameter(name = 'I43x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd63*complexconjugate(Rd66)*complexconjugate(yd33)',
                   texname = '\\text{I43x66}')

I44x11 = Parameter(name = 'I44x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd14*yd11*complexconjugate(Rd11)',
                   texname = '\\text{I44x11}')

I44x14 = Parameter(name = 'I44x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd44*yd11*complexconjugate(Rd11)',
                   texname = '\\text{I44x14}')

I44x22 = Parameter(name = 'I44x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd25*yd22*complexconjugate(Rd22)',
                   texname = '\\text{I44x22}')

I44x25 = Parameter(name = 'I44x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd55*yd22*complexconjugate(Rd22)',
                   texname = '\\text{I44x25}')

I44x33 = Parameter(name = 'I44x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd36*yd33*complexconjugate(Rd33)',
                   texname = '\\text{I44x33}')

I44x36 = Parameter(name = 'I44x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd66*yd33*complexconjugate(Rd33)',
                   texname = '\\text{I44x36}')

I44x41 = Parameter(name = 'I44x41',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd14*yd11*complexconjugate(Rd41)',
                   texname = '\\text{I44x41}')

I44x44 = Parameter(name = 'I44x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd44*yd11*complexconjugate(Rd41)',
                   texname = '\\text{I44x44}')

I44x52 = Parameter(name = 'I44x52',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd25*yd22*complexconjugate(Rd52)',
                   texname = '\\text{I44x52}')

I44x55 = Parameter(name = 'I44x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd55*yd22*complexconjugate(Rd52)',
                   texname = '\\text{I44x55}')

I44x63 = Parameter(name = 'I44x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd36*yd33*complexconjugate(Rd63)',
                   texname = '\\text{I44x63}')

I44x66 = Parameter(name = 'I44x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd66*yd33*complexconjugate(Rd63)',
                   texname = '\\text{I44x66}')

I45x11 = Parameter(name = 'I45x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(Rl14)*complexconjugate(ye11)',
                   texname = '\\text{I45x11}')

I45x14 = Parameter(name = 'I45x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(Rl44)*complexconjugate(ye11)',
                   texname = '\\text{I45x14}')

I45x22 = Parameter(name = 'I45x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(Rl25)*complexconjugate(ye22)',
                   texname = '\\text{I45x22}')

I45x25 = Parameter(name = 'I45x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(Rl55)*complexconjugate(ye22)',
                   texname = '\\text{I45x25}')

I45x33 = Parameter(name = 'I45x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(Rl36)*complexconjugate(ye33)',
                   texname = '\\text{I45x33}')

I45x36 = Parameter(name = 'I45x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(Rl66)*complexconjugate(ye33)',
                   texname = '\\text{I45x36}')

I46x11 = Parameter(name = 'I46x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'ye11*complexconjugate(Rl11)',
                   texname = '\\text{I46x11}')

I46x14 = Parameter(name = 'I46x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'ye11*complexconjugate(Rl41)',
                   texname = '\\text{I46x14}')

I46x22 = Parameter(name = 'I46x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'ye22*complexconjugate(Rl22)',
                   texname = '\\text{I46x22}')

I46x25 = Parameter(name = 'I46x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'ye22*complexconjugate(Rl52)',
                   texname = '\\text{I46x25}')

I46x33 = Parameter(name = 'I46x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'ye33*complexconjugate(Rl33)',
                   texname = '\\text{I46x33}')

I46x36 = Parameter(name = 'I46x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'ye33*complexconjugate(Rl63)',
                   texname = '\\text{I46x36}')

I47x11 = Parameter(name = 'I47x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl11*complexconjugate(Rl11)',
                   texname = '\\text{I47x11}')

I47x14 = Parameter(name = 'I47x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl41*complexconjugate(Rl11)',
                   texname = '\\text{I47x14}')

I47x22 = Parameter(name = 'I47x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl22*complexconjugate(Rl22)',
                   texname = '\\text{I47x22}')

I47x25 = Parameter(name = 'I47x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl52*complexconjugate(Rl22)',
                   texname = '\\text{I47x25}')

I47x33 = Parameter(name = 'I47x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl33*complexconjugate(Rl33)',
                   texname = '\\text{I47x33}')

I47x36 = Parameter(name = 'I47x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl63*complexconjugate(Rl33)',
                   texname = '\\text{I47x36}')

I47x41 = Parameter(name = 'I47x41',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl11*complexconjugate(Rl41)',
                   texname = '\\text{I47x41}')

I47x44 = Parameter(name = 'I47x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl41*complexconjugate(Rl41)',
                   texname = '\\text{I47x44}')

I47x52 = Parameter(name = 'I47x52',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl22*complexconjugate(Rl52)',
                   texname = '\\text{I47x52}')

I47x55 = Parameter(name = 'I47x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl52*complexconjugate(Rl52)',
                   texname = '\\text{I47x55}')

I47x63 = Parameter(name = 'I47x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl33*complexconjugate(Rl63)',
                   texname = '\\text{I47x63}')

I47x66 = Parameter(name = 'I47x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl63*complexconjugate(Rl63)',
                   texname = '\\text{I47x66}')

I48x11 = Parameter(name = 'I48x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl14*complexconjugate(Rl14)',
                   texname = '\\text{I48x11}')

I48x14 = Parameter(name = 'I48x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl44*complexconjugate(Rl14)',
                   texname = '\\text{I48x14}')

I48x22 = Parameter(name = 'I48x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl25*complexconjugate(Rl25)',
                   texname = '\\text{I48x22}')

I48x25 = Parameter(name = 'I48x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl55*complexconjugate(Rl25)',
                   texname = '\\text{I48x25}')

I48x33 = Parameter(name = 'I48x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl36*complexconjugate(Rl36)',
                   texname = '\\text{I48x33}')

I48x36 = Parameter(name = 'I48x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl66*complexconjugate(Rl36)',
                   texname = '\\text{I48x36}')

I48x41 = Parameter(name = 'I48x41',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl14*complexconjugate(Rl44)',
                   texname = '\\text{I48x41}')

I48x44 = Parameter(name = 'I48x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl44*complexconjugate(Rl44)',
                   texname = '\\text{I48x44}')

I48x52 = Parameter(name = 'I48x52',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl25*complexconjugate(Rl55)',
                   texname = '\\text{I48x52}')

I48x55 = Parameter(name = 'I48x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl55*complexconjugate(Rl55)',
                   texname = '\\text{I48x55}')

I48x63 = Parameter(name = 'I48x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl36*complexconjugate(Rl66)',
                   texname = '\\text{I48x63}')

I48x66 = Parameter(name = 'I48x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl66*complexconjugate(Rl66)',
                   texname = '\\text{I48x66}')

I49x11 = Parameter(name = 'I49x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl11*complexconjugate(ye11)',
                   texname = '\\text{I49x11}')

I49x14 = Parameter(name = 'I49x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl41*complexconjugate(ye11)',
                   texname = '\\text{I49x14}')

I49x22 = Parameter(name = 'I49x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl22*complexconjugate(ye22)',
                   texname = '\\text{I49x22}')

I49x25 = Parameter(name = 'I49x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl52*complexconjugate(ye22)',
                   texname = '\\text{I49x25}')

I49x33 = Parameter(name = 'I49x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl33*complexconjugate(ye33)',
                   texname = '\\text{I49x33}')

I49x36 = Parameter(name = 'I49x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl63*complexconjugate(ye33)',
                   texname = '\\text{I49x36}')

I5x11 = Parameter(name = 'I5x11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'complexconjugate(ye11)',
                  texname = '\\text{I5x11}')

I5x22 = Parameter(name = 'I5x22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'complexconjugate(ye22)',
                  texname = '\\text{I5x22}')

I5x33 = Parameter(name = 'I5x33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'complexconjugate(ye33)',
                  texname = '\\text{I5x33}')

I50x11 = Parameter(name = 'I50x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl14*ye11',
                   texname = '\\text{I50x11}')

I50x14 = Parameter(name = 'I50x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl44*ye11',
                   texname = '\\text{I50x14}')

I50x22 = Parameter(name = 'I50x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl25*ye22',
                   texname = '\\text{I50x22}')

I50x25 = Parameter(name = 'I50x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl55*ye22',
                   texname = '\\text{I50x25}')

I50x33 = Parameter(name = 'I50x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl36*ye33',
                   texname = '\\text{I50x33}')

I50x36 = Parameter(name = 'I50x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl66*ye33',
                   texname = '\\text{I50x36}')

I51x11 = Parameter(name = 'I51x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl11',
                   texname = '\\text{I51x11}')

I51x14 = Parameter(name = 'I51x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl41',
                   texname = '\\text{I51x14}')

I51x22 = Parameter(name = 'I51x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl22',
                   texname = '\\text{I51x22}')

I51x25 = Parameter(name = 'I51x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl52',
                   texname = '\\text{I51x25}')

I51x33 = Parameter(name = 'I51x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl33',
                   texname = '\\text{I51x33}')

I51x36 = Parameter(name = 'I51x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl63',
                   texname = '\\text{I51x36}')

I52x11 = Parameter(name = 'I52x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl14*ye11',
                   texname = '\\text{I52x11}')

I52x14 = Parameter(name = 'I52x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl44*ye11',
                   texname = '\\text{I52x14}')

I52x22 = Parameter(name = 'I52x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl25*ye22',
                   texname = '\\text{I52x22}')

I52x25 = Parameter(name = 'I52x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl55*ye22',
                   texname = '\\text{I52x25}')

I52x33 = Parameter(name = 'I52x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl36*ye33',
                   texname = '\\text{I52x33}')

I52x36 = Parameter(name = 'I52x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl66*ye33',
                   texname = '\\text{I52x36}')

I53x11 = Parameter(name = 'I53x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl11*complexconjugate(Rl11)',
                   texname = '\\text{I53x11}')

I53x14 = Parameter(name = 'I53x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl41*complexconjugate(Rl11)',
                   texname = '\\text{I53x14}')

I53x22 = Parameter(name = 'I53x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl22*complexconjugate(Rl22)',
                   texname = '\\text{I53x22}')

I53x25 = Parameter(name = 'I53x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl52*complexconjugate(Rl22)',
                   texname = '\\text{I53x25}')

I53x33 = Parameter(name = 'I53x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl33*complexconjugate(Rl33)',
                   texname = '\\text{I53x33}')

I53x36 = Parameter(name = 'I53x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl63*complexconjugate(Rl33)',
                   texname = '\\text{I53x36}')

I53x41 = Parameter(name = 'I53x41',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl11*complexconjugate(Rl41)',
                   texname = '\\text{I53x41}')

I53x44 = Parameter(name = 'I53x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl41*complexconjugate(Rl41)',
                   texname = '\\text{I53x44}')

I53x52 = Parameter(name = 'I53x52',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl22*complexconjugate(Rl52)',
                   texname = '\\text{I53x52}')

I53x55 = Parameter(name = 'I53x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl52*complexconjugate(Rl52)',
                   texname = '\\text{I53x55}')

I53x63 = Parameter(name = 'I53x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl33*complexconjugate(Rl63)',
                   texname = '\\text{I53x63}')

I53x66 = Parameter(name = 'I53x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl63*complexconjugate(Rl63)',
                   texname = '\\text{I53x66}')

I54x11 = Parameter(name = 'I54x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl14*complexconjugate(Rl14)',
                   texname = '\\text{I54x11}')

I54x14 = Parameter(name = 'I54x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl44*complexconjugate(Rl14)',
                   texname = '\\text{I54x14}')

I54x22 = Parameter(name = 'I54x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl25*complexconjugate(Rl25)',
                   texname = '\\text{I54x22}')

I54x25 = Parameter(name = 'I54x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl55*complexconjugate(Rl25)',
                   texname = '\\text{I54x25}')

I54x33 = Parameter(name = 'I54x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl36*complexconjugate(Rl36)',
                   texname = '\\text{I54x33}')

I54x36 = Parameter(name = 'I54x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl66*complexconjugate(Rl36)',
                   texname = '\\text{I54x36}')

I54x41 = Parameter(name = 'I54x41',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl14*complexconjugate(Rl44)',
                   texname = '\\text{I54x41}')

I54x44 = Parameter(name = 'I54x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl44*complexconjugate(Rl44)',
                   texname = '\\text{I54x44}')

I54x52 = Parameter(name = 'I54x52',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl25*complexconjugate(Rl55)',
                   texname = '\\text{I54x52}')

I54x55 = Parameter(name = 'I54x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl55*complexconjugate(Rl55)',
                   texname = '\\text{I54x55}')

I54x63 = Parameter(name = 'I54x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl36*complexconjugate(Rl66)',
                   texname = '\\text{I54x63}')

I54x66 = Parameter(name = 'I54x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl66*complexconjugate(Rl66)',
                   texname = '\\text{I54x66}')

I55x11 = Parameter(name = 'I55x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl11*complexconjugate(Rl14)*complexconjugate(te11)',
                   texname = '\\text{I55x11}')

I55x14 = Parameter(name = 'I55x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl41*complexconjugate(Rl14)*complexconjugate(te11)',
                   texname = '\\text{I55x14}')

I55x22 = Parameter(name = 'I55x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl22*complexconjugate(Rl25)*complexconjugate(te22)',
                   texname = '\\text{I55x22}')

I55x25 = Parameter(name = 'I55x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl52*complexconjugate(Rl25)*complexconjugate(te22)',
                   texname = '\\text{I55x25}')

I55x33 = Parameter(name = 'I55x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl33*complexconjugate(Rl36)*complexconjugate(te33)',
                   texname = '\\text{I55x33}')

I55x36 = Parameter(name = 'I55x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl63*complexconjugate(Rl36)*complexconjugate(te33)',
                   texname = '\\text{I55x36}')

I55x41 = Parameter(name = 'I55x41',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl11*complexconjugate(Rl44)*complexconjugate(te11)',
                   texname = '\\text{I55x41}')

I55x44 = Parameter(name = 'I55x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl41*complexconjugate(Rl44)*complexconjugate(te11)',
                   texname = '\\text{I55x44}')

I55x52 = Parameter(name = 'I55x52',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl22*complexconjugate(Rl55)*complexconjugate(te22)',
                   texname = '\\text{I55x52}')

I55x55 = Parameter(name = 'I55x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl52*complexconjugate(Rl55)*complexconjugate(te22)',
                   texname = '\\text{I55x55}')

I55x63 = Parameter(name = 'I55x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl33*complexconjugate(Rl66)*complexconjugate(te33)',
                   texname = '\\text{I55x63}')

I55x66 = Parameter(name = 'I55x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl63*complexconjugate(Rl66)*complexconjugate(te33)',
                   texname = '\\text{I55x66}')

I56x11 = Parameter(name = 'I56x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl11*complexconjugate(Rl14)*complexconjugate(ye11)',
                   texname = '\\text{I56x11}')

I56x14 = Parameter(name = 'I56x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl41*complexconjugate(Rl14)*complexconjugate(ye11)',
                   texname = '\\text{I56x14}')

I56x22 = Parameter(name = 'I56x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl22*complexconjugate(Rl25)*complexconjugate(ye22)',
                   texname = '\\text{I56x22}')

I56x25 = Parameter(name = 'I56x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl52*complexconjugate(Rl25)*complexconjugate(ye22)',
                   texname = '\\text{I56x25}')

I56x33 = Parameter(name = 'I56x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl33*complexconjugate(Rl36)*complexconjugate(ye33)',
                   texname = '\\text{I56x33}')

I56x36 = Parameter(name = 'I56x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl63*complexconjugate(Rl36)*complexconjugate(ye33)',
                   texname = '\\text{I56x36}')

I56x41 = Parameter(name = 'I56x41',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl11*complexconjugate(Rl44)*complexconjugate(ye11)',
                   texname = '\\text{I56x41}')

I56x44 = Parameter(name = 'I56x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl41*complexconjugate(Rl44)*complexconjugate(ye11)',
                   texname = '\\text{I56x44}')

I56x52 = Parameter(name = 'I56x52',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl22*complexconjugate(Rl55)*complexconjugate(ye22)',
                   texname = '\\text{I56x52}')

I56x55 = Parameter(name = 'I56x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl52*complexconjugate(Rl55)*complexconjugate(ye22)',
                   texname = '\\text{I56x55}')

I56x63 = Parameter(name = 'I56x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl33*complexconjugate(Rl66)*complexconjugate(ye33)',
                   texname = '\\text{I56x63}')

I56x66 = Parameter(name = 'I56x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl63*complexconjugate(Rl66)*complexconjugate(ye33)',
                   texname = '\\text{I56x66}')

I57x11 = Parameter(name = 'I57x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl14*te11*complexconjugate(Rl11)',
                   texname = '\\text{I57x11}')

I57x14 = Parameter(name = 'I57x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl44*te11*complexconjugate(Rl11)',
                   texname = '\\text{I57x14}')

I57x22 = Parameter(name = 'I57x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl25*te22*complexconjugate(Rl22)',
                   texname = '\\text{I57x22}')

I57x25 = Parameter(name = 'I57x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl55*te22*complexconjugate(Rl22)',
                   texname = '\\text{I57x25}')

I57x33 = Parameter(name = 'I57x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl36*te33*complexconjugate(Rl33)',
                   texname = '\\text{I57x33}')

I57x36 = Parameter(name = 'I57x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl66*te33*complexconjugate(Rl33)',
                   texname = '\\text{I57x36}')

I57x41 = Parameter(name = 'I57x41',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl14*te11*complexconjugate(Rl41)',
                   texname = '\\text{I57x41}')

I57x44 = Parameter(name = 'I57x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl44*te11*complexconjugate(Rl41)',
                   texname = '\\text{I57x44}')

I57x52 = Parameter(name = 'I57x52',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl25*te22*complexconjugate(Rl52)',
                   texname = '\\text{I57x52}')

I57x55 = Parameter(name = 'I57x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl55*te22*complexconjugate(Rl52)',
                   texname = '\\text{I57x55}')

I57x63 = Parameter(name = 'I57x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl36*te33*complexconjugate(Rl63)',
                   texname = '\\text{I57x63}')

I57x66 = Parameter(name = 'I57x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl66*te33*complexconjugate(Rl63)',
                   texname = '\\text{I57x66}')

I58x11 = Parameter(name = 'I58x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl11*ye11*complexconjugate(Rl11)*complexconjugate(ye11)',
                   texname = '\\text{I58x11}')

I58x14 = Parameter(name = 'I58x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl41*ye11*complexconjugate(Rl11)*complexconjugate(ye11)',
                   texname = '\\text{I58x14}')

I58x22 = Parameter(name = 'I58x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl22*ye22*complexconjugate(Rl22)*complexconjugate(ye22)',
                   texname = '\\text{I58x22}')

I58x25 = Parameter(name = 'I58x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl52*ye22*complexconjugate(Rl22)*complexconjugate(ye22)',
                   texname = '\\text{I58x25}')

I58x33 = Parameter(name = 'I58x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl33*ye33*complexconjugate(Rl33)*complexconjugate(ye33)',
                   texname = '\\text{I58x33}')

I58x36 = Parameter(name = 'I58x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl63*ye33*complexconjugate(Rl33)*complexconjugate(ye33)',
                   texname = '\\text{I58x36}')

I58x41 = Parameter(name = 'I58x41',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl11*ye11*complexconjugate(Rl41)*complexconjugate(ye11)',
                   texname = '\\text{I58x41}')

I58x44 = Parameter(name = 'I58x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl41*ye11*complexconjugate(Rl41)*complexconjugate(ye11)',
                   texname = '\\text{I58x44}')

I58x52 = Parameter(name = 'I58x52',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl22*ye22*complexconjugate(Rl52)*complexconjugate(ye22)',
                   texname = '\\text{I58x52}')

I58x55 = Parameter(name = 'I58x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl52*ye22*complexconjugate(Rl52)*complexconjugate(ye22)',
                   texname = '\\text{I58x55}')

I58x63 = Parameter(name = 'I58x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl33*ye33*complexconjugate(Rl63)*complexconjugate(ye33)',
                   texname = '\\text{I58x63}')

I58x66 = Parameter(name = 'I58x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl63*ye33*complexconjugate(Rl63)*complexconjugate(ye33)',
                   texname = '\\text{I58x66}')

I59x11 = Parameter(name = 'I59x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl14*ye11*complexconjugate(Rl11)',
                   texname = '\\text{I59x11}')

I59x14 = Parameter(name = 'I59x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl44*ye11*complexconjugate(Rl11)',
                   texname = '\\text{I59x14}')

I59x22 = Parameter(name = 'I59x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl25*ye22*complexconjugate(Rl22)',
                   texname = '\\text{I59x22}')

I59x25 = Parameter(name = 'I59x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl55*ye22*complexconjugate(Rl22)',
                   texname = '\\text{I59x25}')

I59x33 = Parameter(name = 'I59x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl36*ye33*complexconjugate(Rl33)',
                   texname = '\\text{I59x33}')

I59x36 = Parameter(name = 'I59x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl66*ye33*complexconjugate(Rl33)',
                   texname = '\\text{I59x36}')

I59x41 = Parameter(name = 'I59x41',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl14*ye11*complexconjugate(Rl41)',
                   texname = '\\text{I59x41}')

I59x44 = Parameter(name = 'I59x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl44*ye11*complexconjugate(Rl41)',
                   texname = '\\text{I59x44}')

I59x52 = Parameter(name = 'I59x52',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl25*ye22*complexconjugate(Rl52)',
                   texname = '\\text{I59x52}')

I59x55 = Parameter(name = 'I59x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl55*ye22*complexconjugate(Rl52)',
                   texname = '\\text{I59x55}')

I59x63 = Parameter(name = 'I59x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl36*ye33*complexconjugate(Rl63)',
                   texname = '\\text{I59x63}')

I59x66 = Parameter(name = 'I59x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl66*ye33*complexconjugate(Rl63)',
                   texname = '\\text{I59x66}')

I6x11 = Parameter(name = 'I6x11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'complexconjugate(Rd14)*complexconjugate(yd11)',
                  texname = '\\text{I6x11}')

I6x14 = Parameter(name = 'I6x14',
                  nature = 'internal',
                  type = 'complex',
                  value = 'complexconjugate(Rd44)*complexconjugate(yd11)',
                  texname = '\\text{I6x14}')

I6x22 = Parameter(name = 'I6x22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'complexconjugate(Rd25)*complexconjugate(yd22)',
                  texname = '\\text{I6x22}')

I6x25 = Parameter(name = 'I6x25',
                  nature = 'internal',
                  type = 'complex',
                  value = 'complexconjugate(Rd55)*complexconjugate(yd22)',
                  texname = '\\text{I6x25}')

I6x33 = Parameter(name = 'I6x33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'complexconjugate(Rd36)*complexconjugate(yd33)',
                  texname = '\\text{I6x33}')

I6x36 = Parameter(name = 'I6x36',
                  nature = 'internal',
                  type = 'complex',
                  value = 'complexconjugate(Rd66)*complexconjugate(yd33)',
                  texname = '\\text{I6x36}')

I60x11 = Parameter(name = 'I60x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl14*ye11*complexconjugate(Rl14)*complexconjugate(ye11)',
                   texname = '\\text{I60x11}')

I60x14 = Parameter(name = 'I60x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl44*ye11*complexconjugate(Rl14)*complexconjugate(ye11)',
                   texname = '\\text{I60x14}')

I60x22 = Parameter(name = 'I60x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl25*ye22*complexconjugate(Rl25)*complexconjugate(ye22)',
                   texname = '\\text{I60x22}')

I60x25 = Parameter(name = 'I60x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl55*ye22*complexconjugate(Rl25)*complexconjugate(ye22)',
                   texname = '\\text{I60x25}')

I60x33 = Parameter(name = 'I60x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl36*ye33*complexconjugate(Rl36)*complexconjugate(ye33)',
                   texname = '\\text{I60x33}')

I60x36 = Parameter(name = 'I60x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl66*ye33*complexconjugate(Rl36)*complexconjugate(ye33)',
                   texname = '\\text{I60x36}')

I60x41 = Parameter(name = 'I60x41',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl14*ye11*complexconjugate(Rl44)*complexconjugate(ye11)',
                   texname = '\\text{I60x41}')

I60x44 = Parameter(name = 'I60x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl44*ye11*complexconjugate(Rl44)*complexconjugate(ye11)',
                   texname = '\\text{I60x44}')

I60x52 = Parameter(name = 'I60x52',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl25*ye22*complexconjugate(Rl55)*complexconjugate(ye22)',
                   texname = '\\text{I60x52}')

I60x55 = Parameter(name = 'I60x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl55*ye22*complexconjugate(Rl55)*complexconjugate(ye22)',
                   texname = '\\text{I60x55}')

I60x63 = Parameter(name = 'I60x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl36*ye33*complexconjugate(Rl66)*complexconjugate(ye33)',
                   texname = '\\text{I60x63}')

I60x66 = Parameter(name = 'I60x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl66*ye33*complexconjugate(Rl66)*complexconjugate(ye33)',
                   texname = '\\text{I60x66}')

I61x11 = Parameter(name = 'I61x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl11*ye11*complexconjugate(Rl11)*complexconjugate(ye11)',
                   texname = '\\text{I61x11}')

I61x14 = Parameter(name = 'I61x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl41*ye11*complexconjugate(Rl11)*complexconjugate(ye11)',
                   texname = '\\text{I61x14}')

I61x22 = Parameter(name = 'I61x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl22*ye22*complexconjugate(Rl22)*complexconjugate(ye22)',
                   texname = '\\text{I61x22}')

I61x25 = Parameter(name = 'I61x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl52*ye22*complexconjugate(Rl22)*complexconjugate(ye22)',
                   texname = '\\text{I61x25}')

I61x33 = Parameter(name = 'I61x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl33*ye33*complexconjugate(Rl33)*complexconjugate(ye33)',
                   texname = '\\text{I61x33}')

I61x36 = Parameter(name = 'I61x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl63*ye33*complexconjugate(Rl33)*complexconjugate(ye33)',
                   texname = '\\text{I61x36}')

I61x41 = Parameter(name = 'I61x41',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl11*ye11*complexconjugate(Rl41)*complexconjugate(ye11)',
                   texname = '\\text{I61x41}')

I61x44 = Parameter(name = 'I61x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl41*ye11*complexconjugate(Rl41)*complexconjugate(ye11)',
                   texname = '\\text{I61x44}')

I61x52 = Parameter(name = 'I61x52',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl22*ye22*complexconjugate(Rl52)*complexconjugate(ye22)',
                   texname = '\\text{I61x52}')

I61x55 = Parameter(name = 'I61x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl52*ye22*complexconjugate(Rl52)*complexconjugate(ye22)',
                   texname = '\\text{I61x55}')

I61x63 = Parameter(name = 'I61x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl33*ye33*complexconjugate(Rl63)*complexconjugate(ye33)',
                   texname = '\\text{I61x63}')

I61x66 = Parameter(name = 'I61x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl63*ye33*complexconjugate(Rl63)*complexconjugate(ye33)',
                   texname = '\\text{I61x66}')

I62x11 = Parameter(name = 'I62x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl14*ye11*complexconjugate(Rl14)*complexconjugate(ye11)',
                   texname = '\\text{I62x11}')

I62x14 = Parameter(name = 'I62x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl44*ye11*complexconjugate(Rl14)*complexconjugate(ye11)',
                   texname = '\\text{I62x14}')

I62x22 = Parameter(name = 'I62x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl25*ye22*complexconjugate(Rl25)*complexconjugate(ye22)',
                   texname = '\\text{I62x22}')

I62x25 = Parameter(name = 'I62x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl55*ye22*complexconjugate(Rl25)*complexconjugate(ye22)',
                   texname = '\\text{I62x25}')

I62x33 = Parameter(name = 'I62x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl36*ye33*complexconjugate(Rl36)*complexconjugate(ye33)',
                   texname = '\\text{I62x33}')

I62x36 = Parameter(name = 'I62x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl66*ye33*complexconjugate(Rl36)*complexconjugate(ye33)',
                   texname = '\\text{I62x36}')

I62x41 = Parameter(name = 'I62x41',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl14*ye11*complexconjugate(Rl44)*complexconjugate(ye11)',
                   texname = '\\text{I62x41}')

I62x44 = Parameter(name = 'I62x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl44*ye11*complexconjugate(Rl44)*complexconjugate(ye11)',
                   texname = '\\text{I62x44}')

I62x52 = Parameter(name = 'I62x52',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl25*ye22*complexconjugate(Rl55)*complexconjugate(ye22)',
                   texname = '\\text{I62x52}')

I62x55 = Parameter(name = 'I62x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl55*ye22*complexconjugate(Rl55)*complexconjugate(ye22)',
                   texname = '\\text{I62x55}')

I62x63 = Parameter(name = 'I62x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl36*ye33*complexconjugate(Rl66)*complexconjugate(ye33)',
                   texname = '\\text{I62x63}')

I62x66 = Parameter(name = 'I62x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl66*ye33*complexconjugate(Rl66)*complexconjugate(ye33)',
                   texname = '\\text{I62x66}')

I63x11 = Parameter(name = 'I63x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd11*complexconjugate(Rd11)',
                   texname = '\\text{I63x11}')

I63x14 = Parameter(name = 'I63x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd41*complexconjugate(Rd11)',
                   texname = '\\text{I63x14}')

I63x22 = Parameter(name = 'I63x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd22*complexconjugate(Rd22)',
                   texname = '\\text{I63x22}')

I63x25 = Parameter(name = 'I63x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd52*complexconjugate(Rd22)',
                   texname = '\\text{I63x25}')

I63x33 = Parameter(name = 'I63x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd33*complexconjugate(Rd33)',
                   texname = '\\text{I63x33}')

I63x36 = Parameter(name = 'I63x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd63*complexconjugate(Rd33)',
                   texname = '\\text{I63x36}')

I63x41 = Parameter(name = 'I63x41',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd11*complexconjugate(Rd41)',
                   texname = '\\text{I63x41}')

I63x44 = Parameter(name = 'I63x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd41*complexconjugate(Rd41)',
                   texname = '\\text{I63x44}')

I63x52 = Parameter(name = 'I63x52',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd22*complexconjugate(Rd52)',
                   texname = '\\text{I63x52}')

I63x55 = Parameter(name = 'I63x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd52*complexconjugate(Rd52)',
                   texname = '\\text{I63x55}')

I63x63 = Parameter(name = 'I63x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd33*complexconjugate(Rd63)',
                   texname = '\\text{I63x63}')

I63x66 = Parameter(name = 'I63x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd63*complexconjugate(Rd63)',
                   texname = '\\text{I63x66}')

I64x11 = Parameter(name = 'I64x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl11*complexconjugate(Rl11)',
                   texname = '\\text{I64x11}')

I64x14 = Parameter(name = 'I64x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl41*complexconjugate(Rl11)',
                   texname = '\\text{I64x14}')

I64x22 = Parameter(name = 'I64x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl22*complexconjugate(Rl22)',
                   texname = '\\text{I64x22}')

I64x25 = Parameter(name = 'I64x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl52*complexconjugate(Rl22)',
                   texname = '\\text{I64x25}')

I64x33 = Parameter(name = 'I64x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl33*complexconjugate(Rl33)',
                   texname = '\\text{I64x33}')

I64x36 = Parameter(name = 'I64x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl63*complexconjugate(Rl33)',
                   texname = '\\text{I64x36}')

I64x41 = Parameter(name = 'I64x41',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl11*complexconjugate(Rl41)',
                   texname = '\\text{I64x41}')

I64x44 = Parameter(name = 'I64x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl41*complexconjugate(Rl41)',
                   texname = '\\text{I64x44}')

I64x52 = Parameter(name = 'I64x52',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl22*complexconjugate(Rl52)',
                   texname = '\\text{I64x52}')

I64x55 = Parameter(name = 'I64x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl52*complexconjugate(Rl52)',
                   texname = '\\text{I64x55}')

I64x63 = Parameter(name = 'I64x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl33*complexconjugate(Rl63)',
                   texname = '\\text{I64x63}')

I64x66 = Parameter(name = 'I64x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl63*complexconjugate(Rl63)',
                   texname = '\\text{I64x66}')

I65x11 = Parameter(name = 'I65x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd14*complexconjugate(Rd14)',
                   texname = '\\text{I65x11}')

I65x14 = Parameter(name = 'I65x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd44*complexconjugate(Rd14)',
                   texname = '\\text{I65x14}')

I65x22 = Parameter(name = 'I65x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd25*complexconjugate(Rd25)',
                   texname = '\\text{I65x22}')

I65x25 = Parameter(name = 'I65x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd55*complexconjugate(Rd25)',
                   texname = '\\text{I65x25}')

I65x33 = Parameter(name = 'I65x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd36*complexconjugate(Rd36)',
                   texname = '\\text{I65x33}')

I65x36 = Parameter(name = 'I65x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd66*complexconjugate(Rd36)',
                   texname = '\\text{I65x36}')

I65x41 = Parameter(name = 'I65x41',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd14*complexconjugate(Rd44)',
                   texname = '\\text{I65x41}')

I65x44 = Parameter(name = 'I65x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd44*complexconjugate(Rd44)',
                   texname = '\\text{I65x44}')

I65x52 = Parameter(name = 'I65x52',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd25*complexconjugate(Rd55)',
                   texname = '\\text{I65x52}')

I65x55 = Parameter(name = 'I65x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd55*complexconjugate(Rd55)',
                   texname = '\\text{I65x55}')

I65x63 = Parameter(name = 'I65x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd36*complexconjugate(Rd66)',
                   texname = '\\text{I65x63}')

I65x66 = Parameter(name = 'I65x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd66*complexconjugate(Rd66)',
                   texname = '\\text{I65x66}')

I66x11 = Parameter(name = 'I66x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl14*complexconjugate(Rl14)',
                   texname = '\\text{I66x11}')

I66x14 = Parameter(name = 'I66x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl44*complexconjugate(Rl14)',
                   texname = '\\text{I66x14}')

I66x22 = Parameter(name = 'I66x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl25*complexconjugate(Rl25)',
                   texname = '\\text{I66x22}')

I66x25 = Parameter(name = 'I66x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl55*complexconjugate(Rl25)',
                   texname = '\\text{I66x25}')

I66x33 = Parameter(name = 'I66x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl36*complexconjugate(Rl36)',
                   texname = '\\text{I66x33}')

I66x36 = Parameter(name = 'I66x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl66*complexconjugate(Rl36)',
                   texname = '\\text{I66x36}')

I66x41 = Parameter(name = 'I66x41',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl14*complexconjugate(Rl44)',
                   texname = '\\text{I66x41}')

I66x44 = Parameter(name = 'I66x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl44*complexconjugate(Rl44)',
                   texname = '\\text{I66x44}')

I66x52 = Parameter(name = 'I66x52',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl25*complexconjugate(Rl55)',
                   texname = '\\text{I66x52}')

I66x55 = Parameter(name = 'I66x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl55*complexconjugate(Rl55)',
                   texname = '\\text{I66x55}')

I66x63 = Parameter(name = 'I66x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl36*complexconjugate(Rl66)',
                   texname = '\\text{I66x63}')

I66x66 = Parameter(name = 'I66x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl66*complexconjugate(Rl66)',
                   texname = '\\text{I66x66}')

I67x11 = Parameter(name = 'I67x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl11*complexconjugate(Rl14)*complexconjugate(ye11)',
                   texname = '\\text{I67x11}')

I67x14 = Parameter(name = 'I67x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl41*complexconjugate(Rl14)*complexconjugate(ye11)',
                   texname = '\\text{I67x14}')

I67x22 = Parameter(name = 'I67x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl22*complexconjugate(Rl25)*complexconjugate(ye22)',
                   texname = '\\text{I67x22}')

I67x25 = Parameter(name = 'I67x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl52*complexconjugate(Rl25)*complexconjugate(ye22)',
                   texname = '\\text{I67x25}')

I67x33 = Parameter(name = 'I67x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl33*complexconjugate(Rl36)*complexconjugate(ye33)',
                   texname = '\\text{I67x33}')

I67x36 = Parameter(name = 'I67x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl63*complexconjugate(Rl36)*complexconjugate(ye33)',
                   texname = '\\text{I67x36}')

I67x41 = Parameter(name = 'I67x41',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl11*complexconjugate(Rl44)*complexconjugate(ye11)',
                   texname = '\\text{I67x41}')

I67x44 = Parameter(name = 'I67x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl41*complexconjugate(Rl44)*complexconjugate(ye11)',
                   texname = '\\text{I67x44}')

I67x52 = Parameter(name = 'I67x52',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl22*complexconjugate(Rl55)*complexconjugate(ye22)',
                   texname = '\\text{I67x52}')

I67x55 = Parameter(name = 'I67x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl52*complexconjugate(Rl55)*complexconjugate(ye22)',
                   texname = '\\text{I67x55}')

I67x63 = Parameter(name = 'I67x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl33*complexconjugate(Rl66)*complexconjugate(ye33)',
                   texname = '\\text{I67x63}')

I67x66 = Parameter(name = 'I67x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl63*complexconjugate(Rl66)*complexconjugate(ye33)',
                   texname = '\\text{I67x66}')

I68x11 = Parameter(name = 'I68x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd14*yd11*complexconjugate(Rd11)',
                   texname = '\\text{I68x11}')

I68x14 = Parameter(name = 'I68x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd44*yd11*complexconjugate(Rd11)',
                   texname = '\\text{I68x14}')

I68x22 = Parameter(name = 'I68x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd25*yd22*complexconjugate(Rd22)',
                   texname = '\\text{I68x22}')

I68x25 = Parameter(name = 'I68x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd55*yd22*complexconjugate(Rd22)',
                   texname = '\\text{I68x25}')

I68x33 = Parameter(name = 'I68x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd36*yd33*complexconjugate(Rd33)',
                   texname = '\\text{I68x33}')

I68x36 = Parameter(name = 'I68x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd66*yd33*complexconjugate(Rd33)',
                   texname = '\\text{I68x36}')

I68x41 = Parameter(name = 'I68x41',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd14*yd11*complexconjugate(Rd41)',
                   texname = '\\text{I68x41}')

I68x44 = Parameter(name = 'I68x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd44*yd11*complexconjugate(Rd41)',
                   texname = '\\text{I68x44}')

I68x52 = Parameter(name = 'I68x52',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd25*yd22*complexconjugate(Rd52)',
                   texname = '\\text{I68x52}')

I68x55 = Parameter(name = 'I68x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd55*yd22*complexconjugate(Rd52)',
                   texname = '\\text{I68x55}')

I68x63 = Parameter(name = 'I68x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd36*yd33*complexconjugate(Rd63)',
                   texname = '\\text{I68x63}')

I68x66 = Parameter(name = 'I68x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd66*yd33*complexconjugate(Rd63)',
                   texname = '\\text{I68x66}')

I69x11 = Parameter(name = 'I69x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd11*complexconjugate(Rd14)*complexconjugate(yd11)',
                   texname = '\\text{I69x11}')

I69x14 = Parameter(name = 'I69x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd41*complexconjugate(Rd14)*complexconjugate(yd11)',
                   texname = '\\text{I69x14}')

I69x22 = Parameter(name = 'I69x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd22*complexconjugate(Rd25)*complexconjugate(yd22)',
                   texname = '\\text{I69x22}')

I69x25 = Parameter(name = 'I69x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd52*complexconjugate(Rd25)*complexconjugate(yd22)',
                   texname = '\\text{I69x25}')

I69x33 = Parameter(name = 'I69x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd33*complexconjugate(Rd36)*complexconjugate(yd33)',
                   texname = '\\text{I69x33}')

I69x36 = Parameter(name = 'I69x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd63*complexconjugate(Rd36)*complexconjugate(yd33)',
                   texname = '\\text{I69x36}')

I69x41 = Parameter(name = 'I69x41',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd11*complexconjugate(Rd44)*complexconjugate(yd11)',
                   texname = '\\text{I69x41}')

I69x44 = Parameter(name = 'I69x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd41*complexconjugate(Rd44)*complexconjugate(yd11)',
                   texname = '\\text{I69x44}')

I69x52 = Parameter(name = 'I69x52',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd22*complexconjugate(Rd55)*complexconjugate(yd22)',
                   texname = '\\text{I69x52}')

I69x55 = Parameter(name = 'I69x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd52*complexconjugate(Rd55)*complexconjugate(yd22)',
                   texname = '\\text{I69x55}')

I69x63 = Parameter(name = 'I69x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd33*complexconjugate(Rd66)*complexconjugate(yd33)',
                   texname = '\\text{I69x63}')

I69x66 = Parameter(name = 'I69x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd63*complexconjugate(Rd66)*complexconjugate(yd33)',
                   texname = '\\text{I69x66}')

I7x11 = Parameter(name = 'I7x11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yd11*complexconjugate(Rd11)',
                  texname = '\\text{I7x11}')

I7x14 = Parameter(name = 'I7x14',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yd11*complexconjugate(Rd41)',
                  texname = '\\text{I7x14}')

I7x22 = Parameter(name = 'I7x22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yd22*complexconjugate(Rd22)',
                  texname = '\\text{I7x22}')

I7x25 = Parameter(name = 'I7x25',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yd22*complexconjugate(Rd52)',
                  texname = '\\text{I7x25}')

I7x33 = Parameter(name = 'I7x33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yd33*complexconjugate(Rd33)',
                  texname = '\\text{I7x33}')

I7x36 = Parameter(name = 'I7x36',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yd33*complexconjugate(Rd63)',
                  texname = '\\text{I7x36}')

I70x11 = Parameter(name = 'I70x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl14*ye11*complexconjugate(Rl11)',
                   texname = '\\text{I70x11}')

I70x14 = Parameter(name = 'I70x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl44*ye11*complexconjugate(Rl11)',
                   texname = '\\text{I70x14}')

I70x22 = Parameter(name = 'I70x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl25*ye22*complexconjugate(Rl22)',
                   texname = '\\text{I70x22}')

I70x25 = Parameter(name = 'I70x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl55*ye22*complexconjugate(Rl22)',
                   texname = '\\text{I70x25}')

I70x33 = Parameter(name = 'I70x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl36*ye33*complexconjugate(Rl33)',
                   texname = '\\text{I70x33}')

I70x36 = Parameter(name = 'I70x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl66*ye33*complexconjugate(Rl33)',
                   texname = '\\text{I70x36}')

I70x41 = Parameter(name = 'I70x41',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl14*ye11*complexconjugate(Rl41)',
                   texname = '\\text{I70x41}')

I70x44 = Parameter(name = 'I70x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl44*ye11*complexconjugate(Rl41)',
                   texname = '\\text{I70x44}')

I70x52 = Parameter(name = 'I70x52',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl25*ye22*complexconjugate(Rl52)',
                   texname = '\\text{I70x52}')

I70x55 = Parameter(name = 'I70x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl55*ye22*complexconjugate(Rl52)',
                   texname = '\\text{I70x55}')

I70x63 = Parameter(name = 'I70x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl36*ye33*complexconjugate(Rl63)',
                   texname = '\\text{I70x63}')

I70x66 = Parameter(name = 'I70x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl66*ye33*complexconjugate(Rl63)',
                   texname = '\\text{I70x66}')

I71x11 = Parameter(name = 'I71x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl11*complexconjugate(Rl11)',
                   texname = '\\text{I71x11}')

I71x14 = Parameter(name = 'I71x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl41*complexconjugate(Rl11)',
                   texname = '\\text{I71x14}')

I71x22 = Parameter(name = 'I71x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl22*complexconjugate(Rl22)',
                   texname = '\\text{I71x22}')

I71x25 = Parameter(name = 'I71x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl52*complexconjugate(Rl22)',
                   texname = '\\text{I71x25}')

I71x33 = Parameter(name = 'I71x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl33*complexconjugate(Rl33)',
                   texname = '\\text{I71x33}')

I71x36 = Parameter(name = 'I71x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl63*complexconjugate(Rl33)',
                   texname = '\\text{I71x36}')

I71x41 = Parameter(name = 'I71x41',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl11*complexconjugate(Rl41)',
                   texname = '\\text{I71x41}')

I71x44 = Parameter(name = 'I71x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl41*complexconjugate(Rl41)',
                   texname = '\\text{I71x44}')

I71x52 = Parameter(name = 'I71x52',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl22*complexconjugate(Rl52)',
                   texname = '\\text{I71x52}')

I71x55 = Parameter(name = 'I71x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl52*complexconjugate(Rl52)',
                   texname = '\\text{I71x55}')

I71x63 = Parameter(name = 'I71x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl33*complexconjugate(Rl63)',
                   texname = '\\text{I71x63}')

I71x66 = Parameter(name = 'I71x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl63*complexconjugate(Rl63)',
                   texname = '\\text{I71x66}')

I72x11 = Parameter(name = 'I72x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl11*complexconjugate(Rl11)',
                   texname = '\\text{I72x11}')

I72x14 = Parameter(name = 'I72x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl41*complexconjugate(Rl11)',
                   texname = '\\text{I72x14}')

I72x22 = Parameter(name = 'I72x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl22*complexconjugate(Rl22)',
                   texname = '\\text{I72x22}')

I72x25 = Parameter(name = 'I72x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl52*complexconjugate(Rl22)',
                   texname = '\\text{I72x25}')

I72x33 = Parameter(name = 'I72x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl33*complexconjugate(Rl33)',
                   texname = '\\text{I72x33}')

I72x36 = Parameter(name = 'I72x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl63*complexconjugate(Rl33)',
                   texname = '\\text{I72x36}')

I72x41 = Parameter(name = 'I72x41',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl11*complexconjugate(Rl41)',
                   texname = '\\text{I72x41}')

I72x44 = Parameter(name = 'I72x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl41*complexconjugate(Rl41)',
                   texname = '\\text{I72x44}')

I72x52 = Parameter(name = 'I72x52',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl22*complexconjugate(Rl52)',
                   texname = '\\text{I72x52}')

I72x55 = Parameter(name = 'I72x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl52*complexconjugate(Rl52)',
                   texname = '\\text{I72x55}')

I72x63 = Parameter(name = 'I72x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl33*complexconjugate(Rl63)',
                   texname = '\\text{I72x63}')

I72x66 = Parameter(name = 'I72x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl63*complexconjugate(Rl63)',
                   texname = '\\text{I72x66}')

I73x11 = Parameter(name = 'I73x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl11*complexconjugate(Rl11)',
                   texname = '\\text{I73x11}')

I73x14 = Parameter(name = 'I73x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl41*complexconjugate(Rl11)',
                   texname = '\\text{I73x14}')

I73x22 = Parameter(name = 'I73x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl22*complexconjugate(Rl22)',
                   texname = '\\text{I73x22}')

I73x25 = Parameter(name = 'I73x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl52*complexconjugate(Rl22)',
                   texname = '\\text{I73x25}')

I73x33 = Parameter(name = 'I73x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl33*complexconjugate(Rl33)',
                   texname = '\\text{I73x33}')

I73x36 = Parameter(name = 'I73x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl63*complexconjugate(Rl33)',
                   texname = '\\text{I73x36}')

I73x41 = Parameter(name = 'I73x41',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl11*complexconjugate(Rl41)',
                   texname = '\\text{I73x41}')

I73x44 = Parameter(name = 'I73x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl41*complexconjugate(Rl41)',
                   texname = '\\text{I73x44}')

I73x52 = Parameter(name = 'I73x52',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl22*complexconjugate(Rl52)',
                   texname = '\\text{I73x52}')

I73x55 = Parameter(name = 'I73x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl52*complexconjugate(Rl52)',
                   texname = '\\text{I73x55}')

I73x63 = Parameter(name = 'I73x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl33*complexconjugate(Rl63)',
                   texname = '\\text{I73x63}')

I73x66 = Parameter(name = 'I73x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl63*complexconjugate(Rl63)',
                   texname = '\\text{I73x66}')

I74x11 = Parameter(name = 'I74x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl11*complexconjugate(Rl11)',
                   texname = '\\text{I74x11}')

I74x14 = Parameter(name = 'I74x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl41*complexconjugate(Rl11)',
                   texname = '\\text{I74x14}')

I74x22 = Parameter(name = 'I74x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl22*complexconjugate(Rl22)',
                   texname = '\\text{I74x22}')

I74x25 = Parameter(name = 'I74x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl52*complexconjugate(Rl22)',
                   texname = '\\text{I74x25}')

I74x33 = Parameter(name = 'I74x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl33*complexconjugate(Rl33)',
                   texname = '\\text{I74x33}')

I74x36 = Parameter(name = 'I74x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl63*complexconjugate(Rl33)',
                   texname = '\\text{I74x36}')

I74x41 = Parameter(name = 'I74x41',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl11*complexconjugate(Rl41)',
                   texname = '\\text{I74x41}')

I74x44 = Parameter(name = 'I74x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl41*complexconjugate(Rl41)',
                   texname = '\\text{I74x44}')

I74x52 = Parameter(name = 'I74x52',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl22*complexconjugate(Rl52)',
                   texname = '\\text{I74x52}')

I74x55 = Parameter(name = 'I74x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl52*complexconjugate(Rl52)',
                   texname = '\\text{I74x55}')

I74x63 = Parameter(name = 'I74x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl33*complexconjugate(Rl63)',
                   texname = '\\text{I74x63}')

I74x66 = Parameter(name = 'I74x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl63*complexconjugate(Rl63)',
                   texname = '\\text{I74x66}')

I75x11 = Parameter(name = 'I75x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl11*complexconjugate(Rl11)',
                   texname = '\\text{I75x11}')

I75x14 = Parameter(name = 'I75x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl41*complexconjugate(Rl11)',
                   texname = '\\text{I75x14}')

I75x22 = Parameter(name = 'I75x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl22*complexconjugate(Rl22)',
                   texname = '\\text{I75x22}')

I75x25 = Parameter(name = 'I75x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl52*complexconjugate(Rl22)',
                   texname = '\\text{I75x25}')

I75x33 = Parameter(name = 'I75x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl33*complexconjugate(Rl33)',
                   texname = '\\text{I75x33}')

I75x36 = Parameter(name = 'I75x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl63*complexconjugate(Rl33)',
                   texname = '\\text{I75x36}')

I75x41 = Parameter(name = 'I75x41',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl11*complexconjugate(Rl41)',
                   texname = '\\text{I75x41}')

I75x44 = Parameter(name = 'I75x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl41*complexconjugate(Rl41)',
                   texname = '\\text{I75x44}')

I75x52 = Parameter(name = 'I75x52',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl22*complexconjugate(Rl52)',
                   texname = '\\text{I75x52}')

I75x55 = Parameter(name = 'I75x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl52*complexconjugate(Rl52)',
                   texname = '\\text{I75x55}')

I75x63 = Parameter(name = 'I75x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl33*complexconjugate(Rl63)',
                   texname = '\\text{I75x63}')

I75x66 = Parameter(name = 'I75x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl63*complexconjugate(Rl63)',
                   texname = '\\text{I75x66}')

I76x11 = Parameter(name = 'I76x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl14*complexconjugate(Rl14)',
                   texname = '\\text{I76x11}')

I76x14 = Parameter(name = 'I76x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl44*complexconjugate(Rl14)',
                   texname = '\\text{I76x14}')

I76x22 = Parameter(name = 'I76x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl25*complexconjugate(Rl25)',
                   texname = '\\text{I76x22}')

I76x25 = Parameter(name = 'I76x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl55*complexconjugate(Rl25)',
                   texname = '\\text{I76x25}')

I76x33 = Parameter(name = 'I76x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl36*complexconjugate(Rl36)',
                   texname = '\\text{I76x33}')

I76x36 = Parameter(name = 'I76x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl66*complexconjugate(Rl36)',
                   texname = '\\text{I76x36}')

I76x41 = Parameter(name = 'I76x41',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl14*complexconjugate(Rl44)',
                   texname = '\\text{I76x41}')

I76x44 = Parameter(name = 'I76x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl44*complexconjugate(Rl44)',
                   texname = '\\text{I76x44}')

I76x52 = Parameter(name = 'I76x52',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl25*complexconjugate(Rl55)',
                   texname = '\\text{I76x52}')

I76x55 = Parameter(name = 'I76x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl55*complexconjugate(Rl55)',
                   texname = '\\text{I76x55}')

I76x63 = Parameter(name = 'I76x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl36*complexconjugate(Rl66)',
                   texname = '\\text{I76x63}')

I76x66 = Parameter(name = 'I76x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl66*complexconjugate(Rl66)',
                   texname = '\\text{I76x66}')

I77x11 = Parameter(name = 'I77x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl14*complexconjugate(Rl14)',
                   texname = '\\text{I77x11}')

I77x14 = Parameter(name = 'I77x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl44*complexconjugate(Rl14)',
                   texname = '\\text{I77x14}')

I77x22 = Parameter(name = 'I77x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl25*complexconjugate(Rl25)',
                   texname = '\\text{I77x22}')

I77x25 = Parameter(name = 'I77x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl55*complexconjugate(Rl25)',
                   texname = '\\text{I77x25}')

I77x33 = Parameter(name = 'I77x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl36*complexconjugate(Rl36)',
                   texname = '\\text{I77x33}')

I77x36 = Parameter(name = 'I77x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl66*complexconjugate(Rl36)',
                   texname = '\\text{I77x36}')

I77x41 = Parameter(name = 'I77x41',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl14*complexconjugate(Rl44)',
                   texname = '\\text{I77x41}')

I77x44 = Parameter(name = 'I77x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl44*complexconjugate(Rl44)',
                   texname = '\\text{I77x44}')

I77x52 = Parameter(name = 'I77x52',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl25*complexconjugate(Rl55)',
                   texname = '\\text{I77x52}')

I77x55 = Parameter(name = 'I77x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl55*complexconjugate(Rl55)',
                   texname = '\\text{I77x55}')

I77x63 = Parameter(name = 'I77x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl36*complexconjugate(Rl66)',
                   texname = '\\text{I77x63}')

I77x66 = Parameter(name = 'I77x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl66*complexconjugate(Rl66)',
                   texname = '\\text{I77x66}')

I78x11 = Parameter(name = 'I78x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl14*complexconjugate(Rl14)',
                   texname = '\\text{I78x11}')

I78x14 = Parameter(name = 'I78x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl44*complexconjugate(Rl14)',
                   texname = '\\text{I78x14}')

I78x22 = Parameter(name = 'I78x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl25*complexconjugate(Rl25)',
                   texname = '\\text{I78x22}')

I78x25 = Parameter(name = 'I78x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl55*complexconjugate(Rl25)',
                   texname = '\\text{I78x25}')

I78x33 = Parameter(name = 'I78x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl36*complexconjugate(Rl36)',
                   texname = '\\text{I78x33}')

I78x36 = Parameter(name = 'I78x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl66*complexconjugate(Rl36)',
                   texname = '\\text{I78x36}')

I78x41 = Parameter(name = 'I78x41',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl14*complexconjugate(Rl44)',
                   texname = '\\text{I78x41}')

I78x44 = Parameter(name = 'I78x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl44*complexconjugate(Rl44)',
                   texname = '\\text{I78x44}')

I78x52 = Parameter(name = 'I78x52',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl25*complexconjugate(Rl55)',
                   texname = '\\text{I78x52}')

I78x55 = Parameter(name = 'I78x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl55*complexconjugate(Rl55)',
                   texname = '\\text{I78x55}')

I78x63 = Parameter(name = 'I78x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl36*complexconjugate(Rl66)',
                   texname = '\\text{I78x63}')

I78x66 = Parameter(name = 'I78x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl66*complexconjugate(Rl66)',
                   texname = '\\text{I78x66}')

I79x11 = Parameter(name = 'I79x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl14*complexconjugate(Rl14)',
                   texname = '\\text{I79x11}')

I79x14 = Parameter(name = 'I79x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl44*complexconjugate(Rl14)',
                   texname = '\\text{I79x14}')

I79x22 = Parameter(name = 'I79x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl25*complexconjugate(Rl25)',
                   texname = '\\text{I79x22}')

I79x25 = Parameter(name = 'I79x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl55*complexconjugate(Rl25)',
                   texname = '\\text{I79x25}')

I79x33 = Parameter(name = 'I79x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl36*complexconjugate(Rl36)',
                   texname = '\\text{I79x33}')

I79x36 = Parameter(name = 'I79x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl66*complexconjugate(Rl36)',
                   texname = '\\text{I79x36}')

I79x41 = Parameter(name = 'I79x41',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl14*complexconjugate(Rl44)',
                   texname = '\\text{I79x41}')

I79x44 = Parameter(name = 'I79x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl44*complexconjugate(Rl44)',
                   texname = '\\text{I79x44}')

I79x52 = Parameter(name = 'I79x52',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl25*complexconjugate(Rl55)',
                   texname = '\\text{I79x52}')

I79x55 = Parameter(name = 'I79x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl55*complexconjugate(Rl55)',
                   texname = '\\text{I79x55}')

I79x63 = Parameter(name = 'I79x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl36*complexconjugate(Rl66)',
                   texname = '\\text{I79x63}')

I79x66 = Parameter(name = 'I79x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl66*complexconjugate(Rl66)',
                   texname = '\\text{I79x66}')

I8x11 = Parameter(name = 'I8x11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd11*complexconjugate(Rd11)',
                  texname = '\\text{I8x11}')

I8x14 = Parameter(name = 'I8x14',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd41*complexconjugate(Rd11)',
                  texname = '\\text{I8x14}')

I8x22 = Parameter(name = 'I8x22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd22*complexconjugate(Rd22)',
                  texname = '\\text{I8x22}')

I8x25 = Parameter(name = 'I8x25',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd52*complexconjugate(Rd22)',
                  texname = '\\text{I8x25}')

I8x33 = Parameter(name = 'I8x33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd33*complexconjugate(Rd33)',
                  texname = '\\text{I8x33}')

I8x36 = Parameter(name = 'I8x36',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd63*complexconjugate(Rd33)',
                  texname = '\\text{I8x36}')

I8x41 = Parameter(name = 'I8x41',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd11*complexconjugate(Rd41)',
                  texname = '\\text{I8x41}')

I8x44 = Parameter(name = 'I8x44',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd41*complexconjugate(Rd41)',
                  texname = '\\text{I8x44}')

I8x52 = Parameter(name = 'I8x52',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd22*complexconjugate(Rd52)',
                  texname = '\\text{I8x52}')

I8x55 = Parameter(name = 'I8x55',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd52*complexconjugate(Rd52)',
                  texname = '\\text{I8x55}')

I8x63 = Parameter(name = 'I8x63',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd33*complexconjugate(Rd63)',
                  texname = '\\text{I8x63}')

I8x66 = Parameter(name = 'I8x66',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd63*complexconjugate(Rd63)',
                  texname = '\\text{I8x66}')

I80x11 = Parameter(name = 'I80x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl14*complexconjugate(Rl14)',
                   texname = '\\text{I80x11}')

I80x14 = Parameter(name = 'I80x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl44*complexconjugate(Rl14)',
                   texname = '\\text{I80x14}')

I80x22 = Parameter(name = 'I80x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl25*complexconjugate(Rl25)',
                   texname = '\\text{I80x22}')

I80x25 = Parameter(name = 'I80x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl55*complexconjugate(Rl25)',
                   texname = '\\text{I80x25}')

I80x33 = Parameter(name = 'I80x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl36*complexconjugate(Rl36)',
                   texname = '\\text{I80x33}')

I80x36 = Parameter(name = 'I80x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl66*complexconjugate(Rl36)',
                   texname = '\\text{I80x36}')

I80x41 = Parameter(name = 'I80x41',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl14*complexconjugate(Rl44)',
                   texname = '\\text{I80x41}')

I80x44 = Parameter(name = 'I80x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl44*complexconjugate(Rl44)',
                   texname = '\\text{I80x44}')

I80x52 = Parameter(name = 'I80x52',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl25*complexconjugate(Rl55)',
                   texname = '\\text{I80x52}')

I80x55 = Parameter(name = 'I80x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl55*complexconjugate(Rl55)',
                   texname = '\\text{I80x55}')

I80x63 = Parameter(name = 'I80x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl36*complexconjugate(Rl66)',
                   texname = '\\text{I80x63}')

I80x66 = Parameter(name = 'I80x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl66*complexconjugate(Rl66)',
                   texname = '\\text{I80x66}')

I81x11 = Parameter(name = 'I81x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl14*complexconjugate(Rl14)',
                   texname = '\\text{I81x11}')

I81x14 = Parameter(name = 'I81x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl44*complexconjugate(Rl14)',
                   texname = '\\text{I81x14}')

I81x22 = Parameter(name = 'I81x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl25*complexconjugate(Rl25)',
                   texname = '\\text{I81x22}')

I81x25 = Parameter(name = 'I81x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl55*complexconjugate(Rl25)',
                   texname = '\\text{I81x25}')

I81x33 = Parameter(name = 'I81x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl36*complexconjugate(Rl36)',
                   texname = '\\text{I81x33}')

I81x36 = Parameter(name = 'I81x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl66*complexconjugate(Rl36)',
                   texname = '\\text{I81x36}')

I81x41 = Parameter(name = 'I81x41',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl14*complexconjugate(Rl44)',
                   texname = '\\text{I81x41}')

I81x44 = Parameter(name = 'I81x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl44*complexconjugate(Rl44)',
                   texname = '\\text{I81x44}')

I81x52 = Parameter(name = 'I81x52',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl25*complexconjugate(Rl55)',
                   texname = '\\text{I81x52}')

I81x55 = Parameter(name = 'I81x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl55*complexconjugate(Rl55)',
                   texname = '\\text{I81x55}')

I81x63 = Parameter(name = 'I81x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl36*complexconjugate(Rl66)',
                   texname = '\\text{I81x63}')

I81x66 = Parameter(name = 'I81x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl66*complexconjugate(Rl66)',
                   texname = '\\text{I81x66}')

I82x11 = Parameter(name = 'I82x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl11*complexconjugate(Rl14)*complexconjugate(ye11)',
                   texname = '\\text{I82x11}')

I82x14 = Parameter(name = 'I82x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl41*complexconjugate(Rl14)*complexconjugate(ye11)',
                   texname = '\\text{I82x14}')

I82x22 = Parameter(name = 'I82x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl22*complexconjugate(Rl25)*complexconjugate(ye22)',
                   texname = '\\text{I82x22}')

I82x25 = Parameter(name = 'I82x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl52*complexconjugate(Rl25)*complexconjugate(ye22)',
                   texname = '\\text{I82x25}')

I82x33 = Parameter(name = 'I82x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl33*complexconjugate(Rl36)*complexconjugate(ye33)',
                   texname = '\\text{I82x33}')

I82x36 = Parameter(name = 'I82x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl63*complexconjugate(Rl36)*complexconjugate(ye33)',
                   texname = '\\text{I82x36}')

I82x41 = Parameter(name = 'I82x41',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl11*complexconjugate(Rl44)*complexconjugate(ye11)',
                   texname = '\\text{I82x41}')

I82x44 = Parameter(name = 'I82x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl41*complexconjugate(Rl44)*complexconjugate(ye11)',
                   texname = '\\text{I82x44}')

I82x52 = Parameter(name = 'I82x52',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl22*complexconjugate(Rl55)*complexconjugate(ye22)',
                   texname = '\\text{I82x52}')

I82x55 = Parameter(name = 'I82x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl52*complexconjugate(Rl55)*complexconjugate(ye22)',
                   texname = '\\text{I82x55}')

I82x63 = Parameter(name = 'I82x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl33*complexconjugate(Rl66)*complexconjugate(ye33)',
                   texname = '\\text{I82x63}')

I82x66 = Parameter(name = 'I82x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl63*complexconjugate(Rl66)*complexconjugate(ye33)',
                   texname = '\\text{I82x66}')

I83x11 = Parameter(name = 'I83x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl14*ye11*complexconjugate(Rl11)',
                   texname = '\\text{I83x11}')

I83x14 = Parameter(name = 'I83x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl44*ye11*complexconjugate(Rl11)',
                   texname = '\\text{I83x14}')

I83x22 = Parameter(name = 'I83x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl25*ye22*complexconjugate(Rl22)',
                   texname = '\\text{I83x22}')

I83x25 = Parameter(name = 'I83x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl55*ye22*complexconjugate(Rl22)',
                   texname = '\\text{I83x25}')

I83x33 = Parameter(name = 'I83x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl36*ye33*complexconjugate(Rl33)',
                   texname = '\\text{I83x33}')

I83x36 = Parameter(name = 'I83x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl66*ye33*complexconjugate(Rl33)',
                   texname = '\\text{I83x36}')

I83x41 = Parameter(name = 'I83x41',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl14*ye11*complexconjugate(Rl41)',
                   texname = '\\text{I83x41}')

I83x44 = Parameter(name = 'I83x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl44*ye11*complexconjugate(Rl41)',
                   texname = '\\text{I83x44}')

I83x52 = Parameter(name = 'I83x52',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl25*ye22*complexconjugate(Rl52)',
                   texname = '\\text{I83x52}')

I83x55 = Parameter(name = 'I83x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl55*ye22*complexconjugate(Rl52)',
                   texname = '\\text{I83x55}')

I83x63 = Parameter(name = 'I83x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl36*ye33*complexconjugate(Rl63)',
                   texname = '\\text{I83x63}')

I83x66 = Parameter(name = 'I83x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl66*ye33*complexconjugate(Rl63)',
                   texname = '\\text{I83x66}')

I84x11 = Parameter(name = 'I84x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl11*complexconjugate(Rl14)*complexconjugate(ye11)',
                   texname = '\\text{I84x11}')

I84x14 = Parameter(name = 'I84x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl41*complexconjugate(Rl14)*complexconjugate(ye11)',
                   texname = '\\text{I84x14}')

I84x22 = Parameter(name = 'I84x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl22*complexconjugate(Rl25)*complexconjugate(ye22)',
                   texname = '\\text{I84x22}')

I84x25 = Parameter(name = 'I84x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl52*complexconjugate(Rl25)*complexconjugate(ye22)',
                   texname = '\\text{I84x25}')

I84x33 = Parameter(name = 'I84x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl33*complexconjugate(Rl36)*complexconjugate(ye33)',
                   texname = '\\text{I84x33}')

I84x36 = Parameter(name = 'I84x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl63*complexconjugate(Rl36)*complexconjugate(ye33)',
                   texname = '\\text{I84x36}')

I84x41 = Parameter(name = 'I84x41',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl11*complexconjugate(Rl44)*complexconjugate(ye11)',
                   texname = '\\text{I84x41}')

I84x44 = Parameter(name = 'I84x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl41*complexconjugate(Rl44)*complexconjugate(ye11)',
                   texname = '\\text{I84x44}')

I84x52 = Parameter(name = 'I84x52',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl22*complexconjugate(Rl55)*complexconjugate(ye22)',
                   texname = '\\text{I84x52}')

I84x55 = Parameter(name = 'I84x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl52*complexconjugate(Rl55)*complexconjugate(ye22)',
                   texname = '\\text{I84x55}')

I84x63 = Parameter(name = 'I84x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl33*complexconjugate(Rl66)*complexconjugate(ye33)',
                   texname = '\\text{I84x63}')

I84x66 = Parameter(name = 'I84x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl63*complexconjugate(Rl66)*complexconjugate(ye33)',
                   texname = '\\text{I84x66}')

I85x11 = Parameter(name = 'I85x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl14*ye11*complexconjugate(Rl11)',
                   texname = '\\text{I85x11}')

I85x14 = Parameter(name = 'I85x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl44*ye11*complexconjugate(Rl11)',
                   texname = '\\text{I85x14}')

I85x22 = Parameter(name = 'I85x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl25*ye22*complexconjugate(Rl22)',
                   texname = '\\text{I85x22}')

I85x25 = Parameter(name = 'I85x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl55*ye22*complexconjugate(Rl22)',
                   texname = '\\text{I85x25}')

I85x33 = Parameter(name = 'I85x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl36*ye33*complexconjugate(Rl33)',
                   texname = '\\text{I85x33}')

I85x36 = Parameter(name = 'I85x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl66*ye33*complexconjugate(Rl33)',
                   texname = '\\text{I85x36}')

I85x41 = Parameter(name = 'I85x41',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl14*ye11*complexconjugate(Rl41)',
                   texname = '\\text{I85x41}')

I85x44 = Parameter(name = 'I85x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl44*ye11*complexconjugate(Rl41)',
                   texname = '\\text{I85x44}')

I85x52 = Parameter(name = 'I85x52',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl25*ye22*complexconjugate(Rl52)',
                   texname = '\\text{I85x52}')

I85x55 = Parameter(name = 'I85x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl55*ye22*complexconjugate(Rl52)',
                   texname = '\\text{I85x55}')

I85x63 = Parameter(name = 'I85x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl36*ye33*complexconjugate(Rl63)',
                   texname = '\\text{I85x63}')

I85x66 = Parameter(name = 'I85x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl66*ye33*complexconjugate(Rl63)',
                   texname = '\\text{I85x66}')

I86x11 = Parameter(name = 'I86x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl11*complexconjugate(Rl14)*complexconjugate(ye11)',
                   texname = '\\text{I86x11}')

I86x14 = Parameter(name = 'I86x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl41*complexconjugate(Rl14)*complexconjugate(ye11)',
                   texname = '\\text{I86x14}')

I86x22 = Parameter(name = 'I86x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl22*complexconjugate(Rl25)*complexconjugate(ye22)',
                   texname = '\\text{I86x22}')

I86x25 = Parameter(name = 'I86x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl52*complexconjugate(Rl25)*complexconjugate(ye22)',
                   texname = '\\text{I86x25}')

I86x33 = Parameter(name = 'I86x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl33*complexconjugate(Rl36)*complexconjugate(ye33)',
                   texname = '\\text{I86x33}')

I86x36 = Parameter(name = 'I86x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl63*complexconjugate(Rl36)*complexconjugate(ye33)',
                   texname = '\\text{I86x36}')

I86x41 = Parameter(name = 'I86x41',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl11*complexconjugate(Rl44)*complexconjugate(ye11)',
                   texname = '\\text{I86x41}')

I86x44 = Parameter(name = 'I86x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl41*complexconjugate(Rl44)*complexconjugate(ye11)',
                   texname = '\\text{I86x44}')

I86x52 = Parameter(name = 'I86x52',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl22*complexconjugate(Rl55)*complexconjugate(ye22)',
                   texname = '\\text{I86x52}')

I86x55 = Parameter(name = 'I86x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl52*complexconjugate(Rl55)*complexconjugate(ye22)',
                   texname = '\\text{I86x55}')

I86x63 = Parameter(name = 'I86x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl33*complexconjugate(Rl66)*complexconjugate(ye33)',
                   texname = '\\text{I86x63}')

I86x66 = Parameter(name = 'I86x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl63*complexconjugate(Rl66)*complexconjugate(ye33)',
                   texname = '\\text{I86x66}')

I87x11 = Parameter(name = 'I87x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl14*ye11*complexconjugate(Rl11)',
                   texname = '\\text{I87x11}')

I87x14 = Parameter(name = 'I87x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl44*ye11*complexconjugate(Rl11)',
                   texname = '\\text{I87x14}')

I87x22 = Parameter(name = 'I87x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl25*ye22*complexconjugate(Rl22)',
                   texname = '\\text{I87x22}')

I87x25 = Parameter(name = 'I87x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl55*ye22*complexconjugate(Rl22)',
                   texname = '\\text{I87x25}')

I87x33 = Parameter(name = 'I87x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl36*ye33*complexconjugate(Rl33)',
                   texname = '\\text{I87x33}')

I87x36 = Parameter(name = 'I87x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl66*ye33*complexconjugate(Rl33)',
                   texname = '\\text{I87x36}')

I87x41 = Parameter(name = 'I87x41',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl14*ye11*complexconjugate(Rl41)',
                   texname = '\\text{I87x41}')

I87x44 = Parameter(name = 'I87x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl44*ye11*complexconjugate(Rl41)',
                   texname = '\\text{I87x44}')

I87x52 = Parameter(name = 'I87x52',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl25*ye22*complexconjugate(Rl52)',
                   texname = '\\text{I87x52}')

I87x55 = Parameter(name = 'I87x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl55*ye22*complexconjugate(Rl52)',
                   texname = '\\text{I87x55}')

I87x63 = Parameter(name = 'I87x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl36*ye33*complexconjugate(Rl63)',
                   texname = '\\text{I87x63}')

I87x66 = Parameter(name = 'I87x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl66*ye33*complexconjugate(Rl63)',
                   texname = '\\text{I87x66}')

I88x11 = Parameter(name = 'I88x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl11*complexconjugate(Rl14)*complexconjugate(ye11)',
                   texname = '\\text{I88x11}')

I88x14 = Parameter(name = 'I88x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl41*complexconjugate(Rl14)*complexconjugate(ye11)',
                   texname = '\\text{I88x14}')

I88x22 = Parameter(name = 'I88x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl22*complexconjugate(Rl25)*complexconjugate(ye22)',
                   texname = '\\text{I88x22}')

I88x25 = Parameter(name = 'I88x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl52*complexconjugate(Rl25)*complexconjugate(ye22)',
                   texname = '\\text{I88x25}')

I88x33 = Parameter(name = 'I88x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl33*complexconjugate(Rl36)*complexconjugate(ye33)',
                   texname = '\\text{I88x33}')

I88x36 = Parameter(name = 'I88x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl63*complexconjugate(Rl36)*complexconjugate(ye33)',
                   texname = '\\text{I88x36}')

I88x41 = Parameter(name = 'I88x41',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl11*complexconjugate(Rl44)*complexconjugate(ye11)',
                   texname = '\\text{I88x41}')

I88x44 = Parameter(name = 'I88x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl41*complexconjugate(Rl44)*complexconjugate(ye11)',
                   texname = '\\text{I88x44}')

I88x52 = Parameter(name = 'I88x52',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl22*complexconjugate(Rl55)*complexconjugate(ye22)',
                   texname = '\\text{I88x52}')

I88x55 = Parameter(name = 'I88x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl52*complexconjugate(Rl55)*complexconjugate(ye22)',
                   texname = '\\text{I88x55}')

I88x63 = Parameter(name = 'I88x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl33*complexconjugate(Rl66)*complexconjugate(ye33)',
                   texname = '\\text{I88x63}')

I88x66 = Parameter(name = 'I88x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl63*complexconjugate(Rl66)*complexconjugate(ye33)',
                   texname = '\\text{I88x66}')

I89x11 = Parameter(name = 'I89x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl14*ye11*complexconjugate(Rl11)',
                   texname = '\\text{I89x11}')

I89x14 = Parameter(name = 'I89x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl44*ye11*complexconjugate(Rl11)',
                   texname = '\\text{I89x14}')

I89x22 = Parameter(name = 'I89x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl25*ye22*complexconjugate(Rl22)',
                   texname = '\\text{I89x22}')

I89x25 = Parameter(name = 'I89x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl55*ye22*complexconjugate(Rl22)',
                   texname = '\\text{I89x25}')

I89x33 = Parameter(name = 'I89x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl36*ye33*complexconjugate(Rl33)',
                   texname = '\\text{I89x33}')

I89x36 = Parameter(name = 'I89x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl66*ye33*complexconjugate(Rl33)',
                   texname = '\\text{I89x36}')

I89x41 = Parameter(name = 'I89x41',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl14*ye11*complexconjugate(Rl41)',
                   texname = '\\text{I89x41}')

I89x44 = Parameter(name = 'I89x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl44*ye11*complexconjugate(Rl41)',
                   texname = '\\text{I89x44}')

I89x52 = Parameter(name = 'I89x52',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl25*ye22*complexconjugate(Rl52)',
                   texname = '\\text{I89x52}')

I89x55 = Parameter(name = 'I89x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl55*ye22*complexconjugate(Rl52)',
                   texname = '\\text{I89x55}')

I89x63 = Parameter(name = 'I89x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl36*ye33*complexconjugate(Rl63)',
                   texname = '\\text{I89x63}')

I89x66 = Parameter(name = 'I89x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl66*ye33*complexconjugate(Rl63)',
                   texname = '\\text{I89x66}')

I9x11 = Parameter(name = 'I9x11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd14*complexconjugate(Rd14)',
                  texname = '\\text{I9x11}')

I9x14 = Parameter(name = 'I9x14',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd44*complexconjugate(Rd14)',
                  texname = '\\text{I9x14}')

I9x22 = Parameter(name = 'I9x22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd25*complexconjugate(Rd25)',
                  texname = '\\text{I9x22}')

I9x25 = Parameter(name = 'I9x25',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd55*complexconjugate(Rd25)',
                  texname = '\\text{I9x25}')

I9x33 = Parameter(name = 'I9x33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd36*complexconjugate(Rd36)',
                  texname = '\\text{I9x33}')

I9x36 = Parameter(name = 'I9x36',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd66*complexconjugate(Rd36)',
                  texname = '\\text{I9x36}')

I9x41 = Parameter(name = 'I9x41',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd14*complexconjugate(Rd44)',
                  texname = '\\text{I9x41}')

I9x44 = Parameter(name = 'I9x44',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd44*complexconjugate(Rd44)',
                  texname = '\\text{I9x44}')

I9x52 = Parameter(name = 'I9x52',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd25*complexconjugate(Rd55)',
                  texname = '\\text{I9x52}')

I9x55 = Parameter(name = 'I9x55',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd55*complexconjugate(Rd55)',
                  texname = '\\text{I9x55}')

I9x63 = Parameter(name = 'I9x63',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd36*complexconjugate(Rd66)',
                  texname = '\\text{I9x63}')

I9x66 = Parameter(name = 'I9x66',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd66*complexconjugate(Rd66)',
                  texname = '\\text{I9x66}')

I90x11 = Parameter(name = 'I90x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl11*complexconjugate(Rn11)',
                   texname = '\\text{I90x11}')

I90x14 = Parameter(name = 'I90x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl41*complexconjugate(Rn11)',
                   texname = '\\text{I90x14}')

I90x22 = Parameter(name = 'I90x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl22*complexconjugate(Rn22)',
                   texname = '\\text{I90x22}')

I90x25 = Parameter(name = 'I90x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl52*complexconjugate(Rn22)',
                   texname = '\\text{I90x25}')

I90x33 = Parameter(name = 'I90x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl33*complexconjugate(Rn33)',
                   texname = '\\text{I90x33}')

I90x36 = Parameter(name = 'I90x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl63*complexconjugate(Rn33)',
                   texname = '\\text{I90x36}')

I91x11 = Parameter(name = 'I91x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl14*te11*complexconjugate(Rn11)',
                   texname = '\\text{I91x11}')

I91x14 = Parameter(name = 'I91x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl44*te11*complexconjugate(Rn11)',
                   texname = '\\text{I91x14}')

I91x22 = Parameter(name = 'I91x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl25*te22*complexconjugate(Rn22)',
                   texname = '\\text{I91x22}')

I91x25 = Parameter(name = 'I91x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl55*te22*complexconjugate(Rn22)',
                   texname = '\\text{I91x25}')

I91x33 = Parameter(name = 'I91x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl36*te33*complexconjugate(Rn33)',
                   texname = '\\text{I91x33}')

I91x36 = Parameter(name = 'I91x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl66*te33*complexconjugate(Rn33)',
                   texname = '\\text{I91x36}')

I92x11 = Parameter(name = 'I92x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl11*ye11*complexconjugate(Rn11)*complexconjugate(ye11)',
                   texname = '\\text{I92x11}')

I92x14 = Parameter(name = 'I92x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl41*ye11*complexconjugate(Rn11)*complexconjugate(ye11)',
                   texname = '\\text{I92x14}')

I92x22 = Parameter(name = 'I92x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl22*ye22*complexconjugate(Rn22)*complexconjugate(ye22)',
                   texname = '\\text{I92x22}')

I92x25 = Parameter(name = 'I92x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl52*ye22*complexconjugate(Rn22)*complexconjugate(ye22)',
                   texname = '\\text{I92x25}')

I92x33 = Parameter(name = 'I92x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl33*ye33*complexconjugate(Rn33)*complexconjugate(ye33)',
                   texname = '\\text{I92x33}')

I92x36 = Parameter(name = 'I92x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl63*ye33*complexconjugate(Rn33)*complexconjugate(ye33)',
                   texname = '\\text{I92x36}')

I93x11 = Parameter(name = 'I93x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl14*ye11*complexconjugate(Rn11)',
                   texname = '\\text{I93x11}')

I93x14 = Parameter(name = 'I93x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl44*ye11*complexconjugate(Rn11)',
                   texname = '\\text{I93x14}')

I93x22 = Parameter(name = 'I93x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl25*ye22*complexconjugate(Rn22)',
                   texname = '\\text{I93x22}')

I93x25 = Parameter(name = 'I93x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl55*ye22*complexconjugate(Rn22)',
                   texname = '\\text{I93x25}')

I93x33 = Parameter(name = 'I93x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl36*ye33*complexconjugate(Rn33)',
                   texname = '\\text{I93x33}')

I93x36 = Parameter(name = 'I93x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl66*ye33*complexconjugate(Rn33)',
                   texname = '\\text{I93x36}')

I94x11 = Parameter(name = 'I94x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl11*complexconjugate(Rn11)',
                   texname = '\\text{I94x11}')

I94x14 = Parameter(name = 'I94x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl41*complexconjugate(Rn11)',
                   texname = '\\text{I94x14}')

I94x22 = Parameter(name = 'I94x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl22*complexconjugate(Rn22)',
                   texname = '\\text{I94x22}')

I94x25 = Parameter(name = 'I94x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl52*complexconjugate(Rn22)',
                   texname = '\\text{I94x25}')

I94x33 = Parameter(name = 'I94x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl33*complexconjugate(Rn33)',
                   texname = '\\text{I94x33}')

I94x36 = Parameter(name = 'I94x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl63*complexconjugate(Rn33)',
                   texname = '\\text{I94x36}')

I95x11 = Parameter(name = 'I95x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl11*ye11*complexconjugate(Rn11)*complexconjugate(ye11)',
                   texname = '\\text{I95x11}')

I95x14 = Parameter(name = 'I95x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl41*ye11*complexconjugate(Rn11)*complexconjugate(ye11)',
                   texname = '\\text{I95x14}')

I95x22 = Parameter(name = 'I95x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl22*ye22*complexconjugate(Rn22)*complexconjugate(ye22)',
                   texname = '\\text{I95x22}')

I95x25 = Parameter(name = 'I95x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl52*ye22*complexconjugate(Rn22)*complexconjugate(ye22)',
                   texname = '\\text{I95x25}')

I95x33 = Parameter(name = 'I95x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl33*ye33*complexconjugate(Rn33)*complexconjugate(ye33)',
                   texname = '\\text{I95x33}')

I95x36 = Parameter(name = 'I95x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl63*ye33*complexconjugate(Rn33)*complexconjugate(ye33)',
                   texname = '\\text{I95x36}')

I96x11 = Parameter(name = 'I96x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn11',
                   texname = '\\text{I96x11}')

I96x22 = Parameter(name = 'I96x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn22',
                   texname = '\\text{I96x22}')

I96x33 = Parameter(name = 'I96x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn33',
                   texname = '\\text{I96x33}')

I97x11 = Parameter(name = 'I97x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn11*complexconjugate(ye11)',
                   texname = '\\text{I97x11}')

I97x22 = Parameter(name = 'I97x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn22*complexconjugate(ye22)',
                   texname = '\\text{I97x22}')

I97x33 = Parameter(name = 'I97x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn33*complexconjugate(ye33)',
                   texname = '\\text{I97x33}')

I98x11 = Parameter(name = 'I98x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn11*complexconjugate(Rl11)',
                   texname = '\\text{I98x11}')

I98x14 = Parameter(name = 'I98x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn11*complexconjugate(Rl41)',
                   texname = '\\text{I98x14}')

I98x22 = Parameter(name = 'I98x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn22*complexconjugate(Rl22)',
                   texname = '\\text{I98x22}')

I98x25 = Parameter(name = 'I98x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn22*complexconjugate(Rl52)',
                   texname = '\\text{I98x25}')

I98x33 = Parameter(name = 'I98x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn33*complexconjugate(Rl33)',
                   texname = '\\text{I98x33}')

I98x36 = Parameter(name = 'I98x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn33*complexconjugate(Rl63)',
                   texname = '\\text{I98x36}')

I99x11 = Parameter(name = 'I99x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn11*complexconjugate(Rl14)*complexconjugate(te11)',
                   texname = '\\text{I99x11}')

I99x14 = Parameter(name = 'I99x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn11*complexconjugate(Rl44)*complexconjugate(te11)',
                   texname = '\\text{I99x14}')

I99x22 = Parameter(name = 'I99x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn22*complexconjugate(Rl25)*complexconjugate(te22)',
                   texname = '\\text{I99x22}')

I99x25 = Parameter(name = 'I99x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn22*complexconjugate(Rl55)*complexconjugate(te22)',
                   texname = '\\text{I99x25}')

I99x33 = Parameter(name = 'I99x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn33*complexconjugate(Rl36)*complexconjugate(te33)',
                   texname = '\\text{I99x33}')

I99x36 = Parameter(name = 'I99x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn33*complexconjugate(Rl66)*complexconjugate(te33)',
                   texname = '\\text{I99x36}')
