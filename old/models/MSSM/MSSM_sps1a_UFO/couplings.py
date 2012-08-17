# This file was automatically created by FeynRules 1.6.7
# Mathematica version: 8.0 for Mac OS X x86 (64-bit) (October 14, 2011)
# Date: Fri 17 Aug 2012 00:55:28


from object_library import all_couplings, Coupling

from function_library import complexconjugate, re, im, csc, sec, acsc, asec



GC_1 = Coupling(name = 'GC_1',
                value = '-(ee*complex(0,1))/3.',
                order = {'QED':1})

GC_2 = Coupling(name = 'GC_2',
                value = '(2*ee*complex(0,1))/3.',
                order = {'QED':1})

GC_3 = Coupling(name = 'GC_3',
                value = '-(ee*complex(0,1))',
                order = {'QED':1})

GC_4 = Coupling(name = 'GC_4',
                value = 'ee*complex(0,1)',
                order = {'QED':1})

GC_5 = Coupling(name = 'GC_5',
                value = 'ee**2*complex(0,1)',
                order = {'QED':2})

GC_6 = Coupling(name = 'GC_6',
                value = '-G',
                order = {'QCD':1})

GC_7 = Coupling(name = 'GC_7',
                value = 'complex(0,1)*G',
                order = {'QCD':1})

GC_8 = Coupling(name = 'GC_8',
                value = 'G',
                order = {'QCD':1})

GC_9 = Coupling(name = 'GC_9',
                value = 'complex(0,1)*G**2',
                order = {'QCD':2})

GC_10 = Coupling(name = 'GC_10',
                 value = '(-2*ee*complex(0,1)*I113x11)/3.',
                 order = {'QED':1})

GC_11 = Coupling(name = 'GC_11',
                 value = '-(complex(0,1)*G*I113x11)',
                 order = {'QCD':1})

GC_12 = Coupling(name = 'GC_12',
                 value = '(-2*ee*complex(0,1)*I113x22)/3.',
                 order = {'QED':1})

GC_13 = Coupling(name = 'GC_13',
                 value = '-(complex(0,1)*G*I113x22)',
                 order = {'QCD':1})

GC_14 = Coupling(name = 'GC_14',
                 value = '(-2*ee*complex(0,1)*I113x33)/3. - (2*ee*complex(0,1)*I114x33)/3.',
                 order = {'QED':1})

GC_15 = Coupling(name = 'GC_15',
                 value = '-(complex(0,1)*G*I113x33) - complex(0,1)*G*I114x33',
                 order = {'QCD':1})

GC_16 = Coupling(name = 'GC_16',
                 value = '(-2*ee*complex(0,1)*I113x36)/3. - (2*ee*complex(0,1)*I114x36)/3.',
                 order = {'QED':1})

GC_17 = Coupling(name = 'GC_17',
                 value = '-(complex(0,1)*G*I113x36) - complex(0,1)*G*I114x36',
                 order = {'QCD':1})

GC_18 = Coupling(name = 'GC_18',
                 value = '(-2*ee*complex(0,1)*I114x44)/3.',
                 order = {'QED':1})

GC_19 = Coupling(name = 'GC_19',
                 value = '-(complex(0,1)*G*I114x44)',
                 order = {'QCD':1})

GC_20 = Coupling(name = 'GC_20',
                 value = '(-2*ee*complex(0,1)*I114x55)/3.',
                 order = {'QED':1})

GC_21 = Coupling(name = 'GC_21',
                 value = '-(complex(0,1)*G*I114x55)',
                 order = {'QCD':1})

GC_22 = Coupling(name = 'GC_22',
                 value = '(2*ee*complex(0,1)*I113x63)/3. + (2*ee*complex(0,1)*I114x63)/3.',
                 order = {'QED':1})

GC_23 = Coupling(name = 'GC_23',
                 value = 'complex(0,1)*G*I113x63 + complex(0,1)*G*I114x63',
                 order = {'QCD':1})

GC_24 = Coupling(name = 'GC_24',
                 value = '(-2*ee*complex(0,1)*I113x66)/3. - (2*ee*complex(0,1)*I114x66)/3.',
                 order = {'QED':1})

GC_25 = Coupling(name = 'GC_25',
                 value = '-(complex(0,1)*G*I113x66) - complex(0,1)*G*I114x66',
                 order = {'QCD':1})

GC_26 = Coupling(name = 'GC_26',
                 value = '(8*ee**2*complex(0,1)*I148x11)/9.',
                 order = {'QED':2})

GC_27 = Coupling(name = 'GC_27',
                 value = '(4*ee*complex(0,1)*G*I148x11)/3.',
                 order = {'QCD':1,'QED':1})

GC_28 = Coupling(name = 'GC_28',
                 value = 'complex(0,1)*G**2*I148x11',
                 order = {'QCD':2})

GC_29 = Coupling(name = 'GC_29',
                 value = '(8*ee**2*complex(0,1)*I148x22)/9.',
                 order = {'QED':2})

GC_30 = Coupling(name = 'GC_30',
                 value = '(4*ee*complex(0,1)*G*I148x22)/3.',
                 order = {'QCD':1,'QED':1})

GC_31 = Coupling(name = 'GC_31',
                 value = 'complex(0,1)*G**2*I148x22',
                 order = {'QCD':2})

GC_32 = Coupling(name = 'GC_32',
                 value = '(8*ee**2*complex(0,1)*I148x33)/9. + (8*ee**2*complex(0,1)*I149x33)/9.',
                 order = {'QED':2})

GC_33 = Coupling(name = 'GC_33',
                 value = '(4*ee*complex(0,1)*G*I148x33)/3. + (4*ee*complex(0,1)*G*I149x33)/3.',
                 order = {'QCD':1,'QED':1})

GC_34 = Coupling(name = 'GC_34',
                 value = 'complex(0,1)*G**2*I148x33 + complex(0,1)*G**2*I149x33',
                 order = {'QCD':2})

GC_35 = Coupling(name = 'GC_35',
                 value = '(8*ee**2*complex(0,1)*I148x36)/9. + (8*ee**2*complex(0,1)*I149x36)/9.',
                 order = {'QED':2})

GC_36 = Coupling(name = 'GC_36',
                 value = '(4*ee*complex(0,1)*G*I148x36)/3. + (4*ee*complex(0,1)*G*I149x36)/3.',
                 order = {'QCD':1,'QED':1})

GC_37 = Coupling(name = 'GC_37',
                 value = 'complex(0,1)*G**2*I148x36 + complex(0,1)*G**2*I149x36',
                 order = {'QCD':2})

GC_38 = Coupling(name = 'GC_38',
                 value = '(8*ee**2*complex(0,1)*I149x44)/9.',
                 order = {'QED':2})

GC_39 = Coupling(name = 'GC_39',
                 value = '(4*ee*complex(0,1)*G*I149x44)/3.',
                 order = {'QCD':1,'QED':1})

GC_40 = Coupling(name = 'GC_40',
                 value = 'complex(0,1)*G**2*I149x44',
                 order = {'QCD':2})

GC_41 = Coupling(name = 'GC_41',
                 value = '(8*ee**2*complex(0,1)*I149x55)/9.',
                 order = {'QED':2})

GC_42 = Coupling(name = 'GC_42',
                 value = '(4*ee*complex(0,1)*G*I149x55)/3.',
                 order = {'QCD':1,'QED':1})

GC_43 = Coupling(name = 'GC_43',
                 value = 'complex(0,1)*G**2*I149x55',
                 order = {'QCD':2})

GC_44 = Coupling(name = 'GC_44',
                 value = '(8*ee**2*complex(0,1)*I148x63)/9. + (8*ee**2*complex(0,1)*I149x63)/9.',
                 order = {'QED':2})

GC_45 = Coupling(name = 'GC_45',
                 value = '(4*ee*complex(0,1)*G*I148x63)/3. + (4*ee*complex(0,1)*G*I149x63)/3.',
                 order = {'QCD':1,'QED':1})

GC_46 = Coupling(name = 'GC_46',
                 value = 'complex(0,1)*G**2*I148x63 + complex(0,1)*G**2*I149x63',
                 order = {'QCD':2})

GC_47 = Coupling(name = 'GC_47',
                 value = '(8*ee**2*complex(0,1)*I148x66)/9. + (8*ee**2*complex(0,1)*I149x66)/9.',
                 order = {'QED':2})

GC_48 = Coupling(name = 'GC_48',
                 value = '(4*ee*complex(0,1)*G*I148x66)/3. + (4*ee*complex(0,1)*G*I149x66)/3.',
                 order = {'QCD':1,'QED':1})

GC_49 = Coupling(name = 'GC_49',
                 value = 'complex(0,1)*G**2*I148x66 + complex(0,1)*G**2*I149x66',
                 order = {'QCD':2})

GC_50 = Coupling(name = 'GC_50',
                 value = '(2*ee**2*complex(0,1)*I15x11)/9.',
                 order = {'QED':2})

GC_51 = Coupling(name = 'GC_51',
                 value = '(-2*ee*complex(0,1)*G*I15x11)/3.',
                 order = {'QCD':1,'QED':1})

GC_52 = Coupling(name = 'GC_52',
                 value = 'complex(0,1)*G**2*I15x11',
                 order = {'QCD':2})

GC_53 = Coupling(name = 'GC_53',
                 value = '(2*ee**2*complex(0,1)*I15x22)/9.',
                 order = {'QED':2})

GC_54 = Coupling(name = 'GC_54',
                 value = '(-2*ee*complex(0,1)*G*I15x22)/3.',
                 order = {'QCD':1,'QED':1})

GC_55 = Coupling(name = 'GC_55',
                 value = 'complex(0,1)*G**2*I15x22',
                 order = {'QCD':2})

GC_56 = Coupling(name = 'GC_56',
                 value = '(2*ee**2*complex(0,1)*I15x33)/9. + (2*ee**2*complex(0,1)*I16x33)/9.',
                 order = {'QED':2})

GC_57 = Coupling(name = 'GC_57',
                 value = '(-2*ee*complex(0,1)*G*I15x33)/3. - (2*ee*complex(0,1)*G*I16x33)/3.',
                 order = {'QCD':1,'QED':1})

GC_58 = Coupling(name = 'GC_58',
                 value = 'complex(0,1)*G**2*I15x33 + complex(0,1)*G**2*I16x33',
                 order = {'QCD':2})

GC_59 = Coupling(name = 'GC_59',
                 value = '(2*ee**2*complex(0,1)*I15x36)/9. + (2*ee**2*complex(0,1)*I16x36)/9.',
                 order = {'QED':2})

GC_60 = Coupling(name = 'GC_60',
                 value = '(-2*ee*complex(0,1)*G*I15x36)/3. - (2*ee*complex(0,1)*G*I16x36)/3.',
                 order = {'QCD':1,'QED':1})

GC_61 = Coupling(name = 'GC_61',
                 value = 'complex(0,1)*G**2*I15x36 + complex(0,1)*G**2*I16x36',
                 order = {'QCD':2})

GC_62 = Coupling(name = 'GC_62',
                 value = '(2*ee**2*complex(0,1)*I16x44)/9.',
                 order = {'QED':2})

GC_63 = Coupling(name = 'GC_63',
                 value = '(-2*ee*complex(0,1)*G*I16x44)/3.',
                 order = {'QCD':1,'QED':1})

GC_64 = Coupling(name = 'GC_64',
                 value = 'complex(0,1)*G**2*I16x44',
                 order = {'QCD':2})

GC_65 = Coupling(name = 'GC_65',
                 value = '(2*ee**2*complex(0,1)*I16x55)/9.',
                 order = {'QED':2})

GC_66 = Coupling(name = 'GC_66',
                 value = '(-2*ee*complex(0,1)*G*I16x55)/3.',
                 order = {'QCD':1,'QED':1})

GC_67 = Coupling(name = 'GC_67',
                 value = 'complex(0,1)*G**2*I16x55',
                 order = {'QCD':2})

GC_68 = Coupling(name = 'GC_68',
                 value = '(2*ee**2*complex(0,1)*I15x63)/9. + (2*ee**2*complex(0,1)*I16x63)/9.',
                 order = {'QED':2})

GC_69 = Coupling(name = 'GC_69',
                 value = '(-2*ee*complex(0,1)*G*I15x63)/3. - (2*ee*complex(0,1)*G*I16x63)/3.',
                 order = {'QCD':1,'QED':1})

GC_70 = Coupling(name = 'GC_70',
                 value = 'complex(0,1)*G**2*I15x63 + complex(0,1)*G**2*I16x63',
                 order = {'QCD':2})

GC_71 = Coupling(name = 'GC_71',
                 value = '(2*ee**2*complex(0,1)*I15x66)/9. + (2*ee**2*complex(0,1)*I16x66)/9.',
                 order = {'QED':2})

GC_72 = Coupling(name = 'GC_72',
                 value = '(-2*ee*complex(0,1)*G*I15x66)/3. - (2*ee*complex(0,1)*G*I16x66)/3.',
                 order = {'QCD':1,'QED':1})

GC_73 = Coupling(name = 'GC_73',
                 value = 'complex(0,1)*G**2*I15x66 + complex(0,1)*G**2*I16x66',
                 order = {'QCD':2})

GC_74 = Coupling(name = 'GC_74',
                 value = 'ee*complex(0,1)*I47x11',
                 order = {'QED':1})

GC_75 = Coupling(name = 'GC_75',
                 value = 'ee*complex(0,1)*I47x22',
                 order = {'QED':1})

GC_76 = Coupling(name = 'GC_76',
                 value = 'ee*complex(0,1)*I47x33 + ee*complex(0,1)*I48x33',
                 order = {'QED':1})

GC_77 = Coupling(name = 'GC_77',
                 value = 'ee*complex(0,1)*I47x36 + ee*complex(0,1)*I48x36',
                 order = {'QED':1})

GC_78 = Coupling(name = 'GC_78',
                 value = 'ee*complex(0,1)*I48x44',
                 order = {'QED':1})

GC_79 = Coupling(name = 'GC_79',
                 value = 'ee*complex(0,1)*I48x55',
                 order = {'QED':1})

GC_80 = Coupling(name = 'GC_80',
                 value = '-(ee*complex(0,1)*I47x63) - ee*complex(0,1)*I48x63',
                 order = {'QED':1})

GC_81 = Coupling(name = 'GC_81',
                 value = 'ee*complex(0,1)*I47x66 + ee*complex(0,1)*I48x66',
                 order = {'QED':1})

GC_82 = Coupling(name = 'GC_82',
                 value = '2*ee**2*complex(0,1)*I53x11',
                 order = {'QED':2})

GC_83 = Coupling(name = 'GC_83',
                 value = '2*ee**2*complex(0,1)*I53x22',
                 order = {'QED':2})

GC_84 = Coupling(name = 'GC_84',
                 value = '2*ee**2*complex(0,1)*I53x33 + 2*ee**2*complex(0,1)*I54x33',
                 order = {'QED':2})

GC_85 = Coupling(name = 'GC_85',
                 value = '2*ee**2*complex(0,1)*I53x36 + 2*ee**2*complex(0,1)*I54x36',
                 order = {'QED':2})

GC_86 = Coupling(name = 'GC_86',
                 value = '2*ee**2*complex(0,1)*I54x44',
                 order = {'QED':2})

GC_87 = Coupling(name = 'GC_87',
                 value = '2*ee**2*complex(0,1)*I54x55',
                 order = {'QED':2})

GC_88 = Coupling(name = 'GC_88',
                 value = '2*ee**2*complex(0,1)*I53x63 + 2*ee**2*complex(0,1)*I54x63',
                 order = {'QED':2})

GC_89 = Coupling(name = 'GC_89',
                 value = '2*ee**2*complex(0,1)*I53x66 + 2*ee**2*complex(0,1)*I54x66',
                 order = {'QED':2})

GC_90 = Coupling(name = 'GC_90',
                 value = '(ee*complex(0,1)*I8x11)/3.',
                 order = {'QED':1})

GC_91 = Coupling(name = 'GC_91',
                 value = '-(complex(0,1)*G*I8x11)',
                 order = {'QCD':1})

GC_92 = Coupling(name = 'GC_92',
                 value = '(ee*complex(0,1)*I8x22)/3.',
                 order = {'QED':1})

GC_93 = Coupling(name = 'GC_93',
                 value = '-(complex(0,1)*G*I8x22)',
                 order = {'QCD':1})

GC_94 = Coupling(name = 'GC_94',
                 value = '(ee*complex(0,1)*I8x33)/3. + (ee*complex(0,1)*I9x33)/3.',
                 order = {'QED':1})

GC_95 = Coupling(name = 'GC_95',
                 value = '-(complex(0,1)*G*I8x33) - complex(0,1)*G*I9x33',
                 order = {'QCD':1})

GC_96 = Coupling(name = 'GC_96',
                 value = '(ee*complex(0,1)*I8x36)/3. + (ee*complex(0,1)*I9x36)/3.',
                 order = {'QED':1})

GC_97 = Coupling(name = 'GC_97',
                 value = '-(complex(0,1)*G*I8x36) - complex(0,1)*G*I9x36',
                 order = {'QCD':1})

GC_98 = Coupling(name = 'GC_98',
                 value = '(ee*complex(0,1)*I9x44)/3.',
                 order = {'QED':1})

GC_99 = Coupling(name = 'GC_99',
                 value = '-(complex(0,1)*G*I9x44)',
                 order = {'QCD':1})

GC_100 = Coupling(name = 'GC_100',
                  value = '(ee*complex(0,1)*I9x55)/3.',
                  order = {'QED':1})

GC_101 = Coupling(name = 'GC_101',
                  value = '-(complex(0,1)*G*I9x55)',
                  order = {'QCD':1})

GC_102 = Coupling(name = 'GC_102',
                  value = '-(ee*complex(0,1)*I8x63)/3. - (ee*complex(0,1)*I9x63)/3.',
                  order = {'QED':1})

GC_103 = Coupling(name = 'GC_103',
                  value = 'complex(0,1)*G*I8x63 + complex(0,1)*G*I9x63',
                  order = {'QCD':1})

GC_104 = Coupling(name = 'GC_104',
                  value = '(ee*complex(0,1)*I8x66)/3. + (ee*complex(0,1)*I9x66)/3.',
                  order = {'QED':1})

GC_105 = Coupling(name = 'GC_105',
                  value = '-(complex(0,1)*G*I8x66) - complex(0,1)*G*I9x66',
                  order = {'QCD':1})

GC_106 = Coupling(name = 'GC_106',
                  value = '-(complex(0,1)*G*Rd11*cmath.sqrt(2))',
                  order = {'QCD':1})

GC_107 = Coupling(name = 'GC_107',
                  value = '-(complex(0,1)*G*Rd22*cmath.sqrt(2))',
                  order = {'QCD':1})

GC_108 = Coupling(name = 'GC_108',
                  value = '-(complex(0,1)*G*Rd33*cmath.sqrt(2))',
                  order = {'QCD':1})

GC_109 = Coupling(name = 'GC_109',
                  value = 'complex(0,1)*G*Rd36*cmath.sqrt(2)',
                  order = {'QCD':1})

GC_110 = Coupling(name = 'GC_110',
                  value = 'complex(0,1)*G*Rd44*cmath.sqrt(2)',
                  order = {'QCD':1})

GC_111 = Coupling(name = 'GC_111',
                  value = 'complex(0,1)*G*Rd55*cmath.sqrt(2)',
                  order = {'QCD':1})

GC_112 = Coupling(name = 'GC_112',
                  value = '-(complex(0,1)*G*Rd63*cmath.sqrt(2))',
                  order = {'QCD':1})

GC_113 = Coupling(name = 'GC_113',
                  value = 'complex(0,1)*G*Rd66*cmath.sqrt(2)',
                  order = {'QCD':1})

GC_114 = Coupling(name = 'GC_114',
                  value = '-(complex(0,1)*G*Ru11*cmath.sqrt(2))',
                  order = {'QCD':1})

GC_115 = Coupling(name = 'GC_115',
                  value = '-(complex(0,1)*G*Ru22*cmath.sqrt(2))',
                  order = {'QCD':1})

GC_116 = Coupling(name = 'GC_116',
                  value = '-(complex(0,1)*G*Ru33*cmath.sqrt(2))',
                  order = {'QCD':1})

GC_117 = Coupling(name = 'GC_117',
                  value = 'complex(0,1)*G*Ru36*cmath.sqrt(2)',
                  order = {'QCD':1})

GC_118 = Coupling(name = 'GC_118',
                  value = 'complex(0,1)*G*Ru44*cmath.sqrt(2)',
                  order = {'QCD':1})

GC_119 = Coupling(name = 'GC_119',
                  value = 'complex(0,1)*G*Ru55*cmath.sqrt(2)',
                  order = {'QCD':1})

GC_120 = Coupling(name = 'GC_120',
                  value = '-(complex(0,1)*G*Ru63*cmath.sqrt(2))',
                  order = {'QCD':1})

GC_121 = Coupling(name = 'GC_121',
                  value = 'complex(0,1)*G*Ru66*cmath.sqrt(2)',
                  order = {'QCD':1})

GC_122 = Coupling(name = 'GC_122',
                  value = '-(ee**2*complex(0,1)) + (ee**2*complex(0,1))/sw**2',
                  order = {'QED':2})

GC_123 = Coupling(name = 'GC_123',
                  value = '-(complex(0,1)*I129x33*I130x33) - (ee**2*complex(0,1)*I127x33*I128x33)/(2.*sw**2)',
                  order = {'QED':2})

GC_124 = Coupling(name = 'GC_124',
                  value = '-(complex(0,1)*I129x33*I130x36) - (ee**2*complex(0,1)*I127x36*I128x33)/(2.*sw**2)',
                  order = {'QED':2})

GC_125 = Coupling(name = 'GC_125',
                  value = '-(complex(0,1)*I129x33*I130x63) - (ee**2*complex(0,1)*I127x63*I128x33)/(2.*sw**2)',
                  order = {'QED':2})

GC_126 = Coupling(name = 'GC_126',
                  value = '-(complex(0,1)*I129x33*I130x66) - (ee**2*complex(0,1)*I127x66*I128x33)/(2.*sw**2)',
                  order = {'QED':2})

GC_127 = Coupling(name = 'GC_127',
                  value = '-(complex(0,1)*I129x36*I130x33) - (ee**2*complex(0,1)*I127x33*I128x36)/(2.*sw**2)',
                  order = {'QED':2})

GC_128 = Coupling(name = 'GC_128',
                  value = '-(complex(0,1)*I129x36*I130x36) - (ee**2*complex(0,1)*I127x36*I128x36)/(2.*sw**2)',
                  order = {'QED':2})

GC_129 = Coupling(name = 'GC_129',
                  value = '-(complex(0,1)*I129x36*I130x63) - (ee**2*complex(0,1)*I127x63*I128x36)/(2.*sw**2)',
                  order = {'QED':2})

GC_130 = Coupling(name = 'GC_130',
                  value = '-(complex(0,1)*I129x36*I130x66) - (ee**2*complex(0,1)*I127x66*I128x36)/(2.*sw**2)',
                  order = {'QED':2})

GC_131 = Coupling(name = 'GC_131',
                  value = '-(complex(0,1)*I110x33*I160x33) - (ee**2*complex(0,1)*I107x33*I159x33)/(2.*sw**2)',
                  order = {'QED':2})

GC_132 = Coupling(name = 'GC_132',
                  value = '-(complex(0,1)*I110x36*I160x33) - (ee**2*complex(0,1)*I107x36*I159x33)/(2.*sw**2)',
                  order = {'QED':2})

GC_133 = Coupling(name = 'GC_133',
                  value = '-(complex(0,1)*I110x33*I160x36) - (ee**2*complex(0,1)*I107x33*I159x36)/(2.*sw**2)',
                  order = {'QED':2})

GC_134 = Coupling(name = 'GC_134',
                  value = '-(complex(0,1)*I110x36*I160x36) - (ee**2*complex(0,1)*I107x36*I159x36)/(2.*sw**2)',
                  order = {'QED':2})

GC_135 = Coupling(name = 'GC_135',
                  value = '-(complex(0,1)*I110x33*I160x63) - (ee**2*complex(0,1)*I107x33*I159x63)/(2.*sw**2)',
                  order = {'QED':2})

GC_136 = Coupling(name = 'GC_136',
                  value = '-(complex(0,1)*I110x36*I160x63) - (ee**2*complex(0,1)*I107x36*I159x63)/(2.*sw**2)',
                  order = {'QED':2})

GC_137 = Coupling(name = 'GC_137',
                  value = '-(complex(0,1)*I110x33*I160x66) - (ee**2*complex(0,1)*I107x33*I159x66)/(2.*sw**2)',
                  order = {'QED':2})

GC_138 = Coupling(name = 'GC_138',
                  value = '-(complex(0,1)*I110x36*I160x66) - (ee**2*complex(0,1)*I107x36*I159x66)/(2.*sw**2)',
                  order = {'QED':2})

GC_139 = Coupling(name = 'GC_139',
                  value = '(ee**2*complex(0,1))/(2.*sw**2)',
                  order = {'QED':2})

GC_140 = Coupling(name = 'GC_140',
                  value = '-((ee**2*complex(0,1))/sw**2)',
                  order = {'QED':2})

GC_141 = Coupling(name = 'GC_141',
                  value = '(ee**2*complex(0,1)*I105x11)/(2.*sw**2)',
                  order = {'QED':2})

GC_142 = Coupling(name = 'GC_142',
                  value = '(ee**2*complex(0,1)*I105x22)/(2.*sw**2)',
                  order = {'QED':2})

GC_143 = Coupling(name = 'GC_143',
                  value = '(ee**2*complex(0,1)*I105x33)/(2.*sw**2)',
                  order = {'QED':2})

GC_144 = Coupling(name = 'GC_144',
                  value = '(ee**2*complex(0,1)*I105x36)/(2.*sw**2)',
                  order = {'QED':2})

GC_145 = Coupling(name = 'GC_145',
                  value = '(ee**2*complex(0,1)*I105x63)/(2.*sw**2)',
                  order = {'QED':2})

GC_146 = Coupling(name = 'GC_146',
                  value = '(ee**2*complex(0,1)*I105x66)/(2.*sw**2)',
                  order = {'QED':2})

GC_147 = Coupling(name = 'GC_147',
                  value = '-(ee**2*complex(0,1)*I127x11*I128x11)/(2.*sw**2)',
                  order = {'QED':2})

GC_148 = Coupling(name = 'GC_148',
                  value = '-(ee**2*complex(0,1)*I127x22*I128x11)/(2.*sw**2)',
                  order = {'QED':2})

GC_149 = Coupling(name = 'GC_149',
                  value = '-(ee**2*complex(0,1)*I127x33*I128x11)/(2.*sw**2)',
                  order = {'QED':2})

GC_150 = Coupling(name = 'GC_150',
                  value = '-(ee**2*complex(0,1)*I127x36*I128x11)/(2.*sw**2)',
                  order = {'QED':2})

GC_151 = Coupling(name = 'GC_151',
                  value = '-(ee**2*complex(0,1)*I127x63*I128x11)/(2.*sw**2)',
                  order = {'QED':2})

GC_152 = Coupling(name = 'GC_152',
                  value = '-(ee**2*complex(0,1)*I127x66*I128x11)/(2.*sw**2)',
                  order = {'QED':2})

GC_153 = Coupling(name = 'GC_153',
                  value = '-(ee**2*complex(0,1)*I127x11*I128x22)/(2.*sw**2)',
                  order = {'QED':2})

GC_154 = Coupling(name = 'GC_154',
                  value = '-(ee**2*complex(0,1)*I127x22*I128x22)/(2.*sw**2)',
                  order = {'QED':2})

GC_155 = Coupling(name = 'GC_155',
                  value = '-(ee**2*complex(0,1)*I127x33*I128x22)/(2.*sw**2)',
                  order = {'QED':2})

GC_156 = Coupling(name = 'GC_156',
                  value = '-(ee**2*complex(0,1)*I127x36*I128x22)/(2.*sw**2)',
                  order = {'QED':2})

GC_157 = Coupling(name = 'GC_157',
                  value = '-(ee**2*complex(0,1)*I127x63*I128x22)/(2.*sw**2)',
                  order = {'QED':2})

GC_158 = Coupling(name = 'GC_158',
                  value = '-(ee**2*complex(0,1)*I127x66*I128x22)/(2.*sw**2)',
                  order = {'QED':2})

GC_159 = Coupling(name = 'GC_159',
                  value = '-(ee**2*complex(0,1)*I127x11*I128x33)/(2.*sw**2)',
                  order = {'QED':2})

GC_160 = Coupling(name = 'GC_160',
                  value = '-(ee**2*complex(0,1)*I127x22*I128x33)/(2.*sw**2)',
                  order = {'QED':2})

GC_161 = Coupling(name = 'GC_161',
                  value = '-(ee**2*complex(0,1)*I127x11*I128x36)/(2.*sw**2)',
                  order = {'QED':2})

GC_162 = Coupling(name = 'GC_162',
                  value = '-(ee**2*complex(0,1)*I127x22*I128x36)/(2.*sw**2)',
                  order = {'QED':2})

GC_163 = Coupling(name = 'GC_163',
                  value = '-(ee**2*complex(0,1)*I107x11*I159x11)/(2.*sw**2)',
                  order = {'QED':2})

GC_164 = Coupling(name = 'GC_164',
                  value = '-(ee**2*complex(0,1)*I107x22*I159x11)/(2.*sw**2)',
                  order = {'QED':2})

GC_165 = Coupling(name = 'GC_165',
                  value = '-(ee**2*complex(0,1)*I107x33*I159x11)/(2.*sw**2)',
                  order = {'QED':2})

GC_166 = Coupling(name = 'GC_166',
                  value = '-(ee**2*complex(0,1)*I107x36*I159x11)/(2.*sw**2)',
                  order = {'QED':2})

GC_167 = Coupling(name = 'GC_167',
                  value = '-(ee**2*complex(0,1)*I107x11*I159x22)/(2.*sw**2)',
                  order = {'QED':2})

GC_168 = Coupling(name = 'GC_168',
                  value = '-(ee**2*complex(0,1)*I107x22*I159x22)/(2.*sw**2)',
                  order = {'QED':2})

GC_169 = Coupling(name = 'GC_169',
                  value = '-(ee**2*complex(0,1)*I107x33*I159x22)/(2.*sw**2)',
                  order = {'QED':2})

GC_170 = Coupling(name = 'GC_170',
                  value = '-(ee**2*complex(0,1)*I107x36*I159x22)/(2.*sw**2)',
                  order = {'QED':2})

GC_171 = Coupling(name = 'GC_171',
                  value = '-(ee**2*complex(0,1)*I107x11*I159x33)/(2.*sw**2)',
                  order = {'QED':2})

GC_172 = Coupling(name = 'GC_172',
                  value = '-(ee**2*complex(0,1)*I107x22*I159x33)/(2.*sw**2)',
                  order = {'QED':2})

GC_173 = Coupling(name = 'GC_173',
                  value = '-(ee**2*complex(0,1)*I107x11*I159x36)/(2.*sw**2)',
                  order = {'QED':2})

GC_174 = Coupling(name = 'GC_174',
                  value = '-(ee**2*complex(0,1)*I107x22*I159x36)/(2.*sw**2)',
                  order = {'QED':2})

GC_175 = Coupling(name = 'GC_175',
                  value = '-(ee**2*complex(0,1)*I107x11*I159x63)/(2.*sw**2)',
                  order = {'QED':2})

GC_176 = Coupling(name = 'GC_176',
                  value = '-(ee**2*complex(0,1)*I107x22*I159x63)/(2.*sw**2)',
                  order = {'QED':2})

GC_177 = Coupling(name = 'GC_177',
                  value = '-(ee**2*complex(0,1)*I107x11*I159x66)/(2.*sw**2)',
                  order = {'QED':2})

GC_178 = Coupling(name = 'GC_178',
                  value = '-(ee**2*complex(0,1)*I107x22*I159x66)/(2.*sw**2)',
                  order = {'QED':2})

GC_179 = Coupling(name = 'GC_179',
                  value = '(ee**2*complex(0,1)*I201x11)/(2.*sw**2)',
                  order = {'QED':2})

GC_180 = Coupling(name = 'GC_180',
                  value = '(ee**2*complex(0,1)*I201x22)/(2.*sw**2)',
                  order = {'QED':2})

GC_181 = Coupling(name = 'GC_181',
                  value = '(ee**2*complex(0,1)*I201x33)/(2.*sw**2)',
                  order = {'QED':2})

GC_182 = Coupling(name = 'GC_182',
                  value = '(ee**2*complex(0,1)*I201x36)/(2.*sw**2)',
                  order = {'QED':2})

GC_183 = Coupling(name = 'GC_183',
                  value = '(ee**2*complex(0,1)*I201x63)/(2.*sw**2)',
                  order = {'QED':2})

GC_184 = Coupling(name = 'GC_184',
                  value = '(ee**2*complex(0,1)*I201x66)/(2.*sw**2)',
                  order = {'QED':2})

GC_185 = Coupling(name = 'GC_185',
                  value = '(ee**2*complex(0,1)*I63x11)/(2.*sw**2)',
                  order = {'QED':2})

GC_186 = Coupling(name = 'GC_186',
                  value = '(ee**2*complex(0,1)*I63x22)/(2.*sw**2)',
                  order = {'QED':2})

GC_187 = Coupling(name = 'GC_187',
                  value = '(ee**2*complex(0,1)*I63x33)/(2.*sw**2)',
                  order = {'QED':2})

GC_188 = Coupling(name = 'GC_188',
                  value = '(ee**2*complex(0,1)*I63x36)/(2.*sw**2)',
                  order = {'QED':2})

GC_189 = Coupling(name = 'GC_189',
                  value = '(ee**2*complex(0,1)*I63x63)/(2.*sw**2)',
                  order = {'QED':2})

GC_190 = Coupling(name = 'GC_190',
                  value = '(ee**2*complex(0,1)*I63x66)/(2.*sw**2)',
                  order = {'QED':2})

GC_191 = Coupling(name = 'GC_191',
                  value = '(ee*complex(0,1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_192 = Coupling(name = 'GC_192',
                  value = '(CKM11*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_193 = Coupling(name = 'GC_193',
                  value = '(CKM22*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_194 = Coupling(name = 'GC_194',
                  value = '(CKM33*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_195 = Coupling(name = 'GC_195',
                  value = '-((cw*ee*complex(0,1))/sw)',
                  order = {'QED':1})

GC_196 = Coupling(name = 'GC_196',
                  value = '(cw*ee*complex(0,1))/sw',
                  order = {'QED':1})

GC_197 = Coupling(name = 'GC_197',
                  value = '(-2*cw*ee**2*complex(0,1))/sw',
                  order = {'QED':2})

GC_198 = Coupling(name = 'GC_198',
                  value = '(ee**2*complex(0,1)*I115x11)/(3.*sw*cmath.sqrt(2))',
                  order = {'QED':2})

GC_199 = Coupling(name = 'GC_199',
                  value = '(ee*complex(0,1)*G*I115x11*cmath.sqrt(2))/sw',
                  order = {'QCD':1,'QED':1})

GC_200 = Coupling(name = 'GC_200',
                  value = '(ee**2*complex(0,1)*I115x22)/(3.*sw*cmath.sqrt(2))',
                  order = {'QED':2})

GC_201 = Coupling(name = 'GC_201',
                  value = '(ee*complex(0,1)*G*I115x22*cmath.sqrt(2))/sw',
                  order = {'QCD':1,'QED':1})

GC_202 = Coupling(name = 'GC_202',
                  value = '(ee**2*complex(0,1)*I115x33)/(3.*sw*cmath.sqrt(2))',
                  order = {'QED':2})

GC_203 = Coupling(name = 'GC_203',
                  value = '(ee*complex(0,1)*G*I115x33*cmath.sqrt(2))/sw',
                  order = {'QCD':1,'QED':1})

GC_204 = Coupling(name = 'GC_204',
                  value = '(ee**2*complex(0,1)*I115x36)/(3.*sw*cmath.sqrt(2))',
                  order = {'QED':2})

GC_205 = Coupling(name = 'GC_205',
                  value = '(ee*complex(0,1)*G*I115x36*cmath.sqrt(2))/sw',
                  order = {'QCD':1,'QED':1})

GC_206 = Coupling(name = 'GC_206',
                  value = '(ee**2*complex(0,1)*I115x63)/(3.*sw*cmath.sqrt(2))',
                  order = {'QED':2})

GC_207 = Coupling(name = 'GC_207',
                  value = '(ee*complex(0,1)*G*I115x63*cmath.sqrt(2))/sw',
                  order = {'QCD':1,'QED':1})

GC_208 = Coupling(name = 'GC_208',
                  value = '(ee**2*complex(0,1)*I115x66)/(3.*sw*cmath.sqrt(2))',
                  order = {'QED':2})

GC_209 = Coupling(name = 'GC_209',
                  value = '(ee*complex(0,1)*G*I115x66*cmath.sqrt(2))/sw',
                  order = {'QCD':1,'QED':1})

GC_210 = Coupling(name = 'GC_210',
                  value = '(ee**2*complex(0,1)*I136x11)/(3.*sw*cmath.sqrt(2))',
                  order = {'QED':2})

GC_211 = Coupling(name = 'GC_211',
                  value = '(ee*complex(0,1)*G*I136x11*cmath.sqrt(2))/sw',
                  order = {'QCD':1,'QED':1})

GC_212 = Coupling(name = 'GC_212',
                  value = '(ee**2*complex(0,1)*I136x22)/(3.*sw*cmath.sqrt(2))',
                  order = {'QED':2})

GC_213 = Coupling(name = 'GC_213',
                  value = '(ee*complex(0,1)*G*I136x22*cmath.sqrt(2))/sw',
                  order = {'QCD':1,'QED':1})

GC_214 = Coupling(name = 'GC_214',
                  value = '(ee**2*complex(0,1)*I136x33)/(3.*sw*cmath.sqrt(2))',
                  order = {'QED':2})

GC_215 = Coupling(name = 'GC_215',
                  value = '(ee*complex(0,1)*G*I136x33*cmath.sqrt(2))/sw',
                  order = {'QCD':1,'QED':1})

GC_216 = Coupling(name = 'GC_216',
                  value = '(ee**2*complex(0,1)*I136x36)/(3.*sw*cmath.sqrt(2))',
                  order = {'QED':2})

GC_217 = Coupling(name = 'GC_217',
                  value = '(ee*complex(0,1)*G*I136x36*cmath.sqrt(2))/sw',
                  order = {'QCD':1,'QED':1})

GC_218 = Coupling(name = 'GC_218',
                  value = '(ee**2*complex(0,1)*I136x63)/(3.*sw*cmath.sqrt(2))',
                  order = {'QED':2})

GC_219 = Coupling(name = 'GC_219',
                  value = '(ee*complex(0,1)*G*I136x63*cmath.sqrt(2))/sw',
                  order = {'QCD':1,'QED':1})

GC_220 = Coupling(name = 'GC_220',
                  value = '(ee**2*complex(0,1)*I136x66)/(3.*sw*cmath.sqrt(2))',
                  order = {'QED':2})

GC_221 = Coupling(name = 'GC_221',
                  value = '(ee*complex(0,1)*G*I136x66*cmath.sqrt(2))/sw',
                  order = {'QCD':1,'QED':1})

GC_222 = Coupling(name = 'GC_222',
                  value = '-((ee*complex(0,1)*I197x11)/(sw*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_223 = Coupling(name = 'GC_223',
                  value = '-((ee*complex(0,1)*I197x22)/(sw*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_224 = Coupling(name = 'GC_224',
                  value = '-((ee*complex(0,1)*I197x33)/(sw*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_225 = Coupling(name = 'GC_225',
                  value = '-((ee*complex(0,1)*I197x36)/(sw*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_226 = Coupling(name = 'GC_226',
                  value = '-((ee*complex(0,1)*I197x63)/(sw*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_227 = Coupling(name = 'GC_227',
                  value = '-((ee*complex(0,1)*I197x66)/(sw*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_228 = Coupling(name = 'GC_228',
                  value = '-((ee*complex(0,1)*I198x11)/(sw*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_229 = Coupling(name = 'GC_229',
                  value = '-((ee*complex(0,1)*I198x22)/(sw*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_230 = Coupling(name = 'GC_230',
                  value = '-((ee*complex(0,1)*I198x33)/(sw*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_231 = Coupling(name = 'GC_231',
                  value = '-((ee*complex(0,1)*I198x36)/(sw*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_232 = Coupling(name = 'GC_232',
                  value = '(ee*complex(0,1)*I199x11)/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_233 = Coupling(name = 'GC_233',
                  value = '(ee*complex(0,1)*I199x22)/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_234 = Coupling(name = 'GC_234',
                  value = '(ee*complex(0,1)*I199x33)/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_235 = Coupling(name = 'GC_235',
                  value = '(ee*complex(0,1)*I199x36)/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_236 = Coupling(name = 'GC_236',
                  value = '(ee*complex(0,1)*I199x63)/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_237 = Coupling(name = 'GC_237',
                  value = '(ee*complex(0,1)*I199x66)/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_238 = Coupling(name = 'GC_238',
                  value = '(ee*complex(0,1)*I200x11)/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_239 = Coupling(name = 'GC_239',
                  value = '(ee*complex(0,1)*I200x22)/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_240 = Coupling(name = 'GC_240',
                  value = '(ee*complex(0,1)*I200x33)/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_241 = Coupling(name = 'GC_241',
                  value = '(ee*complex(0,1)*I200x36)/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_242 = Coupling(name = 'GC_242',
                  value = '-((ee**2*complex(0,1)*I90x11)/(sw*cmath.sqrt(2)))',
                  order = {'QED':2})

GC_243 = Coupling(name = 'GC_243',
                  value = '-((ee**2*complex(0,1)*I90x22)/(sw*cmath.sqrt(2)))',
                  order = {'QED':2})

GC_244 = Coupling(name = 'GC_244',
                  value = '-((ee**2*complex(0,1)*I90x33)/(sw*cmath.sqrt(2)))',
                  order = {'QED':2})

GC_245 = Coupling(name = 'GC_245',
                  value = '-((ee**2*complex(0,1)*I90x36)/(sw*cmath.sqrt(2)))',
                  order = {'QED':2})

GC_246 = Coupling(name = 'GC_246',
                  value = '-((ee**2*complex(0,1)*I98x11)/(sw*cmath.sqrt(2)))',
                  order = {'QED':2})

GC_247 = Coupling(name = 'GC_247',
                  value = '-((ee**2*complex(0,1)*I98x22)/(sw*cmath.sqrt(2)))',
                  order = {'QED':2})

GC_248 = Coupling(name = 'GC_248',
                  value = '-((ee**2*complex(0,1)*I98x33)/(sw*cmath.sqrt(2)))',
                  order = {'QED':2})

GC_249 = Coupling(name = 'GC_249',
                  value = '-((ee**2*complex(0,1)*I98x36)/(sw*cmath.sqrt(2)))',
                  order = {'QED':2})

GC_250 = Coupling(name = 'GC_250',
                  value = '-(ee**2*complex(0,1)*I106x44)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_251 = Coupling(name = 'GC_251',
                  value = '-(ee**2*complex(0,1)*I106x55)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_252 = Coupling(name = 'GC_252',
                  value = '(ee**2*complex(0,1)*I149x44)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_253 = Coupling(name = 'GC_253',
                  value = '(ee**2*complex(0,1)*I149x55)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_254 = Coupling(name = 'GC_254',
                  value = '(ee**2*complex(0,1)*I106x44*I161x11)/(6.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_255 = Coupling(name = 'GC_255',
                  value = '(ee**2*complex(0,1)*I106x55*I161x11)/(6.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_256 = Coupling(name = 'GC_256',
                  value = '(ee**2*complex(0,1)*I106x44*I161x22)/(6.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_257 = Coupling(name = 'GC_257',
                  value = '(ee**2*complex(0,1)*I106x55*I161x22)/(6.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_258 = Coupling(name = 'GC_258',
                  value = '(ee**2*complex(0,1)*I105x11*I162x44)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_259 = Coupling(name = 'GC_259',
                  value = '(ee**2*complex(0,1)*I105x22*I162x44)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_260 = Coupling(name = 'GC_260',
                  value = '(-2*ee**2*complex(0,1)*I106x44*I162x44)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_261 = Coupling(name = 'GC_261',
                  value = '(-2*ee**2*complex(0,1)*I106x55*I162x44)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_262 = Coupling(name = 'GC_262',
                  value = '(ee**2*complex(0,1)*I105x11*I162x55)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_263 = Coupling(name = 'GC_263',
                  value = '(ee**2*complex(0,1)*I105x22*I162x55)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_264 = Coupling(name = 'GC_264',
                  value = '(-2*ee**2*complex(0,1)*I106x44*I162x55)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_265 = Coupling(name = 'GC_265',
                  value = '(-2*ee**2*complex(0,1)*I106x55*I162x55)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_266 = Coupling(name = 'GC_266',
                  value = '(4*ee**2*complex(0,1)*I172x44*I175x44)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_267 = Coupling(name = 'GC_267',
                  value = '(4*ee**2*complex(0,1)*I172x55*I175x55)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_268 = Coupling(name = 'GC_268',
                  value = '(4*ee**2*complex(0,1)*I177x44*I178x44)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_269 = Coupling(name = 'GC_269',
                  value = '(4*ee**2*complex(0,1)*I177x55*I178x55)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_270 = Coupling(name = 'GC_270',
                  value = '(cw*ee**2*complex(0,1)*I197x11)/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':2})

GC_271 = Coupling(name = 'GC_271',
                  value = '(cw*ee**2*complex(0,1)*I197x22)/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':2})

GC_272 = Coupling(name = 'GC_272',
                  value = '(cw*ee**2*complex(0,1)*I197x33)/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':2})

GC_273 = Coupling(name = 'GC_273',
                  value = '(cw*ee**2*complex(0,1)*I197x36)/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':2})

GC_274 = Coupling(name = 'GC_274',
                  value = '(cw*ee**2*complex(0,1)*I197x63)/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':2})

GC_275 = Coupling(name = 'GC_275',
                  value = '(cw*ee**2*complex(0,1)*I197x66)/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':2})

GC_276 = Coupling(name = 'GC_276',
                  value = '-((cw*ee**2*complex(0,1)*I198x11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)))',
                  order = {'QED':2})

GC_277 = Coupling(name = 'GC_277',
                  value = '-((cw*ee**2*complex(0,1)*I198x22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)))',
                  order = {'QED':2})

GC_278 = Coupling(name = 'GC_278',
                  value = '-((cw*ee**2*complex(0,1)*I198x33)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)))',
                  order = {'QED':2})

GC_279 = Coupling(name = 'GC_279',
                  value = '-((cw*ee**2*complex(0,1)*I198x36)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)))',
                  order = {'QED':2})

GC_280 = Coupling(name = 'GC_280',
                  value = '(cw*ee**2*complex(0,1)*I199x11)/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':2})

GC_281 = Coupling(name = 'GC_281',
                  value = '(cw*ee**2*complex(0,1)*I199x22)/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':2})

GC_282 = Coupling(name = 'GC_282',
                  value = '(cw*ee**2*complex(0,1)*I199x33)/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':2})

GC_283 = Coupling(name = 'GC_283',
                  value = '(cw*ee**2*complex(0,1)*I199x36)/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':2})

GC_284 = Coupling(name = 'GC_284',
                  value = '(cw*ee**2*complex(0,1)*I199x63)/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':2})

GC_285 = Coupling(name = 'GC_285',
                  value = '(cw*ee**2*complex(0,1)*I199x66)/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':2})

GC_286 = Coupling(name = 'GC_286',
                  value = '-((cw*ee**2*complex(0,1)*I200x11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)))',
                  order = {'QED':2})

GC_287 = Coupling(name = 'GC_287',
                  value = '-((cw*ee**2*complex(0,1)*I200x22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)))',
                  order = {'QED':2})

GC_288 = Coupling(name = 'GC_288',
                  value = '-((cw*ee**2*complex(0,1)*I200x33)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)))',
                  order = {'QED':2})

GC_289 = Coupling(name = 'GC_289',
                  value = '-((cw*ee**2*complex(0,1)*I200x36)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)))',
                  order = {'QED':2})

GC_290 = Coupling(name = 'GC_290',
                  value = '(ee**2*complex(0,1)*I30x44*I33x44)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_291 = Coupling(name = 'GC_291',
                  value = '(ee**2*complex(0,1)*I30x55*I33x55)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_292 = Coupling(name = 'GC_292',
                  value = '(ee**2*complex(0,1)*I35x44*I36x44)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_293 = Coupling(name = 'GC_293',
                  value = '(ee**2*complex(0,1)*I35x55*I36x55)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_294 = Coupling(name = 'GC_294',
                  value = '-(ee**2*complex(0,1)*I162x44*I63x11)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_295 = Coupling(name = 'GC_295',
                  value = '-(ee**2*complex(0,1)*I162x55*I63x11)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_296 = Coupling(name = 'GC_296',
                  value = '-(ee**2*complex(0,1)*I162x44*I63x22)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_297 = Coupling(name = 'GC_297',
                  value = '-(ee**2*complex(0,1)*I162x55*I63x22)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_298 = Coupling(name = 'GC_298',
                  value = '-(ee**2*complex(0,1)*I65x44)/(6.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_299 = Coupling(name = 'GC_299',
                  value = '(ee**2*complex(0,1)*I161x11*I65x44)/(18.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_300 = Coupling(name = 'GC_300',
                  value = '(ee**2*complex(0,1)*I161x22*I65x44)/(18.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_301 = Coupling(name = 'GC_301',
                  value = '(-2*ee**2*complex(0,1)*I162x44*I65x44)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_302 = Coupling(name = 'GC_302',
                  value = '(-2*ee**2*complex(0,1)*I162x55*I65x44)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_303 = Coupling(name = 'GC_303',
                  value = '-(ee**2*complex(0,1)*I64x11*I65x44)/(6.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_304 = Coupling(name = 'GC_304',
                  value = '-(ee**2*complex(0,1)*I64x22*I65x44)/(6.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_305 = Coupling(name = 'GC_305',
                  value = '-(ee**2*complex(0,1)*I65x55)/(6.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_306 = Coupling(name = 'GC_306',
                  value = '(ee**2*complex(0,1)*I161x11*I65x55)/(18.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_307 = Coupling(name = 'GC_307',
                  value = '(ee**2*complex(0,1)*I161x22*I65x55)/(18.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_308 = Coupling(name = 'GC_308',
                  value = '(-2*ee**2*complex(0,1)*I162x44*I65x55)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_309 = Coupling(name = 'GC_309',
                  value = '(-2*ee**2*complex(0,1)*I162x55*I65x55)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_310 = Coupling(name = 'GC_310',
                  value = '-(ee**2*complex(0,1)*I64x11*I65x55)/(6.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_311 = Coupling(name = 'GC_311',
                  value = '-(ee**2*complex(0,1)*I64x22*I65x55)/(6.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_312 = Coupling(name = 'GC_312',
                  value = '(ee**2*complex(0,1)*I63x11*I66x44)/(6.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_313 = Coupling(name = 'GC_313',
                  value = '(ee**2*complex(0,1)*I63x22*I66x44)/(6.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_314 = Coupling(name = 'GC_314',
                  value = '(ee**2*complex(0,1)*I65x44*I66x44)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_315 = Coupling(name = 'GC_315',
                  value = '(ee**2*complex(0,1)*I65x55*I66x44)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_316 = Coupling(name = 'GC_316',
                  value = '(ee**2*complex(0,1)*I63x11*I66x55)/(6.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_317 = Coupling(name = 'GC_317',
                  value = '(ee**2*complex(0,1)*I63x22*I66x55)/(6.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_318 = Coupling(name = 'GC_318',
                  value = '(ee**2*complex(0,1)*I65x44*I66x55)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_319 = Coupling(name = 'GC_319',
                  value = '(ee**2*complex(0,1)*I65x55*I66x55)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_320 = Coupling(name = 'GC_320',
                  value = '(cw*ee*complex(0,1)*NN11*Rd44*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_321 = Coupling(name = 'GC_321',
                  value = '(cw*ee*complex(0,1)*NN21*Rd44*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_322 = Coupling(name = 'GC_322',
                  value = '(cw*ee*complex(0,1)*NN31*Rd44*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_323 = Coupling(name = 'GC_323',
                  value = '(cw*ee*complex(0,1)*NN41*Rd44*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_324 = Coupling(name = 'GC_324',
                  value = '(cw*ee*complex(0,1)*NN11*Rd55*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_325 = Coupling(name = 'GC_325',
                  value = '(cw*ee*complex(0,1)*NN21*Rd55*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_326 = Coupling(name = 'GC_326',
                  value = '(cw*ee*complex(0,1)*NN31*Rd55*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_327 = Coupling(name = 'GC_327',
                  value = '(cw*ee*complex(0,1)*NN41*Rd55*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_328 = Coupling(name = 'GC_328',
                  value = '(cw*ee*complex(0,1)*NN11*Rl44*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_329 = Coupling(name = 'GC_329',
                  value = '(cw*ee*complex(0,1)*NN21*Rl44*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_330 = Coupling(name = 'GC_330',
                  value = '(cw*ee*complex(0,1)*NN31*Rl44*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_331 = Coupling(name = 'GC_331',
                  value = '(cw*ee*complex(0,1)*NN41*Rl44*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_332 = Coupling(name = 'GC_332',
                  value = '(cw*ee*complex(0,1)*NN11*Rl55*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_333 = Coupling(name = 'GC_333',
                  value = '(cw*ee*complex(0,1)*NN21*Rl55*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_334 = Coupling(name = 'GC_334',
                  value = '(cw*ee*complex(0,1)*NN31*Rl55*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_335 = Coupling(name = 'GC_335',
                  value = '(cw*ee*complex(0,1)*NN41*Rl55*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_336 = Coupling(name = 'GC_336',
                  value = '(-2*cw*ee*complex(0,1)*NN11*Ru44*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_337 = Coupling(name = 'GC_337',
                  value = '(-2*cw*ee*complex(0,1)*NN21*Ru44*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_338 = Coupling(name = 'GC_338',
                  value = '(-2*cw*ee*complex(0,1)*NN31*Ru44*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_339 = Coupling(name = 'GC_339',
                  value = '(-2*cw*ee*complex(0,1)*NN41*Ru44*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_340 = Coupling(name = 'GC_340',
                  value = '(-2*cw*ee*complex(0,1)*NN11*Ru55*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_341 = Coupling(name = 'GC_341',
                  value = '(-2*cw*ee*complex(0,1)*NN21*Ru55*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_342 = Coupling(name = 'GC_342',
                  value = '(-2*cw*ee*complex(0,1)*NN31*Ru55*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_343 = Coupling(name = 'GC_343',
                  value = '(-2*cw*ee*complex(0,1)*NN41*Ru55*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_344 = Coupling(name = 'GC_344',
                  value = '(ee**2*complex(0,1))/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_345 = Coupling(name = 'GC_345',
                  value = '-(ee**2*complex(0,1))/(2.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_346 = Coupling(name = 'GC_346',
                  value = '(ee**2*complex(0,1))/(2.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_347 = Coupling(name = 'GC_347',
                  value = '-(cw*ee*complex(0,1))/(2.*(-1 + sw)*sw*(1 + sw))',
                  order = {'QED':1})

GC_348 = Coupling(name = 'GC_348',
                  value = '(cw*ee*complex(0,1))/(2.*(-1 + sw)*sw*(1 + sw))',
                  order = {'QED':1})

GC_349 = Coupling(name = 'GC_349',
                  value = '-(cw*ee*complex(0,1)*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_350 = Coupling(name = 'GC_350',
                  value = '(2*cw*ee*complex(0,1)*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_351 = Coupling(name = 'GC_351',
                  value = '-((cw*ee*complex(0,1)*sw)/((-1 + sw)*(1 + sw)))',
                  order = {'QED':1})

GC_352 = Coupling(name = 'GC_352',
                  value = '(cw*ee*complex(0,1)*I106x44*sw)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_353 = Coupling(name = 'GC_353',
                  value = '(cw*ee*complex(0,1)*I106x55*sw)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_354 = Coupling(name = 'GC_354',
                  value = '(8*cw*ee**2*complex(0,1)*I114x44*sw)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_355 = Coupling(name = 'GC_355',
                  value = '(4*cw*ee*complex(0,1)*G*I114x44*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':1,'QED':1})

GC_356 = Coupling(name = 'GC_356',
                  value = '(8*cw*ee**2*complex(0,1)*I114x55*sw)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_357 = Coupling(name = 'GC_357',
                  value = '(4*cw*ee*complex(0,1)*G*I114x55*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':1,'QED':1})

GC_358 = Coupling(name = 'GC_358',
                  value = '(-2*cw*ee*complex(0,1)*I203x44*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_359 = Coupling(name = 'GC_359',
                  value = '(-2*cw*ee*complex(0,1)*I203x55*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_360 = Coupling(name = 'GC_360',
                  value = '(2*cw*ee**2*complex(0,1)*I48x44*sw)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_361 = Coupling(name = 'GC_361',
                  value = '(2*cw*ee**2*complex(0,1)*I48x55*sw)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_362 = Coupling(name = 'GC_362',
                  value = '(cw*ee*complex(0,1)*I65x44*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_363 = Coupling(name = 'GC_363',
                  value = '(cw*ee*complex(0,1)*I65x55*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_364 = Coupling(name = 'GC_364',
                  value = '(2*cw*ee**2*complex(0,1)*I9x44*sw)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_365 = Coupling(name = 'GC_365',
                  value = '(-2*cw*ee*complex(0,1)*G*I9x44*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':1,'QED':1})

GC_366 = Coupling(name = 'GC_366',
                  value = '(2*cw*ee**2*complex(0,1)*I9x55*sw)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_367 = Coupling(name = 'GC_367',
                  value = '(-2*cw*ee*complex(0,1)*G*I9x55*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':1,'QED':1})

GC_368 = Coupling(name = 'GC_368',
                  value = '(-2*ee**2*complex(0,1)*I106x44*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_369 = Coupling(name = 'GC_369',
                  value = '(-2*ee**2*complex(0,1)*I106x55*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_370 = Coupling(name = 'GC_370',
                  value = '(-8*ee**2*complex(0,1)*I203x44*sw**2)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_371 = Coupling(name = 'GC_371',
                  value = '(-8*ee**2*complex(0,1)*I203x55*sw**2)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_372 = Coupling(name = 'GC_372',
                  value = '(-2*ee**2*complex(0,1)*I65x44*sw**2)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_373 = Coupling(name = 'GC_373',
                  value = '(-2*ee**2*complex(0,1)*I65x55*sw**2)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_374 = Coupling(name = 'GC_374',
                  value = '(ee**2*complex(0,1)*I106x44*I161x33)/(6.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I106x44*I162x33)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_375 = Coupling(name = 'GC_375',
                  value = '(ee**2*complex(0,1)*I106x55*I161x33)/(6.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I106x55*I162x33)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_376 = Coupling(name = 'GC_376',
                  value = '(ee**2*complex(0,1)*I106x44*I161x36)/(6.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I106x44*I162x36)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_377 = Coupling(name = 'GC_377',
                  value = '(ee**2*complex(0,1)*I106x55*I161x36)/(6.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I106x55*I162x36)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_378 = Coupling(name = 'GC_378',
                  value = '(ee**2*complex(0,1)*I105x33*I162x44)/(3.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I106x33*I162x44)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_379 = Coupling(name = 'GC_379',
                  value = '(ee**2*complex(0,1)*I105x36*I162x44)/(3.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I106x36*I162x44)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_380 = Coupling(name = 'GC_380',
                  value = '(ee**2*complex(0,1)*I105x63*I162x44)/(3.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I106x63*I162x44)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_381 = Coupling(name = 'GC_381',
                  value = '(ee**2*complex(0,1)*I105x66*I162x44)/(3.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I106x66*I162x44)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_382 = Coupling(name = 'GC_382',
                  value = '(ee**2*complex(0,1)*I105x33*I162x55)/(3.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I106x33*I162x55)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_383 = Coupling(name = 'GC_383',
                  value = '(ee**2*complex(0,1)*I105x36*I162x55)/(3.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I106x36*I162x55)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_384 = Coupling(name = 'GC_384',
                  value = '(ee**2*complex(0,1)*I105x63*I162x55)/(3.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I106x63*I162x55)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_385 = Coupling(name = 'GC_385',
                  value = '(ee**2*complex(0,1)*I105x66*I162x55)/(3.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I106x66*I162x55)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_386 = Coupling(name = 'GC_386',
                  value = '(ee**2*complex(0,1)*I106x44*I161x63)/(6.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I106x44*I162x63)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_387 = Coupling(name = 'GC_387',
                  value = '(ee**2*complex(0,1)*I106x55*I161x63)/(6.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I106x55*I162x63)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_388 = Coupling(name = 'GC_388',
                  value = '(ee**2*complex(0,1)*I106x44*I161x66)/(6.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I106x44*I162x66)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_389 = Coupling(name = 'GC_389',
                  value = '(ee**2*complex(0,1)*I106x55*I161x66)/(6.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I106x55*I162x66)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_390 = Coupling(name = 'GC_390',
                  value = '-(ee**2*complex(0,1)*I169x11*I172x44)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I173x11*I174x44)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I113x11*I176x44)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I170x11*I177x44)/(36.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_391 = Coupling(name = 'GC_391',
                  value = '-(ee**2*complex(0,1)*I169x22*I172x44)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I173x22*I174x44)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I113x22*I176x44)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I170x22*I177x44)/(36.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_392 = Coupling(name = 'GC_392',
                  value = '-(ee**2*complex(0,1)*I169x11*I172x55)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I173x11*I174x55)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I113x11*I176x55)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I170x11*I177x55)/(36.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_393 = Coupling(name = 'GC_393',
                  value = '-(ee**2*complex(0,1)*I169x22*I172x55)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I173x22*I174x55)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I113x22*I176x55)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I170x22*I177x55)/(36.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_394 = Coupling(name = 'GC_394',
                  value = '-(ee**2*complex(0,1)*I169x33*I172x44)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I173x33*I174x44)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I172x44*I175x33)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I172x33*I175x44)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I113x33*I176x44)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I170x33*I177x44)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I177x44*I178x33)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I177x33*I178x44)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_395 = Coupling(name = 'GC_395',
                  value = '-(ee**2*complex(0,1)*I169x36*I172x44)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I173x36*I174x44)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I172x44*I175x36)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I172x36*I175x44)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I113x36*I176x44)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I170x36*I177x44)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I177x44*I178x36)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I177x36*I178x44)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_396 = Coupling(name = 'GC_396',
                  value = '-(ee**2*complex(0,1)*I169x33*I172x55)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I173x33*I174x55)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I172x55*I175x33)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I172x33*I175x55)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I113x33*I176x55)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I170x33*I177x55)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I177x55*I178x33)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I177x33*I178x55)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_397 = Coupling(name = 'GC_397',
                  value = '-(ee**2*complex(0,1)*I169x36*I172x55)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I173x36*I174x55)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I172x55*I175x36)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I172x36*I175x55)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I113x36*I176x55)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I170x36*I177x55)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I177x55*I178x36)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I177x36*I178x55)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_398 = Coupling(name = 'GC_398',
                  value = '(ee**2*complex(0,1)*I172x55*I175x44)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I172x44*I175x55)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I177x55*I178x44)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I177x44*I178x55)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_399 = Coupling(name = 'GC_399',
                  value = '-(ee**2*complex(0,1)*I169x63*I172x44)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I173x63*I174x44)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I172x63*I175x44)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I172x44*I175x63)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I113x63*I176x44)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I170x63*I177x44)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I177x63*I178x44)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I177x44*I178x63)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_400 = Coupling(name = 'GC_400',
                  value = '-(ee**2*complex(0,1)*I169x63*I172x55)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I173x63*I174x55)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I172x63*I175x55)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I172x55*I175x63)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I113x63*I176x55)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I170x63*I177x55)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I177x63*I178x55)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I177x55*I178x63)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_401 = Coupling(name = 'GC_401',
                  value = '-(ee**2*complex(0,1)*I169x66*I172x44)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I173x66*I174x44)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I172x66*I175x44)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I172x44*I175x66)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I113x66*I176x44)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I170x66*I177x44)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I177x66*I178x44)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I177x44*I178x66)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_402 = Coupling(name = 'GC_402',
                  value = '-(ee**2*complex(0,1)*I169x66*I172x55)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I173x66*I174x55)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I172x66*I175x55)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I172x55*I175x66)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I113x66*I176x55)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I170x66*I177x55)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I177x66*I178x55)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I177x55*I178x66)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_403 = Coupling(name = 'GC_403',
                  value = '(ee**2*complex(0,1)*I30x55*I33x44)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I30x44*I33x55)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I35x55*I36x44)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I35x44*I36x55)/(36.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_404 = Coupling(name = 'GC_404',
                  value = '-(ee**2*complex(0,1)*I162x44*I63x33)/(9.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I162x44*I65x33)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_405 = Coupling(name = 'GC_405',
                  value = '-(ee**2*complex(0,1)*I162x55*I63x33)/(9.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I162x55*I65x33)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_406 = Coupling(name = 'GC_406',
                  value = '-(ee**2*complex(0,1)*I162x44*I63x36)/(9.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I162x44*I65x36)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_407 = Coupling(name = 'GC_407',
                  value = '-(ee**2*complex(0,1)*I162x55*I63x36)/(9.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I162x55*I65x36)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_408 = Coupling(name = 'GC_408',
                  value = '(ee**2*complex(0,1)*I161x33*I65x44)/(18.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I162x33*I65x44)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_409 = Coupling(name = 'GC_409',
                  value = '(ee**2*complex(0,1)*I161x36*I65x44)/(18.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I162x36*I65x44)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_410 = Coupling(name = 'GC_410',
                  value = '(ee**2*complex(0,1)*I161x63*I65x44)/(18.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I162x63*I65x44)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_411 = Coupling(name = 'GC_411',
                  value = '(ee**2*complex(0,1)*I161x66*I65x44)/(18.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I162x66*I65x44)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_412 = Coupling(name = 'GC_412',
                  value = '(ee**2*complex(0,1)*I161x33*I65x55)/(18.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I162x33*I65x55)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_413 = Coupling(name = 'GC_413',
                  value = '(ee**2*complex(0,1)*I161x36*I65x55)/(18.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I162x36*I65x55)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_414 = Coupling(name = 'GC_414',
                  value = '(ee**2*complex(0,1)*I161x63*I65x55)/(18.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I162x63*I65x55)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_415 = Coupling(name = 'GC_415',
                  value = '(ee**2*complex(0,1)*I161x66*I65x55)/(18.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I162x66*I65x55)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_416 = Coupling(name = 'GC_416',
                  value = '-(ee**2*complex(0,1)*I162x44*I63x63)/(9.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I162x44*I65x63)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_417 = Coupling(name = 'GC_417',
                  value = '-(ee**2*complex(0,1)*I162x55*I63x63)/(9.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I162x55*I65x63)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_418 = Coupling(name = 'GC_418',
                  value = '-(ee**2*complex(0,1)*I162x44*I63x66)/(9.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I162x44*I65x66)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_419 = Coupling(name = 'GC_419',
                  value = '-(ee**2*complex(0,1)*I162x55*I63x66)/(9.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I162x55*I65x66)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_420 = Coupling(name = 'GC_420',
                  value = '-(ee**2*complex(0,1)*I64x33*I65x44)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I65x44*I66x33)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_421 = Coupling(name = 'GC_421',
                  value = '-(ee**2*complex(0,1)*I64x33*I65x55)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I65x55*I66x33)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_422 = Coupling(name = 'GC_422',
                  value = '-(ee**2*complex(0,1)*I64x36*I65x44)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I65x44*I66x36)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_423 = Coupling(name = 'GC_423',
                  value = '-(ee**2*complex(0,1)*I64x36*I65x55)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I65x55*I66x36)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_424 = Coupling(name = 'GC_424',
                  value = '(ee**2*complex(0,1)*I63x33*I66x44)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I65x33*I66x44)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_425 = Coupling(name = 'GC_425',
                  value = '(ee**2*complex(0,1)*I63x36*I66x44)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I65x36*I66x44)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_426 = Coupling(name = 'GC_426',
                  value = '(ee**2*complex(0,1)*I63x63*I66x44)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I65x63*I66x44)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_427 = Coupling(name = 'GC_427',
                  value = '(ee**2*complex(0,1)*I63x66*I66x44)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I65x66*I66x44)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_428 = Coupling(name = 'GC_428',
                  value = '(ee**2*complex(0,1)*I63x33*I66x55)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I65x33*I66x55)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_429 = Coupling(name = 'GC_429',
                  value = '(ee**2*complex(0,1)*I63x36*I66x55)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I65x36*I66x55)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_430 = Coupling(name = 'GC_430',
                  value = '(ee**2*complex(0,1)*I63x63*I66x55)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I65x63*I66x55)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_431 = Coupling(name = 'GC_431',
                  value = '(ee**2*complex(0,1)*I63x66*I66x55)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I65x66*I66x55)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_432 = Coupling(name = 'GC_432',
                  value = '-(ee**2*complex(0,1)*I64x63*I65x44)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I65x44*I66x63)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_433 = Coupling(name = 'GC_433',
                  value = '-(ee**2*complex(0,1)*I64x63*I65x55)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I65x55*I66x63)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_434 = Coupling(name = 'GC_434',
                  value = '-(ee**2*complex(0,1)*I64x66*I65x44)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I65x44*I66x66)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_435 = Coupling(name = 'GC_435',
                  value = '-(ee**2*complex(0,1)*I64x66*I65x55)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I65x55*I66x66)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_436 = Coupling(name = 'GC_436',
                  value = '-(ee**2*complex(0,1)*I75x11*I76x44)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I72x11*I77x44)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I47x11*I79x44)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I73x11*I80x44)/(8.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_437 = Coupling(name = 'GC_437',
                  value = '-(ee**2*complex(0,1)*I75x22*I76x44)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I72x22*I77x44)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I47x22*I79x44)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I73x22*I80x44)/(8.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_438 = Coupling(name = 'GC_438',
                  value = '-(ee**2*complex(0,1)*I75x11*I76x55)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I72x11*I77x55)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I47x11*I79x55)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I73x11*I80x55)/(8.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_439 = Coupling(name = 'GC_439',
                  value = '-(ee**2*complex(0,1)*I75x22*I76x55)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I72x22*I77x55)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I47x22*I79x55)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I73x22*I80x55)/(8.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_440 = Coupling(name = 'GC_440',
                  value = '-(ee**2*complex(0,1)*I75x33*I76x44)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I72x33*I77x44)/(8.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I77x44*I78x33)/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I77x33*I78x44)/(4.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I47x33*I79x44)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I73x33*I80x44)/(8.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I80x44*I81x33)/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I80x33*I81x44)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_441 = Coupling(name = 'GC_441',
                  value = '-(ee**2*complex(0,1)*I75x36*I76x44)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I72x36*I77x44)/(8.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I77x44*I78x36)/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I77x36*I78x44)/(4.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I47x36*I79x44)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I73x36*I80x44)/(8.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I80x44*I81x36)/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I80x36*I81x44)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_442 = Coupling(name = 'GC_442',
                  value = '(ee**2*complex(0,1)*I77x44*I78x44)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I80x44*I81x44)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_443 = Coupling(name = 'GC_443',
                  value = '-(ee**2*complex(0,1)*I75x33*I76x55)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I72x33*I77x55)/(8.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I77x55*I78x33)/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I77x33*I78x55)/(4.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I47x33*I79x55)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I73x33*I80x55)/(8.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I80x55*I81x33)/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I80x33*I81x55)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_444 = Coupling(name = 'GC_444',
                  value = '-(ee**2*complex(0,1)*I75x36*I76x55)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I72x36*I77x55)/(8.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I77x55*I78x36)/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I77x36*I78x55)/(4.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I47x36*I79x55)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I73x36*I80x55)/(8.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I80x55*I81x36)/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I80x36*I81x55)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_445 = Coupling(name = 'GC_445',
                  value = '(ee**2*complex(0,1)*I77x55*I78x44)/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I77x44*I78x55)/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I80x55*I81x44)/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I80x44*I81x55)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_446 = Coupling(name = 'GC_446',
                  value = '(ee**2*complex(0,1)*I77x55*I78x55)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I80x55*I81x55)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_447 = Coupling(name = 'GC_447',
                  value = '-(ee**2*complex(0,1)*I75x63*I76x44)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I72x63*I77x44)/(8.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I77x63*I78x44)/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I77x44*I78x63)/(4.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I47x63*I79x44)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I73x63*I80x44)/(8.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I80x63*I81x44)/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I80x44*I81x63)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_448 = Coupling(name = 'GC_448',
                  value = '-(ee**2*complex(0,1)*I75x63*I76x55)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I72x63*I77x55)/(8.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I77x63*I78x55)/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I77x55*I78x63)/(4.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I47x63*I79x55)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I73x63*I80x55)/(8.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I80x63*I81x55)/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I80x55*I81x63)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_449 = Coupling(name = 'GC_449',
                  value = '-(ee**2*complex(0,1)*I75x66*I76x44)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I72x66*I77x44)/(8.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I77x66*I78x44)/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I77x44*I78x66)/(4.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I47x66*I79x44)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I73x66*I80x44)/(8.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I80x66*I81x44)/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I80x44*I81x66)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_450 = Coupling(name = 'GC_450',
                  value = '-(ee**2*complex(0,1)*I75x66*I76x55)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I72x66*I77x55)/(8.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I77x66*I78x55)/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I77x55*I78x66)/(4.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I47x66*I79x55)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I73x66*I80x55)/(8.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I80x66*I81x55)/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I80x55*I81x66)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_451 = Coupling(name = 'GC_451',
                  value = '(ee**2*complex(0,1)*I27x11*I30x44)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I31x11*I32x44)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I28x11*I35x44)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I34x44*I8x11)/(72.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_452 = Coupling(name = 'GC_452',
                  value = '(ee**2*complex(0,1)*I27x11*I30x55)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I31x11*I32x55)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I28x11*I35x55)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I34x55*I8x11)/(72.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_453 = Coupling(name = 'GC_453',
                  value = '(ee**2*complex(0,1)*I27x22*I30x44)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I31x22*I32x44)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I28x22*I35x44)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I34x44*I8x22)/(72.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_454 = Coupling(name = 'GC_454',
                  value = '(ee**2*complex(0,1)*I27x22*I30x55)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I31x22*I32x55)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I28x22*I35x55)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I34x55*I8x22)/(72.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_455 = Coupling(name = 'GC_455',
                  value = '(ee**2*complex(0,1)*I27x33*I30x44)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I31x33*I32x44)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I30x44*I33x33)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I30x33*I33x44)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I28x33*I35x44)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I35x44*I36x33)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I35x33*I36x44)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I34x44*I8x33)/(72.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_456 = Coupling(name = 'GC_456',
                  value = '(ee**2*complex(0,1)*I27x33*I30x55)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I31x33*I32x55)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I30x55*I33x33)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I30x33*I33x55)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I28x33*I35x55)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I35x55*I36x33)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I35x33*I36x55)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I34x55*I8x33)/(72.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_457 = Coupling(name = 'GC_457',
                  value = '(ee**2*complex(0,1)*I27x36*I30x44)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I31x36*I32x44)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I30x44*I33x36)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I30x36*I33x44)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I28x36*I35x44)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I35x44*I36x36)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I35x36*I36x44)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I34x44*I8x36)/(72.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_458 = Coupling(name = 'GC_458',
                  value = '(ee**2*complex(0,1)*I27x36*I30x55)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I31x36*I32x55)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I30x55*I33x36)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I30x36*I33x55)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I28x36*I35x55)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I35x55*I36x36)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I35x36*I36x55)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I34x55*I8x36)/(72.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_459 = Coupling(name = 'GC_459',
                  value = '(ee**2*complex(0,1)*I27x63*I30x44)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I31x63*I32x44)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I30x63*I33x44)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I30x44*I33x63)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I28x63*I35x44)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I35x63*I36x44)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I35x44*I36x63)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I34x44*I8x63)/(72.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_460 = Coupling(name = 'GC_460',
                  value = '(ee**2*complex(0,1)*I27x63*I30x55)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I31x63*I32x55)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I30x63*I33x55)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I30x55*I33x63)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I28x63*I35x55)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I35x63*I36x55)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I35x55*I36x63)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I34x55*I8x63)/(72.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_461 = Coupling(name = 'GC_461',
                  value = '(ee**2*complex(0,1)*I27x66*I30x44)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I31x66*I32x44)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I30x66*I33x44)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I30x44*I33x66)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I28x66*I35x44)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I35x66*I36x44)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I35x44*I36x66)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I34x44*I8x66)/(72.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_462 = Coupling(name = 'GC_462',
                  value = '(ee**2*complex(0,1)*I27x66*I30x55)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I31x66*I32x55)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I30x66*I33x55)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I30x55*I33x66)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I28x66*I35x55)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I35x66*I36x55)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I35x55*I36x66)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I34x55*I8x66)/(72.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_463 = Coupling(name = 'GC_463',
                  value = '(ee**2*complex(0,1)*I105x11)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I105x11)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_464 = Coupling(name = 'GC_464',
                  value = '(ee**2*complex(0,1)*I105x22)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I105x22)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_465 = Coupling(name = 'GC_465',
                  value = '(ee**2*complex(0,1)*I105x33)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I106x33)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I105x33)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_466 = Coupling(name = 'GC_466',
                  value = '(ee**2*complex(0,1)*I105x36)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I106x36)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I105x36)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_467 = Coupling(name = 'GC_467',
                  value = '(ee**2*complex(0,1)*I105x63)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I106x63)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I105x63)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_468 = Coupling(name = 'GC_468',
                  value = '(ee**2*complex(0,1)*I105x66)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I106x66)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I105x66)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_469 = Coupling(name = 'GC_469',
                  value = '(ee**2*complex(0,1)*I105x11)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I107x11*I108x11)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I105x11)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I107x11*I108x11)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_470 = Coupling(name = 'GC_470',
                  value = '-(ee**2*complex(0,1)*I107x22*I108x11)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I107x22*I108x11)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_471 = Coupling(name = 'GC_471',
                  value = '-(ee**2*complex(0,1)*I107x33*I108x11)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I107x33*I108x11)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_472 = Coupling(name = 'GC_472',
                  value = '-(ee**2*complex(0,1)*I107x36*I108x11)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I107x36*I108x11)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_473 = Coupling(name = 'GC_473',
                  value = '-(ee**2*complex(0,1)*I107x11*I108x22)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I107x11*I108x22)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_474 = Coupling(name = 'GC_474',
                  value = '(ee**2*complex(0,1)*I105x22)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I107x22*I108x22)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I105x22)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I107x22*I108x22)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_475 = Coupling(name = 'GC_475',
                  value = '-(ee**2*complex(0,1)*I107x33*I108x22)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I107x33*I108x22)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_476 = Coupling(name = 'GC_476',
                  value = '-(ee**2*complex(0,1)*I107x36*I108x22)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I107x36*I108x22)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_477 = Coupling(name = 'GC_477',
                  value = '-(ee**2*complex(0,1)*I107x11*I108x33)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I107x11*I108x33)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_478 = Coupling(name = 'GC_478',
                  value = '-(ee**2*complex(0,1)*I107x22*I108x33)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I107x22*I108x33)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_479 = Coupling(name = 'GC_479',
                  value = '-(ee**2*complex(0,1)*I107x11*I108x36)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I107x11*I108x36)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_480 = Coupling(name = 'GC_480',
                  value = '-(ee**2*complex(0,1)*I107x22*I108x36)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I107x22*I108x36)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_481 = Coupling(name = 'GC_481',
                  value = '-(ee**2*complex(0,1)*I148x11)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I148x11)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_482 = Coupling(name = 'GC_482',
                  value = '-(ee**2*complex(0,1)*I148x22)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I148x22)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_483 = Coupling(name = 'GC_483',
                  value = '-(ee**2*complex(0,1)*I148x33)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I149x33)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I148x33)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_484 = Coupling(name = 'GC_484',
                  value = '-(ee**2*complex(0,1)*I148x36)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I149x36)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I148x36)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_485 = Coupling(name = 'GC_485',
                  value = '-(ee**2*complex(0,1)*I148x63)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I149x63)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I148x63)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_486 = Coupling(name = 'GC_486',
                  value = '-(ee**2*complex(0,1)*I148x66)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I149x66)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I148x66)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_487 = Coupling(name = 'GC_487',
                  value = '(ee**2*complex(0,1)*I105x11*I161x11)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I105x11*I161x11)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_488 = Coupling(name = 'GC_488',
                  value = '(ee**2*complex(0,1)*I105x22*I161x11)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I105x22*I161x11)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_489 = Coupling(name = 'GC_489',
                  value = '(ee**2*complex(0,1)*I105x33*I161x11)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I106x33*I161x11)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I105x33*I161x11)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_490 = Coupling(name = 'GC_490',
                  value = '(ee**2*complex(0,1)*I105x36*I161x11)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I106x36*I161x11)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I105x36*I161x11)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_491 = Coupling(name = 'GC_491',
                  value = '(ee**2*complex(0,1)*I105x63*I161x11)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I106x63*I161x11)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I105x63*I161x11)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_492 = Coupling(name = 'GC_492',
                  value = '(ee**2*complex(0,1)*I105x66*I161x11)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I106x66*I161x11)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I105x66*I161x11)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_493 = Coupling(name = 'GC_493',
                  value = '(ee**2*complex(0,1)*I105x11*I161x22)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I105x11*I161x22)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_494 = Coupling(name = 'GC_494',
                  value = '(ee**2*complex(0,1)*I105x22*I161x22)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I105x22*I161x22)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_495 = Coupling(name = 'GC_495',
                  value = '(ee**2*complex(0,1)*I105x33*I161x22)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I106x33*I161x22)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I105x33*I161x22)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_496 = Coupling(name = 'GC_496',
                  value = '(ee**2*complex(0,1)*I105x36*I161x22)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I106x36*I161x22)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I105x36*I161x22)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_497 = Coupling(name = 'GC_497',
                  value = '(ee**2*complex(0,1)*I105x63*I161x22)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I106x63*I161x22)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I105x63*I161x22)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_498 = Coupling(name = 'GC_498',
                  value = '(ee**2*complex(0,1)*I105x66*I161x22)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I106x66*I161x22)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I105x66*I161x22)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_499 = Coupling(name = 'GC_499',
                  value = '(ee**2*complex(0,1)*I105x11*I161x33)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I105x11*I162x33)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I105x11*I161x33)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_500 = Coupling(name = 'GC_500',
                  value = '(ee**2*complex(0,1)*I105x22*I161x33)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I105x22*I162x33)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I105x22*I161x33)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_501 = Coupling(name = 'GC_501',
                  value = '(ee**2*complex(0,1)*I105x33*I161x33)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I106x33*I161x33)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I105x33*I162x33)/(3.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I106x33*I162x33)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I105x33*I161x33)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_502 = Coupling(name = 'GC_502',
                  value = '(ee**2*complex(0,1)*I105x36*I161x33)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I106x36*I161x33)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I105x36*I162x33)/(3.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I106x36*I162x33)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I105x36*I161x33)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_503 = Coupling(name = 'GC_503',
                  value = '(ee**2*complex(0,1)*I105x63*I161x33)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I106x63*I161x33)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I105x63*I162x33)/(3.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I106x63*I162x33)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I105x63*I161x33)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_504 = Coupling(name = 'GC_504',
                  value = '(ee**2*complex(0,1)*I105x66*I161x33)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I106x66*I161x33)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I105x66*I162x33)/(3.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I106x66*I162x33)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I105x66*I161x33)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_505 = Coupling(name = 'GC_505',
                  value = '(ee**2*complex(0,1)*I105x11*I161x36)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I105x11*I162x36)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I105x11*I161x36)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_506 = Coupling(name = 'GC_506',
                  value = '(ee**2*complex(0,1)*I105x22*I161x36)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I105x22*I162x36)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I105x22*I161x36)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_507 = Coupling(name = 'GC_507',
                  value = '(ee**2*complex(0,1)*I105x33*I161x36)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I106x33*I161x36)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I105x33*I162x36)/(3.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I106x33*I162x36)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I105x33*I161x36)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_508 = Coupling(name = 'GC_508',
                  value = '(ee**2*complex(0,1)*I105x36*I161x36)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I106x36*I161x36)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I105x36*I162x36)/(3.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I106x36*I162x36)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I105x36*I161x36)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_509 = Coupling(name = 'GC_509',
                  value = '(ee**2*complex(0,1)*I105x63*I161x36)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I106x63*I161x36)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I105x63*I162x36)/(3.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I106x63*I162x36)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I105x63*I161x36)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_510 = Coupling(name = 'GC_510',
                  value = '(ee**2*complex(0,1)*I105x66*I161x36)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I106x66*I161x36)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I105x66*I162x36)/(3.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I106x66*I162x36)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I105x66*I161x36)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_511 = Coupling(name = 'GC_511',
                  value = '(ee**2*complex(0,1)*I105x11*I161x63)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I105x11*I162x63)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I105x11*I161x63)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_512 = Coupling(name = 'GC_512',
                  value = '(ee**2*complex(0,1)*I105x22*I161x63)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I105x22*I162x63)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I105x22*I161x63)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_513 = Coupling(name = 'GC_513',
                  value = '(ee**2*complex(0,1)*I105x33*I161x63)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I106x33*I161x63)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I105x33*I162x63)/(3.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I106x33*I162x63)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I105x33*I161x63)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_514 = Coupling(name = 'GC_514',
                  value = '(ee**2*complex(0,1)*I105x36*I161x63)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I106x36*I161x63)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I105x36*I162x63)/(3.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I106x36*I162x63)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I105x36*I161x63)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_515 = Coupling(name = 'GC_515',
                  value = '(ee**2*complex(0,1)*I105x63*I161x63)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I106x63*I161x63)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I105x63*I162x63)/(3.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I106x63*I162x63)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I105x63*I161x63)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_516 = Coupling(name = 'GC_516',
                  value = '(ee**2*complex(0,1)*I105x66*I161x63)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I106x66*I161x63)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I105x66*I162x63)/(3.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I106x66*I162x63)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I105x66*I161x63)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_517 = Coupling(name = 'GC_517',
                  value = '(ee**2*complex(0,1)*I105x11*I161x66)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I105x11*I162x66)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I105x11*I161x66)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_518 = Coupling(name = 'GC_518',
                  value = '(ee**2*complex(0,1)*I105x22*I161x66)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I105x22*I162x66)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I105x22*I161x66)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_519 = Coupling(name = 'GC_519',
                  value = '(ee**2*complex(0,1)*I105x33*I161x66)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I106x33*I161x66)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I105x33*I162x66)/(3.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I106x33*I162x66)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I105x33*I161x66)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_520 = Coupling(name = 'GC_520',
                  value = '(ee**2*complex(0,1)*I105x36*I161x66)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I106x36*I161x66)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I105x36*I162x66)/(3.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I106x36*I162x66)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I105x36*I161x66)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_521 = Coupling(name = 'GC_521',
                  value = '(ee**2*complex(0,1)*I105x63*I161x66)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I106x63*I161x66)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I105x63*I162x66)/(3.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I106x63*I162x66)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I105x63*I161x66)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_522 = Coupling(name = 'GC_522',
                  value = '(ee**2*complex(0,1)*I105x66*I161x66)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I106x66*I161x66)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I105x66*I162x66)/(3.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I106x66*I162x66)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I105x66*I161x66)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_523 = Coupling(name = 'GC_523',
                  value = '-(ee**2*complex(0,1)*I159x11*I163x11)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I159x11*I163x11)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_524 = Coupling(name = 'GC_524',
                  value = '-(ee**2*complex(0,1)*I159x22*I163x11)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I159x22*I163x11)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_525 = Coupling(name = 'GC_525',
                  value = '-(ee**2*complex(0,1)*I159x33*I163x11)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I159x33*I163x11)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_526 = Coupling(name = 'GC_526',
                  value = '-(ee**2*complex(0,1)*I159x36*I163x11)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I159x36*I163x11)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_527 = Coupling(name = 'GC_527',
                  value = '-(ee**2*complex(0,1)*I159x63*I163x11)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I159x63*I163x11)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_528 = Coupling(name = 'GC_528',
                  value = '-(ee**2*complex(0,1)*I159x66*I163x11)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I159x66*I163x11)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_529 = Coupling(name = 'GC_529',
                  value = '-(ee**2*complex(0,1)*I159x11*I163x22)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I159x11*I163x22)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_530 = Coupling(name = 'GC_530',
                  value = '-(ee**2*complex(0,1)*I159x22*I163x22)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I159x22*I163x22)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_531 = Coupling(name = 'GC_531',
                  value = '-(ee**2*complex(0,1)*I159x33*I163x22)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I159x33*I163x22)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_532 = Coupling(name = 'GC_532',
                  value = '-(ee**2*complex(0,1)*I159x36*I163x22)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I159x36*I163x22)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_533 = Coupling(name = 'GC_533',
                  value = '-(ee**2*complex(0,1)*I159x63*I163x22)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I159x63*I163x22)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_534 = Coupling(name = 'GC_534',
                  value = '-(ee**2*complex(0,1)*I159x66*I163x22)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I159x66*I163x22)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_535 = Coupling(name = 'GC_535',
                  value = '-(ee**2*complex(0,1)*I159x11*I163x33)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I159x11*I163x33)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_536 = Coupling(name = 'GC_536',
                  value = '-(ee**2*complex(0,1)*I159x22*I163x33)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I159x22*I163x33)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_537 = Coupling(name = 'GC_537',
                  value = '-(ee**2*complex(0,1)*I159x11*I163x36)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I159x11*I163x36)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_538 = Coupling(name = 'GC_538',
                  value = '-(ee**2*complex(0,1)*I159x22*I163x36)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I159x22*I163x36)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_539 = Coupling(name = 'GC_539',
                  value = '-(ee**2*complex(0,1)*I159x11*I163x63)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I159x11*I163x63)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_540 = Coupling(name = 'GC_540',
                  value = '-(ee**2*complex(0,1)*I159x22*I163x63)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I159x22*I163x63)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_541 = Coupling(name = 'GC_541',
                  value = '-(ee**2*complex(0,1)*I159x11*I163x66)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I159x11*I163x66)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_542 = Coupling(name = 'GC_542',
                  value = '-(ee**2*complex(0,1)*I159x22*I163x66)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I159x22*I163x66)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_543 = Coupling(name = 'GC_543',
                  value = '(-2*ee**2*complex(0,1)*I168x11*I169x11)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I168x11*I169x11)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_544 = Coupling(name = 'GC_544',
                  value = '(-2*ee**2*complex(0,1)*I168x22*I169x22)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I168x22*I169x22)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_545 = Coupling(name = 'GC_545',
                  value = '(-2*ee**2*complex(0,1)*I170x11*I171x11)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I170x11*I171x11)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_546 = Coupling(name = 'GC_546',
                  value = '-(ee**2*complex(0,1)*I168x22*I169x11)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I168x11*I169x22)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I170x22*I171x11)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I170x11*I171x22)/(18.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I168x22*I169x11)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I168x11*I169x22)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I170x22*I171x11)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I170x11*I171x22)/(16.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_547 = Coupling(name = 'GC_547',
                  value = '(-2*ee**2*complex(0,1)*I170x22*I171x22)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I170x22*I171x22)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_548 = Coupling(name = 'GC_548',
                  value = '-(ee**2*complex(0,1)*I168x33*I169x11)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I168x11*I169x33)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I170x33*I171x11)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I170x11*I171x33)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I169x11*I172x33)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I173x11*I174x33)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I113x11*I176x33)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I170x11*I177x33)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I168x33*I169x11)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I168x11*I169x33)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I170x33*I171x11)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I170x11*I171x33)/(16.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_549 = Coupling(name = 'GC_549',
                  value = '-(ee**2*complex(0,1)*I168x33*I169x22)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I168x22*I169x33)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I170x33*I171x22)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I170x22*I171x33)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I169x22*I172x33)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I173x22*I174x33)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I113x22*I176x33)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I170x22*I177x33)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I168x33*I169x22)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I168x22*I169x33)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I170x33*I171x22)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I170x22*I171x33)/(16.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_550 = Coupling(name = 'GC_550',
                  value = '-(ee**2*complex(0,1)*I168x36*I169x11)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I168x11*I169x36)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I170x36*I171x11)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I170x11*I171x36)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I169x11*I172x36)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I173x11*I174x36)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I113x11*I176x36)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I170x11*I177x36)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I168x36*I169x11)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I168x11*I169x36)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I170x36*I171x11)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I170x11*I171x36)/(16.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_551 = Coupling(name = 'GC_551',
                  value = '-(ee**2*complex(0,1)*I168x36*I169x22)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I168x22*I169x36)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I170x36*I171x22)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I170x22*I171x36)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I169x22*I172x36)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I173x22*I174x36)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I113x22*I176x36)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I170x22*I177x36)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I168x36*I169x22)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I168x22*I169x36)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I170x36*I171x22)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I170x22*I171x36)/(16.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_552 = Coupling(name = 'GC_552',
                  value = '-(ee**2*complex(0,1)*I168x63*I169x11)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I168x11*I169x63)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I170x63*I171x11)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I170x11*I171x63)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I169x11*I172x63)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I173x11*I174x63)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I113x11*I176x63)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I170x11*I177x63)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I168x63*I169x11)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I168x11*I169x63)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I170x63*I171x11)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I170x11*I171x63)/(16.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_553 = Coupling(name = 'GC_553',
                  value = '-(ee**2*complex(0,1)*I168x63*I169x22)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I168x22*I169x63)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I170x63*I171x22)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I170x22*I171x63)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I169x22*I172x63)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I173x22*I174x63)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I113x22*I176x63)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I170x22*I177x63)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I168x63*I169x22)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I168x22*I169x63)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I170x63*I171x22)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I170x22*I171x63)/(16.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_554 = Coupling(name = 'GC_554',
                  value = '-(ee**2*complex(0,1)*I168x66*I169x11)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I168x11*I169x66)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I170x66*I171x11)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I170x11*I171x66)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I169x11*I172x66)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I173x11*I174x66)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I113x11*I176x66)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I170x11*I177x66)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I168x66*I169x11)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I168x11*I169x66)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I170x66*I171x11)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I170x11*I171x66)/(16.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_555 = Coupling(name = 'GC_555',
                  value = '-(ee**2*complex(0,1)*I168x66*I169x22)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I168x22*I169x66)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I170x66*I171x22)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I170x22*I171x66)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I169x22*I172x66)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I173x22*I174x66)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I113x22*I176x66)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I170x22*I177x66)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I168x66*I169x22)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I168x22*I169x66)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I170x66*I171x22)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I170x22*I171x66)/(16.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_556 = Coupling(name = 'GC_556',
                  value = '(-2*ee**2*complex(0,1)*I26x11*I27x11)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I26x11*I27x11)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_557 = Coupling(name = 'GC_557',
                  value = '(-2*ee**2*complex(0,1)*I26x22*I27x22)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I26x22*I27x22)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_558 = Coupling(name = 'GC_558',
                  value = '(-2*ee**2*complex(0,1)*I28x11*I29x11)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I28x11*I29x11)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_559 = Coupling(name = 'GC_559',
                  value = '-(ee**2*complex(0,1)*I26x22*I27x11)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I26x11*I27x22)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I28x22*I29x11)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I28x11*I29x22)/(18.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I26x22*I27x11)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I26x11*I27x22)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I28x22*I29x11)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I28x11*I29x22)/(16.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_560 = Coupling(name = 'GC_560',
                  value = '(-2*ee**2*complex(0,1)*I28x22*I29x22)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I28x22*I29x22)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_561 = Coupling(name = 'GC_561',
                  value = '-(ee**2*complex(0,1)*I26x33*I27x11)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I26x11*I27x33)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I28x33*I29x11)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I28x11*I29x33)/(18.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I27x11*I30x33)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I31x11*I32x33)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I28x11*I35x33)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I34x33*I8x11)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I26x33*I27x11)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I26x11*I27x33)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I28x33*I29x11)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I28x11*I29x33)/(16.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_562 = Coupling(name = 'GC_562',
                  value = '-(ee**2*complex(0,1)*I26x33*I27x22)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I26x22*I27x33)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I28x33*I29x22)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I28x22*I29x33)/(18.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I27x22*I30x33)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I31x22*I32x33)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I28x22*I35x33)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I34x33*I8x22)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I26x33*I27x22)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I26x22*I27x33)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I28x33*I29x22)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I28x22*I29x33)/(16.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_563 = Coupling(name = 'GC_563',
                  value = '-(ee**2*complex(0,1)*I26x36*I27x11)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I26x11*I27x36)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I28x36*I29x11)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I28x11*I29x36)/(18.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I27x11*I30x36)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I31x11*I32x36)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I28x11*I35x36)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I34x36*I8x11)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I26x36*I27x11)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I26x11*I27x36)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I28x36*I29x11)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I28x11*I29x36)/(16.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_564 = Coupling(name = 'GC_564',
                  value = '-(ee**2*complex(0,1)*I26x36*I27x22)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I26x22*I27x36)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I28x36*I29x22)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I28x22*I29x36)/(18.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I27x22*I30x36)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I31x22*I32x36)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I28x22*I35x36)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I34x36*I8x22)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I26x36*I27x22)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I26x22*I27x36)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I28x36*I29x22)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I28x22*I29x36)/(16.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_565 = Coupling(name = 'GC_565',
                  value = '-(ee**2*complex(0,1)*I26x63*I27x11)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I26x11*I27x63)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I28x63*I29x11)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I28x11*I29x63)/(18.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I27x11*I30x63)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I31x11*I32x63)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I28x11*I35x63)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I34x63*I8x11)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I26x63*I27x11)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I26x11*I27x63)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I28x63*I29x11)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I28x11*I29x63)/(16.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_566 = Coupling(name = 'GC_566',
                  value = '-(ee**2*complex(0,1)*I26x63*I27x22)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I26x22*I27x63)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I28x63*I29x22)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I28x22*I29x63)/(18.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I27x22*I30x63)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I31x22*I32x63)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I28x22*I35x63)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I34x63*I8x22)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I26x63*I27x22)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I26x22*I27x63)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I28x63*I29x22)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I28x22*I29x63)/(16.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_567 = Coupling(name = 'GC_567',
                  value = '-(ee**2*complex(0,1)*I26x66*I27x11)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I26x11*I27x66)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I28x66*I29x11)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I28x11*I29x66)/(18.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I27x11*I30x66)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I31x11*I32x66)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I28x11*I35x66)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I34x66*I8x11)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I26x66*I27x11)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I26x11*I27x66)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I28x66*I29x11)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I28x11*I29x66)/(16.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_568 = Coupling(name = 'GC_568',
                  value = '-(ee**2*complex(0,1)*I26x66*I27x22)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I26x22*I27x66)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I28x66*I29x22)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I28x22*I29x66)/(18.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I27x22*I30x66)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I31x22*I32x66)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I28x22*I35x66)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I34x66*I8x22)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I26x66*I27x22)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I26x22*I27x66)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I28x66*I29x22)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I28x22*I29x66)/(16.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_569 = Coupling(name = 'GC_569',
                  value = '(ee**2*complex(0,1)*I63x11)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I63x11)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_570 = Coupling(name = 'GC_570',
                  value = '(5*ee**2*complex(0,1)*I161x11*I63x11)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I161x11*I63x11)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_571 = Coupling(name = 'GC_571',
                  value = '(5*ee**2*complex(0,1)*I161x22*I63x11)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I161x22*I63x11)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_572 = Coupling(name = 'GC_572',
                  value = '(5*ee**2*complex(0,1)*I161x33*I63x11)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I162x33*I63x11)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I161x33*I63x11)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_573 = Coupling(name = 'GC_573',
                  value = '(5*ee**2*complex(0,1)*I161x36*I63x11)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I162x36*I63x11)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I161x36*I63x11)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_574 = Coupling(name = 'GC_574',
                  value = '(5*ee**2*complex(0,1)*I161x63*I63x11)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I162x63*I63x11)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I161x63*I63x11)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_575 = Coupling(name = 'GC_575',
                  value = '(5*ee**2*complex(0,1)*I161x66*I63x11)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I162x66*I63x11)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I161x66*I63x11)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_576 = Coupling(name = 'GC_576',
                  value = '(ee**2*complex(0,1)*I63x22)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I63x22)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_577 = Coupling(name = 'GC_577',
                  value = '(5*ee**2*complex(0,1)*I161x11*I63x22)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I161x11*I63x22)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_578 = Coupling(name = 'GC_578',
                  value = '(5*ee**2*complex(0,1)*I161x22*I63x22)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I161x22*I63x22)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_579 = Coupling(name = 'GC_579',
                  value = '(5*ee**2*complex(0,1)*I161x33*I63x22)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I162x33*I63x22)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I161x33*I63x22)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_580 = Coupling(name = 'GC_580',
                  value = '(5*ee**2*complex(0,1)*I161x36*I63x22)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I162x36*I63x22)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I161x36*I63x22)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_581 = Coupling(name = 'GC_581',
                  value = '(5*ee**2*complex(0,1)*I161x63*I63x22)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I162x63*I63x22)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I161x63*I63x22)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_582 = Coupling(name = 'GC_582',
                  value = '(5*ee**2*complex(0,1)*I161x66*I63x22)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I162x66*I63x22)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I161x66*I63x22)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_583 = Coupling(name = 'GC_583',
                  value = '(ee**2*complex(0,1)*I63x33)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I65x33)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I63x33)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_584 = Coupling(name = 'GC_584',
                  value = '(5*ee**2*complex(0,1)*I161x11*I63x33)/(18.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I161x11*I65x33)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I161x11*I63x33)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_585 = Coupling(name = 'GC_585',
                  value = '(5*ee**2*complex(0,1)*I161x22*I63x33)/(18.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I161x22*I65x33)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I161x22*I63x33)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_586 = Coupling(name = 'GC_586',
                  value = '(5*ee**2*complex(0,1)*I161x33*I63x33)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I162x33*I63x33)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I161x33*I65x33)/(18.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I162x33*I65x33)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I161x33*I63x33)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_587 = Coupling(name = 'GC_587',
                  value = '(5*ee**2*complex(0,1)*I161x36*I63x33)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I162x36*I63x33)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I161x36*I65x33)/(18.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I162x36*I65x33)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I161x36*I63x33)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_588 = Coupling(name = 'GC_588',
                  value = '(5*ee**2*complex(0,1)*I161x63*I63x33)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I162x63*I63x33)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I161x63*I65x33)/(18.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I162x63*I65x33)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I161x63*I63x33)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_589 = Coupling(name = 'GC_589',
                  value = '(5*ee**2*complex(0,1)*I161x66*I63x33)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I162x66*I63x33)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I161x66*I65x33)/(18.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I162x66*I65x33)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I161x66*I63x33)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_590 = Coupling(name = 'GC_590',
                  value = '(ee**2*complex(0,1)*I63x36)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I65x36)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I63x36)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_591 = Coupling(name = 'GC_591',
                  value = '(5*ee**2*complex(0,1)*I161x11*I63x36)/(18.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I161x11*I65x36)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I161x11*I63x36)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_592 = Coupling(name = 'GC_592',
                  value = '(5*ee**2*complex(0,1)*I161x22*I63x36)/(18.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I161x22*I65x36)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I161x22*I63x36)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_593 = Coupling(name = 'GC_593',
                  value = '(5*ee**2*complex(0,1)*I161x33*I63x36)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I162x33*I63x36)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I161x33*I65x36)/(18.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I162x33*I65x36)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I161x33*I63x36)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_594 = Coupling(name = 'GC_594',
                  value = '(5*ee**2*complex(0,1)*I161x36*I63x36)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I162x36*I63x36)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I161x36*I65x36)/(18.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I162x36*I65x36)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I161x36*I63x36)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_595 = Coupling(name = 'GC_595',
                  value = '(5*ee**2*complex(0,1)*I161x63*I63x36)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I162x63*I63x36)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I161x63*I65x36)/(18.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I162x63*I65x36)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I161x63*I63x36)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_596 = Coupling(name = 'GC_596',
                  value = '(5*ee**2*complex(0,1)*I161x66*I63x36)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I162x66*I63x36)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I161x66*I65x36)/(18.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I162x66*I65x36)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I161x66*I63x36)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_597 = Coupling(name = 'GC_597',
                  value = '(ee**2*complex(0,1)*I63x63)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I65x63)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I63x63)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_598 = Coupling(name = 'GC_598',
                  value = '(5*ee**2*complex(0,1)*I161x11*I63x63)/(18.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I161x11*I65x63)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I161x11*I63x63)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_599 = Coupling(name = 'GC_599',
                  value = '(5*ee**2*complex(0,1)*I161x22*I63x63)/(18.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I161x22*I65x63)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I161x22*I63x63)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_600 = Coupling(name = 'GC_600',
                  value = '(5*ee**2*complex(0,1)*I161x33*I63x63)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I162x33*I63x63)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I161x33*I65x63)/(18.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I162x33*I65x63)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I161x33*I63x63)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_601 = Coupling(name = 'GC_601',
                  value = '(5*ee**2*complex(0,1)*I161x36*I63x63)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I162x36*I63x63)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I161x36*I65x63)/(18.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I162x36*I65x63)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I161x36*I63x63)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_602 = Coupling(name = 'GC_602',
                  value = '(5*ee**2*complex(0,1)*I161x63*I63x63)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I162x63*I63x63)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I161x63*I65x63)/(18.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I162x63*I65x63)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I161x63*I63x63)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_603 = Coupling(name = 'GC_603',
                  value = '(5*ee**2*complex(0,1)*I161x66*I63x63)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I162x66*I63x63)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I161x66*I65x63)/(18.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I162x66*I65x63)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I161x66*I63x63)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_604 = Coupling(name = 'GC_604',
                  value = '(ee**2*complex(0,1)*I63x66)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I65x66)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I63x66)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_605 = Coupling(name = 'GC_605',
                  value = '(5*ee**2*complex(0,1)*I161x11*I63x66)/(18.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I161x11*I65x66)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I161x11*I63x66)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_606 = Coupling(name = 'GC_606',
                  value = '(5*ee**2*complex(0,1)*I161x22*I63x66)/(18.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I161x22*I65x66)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I161x22*I63x66)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_607 = Coupling(name = 'GC_607',
                  value = '(5*ee**2*complex(0,1)*I161x33*I63x66)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I162x33*I63x66)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I161x33*I65x66)/(18.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I162x33*I65x66)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I161x33*I63x66)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_608 = Coupling(name = 'GC_608',
                  value = '(5*ee**2*complex(0,1)*I161x36*I63x66)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I162x36*I63x66)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I161x36*I65x66)/(18.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I162x36*I65x66)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I161x36*I63x66)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_609 = Coupling(name = 'GC_609',
                  value = '(5*ee**2*complex(0,1)*I161x63*I63x66)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I162x63*I63x66)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I161x63*I65x66)/(18.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I162x63*I65x66)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I161x63*I63x66)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_610 = Coupling(name = 'GC_610',
                  value = '(5*ee**2*complex(0,1)*I161x66*I63x66)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I162x66*I63x66)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I161x66*I65x66)/(18.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I162x66*I65x66)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I161x66*I63x66)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_611 = Coupling(name = 'GC_611',
                  value = '-(ee**2*complex(0,1)*I63x11*I64x11)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I63x11*I64x11)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_612 = Coupling(name = 'GC_612',
                  value = '-(ee**2*complex(0,1)*I63x22*I64x11)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I63x22*I64x11)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_613 = Coupling(name = 'GC_613',
                  value = '-(ee**2*complex(0,1)*I63x33*I64x11)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I64x11*I65x33)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I63x33*I64x11)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_614 = Coupling(name = 'GC_614',
                  value = '-(ee**2*complex(0,1)*I63x36*I64x11)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I64x11*I65x36)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I63x36*I64x11)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_615 = Coupling(name = 'GC_615',
                  value = '-(ee**2*complex(0,1)*I63x63*I64x11)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I64x11*I65x63)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I63x63*I64x11)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_616 = Coupling(name = 'GC_616',
                  value = '-(ee**2*complex(0,1)*I63x66*I64x11)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I64x11*I65x66)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I63x66*I64x11)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_617 = Coupling(name = 'GC_617',
                  value = '-(ee**2*complex(0,1)*I63x11*I64x22)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I63x11*I64x22)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_618 = Coupling(name = 'GC_618',
                  value = '-(ee**2*complex(0,1)*I63x22*I64x22)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I63x22*I64x22)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_619 = Coupling(name = 'GC_619',
                  value = '-(ee**2*complex(0,1)*I63x33*I64x22)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I64x22*I65x33)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I63x33*I64x22)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_620 = Coupling(name = 'GC_620',
                  value = '-(ee**2*complex(0,1)*I63x36*I64x22)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I64x22*I65x36)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I63x36*I64x22)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_621 = Coupling(name = 'GC_621',
                  value = '-(ee**2*complex(0,1)*I63x63*I64x22)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I64x22*I65x63)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I63x63*I64x22)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_622 = Coupling(name = 'GC_622',
                  value = '-(ee**2*complex(0,1)*I63x66*I64x22)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I64x22*I65x66)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I63x66*I64x22)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_623 = Coupling(name = 'GC_623',
                  value = '-(ee**2*complex(0,1)*I63x11*I64x33)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I63x11*I66x33)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I63x11*I64x33)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_624 = Coupling(name = 'GC_624',
                  value = '-(ee**2*complex(0,1)*I63x22*I64x33)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I63x22*I66x33)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I63x22*I64x33)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_625 = Coupling(name = 'GC_625',
                  value = '-(ee**2*complex(0,1)*I63x11*I64x36)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I63x11*I66x36)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I63x11*I64x36)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_626 = Coupling(name = 'GC_626',
                  value = '-(ee**2*complex(0,1)*I63x22*I64x36)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I63x22*I66x36)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I63x22*I64x36)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_627 = Coupling(name = 'GC_627',
                  value = '-(ee**2*complex(0,1)*I63x11*I64x63)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I63x11*I66x63)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I63x11*I64x63)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_628 = Coupling(name = 'GC_628',
                  value = '-(ee**2*complex(0,1)*I63x22*I64x63)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I63x22*I66x63)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I63x22*I64x63)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_629 = Coupling(name = 'GC_629',
                  value = '-(ee**2*complex(0,1)*I63x11*I64x66)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I63x11*I66x66)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I63x11*I64x66)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_630 = Coupling(name = 'GC_630',
                  value = '-(ee**2*complex(0,1)*I63x22*I64x66)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I63x22*I66x66)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I63x22*I64x66)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_631 = Coupling(name = 'GC_631',
                  value = '(ee**2*complex(0,1)*I71x11*I72x11)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I73x11*I74x11)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_632 = Coupling(name = 'GC_632',
                  value = '(ee**2*complex(0,1)*I71x22*I72x11)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I71x11*I72x22)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I73x22*I74x11)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I73x11*I74x22)/(16.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_633 = Coupling(name = 'GC_633',
                  value = '(ee**2*complex(0,1)*I71x22*I72x22)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I73x22*I74x22)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_634 = Coupling(name = 'GC_634',
                  value = '-(ee**2*complex(0,1)*I75x11*I76x33)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I72x11*I77x33)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I47x11*I79x33)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I73x11*I80x33)/(8.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I71x33*I72x11)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I71x11*I72x33)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I73x33*I74x11)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I73x11*I74x33)/(16.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_635 = Coupling(name = 'GC_635',
                  value = '-(ee**2*complex(0,1)*I75x22*I76x33)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I72x22*I77x33)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I47x22*I79x33)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I73x22*I80x33)/(8.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I71x33*I72x22)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I71x22*I72x33)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I73x33*I74x22)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I73x22*I74x33)/(16.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_636 = Coupling(name = 'GC_636',
                  value = '-(ee**2*complex(0,1)*I75x11*I76x36)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I72x11*I77x36)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I47x11*I79x36)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I73x11*I80x36)/(8.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I71x36*I72x11)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I71x11*I72x36)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I73x36*I74x11)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I73x11*I74x36)/(16.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_637 = Coupling(name = 'GC_637',
                  value = '-(ee**2*complex(0,1)*I75x22*I76x36)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I72x22*I77x36)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I47x22*I79x36)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I73x22*I80x36)/(8.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I71x36*I72x22)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I71x22*I72x36)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I73x36*I74x22)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I73x22*I74x36)/(16.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_638 = Coupling(name = 'GC_638',
                  value = '-(ee**2*complex(0,1)*I75x11*I76x63)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I72x11*I77x63)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I47x11*I79x63)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I73x11*I80x63)/(8.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I71x63*I72x11)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I71x11*I72x63)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I73x63*I74x11)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I73x11*I74x63)/(16.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_639 = Coupling(name = 'GC_639',
                  value = '-(ee**2*complex(0,1)*I75x22*I76x63)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I72x22*I77x63)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I47x22*I79x63)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I73x22*I80x63)/(8.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I71x63*I72x22)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I71x22*I72x63)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I73x63*I74x22)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I73x22*I74x63)/(16.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_640 = Coupling(name = 'GC_640',
                  value = '-(ee**2*complex(0,1)*I75x11*I76x66)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I72x11*I77x66)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I47x11*I79x66)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I73x11*I80x66)/(8.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I71x66*I72x11)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I71x11*I72x66)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I73x66*I74x11)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I73x11*I74x66)/(16.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_641 = Coupling(name = 'GC_641',
                  value = '-(ee**2*complex(0,1)*I75x22*I76x66)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I72x22*I77x66)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I47x22*I79x66)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I73x22*I80x66)/(8.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I71x66*I72x22)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I71x22*I72x66)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I73x66*I74x22)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I73x22*I74x66)/(16.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_642 = Coupling(name = 'GC_642',
                  value = '-(cw*ee*complex(0,1)*I105x11)/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*I105x11*sw)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_643 = Coupling(name = 'GC_643',
                  value = '-(cw*ee*complex(0,1)*I105x22)/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*I105x22*sw)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_644 = Coupling(name = 'GC_644',
                  value = '-(cw*ee*complex(0,1)*I105x33)/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*I105x33*sw)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*I106x33*sw)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_645 = Coupling(name = 'GC_645',
                  value = '-(cw*ee*complex(0,1)*I105x36)/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*I105x36*sw)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*I106x36*sw)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_646 = Coupling(name = 'GC_646',
                  value = '(cw*ee*complex(0,1)*I105x63)/(2.*(-1 + sw)*sw*(1 + sw)) - (cw*ee*complex(0,1)*I105x63*sw)/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*I106x63*sw)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_647 = Coupling(name = 'GC_647',
                  value = '-(cw*ee*complex(0,1)*I105x66)/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*I105x66*sw)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*I106x66*sw)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_648 = Coupling(name = 'GC_648',
                  value = '(-2*cw*ee**2*complex(0,1)*I113x11)/(3.*(-1 + sw)*sw*(1 + sw)) + (8*cw*ee**2*complex(0,1)*I113x11*sw)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_649 = Coupling(name = 'GC_649',
                  value = '-((cw*ee*complex(0,1)*G*I113x11)/((-1 + sw)*sw*(1 + sw))) + (4*cw*ee*complex(0,1)*G*I113x11*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':1,'QED':1})

GC_650 = Coupling(name = 'GC_650',
                  value = '(-2*cw*ee**2*complex(0,1)*I113x22)/(3.*(-1 + sw)*sw*(1 + sw)) + (8*cw*ee**2*complex(0,1)*I113x22*sw)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_651 = Coupling(name = 'GC_651',
                  value = '-((cw*ee*complex(0,1)*G*I113x22)/((-1 + sw)*sw*(1 + sw))) + (4*cw*ee*complex(0,1)*G*I113x22*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':1,'QED':1})

GC_652 = Coupling(name = 'GC_652',
                  value = '(-2*cw*ee**2*complex(0,1)*I113x33)/(3.*(-1 + sw)*sw*(1 + sw)) + (8*cw*ee**2*complex(0,1)*I113x33*sw)/(9.*(-1 + sw)*(1 + sw)) + (8*cw*ee**2*complex(0,1)*I114x33*sw)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_653 = Coupling(name = 'GC_653',
                  value = '-((cw*ee*complex(0,1)*G*I113x33)/((-1 + sw)*sw*(1 + sw))) + (4*cw*ee*complex(0,1)*G*I113x33*sw)/(3.*(-1 + sw)*(1 + sw)) + (4*cw*ee*complex(0,1)*G*I114x33*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':1,'QED':1})

GC_654 = Coupling(name = 'GC_654',
                  value = '(-2*cw*ee**2*complex(0,1)*I113x36)/(3.*(-1 + sw)*sw*(1 + sw)) + (8*cw*ee**2*complex(0,1)*I113x36*sw)/(9.*(-1 + sw)*(1 + sw)) + (8*cw*ee**2*complex(0,1)*I114x36*sw)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_655 = Coupling(name = 'GC_655',
                  value = '-((cw*ee*complex(0,1)*G*I113x36)/((-1 + sw)*sw*(1 + sw))) + (4*cw*ee*complex(0,1)*G*I113x36*sw)/(3.*(-1 + sw)*(1 + sw)) + (4*cw*ee*complex(0,1)*G*I114x36*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':1,'QED':1})

GC_656 = Coupling(name = 'GC_656',
                  value = '(-2*cw*ee**2*complex(0,1)*I113x63)/(3.*(-1 + sw)*sw*(1 + sw)) + (8*cw*ee**2*complex(0,1)*I113x63*sw)/(9.*(-1 + sw)*(1 + sw)) + (8*cw*ee**2*complex(0,1)*I114x63*sw)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_657 = Coupling(name = 'GC_657',
                  value = '-((cw*ee*complex(0,1)*G*I113x63)/((-1 + sw)*sw*(1 + sw))) + (4*cw*ee*complex(0,1)*G*I113x63*sw)/(3.*(-1 + sw)*(1 + sw)) + (4*cw*ee*complex(0,1)*G*I114x63*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':1,'QED':1})

GC_658 = Coupling(name = 'GC_658',
                  value = '(-2*cw*ee**2*complex(0,1)*I113x66)/(3.*(-1 + sw)*sw*(1 + sw)) + (8*cw*ee**2*complex(0,1)*I113x66*sw)/(9.*(-1 + sw)*(1 + sw)) + (8*cw*ee**2*complex(0,1)*I114x66*sw)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_659 = Coupling(name = 'GC_659',
                  value = '-((cw*ee*complex(0,1)*G*I113x66)/((-1 + sw)*sw*(1 + sw))) + (4*cw*ee*complex(0,1)*G*I113x66*sw)/(3.*(-1 + sw)*(1 + sw)) + (4*cw*ee*complex(0,1)*G*I114x66*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':1,'QED':1})

GC_660 = Coupling(name = 'GC_660',
                  value = '(cw*ee*complex(0,1)*I201x11)/(2.*(-1 + sw)*sw*(1 + sw)) - (2*cw*ee*complex(0,1)*I201x11*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_661 = Coupling(name = 'GC_661',
                  value = '(cw*ee*complex(0,1)*I201x22)/(2.*(-1 + sw)*sw*(1 + sw)) - (2*cw*ee*complex(0,1)*I201x22*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_662 = Coupling(name = 'GC_662',
                  value = '(cw*ee*complex(0,1)*I201x33)/(2.*(-1 + sw)*sw*(1 + sw)) - (2*cw*ee*complex(0,1)*I201x33*sw)/(3.*(-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*I203x33*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_663 = Coupling(name = 'GC_663',
                  value = '(cw*ee*complex(0,1)*I201x36)/(2.*(-1 + sw)*sw*(1 + sw)) - (2*cw*ee*complex(0,1)*I201x36*sw)/(3.*(-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*I203x36*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_664 = Coupling(name = 'GC_664',
                  value = '-(cw*ee*complex(0,1)*I201x63)/(2.*(-1 + sw)*sw*(1 + sw)) + (2*cw*ee*complex(0,1)*I201x63*sw)/(3.*(-1 + sw)*(1 + sw)) + (2*cw*ee*complex(0,1)*I203x63*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_665 = Coupling(name = 'GC_665',
                  value = '(cw*ee*complex(0,1)*I201x66)/(2.*(-1 + sw)*sw*(1 + sw)) - (2*cw*ee*complex(0,1)*I201x66*sw)/(3.*(-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*I203x66*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_666 = Coupling(name = 'GC_666',
                  value = '-((cw*ee**2*complex(0,1)*I47x11)/((-1 + sw)*sw*(1 + sw))) + (2*cw*ee**2*complex(0,1)*I47x11*sw)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_667 = Coupling(name = 'GC_667',
                  value = '-((cw*ee**2*complex(0,1)*I47x22)/((-1 + sw)*sw*(1 + sw))) + (2*cw*ee**2*complex(0,1)*I47x22*sw)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_668 = Coupling(name = 'GC_668',
                  value = '-((cw*ee**2*complex(0,1)*I47x33)/((-1 + sw)*sw*(1 + sw))) + (2*cw*ee**2*complex(0,1)*I47x33*sw)/((-1 + sw)*(1 + sw)) + (2*cw*ee**2*complex(0,1)*I48x33*sw)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_669 = Coupling(name = 'GC_669',
                  value = '-((cw*ee**2*complex(0,1)*I47x36)/((-1 + sw)*sw*(1 + sw))) + (2*cw*ee**2*complex(0,1)*I47x36*sw)/((-1 + sw)*(1 + sw)) + (2*cw*ee**2*complex(0,1)*I48x36*sw)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_670 = Coupling(name = 'GC_670',
                  value = '-((cw*ee**2*complex(0,1)*I47x63)/((-1 + sw)*sw*(1 + sw))) + (2*cw*ee**2*complex(0,1)*I47x63*sw)/((-1 + sw)*(1 + sw)) + (2*cw*ee**2*complex(0,1)*I48x63*sw)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_671 = Coupling(name = 'GC_671',
                  value = '-((cw*ee**2*complex(0,1)*I47x66)/((-1 + sw)*sw*(1 + sw))) + (2*cw*ee**2*complex(0,1)*I47x66*sw)/((-1 + sw)*(1 + sw)) + (2*cw*ee**2*complex(0,1)*I48x66*sw)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_672 = Coupling(name = 'GC_672',
                  value = '-(cw*ee*complex(0,1)*I63x11)/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*I63x11*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_673 = Coupling(name = 'GC_673',
                  value = '-(cw*ee*complex(0,1)*I63x22)/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*I63x22*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_674 = Coupling(name = 'GC_674',
                  value = '-(cw*ee*complex(0,1)*I63x33)/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*I63x33*sw)/(3.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*I65x33*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_675 = Coupling(name = 'GC_675',
                  value = '-(cw*ee*complex(0,1)*I63x36)/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*I63x36*sw)/(3.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*I65x36*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_676 = Coupling(name = 'GC_676',
                  value = '(cw*ee*complex(0,1)*I63x63)/(2.*(-1 + sw)*sw*(1 + sw)) - (cw*ee*complex(0,1)*I63x63*sw)/(3.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*I65x63*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_677 = Coupling(name = 'GC_677',
                  value = '-(cw*ee*complex(0,1)*I63x66)/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*I63x66*sw)/(3.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*I65x66*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_678 = Coupling(name = 'GC_678',
                  value = '-(cw*ee**2*complex(0,1)*I8x11)/(3.*(-1 + sw)*sw*(1 + sw)) + (2*cw*ee**2*complex(0,1)*I8x11*sw)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_679 = Coupling(name = 'GC_679',
                  value = '(cw*ee*complex(0,1)*G*I8x11)/((-1 + sw)*sw*(1 + sw)) - (2*cw*ee*complex(0,1)*G*I8x11*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':1,'QED':1})

GC_680 = Coupling(name = 'GC_680',
                  value = '-(cw*ee**2*complex(0,1)*I8x22)/(3.*(-1 + sw)*sw*(1 + sw)) + (2*cw*ee**2*complex(0,1)*I8x22*sw)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_681 = Coupling(name = 'GC_681',
                  value = '(cw*ee*complex(0,1)*G*I8x22)/((-1 + sw)*sw*(1 + sw)) - (2*cw*ee*complex(0,1)*G*I8x22*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':1,'QED':1})

GC_682 = Coupling(name = 'GC_682',
                  value = '-(cw*ee**2*complex(0,1)*I8x33)/(3.*(-1 + sw)*sw*(1 + sw)) + (2*cw*ee**2*complex(0,1)*I8x33*sw)/(9.*(-1 + sw)*(1 + sw)) + (2*cw*ee**2*complex(0,1)*I9x33*sw)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_683 = Coupling(name = 'GC_683',
                  value = '(cw*ee*complex(0,1)*G*I8x33)/((-1 + sw)*sw*(1 + sw)) - (2*cw*ee*complex(0,1)*G*I8x33*sw)/(3.*(-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*G*I9x33*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':1,'QED':1})

GC_684 = Coupling(name = 'GC_684',
                  value = '-(cw*ee**2*complex(0,1)*I8x36)/(3.*(-1 + sw)*sw*(1 + sw)) + (2*cw*ee**2*complex(0,1)*I8x36*sw)/(9.*(-1 + sw)*(1 + sw)) + (2*cw*ee**2*complex(0,1)*I9x36*sw)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_685 = Coupling(name = 'GC_685',
                  value = '(cw*ee*complex(0,1)*G*I8x36)/((-1 + sw)*sw*(1 + sw)) - (2*cw*ee*complex(0,1)*G*I8x36*sw)/(3.*(-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*G*I9x36*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':1,'QED':1})

GC_686 = Coupling(name = 'GC_686',
                  value = '-(cw*ee**2*complex(0,1)*I8x63)/(3.*(-1 + sw)*sw*(1 + sw)) + (2*cw*ee**2*complex(0,1)*I8x63*sw)/(9.*(-1 + sw)*(1 + sw)) + (2*cw*ee**2*complex(0,1)*I9x63*sw)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_687 = Coupling(name = 'GC_687',
                  value = '(cw*ee*complex(0,1)*G*I8x63)/((-1 + sw)*sw*(1 + sw)) - (2*cw*ee*complex(0,1)*G*I8x63*sw)/(3.*(-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*G*I9x63*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':1,'QED':1})

GC_688 = Coupling(name = 'GC_688',
                  value = '-(cw*ee**2*complex(0,1)*I8x66)/(3.*(-1 + sw)*sw*(1 + sw)) + (2*cw*ee**2*complex(0,1)*I8x66*sw)/(9.*(-1 + sw)*(1 + sw)) + (2*cw*ee**2*complex(0,1)*I9x66*sw)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_689 = Coupling(name = 'GC_689',
                  value = '(cw*ee*complex(0,1)*G*I8x66)/((-1 + sw)*sw*(1 + sw)) - (2*cw*ee*complex(0,1)*G*I8x66*sw)/(3.*(-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*G*I9x66*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':1,'QED':1})

GC_690 = Coupling(name = 'GC_690',
                  value = '(2*ee**2*complex(0,1)*I105x11)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I105x11)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (2*ee**2*complex(0,1)*I105x11*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_691 = Coupling(name = 'GC_691',
                  value = '(2*ee**2*complex(0,1)*I105x22)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I105x22)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (2*ee**2*complex(0,1)*I105x22*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_692 = Coupling(name = 'GC_692',
                  value = '(2*ee**2*complex(0,1)*I105x33)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I105x33)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (2*ee**2*complex(0,1)*I105x33*sw**2)/((-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I106x33*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_693 = Coupling(name = 'GC_693',
                  value = '(2*ee**2*complex(0,1)*I105x36)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I105x36)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (2*ee**2*complex(0,1)*I105x36*sw**2)/((-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I106x36*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_694 = Coupling(name = 'GC_694',
                  value = '(2*ee**2*complex(0,1)*I105x63)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I105x63)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (2*ee**2*complex(0,1)*I105x63*sw**2)/((-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I106x63*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_695 = Coupling(name = 'GC_695',
                  value = '(2*ee**2*complex(0,1)*I105x66)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I105x66)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (2*ee**2*complex(0,1)*I105x66*sw**2)/((-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I106x66*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_696 = Coupling(name = 'GC_696',
                  value = '(ee**2*complex(0,1)*I105x33)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I106x33)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I107x33*I108x33)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I109x33*I110x33)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I105x33)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I107x33*I108x33)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I109x33*I110x33*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_697 = Coupling(name = 'GC_697',
                  value = '(ee**2*complex(0,1)*I105x63)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I106x63)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I107x33*I108x36)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I109x36*I110x33)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I105x63)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I107x33*I108x36)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I109x36*I110x33*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_698 = Coupling(name = 'GC_698',
                  value = '(ee**2*complex(0,1)*I105x36)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I106x36)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I107x36*I108x33)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I109x33*I110x36)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I105x36)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I107x36*I108x33)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I109x33*I110x36*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_699 = Coupling(name = 'GC_699',
                  value = '(ee**2*complex(0,1)*I105x66)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I106x66)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I107x36*I108x36)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I109x36*I110x36)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I105x66)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I107x36*I108x36)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I109x36*I110x36*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_700 = Coupling(name = 'GC_700',
                  value = '-(ee**2*complex(0,1)*I159x33*I163x33)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I164x33*I165x33)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I166x33*I167x33)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I159x33*I163x33)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I164x33*I165x33*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I166x33*I167x33*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_701 = Coupling(name = 'GC_701',
                  value = '-(ee**2*complex(0,1)*I159x33*I163x36)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I164x33*I165x36)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I166x36*I167x33)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I159x33*I163x36)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I164x33*I165x36*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I166x36*I167x33*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_702 = Coupling(name = 'GC_702',
                  value = '-(ee**2*complex(0,1)*I159x33*I163x63)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I164x33*I165x63)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I166x63*I167x33)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I159x33*I163x63)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I164x33*I165x63*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I166x63*I167x33*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_703 = Coupling(name = 'GC_703',
                  value = '-(ee**2*complex(0,1)*I159x33*I163x66)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I164x33*I165x66)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I166x66*I167x33)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I159x33*I163x66)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I164x33*I165x66*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I166x66*I167x33*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_704 = Coupling(name = 'GC_704',
                  value = '-(ee**2*complex(0,1)*I159x36*I163x33)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I164x36*I165x33)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I166x33*I167x36)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I159x36*I163x33)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I164x36*I165x33*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I166x33*I167x36*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_705 = Coupling(name = 'GC_705',
                  value = '-(ee**2*complex(0,1)*I159x36*I163x36)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I164x36*I165x36)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I166x36*I167x36)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I159x36*I163x36)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I164x36*I165x36*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I166x36*I167x36*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_706 = Coupling(name = 'GC_706',
                  value = '-(ee**2*complex(0,1)*I159x36*I163x63)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I164x36*I165x63)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I166x63*I167x36)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I159x36*I163x63)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I164x36*I165x63*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I166x63*I167x36*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_707 = Coupling(name = 'GC_707',
                  value = '-(ee**2*complex(0,1)*I159x36*I163x66)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I164x36*I165x66)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I166x66*I167x36)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I159x36*I163x66)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I164x36*I165x66*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I166x66*I167x36*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_708 = Coupling(name = 'GC_708',
                  value = '-(ee**2*complex(0,1)*I159x63*I163x33)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I164x63*I165x33)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I166x33*I167x63)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I159x63*I163x33)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I164x63*I165x33*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I166x33*I167x63*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_709 = Coupling(name = 'GC_709',
                  value = '-(ee**2*complex(0,1)*I159x63*I163x36)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I164x63*I165x36)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I166x36*I167x63)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I159x63*I163x36)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I164x63*I165x36*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I166x36*I167x63*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_710 = Coupling(name = 'GC_710',
                  value = '-(ee**2*complex(0,1)*I159x63*I163x63)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I164x63*I165x63)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I166x63*I167x63)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I159x63*I163x63)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I164x63*I165x63*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I166x63*I167x63*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_711 = Coupling(name = 'GC_711',
                  value = '-(ee**2*complex(0,1)*I159x63*I163x66)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I164x63*I165x66)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I166x66*I167x63)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I159x63*I163x66)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I164x63*I165x66*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I166x66*I167x63*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_712 = Coupling(name = 'GC_712',
                  value = '-(ee**2*complex(0,1)*I159x66*I163x33)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I164x66*I165x33)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I166x33*I167x66)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I159x66*I163x33)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I164x66*I165x33*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I166x33*I167x66*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_713 = Coupling(name = 'GC_713',
                  value = '-(ee**2*complex(0,1)*I159x66*I163x36)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I164x66*I165x36)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I166x36*I167x66)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I159x66*I163x36)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I164x66*I165x36*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I166x36*I167x66*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_714 = Coupling(name = 'GC_714',
                  value = '-(ee**2*complex(0,1)*I159x66*I163x63)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I164x66*I165x63)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I166x63*I167x66)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I159x66*I163x63)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I164x66*I165x63*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I166x63*I167x66*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_715 = Coupling(name = 'GC_715',
                  value = '-(ee**2*complex(0,1)*I159x66*I163x66)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I164x66*I165x66)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I166x66*I167x66)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I159x66*I163x66)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I164x66*I165x66*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I166x66*I167x66*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_716 = Coupling(name = 'GC_716',
                  value = '(complex(0,1)*G**2*I168x11*I169x11)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I168x11*I169x11*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_717 = Coupling(name = 'GC_717',
                  value = '(complex(0,1)*G**2*I168x22*I169x22)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I168x22*I169x22*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_718 = Coupling(name = 'GC_718',
                  value = '(complex(0,1)*G**2*I170x11*I171x11)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I170x11*I171x11*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_719 = Coupling(name = 'GC_719',
                  value = '(complex(0,1)*G**2*I168x22*I169x11)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I168x11*I169x22)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I170x22*I171x11)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I170x11*I171x22)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I168x22*I169x11*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I168x11*I169x22*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I170x22*I171x11*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I170x11*I171x22*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_720 = Coupling(name = 'GC_720',
                  value = '(complex(0,1)*G**2*I170x22*I171x22)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I170x22*I171x22*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_721 = Coupling(name = 'GC_721',
                  value = '(complex(0,1)*G**2*I172x44*I175x44)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I172x44*I175x44*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_722 = Coupling(name = 'GC_722',
                  value = '(complex(0,1)*G**2*I172x55*I175x55)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I172x55*I175x55*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_723 = Coupling(name = 'GC_723',
                  value = '(complex(0,1)*G**2*I168x33*I169x33)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I169x33*I172x33)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I172x33*I175x33)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I113x33*I176x33)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I168x33*I169x33*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I169x33*I172x33*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I172x33*I175x33*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I113x33*I176x33*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_724 = Coupling(name = 'GC_724',
                  value = '(complex(0,1)*G**2*I168x36*I169x36)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I169x36*I172x36)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I172x36*I175x36)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I113x36*I176x36)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I168x36*I169x36*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I169x36*I172x36*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I172x36*I175x36*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I113x36*I176x36*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_725 = Coupling(name = 'GC_725',
                  value = '(complex(0,1)*G**2*I168x63*I169x63)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I169x63*I172x63)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I172x63*I175x63)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I113x63*I176x63)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I168x63*I169x63*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I169x63*I172x63*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I172x63*I175x63*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I113x63*I176x63*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_726 = Coupling(name = 'GC_726',
                  value = '(complex(0,1)*G**2*I168x66*I169x66)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I169x66*I172x66)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I172x66*I175x66)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I113x66*I176x66)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I168x66*I169x66*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I169x66*I172x66*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I172x66*I175x66*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I113x66*I176x66*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_727 = Coupling(name = 'GC_727',
                  value = '(complex(0,1)*G**2*I168x33*I169x11)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I168x11*I169x33)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I170x33*I171x11)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I170x11*I171x33)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I169x11*I172x33)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I173x11*I174x33)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I113x11*I176x33)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I170x11*I177x33)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I168x33*I169x11*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I168x11*I169x33*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I170x33*I171x11*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I170x11*I171x33*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I169x11*I172x33*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I173x11*I174x33*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I113x11*I176x33*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I170x11*I177x33*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_728 = Coupling(name = 'GC_728',
                  value = '(complex(0,1)*G**2*I168x33*I169x22)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I168x22*I169x33)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I170x33*I171x22)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I170x22*I171x33)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I169x22*I172x33)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I173x22*I174x33)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I113x22*I176x33)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I170x22*I177x33)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I168x33*I169x22*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I168x22*I169x33*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I170x33*I171x22*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I170x22*I171x33*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I169x22*I172x33*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I173x22*I174x33*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I113x22*I176x33*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I170x22*I177x33*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_729 = Coupling(name = 'GC_729',
                  value = '(complex(0,1)*G**2*I168x36*I169x11)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I168x11*I169x36)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I170x36*I171x11)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I170x11*I171x36)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I169x11*I172x36)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I173x11*I174x36)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I113x11*I176x36)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I170x11*I177x36)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I168x36*I169x11*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I168x11*I169x36*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I170x36*I171x11*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I170x11*I171x36*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I169x11*I172x36*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I173x11*I174x36*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I113x11*I176x36*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I170x11*I177x36*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_730 = Coupling(name = 'GC_730',
                  value = '(complex(0,1)*G**2*I168x36*I169x22)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I168x22*I169x36)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I170x36*I171x22)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I170x22*I171x36)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I169x22*I172x36)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I173x22*I174x36)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I113x22*I176x36)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I170x22*I177x36)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I168x36*I169x22*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I168x22*I169x36*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I170x36*I171x22*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I170x22*I171x36*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I169x22*I172x36*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I173x22*I174x36*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I113x22*I176x36*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I170x22*I177x36*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_731 = Coupling(name = 'GC_731',
                  value = '-(complex(0,1)*G**2*I169x11*I172x44)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I173x11*I174x44)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I113x11*I176x44)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I170x11*I177x44)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I169x11*I172x44*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I173x11*I174x44*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I113x11*I176x44*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I170x11*I177x44*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_732 = Coupling(name = 'GC_732',
                  value = '-(complex(0,1)*G**2*I169x22*I172x44)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I173x22*I174x44)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I113x22*I176x44)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I170x22*I177x44)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I169x22*I172x44*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I173x22*I174x44*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I113x22*I176x44*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I170x22*I177x44*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_733 = Coupling(name = 'GC_733',
                  value = '-(complex(0,1)*G**2*I169x11*I172x55)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I173x11*I174x55)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I113x11*I176x55)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I170x11*I177x55)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I169x11*I172x55*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I173x11*I174x55*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I113x11*I176x55*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I170x11*I177x55*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_734 = Coupling(name = 'GC_734',
                  value = '-(complex(0,1)*G**2*I169x22*I172x55)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I173x22*I174x55)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I113x22*I176x55)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I170x22*I177x55)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I169x22*I172x55*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I173x22*I174x55*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I113x22*I176x55*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I170x22*I177x55*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_735 = Coupling(name = 'GC_735',
                  value = '(complex(0,1)*G**2*I168x63*I169x11)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I168x11*I169x63)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I170x63*I171x11)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I170x11*I171x63)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I169x11*I172x63)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I173x11*I174x63)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I113x11*I176x63)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I170x11*I177x63)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I168x63*I169x11*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I168x11*I169x63*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I170x63*I171x11*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I170x11*I171x63*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I169x11*I172x63*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I173x11*I174x63*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I113x11*I176x63*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I170x11*I177x63*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_736 = Coupling(name = 'GC_736',
                  value = '(complex(0,1)*G**2*I168x63*I169x22)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I168x22*I169x63)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I170x63*I171x22)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I170x22*I171x63)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I169x22*I172x63)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I173x22*I174x63)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I113x22*I176x63)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I170x22*I177x63)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I168x63*I169x22*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I168x22*I169x63*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I170x63*I171x22*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I170x22*I171x63*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I169x22*I172x63*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I173x22*I174x63*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I113x22*I176x63*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I170x22*I177x63*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_737 = Coupling(name = 'GC_737',
                  value = '(complex(0,1)*G**2*I168x66*I169x11)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I168x11*I169x66)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I170x66*I171x11)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I170x11*I171x66)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I169x11*I172x66)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I173x11*I174x66)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I113x11*I176x66)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I170x11*I177x66)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I168x66*I169x11*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I168x11*I169x66*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I170x66*I171x11*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I170x11*I171x66*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I169x11*I172x66*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I173x11*I174x66*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I113x11*I176x66*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I170x11*I177x66*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_738 = Coupling(name = 'GC_738',
                  value = '(complex(0,1)*G**2*I168x66*I169x22)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I168x22*I169x66)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I170x66*I171x22)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I170x22*I171x66)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I169x22*I172x66)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I173x22*I174x66)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I113x22*I176x66)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I170x22*I177x66)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I168x66*I169x22*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I168x22*I169x66*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I170x66*I171x22*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I170x22*I171x66*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I169x22*I172x66*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I173x22*I174x66*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I113x22*I176x66*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I170x22*I177x66*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_739 = Coupling(name = 'GC_739',
                  value = '(complex(0,1)*G**2*I170x33*I171x33)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I173x33*I174x33)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I170x33*I177x33)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I177x33*I178x33)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I170x33*I171x33*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I173x33*I174x33*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I170x33*I177x33*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I177x33*I178x33*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_740 = Coupling(name = 'GC_740',
                  value = '(complex(0,1)*G**2*I168x36*I169x33)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I170x33*I171x36)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I169x33*I172x36)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I173x36*I174x33)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I172x36*I175x33)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I113x36*I176x33)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I170x33*I177x36)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I177x36*I178x33)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I168x36*I169x33*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I170x33*I171x36*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I169x33*I172x36*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I173x36*I174x33*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I172x36*I175x33*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I113x36*I176x33*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I170x33*I177x36*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I177x36*I178x33*sw**2)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_741 = Coupling(name = 'GC_741',
                  value = '(complex(0,1)*G**2*I168x33*I169x63)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I170x33*I171x63)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I169x63*I172x33)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I173x63*I174x33)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I172x33*I175x63)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I113x33*I176x63)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I170x33*I177x63)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I177x63*I178x33)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I168x33*I169x63*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I170x33*I171x63*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I169x63*I172x33*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I173x63*I174x33*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I172x33*I175x63*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I113x33*I176x63*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I170x33*I177x63*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I177x63*I178x33*sw**2)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_742 = Coupling(name = 'GC_742',
                  value = '(complex(0,1)*G**2*I168x33*I169x36)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I170x36*I171x33)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I169x36*I172x33)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I173x33*I174x36)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I172x33*I175x36)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I113x33*I176x36)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I170x36*I177x33)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I177x33*I178x36)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I168x33*I169x36*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I170x36*I171x33*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I169x36*I172x33*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I173x33*I174x36*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I172x33*I175x36*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I113x33*I176x36*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I170x36*I177x33*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I177x33*I178x36*sw**2)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_743 = Coupling(name = 'GC_743',
                  value = '(complex(0,1)*G**2*I170x36*I171x36)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I173x36*I174x36)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I170x36*I177x36)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I177x36*I178x36)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I170x36*I171x36*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I173x36*I174x36*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I170x36*I177x36*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I177x36*I178x36*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_744 = Coupling(name = 'GC_744',
                  value = '(complex(0,1)*G**2*I168x36*I169x66)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I170x36*I171x66)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I169x66*I172x36)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I173x66*I174x36)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I172x36*I175x66)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I113x36*I176x66)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I170x36*I177x66)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I177x66*I178x36)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I168x36*I169x66*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I170x36*I171x66*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I169x66*I172x36*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I173x66*I174x36*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I172x36*I175x66*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I113x36*I176x66*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I170x36*I177x66*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I177x66*I178x36*sw**2)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_745 = Coupling(name = 'GC_745',
                  value = '-(complex(0,1)*G**2*I169x33*I172x44)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I173x33*I174x44)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I172x44*I175x33)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I172x33*I175x44)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I113x33*I176x44)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I170x33*I177x44)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I177x44*I178x33)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I177x33*I178x44)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I169x33*I172x44*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I173x33*I174x44*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I172x44*I175x33*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I172x33*I175x44*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I113x33*I176x44*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I170x33*I177x44*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I177x44*I178x33*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I177x33*I178x44*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_746 = Coupling(name = 'GC_746',
                  value = '-(complex(0,1)*G**2*I169x36*I172x44)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I173x36*I174x44)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I172x44*I175x36)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I172x36*I175x44)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I113x36*I176x44)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I170x36*I177x44)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I177x44*I178x36)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I177x36*I178x44)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I169x36*I172x44*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I173x36*I174x44*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I172x44*I175x36*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I172x36*I175x44*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I113x36*I176x44*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I170x36*I177x44*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I177x44*I178x36*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I177x36*I178x44*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_747 = Coupling(name = 'GC_747',
                  value = '(complex(0,1)*G**2*I177x44*I178x44)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I177x44*I178x44*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_748 = Coupling(name = 'GC_748',
                  value = '-(complex(0,1)*G**2*I169x33*I172x55)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I173x33*I174x55)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I172x55*I175x33)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I172x33*I175x55)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I113x33*I176x55)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I170x33*I177x55)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I177x55*I178x33)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I177x33*I178x55)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I169x33*I172x55*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I173x33*I174x55*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I172x55*I175x33*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I172x33*I175x55*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I113x33*I176x55*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I170x33*I177x55*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I177x55*I178x33*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I177x33*I178x55*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_749 = Coupling(name = 'GC_749',
                  value = '-(complex(0,1)*G**2*I169x36*I172x55)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I173x36*I174x55)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I172x55*I175x36)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I172x36*I175x55)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I113x36*I176x55)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I170x36*I177x55)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I177x55*I178x36)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I177x36*I178x55)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I169x36*I172x55*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I173x36*I174x55*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I172x55*I175x36*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I172x36*I175x55*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I113x36*I176x55*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I170x36*I177x55*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I177x55*I178x36*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I177x36*I178x55*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_750 = Coupling(name = 'GC_750',
                  value = '(complex(0,1)*G**2*I172x55*I175x44)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I172x44*I175x55)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I177x55*I178x44)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I177x44*I178x55)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I172x55*I175x44*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I172x44*I175x55*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I177x55*I178x44*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I177x44*I178x55*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_751 = Coupling(name = 'GC_751',
                  value = '(complex(0,1)*G**2*I177x55*I178x55)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I177x55*I178x55*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_752 = Coupling(name = 'GC_752',
                  value = '(complex(0,1)*G**2*I168x63*I169x33)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I170x63*I171x33)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I169x33*I172x63)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I173x33*I174x63)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I172x63*I175x33)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I113x63*I176x33)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I170x63*I177x33)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I177x33*I178x63)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I168x63*I169x33*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I170x63*I171x33*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I169x33*I172x63*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I173x33*I174x63*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I172x63*I175x33*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I113x63*I176x33*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I170x63*I177x33*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I177x33*I178x63*sw**2)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_753 = Coupling(name = 'GC_753',
                  value = '(complex(0,1)*G**2*I168x63*I169x36)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I168x36*I169x63)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I170x63*I171x36)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I170x36*I171x63)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I169x63*I172x36)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I169x36*I172x63)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I173x63*I174x36)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I173x36*I174x63)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I172x63*I175x36)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I172x36*I175x63)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I113x63*I176x36)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I113x36*I176x63)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I170x63*I177x36)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I170x36*I177x63)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I177x63*I178x36)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I177x36*I178x63)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I168x63*I169x36*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I168x36*I169x63*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I170x63*I171x36*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I170x36*I171x63*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I169x63*I172x36*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I169x36*I172x63*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I173x63*I174x36*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I173x36*I174x63*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I172x63*I175x36*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I172x36*I175x63*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I113x63*I176x36*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I113x36*I176x63*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I170x63*I177x36*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I170x36*I177x63*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I177x63*I178x36*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I177x36*I178x63*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_754 = Coupling(name = 'GC_754',
                  value = '-(complex(0,1)*G**2*I169x63*I172x44)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I173x63*I174x44)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I172x63*I175x44)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I172x44*I175x63)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I113x63*I176x44)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I170x63*I177x44)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I177x63*I178x44)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I177x44*I178x63)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I169x63*I172x44*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I173x63*I174x44*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I172x63*I175x44*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I172x44*I175x63*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I113x63*I176x44*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I170x63*I177x44*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I177x63*I178x44*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I177x44*I178x63*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_755 = Coupling(name = 'GC_755',
                  value = '-(complex(0,1)*G**2*I169x63*I172x55)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I173x63*I174x55)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I172x63*I175x55)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I172x55*I175x63)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I113x63*I176x55)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I170x63*I177x55)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I177x63*I178x55)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I177x55*I178x63)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I169x63*I172x55*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I173x63*I174x55*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I172x63*I175x55*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I172x55*I175x63*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I113x63*I176x55*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I170x63*I177x55*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I177x63*I178x55*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I177x55*I178x63*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_756 = Coupling(name = 'GC_756',
                  value = '(complex(0,1)*G**2*I170x63*I171x63)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I173x63*I174x63)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I170x63*I177x63)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I177x63*I178x63)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I170x63*I171x63*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I173x63*I174x63*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I170x63*I177x63*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I177x63*I178x63*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_757 = Coupling(name = 'GC_757',
                  value = '(complex(0,1)*G**2*I168x66*I169x63)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I170x63*I171x66)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I169x63*I172x66)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I173x66*I174x63)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I172x66*I175x63)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I113x66*I176x63)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I170x63*I177x66)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I177x66*I178x63)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I168x66*I169x63*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I170x63*I171x66*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I169x63*I172x66*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I173x66*I174x63*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I172x66*I175x63*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I113x66*I176x63*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I170x63*I177x66*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I177x66*I178x63*sw**2)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_758 = Coupling(name = 'GC_758',
                  value = '(complex(0,1)*G**2*I168x66*I169x33)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I168x33*I169x66)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I170x66*I171x33)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I170x33*I171x66)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I169x66*I172x33)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I169x33*I172x66)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I173x66*I174x33)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I173x33*I174x66)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I172x66*I175x33)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I172x33*I175x66)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I113x66*I176x33)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I113x33*I176x66)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I170x66*I177x33)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I170x33*I177x66)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I177x66*I178x33)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I177x33*I178x66)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I168x66*I169x33*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I168x33*I169x66*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I170x66*I171x33*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I170x33*I171x66*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I169x66*I172x33*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I169x33*I172x66*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I173x66*I174x33*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I173x33*I174x66*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I172x66*I175x33*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I172x33*I175x66*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I113x66*I176x33*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I113x33*I176x66*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I170x66*I177x33*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I170x33*I177x66*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I177x66*I178x33*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I177x33*I178x66*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_759 = Coupling(name = 'GC_759',
                  value = '(complex(0,1)*G**2*I168x66*I169x36)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I170x66*I171x36)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I169x36*I172x66)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I173x36*I174x66)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I172x66*I175x36)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I113x66*I176x36)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I170x66*I177x36)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I177x36*I178x66)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I168x66*I169x36*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I170x66*I171x36*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I169x36*I172x66*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I173x36*I174x66*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I172x66*I175x36*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I113x66*I176x36*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I170x66*I177x36*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I177x36*I178x66*sw**2)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_760 = Coupling(name = 'GC_760',
                  value = '-(complex(0,1)*G**2*I169x66*I172x44)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I173x66*I174x44)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I172x66*I175x44)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I172x44*I175x66)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I113x66*I176x44)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I170x66*I177x44)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I177x66*I178x44)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I177x44*I178x66)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I169x66*I172x44*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I173x66*I174x44*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I172x66*I175x44*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I172x44*I175x66*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I113x66*I176x44*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I170x66*I177x44*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I177x66*I178x44*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I177x44*I178x66*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_761 = Coupling(name = 'GC_761',
                  value = '-(complex(0,1)*G**2*I169x66*I172x55)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I173x66*I174x55)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I172x66*I175x55)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I172x55*I175x66)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I113x66*I176x55)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I170x66*I177x55)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I177x66*I178x55)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I177x55*I178x66)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I169x66*I172x55*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I173x66*I174x55*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I172x66*I175x55*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I172x55*I175x66*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I113x66*I176x55*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I170x66*I177x55*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I177x66*I178x55*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I177x55*I178x66*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_762 = Coupling(name = 'GC_762',
                  value = '(complex(0,1)*G**2*I168x63*I169x66)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I170x66*I171x63)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I169x66*I172x63)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I173x63*I174x66)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I172x63*I175x66)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I113x63*I176x66)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I170x66*I177x63)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I177x63*I178x66)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I168x63*I169x66*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I170x66*I171x63*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I169x66*I172x63*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I173x63*I174x66*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I172x63*I175x66*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I113x63*I176x66*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I170x66*I177x63*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I177x63*I178x66*sw**2)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_763 = Coupling(name = 'GC_763',
                  value = '(complex(0,1)*G**2*I170x66*I171x66)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I173x66*I174x66)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I170x66*I177x66)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I177x66*I178x66)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I170x66*I171x66*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I173x66*I174x66*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I170x66*I177x66*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I177x66*I178x66*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_764 = Coupling(name = 'GC_764',
                  value = '(-2*ee**2*complex(0,1)*I168x33*I169x33)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I169x33*I172x33)/(9.*(-1 + sw)*(1 + sw)) + (4*ee**2*complex(0,1)*I172x33*I175x33)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I113x33*I176x33)/(9.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I179x33*I180x33)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I183x33*I184x33)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I168x33*I169x33)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I179x33*I180x33*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I183x33*I184x33*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_765 = Coupling(name = 'GC_765',
                  value = '(-2*ee**2*complex(0,1)*I168x36*I169x36)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I169x36*I172x36)/(9.*(-1 + sw)*(1 + sw)) + (4*ee**2*complex(0,1)*I172x36*I175x36)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I113x36*I176x36)/(9.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I179x36*I180x36)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I183x36*I184x36)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I168x36*I169x36)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I179x36*I180x36*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I183x36*I184x36*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_766 = Coupling(name = 'GC_766',
                  value = '(-2*ee**2*complex(0,1)*I168x63*I169x63)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I169x63*I172x63)/(9.*(-1 + sw)*(1 + sw)) + (4*ee**2*complex(0,1)*I172x63*I175x63)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I113x63*I176x63)/(9.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I179x63*I180x63)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I183x63*I184x63)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I168x63*I169x63)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I179x63*I180x63*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I183x63*I184x63*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_767 = Coupling(name = 'GC_767',
                  value = '(-2*ee**2*complex(0,1)*I168x66*I169x66)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I169x66*I172x66)/(9.*(-1 + sw)*(1 + sw)) + (4*ee**2*complex(0,1)*I172x66*I175x66)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I113x66*I176x66)/(9.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I179x66*I180x66)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I183x66*I184x66)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I168x66*I169x66)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I179x66*I180x66*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I183x66*I184x66*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_768 = Coupling(name = 'GC_768',
                  value = '(-2*ee**2*complex(0,1)*I170x33*I171x33)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I173x33*I174x33)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I170x33*I177x33)/(9.*(-1 + sw)*(1 + sw)) + (4*ee**2*complex(0,1)*I177x33*I178x33)/(9.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I181x33*I182x33)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I185x33*I186x33)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I170x33*I171x33)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I181x33*I182x33*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I185x33*I186x33*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_769 = Coupling(name = 'GC_769',
                  value = '-(ee**2*complex(0,1)*I168x33*I169x36)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I170x36*I171x33)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I169x36*I172x33)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I173x33*I174x36)/(18.*(-1 + sw)*(1 + sw)) + (2*ee**2*complex(0,1)*I172x33*I175x36)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I113x33*I176x36)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I170x36*I177x33)/(18.*(-1 + sw)*(1 + sw)) + (2*ee**2*complex(0,1)*I177x33*I178x36)/(9.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I179x36*I180x33)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I181x33*I182x36)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I183x33*I184x36)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I185x36*I186x33)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I168x33*I169x36)/(8.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I170x36*I171x33)/(8.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I179x36*I180x33*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I181x33*I182x36*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I183x33*I184x36*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I185x36*I186x33*sw**2)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_770 = Coupling(name = 'GC_770',
                  value = '-(ee**2*complex(0,1)*I168x63*I169x33)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I170x63*I171x33)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I169x33*I172x63)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I173x33*I174x63)/(18.*(-1 + sw)*(1 + sw)) + (2*ee**2*complex(0,1)*I172x63*I175x33)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I113x63*I176x33)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I170x63*I177x33)/(18.*(-1 + sw)*(1 + sw)) + (2*ee**2*complex(0,1)*I177x33*I178x63)/(9.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I179x33*I180x63)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I181x33*I182x63)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I183x63*I184x33)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I185x63*I186x33)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I168x63*I169x33)/(8.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I170x63*I171x33)/(8.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I179x33*I180x63*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I181x33*I182x63*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I183x63*I184x33*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I185x63*I186x33*sw**2)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_771 = Coupling(name = 'GC_771',
                  value = '-(ee**2*complex(0,1)*I168x36*I169x33)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I170x33*I171x36)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I169x33*I172x36)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I173x36*I174x33)/(18.*(-1 + sw)*(1 + sw)) + (2*ee**2*complex(0,1)*I172x36*I175x33)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I113x36*I176x33)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I170x33*I177x36)/(18.*(-1 + sw)*(1 + sw)) + (2*ee**2*complex(0,1)*I177x36*I178x33)/(9.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I179x33*I180x36)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I181x36*I182x33)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I183x36*I184x33)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I185x33*I186x36)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I168x36*I169x33)/(8.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I170x33*I171x36)/(8.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I179x33*I180x36*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I181x36*I182x33*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I183x36*I184x33*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I185x33*I186x36*sw**2)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_772 = Coupling(name = 'GC_772',
                  value = '(-2*ee**2*complex(0,1)*I170x36*I171x36)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I173x36*I174x36)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I170x36*I177x36)/(9.*(-1 + sw)*(1 + sw)) + (4*ee**2*complex(0,1)*I177x36*I178x36)/(9.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I181x36*I182x36)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I185x36*I186x36)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I170x36*I171x36)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I181x36*I182x36*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I185x36*I186x36*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_773 = Coupling(name = 'GC_773',
                  value = '-(ee**2*complex(0,1)*I168x66*I169x36)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I170x66*I171x36)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I169x36*I172x66)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I173x36*I174x66)/(18.*(-1 + sw)*(1 + sw)) + (2*ee**2*complex(0,1)*I172x66*I175x36)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I113x66*I176x36)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I170x66*I177x36)/(18.*(-1 + sw)*(1 + sw)) + (2*ee**2*complex(0,1)*I177x36*I178x66)/(9.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I179x36*I180x66)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I181x36*I182x66)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I183x66*I184x36)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I185x66*I186x36)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I168x66*I169x36)/(8.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I170x66*I171x36)/(8.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I179x36*I180x66*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I181x36*I182x66*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I183x66*I184x36*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I185x66*I186x36*sw**2)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_774 = Coupling(name = 'GC_774',
                  value = '-(ee**2*complex(0,1)*I168x33*I169x63)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I170x33*I171x63)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I169x63*I172x33)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I173x63*I174x33)/(18.*(-1 + sw)*(1 + sw)) + (2*ee**2*complex(0,1)*I172x33*I175x63)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I113x33*I176x63)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I170x33*I177x63)/(18.*(-1 + sw)*(1 + sw)) + (2*ee**2*complex(0,1)*I177x63*I178x33)/(9.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I179x63*I180x33)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I181x63*I182x33)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I183x33*I184x63)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I185x33*I186x63)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I168x33*I169x63)/(8.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I170x33*I171x63)/(8.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I179x63*I180x33*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I181x63*I182x33*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I183x33*I184x63*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I185x33*I186x63*sw**2)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_775 = Coupling(name = 'GC_775',
                  value = '-(ee**2*complex(0,1)*I168x63*I169x36)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I168x36*I169x63)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I170x63*I171x36)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I170x36*I171x63)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I169x63*I172x36)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I169x36*I172x63)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I173x63*I174x36)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I173x36*I174x63)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I172x63*I175x36)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I172x36*I175x63)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I113x63*I176x36)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I113x36*I176x63)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I170x63*I177x36)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I170x36*I177x63)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I177x63*I178x36)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I177x36*I178x63)/(9.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I179x63*I180x36)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I179x36*I180x63)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I181x63*I182x36)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I181x36*I182x63)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I183x63*I184x36)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I183x36*I184x63)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I185x63*I186x36)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I185x36*I186x63)/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I168x63*I169x36)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I168x36*I169x63)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I170x63*I171x36)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I170x36*I171x63)/(16.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I179x63*I180x36*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I179x36*I180x63*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I181x63*I182x36*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I181x36*I182x63*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I183x63*I184x36*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I183x36*I184x63*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I185x63*I186x36*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I185x36*I186x63*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_776 = Coupling(name = 'GC_776',
                  value = '(-2*ee**2*complex(0,1)*I170x63*I171x63)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I173x63*I174x63)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I170x63*I177x63)/(9.*(-1 + sw)*(1 + sw)) + (4*ee**2*complex(0,1)*I177x63*I178x63)/(9.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I181x63*I182x63)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I185x63*I186x63)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I170x63*I171x63)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I181x63*I182x63*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I185x63*I186x63*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_777 = Coupling(name = 'GC_777',
                  value = '-(ee**2*complex(0,1)*I168x63*I169x66)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I170x66*I171x63)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I169x66*I172x63)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I173x63*I174x66)/(18.*(-1 + sw)*(1 + sw)) + (2*ee**2*complex(0,1)*I172x63*I175x66)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I113x63*I176x66)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I170x66*I177x63)/(18.*(-1 + sw)*(1 + sw)) + (2*ee**2*complex(0,1)*I177x63*I178x66)/(9.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I179x66*I180x63)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I181x63*I182x66)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I183x63*I184x66)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I185x66*I186x63)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I168x63*I169x66)/(8.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I170x66*I171x63)/(8.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I179x66*I180x63*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I181x63*I182x66*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I183x63*I184x66*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I185x66*I186x63*sw**2)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_778 = Coupling(name = 'GC_778',
                  value = '-(ee**2*complex(0,1)*I168x66*I169x33)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I168x33*I169x66)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I170x66*I171x33)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I170x33*I171x66)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I169x66*I172x33)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I169x33*I172x66)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I173x66*I174x33)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I173x33*I174x66)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I172x66*I175x33)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I172x33*I175x66)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I113x66*I176x33)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I113x33*I176x66)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I170x66*I177x33)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I170x33*I177x66)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I177x66*I178x33)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I177x33*I178x66)/(9.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I179x66*I180x33)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I179x33*I180x66)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I181x66*I182x33)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I181x33*I182x66)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I183x66*I184x33)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I183x33*I184x66)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I185x66*I186x33)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I185x33*I186x66)/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I168x66*I169x33)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I168x33*I169x66)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I170x66*I171x33)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I170x33*I171x66)/(16.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I179x66*I180x33*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I179x33*I180x66*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I181x66*I182x33*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I181x33*I182x66*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I183x66*I184x33*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I183x33*I184x66*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I185x66*I186x33*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I185x33*I186x66*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_779 = Coupling(name = 'GC_779',
                  value = '-(ee**2*complex(0,1)*I168x36*I169x66)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I170x36*I171x66)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I169x66*I172x36)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I173x66*I174x36)/(18.*(-1 + sw)*(1 + sw)) + (2*ee**2*complex(0,1)*I172x36*I175x66)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I113x36*I176x66)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I170x36*I177x66)/(18.*(-1 + sw)*(1 + sw)) + (2*ee**2*complex(0,1)*I177x66*I178x36)/(9.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I179x66*I180x36)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I181x66*I182x36)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I183x36*I184x66)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I185x36*I186x66)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I168x36*I169x66)/(8.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I170x36*I171x66)/(8.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I179x66*I180x36*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I181x66*I182x36*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I183x36*I184x66*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I185x36*I186x66*sw**2)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_780 = Coupling(name = 'GC_780',
                  value = '-(ee**2*complex(0,1)*I168x66*I169x63)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I170x63*I171x66)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I169x63*I172x66)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I173x66*I174x63)/(18.*(-1 + sw)*(1 + sw)) + (2*ee**2*complex(0,1)*I172x66*I175x63)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I113x66*I176x63)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I170x63*I177x66)/(18.*(-1 + sw)*(1 + sw)) + (2*ee**2*complex(0,1)*I177x66*I178x63)/(9.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I179x63*I180x66)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I181x66*I182x63)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I183x66*I184x63)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I185x63*I186x66)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I168x66*I169x63)/(8.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I170x63*I171x66)/(8.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I179x63*I180x66*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I181x66*I182x63*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I183x66*I184x63*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I185x63*I186x66*sw**2)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_781 = Coupling(name = 'GC_781',
                  value = '(-2*ee**2*complex(0,1)*I170x66*I171x66)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I173x66*I174x66)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I170x66*I177x66)/(9.*(-1 + sw)*(1 + sw)) + (4*ee**2*complex(0,1)*I177x66*I178x66)/(9.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I181x66*I182x66)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I185x66*I186x66)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I170x66*I171x66)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I181x66*I182x66*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I185x66*I186x66*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_782 = Coupling(name = 'GC_782',
                  value = '(4*ee**2*complex(0,1)*I201x11)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I201x11)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (8*ee**2*complex(0,1)*I201x11*sw**2)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_783 = Coupling(name = 'GC_783',
                  value = '(4*ee**2*complex(0,1)*I201x22)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I201x22)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (8*ee**2*complex(0,1)*I201x22*sw**2)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_784 = Coupling(name = 'GC_784',
                  value = '(4*ee**2*complex(0,1)*I201x33)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I201x33)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (8*ee**2*complex(0,1)*I201x33*sw**2)/(9.*(-1 + sw)*(1 + sw)) - (8*ee**2*complex(0,1)*I203x33*sw**2)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_785 = Coupling(name = 'GC_785',
                  value = '(4*ee**2*complex(0,1)*I201x36)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I201x36)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (8*ee**2*complex(0,1)*I201x36*sw**2)/(9.*(-1 + sw)*(1 + sw)) - (8*ee**2*complex(0,1)*I203x36*sw**2)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_786 = Coupling(name = 'GC_786',
                  value = '(4*ee**2*complex(0,1)*I201x63)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I201x63)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (8*ee**2*complex(0,1)*I201x63*sw**2)/(9.*(-1 + sw)*(1 + sw)) - (8*ee**2*complex(0,1)*I203x63*sw**2)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_787 = Coupling(name = 'GC_787',
                  value = '(4*ee**2*complex(0,1)*I201x66)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I201x66)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (8*ee**2*complex(0,1)*I201x66*sw**2)/(9.*(-1 + sw)*(1 + sw)) - (8*ee**2*complex(0,1)*I203x66*sw**2)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_788 = Coupling(name = 'GC_788',
                  value = '(complex(0,1)*G**2*I26x11*I27x11)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I26x11*I27x11*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_789 = Coupling(name = 'GC_789',
                  value = '(complex(0,1)*G**2*I26x22*I27x22)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I26x22*I27x22*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_790 = Coupling(name = 'GC_790',
                  value = '(complex(0,1)*G**2*I28x11*I29x11)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I28x11*I29x11*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_791 = Coupling(name = 'GC_791',
                  value = '(complex(0,1)*G**2*I26x22*I27x11)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I26x11*I27x22)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I28x22*I29x11)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I28x11*I29x22)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I26x22*I27x11*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I26x11*I27x22*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I28x22*I29x11*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I28x11*I29x22*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_792 = Coupling(name = 'GC_792',
                  value = '(complex(0,1)*G**2*I28x22*I29x22)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I28x22*I29x22*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_793 = Coupling(name = 'GC_793',
                  value = '(complex(0,1)*G**2*I30x44*I33x44)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I30x44*I33x44*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_794 = Coupling(name = 'GC_794',
                  value = '(complex(0,1)*G**2*I30x55*I33x55)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I30x55*I33x55*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_795 = Coupling(name = 'GC_795',
                  value = '(complex(0,1)*G**2*I28x33*I29x33)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I31x33*I32x33)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I28x33*I35x33)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I35x33*I36x33)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I28x33*I29x33*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I31x33*I32x33*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I28x33*I35x33*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I35x33*I36x33*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_796 = Coupling(name = 'GC_796',
                  value = '(complex(0,1)*G**2*I28x36*I29x36)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I31x36*I32x36)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I28x36*I35x36)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I35x36*I36x36)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I28x36*I29x36*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I31x36*I32x36*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I28x36*I35x36*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I35x36*I36x36*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_797 = Coupling(name = 'GC_797',
                  value = '(complex(0,1)*G**2*I35x44*I36x44)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I35x44*I36x44*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_798 = Coupling(name = 'GC_798',
                  value = '(complex(0,1)*G**2*I30x55*I33x44)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I30x44*I33x55)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I35x55*I36x44)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I35x44*I36x55)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I30x55*I33x44*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I30x44*I33x55*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I35x55*I36x44*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I35x44*I36x55*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_799 = Coupling(name = 'GC_799',
                  value = '(complex(0,1)*G**2*I35x55*I36x55)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I35x55*I36x55*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_800 = Coupling(name = 'GC_800',
                  value = '(complex(0,1)*G**2*I28x63*I29x63)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I31x63*I32x63)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I28x63*I35x63)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I35x63*I36x63)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I28x63*I29x63*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I31x63*I32x63*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I28x63*I35x63*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I35x63*I36x63*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_801 = Coupling(name = 'GC_801',
                  value = '(complex(0,1)*G**2*I28x66*I29x66)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I31x66*I32x66)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I28x66*I35x66)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I35x66*I36x66)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I28x66*I29x66*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I31x66*I32x66*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I28x66*I35x66*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I35x66*I36x66*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_802 = Coupling(name = 'GC_802',
                  value = '(-2*ee**2*complex(0,1)*I26x33*I27x33)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I27x33*I30x33)/(18.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I30x33*I33x33)/(9.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I37x33*I38x33)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I41x33*I42x33)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I34x33*I8x33)/(18.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I26x33*I27x33)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I37x33*I38x33*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I41x33*I42x33*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_803 = Coupling(name = 'GC_803',
                  value = '(-2*ee**2*complex(0,1)*I26x36*I27x36)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I27x36*I30x36)/(18.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I30x36*I33x36)/(9.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I37x36*I38x36)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I41x36*I42x36)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I34x36*I8x36)/(18.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I26x36*I27x36)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I37x36*I38x36*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I41x36*I42x36*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_804 = Coupling(name = 'GC_804',
                  value = '(-2*ee**2*complex(0,1)*I26x63*I27x63)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I27x63*I30x63)/(18.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I30x63*I33x63)/(9.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I37x63*I38x63)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I41x63*I42x63)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I34x63*I8x63)/(18.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I26x63*I27x63)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I37x63*I38x63*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I41x63*I42x63*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_805 = Coupling(name = 'GC_805',
                  value = '(-2*ee**2*complex(0,1)*I26x66*I27x66)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I27x66*I30x66)/(18.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I30x66*I33x66)/(9.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I37x66*I38x66)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I41x66*I42x66)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I34x66*I8x66)/(18.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I26x66*I27x66)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I37x66*I38x66*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I41x66*I42x66*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_806 = Coupling(name = 'GC_806',
                  value = '(-2*ee**2*complex(0,1)*I28x33*I29x33)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I31x33*I32x33)/(18.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I28x33*I35x33)/(18.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I35x33*I36x33)/(9.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I39x33*I40x33)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I43x33*I44x33)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I28x33*I29x33)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I39x33*I40x33*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I43x33*I44x33*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_807 = Coupling(name = 'GC_807',
                  value = '-(ee**2*complex(0,1)*I26x33*I27x36)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I28x36*I29x33)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I27x36*I30x33)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I31x33*I32x36)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I30x33*I33x36)/(18.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I28x36*I35x33)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I35x33*I36x36)/(18.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I37x36*I38x33)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I39x33*I40x36)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I41x33*I42x36)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I43x36*I44x33)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I34x36*I8x33)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I26x33*I27x36)/(8.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I28x36*I29x33)/(8.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I37x36*I38x33*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I39x33*I40x36*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I41x33*I42x36*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I43x36*I44x33*sw**2)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_808 = Coupling(name = 'GC_808',
                  value = '-(ee**2*complex(0,1)*I26x63*I27x33)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I28x63*I29x33)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I27x33*I30x63)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I31x33*I32x63)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I30x63*I33x33)/(18.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I28x63*I35x33)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I35x33*I36x63)/(18.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I37x33*I38x63)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I39x33*I40x63)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I41x63*I42x33)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I43x63*I44x33)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I34x33*I8x63)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I26x63*I27x33)/(8.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I28x63*I29x33)/(8.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I37x33*I38x63*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I39x33*I40x63*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I41x63*I42x33*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I43x63*I44x33*sw**2)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_809 = Coupling(name = 'GC_809',
                  value = '-(ee**2*complex(0,1)*I26x36*I27x33)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I28x33*I29x36)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I27x33*I30x36)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I31x36*I32x33)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I30x36*I33x33)/(18.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I28x33*I35x36)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I35x36*I36x33)/(18.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I37x33*I38x36)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I39x36*I40x33)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I41x36*I42x33)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I43x33*I44x36)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I34x33*I8x36)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I26x36*I27x33)/(8.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I28x33*I29x36)/(8.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I37x33*I38x36*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I39x36*I40x33*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I41x36*I42x33*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I43x33*I44x36*sw**2)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_810 = Coupling(name = 'GC_810',
                  value = '(-2*ee**2*complex(0,1)*I28x36*I29x36)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I31x36*I32x36)/(18.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I28x36*I35x36)/(18.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I35x36*I36x36)/(9.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I39x36*I40x36)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I43x36*I44x36)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I28x36*I29x36)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I39x36*I40x36*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I43x36*I44x36*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_811 = Coupling(name = 'GC_811',
                  value = '-(ee**2*complex(0,1)*I26x66*I27x36)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I28x66*I29x36)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I27x36*I30x66)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I31x36*I32x66)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I30x66*I33x36)/(18.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I28x66*I35x36)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I35x36*I36x66)/(18.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I37x36*I38x66)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I39x36*I40x66)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I41x66*I42x36)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I43x66*I44x36)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I34x36*I8x66)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I26x66*I27x36)/(8.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I28x66*I29x36)/(8.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I37x36*I38x66*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I39x36*I40x66*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I41x66*I42x36*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I43x66*I44x36*sw**2)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_812 = Coupling(name = 'GC_812',
                  value = '-(ee**2*complex(0,1)*I26x33*I27x63)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I28x33*I29x63)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I27x63*I30x33)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I31x63*I32x33)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I30x33*I33x63)/(18.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I28x33*I35x63)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I35x63*I36x33)/(18.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I37x63*I38x33)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I39x63*I40x33)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I41x33*I42x63)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I43x33*I44x63)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I34x63*I8x33)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I26x33*I27x63)/(8.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I28x33*I29x63)/(8.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I37x63*I38x33*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I39x63*I40x33*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I41x33*I42x63*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I43x33*I44x63*sw**2)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_813 = Coupling(name = 'GC_813',
                  value = '-(ee**2*complex(0,1)*I26x63*I27x36)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I26x36*I27x63)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I28x63*I29x36)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I28x36*I29x63)/(18.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I27x63*I30x36)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I27x36*I30x63)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I31x63*I32x36)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I31x36*I32x63)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I30x63*I33x36)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I30x36*I33x63)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I28x63*I35x36)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I28x36*I35x63)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I35x63*I36x36)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I35x36*I36x63)/(36.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I37x63*I38x36)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I37x36*I38x63)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I39x63*I40x36)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I39x36*I40x63)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I41x63*I42x36)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I41x36*I42x63)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I43x63*I44x36)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I43x36*I44x63)/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I34x63*I8x36)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I34x36*I8x63)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I26x63*I27x36)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I26x36*I27x63)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I28x63*I29x36)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I28x36*I29x63)/(16.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I37x63*I38x36*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I37x36*I38x63*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I39x63*I40x36*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I39x36*I40x63*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I41x63*I42x36*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I41x36*I42x63*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I43x63*I44x36*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I43x36*I44x63*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_814 = Coupling(name = 'GC_814',
                  value = '(-2*ee**2*complex(0,1)*I28x63*I29x63)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I31x63*I32x63)/(18.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I28x63*I35x63)/(18.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I35x63*I36x63)/(9.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I39x63*I40x63)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I43x63*I44x63)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I28x63*I29x63)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I39x63*I40x63*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I43x63*I44x63*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_815 = Coupling(name = 'GC_815',
                  value = '-(ee**2*complex(0,1)*I26x63*I27x66)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I28x66*I29x63)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I27x66*I30x63)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I31x63*I32x66)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I30x63*I33x66)/(18.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I28x66*I35x63)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I35x63*I36x66)/(18.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I37x66*I38x63)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I39x63*I40x66)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I41x63*I42x66)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I43x66*I44x63)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I34x66*I8x63)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I26x63*I27x66)/(8.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I28x66*I29x63)/(8.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I37x66*I38x63*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I39x63*I40x66*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I41x63*I42x66*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I43x66*I44x63*sw**2)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_816 = Coupling(name = 'GC_816',
                  value = '-(ee**2*complex(0,1)*I26x66*I27x33)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I26x33*I27x66)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I28x66*I29x33)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I28x33*I29x66)/(18.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I27x66*I30x33)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I27x33*I30x66)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I31x66*I32x33)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I31x33*I32x66)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I30x66*I33x33)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I30x33*I33x66)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I28x66*I35x33)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I28x33*I35x66)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I35x66*I36x33)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I35x33*I36x66)/(36.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I37x66*I38x33)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I37x33*I38x66)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I39x66*I40x33)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I39x33*I40x66)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I41x66*I42x33)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I41x33*I42x66)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I43x66*I44x33)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I43x33*I44x66)/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I34x66*I8x33)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I34x33*I8x66)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I26x66*I27x33)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I26x33*I27x66)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I28x66*I29x33)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I28x33*I29x66)/(16.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I37x66*I38x33*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I37x33*I38x66*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I39x66*I40x33*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I39x33*I40x66*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I41x66*I42x33*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I41x33*I42x66*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I43x66*I44x33*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I43x33*I44x66*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_817 = Coupling(name = 'GC_817',
                  value = '-(ee**2*complex(0,1)*I26x36*I27x66)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I28x36*I29x66)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I27x66*I30x36)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I31x66*I32x36)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I30x36*I33x66)/(18.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I28x36*I35x66)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I35x66*I36x36)/(18.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I37x66*I38x36)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I39x66*I40x36)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I41x36*I42x66)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I43x36*I44x66)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I34x66*I8x36)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I26x36*I27x66)/(8.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I28x36*I29x66)/(8.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I37x66*I38x36*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I39x66*I40x36*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I41x36*I42x66*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I43x36*I44x66*sw**2)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_818 = Coupling(name = 'GC_818',
                  value = '-(ee**2*complex(0,1)*I26x66*I27x63)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I28x63*I29x66)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I27x63*I30x66)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I31x66*I32x63)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I30x66*I33x63)/(18.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I28x63*I35x66)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I35x66*I36x63)/(18.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I37x63*I38x66)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I39x66*I40x63)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I41x66*I42x63)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I43x63*I44x66)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I34x63*I8x66)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I26x66*I27x63)/(8.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I28x63*I29x66)/(8.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I37x63*I38x66*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I39x66*I40x63*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I41x66*I42x63*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I43x63*I44x66*sw**2)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_819 = Coupling(name = 'GC_819',
                  value = '(-2*ee**2*complex(0,1)*I28x66*I29x66)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I31x66*I32x66)/(18.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I28x66*I35x66)/(18.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I35x66*I36x66)/(9.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I39x66*I40x66)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I43x66*I44x66)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I28x66*I29x66)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I39x66*I40x66*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I43x66*I44x66*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_820 = Coupling(name = 'GC_820',
                  value = '(2*ee**2*complex(0,1)*I63x11)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I63x11)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (2*ee**2*complex(0,1)*I63x11*sw**2)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_821 = Coupling(name = 'GC_821',
                  value = '(complex(0,1)*G**2*I161x11*I63x11)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I161x11*I63x11*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_822 = Coupling(name = 'GC_822',
                  value = '(complex(0,1)*G**2*I161x22*I63x11)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I161x22*I63x11*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_823 = Coupling(name = 'GC_823',
                  value = '(complex(0,1)*G**2*I161x33*I63x11)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I162x33*I63x11)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I161x33*I63x11*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I162x33*I63x11*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_824 = Coupling(name = 'GC_824',
                  value = '(complex(0,1)*G**2*I161x36*I63x11)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I162x36*I63x11)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I161x36*I63x11*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I162x36*I63x11*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_825 = Coupling(name = 'GC_825',
                  value = '-((complex(0,1)*G**2*I162x44*I63x11)/((-1 + sw)*(1 + sw))) + (complex(0,1)*G**2*I162x44*I63x11*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_826 = Coupling(name = 'GC_826',
                  value = '-((complex(0,1)*G**2*I162x55*I63x11)/((-1 + sw)*(1 + sw))) + (complex(0,1)*G**2*I162x55*I63x11*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_827 = Coupling(name = 'GC_827',
                  value = '(complex(0,1)*G**2*I161x63*I63x11)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I162x63*I63x11)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I161x63*I63x11*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I162x63*I63x11*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_828 = Coupling(name = 'GC_828',
                  value = '(complex(0,1)*G**2*I161x66*I63x11)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I162x66*I63x11)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I161x66*I63x11*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I162x66*I63x11*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_829 = Coupling(name = 'GC_829',
                  value = '(2*ee**2*complex(0,1)*I63x22)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I63x22)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (2*ee**2*complex(0,1)*I63x22*sw**2)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_830 = Coupling(name = 'GC_830',
                  value = '(complex(0,1)*G**2*I161x11*I63x22)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I161x11*I63x22*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_831 = Coupling(name = 'GC_831',
                  value = '(complex(0,1)*G**2*I161x22*I63x22)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I161x22*I63x22*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_832 = Coupling(name = 'GC_832',
                  value = '(complex(0,1)*G**2*I161x33*I63x22)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I162x33*I63x22)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I161x33*I63x22*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I162x33*I63x22*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_833 = Coupling(name = 'GC_833',
                  value = '(complex(0,1)*G**2*I161x36*I63x22)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I162x36*I63x22)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I161x36*I63x22*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I162x36*I63x22*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_834 = Coupling(name = 'GC_834',
                  value = '-((complex(0,1)*G**2*I162x44*I63x22)/((-1 + sw)*(1 + sw))) + (complex(0,1)*G**2*I162x44*I63x22*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_835 = Coupling(name = 'GC_835',
                  value = '-((complex(0,1)*G**2*I162x55*I63x22)/((-1 + sw)*(1 + sw))) + (complex(0,1)*G**2*I162x55*I63x22*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_836 = Coupling(name = 'GC_836',
                  value = '(complex(0,1)*G**2*I161x63*I63x22)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I162x63*I63x22)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I161x63*I63x22*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I162x63*I63x22*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_837 = Coupling(name = 'GC_837',
                  value = '(complex(0,1)*G**2*I161x66*I63x22)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I162x66*I63x22)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I161x66*I63x22*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I162x66*I63x22*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_838 = Coupling(name = 'GC_838',
                  value = '(2*ee**2*complex(0,1)*I63x33)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I63x33)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (2*ee**2*complex(0,1)*I63x33*sw**2)/(9.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I65x33*sw**2)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_839 = Coupling(name = 'GC_839',
                  value = '(complex(0,1)*G**2*I161x11*I63x33)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I161x11*I65x33)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I161x11*I63x33*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I161x11*I65x33*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_840 = Coupling(name = 'GC_840',
                  value = '(complex(0,1)*G**2*I161x22*I63x33)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I161x22*I65x33)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I161x22*I63x33*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I161x22*I65x33*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_841 = Coupling(name = 'GC_841',
                  value = '(complex(0,1)*G**2*I161x33*I63x33)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I162x33*I63x33)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I161x33*I65x33)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I162x33*I65x33)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I161x33*I63x33*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I162x33*I63x33*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I161x33*I65x33*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I162x33*I65x33*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_842 = Coupling(name = 'GC_842',
                  value = '(complex(0,1)*G**2*I161x36*I63x33)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I162x36*I63x33)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I161x36*I65x33)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I162x36*I65x33)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I161x36*I63x33*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I162x36*I63x33*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I161x36*I65x33*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I162x36*I65x33*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_843 = Coupling(name = 'GC_843',
                  value = '-((complex(0,1)*G**2*I162x44*I63x33)/((-1 + sw)*(1 + sw))) + (complex(0,1)*G**2*I162x44*I65x33)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I162x44*I63x33*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I162x44*I65x33*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_844 = Coupling(name = 'GC_844',
                  value = '-((complex(0,1)*G**2*I162x55*I63x33)/((-1 + sw)*(1 + sw))) + (complex(0,1)*G**2*I162x55*I65x33)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I162x55*I63x33*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I162x55*I65x33*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_845 = Coupling(name = 'GC_845',
                  value = '(complex(0,1)*G**2*I161x63*I63x33)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I162x63*I63x33)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I161x63*I65x33)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I162x63*I65x33)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I161x63*I63x33*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I162x63*I63x33*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I161x63*I65x33*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I162x63*I65x33*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_846 = Coupling(name = 'GC_846',
                  value = '(complex(0,1)*G**2*I161x66*I63x33)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I162x66*I63x33)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I161x66*I65x33)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I162x66*I65x33)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I161x66*I63x33*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I162x66*I63x33*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I161x66*I65x33*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I162x66*I65x33*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_847 = Coupling(name = 'GC_847',
                  value = '(2*ee**2*complex(0,1)*I63x36)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I63x36)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (2*ee**2*complex(0,1)*I63x36*sw**2)/(9.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I65x36*sw**2)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_848 = Coupling(name = 'GC_848',
                  value = '(complex(0,1)*G**2*I161x11*I63x36)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I161x11*I65x36)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I161x11*I63x36*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I161x11*I65x36*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_849 = Coupling(name = 'GC_849',
                  value = '(complex(0,1)*G**2*I161x22*I63x36)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I161x22*I65x36)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I161x22*I63x36*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I161x22*I65x36*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_850 = Coupling(name = 'GC_850',
                  value = '(complex(0,1)*G**2*I161x33*I63x36)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I162x33*I63x36)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I161x33*I65x36)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I162x33*I65x36)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I161x33*I63x36*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I162x33*I63x36*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I161x33*I65x36*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I162x33*I65x36*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_851 = Coupling(name = 'GC_851',
                  value = '(complex(0,1)*G**2*I161x36*I63x36)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I162x36*I63x36)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I161x36*I65x36)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I162x36*I65x36)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I161x36*I63x36*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I162x36*I63x36*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I161x36*I65x36*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I162x36*I65x36*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_852 = Coupling(name = 'GC_852',
                  value = '-((complex(0,1)*G**2*I162x44*I63x36)/((-1 + sw)*(1 + sw))) + (complex(0,1)*G**2*I162x44*I65x36)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I162x44*I63x36*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I162x44*I65x36*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_853 = Coupling(name = 'GC_853',
                  value = '-((complex(0,1)*G**2*I162x55*I63x36)/((-1 + sw)*(1 + sw))) + (complex(0,1)*G**2*I162x55*I65x36)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I162x55*I63x36*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I162x55*I65x36*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_854 = Coupling(name = 'GC_854',
                  value = '(complex(0,1)*G**2*I161x63*I63x36)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I162x63*I63x36)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I161x63*I65x36)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I162x63*I65x36)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I161x63*I63x36*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I162x63*I63x36*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I161x63*I65x36*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I162x63*I65x36*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_855 = Coupling(name = 'GC_855',
                  value = '(complex(0,1)*G**2*I161x66*I63x36)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I162x66*I63x36)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I161x66*I65x36)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I162x66*I65x36)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I161x66*I63x36*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I162x66*I63x36*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I161x66*I65x36*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I162x66*I65x36*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_856 = Coupling(name = 'GC_856',
                  value = '-((complex(0,1)*G**2*I161x11*I65x44)/((-1 + sw)*(1 + sw))) + (complex(0,1)*G**2*I161x11*I65x44*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_857 = Coupling(name = 'GC_857',
                  value = '-((complex(0,1)*G**2*I161x22*I65x44)/((-1 + sw)*(1 + sw))) + (complex(0,1)*G**2*I161x22*I65x44*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_858 = Coupling(name = 'GC_858',
                  value = '-((complex(0,1)*G**2*I161x33*I65x44)/((-1 + sw)*(1 + sw))) + (complex(0,1)*G**2*I162x33*I65x44)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I161x33*I65x44*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I162x33*I65x44*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_859 = Coupling(name = 'GC_859',
                  value = '-((complex(0,1)*G**2*I161x36*I65x44)/((-1 + sw)*(1 + sw))) + (complex(0,1)*G**2*I162x36*I65x44)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I161x36*I65x44*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I162x36*I65x44*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_860 = Coupling(name = 'GC_860',
                  value = '(complex(0,1)*G**2*I162x44*I65x44)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I162x44*I65x44*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_861 = Coupling(name = 'GC_861',
                  value = '(complex(0,1)*G**2*I162x55*I65x44)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I162x55*I65x44*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_862 = Coupling(name = 'GC_862',
                  value = '-((complex(0,1)*G**2*I161x63*I65x44)/((-1 + sw)*(1 + sw))) + (complex(0,1)*G**2*I162x63*I65x44)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I161x63*I65x44*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I162x63*I65x44*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_863 = Coupling(name = 'GC_863',
                  value = '-((complex(0,1)*G**2*I161x66*I65x44)/((-1 + sw)*(1 + sw))) + (complex(0,1)*G**2*I162x66*I65x44)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I161x66*I65x44*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I162x66*I65x44*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_864 = Coupling(name = 'GC_864',
                  value = '-((complex(0,1)*G**2*I161x11*I65x55)/((-1 + sw)*(1 + sw))) + (complex(0,1)*G**2*I161x11*I65x55*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_865 = Coupling(name = 'GC_865',
                  value = '-((complex(0,1)*G**2*I161x22*I65x55)/((-1 + sw)*(1 + sw))) + (complex(0,1)*G**2*I161x22*I65x55*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_866 = Coupling(name = 'GC_866',
                  value = '-((complex(0,1)*G**2*I161x33*I65x55)/((-1 + sw)*(1 + sw))) + (complex(0,1)*G**2*I162x33*I65x55)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I161x33*I65x55*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I162x33*I65x55*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_867 = Coupling(name = 'GC_867',
                  value = '-((complex(0,1)*G**2*I161x36*I65x55)/((-1 + sw)*(1 + sw))) + (complex(0,1)*G**2*I162x36*I65x55)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I161x36*I65x55*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I162x36*I65x55*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_868 = Coupling(name = 'GC_868',
                  value = '(complex(0,1)*G**2*I162x44*I65x55)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I162x44*I65x55*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_869 = Coupling(name = 'GC_869',
                  value = '(complex(0,1)*G**2*I162x55*I65x55)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I162x55*I65x55*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_870 = Coupling(name = 'GC_870',
                  value = '-((complex(0,1)*G**2*I161x63*I65x55)/((-1 + sw)*(1 + sw))) + (complex(0,1)*G**2*I162x63*I65x55)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I161x63*I65x55*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I162x63*I65x55*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_871 = Coupling(name = 'GC_871',
                  value = '-((complex(0,1)*G**2*I161x66*I65x55)/((-1 + sw)*(1 + sw))) + (complex(0,1)*G**2*I162x66*I65x55)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I161x66*I65x55*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I162x66*I65x55*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_872 = Coupling(name = 'GC_872',
                  value = '(2*ee**2*complex(0,1)*I63x63)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I63x63)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (2*ee**2*complex(0,1)*I63x63*sw**2)/(9.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I65x63*sw**2)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_873 = Coupling(name = 'GC_873',
                  value = '(complex(0,1)*G**2*I161x11*I63x63)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I161x11*I65x63)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I161x11*I63x63*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I161x11*I65x63*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_874 = Coupling(name = 'GC_874',
                  value = '(complex(0,1)*G**2*I161x22*I63x63)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I161x22*I65x63)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I161x22*I63x63*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I161x22*I65x63*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_875 = Coupling(name = 'GC_875',
                  value = '(complex(0,1)*G**2*I161x33*I63x63)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I162x33*I63x63)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I161x33*I65x63)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I162x33*I65x63)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I161x33*I63x63*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I162x33*I63x63*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I161x33*I65x63*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I162x33*I65x63*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_876 = Coupling(name = 'GC_876',
                  value = '(complex(0,1)*G**2*I161x36*I63x63)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I162x36*I63x63)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I161x36*I65x63)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I162x36*I65x63)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I161x36*I63x63*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I162x36*I63x63*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I161x36*I65x63*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I162x36*I65x63*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_877 = Coupling(name = 'GC_877',
                  value = '-((complex(0,1)*G**2*I162x44*I63x63)/((-1 + sw)*(1 + sw))) + (complex(0,1)*G**2*I162x44*I65x63)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I162x44*I63x63*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I162x44*I65x63*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_878 = Coupling(name = 'GC_878',
                  value = '-((complex(0,1)*G**2*I162x55*I63x63)/((-1 + sw)*(1 + sw))) + (complex(0,1)*G**2*I162x55*I65x63)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I162x55*I63x63*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I162x55*I65x63*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_879 = Coupling(name = 'GC_879',
                  value = '(complex(0,1)*G**2*I161x63*I63x63)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I162x63*I63x63)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I161x63*I65x63)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I162x63*I65x63)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I161x63*I63x63*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I162x63*I63x63*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I161x63*I65x63*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I162x63*I65x63*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_880 = Coupling(name = 'GC_880',
                  value = '(complex(0,1)*G**2*I161x66*I63x63)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I162x66*I63x63)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I161x66*I65x63)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I162x66*I65x63)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I161x66*I63x63*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I162x66*I63x63*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I161x66*I65x63*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I162x66*I65x63*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_881 = Coupling(name = 'GC_881',
                  value = '(2*ee**2*complex(0,1)*I63x66)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I63x66)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (2*ee**2*complex(0,1)*I63x66*sw**2)/(9.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I65x66*sw**2)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_882 = Coupling(name = 'GC_882',
                  value = '(complex(0,1)*G**2*I161x11*I63x66)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I161x11*I65x66)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I161x11*I63x66*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I161x11*I65x66*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_883 = Coupling(name = 'GC_883',
                  value = '(complex(0,1)*G**2*I161x22*I63x66)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I161x22*I65x66)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I161x22*I63x66*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I161x22*I65x66*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_884 = Coupling(name = 'GC_884',
                  value = '(complex(0,1)*G**2*I161x33*I63x66)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I162x33*I63x66)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I161x33*I65x66)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I162x33*I65x66)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I161x33*I63x66*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I162x33*I63x66*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I161x33*I65x66*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I162x33*I65x66*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_885 = Coupling(name = 'GC_885',
                  value = '(complex(0,1)*G**2*I161x36*I63x66)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I162x36*I63x66)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I161x36*I65x66)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I162x36*I65x66)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I161x36*I63x66*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I162x36*I63x66*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I161x36*I65x66*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I162x36*I65x66*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_886 = Coupling(name = 'GC_886',
                  value = '-((complex(0,1)*G**2*I162x44*I63x66)/((-1 + sw)*(1 + sw))) + (complex(0,1)*G**2*I162x44*I65x66)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I162x44*I63x66*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I162x44*I65x66*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_887 = Coupling(name = 'GC_887',
                  value = '-((complex(0,1)*G**2*I162x55*I63x66)/((-1 + sw)*(1 + sw))) + (complex(0,1)*G**2*I162x55*I65x66)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I162x55*I63x66*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I162x55*I65x66*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_888 = Coupling(name = 'GC_888',
                  value = '(complex(0,1)*G**2*I161x63*I63x66)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I162x63*I63x66)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I161x63*I65x66)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I162x63*I65x66)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I161x63*I63x66*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I162x63*I63x66*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I161x63*I65x66*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I162x63*I65x66*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_889 = Coupling(name = 'GC_889',
                  value = '(complex(0,1)*G**2*I161x66*I63x66)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I162x66*I63x66)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I161x66*I65x66)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I162x66*I65x66)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I161x66*I63x66*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I162x66*I63x66*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I161x66*I65x66*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I162x66*I65x66*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_890 = Coupling(name = 'GC_890',
                  value = '-(ee**2*complex(0,1)*I63x33*I64x33)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I64x33*I65x33)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I63x33*I66x33)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I65x33*I66x33)/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I67x33*I68x33)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I69x33*I70x33)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I63x33*I64x33)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I67x33*I68x33*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I69x33*I70x33*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_891 = Coupling(name = 'GC_891',
                  value = '-(ee**2*complex(0,1)*I63x36*I64x33)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I64x33*I65x36)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I63x36*I66x33)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I65x36*I66x33)/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I67x33*I68x36)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I69x36*I70x33)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I63x36*I64x33)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I67x33*I68x36*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I69x36*I70x33*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_892 = Coupling(name = 'GC_892',
                  value = '-(ee**2*complex(0,1)*I63x63*I64x33)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I64x33*I65x63)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I63x63*I66x33)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I65x63*I66x33)/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I67x33*I68x63)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I69x63*I70x33)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I63x63*I64x33)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I67x33*I68x63*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I69x63*I70x33*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_893 = Coupling(name = 'GC_893',
                  value = '-(ee**2*complex(0,1)*I63x66*I64x33)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I64x33*I65x66)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I63x66*I66x33)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I65x66*I66x33)/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I67x33*I68x66)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I69x66*I70x33)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I63x66*I64x33)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I67x33*I68x66*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I69x66*I70x33*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_894 = Coupling(name = 'GC_894',
                  value = '-(ee**2*complex(0,1)*I63x33*I64x36)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I64x36*I65x33)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I63x33*I66x36)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I65x33*I66x36)/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I67x36*I68x33)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I69x33*I70x36)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I63x33*I64x36)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I67x36*I68x33*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I69x33*I70x36*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_895 = Coupling(name = 'GC_895',
                  value = '-(ee**2*complex(0,1)*I63x36*I64x36)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I64x36*I65x36)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I63x36*I66x36)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I65x36*I66x36)/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I67x36*I68x36)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I69x36*I70x36)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I63x36*I64x36)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I67x36*I68x36*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I69x36*I70x36*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_896 = Coupling(name = 'GC_896',
                  value = '-(ee**2*complex(0,1)*I63x63*I64x36)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I64x36*I65x63)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I63x63*I66x36)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I65x63*I66x36)/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I67x36*I68x63)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I69x63*I70x36)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I63x63*I64x36)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I67x36*I68x63*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I69x63*I70x36*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_897 = Coupling(name = 'GC_897',
                  value = '-(ee**2*complex(0,1)*I63x66*I64x36)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I64x36*I65x66)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I63x66*I66x36)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I65x66*I66x36)/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I67x36*I68x66)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I69x66*I70x36)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I63x66*I64x36)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I67x36*I68x66*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I69x66*I70x36*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_898 = Coupling(name = 'GC_898',
                  value = '-(ee**2*complex(0,1)*I63x33*I64x63)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I64x63*I65x33)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I63x33*I66x63)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I65x33*I66x63)/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I67x63*I68x33)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I69x33*I70x63)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I63x33*I64x63)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I67x63*I68x33*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I69x33*I70x63*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_899 = Coupling(name = 'GC_899',
                  value = '-(ee**2*complex(0,1)*I63x36*I64x63)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I64x63*I65x36)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I63x36*I66x63)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I65x36*I66x63)/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I67x63*I68x36)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I69x36*I70x63)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I63x36*I64x63)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I67x63*I68x36*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I69x36*I70x63*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_900 = Coupling(name = 'GC_900',
                  value = '-(ee**2*complex(0,1)*I63x63*I64x63)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I64x63*I65x63)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I63x63*I66x63)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I65x63*I66x63)/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I67x63*I68x63)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I69x63*I70x63)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I63x63*I64x63)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I67x63*I68x63*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I69x63*I70x63*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_901 = Coupling(name = 'GC_901',
                  value = '-(ee**2*complex(0,1)*I63x66*I64x63)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I64x63*I65x66)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I63x66*I66x63)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I65x66*I66x63)/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I67x63*I68x66)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I69x66*I70x63)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I63x66*I64x63)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I67x63*I68x66*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I69x66*I70x63*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_902 = Coupling(name = 'GC_902',
                  value = '-(ee**2*complex(0,1)*I63x33*I64x66)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I64x66*I65x33)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I63x33*I66x66)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I65x33*I66x66)/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I67x66*I68x33)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I69x33*I70x66)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I63x33*I64x66)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I67x66*I68x33*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I69x33*I70x66*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_903 = Coupling(name = 'GC_903',
                  value = '-(ee**2*complex(0,1)*I63x36*I64x66)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I64x66*I65x36)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I63x36*I66x66)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I65x36*I66x66)/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I67x66*I68x36)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I69x36*I70x66)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I63x36*I64x66)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I67x66*I68x36*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I69x36*I70x66*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_904 = Coupling(name = 'GC_904',
                  value = '-(ee**2*complex(0,1)*I63x63*I64x66)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I64x66*I65x63)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I63x63*I66x66)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I65x63*I66x66)/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I67x66*I68x63)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I69x63*I70x66)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I63x63*I64x66)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I67x66*I68x63*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I69x63*I70x66*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_905 = Coupling(name = 'GC_905',
                  value = '-(ee**2*complex(0,1)*I63x66*I64x66)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I64x66*I65x66)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I63x66*I66x66)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I65x66*I66x66)/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I67x66*I68x66)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I69x66*I70x66)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I63x66*I64x66)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I67x66*I68x66*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I69x66*I70x66*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_906 = Coupling(name = 'GC_906',
                  value = '-(ee**2*complex(0,1)*I75x33*I76x33)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I72x33*I77x33)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I77x33*I78x33)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I47x33*I79x33)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I73x33*I80x33)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I80x33*I81x33)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I82x33*I83x33)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I84x33*I85x33)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I86x33*I87x33)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I88x33*I89x33)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I71x33*I72x33)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I73x33*I74x33)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I82x33*I83x33*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I84x33*I85x33*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I86x33*I87x33*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I88x33*I89x33*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_907 = Coupling(name = 'GC_907',
                  value = '-(ee**2*complex(0,1)*I75x36*I76x33)/(4.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I75x33*I76x36)/(4.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I72x36*I77x33)/(4.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I72x33*I77x36)/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I77x36*I78x33)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I77x33*I78x36)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I47x36*I79x33)/(4.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I47x33*I79x36)/(4.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I73x36*I80x33)/(4.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I73x33*I80x36)/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I80x36*I81x33)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I80x33*I81x36)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I82x36*I83x33)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I82x33*I83x36)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I84x36*I85x33)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I84x33*I85x36)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I86x36*I87x33)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I86x33*I87x36)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I88x36*I89x33)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I88x33*I89x36)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I71x36*I72x33)/(8.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I71x33*I72x36)/(8.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I73x36*I74x33)/(8.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I73x33*I74x36)/(8.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I82x36*I83x33*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I82x33*I83x36*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I84x36*I85x33*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I84x33*I85x36*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I86x36*I87x33*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I86x33*I87x36*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I88x36*I89x33*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I88x33*I89x36*sw**2)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_908 = Coupling(name = 'GC_908',
                  value = '-(ee**2*complex(0,1)*I75x36*I76x36)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I72x36*I77x36)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I77x36*I78x36)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I47x36*I79x36)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I73x36*I80x36)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I80x36*I81x36)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I82x36*I83x36)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I84x36*I85x36)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I86x36*I87x36)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I88x36*I89x36)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I71x36*I72x36)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I73x36*I74x36)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I82x36*I83x36*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I84x36*I85x36*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I86x36*I87x36*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I88x36*I89x36*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_909 = Coupling(name = 'GC_909',
                  value = '-(ee**2*complex(0,1)*I75x63*I76x33)/(4.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I75x33*I76x63)/(4.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I72x63*I77x33)/(4.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I72x33*I77x63)/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I77x63*I78x33)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I77x33*I78x63)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I47x63*I79x33)/(4.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I47x33*I79x63)/(4.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I73x63*I80x33)/(4.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I73x33*I80x63)/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I80x63*I81x33)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I80x33*I81x63)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I82x63*I83x33)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I82x33*I83x63)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I84x63*I85x33)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I84x33*I85x63)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I86x63*I87x33)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I86x33*I87x63)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I88x63*I89x33)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I88x33*I89x63)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I71x63*I72x33)/(8.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I71x33*I72x63)/(8.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I73x63*I74x33)/(8.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I73x33*I74x63)/(8.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I82x63*I83x33*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I82x33*I83x63*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I84x63*I85x33*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I84x33*I85x63*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I86x63*I87x33*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I86x33*I87x63*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I88x63*I89x33*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I88x33*I89x63*sw**2)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_910 = Coupling(name = 'GC_910',
                  value = '-(ee**2*complex(0,1)*I75x63*I76x63)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I72x63*I77x63)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I77x63*I78x63)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I47x63*I79x63)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I73x63*I80x63)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I80x63*I81x63)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I82x63*I83x63)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I84x63*I85x63)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I86x63*I87x63)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I88x63*I89x63)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I71x63*I72x63)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I73x63*I74x63)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I82x63*I83x63*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I84x63*I85x63*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I86x63*I87x63*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I88x63*I89x63*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_911 = Coupling(name = 'GC_911',
                  value = '-(ee**2*complex(0,1)*I75x66*I76x33)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I75x63*I76x36)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I75x36*I76x63)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I75x33*I76x66)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I72x66*I77x33)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I72x63*I77x36)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I72x36*I77x63)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I72x33*I77x66)/(8.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I77x66*I78x33)/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I77x63*I78x36)/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I77x36*I78x63)/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I77x33*I78x66)/(4.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I47x66*I79x33)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I47x63*I79x36)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I47x36*I79x63)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I47x33*I79x66)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I73x66*I80x33)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I73x63*I80x36)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I73x36*I80x63)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I73x33*I80x66)/(8.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I80x66*I81x33)/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I80x63*I81x36)/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I80x36*I81x63)/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I80x33*I81x66)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I82x66*I83x33)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I82x63*I83x36)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I82x36*I83x63)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I82x33*I83x66)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I84x66*I85x33)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I84x63*I85x36)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I84x36*I85x63)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I84x33*I85x66)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I86x66*I87x33)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I86x63*I87x36)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I86x36*I87x63)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I86x33*I87x66)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I88x66*I89x33)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I88x63*I89x36)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I88x36*I89x63)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I88x33*I89x66)/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I71x66*I72x33)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I71x63*I72x36)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I71x36*I72x63)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I71x33*I72x66)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I73x66*I74x33)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I73x63*I74x36)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I73x36*I74x63)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I73x33*I74x66)/(16.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I82x66*I83x33*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I82x63*I83x36*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I82x36*I83x63*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I82x33*I83x66*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I84x66*I85x33*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I84x63*I85x36*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I84x36*I85x63*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I84x33*I85x66*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I86x66*I87x33*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I86x63*I87x36*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I86x36*I87x63*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I86x33*I87x66*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I88x66*I89x33*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I88x63*I89x36*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I88x36*I89x63*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I88x33*I89x66*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_912 = Coupling(name = 'GC_912',
                  value = '-(ee**2*complex(0,1)*I75x66*I76x36)/(4.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I75x36*I76x66)/(4.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I72x66*I77x36)/(4.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I72x36*I77x66)/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I77x66*I78x36)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I77x36*I78x66)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I47x66*I79x36)/(4.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I47x36*I79x66)/(4.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I73x66*I80x36)/(4.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I73x36*I80x66)/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I80x66*I81x36)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I80x36*I81x66)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I82x66*I83x36)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I82x36*I83x66)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I84x66*I85x36)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I84x36*I85x66)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I86x66*I87x36)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I86x36*I87x66)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I88x66*I89x36)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I88x36*I89x66)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I71x66*I72x36)/(8.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I71x36*I72x66)/(8.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I73x66*I74x36)/(8.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I73x36*I74x66)/(8.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I82x66*I83x36*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I82x36*I83x66*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I84x66*I85x36*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I84x36*I85x66*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I86x66*I87x36*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I86x36*I87x66*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I88x66*I89x36*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I88x36*I89x66*sw**2)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_913 = Coupling(name = 'GC_913',
                  value = '-(ee**2*complex(0,1)*I75x66*I76x63)/(4.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I75x63*I76x66)/(4.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I72x66*I77x63)/(4.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I72x63*I77x66)/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I77x66*I78x63)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I77x63*I78x66)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I47x66*I79x63)/(4.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I47x63*I79x66)/(4.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I73x66*I80x63)/(4.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I73x63*I80x66)/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I80x66*I81x63)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I80x63*I81x66)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I82x66*I83x63)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I82x63*I83x66)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I84x66*I85x63)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I84x63*I85x66)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I86x66*I87x63)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I86x63*I87x66)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I88x66*I89x63)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I88x63*I89x66)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I71x66*I72x63)/(8.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I71x63*I72x66)/(8.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I73x66*I74x63)/(8.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I73x63*I74x66)/(8.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I82x66*I83x63*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I82x63*I83x66*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I84x66*I85x63*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I84x63*I85x66*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I86x66*I87x63*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I86x63*I87x66*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I88x66*I89x63*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I88x63*I89x66*sw**2)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_914 = Coupling(name = 'GC_914',
                  value = '-(ee**2*complex(0,1)*I75x66*I76x66)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I72x66*I77x66)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I77x66*I78x66)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I47x66*I79x66)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I73x66*I80x66)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I80x66*I81x66)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I82x66*I83x66)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I84x66*I85x66)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I86x66*I87x66)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I88x66*I89x66)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I71x66*I72x66)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I73x66*I74x66)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I82x66*I83x66*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I84x66*I85x66*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I86x66*I87x66*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I88x66*I89x66*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_915 = Coupling(name = 'GC_915',
                  value = '(complex(0,1)*G**2*I26x33*I27x11)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I26x11*I27x33)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I28x33*I29x11)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I28x11*I29x33)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I27x11*I30x33)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I31x11*I32x33)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I28x11*I35x33)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I34x33*I8x11)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I26x33*I27x11*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I26x11*I27x33*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I28x33*I29x11*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I28x11*I29x33*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I27x11*I30x33*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I31x11*I32x33*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I28x11*I35x33*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I34x33*I8x11*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_916 = Coupling(name = 'GC_916',
                  value = '(complex(0,1)*G**2*I26x36*I27x11)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I26x11*I27x36)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I28x36*I29x11)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I28x11*I29x36)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I27x11*I30x36)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I31x11*I32x36)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I28x11*I35x36)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I34x36*I8x11)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I26x36*I27x11*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I26x11*I27x36*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I28x36*I29x11*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I28x11*I29x36*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I27x11*I30x36*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I31x11*I32x36*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I28x11*I35x36*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I34x36*I8x11*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_917 = Coupling(name = 'GC_917',
                  value = '-(complex(0,1)*G**2*I27x11*I30x44)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I31x11*I32x44)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I28x11*I35x44)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I34x44*I8x11)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I27x11*I30x44*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I31x11*I32x44*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I28x11*I35x44*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I34x44*I8x11*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_918 = Coupling(name = 'GC_918',
                  value = '-(complex(0,1)*G**2*I27x11*I30x55)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I31x11*I32x55)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I28x11*I35x55)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I34x55*I8x11)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I27x11*I30x55*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I31x11*I32x55*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I28x11*I35x55*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I34x55*I8x11*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_919 = Coupling(name = 'GC_919',
                  value = '(complex(0,1)*G**2*I26x63*I27x11)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I26x11*I27x63)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I28x63*I29x11)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I28x11*I29x63)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I27x11*I30x63)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I31x11*I32x63)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I28x11*I35x63)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I34x63*I8x11)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I26x63*I27x11*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I26x11*I27x63*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I28x63*I29x11*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I28x11*I29x63*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I27x11*I30x63*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I31x11*I32x63*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I28x11*I35x63*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I34x63*I8x11*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_920 = Coupling(name = 'GC_920',
                  value = '(complex(0,1)*G**2*I26x66*I27x11)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I26x11*I27x66)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I28x66*I29x11)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I28x11*I29x66)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I27x11*I30x66)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I31x11*I32x66)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I28x11*I35x66)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I34x66*I8x11)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I26x66*I27x11*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I26x11*I27x66*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I28x66*I29x11*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I28x11*I29x66*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I27x11*I30x66*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I31x11*I32x66*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I28x11*I35x66*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I34x66*I8x11*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_921 = Coupling(name = 'GC_921',
                  value = '(complex(0,1)*G**2*I26x33*I27x22)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I26x22*I27x33)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I28x33*I29x22)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I28x22*I29x33)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I27x22*I30x33)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I31x22*I32x33)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I28x22*I35x33)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I34x33*I8x22)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I26x33*I27x22*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I26x22*I27x33*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I28x33*I29x22*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I28x22*I29x33*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I27x22*I30x33*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I31x22*I32x33*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I28x22*I35x33*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I34x33*I8x22*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_922 = Coupling(name = 'GC_922',
                  value = '(complex(0,1)*G**2*I26x36*I27x22)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I26x22*I27x36)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I28x36*I29x22)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I28x22*I29x36)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I27x22*I30x36)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I31x22*I32x36)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I28x22*I35x36)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I34x36*I8x22)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I26x36*I27x22*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I26x22*I27x36*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I28x36*I29x22*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I28x22*I29x36*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I27x22*I30x36*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I31x22*I32x36*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I28x22*I35x36*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I34x36*I8x22*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_923 = Coupling(name = 'GC_923',
                  value = '-(complex(0,1)*G**2*I27x22*I30x44)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I31x22*I32x44)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I28x22*I35x44)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I34x44*I8x22)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I27x22*I30x44*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I31x22*I32x44*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I28x22*I35x44*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I34x44*I8x22*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_924 = Coupling(name = 'GC_924',
                  value = '-(complex(0,1)*G**2*I27x22*I30x55)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I31x22*I32x55)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I28x22*I35x55)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I34x55*I8x22)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I27x22*I30x55*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I31x22*I32x55*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I28x22*I35x55*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I34x55*I8x22*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_925 = Coupling(name = 'GC_925',
                  value = '(complex(0,1)*G**2*I26x63*I27x22)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I26x22*I27x63)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I28x63*I29x22)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I28x22*I29x63)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I27x22*I30x63)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I31x22*I32x63)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I28x22*I35x63)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I34x63*I8x22)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I26x63*I27x22*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I26x22*I27x63*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I28x63*I29x22*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I28x22*I29x63*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I27x22*I30x63*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I31x22*I32x63*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I28x22*I35x63*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I34x63*I8x22*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_926 = Coupling(name = 'GC_926',
                  value = '(complex(0,1)*G**2*I26x66*I27x22)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I26x22*I27x66)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I28x66*I29x22)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I28x22*I29x66)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I27x22*I30x66)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I31x22*I32x66)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I28x22*I35x66)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I34x66*I8x22)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I26x66*I27x22*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I26x22*I27x66*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I28x66*I29x22*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I28x22*I29x66*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I27x22*I30x66*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I31x22*I32x66*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I28x22*I35x66*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I34x66*I8x22*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_927 = Coupling(name = 'GC_927',
                  value = '(complex(0,1)*G**2*I26x33*I27x33)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I27x33*I30x33)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I30x33*I33x33)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I34x33*I8x33)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I26x33*I27x33*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I27x33*I30x33*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I30x33*I33x33*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I34x33*I8x33*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_928 = Coupling(name = 'GC_928',
                  value = '(complex(0,1)*G**2*I26x33*I27x36)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I28x36*I29x33)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I27x36*I30x33)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I31x33*I32x36)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I30x33*I33x36)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I28x36*I35x33)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I35x33*I36x36)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I34x36*I8x33)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I26x33*I27x36*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I28x36*I29x33*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I27x36*I30x33*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I31x33*I32x36*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I30x33*I33x36*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I28x36*I35x33*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I35x33*I36x36*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I34x36*I8x33*sw**2)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_929 = Coupling(name = 'GC_929',
                  value = '-(complex(0,1)*G**2*I27x33*I30x44)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I31x33*I32x44)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I30x44*I33x33)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I30x33*I33x44)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I28x33*I35x44)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I35x44*I36x33)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I35x33*I36x44)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I34x44*I8x33)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I27x33*I30x44*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I31x33*I32x44*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I30x44*I33x33*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I30x33*I33x44*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I28x33*I35x44*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I35x44*I36x33*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I35x33*I36x44*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I34x44*I8x33*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_930 = Coupling(name = 'GC_930',
                  value = '-(complex(0,1)*G**2*I27x33*I30x55)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I31x33*I32x55)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I30x55*I33x33)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I30x33*I33x55)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I28x33*I35x55)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I35x55*I36x33)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I35x33*I36x55)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I34x55*I8x33)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I27x33*I30x55*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I31x33*I32x55*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I30x55*I33x33*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I30x33*I33x55*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I28x33*I35x55*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I35x55*I36x33*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I35x33*I36x55*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I34x55*I8x33*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_931 = Coupling(name = 'GC_931',
                  value = '(complex(0,1)*G**2*I26x33*I27x63)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I28x33*I29x63)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I27x63*I30x33)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I31x63*I32x33)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I30x33*I33x63)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I28x33*I35x63)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I35x63*I36x33)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I34x63*I8x33)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I26x33*I27x63*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I28x33*I29x63*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I27x63*I30x33*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I31x63*I32x33*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I30x33*I33x63*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I28x33*I35x63*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I35x63*I36x33*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I34x63*I8x33*sw**2)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_932 = Coupling(name = 'GC_932',
                  value = '(complex(0,1)*G**2*I26x36*I27x33)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I28x33*I29x36)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I27x33*I30x36)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I31x36*I32x33)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I30x36*I33x33)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I28x33*I35x36)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I35x36*I36x33)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I34x33*I8x36)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I26x36*I27x33*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I28x33*I29x36*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I27x33*I30x36*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I31x36*I32x33*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I30x36*I33x33*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I28x33*I35x36*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I35x36*I36x33*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I34x33*I8x36*sw**2)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_933 = Coupling(name = 'GC_933',
                  value = '(complex(0,1)*G**2*I26x36*I27x36)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I27x36*I30x36)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I30x36*I33x36)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I34x36*I8x36)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I26x36*I27x36*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I27x36*I30x36*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I30x36*I33x36*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I34x36*I8x36*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_934 = Coupling(name = 'GC_934',
                  value = '-(complex(0,1)*G**2*I27x36*I30x44)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I31x36*I32x44)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I30x44*I33x36)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I30x36*I33x44)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I28x36*I35x44)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I35x44*I36x36)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I35x36*I36x44)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I34x44*I8x36)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I27x36*I30x44*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I31x36*I32x44*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I30x44*I33x36*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I30x36*I33x44*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I28x36*I35x44*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I35x44*I36x36*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I35x36*I36x44*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I34x44*I8x36*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_935 = Coupling(name = 'GC_935',
                  value = '-(complex(0,1)*G**2*I27x36*I30x55)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I31x36*I32x55)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I30x55*I33x36)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I30x36*I33x55)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I28x36*I35x55)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I35x55*I36x36)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I35x36*I36x55)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I34x55*I8x36)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I27x36*I30x55*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I31x36*I32x55*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I30x55*I33x36*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I30x36*I33x55*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I28x36*I35x55*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I35x55*I36x36*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I35x36*I36x55*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I34x55*I8x36*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_936 = Coupling(name = 'GC_936',
                  value = '(complex(0,1)*G**2*I26x36*I27x66)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I28x36*I29x66)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I27x66*I30x36)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I31x66*I32x36)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I30x36*I33x66)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I28x36*I35x66)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I35x66*I36x36)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I34x66*I8x36)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I26x36*I27x66*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I28x36*I29x66*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I27x66*I30x36*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I31x66*I32x36*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I30x36*I33x66*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I28x36*I35x66*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I35x66*I36x36*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I34x66*I8x36*sw**2)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_937 = Coupling(name = 'GC_937',
                  value = '(complex(0,1)*G**2*I26x63*I27x33)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I28x63*I29x33)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I27x33*I30x63)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I31x33*I32x63)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I30x63*I33x33)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I28x63*I35x33)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I35x33*I36x63)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I34x33*I8x63)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I26x63*I27x33*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I28x63*I29x33*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I27x33*I30x63*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I31x33*I32x63*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I30x63*I33x33*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I28x63*I35x33*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I35x33*I36x63*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I34x33*I8x63*sw**2)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_938 = Coupling(name = 'GC_938',
                  value = '(complex(0,1)*G**2*I26x63*I27x36)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I26x36*I27x63)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I28x63*I29x36)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I28x36*I29x63)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I27x63*I30x36)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I27x36*I30x63)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I31x63*I32x36)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I31x36*I32x63)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I30x63*I33x36)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I30x36*I33x63)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I28x63*I35x36)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I28x36*I35x63)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I35x63*I36x36)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I35x36*I36x63)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I34x63*I8x36)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I34x36*I8x63)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I26x63*I27x36*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I26x36*I27x63*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I28x63*I29x36*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I28x36*I29x63*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I27x63*I30x36*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I27x36*I30x63*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I31x63*I32x36*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I31x36*I32x63*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I30x63*I33x36*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I30x36*I33x63*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I28x63*I35x36*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I28x36*I35x63*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I35x63*I36x36*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I35x36*I36x63*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I34x63*I8x36*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I34x36*I8x63*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_939 = Coupling(name = 'GC_939',
                  value = '-(complex(0,1)*G**2*I27x63*I30x44)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I31x63*I32x44)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I30x63*I33x44)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I30x44*I33x63)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I28x63*I35x44)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I35x63*I36x44)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I35x44*I36x63)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I34x44*I8x63)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I27x63*I30x44*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I31x63*I32x44*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I30x63*I33x44*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I30x44*I33x63*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I28x63*I35x44*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I35x63*I36x44*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I35x44*I36x63*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I34x44*I8x63*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_940 = Coupling(name = 'GC_940',
                  value = '-(complex(0,1)*G**2*I27x63*I30x55)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I31x63*I32x55)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I30x63*I33x55)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I30x55*I33x63)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I28x63*I35x55)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I35x63*I36x55)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I35x55*I36x63)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I34x55*I8x63)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I27x63*I30x55*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I31x63*I32x55*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I30x63*I33x55*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I30x55*I33x63*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I28x63*I35x55*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I35x63*I36x55*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I35x55*I36x63*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I34x55*I8x63*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_941 = Coupling(name = 'GC_941',
                  value = '(complex(0,1)*G**2*I26x63*I27x63)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I27x63*I30x63)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I30x63*I33x63)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I34x63*I8x63)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I26x63*I27x63*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I27x63*I30x63*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I30x63*I33x63*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I34x63*I8x63*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_942 = Coupling(name = 'GC_942',
                  value = '(complex(0,1)*G**2*I26x63*I27x66)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I28x66*I29x63)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I27x66*I30x63)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I31x63*I32x66)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I30x63*I33x66)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I28x66*I35x63)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I35x63*I36x66)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I34x66*I8x63)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I26x63*I27x66*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I28x66*I29x63*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I27x66*I30x63*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I31x63*I32x66*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I30x63*I33x66*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I28x66*I35x63*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I35x63*I36x66*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I34x66*I8x63*sw**2)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_943 = Coupling(name = 'GC_943',
                  value = '(complex(0,1)*G**2*I26x66*I27x33)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I26x33*I27x66)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I28x66*I29x33)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I28x33*I29x66)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I27x66*I30x33)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I27x33*I30x66)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I31x66*I32x33)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I31x33*I32x66)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I30x66*I33x33)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I30x33*I33x66)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I28x66*I35x33)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I28x33*I35x66)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I35x66*I36x33)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I35x33*I36x66)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I34x66*I8x33)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I34x33*I8x66)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I26x66*I27x33*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I26x33*I27x66*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I28x66*I29x33*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I28x33*I29x66*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I27x66*I30x33*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I27x33*I30x66*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I31x66*I32x33*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I31x33*I32x66*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I30x66*I33x33*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I30x33*I33x66*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I28x66*I35x33*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I28x33*I35x66*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I35x66*I36x33*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I35x33*I36x66*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I34x66*I8x33*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I34x33*I8x66*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_944 = Coupling(name = 'GC_944',
                  value = '(complex(0,1)*G**2*I26x66*I27x36)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I28x66*I29x36)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I27x36*I30x66)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I31x36*I32x66)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I30x66*I33x36)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I28x66*I35x36)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I35x36*I36x66)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I34x36*I8x66)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I26x66*I27x36*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I28x66*I29x36*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I27x36*I30x66*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I31x36*I32x66*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I30x66*I33x36*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I28x66*I35x36*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I35x36*I36x66*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I34x36*I8x66*sw**2)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_945 = Coupling(name = 'GC_945',
                  value = '-(complex(0,1)*G**2*I27x66*I30x44)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I31x66*I32x44)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I30x66*I33x44)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I30x44*I33x66)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I28x66*I35x44)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I35x66*I36x44)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I35x44*I36x66)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I34x44*I8x66)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I27x66*I30x44*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I31x66*I32x44*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I30x66*I33x44*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I30x44*I33x66*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I28x66*I35x44*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I35x66*I36x44*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I35x44*I36x66*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I34x44*I8x66*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_946 = Coupling(name = 'GC_946',
                  value = '-(complex(0,1)*G**2*I27x66*I30x55)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I31x66*I32x55)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I30x66*I33x55)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I30x55*I33x66)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I28x66*I35x55)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I35x66*I36x55)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I35x55*I36x66)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I34x55*I8x66)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I27x66*I30x55*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I31x66*I32x55*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I30x66*I33x55*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I30x55*I33x66*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I28x66*I35x55*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I35x66*I36x55*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I35x55*I36x66*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I34x55*I8x66*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_947 = Coupling(name = 'GC_947',
                  value = '(complex(0,1)*G**2*I26x66*I27x63)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I28x63*I29x66)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I27x63*I30x66)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I31x66*I32x63)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I30x66*I33x63)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I28x63*I35x66)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I35x66*I36x63)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I34x63*I8x66)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I26x66*I27x63*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I28x63*I29x66*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I27x63*I30x66*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I31x66*I32x63*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I30x66*I33x63*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I28x63*I35x66*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I35x66*I36x63*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I34x63*I8x66*sw**2)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_948 = Coupling(name = 'GC_948',
                  value = '(complex(0,1)*G**2*I26x66*I27x66)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I27x66*I30x66)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I30x66*I33x66)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I34x66*I8x66)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I26x66*I27x66*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I27x66*I30x66*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I30x66*I33x66*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I34x66*I8x66*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_949 = Coupling(name = 'GC_949',
                  value = '(complex(0,1)*I13x33*NN13)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I13x33*NN13*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN11*Rd36*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_950 = Coupling(name = 'GC_950',
                  value = '(complex(0,1)*I13x36*NN13)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I13x36*NN13*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN11*Rd66*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_951 = Coupling(name = 'GC_951',
                  value = '(complex(0,1)*I49x33*NN13)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I49x33*NN13*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN11*Rl36*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_952 = Coupling(name = 'GC_952',
                  value = '(complex(0,1)*I49x36*NN13)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I49x36*NN13*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN11*Rl66*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_953 = Coupling(name = 'GC_953',
                  value = '(complex(0,1)*I131x33*NN14)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I131x33*NN14*sw**2)/((-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*NN11*Ru36*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_954 = Coupling(name = 'GC_954',
                  value = '(complex(0,1)*I131x36*NN14)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I131x36*NN14*sw**2)/((-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*NN11*Ru66*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_955 = Coupling(name = 'GC_955',
                  value = '(complex(0,1)*I13x33*NN23)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I13x33*NN23*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN21*Rd36*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_956 = Coupling(name = 'GC_956',
                  value = '(complex(0,1)*I13x36*NN23)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I13x36*NN23*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN21*Rd66*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_957 = Coupling(name = 'GC_957',
                  value = '(complex(0,1)*I49x33*NN23)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I49x33*NN23*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN21*Rl36*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_958 = Coupling(name = 'GC_958',
                  value = '(complex(0,1)*I49x36*NN23)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I49x36*NN23*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN21*Rl66*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_959 = Coupling(name = 'GC_959',
                  value = '(complex(0,1)*I131x33*NN24)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I131x33*NN24*sw**2)/((-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*NN21*Ru36*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_960 = Coupling(name = 'GC_960',
                  value = '(complex(0,1)*I131x36*NN24)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I131x36*NN24*sw**2)/((-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*NN21*Ru66*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_961 = Coupling(name = 'GC_961',
                  value = '(complex(0,1)*I13x33*NN33)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I13x33*NN33*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN31*Rd36*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_962 = Coupling(name = 'GC_962',
                  value = '(complex(0,1)*I13x36*NN33)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I13x36*NN33*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN31*Rd66*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_963 = Coupling(name = 'GC_963',
                  value = '(complex(0,1)*I49x33*NN33)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I49x33*NN33*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN31*Rl36*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_964 = Coupling(name = 'GC_964',
                  value = '(complex(0,1)*I49x36*NN33)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I49x36*NN33*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN31*Rl66*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_965 = Coupling(name = 'GC_965',
                  value = '(complex(0,1)*I131x33*NN34)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I131x33*NN34*sw**2)/((-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*NN31*Ru36*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_966 = Coupling(name = 'GC_966',
                  value = '(complex(0,1)*I131x36*NN34)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I131x36*NN34*sw**2)/((-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*NN31*Ru66*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_967 = Coupling(name = 'GC_967',
                  value = '(complex(0,1)*I13x33*NN43)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I13x33*NN43*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN41*Rd36*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_968 = Coupling(name = 'GC_968',
                  value = '(complex(0,1)*I13x36*NN43)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I13x36*NN43*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN41*Rd66*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_969 = Coupling(name = 'GC_969',
                  value = '(complex(0,1)*I49x33*NN43)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I49x33*NN43*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN41*Rl36*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_970 = Coupling(name = 'GC_970',
                  value = '(complex(0,1)*I49x36*NN43)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I49x36*NN43*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN41*Rl66*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_971 = Coupling(name = 'GC_971',
                  value = '(complex(0,1)*I131x33*NN44)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I131x33*NN44*sw**2)/((-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*NN41*Ru36*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_972 = Coupling(name = 'GC_972',
                  value = '(complex(0,1)*I131x36*NN44)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I131x36*NN44*sw**2)/((-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*NN41*Ru66*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_973 = Coupling(name = 'GC_973',
                  value = '-((ee*complex(0,1)*I187x11*UU11)/sw)',
                  order = {'QED':1})

GC_974 = Coupling(name = 'GC_974',
                  value = '-((ee*complex(0,1)*I187x22*UU11)/sw)',
                  order = {'QED':1})

GC_975 = Coupling(name = 'GC_975',
                  value = '-((ee*complex(0,1)*I190x11*UU11)/sw)',
                  order = {'QED':1})

GC_976 = Coupling(name = 'GC_976',
                  value = '-((ee*complex(0,1)*I190x22*UU11)/sw)',
                  order = {'QED':1})

GC_977 = Coupling(name = 'GC_977',
                  value = 'complex(0,1)*I134x33*UU12',
                  order = {'QED':1})

GC_978 = Coupling(name = 'GC_978',
                  value = 'complex(0,1)*I134x36*UU12',
                  order = {'QED':1})

GC_979 = Coupling(name = 'GC_979',
                  value = 'complex(0,1)*I97x33*UU12',
                  order = {'QED':1})

GC_980 = Coupling(name = 'GC_980',
                  value = '-((ee*complex(0,1)*I187x33*UU11)/sw) + complex(0,1)*I188x33*UU12',
                  order = {'QED':1})

GC_981 = Coupling(name = 'GC_981',
                  value = '-((ee*complex(0,1)*I187x36*UU11)/sw) + complex(0,1)*I188x36*UU12',
                  order = {'QED':1})

GC_982 = Coupling(name = 'GC_982',
                  value = '-((ee*complex(0,1)*I190x33*UU11)/sw) + complex(0,1)*I191x33*UU12',
                  order = {'QED':1})

GC_983 = Coupling(name = 'GC_983',
                  value = '-((ee*complex(0,1)*I190x36*UU11)/sw) + complex(0,1)*I191x36*UU12',
                  order = {'QED':1})

GC_984 = Coupling(name = 'GC_984',
                  value = '-((ee*complex(0,1)*I187x11*UU21)/sw)',
                  order = {'QED':1})

GC_985 = Coupling(name = 'GC_985',
                  value = '-((ee*complex(0,1)*I187x22*UU21)/sw)',
                  order = {'QED':1})

GC_986 = Coupling(name = 'GC_986',
                  value = '-((ee*complex(0,1)*I190x11*UU21)/sw)',
                  order = {'QED':1})

GC_987 = Coupling(name = 'GC_987',
                  value = '-((ee*complex(0,1)*I190x22*UU21)/sw)',
                  order = {'QED':1})

GC_988 = Coupling(name = 'GC_988',
                  value = 'complex(0,1)*I134x33*UU22',
                  order = {'QED':1})

GC_989 = Coupling(name = 'GC_989',
                  value = 'complex(0,1)*I134x36*UU22',
                  order = {'QED':1})

GC_990 = Coupling(name = 'GC_990',
                  value = 'complex(0,1)*I97x33*UU22',
                  order = {'QED':1})

GC_991 = Coupling(name = 'GC_991',
                  value = '-((ee*complex(0,1)*I187x33*UU21)/sw) + complex(0,1)*I188x33*UU22',
                  order = {'QED':1})

GC_992 = Coupling(name = 'GC_992',
                  value = '-((ee*complex(0,1)*I187x36*UU21)/sw) + complex(0,1)*I188x36*UU22',
                  order = {'QED':1})

GC_993 = Coupling(name = 'GC_993',
                  value = '-((ee*complex(0,1)*I190x33*UU21)/sw) + complex(0,1)*I191x33*UU22',
                  order = {'QED':1})

GC_994 = Coupling(name = 'GC_994',
                  value = '-((ee*complex(0,1)*I190x36*UU21)/sw) + complex(0,1)*I191x36*UU22',
                  order = {'QED':1})

GC_995 = Coupling(name = 'GC_995',
                  value = '-((ee*complex(0,1)*I192x11*VV11)/sw)',
                  order = {'QED':1})

GC_996 = Coupling(name = 'GC_996',
                  value = '-((ee*complex(0,1)*I192x22*VV11)/sw)',
                  order = {'QED':1})

GC_997 = Coupling(name = 'GC_997',
                  value = '-((ee*complex(0,1)*I192x33*VV11)/sw)',
                  order = {'QED':1})

GC_998 = Coupling(name = 'GC_998',
                  value = '-((ee*complex(0,1)*I194x11*VV11)/sw)',
                  order = {'QED':1})

GC_999 = Coupling(name = 'GC_999',
                  value = '-((ee*complex(0,1)*I194x22*VV11)/sw)',
                  order = {'QED':1})

GC_1000 = Coupling(name = 'GC_1000',
                   value = 'complex(0,1)*I11x33*VV12',
                   order = {'QED':1})

GC_1001 = Coupling(name = 'GC_1001',
                   value = 'complex(0,1)*I11x36*VV12',
                   order = {'QED':1})

GC_1002 = Coupling(name = 'GC_1002',
                   value = '-((ee*complex(0,1)*I194x33*VV11)/sw) + complex(0,1)*I195x33*VV12',
                   order = {'QED':1})

GC_1003 = Coupling(name = 'GC_1003',
                   value = '-((ee*complex(0,1)*I194x36*VV11)/sw) + complex(0,1)*I195x36*VV12',
                   order = {'QED':1})

GC_1004 = Coupling(name = 'GC_1004',
                   value = '-((ee*complex(0,1)*I192x11*VV21)/sw)',
                   order = {'QED':1})

GC_1005 = Coupling(name = 'GC_1005',
                   value = '-((ee*complex(0,1)*I192x22*VV21)/sw)',
                   order = {'QED':1})

GC_1006 = Coupling(name = 'GC_1006',
                   value = '-((ee*complex(0,1)*I192x33*VV21)/sw)',
                   order = {'QED':1})

GC_1007 = Coupling(name = 'GC_1007',
                   value = '-((ee*complex(0,1)*I194x11*VV21)/sw)',
                   order = {'QED':1})

GC_1008 = Coupling(name = 'GC_1008',
                   value = '-((ee*complex(0,1)*I194x22*VV21)/sw)',
                   order = {'QED':1})

GC_1009 = Coupling(name = 'GC_1009',
                   value = 'complex(0,1)*I11x33*VV22',
                   order = {'QED':1})

GC_1010 = Coupling(name = 'GC_1010',
                   value = 'complex(0,1)*I11x36*VV22',
                   order = {'QED':1})

GC_1011 = Coupling(name = 'GC_1011',
                   value = '-((ee*complex(0,1)*I194x33*VV21)/sw) + complex(0,1)*I195x33*VV22',
                   order = {'QED':1})

GC_1012 = Coupling(name = 'GC_1012',
                   value = '-((ee*complex(0,1)*I194x36*VV21)/sw) + complex(0,1)*I195x36*VV22',
                   order = {'QED':1})

GC_1013 = Coupling(name = 'GC_1013',
                   value = '(ee*complex(0,1)*complexconjugate(CKM11))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1014 = Coupling(name = 'GC_1014',
                   value = '(ee*complex(0,1)*complexconjugate(CKM22))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1015 = Coupling(name = 'GC_1015',
                   value = '(ee*complex(0,1)*complexconjugate(CKM33))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1016 = Coupling(name = 'GC_1016',
                   value = '(cw*ee*complex(0,1)*Rd11*complexconjugate(NN11))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rd11*complexconjugate(NN12))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rd11*sw*complexconjugate(NN12))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1017 = Coupling(name = 'GC_1017',
                   value = '(cw*ee*complex(0,1)*Rd22*complexconjugate(NN11))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rd22*complexconjugate(NN12))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rd22*sw*complexconjugate(NN12))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1018 = Coupling(name = 'GC_1018',
                   value = '-((cw*ee*complex(0,1)*Rl11*complexconjugate(NN11))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) - (ee*complex(0,1)*Rl11*complexconjugate(NN12))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rl11*sw*complexconjugate(NN12))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1019 = Coupling(name = 'GC_1019',
                   value = '-((cw*ee*complex(0,1)*Rl22*complexconjugate(NN11))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) - (ee*complex(0,1)*Rl22*complexconjugate(NN12))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rl22*sw*complexconjugate(NN12))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1020 = Coupling(name = 'GC_1020',
                   value = '-((cw*ee*complex(0,1)*Rn11*complexconjugate(NN11))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*Rn11*complexconjugate(NN12))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rn11*sw*complexconjugate(NN12))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1021 = Coupling(name = 'GC_1021',
                   value = '-((cw*ee*complex(0,1)*Rn22*complexconjugate(NN11))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*Rn22*complexconjugate(NN12))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rn22*sw*complexconjugate(NN12))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1022 = Coupling(name = 'GC_1022',
                   value = '-((cw*ee*complex(0,1)*Rn33*complexconjugate(NN11))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*Rn33*complexconjugate(NN12))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rn33*sw*complexconjugate(NN12))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1023 = Coupling(name = 'GC_1023',
                   value = '(cw*ee*complex(0,1)*Ru11*complexconjugate(NN11))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Ru11*complexconjugate(NN12))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Ru11*sw*complexconjugate(NN12))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1024 = Coupling(name = 'GC_1024',
                   value = '(cw*ee*complex(0,1)*Ru22*complexconjugate(NN11))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Ru22*complexconjugate(NN12))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Ru22*sw*complexconjugate(NN12))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1025 = Coupling(name = 'GC_1025',
                   value = '(complex(0,1)*I14x33*complexconjugate(NN13))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I14x33*sw**2*complexconjugate(NN13))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*Rd33*complexconjugate(NN11))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rd33*complexconjugate(NN12))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rd33*sw*complexconjugate(NN12))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1026 = Coupling(name = 'GC_1026',
                   value = '(complex(0,1)*I14x36*complexconjugate(NN13))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I14x36*sw**2*complexconjugate(NN13))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*Rd63*complexconjugate(NN11))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rd63*complexconjugate(NN12))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rd63*sw*complexconjugate(NN12))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1027 = Coupling(name = 'GC_1027',
                   value = '(complex(0,1)*I50x33*complexconjugate(NN13))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I50x33*sw**2*complexconjugate(NN13))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*Rl33*complexconjugate(NN11))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rl33*complexconjugate(NN12))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rl33*sw*complexconjugate(NN12))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1028 = Coupling(name = 'GC_1028',
                   value = '(complex(0,1)*I50x36*complexconjugate(NN13))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I50x36*sw**2*complexconjugate(NN13))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*Rl63*complexconjugate(NN11))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rl63*complexconjugate(NN12))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rl63*sw*complexconjugate(NN12))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1029 = Coupling(name = 'GC_1029',
                   value = '-((ee*complex(0,1)*UU11*complexconjugate(NN12))/sw) - (ee*complex(0,1)*UU12*complexconjugate(NN13))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1030 = Coupling(name = 'GC_1030',
                   value = '-((ee*complex(0,1)*UU21*complexconjugate(NN12))/sw) - (ee*complex(0,1)*UU22*complexconjugate(NN13))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1031 = Coupling(name = 'GC_1031',
                   value = '-(cw*ee*complex(0,1)*NN13*complexconjugate(NN13))/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*NN14*complexconjugate(NN14))/(2.*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1})

GC_1032 = Coupling(name = 'GC_1032',
                   value = '(cw*ee*complex(0,1)*NN23*complexconjugate(NN13))/(2.*(-1 + sw)*sw*(1 + sw)) - (cw*ee*complex(0,1)*NN24*complexconjugate(NN14))/(2.*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1})

GC_1033 = Coupling(name = 'GC_1033',
                   value = '(cw*ee*complex(0,1)*NN33*complexconjugate(NN13))/(2.*(-1 + sw)*sw*(1 + sw)) - (cw*ee*complex(0,1)*NN34*complexconjugate(NN14))/(2.*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1})

GC_1034 = Coupling(name = 'GC_1034',
                   value = '(cw*ee*complex(0,1)*NN43*complexconjugate(NN13))/(2.*(-1 + sw)*sw*(1 + sw)) - (cw*ee*complex(0,1)*NN44*complexconjugate(NN14))/(2.*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1})

GC_1035 = Coupling(name = 'GC_1035',
                   value = '(complex(0,1)*I132x33*complexconjugate(NN14))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I132x33*sw**2*complexconjugate(NN14))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*Ru33*complexconjugate(NN11))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Ru33*complexconjugate(NN12))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Ru33*sw*complexconjugate(NN12))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1036 = Coupling(name = 'GC_1036',
                   value = '(complex(0,1)*I132x36*complexconjugate(NN14))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I132x36*sw**2*complexconjugate(NN14))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*Ru63*complexconjugate(NN11))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Ru63*complexconjugate(NN12))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Ru63*sw*complexconjugate(NN12))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1037 = Coupling(name = 'GC_1037',
                   value = '-((ee*complex(0,1)*VV11*complexconjugate(NN12))/sw) + (ee*complex(0,1)*VV12*complexconjugate(NN14))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1038 = Coupling(name = 'GC_1038',
                   value = '-((ee*complex(0,1)*VV21*complexconjugate(NN12))/sw) + (ee*complex(0,1)*VV22*complexconjugate(NN14))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1039 = Coupling(name = 'GC_1039',
                   value = '(cw*ee*complex(0,1)*Rd11*complexconjugate(NN21))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rd11*complexconjugate(NN22))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rd11*sw*complexconjugate(NN22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1040 = Coupling(name = 'GC_1040',
                   value = '(cw*ee*complex(0,1)*Rd22*complexconjugate(NN21))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rd22*complexconjugate(NN22))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rd22*sw*complexconjugate(NN22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1041 = Coupling(name = 'GC_1041',
                   value = '-((cw*ee*complex(0,1)*Rl11*complexconjugate(NN21))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) - (ee*complex(0,1)*Rl11*complexconjugate(NN22))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rl11*sw*complexconjugate(NN22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1042 = Coupling(name = 'GC_1042',
                   value = '-((cw*ee*complex(0,1)*Rl22*complexconjugate(NN21))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) - (ee*complex(0,1)*Rl22*complexconjugate(NN22))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rl22*sw*complexconjugate(NN22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1043 = Coupling(name = 'GC_1043',
                   value = '-((cw*ee*complex(0,1)*Rn11*complexconjugate(NN21))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*Rn11*complexconjugate(NN22))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rn11*sw*complexconjugate(NN22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1044 = Coupling(name = 'GC_1044',
                   value = '-((cw*ee*complex(0,1)*Rn22*complexconjugate(NN21))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*Rn22*complexconjugate(NN22))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rn22*sw*complexconjugate(NN22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1045 = Coupling(name = 'GC_1045',
                   value = '-((cw*ee*complex(0,1)*Rn33*complexconjugate(NN21))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*Rn33*complexconjugate(NN22))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rn33*sw*complexconjugate(NN22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1046 = Coupling(name = 'GC_1046',
                   value = '(cw*ee*complex(0,1)*Ru11*complexconjugate(NN21))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Ru11*complexconjugate(NN22))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Ru11*sw*complexconjugate(NN22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1047 = Coupling(name = 'GC_1047',
                   value = '(cw*ee*complex(0,1)*Ru22*complexconjugate(NN21))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Ru22*complexconjugate(NN22))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Ru22*sw*complexconjugate(NN22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1048 = Coupling(name = 'GC_1048',
                   value = '(complex(0,1)*I14x33*complexconjugate(NN23))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I14x33*sw**2*complexconjugate(NN23))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*Rd33*complexconjugate(NN21))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rd33*complexconjugate(NN22))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rd33*sw*complexconjugate(NN22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1049 = Coupling(name = 'GC_1049',
                   value = '(complex(0,1)*I14x36*complexconjugate(NN23))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I14x36*sw**2*complexconjugate(NN23))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*Rd63*complexconjugate(NN21))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rd63*complexconjugate(NN22))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rd63*sw*complexconjugate(NN22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1050 = Coupling(name = 'GC_1050',
                   value = '(complex(0,1)*I50x33*complexconjugate(NN23))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I50x33*sw**2*complexconjugate(NN23))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*Rl33*complexconjugate(NN21))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rl33*complexconjugate(NN22))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rl33*sw*complexconjugate(NN22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1051 = Coupling(name = 'GC_1051',
                   value = '(complex(0,1)*I50x36*complexconjugate(NN23))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I50x36*sw**2*complexconjugate(NN23))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*Rl63*complexconjugate(NN21))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rl63*complexconjugate(NN22))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rl63*sw*complexconjugate(NN22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1052 = Coupling(name = 'GC_1052',
                   value = '-((ee*complex(0,1)*UU11*complexconjugate(NN22))/sw) - (ee*complex(0,1)*UU12*complexconjugate(NN23))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1053 = Coupling(name = 'GC_1053',
                   value = '-((ee*complex(0,1)*UU21*complexconjugate(NN22))/sw) - (ee*complex(0,1)*UU22*complexconjugate(NN23))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1054 = Coupling(name = 'GC_1054',
                   value = '-(cw*ee*complex(0,1)*NN13*complexconjugate(NN23))/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*NN14*complexconjugate(NN24))/(2.*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1})

GC_1055 = Coupling(name = 'GC_1055',
                   value = '-(cw*ee*complex(0,1)*NN23*complexconjugate(NN23))/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*NN24*complexconjugate(NN24))/(2.*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1})

GC_1056 = Coupling(name = 'GC_1056',
                   value = '(cw*ee*complex(0,1)*NN33*complexconjugate(NN23))/(2.*(-1 + sw)*sw*(1 + sw)) - (cw*ee*complex(0,1)*NN34*complexconjugate(NN24))/(2.*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1})

GC_1057 = Coupling(name = 'GC_1057',
                   value = '(cw*ee*complex(0,1)*NN43*complexconjugate(NN23))/(2.*(-1 + sw)*sw*(1 + sw)) - (cw*ee*complex(0,1)*NN44*complexconjugate(NN24))/(2.*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1})

GC_1058 = Coupling(name = 'GC_1058',
                   value = '(complex(0,1)*I132x33*complexconjugate(NN24))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I132x33*sw**2*complexconjugate(NN24))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*Ru33*complexconjugate(NN21))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Ru33*complexconjugate(NN22))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Ru33*sw*complexconjugate(NN22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1059 = Coupling(name = 'GC_1059',
                   value = '(complex(0,1)*I132x36*complexconjugate(NN24))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I132x36*sw**2*complexconjugate(NN24))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*Ru63*complexconjugate(NN21))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Ru63*complexconjugate(NN22))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Ru63*sw*complexconjugate(NN22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1060 = Coupling(name = 'GC_1060',
                   value = '-((ee*complex(0,1)*VV11*complexconjugate(NN22))/sw) + (ee*complex(0,1)*VV12*complexconjugate(NN24))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1061 = Coupling(name = 'GC_1061',
                   value = '-((ee*complex(0,1)*VV21*complexconjugate(NN22))/sw) + (ee*complex(0,1)*VV22*complexconjugate(NN24))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1062 = Coupling(name = 'GC_1062',
                   value = '(cw*ee*complex(0,1)*Rd11*complexconjugate(NN31))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rd11*complexconjugate(NN32))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rd11*sw*complexconjugate(NN32))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1063 = Coupling(name = 'GC_1063',
                   value = '(cw*ee*complex(0,1)*Rd22*complexconjugate(NN31))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rd22*complexconjugate(NN32))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rd22*sw*complexconjugate(NN32))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1064 = Coupling(name = 'GC_1064',
                   value = '-((cw*ee*complex(0,1)*Rl11*complexconjugate(NN31))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) - (ee*complex(0,1)*Rl11*complexconjugate(NN32))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rl11*sw*complexconjugate(NN32))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1065 = Coupling(name = 'GC_1065',
                   value = '-((cw*ee*complex(0,1)*Rl22*complexconjugate(NN31))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) - (ee*complex(0,1)*Rl22*complexconjugate(NN32))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rl22*sw*complexconjugate(NN32))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1066 = Coupling(name = 'GC_1066',
                   value = '-((cw*ee*complex(0,1)*Rn11*complexconjugate(NN31))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*Rn11*complexconjugate(NN32))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rn11*sw*complexconjugate(NN32))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1067 = Coupling(name = 'GC_1067',
                   value = '-((cw*ee*complex(0,1)*Rn22*complexconjugate(NN31))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*Rn22*complexconjugate(NN32))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rn22*sw*complexconjugate(NN32))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1068 = Coupling(name = 'GC_1068',
                   value = '-((cw*ee*complex(0,1)*Rn33*complexconjugate(NN31))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*Rn33*complexconjugate(NN32))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rn33*sw*complexconjugate(NN32))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1069 = Coupling(name = 'GC_1069',
                   value = '(cw*ee*complex(0,1)*Ru11*complexconjugate(NN31))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Ru11*complexconjugate(NN32))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Ru11*sw*complexconjugate(NN32))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1070 = Coupling(name = 'GC_1070',
                   value = '(cw*ee*complex(0,1)*Ru22*complexconjugate(NN31))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Ru22*complexconjugate(NN32))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Ru22*sw*complexconjugate(NN32))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1071 = Coupling(name = 'GC_1071',
                   value = '(complex(0,1)*I14x33*complexconjugate(NN33))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I14x33*sw**2*complexconjugate(NN33))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*Rd33*complexconjugate(NN31))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rd33*complexconjugate(NN32))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rd33*sw*complexconjugate(NN32))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1072 = Coupling(name = 'GC_1072',
                   value = '(complex(0,1)*I14x36*complexconjugate(NN33))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I14x36*sw**2*complexconjugate(NN33))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*Rd63*complexconjugate(NN31))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rd63*complexconjugate(NN32))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rd63*sw*complexconjugate(NN32))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1073 = Coupling(name = 'GC_1073',
                   value = '(complex(0,1)*I50x33*complexconjugate(NN33))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I50x33*sw**2*complexconjugate(NN33))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*Rl33*complexconjugate(NN31))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rl33*complexconjugate(NN32))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rl33*sw*complexconjugate(NN32))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1074 = Coupling(name = 'GC_1074',
                   value = '(complex(0,1)*I50x36*complexconjugate(NN33))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I50x36*sw**2*complexconjugate(NN33))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*Rl63*complexconjugate(NN31))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rl63*complexconjugate(NN32))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rl63*sw*complexconjugate(NN32))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1075 = Coupling(name = 'GC_1075',
                   value = '-((ee*complex(0,1)*UU11*complexconjugate(NN32))/sw) - (ee*complex(0,1)*UU12*complexconjugate(NN33))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1076 = Coupling(name = 'GC_1076',
                   value = '-((ee*complex(0,1)*UU21*complexconjugate(NN32))/sw) - (ee*complex(0,1)*UU22*complexconjugate(NN33))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1077 = Coupling(name = 'GC_1077',
                   value = '-(cw*ee*complex(0,1)*NN13*complexconjugate(NN33))/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*NN14*complexconjugate(NN34))/(2.*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1})

GC_1078 = Coupling(name = 'GC_1078',
                   value = '-(cw*ee*complex(0,1)*NN23*complexconjugate(NN33))/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*NN24*complexconjugate(NN34))/(2.*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1})

GC_1079 = Coupling(name = 'GC_1079',
                   value = '-(cw*ee*complex(0,1)*NN33*complexconjugate(NN33))/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*NN34*complexconjugate(NN34))/(2.*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1})

GC_1080 = Coupling(name = 'GC_1080',
                   value = '(cw*ee*complex(0,1)*NN43*complexconjugate(NN33))/(2.*(-1 + sw)*sw*(1 + sw)) - (cw*ee*complex(0,1)*NN44*complexconjugate(NN34))/(2.*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1})

GC_1081 = Coupling(name = 'GC_1081',
                   value = '(complex(0,1)*I132x33*complexconjugate(NN34))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I132x33*sw**2*complexconjugate(NN34))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*Ru33*complexconjugate(NN31))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Ru33*complexconjugate(NN32))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Ru33*sw*complexconjugate(NN32))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1082 = Coupling(name = 'GC_1082',
                   value = '(complex(0,1)*I132x36*complexconjugate(NN34))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I132x36*sw**2*complexconjugate(NN34))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*Ru63*complexconjugate(NN31))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Ru63*complexconjugate(NN32))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Ru63*sw*complexconjugate(NN32))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1083 = Coupling(name = 'GC_1083',
                   value = '-((ee*complex(0,1)*VV11*complexconjugate(NN32))/sw) + (ee*complex(0,1)*VV12*complexconjugate(NN34))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1084 = Coupling(name = 'GC_1084',
                   value = '-((ee*complex(0,1)*VV21*complexconjugate(NN32))/sw) + (ee*complex(0,1)*VV22*complexconjugate(NN34))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1085 = Coupling(name = 'GC_1085',
                   value = '(cw*ee*complex(0,1)*Rd11*complexconjugate(NN41))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rd11*complexconjugate(NN42))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rd11*sw*complexconjugate(NN42))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1086 = Coupling(name = 'GC_1086',
                   value = '(cw*ee*complex(0,1)*Rd22*complexconjugate(NN41))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rd22*complexconjugate(NN42))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rd22*sw*complexconjugate(NN42))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1087 = Coupling(name = 'GC_1087',
                   value = '-((cw*ee*complex(0,1)*Rl11*complexconjugate(NN41))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) - (ee*complex(0,1)*Rl11*complexconjugate(NN42))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rl11*sw*complexconjugate(NN42))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1088 = Coupling(name = 'GC_1088',
                   value = '-((cw*ee*complex(0,1)*Rl22*complexconjugate(NN41))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) - (ee*complex(0,1)*Rl22*complexconjugate(NN42))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rl22*sw*complexconjugate(NN42))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1089 = Coupling(name = 'GC_1089',
                   value = '-((cw*ee*complex(0,1)*Rn11*complexconjugate(NN41))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*Rn11*complexconjugate(NN42))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rn11*sw*complexconjugate(NN42))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1090 = Coupling(name = 'GC_1090',
                   value = '-((cw*ee*complex(0,1)*Rn22*complexconjugate(NN41))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*Rn22*complexconjugate(NN42))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rn22*sw*complexconjugate(NN42))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1091 = Coupling(name = 'GC_1091',
                   value = '-((cw*ee*complex(0,1)*Rn33*complexconjugate(NN41))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*Rn33*complexconjugate(NN42))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rn33*sw*complexconjugate(NN42))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1092 = Coupling(name = 'GC_1092',
                   value = '(cw*ee*complex(0,1)*Ru11*complexconjugate(NN41))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Ru11*complexconjugate(NN42))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Ru11*sw*complexconjugate(NN42))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1093 = Coupling(name = 'GC_1093',
                   value = '(cw*ee*complex(0,1)*Ru22*complexconjugate(NN41))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Ru22*complexconjugate(NN42))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Ru22*sw*complexconjugate(NN42))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1094 = Coupling(name = 'GC_1094',
                   value = '(complex(0,1)*I14x33*complexconjugate(NN43))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I14x33*sw**2*complexconjugate(NN43))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*Rd33*complexconjugate(NN41))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rd33*complexconjugate(NN42))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rd33*sw*complexconjugate(NN42))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1095 = Coupling(name = 'GC_1095',
                   value = '(complex(0,1)*I14x36*complexconjugate(NN43))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I14x36*sw**2*complexconjugate(NN43))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*Rd63*complexconjugate(NN41))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rd63*complexconjugate(NN42))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rd63*sw*complexconjugate(NN42))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1096 = Coupling(name = 'GC_1096',
                   value = '(complex(0,1)*I50x33*complexconjugate(NN43))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I50x33*sw**2*complexconjugate(NN43))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*Rl33*complexconjugate(NN41))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rl33*complexconjugate(NN42))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rl33*sw*complexconjugate(NN42))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1097 = Coupling(name = 'GC_1097',
                   value = '(complex(0,1)*I50x36*complexconjugate(NN43))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I50x36*sw**2*complexconjugate(NN43))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*Rl63*complexconjugate(NN41))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rl63*complexconjugate(NN42))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rl63*sw*complexconjugate(NN42))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1098 = Coupling(name = 'GC_1098',
                   value = '-((ee*complex(0,1)*UU11*complexconjugate(NN42))/sw) - (ee*complex(0,1)*UU12*complexconjugate(NN43))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1099 = Coupling(name = 'GC_1099',
                   value = '-((ee*complex(0,1)*UU21*complexconjugate(NN42))/sw) - (ee*complex(0,1)*UU22*complexconjugate(NN43))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1100 = Coupling(name = 'GC_1100',
                   value = '-(cw*ee*complex(0,1)*NN13*complexconjugate(NN43))/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*NN14*complexconjugate(NN44))/(2.*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1})

GC_1101 = Coupling(name = 'GC_1101',
                   value = '-(cw*ee*complex(0,1)*NN23*complexconjugate(NN43))/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*NN24*complexconjugate(NN44))/(2.*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1})

GC_1102 = Coupling(name = 'GC_1102',
                   value = '-(cw*ee*complex(0,1)*NN33*complexconjugate(NN43))/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*NN34*complexconjugate(NN44))/(2.*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1})

GC_1103 = Coupling(name = 'GC_1103',
                   value = '-(cw*ee*complex(0,1)*NN43*complexconjugate(NN43))/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*NN44*complexconjugate(NN44))/(2.*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1})

GC_1104 = Coupling(name = 'GC_1104',
                   value = '(complex(0,1)*I132x33*complexconjugate(NN44))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I132x33*sw**2*complexconjugate(NN44))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*Ru33*complexconjugate(NN41))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Ru33*complexconjugate(NN42))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Ru33*sw*complexconjugate(NN42))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1105 = Coupling(name = 'GC_1105',
                   value = '(complex(0,1)*I132x36*complexconjugate(NN44))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I132x36*sw**2*complexconjugate(NN44))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*Ru63*complexconjugate(NN41))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Ru63*complexconjugate(NN42))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Ru63*sw*complexconjugate(NN42))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1106 = Coupling(name = 'GC_1106',
                   value = '-((ee*complex(0,1)*VV11*complexconjugate(NN42))/sw) + (ee*complex(0,1)*VV12*complexconjugate(NN44))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1107 = Coupling(name = 'GC_1107',
                   value = '-((ee*complex(0,1)*VV21*complexconjugate(NN42))/sw) + (ee*complex(0,1)*VV22*complexconjugate(NN44))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1108 = Coupling(name = 'GC_1108',
                   value = '-(complex(0,1)*G*complexconjugate(Rd11)*cmath.sqrt(2))',
                   order = {'QCD':1})

GC_1109 = Coupling(name = 'GC_1109',
                   value = '(cw*ee*complex(0,1)*NN11*complexconjugate(Rd11))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN12*complexconjugate(Rd11))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN12*sw*complexconjugate(Rd11))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1110 = Coupling(name = 'GC_1110',
                   value = '(cw*ee*complex(0,1)*NN21*complexconjugate(Rd11))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN22*complexconjugate(Rd11))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN22*sw*complexconjugate(Rd11))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1111 = Coupling(name = 'GC_1111',
                   value = '(cw*ee*complex(0,1)*NN31*complexconjugate(Rd11))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN32*complexconjugate(Rd11))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN32*sw*complexconjugate(Rd11))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1112 = Coupling(name = 'GC_1112',
                   value = '(cw*ee*complex(0,1)*NN41*complexconjugate(Rd11))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN42*complexconjugate(Rd11))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN42*sw*complexconjugate(Rd11))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1113 = Coupling(name = 'GC_1113',
                   value = '-(complex(0,1)*G*complexconjugate(Rd22)*cmath.sqrt(2))',
                   order = {'QCD':1})

GC_1114 = Coupling(name = 'GC_1114',
                   value = '(cw*ee*complex(0,1)*NN11*complexconjugate(Rd22))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN12*complexconjugate(Rd22))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN12*sw*complexconjugate(Rd22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1115 = Coupling(name = 'GC_1115',
                   value = '(cw*ee*complex(0,1)*NN21*complexconjugate(Rd22))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN22*complexconjugate(Rd22))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN22*sw*complexconjugate(Rd22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1116 = Coupling(name = 'GC_1116',
                   value = '(cw*ee*complex(0,1)*NN31*complexconjugate(Rd22))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN32*complexconjugate(Rd22))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN32*sw*complexconjugate(Rd22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1117 = Coupling(name = 'GC_1117',
                   value = '(cw*ee*complex(0,1)*NN41*complexconjugate(Rd22))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN42*complexconjugate(Rd22))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN42*sw*complexconjugate(Rd22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1118 = Coupling(name = 'GC_1118',
                   value = '-(complex(0,1)*G*complexconjugate(Rd33)*cmath.sqrt(2))',
                   order = {'QCD':1})

GC_1119 = Coupling(name = 'GC_1119',
                   value = '(complex(0,1)*I6x33*NN13)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I6x33*NN13*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN11*complexconjugate(Rd33))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN12*complexconjugate(Rd33))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN12*sw*complexconjugate(Rd33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1120 = Coupling(name = 'GC_1120',
                   value = '(complex(0,1)*I6x33*NN23)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I6x33*NN23*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN21*complexconjugate(Rd33))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN22*complexconjugate(Rd33))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN22*sw*complexconjugate(Rd33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1121 = Coupling(name = 'GC_1121',
                   value = '(complex(0,1)*I6x33*NN33)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I6x33*NN33*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN31*complexconjugate(Rd33))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN32*complexconjugate(Rd33))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN32*sw*complexconjugate(Rd33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1122 = Coupling(name = 'GC_1122',
                   value = '(complex(0,1)*I6x33*NN43)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I6x33*NN43*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN41*complexconjugate(Rd33))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN42*complexconjugate(Rd33))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN42*sw*complexconjugate(Rd33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1123 = Coupling(name = 'GC_1123',
                   value = 'complex(0,1)*G*complexconjugate(Rd36)*cmath.sqrt(2)',
                   order = {'QCD':1})

GC_1124 = Coupling(name = 'GC_1124',
                   value = '(complex(0,1)*I7x33*complexconjugate(NN13))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I7x33*sw**2*complexconjugate(NN13))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN11)*complexconjugate(Rd36)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1125 = Coupling(name = 'GC_1125',
                   value = '(complex(0,1)*I7x33*complexconjugate(NN23))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I7x33*sw**2*complexconjugate(NN23))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN21)*complexconjugate(Rd36)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1126 = Coupling(name = 'GC_1126',
                   value = '(complex(0,1)*I7x33*complexconjugate(NN33))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I7x33*sw**2*complexconjugate(NN33))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN31)*complexconjugate(Rd36)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1127 = Coupling(name = 'GC_1127',
                   value = '(complex(0,1)*I7x33*complexconjugate(NN43))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I7x33*sw**2*complexconjugate(NN43))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN41)*complexconjugate(Rd36)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1128 = Coupling(name = 'GC_1128',
                   value = 'complex(0,1)*G*complexconjugate(Rd44)*cmath.sqrt(2)',
                   order = {'QCD':1})

GC_1129 = Coupling(name = 'GC_1129',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN11)*complexconjugate(Rd44)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1130 = Coupling(name = 'GC_1130',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN21)*complexconjugate(Rd44)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1131 = Coupling(name = 'GC_1131',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN31)*complexconjugate(Rd44)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1132 = Coupling(name = 'GC_1132',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN41)*complexconjugate(Rd44)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1133 = Coupling(name = 'GC_1133',
                   value = 'complex(0,1)*G*complexconjugate(Rd55)*cmath.sqrt(2)',
                   order = {'QCD':1})

GC_1134 = Coupling(name = 'GC_1134',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN11)*complexconjugate(Rd55)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1135 = Coupling(name = 'GC_1135',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN21)*complexconjugate(Rd55)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1136 = Coupling(name = 'GC_1136',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN31)*complexconjugate(Rd55)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1137 = Coupling(name = 'GC_1137',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN41)*complexconjugate(Rd55)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1138 = Coupling(name = 'GC_1138',
                   value = '-(complex(0,1)*G*complexconjugate(Rd63)*cmath.sqrt(2))',
                   order = {'QCD':1})

GC_1139 = Coupling(name = 'GC_1139',
                   value = '(complex(0,1)*I6x36*NN13)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I6x36*NN13*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN11*complexconjugate(Rd63))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN12*complexconjugate(Rd63))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN12*sw*complexconjugate(Rd63))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1140 = Coupling(name = 'GC_1140',
                   value = '(complex(0,1)*I6x36*NN23)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I6x36*NN23*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN21*complexconjugate(Rd63))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN22*complexconjugate(Rd63))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN22*sw*complexconjugate(Rd63))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1141 = Coupling(name = 'GC_1141',
                   value = '(complex(0,1)*I6x36*NN33)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I6x36*NN33*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN31*complexconjugate(Rd63))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN32*complexconjugate(Rd63))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN32*sw*complexconjugate(Rd63))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1142 = Coupling(name = 'GC_1142',
                   value = '(complex(0,1)*I6x36*NN43)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I6x36*NN43*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN41*complexconjugate(Rd63))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN42*complexconjugate(Rd63))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN42*sw*complexconjugate(Rd63))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1143 = Coupling(name = 'GC_1143',
                   value = 'complex(0,1)*G*complexconjugate(Rd66)*cmath.sqrt(2)',
                   order = {'QCD':1})

GC_1144 = Coupling(name = 'GC_1144',
                   value = '(complex(0,1)*I7x36*complexconjugate(NN13))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I7x36*sw**2*complexconjugate(NN13))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN11)*complexconjugate(Rd66)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1145 = Coupling(name = 'GC_1145',
                   value = '(complex(0,1)*I7x36*complexconjugate(NN23))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I7x36*sw**2*complexconjugate(NN23))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN21)*complexconjugate(Rd66)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1146 = Coupling(name = 'GC_1146',
                   value = '(complex(0,1)*I7x36*complexconjugate(NN33))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I7x36*sw**2*complexconjugate(NN33))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN31)*complexconjugate(Rd66)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1147 = Coupling(name = 'GC_1147',
                   value = '(complex(0,1)*I7x36*complexconjugate(NN43))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I7x36*sw**2*complexconjugate(NN43))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN41)*complexconjugate(Rd66)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1148 = Coupling(name = 'GC_1148',
                   value = '-((cw*ee*complex(0,1)*NN11*complexconjugate(Rl11))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) - (ee*complex(0,1)*NN12*complexconjugate(Rl11))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN12*sw*complexconjugate(Rl11))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1149 = Coupling(name = 'GC_1149',
                   value = '-((cw*ee*complex(0,1)*NN21*complexconjugate(Rl11))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) - (ee*complex(0,1)*NN22*complexconjugate(Rl11))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN22*sw*complexconjugate(Rl11))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1150 = Coupling(name = 'GC_1150',
                   value = '-((cw*ee*complex(0,1)*NN31*complexconjugate(Rl11))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) - (ee*complex(0,1)*NN32*complexconjugate(Rl11))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN32*sw*complexconjugate(Rl11))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1151 = Coupling(name = 'GC_1151',
                   value = '-((cw*ee*complex(0,1)*NN41*complexconjugate(Rl11))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) - (ee*complex(0,1)*NN42*complexconjugate(Rl11))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN42*sw*complexconjugate(Rl11))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1152 = Coupling(name = 'GC_1152',
                   value = '-((cw*ee*complex(0,1)*NN11*complexconjugate(Rl22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) - (ee*complex(0,1)*NN12*complexconjugate(Rl22))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN12*sw*complexconjugate(Rl22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1153 = Coupling(name = 'GC_1153',
                   value = '-((cw*ee*complex(0,1)*NN21*complexconjugate(Rl22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) - (ee*complex(0,1)*NN22*complexconjugate(Rl22))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN22*sw*complexconjugate(Rl22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1154 = Coupling(name = 'GC_1154',
                   value = '-((cw*ee*complex(0,1)*NN31*complexconjugate(Rl22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) - (ee*complex(0,1)*NN32*complexconjugate(Rl22))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN32*sw*complexconjugate(Rl22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1155 = Coupling(name = 'GC_1155',
                   value = '-((cw*ee*complex(0,1)*NN41*complexconjugate(Rl22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) - (ee*complex(0,1)*NN42*complexconjugate(Rl22))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN42*sw*complexconjugate(Rl22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1156 = Coupling(name = 'GC_1156',
                   value = '(complex(0,1)*I45x33*NN13)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I45x33*NN13*sw**2)/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN11*complexconjugate(Rl33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN12*complexconjugate(Rl33))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN12*sw*complexconjugate(Rl33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1157 = Coupling(name = 'GC_1157',
                   value = '(complex(0,1)*I45x33*NN23)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I45x33*NN23*sw**2)/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN21*complexconjugate(Rl33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN22*complexconjugate(Rl33))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN22*sw*complexconjugate(Rl33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1158 = Coupling(name = 'GC_1158',
                   value = '(complex(0,1)*I45x33*NN33)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I45x33*NN33*sw**2)/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN31*complexconjugate(Rl33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN32*complexconjugate(Rl33))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN32*sw*complexconjugate(Rl33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1159 = Coupling(name = 'GC_1159',
                   value = '(complex(0,1)*I45x33*NN43)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I45x33*NN43*sw**2)/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN41*complexconjugate(Rl33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN42*complexconjugate(Rl33))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN42*sw*complexconjugate(Rl33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1160 = Coupling(name = 'GC_1160',
                   value = '(complex(0,1)*I46x33*complexconjugate(NN13))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I46x33*sw**2*complexconjugate(NN13))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN11)*complexconjugate(Rl36)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1161 = Coupling(name = 'GC_1161',
                   value = '(complex(0,1)*I46x33*complexconjugate(NN23))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I46x33*sw**2*complexconjugate(NN23))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN21)*complexconjugate(Rl36)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1162 = Coupling(name = 'GC_1162',
                   value = '(complex(0,1)*I46x33*complexconjugate(NN33))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I46x33*sw**2*complexconjugate(NN33))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN31)*complexconjugate(Rl36)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1163 = Coupling(name = 'GC_1163',
                   value = '(complex(0,1)*I46x33*complexconjugate(NN43))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I46x33*sw**2*complexconjugate(NN43))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN41)*complexconjugate(Rl36)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1164 = Coupling(name = 'GC_1164',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN11)*complexconjugate(Rl44)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1165 = Coupling(name = 'GC_1165',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN21)*complexconjugate(Rl44)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1166 = Coupling(name = 'GC_1166',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN31)*complexconjugate(Rl44)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1167 = Coupling(name = 'GC_1167',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN41)*complexconjugate(Rl44)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1168 = Coupling(name = 'GC_1168',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN11)*complexconjugate(Rl55)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1169 = Coupling(name = 'GC_1169',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN21)*complexconjugate(Rl55)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1170 = Coupling(name = 'GC_1170',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN31)*complexconjugate(Rl55)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1171 = Coupling(name = 'GC_1171',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN41)*complexconjugate(Rl55)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1172 = Coupling(name = 'GC_1172',
                   value = '(complex(0,1)*I45x36*NN13)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I45x36*NN13*sw**2)/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN11*complexconjugate(Rl63))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN12*complexconjugate(Rl63))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN12*sw*complexconjugate(Rl63))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1173 = Coupling(name = 'GC_1173',
                   value = '(complex(0,1)*I45x36*NN23)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I45x36*NN23*sw**2)/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN21*complexconjugate(Rl63))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN22*complexconjugate(Rl63))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN22*sw*complexconjugate(Rl63))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1174 = Coupling(name = 'GC_1174',
                   value = '(complex(0,1)*I45x36*NN33)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I45x36*NN33*sw**2)/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN31*complexconjugate(Rl63))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN32*complexconjugate(Rl63))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN32*sw*complexconjugate(Rl63))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1175 = Coupling(name = 'GC_1175',
                   value = '(complex(0,1)*I45x36*NN43)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I45x36*NN43*sw**2)/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN41*complexconjugate(Rl63))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN42*complexconjugate(Rl63))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN42*sw*complexconjugate(Rl63))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1176 = Coupling(name = 'GC_1176',
                   value = '(complex(0,1)*I46x36*complexconjugate(NN13))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I46x36*sw**2*complexconjugate(NN13))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN11)*complexconjugate(Rl66)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1177 = Coupling(name = 'GC_1177',
                   value = '(complex(0,1)*I46x36*complexconjugate(NN23))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I46x36*sw**2*complexconjugate(NN23))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN21)*complexconjugate(Rl66)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1178 = Coupling(name = 'GC_1178',
                   value = '(complex(0,1)*I46x36*complexconjugate(NN33))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I46x36*sw**2*complexconjugate(NN33))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN31)*complexconjugate(Rl66)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1179 = Coupling(name = 'GC_1179',
                   value = '(complex(0,1)*I46x36*complexconjugate(NN43))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I46x36*sw**2*complexconjugate(NN43))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN41)*complexconjugate(Rl66)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1180 = Coupling(name = 'GC_1180',
                   value = '-((cw*ee*complex(0,1)*NN11*complexconjugate(Rn11))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*NN12*complexconjugate(Rn11))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN12*sw*complexconjugate(Rn11))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1181 = Coupling(name = 'GC_1181',
                   value = '-((cw*ee*complex(0,1)*NN21*complexconjugate(Rn11))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*NN22*complexconjugate(Rn11))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN22*sw*complexconjugate(Rn11))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1182 = Coupling(name = 'GC_1182',
                   value = '-((cw*ee*complex(0,1)*NN31*complexconjugate(Rn11))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*NN32*complexconjugate(Rn11))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN32*sw*complexconjugate(Rn11))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1183 = Coupling(name = 'GC_1183',
                   value = '-((cw*ee*complex(0,1)*NN41*complexconjugate(Rn11))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*NN42*complexconjugate(Rn11))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN42*sw*complexconjugate(Rn11))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1184 = Coupling(name = 'GC_1184',
                   value = '-((cw*ee*complex(0,1)*NN11*complexconjugate(Rn22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*NN12*complexconjugate(Rn22))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN12*sw*complexconjugate(Rn22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1185 = Coupling(name = 'GC_1185',
                   value = '-((cw*ee*complex(0,1)*NN21*complexconjugate(Rn22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*NN22*complexconjugate(Rn22))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN22*sw*complexconjugate(Rn22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1186 = Coupling(name = 'GC_1186',
                   value = '-((cw*ee*complex(0,1)*NN31*complexconjugate(Rn22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*NN32*complexconjugate(Rn22))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN32*sw*complexconjugate(Rn22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1187 = Coupling(name = 'GC_1187',
                   value = '-((cw*ee*complex(0,1)*NN41*complexconjugate(Rn22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*NN42*complexconjugate(Rn22))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN42*sw*complexconjugate(Rn22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1188 = Coupling(name = 'GC_1188',
                   value = '-((cw*ee*complex(0,1)*NN11*complexconjugate(Rn33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*NN12*complexconjugate(Rn33))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN12*sw*complexconjugate(Rn33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1189 = Coupling(name = 'GC_1189',
                   value = '-((cw*ee*complex(0,1)*NN21*complexconjugate(Rn33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*NN22*complexconjugate(Rn33))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN22*sw*complexconjugate(Rn33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1190 = Coupling(name = 'GC_1190',
                   value = '-((cw*ee*complex(0,1)*NN31*complexconjugate(Rn33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*NN32*complexconjugate(Rn33))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN32*sw*complexconjugate(Rn33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1191 = Coupling(name = 'GC_1191',
                   value = '-((cw*ee*complex(0,1)*NN41*complexconjugate(Rn33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*NN42*complexconjugate(Rn33))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN42*sw*complexconjugate(Rn33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1192 = Coupling(name = 'GC_1192',
                   value = '-(complex(0,1)*G*complexconjugate(Ru11)*cmath.sqrt(2))',
                   order = {'QCD':1})

GC_1193 = Coupling(name = 'GC_1193',
                   value = '(cw*ee*complex(0,1)*NN11*complexconjugate(Ru11))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN12*complexconjugate(Ru11))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN12*sw*complexconjugate(Ru11))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1194 = Coupling(name = 'GC_1194',
                   value = '(cw*ee*complex(0,1)*NN21*complexconjugate(Ru11))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN22*complexconjugate(Ru11))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN22*sw*complexconjugate(Ru11))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1195 = Coupling(name = 'GC_1195',
                   value = '(cw*ee*complex(0,1)*NN31*complexconjugate(Ru11))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN32*complexconjugate(Ru11))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN32*sw*complexconjugate(Ru11))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1196 = Coupling(name = 'GC_1196',
                   value = '(cw*ee*complex(0,1)*NN41*complexconjugate(Ru11))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN42*complexconjugate(Ru11))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN42*sw*complexconjugate(Ru11))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1197 = Coupling(name = 'GC_1197',
                   value = '-(complex(0,1)*G*complexconjugate(Ru22)*cmath.sqrt(2))',
                   order = {'QCD':1})

GC_1198 = Coupling(name = 'GC_1198',
                   value = '(cw*ee*complex(0,1)*NN11*complexconjugate(Ru22))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN12*complexconjugate(Ru22))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN12*sw*complexconjugate(Ru22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1199 = Coupling(name = 'GC_1199',
                   value = '(cw*ee*complex(0,1)*NN21*complexconjugate(Ru22))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN22*complexconjugate(Ru22))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN22*sw*complexconjugate(Ru22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1200 = Coupling(name = 'GC_1200',
                   value = '(cw*ee*complex(0,1)*NN31*complexconjugate(Ru22))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN32*complexconjugate(Ru22))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN32*sw*complexconjugate(Ru22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1201 = Coupling(name = 'GC_1201',
                   value = '(cw*ee*complex(0,1)*NN41*complexconjugate(Ru22))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN42*complexconjugate(Ru22))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN42*sw*complexconjugate(Ru22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1202 = Coupling(name = 'GC_1202',
                   value = '-(complex(0,1)*G*complexconjugate(Ru33)*cmath.sqrt(2))',
                   order = {'QCD':1})

GC_1203 = Coupling(name = 'GC_1203',
                   value = '(complex(0,1)*I111x33*NN14)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I111x33*NN14*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN11*complexconjugate(Ru33))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN12*complexconjugate(Ru33))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN12*sw*complexconjugate(Ru33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1204 = Coupling(name = 'GC_1204',
                   value = '(complex(0,1)*I111x33*NN24)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I111x33*NN24*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN21*complexconjugate(Ru33))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN22*complexconjugate(Ru33))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN22*sw*complexconjugate(Ru33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1205 = Coupling(name = 'GC_1205',
                   value = '(complex(0,1)*I111x33*NN34)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I111x33*NN34*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN31*complexconjugate(Ru33))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN32*complexconjugate(Ru33))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN32*sw*complexconjugate(Ru33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1206 = Coupling(name = 'GC_1206',
                   value = '(complex(0,1)*I111x33*NN44)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I111x33*NN44*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN41*complexconjugate(Ru33))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN42*complexconjugate(Ru33))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN42*sw*complexconjugate(Ru33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1207 = Coupling(name = 'GC_1207',
                   value = 'complex(0,1)*G*complexconjugate(Ru36)*cmath.sqrt(2)',
                   order = {'QCD':1})

GC_1208 = Coupling(name = 'GC_1208',
                   value = '(complex(0,1)*I112x33*complexconjugate(NN14))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I112x33*sw**2*complexconjugate(NN14))/((-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*complexconjugate(NN11)*complexconjugate(Ru36)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1209 = Coupling(name = 'GC_1209',
                   value = '(complex(0,1)*I112x33*complexconjugate(NN24))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I112x33*sw**2*complexconjugate(NN24))/((-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*complexconjugate(NN21)*complexconjugate(Ru36)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1210 = Coupling(name = 'GC_1210',
                   value = '(complex(0,1)*I112x33*complexconjugate(NN34))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I112x33*sw**2*complexconjugate(NN34))/((-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*complexconjugate(NN31)*complexconjugate(Ru36)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1211 = Coupling(name = 'GC_1211',
                   value = '(complex(0,1)*I112x33*complexconjugate(NN44))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I112x33*sw**2*complexconjugate(NN44))/((-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*complexconjugate(NN41)*complexconjugate(Ru36)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1212 = Coupling(name = 'GC_1212',
                   value = 'complex(0,1)*G*complexconjugate(Ru44)*cmath.sqrt(2)',
                   order = {'QCD':1})

GC_1213 = Coupling(name = 'GC_1213',
                   value = '(-2*cw*ee*complex(0,1)*complexconjugate(NN11)*complexconjugate(Ru44)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1214 = Coupling(name = 'GC_1214',
                   value = '(-2*cw*ee*complex(0,1)*complexconjugate(NN21)*complexconjugate(Ru44)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1215 = Coupling(name = 'GC_1215',
                   value = '(-2*cw*ee*complex(0,1)*complexconjugate(NN31)*complexconjugate(Ru44)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1216 = Coupling(name = 'GC_1216',
                   value = '(-2*cw*ee*complex(0,1)*complexconjugate(NN41)*complexconjugate(Ru44)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1217 = Coupling(name = 'GC_1217',
                   value = 'complex(0,1)*G*complexconjugate(Ru55)*cmath.sqrt(2)',
                   order = {'QCD':1})

GC_1218 = Coupling(name = 'GC_1218',
                   value = '(-2*cw*ee*complex(0,1)*complexconjugate(NN11)*complexconjugate(Ru55)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1219 = Coupling(name = 'GC_1219',
                   value = '(-2*cw*ee*complex(0,1)*complexconjugate(NN21)*complexconjugate(Ru55)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1220 = Coupling(name = 'GC_1220',
                   value = '(-2*cw*ee*complex(0,1)*complexconjugate(NN31)*complexconjugate(Ru55)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1221 = Coupling(name = 'GC_1221',
                   value = '(-2*cw*ee*complex(0,1)*complexconjugate(NN41)*complexconjugate(Ru55)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1222 = Coupling(name = 'GC_1222',
                   value = '-(complex(0,1)*G*complexconjugate(Ru63)*cmath.sqrt(2))',
                   order = {'QCD':1})

GC_1223 = Coupling(name = 'GC_1223',
                   value = '(complex(0,1)*I111x36*NN14)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I111x36*NN14*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN11*complexconjugate(Ru63))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN12*complexconjugate(Ru63))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN12*sw*complexconjugate(Ru63))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1224 = Coupling(name = 'GC_1224',
                   value = '(complex(0,1)*I111x36*NN24)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I111x36*NN24*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN21*complexconjugate(Ru63))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN22*complexconjugate(Ru63))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN22*sw*complexconjugate(Ru63))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1225 = Coupling(name = 'GC_1225',
                   value = '(complex(0,1)*I111x36*NN34)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I111x36*NN34*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN31*complexconjugate(Ru63))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN32*complexconjugate(Ru63))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN32*sw*complexconjugate(Ru63))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1226 = Coupling(name = 'GC_1226',
                   value = '(complex(0,1)*I111x36*NN44)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I111x36*NN44*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN41*complexconjugate(Ru63))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN42*complexconjugate(Ru63))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN42*sw*complexconjugate(Ru63))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1227 = Coupling(name = 'GC_1227',
                   value = 'complex(0,1)*G*complexconjugate(Ru66)*cmath.sqrt(2)',
                   order = {'QCD':1})

GC_1228 = Coupling(name = 'GC_1228',
                   value = '(complex(0,1)*I112x36*complexconjugate(NN14))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I112x36*sw**2*complexconjugate(NN14))/((-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*complexconjugate(NN11)*complexconjugate(Ru66)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1229 = Coupling(name = 'GC_1229',
                   value = '(complex(0,1)*I112x36*complexconjugate(NN24))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I112x36*sw**2*complexconjugate(NN24))/((-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*complexconjugate(NN21)*complexconjugate(Ru66)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1230 = Coupling(name = 'GC_1230',
                   value = '(complex(0,1)*I112x36*complexconjugate(NN34))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I112x36*sw**2*complexconjugate(NN34))/((-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*complexconjugate(NN31)*complexconjugate(Ru66)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1231 = Coupling(name = 'GC_1231',
                   value = '(complex(0,1)*I112x36*complexconjugate(NN44))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I112x36*sw**2*complexconjugate(NN44))/((-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*complexconjugate(NN41)*complexconjugate(Ru66)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1232 = Coupling(name = 'GC_1232',
                   value = '-((ee*complex(0,1)*I10x11*complexconjugate(UU11))/sw)',
                   order = {'QED':1})

GC_1233 = Coupling(name = 'GC_1233',
                   value = '-((ee*complex(0,1)*I10x22*complexconjugate(UU11))/sw)',
                   order = {'QED':1})

GC_1234 = Coupling(name = 'GC_1234',
                   value = '-((ee*complex(0,1)*I51x11*complexconjugate(UU11))/sw)',
                   order = {'QED':1})

GC_1235 = Coupling(name = 'GC_1235',
                   value = '-((ee*complex(0,1)*I51x22*complexconjugate(UU11))/sw)',
                   order = {'QED':1})

GC_1236 = Coupling(name = 'GC_1236',
                   value = 'complex(0,1)*I193x33*complexconjugate(UU12)',
                   order = {'QED':1})

GC_1237 = Coupling(name = 'GC_1237',
                   value = 'complex(0,1)*I196x33*complexconjugate(UU12)',
                   order = {'QED':1})

GC_1238 = Coupling(name = 'GC_1238',
                   value = 'complex(0,1)*I196x36*complexconjugate(UU12)',
                   order = {'QED':1})

GC_1239 = Coupling(name = 'GC_1239',
                   value = '-((ee*complex(0,1)*I10x33*complexconjugate(UU11))/sw) + complex(0,1)*I12x33*complexconjugate(UU12)',
                   order = {'QED':1})

GC_1240 = Coupling(name = 'GC_1240',
                   value = '-((ee*complex(0,1)*I10x36*complexconjugate(UU11))/sw) + complex(0,1)*I12x36*complexconjugate(UU12)',
                   order = {'QED':1})

GC_1241 = Coupling(name = 'GC_1241',
                   value = '-((ee*complex(0,1)*I51x33*complexconjugate(UU11))/sw) + complex(0,1)*I52x33*complexconjugate(UU12)',
                   order = {'QED':1})

GC_1242 = Coupling(name = 'GC_1242',
                   value = '-((ee*complex(0,1)*I51x36*complexconjugate(UU11))/sw) + complex(0,1)*I52x36*complexconjugate(UU12)',
                   order = {'QED':1})

GC_1243 = Coupling(name = 'GC_1243',
                   value = '-((ee*complex(0,1)*NN12*complexconjugate(UU11))/sw) - (ee*complex(0,1)*NN13*complexconjugate(UU12))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1244 = Coupling(name = 'GC_1244',
                   value = '-((ee*complex(0,1)*NN22*complexconjugate(UU11))/sw) - (ee*complex(0,1)*NN23*complexconjugate(UU12))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1245 = Coupling(name = 'GC_1245',
                   value = '-((ee*complex(0,1)*NN32*complexconjugate(UU11))/sw) - (ee*complex(0,1)*NN33*complexconjugate(UU12))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1246 = Coupling(name = 'GC_1246',
                   value = '-((ee*complex(0,1)*NN42*complexconjugate(UU11))/sw) - (ee*complex(0,1)*NN43*complexconjugate(UU12))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1247 = Coupling(name = 'GC_1247',
                   value = 'ee*complex(0,1)*UU11*complexconjugate(UU11) + ee*complex(0,1)*UU12*complexconjugate(UU12)',
                   order = {'QED':1})

GC_1248 = Coupling(name = 'GC_1248',
                   value = '-((cw*ee*complex(0,1)*UU11*complexconjugate(UU11))/((-1 + sw)*sw*(1 + sw))) + (cw*ee*complex(0,1)*sw*UU11*complexconjugate(UU11))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*UU12*complexconjugate(UU12))/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*sw*UU12*complexconjugate(UU12))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1249 = Coupling(name = 'GC_1249',
                   value = 'ee*complex(0,1)*UU21*complexconjugate(UU11) + ee*complex(0,1)*UU22*complexconjugate(UU12)',
                   order = {'QED':1})

GC_1250 = Coupling(name = 'GC_1250',
                   value = '-((cw*ee*complex(0,1)*UU21*complexconjugate(UU11))/((-1 + sw)*sw*(1 + sw))) + (cw*ee*complex(0,1)*sw*UU21*complexconjugate(UU11))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*UU22*complexconjugate(UU12))/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*sw*UU22*complexconjugate(UU12))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1251 = Coupling(name = 'GC_1251',
                   value = '-((ee*complex(0,1)*I10x11*complexconjugate(UU21))/sw)',
                   order = {'QED':1})

GC_1252 = Coupling(name = 'GC_1252',
                   value = '-((ee*complex(0,1)*I10x22*complexconjugate(UU21))/sw)',
                   order = {'QED':1})

GC_1253 = Coupling(name = 'GC_1253',
                   value = '-((ee*complex(0,1)*I51x11*complexconjugate(UU21))/sw)',
                   order = {'QED':1})

GC_1254 = Coupling(name = 'GC_1254',
                   value = '-((ee*complex(0,1)*I51x22*complexconjugate(UU21))/sw)',
                   order = {'QED':1})

GC_1255 = Coupling(name = 'GC_1255',
                   value = 'complex(0,1)*I193x33*complexconjugate(UU22)',
                   order = {'QED':1})

GC_1256 = Coupling(name = 'GC_1256',
                   value = 'complex(0,1)*I196x33*complexconjugate(UU22)',
                   order = {'QED':1})

GC_1257 = Coupling(name = 'GC_1257',
                   value = 'complex(0,1)*I196x36*complexconjugate(UU22)',
                   order = {'QED':1})

GC_1258 = Coupling(name = 'GC_1258',
                   value = '-((ee*complex(0,1)*I10x33*complexconjugate(UU21))/sw) + complex(0,1)*I12x33*complexconjugate(UU22)',
                   order = {'QED':1})

GC_1259 = Coupling(name = 'GC_1259',
                   value = '-((ee*complex(0,1)*I10x36*complexconjugate(UU21))/sw) + complex(0,1)*I12x36*complexconjugate(UU22)',
                   order = {'QED':1})

GC_1260 = Coupling(name = 'GC_1260',
                   value = '-((ee*complex(0,1)*I51x33*complexconjugate(UU21))/sw) + complex(0,1)*I52x33*complexconjugate(UU22)',
                   order = {'QED':1})

GC_1261 = Coupling(name = 'GC_1261',
                   value = '-((ee*complex(0,1)*I51x36*complexconjugate(UU21))/sw) + complex(0,1)*I52x36*complexconjugate(UU22)',
                   order = {'QED':1})

GC_1262 = Coupling(name = 'GC_1262',
                   value = '-((ee*complex(0,1)*NN12*complexconjugate(UU21))/sw) - (ee*complex(0,1)*NN13*complexconjugate(UU22))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1263 = Coupling(name = 'GC_1263',
                   value = '-((ee*complex(0,1)*NN22*complexconjugate(UU21))/sw) - (ee*complex(0,1)*NN23*complexconjugate(UU22))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1264 = Coupling(name = 'GC_1264',
                   value = '-((ee*complex(0,1)*NN32*complexconjugate(UU21))/sw) - (ee*complex(0,1)*NN33*complexconjugate(UU22))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1265 = Coupling(name = 'GC_1265',
                   value = '-((ee*complex(0,1)*NN42*complexconjugate(UU21))/sw) - (ee*complex(0,1)*NN43*complexconjugate(UU22))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1266 = Coupling(name = 'GC_1266',
                   value = 'ee*complex(0,1)*UU11*complexconjugate(UU21) + ee*complex(0,1)*UU12*complexconjugate(UU22)',
                   order = {'QED':1})

GC_1267 = Coupling(name = 'GC_1267',
                   value = '-((cw*ee*complex(0,1)*UU11*complexconjugate(UU21))/((-1 + sw)*sw*(1 + sw))) + (cw*ee*complex(0,1)*sw*UU11*complexconjugate(UU21))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*UU12*complexconjugate(UU22))/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*sw*UU12*complexconjugate(UU22))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1268 = Coupling(name = 'GC_1268',
                   value = 'ee*complex(0,1)*UU21*complexconjugate(UU21) + ee*complex(0,1)*UU22*complexconjugate(UU22)',
                   order = {'QED':1})

GC_1269 = Coupling(name = 'GC_1269',
                   value = '-((cw*ee*complex(0,1)*UU21*complexconjugate(UU21))/((-1 + sw)*sw*(1 + sw))) + (cw*ee*complex(0,1)*sw*UU21*complexconjugate(UU21))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*UU22*complexconjugate(UU22))/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*sw*UU22*complexconjugate(UU22))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1270 = Coupling(name = 'GC_1270',
                   value = '-((ee*complex(0,1)*I133x11*complexconjugate(VV11))/sw)',
                   order = {'QED':1})

GC_1271 = Coupling(name = 'GC_1271',
                   value = '-((ee*complex(0,1)*I133x22*complexconjugate(VV11))/sw)',
                   order = {'QED':1})

GC_1272 = Coupling(name = 'GC_1272',
                   value = '-((ee*complex(0,1)*I96x11*complexconjugate(VV11))/sw)',
                   order = {'QED':1})

GC_1273 = Coupling(name = 'GC_1273',
                   value = '-((ee*complex(0,1)*I96x22*complexconjugate(VV11))/sw)',
                   order = {'QED':1})

GC_1274 = Coupling(name = 'GC_1274',
                   value = '-((ee*complex(0,1)*I96x33*complexconjugate(VV11))/sw)',
                   order = {'QED':1})

GC_1275 = Coupling(name = 'GC_1275',
                   value = 'complex(0,1)*I189x33*complexconjugate(VV12)',
                   order = {'QED':1})

GC_1276 = Coupling(name = 'GC_1276',
                   value = 'complex(0,1)*I189x36*complexconjugate(VV12)',
                   order = {'QED':1})

GC_1277 = Coupling(name = 'GC_1277',
                   value = '-((ee*complex(0,1)*I133x33*complexconjugate(VV11))/sw) + complex(0,1)*I135x33*complexconjugate(VV12)',
                   order = {'QED':1})

GC_1278 = Coupling(name = 'GC_1278',
                   value = '-((ee*complex(0,1)*I133x36*complexconjugate(VV11))/sw) + complex(0,1)*I135x36*complexconjugate(VV12)',
                   order = {'QED':1})

GC_1279 = Coupling(name = 'GC_1279',
                   value = '-((ee*complex(0,1)*NN12*complexconjugate(VV11))/sw) + (ee*complex(0,1)*NN14*complexconjugate(VV12))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1280 = Coupling(name = 'GC_1280',
                   value = '-((ee*complex(0,1)*NN22*complexconjugate(VV11))/sw) + (ee*complex(0,1)*NN24*complexconjugate(VV12))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1281 = Coupling(name = 'GC_1281',
                   value = '-((ee*complex(0,1)*NN32*complexconjugate(VV11))/sw) + (ee*complex(0,1)*NN34*complexconjugate(VV12))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1282 = Coupling(name = 'GC_1282',
                   value = '-((ee*complex(0,1)*NN42*complexconjugate(VV11))/sw) + (ee*complex(0,1)*NN44*complexconjugate(VV12))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1283 = Coupling(name = 'GC_1283',
                   value = 'ee*complex(0,1)*VV11*complexconjugate(VV11) + ee*complex(0,1)*VV12*complexconjugate(VV12)',
                   order = {'QED':1})

GC_1284 = Coupling(name = 'GC_1284',
                   value = '-((cw*ee*complex(0,1)*VV11*complexconjugate(VV11))/((-1 + sw)*sw*(1 + sw))) + (cw*ee*complex(0,1)*sw*VV11*complexconjugate(VV11))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*VV12*complexconjugate(VV12))/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*sw*VV12*complexconjugate(VV12))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1285 = Coupling(name = 'GC_1285',
                   value = 'ee*complex(0,1)*VV21*complexconjugate(VV11) + ee*complex(0,1)*VV22*complexconjugate(VV12)',
                   order = {'QED':1})

GC_1286 = Coupling(name = 'GC_1286',
                   value = '-((cw*ee*complex(0,1)*VV21*complexconjugate(VV11))/((-1 + sw)*sw*(1 + sw))) + (cw*ee*complex(0,1)*sw*VV21*complexconjugate(VV11))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*VV22*complexconjugate(VV12))/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*sw*VV22*complexconjugate(VV12))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1287 = Coupling(name = 'GC_1287',
                   value = '-((ee*complex(0,1)*I133x11*complexconjugate(VV21))/sw)',
                   order = {'QED':1})

GC_1288 = Coupling(name = 'GC_1288',
                   value = '-((ee*complex(0,1)*I133x22*complexconjugate(VV21))/sw)',
                   order = {'QED':1})

GC_1289 = Coupling(name = 'GC_1289',
                   value = '-((ee*complex(0,1)*I96x11*complexconjugate(VV21))/sw)',
                   order = {'QED':1})

GC_1290 = Coupling(name = 'GC_1290',
                   value = '-((ee*complex(0,1)*I96x22*complexconjugate(VV21))/sw)',
                   order = {'QED':1})

GC_1291 = Coupling(name = 'GC_1291',
                   value = '-((ee*complex(0,1)*I96x33*complexconjugate(VV21))/sw)',
                   order = {'QED':1})

GC_1292 = Coupling(name = 'GC_1292',
                   value = 'complex(0,1)*I189x33*complexconjugate(VV22)',
                   order = {'QED':1})

GC_1293 = Coupling(name = 'GC_1293',
                   value = 'complex(0,1)*I189x36*complexconjugate(VV22)',
                   order = {'QED':1})

GC_1294 = Coupling(name = 'GC_1294',
                   value = '-((ee*complex(0,1)*I133x33*complexconjugate(VV21))/sw) + complex(0,1)*I135x33*complexconjugate(VV22)',
                   order = {'QED':1})

GC_1295 = Coupling(name = 'GC_1295',
                   value = '-((ee*complex(0,1)*I133x36*complexconjugate(VV21))/sw) + complex(0,1)*I135x36*complexconjugate(VV22)',
                   order = {'QED':1})

GC_1296 = Coupling(name = 'GC_1296',
                   value = '-((ee*complex(0,1)*NN12*complexconjugate(VV21))/sw) + (ee*complex(0,1)*NN14*complexconjugate(VV22))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1297 = Coupling(name = 'GC_1297',
                   value = '-((ee*complex(0,1)*NN22*complexconjugate(VV21))/sw) + (ee*complex(0,1)*NN24*complexconjugate(VV22))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1298 = Coupling(name = 'GC_1298',
                   value = '-((ee*complex(0,1)*NN32*complexconjugate(VV21))/sw) + (ee*complex(0,1)*NN34*complexconjugate(VV22))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1299 = Coupling(name = 'GC_1299',
                   value = '-((ee*complex(0,1)*NN42*complexconjugate(VV21))/sw) + (ee*complex(0,1)*NN44*complexconjugate(VV22))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1300 = Coupling(name = 'GC_1300',
                   value = 'ee*complex(0,1)*VV11*complexconjugate(VV21) + ee*complex(0,1)*VV12*complexconjugate(VV22)',
                   order = {'QED':1})

GC_1301 = Coupling(name = 'GC_1301',
                   value = '-((cw*ee*complex(0,1)*VV11*complexconjugate(VV21))/((-1 + sw)*sw*(1 + sw))) + (cw*ee*complex(0,1)*sw*VV11*complexconjugate(VV21))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*VV12*complexconjugate(VV22))/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*sw*VV12*complexconjugate(VV22))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1302 = Coupling(name = 'GC_1302',
                   value = 'ee*complex(0,1)*VV21*complexconjugate(VV21) + ee*complex(0,1)*VV22*complexconjugate(VV22)',
                   order = {'QED':1})

GC_1303 = Coupling(name = 'GC_1303',
                   value = '-((cw*ee*complex(0,1)*VV21*complexconjugate(VV21))/((-1 + sw)*sw*(1 + sw))) + (cw*ee*complex(0,1)*sw*VV21*complexconjugate(VV21))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*VV22*complexconjugate(VV22))/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*sw*VV22*complexconjugate(VV22))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1304 = Coupling(name = 'GC_1304',
                   value = '-((complex(0,1)*yd33*cmath.cos(alp))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1305 = Coupling(name = 'GC_1305',
                   value = '-((complex(0,1)*ye33*cmath.cos(alp))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1306 = Coupling(name = 'GC_1306',
                   value = '-((complex(0,1)*yu33*cmath.cos(alp))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1307 = Coupling(name = 'GC_1307',
                   value = '-((complex(0,1)*complexconjugate(yd33)*cmath.cos(alp))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1308 = Coupling(name = 'GC_1308',
                   value = '-((complex(0,1)*complexconjugate(ye33)*cmath.cos(alp))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1309 = Coupling(name = 'GC_1309',
                   value = '-((complex(0,1)*complexconjugate(yu33)*cmath.cos(alp))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1310 = Coupling(name = 'GC_1310',
                   value = 'complex(0,1)*I1x33*cmath.cos(beta)',
                   order = {'QED':1})

GC_1311 = Coupling(name = 'GC_1311',
                   value = '-(complex(0,1)*I202x33*cmath.cos(beta))',
                   order = {'QED':1})

GC_1312 = Coupling(name = 'GC_1312',
                   value = '-(complex(0,1)*I2x33*cmath.cos(beta))',
                   order = {'QED':1})

GC_1313 = Coupling(name = 'GC_1313',
                   value = '-(complex(0,1)*I3x33*cmath.cos(beta))',
                   order = {'QED':1})

GC_1314 = Coupling(name = 'GC_1314',
                   value = 'complex(0,1)*I4x33*cmath.cos(beta)',
                   order = {'QED':1})

GC_1315 = Coupling(name = 'GC_1315',
                   value = '-(complex(0,1)*I5x33*cmath.cos(beta))',
                   order = {'QED':1})

GC_1316 = Coupling(name = 'GC_1316',
                   value = '-((yd33*cmath.cos(beta))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1317 = Coupling(name = 'GC_1317',
                   value = '-((ye33*cmath.cos(beta))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1318 = Coupling(name = 'GC_1318',
                   value = '(yu33*cmath.cos(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1319 = Coupling(name = 'GC_1319',
                   value = '(complexconjugate(yd33)*cmath.cos(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1320 = Coupling(name = 'GC_1320',
                   value = '(complexconjugate(ye33)*cmath.cos(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1321 = Coupling(name = 'GC_1321',
                   value = '-((complexconjugate(yu33)*cmath.cos(beta))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1322 = Coupling(name = 'GC_1322',
                   value = '-((ee*complex(0,1)*NN13*UU11*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw))) + (ee*complex(0,1)*NN13*sw*UU11*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN11*UU12*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN12*UU12*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN12*sw*UU12*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1323 = Coupling(name = 'GC_1323',
                   value = '-((ee*complex(0,1)*NN23*UU11*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw))) + (ee*complex(0,1)*NN23*sw*UU11*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN21*UU12*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN22*UU12*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN22*sw*UU12*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1324 = Coupling(name = 'GC_1324',
                   value = '-((ee*complex(0,1)*NN33*UU11*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw))) + (ee*complex(0,1)*NN33*sw*UU11*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN31*UU12*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN32*UU12*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN32*sw*UU12*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1325 = Coupling(name = 'GC_1325',
                   value = '-((ee*complex(0,1)*NN43*UU11*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw))) + (ee*complex(0,1)*NN43*sw*UU11*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN41*UU12*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN42*UU12*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN42*sw*UU12*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1326 = Coupling(name = 'GC_1326',
                   value = '-((ee*complex(0,1)*NN13*UU21*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw))) + (ee*complex(0,1)*NN13*sw*UU21*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN11*UU22*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN12*UU22*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN12*sw*UU22*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1327 = Coupling(name = 'GC_1327',
                   value = '-((ee*complex(0,1)*NN23*UU21*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw))) + (ee*complex(0,1)*NN23*sw*UU21*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN21*UU22*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN22*UU22*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN22*sw*UU22*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1328 = Coupling(name = 'GC_1328',
                   value = '-((ee*complex(0,1)*NN33*UU21*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw))) + (ee*complex(0,1)*NN33*sw*UU21*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN31*UU22*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN32*UU22*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN32*sw*UU22*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1329 = Coupling(name = 'GC_1329',
                   value = '-((ee*complex(0,1)*NN43*UU21*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw))) + (ee*complex(0,1)*NN43*sw*UU21*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN41*UU22*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN42*UU22*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN42*sw*UU22*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1330 = Coupling(name = 'GC_1330',
                   value = '(ee*complex(0,1)*NN14*VV11*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN14*sw*VV11*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN11*VV12*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN12*VV12*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN12*sw*VV12*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1331 = Coupling(name = 'GC_1331',
                   value = '(ee*complex(0,1)*NN24*VV11*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN24*sw*VV11*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN21*VV12*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN22*VV12*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN22*sw*VV12*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1332 = Coupling(name = 'GC_1332',
                   value = '(ee*complex(0,1)*NN34*VV11*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN34*sw*VV11*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN31*VV12*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN32*VV12*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN32*sw*VV12*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1333 = Coupling(name = 'GC_1333',
                   value = '(ee*complex(0,1)*NN44*VV11*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN44*sw*VV11*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN41*VV12*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN42*VV12*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN42*sw*VV12*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1334 = Coupling(name = 'GC_1334',
                   value = '(ee*complex(0,1)*NN14*VV21*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN14*sw*VV21*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN11*VV22*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN12*VV22*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN12*sw*VV22*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1335 = Coupling(name = 'GC_1335',
                   value = '(ee*complex(0,1)*NN24*VV21*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN24*sw*VV21*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN21*VV22*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN22*VV22*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN22*sw*VV22*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1336 = Coupling(name = 'GC_1336',
                   value = '(ee*complex(0,1)*NN34*VV21*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN34*sw*VV21*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN31*VV22*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN32*VV22*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN32*sw*VV22*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1337 = Coupling(name = 'GC_1337',
                   value = '(ee*complex(0,1)*NN44*VV21*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN44*sw*VV21*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN41*VV22*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN42*VV22*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN42*sw*VV22*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1338 = Coupling(name = 'GC_1338',
                   value = '-((ee*complex(0,1)*complexconjugate(NN13)*complexconjugate(UU11)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw))) + (ee*complex(0,1)*sw*complexconjugate(NN13)*complexconjugate(UU11)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN11)*complexconjugate(UU12)*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*complexconjugate(NN12)*complexconjugate(UU12)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*sw*complexconjugate(NN12)*complexconjugate(UU12)*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1339 = Coupling(name = 'GC_1339',
                   value = '-((ee*complex(0,1)*complexconjugate(NN23)*complexconjugate(UU11)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw))) + (ee*complex(0,1)*sw*complexconjugate(NN23)*complexconjugate(UU11)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN21)*complexconjugate(UU12)*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*complexconjugate(NN22)*complexconjugate(UU12)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*sw*complexconjugate(NN22)*complexconjugate(UU12)*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1340 = Coupling(name = 'GC_1340',
                   value = '-((ee*complex(0,1)*complexconjugate(NN33)*complexconjugate(UU11)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw))) + (ee*complex(0,1)*sw*complexconjugate(NN33)*complexconjugate(UU11)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN31)*complexconjugate(UU12)*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*complexconjugate(NN32)*complexconjugate(UU12)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*sw*complexconjugate(NN32)*complexconjugate(UU12)*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1341 = Coupling(name = 'GC_1341',
                   value = '-((ee*complex(0,1)*complexconjugate(NN43)*complexconjugate(UU11)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw))) + (ee*complex(0,1)*sw*complexconjugate(NN43)*complexconjugate(UU11)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN41)*complexconjugate(UU12)*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*complexconjugate(NN42)*complexconjugate(UU12)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*sw*complexconjugate(NN42)*complexconjugate(UU12)*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1342 = Coupling(name = 'GC_1342',
                   value = '-((ee*complex(0,1)*complexconjugate(NN13)*complexconjugate(UU21)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw))) + (ee*complex(0,1)*sw*complexconjugate(NN13)*complexconjugate(UU21)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN11)*complexconjugate(UU22)*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*complexconjugate(NN12)*complexconjugate(UU22)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*sw*complexconjugate(NN12)*complexconjugate(UU22)*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1343 = Coupling(name = 'GC_1343',
                   value = '-((ee*complex(0,1)*complexconjugate(NN23)*complexconjugate(UU21)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw))) + (ee*complex(0,1)*sw*complexconjugate(NN23)*complexconjugate(UU21)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN21)*complexconjugate(UU22)*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*complexconjugate(NN22)*complexconjugate(UU22)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*sw*complexconjugate(NN22)*complexconjugate(UU22)*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1344 = Coupling(name = 'GC_1344',
                   value = '-((ee*complex(0,1)*complexconjugate(NN33)*complexconjugate(UU21)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw))) + (ee*complex(0,1)*sw*complexconjugate(NN33)*complexconjugate(UU21)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN31)*complexconjugate(UU22)*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*complexconjugate(NN32)*complexconjugate(UU22)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*sw*complexconjugate(NN32)*complexconjugate(UU22)*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1345 = Coupling(name = 'GC_1345',
                   value = '-((ee*complex(0,1)*complexconjugate(NN43)*complexconjugate(UU21)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw))) + (ee*complex(0,1)*sw*complexconjugate(NN43)*complexconjugate(UU21)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN41)*complexconjugate(UU22)*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*complexconjugate(NN42)*complexconjugate(UU22)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*sw*complexconjugate(NN42)*complexconjugate(UU22)*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1346 = Coupling(name = 'GC_1346',
                   value = '(ee*complex(0,1)*complexconjugate(NN14)*complexconjugate(VV11)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN14)*complexconjugate(VV11)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN11)*complexconjugate(VV12)*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*complexconjugate(NN12)*complexconjugate(VV12)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*sw*complexconjugate(NN12)*complexconjugate(VV12)*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1347 = Coupling(name = 'GC_1347',
                   value = '(ee*complex(0,1)*complexconjugate(NN24)*complexconjugate(VV11)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN24)*complexconjugate(VV11)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN21)*complexconjugate(VV12)*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*complexconjugate(NN22)*complexconjugate(VV12)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*sw*complexconjugate(NN22)*complexconjugate(VV12)*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1348 = Coupling(name = 'GC_1348',
                   value = '(ee*complex(0,1)*complexconjugate(NN34)*complexconjugate(VV11)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN34)*complexconjugate(VV11)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN31)*complexconjugate(VV12)*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*complexconjugate(NN32)*complexconjugate(VV12)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*sw*complexconjugate(NN32)*complexconjugate(VV12)*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1349 = Coupling(name = 'GC_1349',
                   value = '(ee*complex(0,1)*complexconjugate(NN44)*complexconjugate(VV11)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN44)*complexconjugate(VV11)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN41)*complexconjugate(VV12)*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*complexconjugate(NN42)*complexconjugate(VV12)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*sw*complexconjugate(NN42)*complexconjugate(VV12)*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1350 = Coupling(name = 'GC_1350',
                   value = '(ee*complex(0,1)*complexconjugate(NN14)*complexconjugate(VV21)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN14)*complexconjugate(VV21)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN11)*complexconjugate(VV22)*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*complexconjugate(NN12)*complexconjugate(VV22)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*sw*complexconjugate(NN12)*complexconjugate(VV22)*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1351 = Coupling(name = 'GC_1351',
                   value = '(ee*complex(0,1)*complexconjugate(NN24)*complexconjugate(VV21)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN24)*complexconjugate(VV21)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN21)*complexconjugate(VV22)*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*complexconjugate(NN22)*complexconjugate(VV22)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*sw*complexconjugate(NN22)*complexconjugate(VV22)*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1352 = Coupling(name = 'GC_1352',
                   value = '(ee*complex(0,1)*complexconjugate(NN34)*complexconjugate(VV21)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN34)*complexconjugate(VV21)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN31)*complexconjugate(VV22)*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*complexconjugate(NN32)*complexconjugate(VV22)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*sw*complexconjugate(NN32)*complexconjugate(VV22)*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1353 = Coupling(name = 'GC_1353',
                   value = '(ee*complex(0,1)*complexconjugate(NN44)*complexconjugate(VV21)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN44)*complexconjugate(VV21)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN41)*complexconjugate(VV22)*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*complexconjugate(NN42)*complexconjugate(VV22)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*sw*complexconjugate(NN42)*complexconjugate(VV22)*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1354 = Coupling(name = 'GC_1354',
                   value = '(complex(0,1)*yd33*cmath.sin(alp))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1355 = Coupling(name = 'GC_1355',
                   value = '(complex(0,1)*ye33*cmath.sin(alp))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1356 = Coupling(name = 'GC_1356',
                   value = '-((complex(0,1)*yu33*cmath.sin(alp))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1357 = Coupling(name = 'GC_1357',
                   value = '(complex(0,1)*complexconjugate(yd33)*cmath.sin(alp))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1358 = Coupling(name = 'GC_1358',
                   value = '(complex(0,1)*complexconjugate(ye33)*cmath.sin(alp))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1359 = Coupling(name = 'GC_1359',
                   value = '-((complex(0,1)*complexconjugate(yu33)*cmath.sin(alp))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1360 = Coupling(name = 'GC_1360',
                   value = '(-2*ee**2*complex(0,1)*I149x44*cmath.cos(alp)*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1361 = Coupling(name = 'GC_1361',
                   value = '(-2*ee**2*complex(0,1)*I149x55*cmath.cos(alp)*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1362 = Coupling(name = 'GC_1362',
                   value = '(ee**2*complex(0,1)*I16x44*cmath.cos(alp)*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1363 = Coupling(name = 'GC_1363',
                   value = '(ee**2*complex(0,1)*I16x55*cmath.cos(alp)*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1364 = Coupling(name = 'GC_1364',
                   value = '(ee**2*complex(0,1)*I54x44*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1365 = Coupling(name = 'GC_1365',
                   value = '(ee**2*complex(0,1)*I54x55*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1366 = Coupling(name = 'GC_1366',
                   value = '-(ee**2*complex(0,1)*cmath.cos(alp)*cmath.sin(alp))/(2.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1367 = Coupling(name = 'GC_1367',
                   value = '(cw*ee*complex(0,1)*NN11*NN14*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN12*NN14*cmath.cos(alp))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN12*NN14*sw*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN11*NN13*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN12*NN13*cmath.sin(alp))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN12*NN13*sw*cmath.sin(alp))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1368 = Coupling(name = 'GC_1368',
                   value = '-((cw*ee*complex(0,1)*NN11*NN13*cmath.cos(alp))/((-1 + sw)*(1 + sw))) + (ee*complex(0,1)*NN12*NN13*cmath.cos(alp))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN12*NN13*sw*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN11*NN14*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN12*NN14*cmath.sin(alp))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN12*NN14*sw*cmath.sin(alp))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1369 = Coupling(name = 'GC_1369',
                   value = '(cw*ee*complex(0,1)*NN14*NN21*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN11*NN24*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN14*NN22*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN12*NN24*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN14*NN22*sw*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN12*NN24*sw*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN13*NN21*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN11*NN23*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN13*NN22*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN12*NN23*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN13*NN22*sw*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN12*NN23*sw*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1370 = Coupling(name = 'GC_1370',
                   value = '(cw*ee*complex(0,1)*NN21*NN24*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN22*NN24*cmath.cos(alp))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN22*NN24*sw*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN21*NN23*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN22*NN23*cmath.sin(alp))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN22*NN23*sw*cmath.sin(alp))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1371 = Coupling(name = 'GC_1371',
                   value = '-(cw*ee*complex(0,1)*NN13*NN21*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN11*NN23*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN13*NN22*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN12*NN23*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN13*NN22*sw*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN12*NN23*sw*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN14*NN21*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN11*NN24*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN14*NN22*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN12*NN24*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN14*NN22*sw*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN12*NN24*sw*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1372 = Coupling(name = 'GC_1372',
                   value = '-((cw*ee*complex(0,1)*NN21*NN23*cmath.cos(alp))/((-1 + sw)*(1 + sw))) + (ee*complex(0,1)*NN22*NN23*cmath.cos(alp))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN22*NN23*sw*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN21*NN24*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN22*NN24*cmath.sin(alp))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN22*NN24*sw*cmath.sin(alp))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1373 = Coupling(name = 'GC_1373',
                   value = '(cw*ee*complex(0,1)*NN14*NN31*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN11*NN34*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN14*NN32*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN12*NN34*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN14*NN32*sw*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN12*NN34*sw*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN13*NN31*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN11*NN33*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN13*NN32*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN12*NN33*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN13*NN32*sw*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN12*NN33*sw*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1374 = Coupling(name = 'GC_1374',
                   value = '(cw*ee*complex(0,1)*NN24*NN31*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN21*NN34*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN24*NN32*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN22*NN34*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN24*NN32*sw*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN22*NN34*sw*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN23*NN31*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN21*NN33*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN23*NN32*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN22*NN33*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN23*NN32*sw*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN22*NN33*sw*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1375 = Coupling(name = 'GC_1375',
                   value = '(cw*ee*complex(0,1)*NN31*NN34*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN32*NN34*cmath.cos(alp))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN32*NN34*sw*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN31*NN33*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN32*NN33*cmath.sin(alp))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN32*NN33*sw*cmath.sin(alp))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1376 = Coupling(name = 'GC_1376',
                   value = '-(cw*ee*complex(0,1)*NN13*NN31*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN11*NN33*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN13*NN32*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN12*NN33*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN13*NN32*sw*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN12*NN33*sw*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN14*NN31*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN11*NN34*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN14*NN32*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN12*NN34*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN14*NN32*sw*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN12*NN34*sw*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1377 = Coupling(name = 'GC_1377',
                   value = '-(cw*ee*complex(0,1)*NN23*NN31*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN21*NN33*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN23*NN32*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN22*NN33*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN23*NN32*sw*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN22*NN33*sw*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN24*NN31*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN21*NN34*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN24*NN32*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN22*NN34*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN24*NN32*sw*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN22*NN34*sw*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1378 = Coupling(name = 'GC_1378',
                   value = '-((cw*ee*complex(0,1)*NN31*NN33*cmath.cos(alp))/((-1 + sw)*(1 + sw))) + (ee*complex(0,1)*NN32*NN33*cmath.cos(alp))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN32*NN33*sw*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN31*NN34*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN32*NN34*cmath.sin(alp))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN32*NN34*sw*cmath.sin(alp))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1379 = Coupling(name = 'GC_1379',
                   value = '(cw*ee*complex(0,1)*NN14*NN41*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN11*NN44*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN14*NN42*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN12*NN44*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN14*NN42*sw*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN12*NN44*sw*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN13*NN41*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN11*NN43*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN13*NN42*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN12*NN43*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN13*NN42*sw*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN12*NN43*sw*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1380 = Coupling(name = 'GC_1380',
                   value = '(cw*ee*complex(0,1)*NN24*NN41*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN21*NN44*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN24*NN42*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN22*NN44*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN24*NN42*sw*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN22*NN44*sw*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN23*NN41*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN21*NN43*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN23*NN42*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN22*NN43*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN23*NN42*sw*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN22*NN43*sw*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1381 = Coupling(name = 'GC_1381',
                   value = '(cw*ee*complex(0,1)*NN34*NN41*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN31*NN44*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN34*NN42*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN32*NN44*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN34*NN42*sw*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN32*NN44*sw*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN33*NN41*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN31*NN43*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN33*NN42*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN32*NN43*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN33*NN42*sw*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN32*NN43*sw*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1382 = Coupling(name = 'GC_1382',
                   value = '(cw*ee*complex(0,1)*NN41*NN44*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN42*NN44*cmath.cos(alp))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN42*NN44*sw*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN41*NN43*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN42*NN43*cmath.sin(alp))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN42*NN43*sw*cmath.sin(alp))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1383 = Coupling(name = 'GC_1383',
                   value = '-(cw*ee*complex(0,1)*NN13*NN41*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN11*NN43*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN13*NN42*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN12*NN43*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN13*NN42*sw*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN12*NN43*sw*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN14*NN41*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN11*NN44*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN14*NN42*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN12*NN44*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN14*NN42*sw*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN12*NN44*sw*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1384 = Coupling(name = 'GC_1384',
                   value = '-(cw*ee*complex(0,1)*NN23*NN41*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN21*NN43*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN23*NN42*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN22*NN43*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN23*NN42*sw*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN22*NN43*sw*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN24*NN41*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN21*NN44*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN24*NN42*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN22*NN44*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN24*NN42*sw*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN22*NN44*sw*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1385 = Coupling(name = 'GC_1385',
                   value = '-(cw*ee*complex(0,1)*NN33*NN41*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN31*NN43*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN33*NN42*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN32*NN43*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN33*NN42*sw*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN32*NN43*sw*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN34*NN41*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN31*NN44*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN34*NN42*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN32*NN44*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN34*NN42*sw*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN32*NN44*sw*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1386 = Coupling(name = 'GC_1386',
                   value = '-((cw*ee*complex(0,1)*NN41*NN43*cmath.cos(alp))/((-1 + sw)*(1 + sw))) + (ee*complex(0,1)*NN42*NN43*cmath.cos(alp))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN42*NN43*sw*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN41*NN44*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN42*NN44*cmath.sin(alp))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN42*NN44*sw*cmath.sin(alp))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1387 = Coupling(name = 'GC_1387',
                   value = '-(ee**2*complex(0,1)*vu*cmath.cos(alp))/(4.*sw**2) + (ee**2*complex(0,1)*vd*cmath.sin(alp))/(4.*sw**2)',
                   order = {'QED':1})

GC_1388 = Coupling(name = 'GC_1388',
                   value = '(ee**2*complex(0,1)*vu*cmath.cos(alp))/(2.*sw**2) - (ee**2*complex(0,1)*vd*cmath.sin(alp))/(2.*sw**2)',
                   order = {'QED':1})

GC_1389 = Coupling(name = 'GC_1389',
                   value = '-(ee**2*complex(0,1)*vu*cmath.cos(alp))/2. - (cw**2*ee**2*complex(0,1)*vu*cmath.cos(alp))/(4.*sw**2) - (ee**2*complex(0,1)*sw**2*vu*cmath.cos(alp))/(4.*cw**2) + (ee**2*complex(0,1)*vd*cmath.sin(alp))/2. + (cw**2*ee**2*complex(0,1)*vd*cmath.sin(alp))/(4.*sw**2) + (ee**2*complex(0,1)*sw**2*vd*cmath.sin(alp))/(4.*cw**2)',
                   order = {'QED':1})

GC_1390 = Coupling(name = 'GC_1390',
                   value = '-(ee**2*complex(0,1)*I114x44*vu*cmath.cos(alp))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I114x44*vd*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1391 = Coupling(name = 'GC_1391',
                   value = '-(ee**2*complex(0,1)*I114x55*vu*cmath.cos(alp))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I114x55*vd*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1392 = Coupling(name = 'GC_1392',
                   value = '(ee**2*complex(0,1)*I48x44*vu*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I48x44*vd*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1393 = Coupling(name = 'GC_1393',
                   value = '(ee**2*complex(0,1)*I48x55*vu*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I48x55*vd*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1394 = Coupling(name = 'GC_1394',
                   value = '(ee**2*complex(0,1)*I9x44*vu*cmath.cos(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I9x44*vd*cmath.sin(alp))/(6.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1395 = Coupling(name = 'GC_1395',
                   value = '(ee**2*complex(0,1)*I9x55*vu*cmath.cos(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I9x55*vd*cmath.sin(alp))/(6.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1396 = Coupling(name = 'GC_1396',
                   value = '-(ee**2*complex(0,1)*vu*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*vd*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':1})

GC_1397 = Coupling(name = 'GC_1397',
                   value = '-(ee**2*complex(0,1)*vu*cmath.cos(alp))/(2.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*vd*cmath.sin(alp))/(2.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':1})

GC_1398 = Coupling(name = 'GC_1398',
                   value = '(ee**2*complex(0,1)*I113x11*vu*cmath.cos(alp))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I113x11*vu*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I113x11*vd*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I113x11*vd*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':1})

GC_1399 = Coupling(name = 'GC_1399',
                   value = '(ee**2*complex(0,1)*I113x22*vu*cmath.cos(alp))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I113x22*vu*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I113x22*vd*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I113x22*vd*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':1})

GC_1400 = Coupling(name = 'GC_1400',
                   value = '-(ee**2*complex(0,1)*I47x11*vu*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I47x11*vu*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*I47x11*vd*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I47x11*vd*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':1})

GC_1401 = Coupling(name = 'GC_1401',
                   value = '-(ee**2*complex(0,1)*I47x22*vu*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I47x22*vu*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*I47x22*vd*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I47x22*vd*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':1})

GC_1402 = Coupling(name = 'GC_1402',
                   value = '-(ee**2*complex(0,1)*I8x11*vu*cmath.cos(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I8x11*vu*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*I8x11*vd*cmath.sin(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I8x11*vd*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':1})

GC_1403 = Coupling(name = 'GC_1403',
                   value = '-(ee**2*complex(0,1)*I8x22*vu*cmath.cos(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I8x22*vu*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*I8x22*vd*cmath.sin(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I8x22*vd*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':1})

GC_1404 = Coupling(name = 'GC_1404',
                   value = '-(ee**2*complex(0,1)*I8x33*vu*cmath.cos(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I9x33*vu*cmath.cos(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I8x33*vu*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I18x33*MUH*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I18x33*MUH*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I21x33*complexconjugate(MUH)*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I21x33*sw**2*complexconjugate(MUH)*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I20x33*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I22x33*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I8x33*vd*cmath.sin(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I9x33*vd*cmath.sin(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I8x33*vd*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*I20x33*sw**2*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I22x33*sw**2*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I17x33*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I19x33*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I17x33*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I19x33*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1405 = Coupling(name = 'GC_1405',
                   value = '-(ee**2*complex(0,1)*I8x36*vu*cmath.cos(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I9x36*vu*cmath.cos(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I8x36*vu*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I18x36*MUH*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I18x36*MUH*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I21x36*complexconjugate(MUH)*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I21x36*sw**2*complexconjugate(MUH)*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I20x36*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I22x36*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I8x36*vd*cmath.sin(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I9x36*vd*cmath.sin(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I8x36*vd*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*I20x36*sw**2*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I22x36*sw**2*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I17x36*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I19x36*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I17x36*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I19x36*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1406 = Coupling(name = 'GC_1406',
                   value = '-(ee**2*complex(0,1)*I8x63*vu*cmath.cos(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I9x63*vu*cmath.cos(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I8x63*vu*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I18x63*MUH*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I18x63*MUH*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I21x63*complexconjugate(MUH)*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I21x63*sw**2*complexconjugate(MUH)*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I20x63*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I22x63*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I8x63*vd*cmath.sin(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I9x63*vd*cmath.sin(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I8x63*vd*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*I20x63*sw**2*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I22x63*sw**2*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I17x63*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I19x63*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I17x63*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I19x63*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1407 = Coupling(name = 'GC_1407',
                   value = '-(ee**2*complex(0,1)*I8x66*vu*cmath.cos(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I9x66*vu*cmath.cos(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I8x66*vu*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I18x66*MUH*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I18x66*MUH*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I21x66*complexconjugate(MUH)*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I21x66*sw**2*complexconjugate(MUH)*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I20x66*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I22x66*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I8x66*vd*cmath.sin(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I9x66*vd*cmath.sin(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I8x66*vd*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*I20x66*sw**2*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I22x66*sw**2*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I17x66*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I19x66*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I17x66*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I19x66*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1408 = Coupling(name = 'GC_1408',
                   value = '-(ee**2*complex(0,1)*I47x33*vu*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I48x33*vu*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I47x33*vu*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I56x33*MUH*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I56x33*MUH*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I59x33*complexconjugate(MUH)*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I59x33*sw**2*complexconjugate(MUH)*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee**2*complex(0,1)*I47x33*vd*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I48x33*vd*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I58x33*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I60x33*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I47x33*vd*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*I58x33*sw**2*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I60x33*sw**2*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I55x33*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I57x33*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I55x33*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I57x33*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1409 = Coupling(name = 'GC_1409',
                   value = '-(ee**2*complex(0,1)*I47x36*vu*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I48x36*vu*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I47x36*vu*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I56x36*MUH*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I56x36*MUH*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I59x36*complexconjugate(MUH)*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I59x36*sw**2*complexconjugate(MUH)*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee**2*complex(0,1)*I47x36*vd*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I48x36*vd*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I58x36*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I60x36*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I47x36*vd*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*I58x36*sw**2*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I60x36*sw**2*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I55x36*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I57x36*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I55x36*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I57x36*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1410 = Coupling(name = 'GC_1410',
                   value = '-(ee**2*complex(0,1)*I47x63*vu*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I48x63*vu*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I47x63*vu*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I56x63*MUH*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I56x63*MUH*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I59x63*complexconjugate(MUH)*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I59x63*sw**2*complexconjugate(MUH)*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee**2*complex(0,1)*I47x63*vd*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I48x63*vd*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I58x63*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I60x63*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I47x63*vd*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*I58x63*sw**2*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I60x63*sw**2*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I55x63*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I57x63*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I55x63*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I57x63*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1411 = Coupling(name = 'GC_1411',
                   value = '-(ee**2*complex(0,1)*I47x66*vu*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I48x66*vu*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I47x66*vu*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I56x66*MUH*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I56x66*MUH*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I59x66*complexconjugate(MUH)*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I59x66*sw**2*complexconjugate(MUH)*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee**2*complex(0,1)*I47x66*vd*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I48x66*vd*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I58x66*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I60x66*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I47x66*vd*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*I58x66*sw**2*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I60x66*sw**2*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I55x66*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I57x66*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I55x66*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I57x66*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1412 = Coupling(name = 'GC_1412',
                   value = '-(ee**2*complex(0,1)*vd*cmath.cos(alp))/(4.*sw**2) - (ee**2*complex(0,1)*vu*cmath.sin(alp))/(4.*sw**2)',
                   order = {'QED':1})

GC_1413 = Coupling(name = 'GC_1413',
                   value = '(ee**2*complex(0,1)*vd*cmath.cos(alp))/(2.*sw**2) + (ee**2*complex(0,1)*vu*cmath.sin(alp))/(2.*sw**2)',
                   order = {'QED':1})

GC_1414 = Coupling(name = 'GC_1414',
                   value = '-(ee**2*complex(0,1)*vd*cmath.cos(alp))/2. - (cw**2*ee**2*complex(0,1)*vd*cmath.cos(alp))/(4.*sw**2) - (ee**2*complex(0,1)*sw**2*vd*cmath.cos(alp))/(4.*cw**2) - (ee**2*complex(0,1)*vu*cmath.sin(alp))/2. - (cw**2*ee**2*complex(0,1)*vu*cmath.sin(alp))/(4.*sw**2) - (ee**2*complex(0,1)*sw**2*vu*cmath.sin(alp))/(4.*cw**2)',
                   order = {'QED':1})

GC_1415 = Coupling(name = 'GC_1415',
                   value = '(ee**2*complex(0,1)*I114x44*vd*cmath.cos(alp))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I114x44*vu*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1416 = Coupling(name = 'GC_1416',
                   value = '(ee**2*complex(0,1)*I114x55*vd*cmath.cos(alp))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I114x55*vu*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1417 = Coupling(name = 'GC_1417',
                   value = '-(ee**2*complex(0,1)*I48x44*vd*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I48x44*vu*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1418 = Coupling(name = 'GC_1418',
                   value = '-(ee**2*complex(0,1)*I48x55*vd*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I48x55*vu*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1419 = Coupling(name = 'GC_1419',
                   value = '-(ee**2*complex(0,1)*I9x44*vd*cmath.cos(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I9x44*vu*cmath.sin(alp))/(6.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1420 = Coupling(name = 'GC_1420',
                   value = '-(ee**2*complex(0,1)*I9x55*vd*cmath.cos(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I9x55*vu*cmath.sin(alp))/(6.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1421 = Coupling(name = 'GC_1421',
                   value = '(ee**2*complex(0,1)*vd*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*vu*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':1})

GC_1422 = Coupling(name = 'GC_1422',
                   value = '-(ee**2*complex(0,1)*vd*cmath.cos(alp))/(2.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*vu*cmath.sin(alp))/(2.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':1})

GC_1423 = Coupling(name = 'GC_1423',
                   value = '-(ee**2*complex(0,1)*I113x11*vd*cmath.cos(alp))/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I113x11*vd*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I113x11*vu*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I113x11*vu*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':1})

GC_1424 = Coupling(name = 'GC_1424',
                   value = '-(ee**2*complex(0,1)*I113x22*vd*cmath.cos(alp))/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I113x22*vd*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I113x22*vu*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I113x22*vu*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':1})

GC_1425 = Coupling(name = 'GC_1425',
                   value = '(ee**2*complex(0,1)*I47x11*vd*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I47x11*vd*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*I47x11*vu*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I47x11*vu*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':1})

GC_1426 = Coupling(name = 'GC_1426',
                   value = '(ee**2*complex(0,1)*I47x22*vd*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I47x22*vd*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*I47x22*vu*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I47x22*vu*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':1})

GC_1427 = Coupling(name = 'GC_1427',
                   value = '(ee**2*complex(0,1)*I8x11*vd*cmath.cos(alp))/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I8x11*vd*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*I8x11*vu*cmath.sin(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I8x11*vu*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':1})

GC_1428 = Coupling(name = 'GC_1428',
                   value = '(ee**2*complex(0,1)*I8x22*vd*cmath.cos(alp))/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I8x22*vd*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*I8x22*vu*cmath.sin(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I8x22*vu*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':1})

GC_1429 = Coupling(name = 'GC_1429',
                   value = '-(ee**2*complex(0,1)*I113x33*vd*cmath.cos(alp))/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I114x33*vd*cmath.cos(alp))/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I113x33*vd*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I150x33*MUH*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I150x33*MUH*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I153x33*complexconjugate(MUH)*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I153x33*sw**2*complexconjugate(MUH)*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee**2*complex(0,1)*I113x33*vu*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I114x33*vu*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I154x33*vu*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I155x33*vu*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I113x33*vu*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I154x33*sw**2*vu*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I155x33*sw**2*vu*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I151x33*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I152x33*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I151x33*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I152x33*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1430 = Coupling(name = 'GC_1430',
                   value = '-(ee**2*complex(0,1)*I113x36*vd*cmath.cos(alp))/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I114x36*vd*cmath.cos(alp))/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I113x36*vd*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I150x36*MUH*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I150x36*MUH*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I153x36*complexconjugate(MUH)*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I153x36*sw**2*complexconjugate(MUH)*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee**2*complex(0,1)*I113x36*vu*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I114x36*vu*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I154x36*vu*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I155x36*vu*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I113x36*vu*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I154x36*sw**2*vu*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I155x36*sw**2*vu*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I151x36*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I152x36*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I151x36*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I152x36*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1431 = Coupling(name = 'GC_1431',
                   value = '-(ee**2*complex(0,1)*I113x63*vd*cmath.cos(alp))/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I114x63*vd*cmath.cos(alp))/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I113x63*vd*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I150x63*MUH*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I150x63*MUH*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I153x63*complexconjugate(MUH)*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I153x63*sw**2*complexconjugate(MUH)*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee**2*complex(0,1)*I113x63*vu*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I114x63*vu*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I154x63*vu*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I155x63*vu*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I113x63*vu*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I154x63*sw**2*vu*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I155x63*sw**2*vu*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I151x63*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I152x63*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I151x63*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I152x63*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1432 = Coupling(name = 'GC_1432',
                   value = '-(ee**2*complex(0,1)*I113x66*vd*cmath.cos(alp))/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I114x66*vd*cmath.cos(alp))/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I113x66*vd*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I150x66*MUH*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I150x66*MUH*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I153x66*complexconjugate(MUH)*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I153x66*sw**2*complexconjugate(MUH)*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee**2*complex(0,1)*I113x66*vu*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I114x66*vu*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I154x66*vu*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I155x66*vu*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I113x66*vu*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I154x66*sw**2*vu*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I155x66*sw**2*vu*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I151x66*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I152x66*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I151x66*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I152x66*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1433 = Coupling(name = 'GC_1433',
                   value = '-((ee*complex(0,1)*UU11*VV12*cmath.cos(alp))/(sw*cmath.sqrt(2))) + (ee*complex(0,1)*UU12*VV11*cmath.sin(alp))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1434 = Coupling(name = 'GC_1434',
                   value = '-((ee*complex(0,1)*UU21*VV12*cmath.cos(alp))/(sw*cmath.sqrt(2))) + (ee*complex(0,1)*UU22*VV11*cmath.sin(alp))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1435 = Coupling(name = 'GC_1435',
                   value = '-((ee*complex(0,1)*UU12*VV11*cmath.cos(alp))/(sw*cmath.sqrt(2))) - (ee*complex(0,1)*UU11*VV12*cmath.sin(alp))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1436 = Coupling(name = 'GC_1436',
                   value = '-((ee*complex(0,1)*UU22*VV11*cmath.cos(alp))/(sw*cmath.sqrt(2))) - (ee*complex(0,1)*UU21*VV12*cmath.sin(alp))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1437 = Coupling(name = 'GC_1437',
                   value = '-((ee*complex(0,1)*UU11*VV22*cmath.cos(alp))/(sw*cmath.sqrt(2))) + (ee*complex(0,1)*UU12*VV21*cmath.sin(alp))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1438 = Coupling(name = 'GC_1438',
                   value = '-((ee*complex(0,1)*UU21*VV22*cmath.cos(alp))/(sw*cmath.sqrt(2))) + (ee*complex(0,1)*UU22*VV21*cmath.sin(alp))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1439 = Coupling(name = 'GC_1439',
                   value = '-((ee*complex(0,1)*UU12*VV21*cmath.cos(alp))/(sw*cmath.sqrt(2))) - (ee*complex(0,1)*UU11*VV22*cmath.sin(alp))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1440 = Coupling(name = 'GC_1440',
                   value = '-((ee*complex(0,1)*UU22*VV21*cmath.cos(alp))/(sw*cmath.sqrt(2))) - (ee*complex(0,1)*UU21*VV22*cmath.sin(alp))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1441 = Coupling(name = 'GC_1441',
                   value = '(ee**2*complex(0,1)*I113x33*vu*cmath.cos(alp))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I114x33*vu*cmath.cos(alp))/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I154x33*vu*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I155x33*vu*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I113x33*vu*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I154x33*sw**2*vu*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I155x33*sw**2*vu*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I151x33*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I152x33*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I151x33*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I152x33*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee**2*complex(0,1)*I113x33*vd*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I114x33*vd*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I113x33*vd*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*I150x33*MUH*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I150x33*MUH*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I153x33*complexconjugate(MUH)*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I153x33*sw**2*complexconjugate(MUH)*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1442 = Coupling(name = 'GC_1442',
                   value = '(ee**2*complex(0,1)*I113x36*vu*cmath.cos(alp))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I114x36*vu*cmath.cos(alp))/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I154x36*vu*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I155x36*vu*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I113x36*vu*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I154x36*sw**2*vu*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I155x36*sw**2*vu*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I151x36*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I152x36*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I151x36*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I152x36*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee**2*complex(0,1)*I113x36*vd*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I114x36*vd*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I113x36*vd*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*I150x36*MUH*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I150x36*MUH*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I153x36*complexconjugate(MUH)*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I153x36*sw**2*complexconjugate(MUH)*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1443 = Coupling(name = 'GC_1443',
                   value = '(ee**2*complex(0,1)*I113x63*vu*cmath.cos(alp))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I114x63*vu*cmath.cos(alp))/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I154x63*vu*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I155x63*vu*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I113x63*vu*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I154x63*sw**2*vu*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I155x63*sw**2*vu*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I151x63*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I152x63*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I151x63*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I152x63*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee**2*complex(0,1)*I113x63*vd*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I114x63*vd*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I113x63*vd*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*I150x63*MUH*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I150x63*MUH*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I153x63*complexconjugate(MUH)*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I153x63*sw**2*complexconjugate(MUH)*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1444 = Coupling(name = 'GC_1444',
                   value = '(ee**2*complex(0,1)*I113x66*vu*cmath.cos(alp))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I114x66*vu*cmath.cos(alp))/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I154x66*vu*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I155x66*vu*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I113x66*vu*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I154x66*sw**2*vu*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I155x66*sw**2*vu*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I151x66*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I152x66*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I151x66*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I152x66*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee**2*complex(0,1)*I113x66*vd*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I114x66*vd*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I113x66*vd*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*I150x66*MUH*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I150x66*MUH*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I153x66*complexconjugate(MUH)*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I153x66*sw**2*complexconjugate(MUH)*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1445 = Coupling(name = 'GC_1445',
                   value = '(complex(0,1)*I20x33*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I22x33*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I8x33*vd*cmath.cos(alp))/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I9x33*vd*cmath.cos(alp))/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I8x33*vd*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I20x33*sw**2*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I22x33*sw**2*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I17x33*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I19x33*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I17x33*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I19x33*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee**2*complex(0,1)*I8x33*vu*cmath.sin(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I9x33*vu*cmath.sin(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I8x33*vu*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I18x33*MUH*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I18x33*MUH*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I21x33*complexconjugate(MUH)*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I21x33*sw**2*complexconjugate(MUH)*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1446 = Coupling(name = 'GC_1446',
                   value = '(complex(0,1)*I20x36*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I22x36*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I8x36*vd*cmath.cos(alp))/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I9x36*vd*cmath.cos(alp))/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I8x36*vd*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I20x36*sw**2*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I22x36*sw**2*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I17x36*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I19x36*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I17x36*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I19x36*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee**2*complex(0,1)*I8x36*vu*cmath.sin(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I9x36*vu*cmath.sin(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I8x36*vu*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I18x36*MUH*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I18x36*MUH*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I21x36*complexconjugate(MUH)*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I21x36*sw**2*complexconjugate(MUH)*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1447 = Coupling(name = 'GC_1447',
                   value = '(complex(0,1)*I20x63*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I22x63*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I8x63*vd*cmath.cos(alp))/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I9x63*vd*cmath.cos(alp))/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I8x63*vd*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I20x63*sw**2*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I22x63*sw**2*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I17x63*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I19x63*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I17x63*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I19x63*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee**2*complex(0,1)*I8x63*vu*cmath.sin(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I9x63*vu*cmath.sin(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I8x63*vu*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I18x63*MUH*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I18x63*MUH*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I21x63*complexconjugate(MUH)*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I21x63*sw**2*complexconjugate(MUH)*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1448 = Coupling(name = 'GC_1448',
                   value = '(complex(0,1)*I20x66*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I22x66*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I8x66*vd*cmath.cos(alp))/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I9x66*vd*cmath.cos(alp))/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I8x66*vd*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I20x66*sw**2*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I22x66*sw**2*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I17x66*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I19x66*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I17x66*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I19x66*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee**2*complex(0,1)*I8x66*vu*cmath.sin(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I9x66*vu*cmath.sin(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I8x66*vu*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I18x66*MUH*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I18x66*MUH*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I21x66*complexconjugate(MUH)*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I21x66*sw**2*complexconjugate(MUH)*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1449 = Coupling(name = 'GC_1449',
                   value = '(ee**2*complex(0,1)*I47x33*vd*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I48x33*vd*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I58x33*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I60x33*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I47x33*vd*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I58x33*sw**2*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I60x33*sw**2*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I55x33*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I57x33*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I55x33*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I57x33*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee**2*complex(0,1)*I47x33*vu*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I48x33*vu*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I47x33*vu*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I56x33*MUH*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I56x33*MUH*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I59x33*complexconjugate(MUH)*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I59x33*sw**2*complexconjugate(MUH)*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1450 = Coupling(name = 'GC_1450',
                   value = '(ee**2*complex(0,1)*I47x36*vd*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I48x36*vd*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I58x36*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I60x36*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I47x36*vd*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I58x36*sw**2*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I60x36*sw**2*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I55x36*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I57x36*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I55x36*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I57x36*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee**2*complex(0,1)*I47x36*vu*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I48x36*vu*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I47x36*vu*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I56x36*MUH*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I56x36*MUH*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I59x36*complexconjugate(MUH)*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I59x36*sw**2*complexconjugate(MUH)*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1451 = Coupling(name = 'GC_1451',
                   value = '(ee**2*complex(0,1)*I47x63*vd*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I48x63*vd*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I58x63*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I60x63*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I47x63*vd*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I58x63*sw**2*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I60x63*sw**2*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I55x63*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I57x63*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I55x63*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I57x63*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee**2*complex(0,1)*I47x63*vu*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I48x63*vu*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I47x63*vu*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I56x63*MUH*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I56x63*MUH*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I59x63*complexconjugate(MUH)*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I59x63*sw**2*complexconjugate(MUH)*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1452 = Coupling(name = 'GC_1452',
                   value = '(ee**2*complex(0,1)*I47x66*vd*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I48x66*vd*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I58x66*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I60x66*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I47x66*vd*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I58x66*sw**2*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I60x66*sw**2*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I55x66*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I57x66*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I55x66*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I57x66*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee**2*complex(0,1)*I47x66*vu*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I48x66*vu*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I47x66*vu*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I56x66*MUH*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I56x66*MUH*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I59x66*complexconjugate(MUH)*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I59x66*sw**2*complexconjugate(MUH)*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1453 = Coupling(name = 'GC_1453',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN11)*complexconjugate(NN14)*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN12)*complexconjugate(NN14)*cmath.cos(alp))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN12)*complexconjugate(NN14)*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN11)*complexconjugate(NN13)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN12)*complexconjugate(NN13)*cmath.sin(alp))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN12)*complexconjugate(NN13)*cmath.sin(alp))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1454 = Coupling(name = 'GC_1454',
                   value = '-((cw*ee*complex(0,1)*complexconjugate(NN11)*complexconjugate(NN13)*cmath.cos(alp))/((-1 + sw)*(1 + sw))) + (ee*complex(0,1)*complexconjugate(NN12)*complexconjugate(NN13)*cmath.cos(alp))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN12)*complexconjugate(NN13)*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN11)*complexconjugate(NN14)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN12)*complexconjugate(NN14)*cmath.sin(alp))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN12)*complexconjugate(NN14)*cmath.sin(alp))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1455 = Coupling(name = 'GC_1455',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN14)*complexconjugate(NN21)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN14)*complexconjugate(NN22)*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN14)*complexconjugate(NN22)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN11)*complexconjugate(NN24)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN12)*complexconjugate(NN24)*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN12)*complexconjugate(NN24)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN13)*complexconjugate(NN21)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN13)*complexconjugate(NN22)*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN13)*complexconjugate(NN22)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN11)*complexconjugate(NN23)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN12)*complexconjugate(NN23)*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN12)*complexconjugate(NN23)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1456 = Coupling(name = 'GC_1456',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN21)*complexconjugate(NN24)*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN22)*complexconjugate(NN24)*cmath.cos(alp))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN22)*complexconjugate(NN24)*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN21)*complexconjugate(NN23)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN22)*complexconjugate(NN23)*cmath.sin(alp))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN22)*complexconjugate(NN23)*cmath.sin(alp))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1457 = Coupling(name = 'GC_1457',
                   value = '-(cw*ee*complex(0,1)*complexconjugate(NN13)*complexconjugate(NN21)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*complexconjugate(NN13)*complexconjugate(NN22)*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN13)*complexconjugate(NN22)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*complexconjugate(NN11)*complexconjugate(NN23)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*complexconjugate(NN12)*complexconjugate(NN23)*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN12)*complexconjugate(NN23)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN14)*complexconjugate(NN21)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN14)*complexconjugate(NN22)*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN14)*complexconjugate(NN22)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN11)*complexconjugate(NN24)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN12)*complexconjugate(NN24)*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN12)*complexconjugate(NN24)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1458 = Coupling(name = 'GC_1458',
                   value = '-((cw*ee*complex(0,1)*complexconjugate(NN21)*complexconjugate(NN23)*cmath.cos(alp))/((-1 + sw)*(1 + sw))) + (ee*complex(0,1)*complexconjugate(NN22)*complexconjugate(NN23)*cmath.cos(alp))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN22)*complexconjugate(NN23)*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN21)*complexconjugate(NN24)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN22)*complexconjugate(NN24)*cmath.sin(alp))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN22)*complexconjugate(NN24)*cmath.sin(alp))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1459 = Coupling(name = 'GC_1459',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN14)*complexconjugate(NN31)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN14)*complexconjugate(NN32)*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN14)*complexconjugate(NN32)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN11)*complexconjugate(NN34)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN12)*complexconjugate(NN34)*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN12)*complexconjugate(NN34)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN13)*complexconjugate(NN31)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN13)*complexconjugate(NN32)*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN13)*complexconjugate(NN32)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN11)*complexconjugate(NN33)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN12)*complexconjugate(NN33)*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN12)*complexconjugate(NN33)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1460 = Coupling(name = 'GC_1460',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN24)*complexconjugate(NN31)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN24)*complexconjugate(NN32)*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN24)*complexconjugate(NN32)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN21)*complexconjugate(NN34)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN22)*complexconjugate(NN34)*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN22)*complexconjugate(NN34)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN23)*complexconjugate(NN31)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN23)*complexconjugate(NN32)*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN23)*complexconjugate(NN32)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN21)*complexconjugate(NN33)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN22)*complexconjugate(NN33)*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN22)*complexconjugate(NN33)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1461 = Coupling(name = 'GC_1461',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN31)*complexconjugate(NN34)*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN32)*complexconjugate(NN34)*cmath.cos(alp))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN32)*complexconjugate(NN34)*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN31)*complexconjugate(NN33)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN32)*complexconjugate(NN33)*cmath.sin(alp))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN32)*complexconjugate(NN33)*cmath.sin(alp))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1462 = Coupling(name = 'GC_1462',
                   value = '-(cw*ee*complex(0,1)*complexconjugate(NN13)*complexconjugate(NN31)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*complexconjugate(NN13)*complexconjugate(NN32)*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN13)*complexconjugate(NN32)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*complexconjugate(NN11)*complexconjugate(NN33)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*complexconjugate(NN12)*complexconjugate(NN33)*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN12)*complexconjugate(NN33)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN14)*complexconjugate(NN31)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN14)*complexconjugate(NN32)*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN14)*complexconjugate(NN32)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN11)*complexconjugate(NN34)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN12)*complexconjugate(NN34)*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN12)*complexconjugate(NN34)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1463 = Coupling(name = 'GC_1463',
                   value = '-(cw*ee*complex(0,1)*complexconjugate(NN23)*complexconjugate(NN31)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*complexconjugate(NN23)*complexconjugate(NN32)*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN23)*complexconjugate(NN32)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*complexconjugate(NN21)*complexconjugate(NN33)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*complexconjugate(NN22)*complexconjugate(NN33)*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN22)*complexconjugate(NN33)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN24)*complexconjugate(NN31)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN24)*complexconjugate(NN32)*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN24)*complexconjugate(NN32)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN21)*complexconjugate(NN34)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN22)*complexconjugate(NN34)*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN22)*complexconjugate(NN34)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1464 = Coupling(name = 'GC_1464',
                   value = '-((cw*ee*complex(0,1)*complexconjugate(NN31)*complexconjugate(NN33)*cmath.cos(alp))/((-1 + sw)*(1 + sw))) + (ee*complex(0,1)*complexconjugate(NN32)*complexconjugate(NN33)*cmath.cos(alp))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN32)*complexconjugate(NN33)*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN31)*complexconjugate(NN34)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN32)*complexconjugate(NN34)*cmath.sin(alp))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN32)*complexconjugate(NN34)*cmath.sin(alp))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1465 = Coupling(name = 'GC_1465',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN14)*complexconjugate(NN41)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN14)*complexconjugate(NN42)*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN14)*complexconjugate(NN42)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN11)*complexconjugate(NN44)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN12)*complexconjugate(NN44)*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN12)*complexconjugate(NN44)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN13)*complexconjugate(NN41)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN13)*complexconjugate(NN42)*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN13)*complexconjugate(NN42)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN11)*complexconjugate(NN43)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN12)*complexconjugate(NN43)*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN12)*complexconjugate(NN43)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1466 = Coupling(name = 'GC_1466',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN24)*complexconjugate(NN41)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN24)*complexconjugate(NN42)*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN24)*complexconjugate(NN42)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN21)*complexconjugate(NN44)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN22)*complexconjugate(NN44)*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN22)*complexconjugate(NN44)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN23)*complexconjugate(NN41)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN23)*complexconjugate(NN42)*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN23)*complexconjugate(NN42)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN21)*complexconjugate(NN43)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN22)*complexconjugate(NN43)*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN22)*complexconjugate(NN43)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1467 = Coupling(name = 'GC_1467',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN34)*complexconjugate(NN41)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN34)*complexconjugate(NN42)*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN34)*complexconjugate(NN42)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN31)*complexconjugate(NN44)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN32)*complexconjugate(NN44)*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN32)*complexconjugate(NN44)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN33)*complexconjugate(NN41)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN33)*complexconjugate(NN42)*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN33)*complexconjugate(NN42)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN31)*complexconjugate(NN43)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN32)*complexconjugate(NN43)*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN32)*complexconjugate(NN43)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1468 = Coupling(name = 'GC_1468',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN41)*complexconjugate(NN44)*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN42)*complexconjugate(NN44)*cmath.cos(alp))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN42)*complexconjugate(NN44)*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN41)*complexconjugate(NN43)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN42)*complexconjugate(NN43)*cmath.sin(alp))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN42)*complexconjugate(NN43)*cmath.sin(alp))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1469 = Coupling(name = 'GC_1469',
                   value = '-(cw*ee*complex(0,1)*complexconjugate(NN13)*complexconjugate(NN41)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*complexconjugate(NN13)*complexconjugate(NN42)*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN13)*complexconjugate(NN42)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*complexconjugate(NN11)*complexconjugate(NN43)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*complexconjugate(NN12)*complexconjugate(NN43)*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN12)*complexconjugate(NN43)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN14)*complexconjugate(NN41)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN14)*complexconjugate(NN42)*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN14)*complexconjugate(NN42)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN11)*complexconjugate(NN44)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN12)*complexconjugate(NN44)*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN12)*complexconjugate(NN44)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1470 = Coupling(name = 'GC_1470',
                   value = '-(cw*ee*complex(0,1)*complexconjugate(NN23)*complexconjugate(NN41)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*complexconjugate(NN23)*complexconjugate(NN42)*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN23)*complexconjugate(NN42)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*complexconjugate(NN21)*complexconjugate(NN43)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*complexconjugate(NN22)*complexconjugate(NN43)*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN22)*complexconjugate(NN43)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN24)*complexconjugate(NN41)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN24)*complexconjugate(NN42)*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN24)*complexconjugate(NN42)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN21)*complexconjugate(NN44)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN22)*complexconjugate(NN44)*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN22)*complexconjugate(NN44)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1471 = Coupling(name = 'GC_1471',
                   value = '-(cw*ee*complex(0,1)*complexconjugate(NN33)*complexconjugate(NN41)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*complexconjugate(NN33)*complexconjugate(NN42)*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN33)*complexconjugate(NN42)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*complexconjugate(NN31)*complexconjugate(NN43)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*complexconjugate(NN32)*complexconjugate(NN43)*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN32)*complexconjugate(NN43)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN34)*complexconjugate(NN41)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN34)*complexconjugate(NN42)*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN34)*complexconjugate(NN42)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN31)*complexconjugate(NN44)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN32)*complexconjugate(NN44)*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN32)*complexconjugate(NN44)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1472 = Coupling(name = 'GC_1472',
                   value = '-((cw*ee*complex(0,1)*complexconjugate(NN41)*complexconjugate(NN43)*cmath.cos(alp))/((-1 + sw)*(1 + sw))) + (ee*complex(0,1)*complexconjugate(NN42)*complexconjugate(NN43)*cmath.cos(alp))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN42)*complexconjugate(NN43)*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN41)*complexconjugate(NN44)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN42)*complexconjugate(NN44)*cmath.sin(alp))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN42)*complexconjugate(NN44)*cmath.sin(alp))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1473 = Coupling(name = 'GC_1473',
                   value = '-((ee*complex(0,1)*complexconjugate(UU11)*complexconjugate(VV12)*cmath.cos(alp))/(sw*cmath.sqrt(2))) + (ee*complex(0,1)*complexconjugate(UU12)*complexconjugate(VV11)*cmath.sin(alp))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1474 = Coupling(name = 'GC_1474',
                   value = '-((ee*complex(0,1)*complexconjugate(UU21)*complexconjugate(VV12)*cmath.cos(alp))/(sw*cmath.sqrt(2))) + (ee*complex(0,1)*complexconjugate(UU22)*complexconjugate(VV11)*cmath.sin(alp))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1475 = Coupling(name = 'GC_1475',
                   value = '-((ee*complex(0,1)*complexconjugate(UU12)*complexconjugate(VV11)*cmath.cos(alp))/(sw*cmath.sqrt(2))) - (ee*complex(0,1)*complexconjugate(UU11)*complexconjugate(VV12)*cmath.sin(alp))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1476 = Coupling(name = 'GC_1476',
                   value = '-((ee*complex(0,1)*complexconjugate(UU22)*complexconjugate(VV11)*cmath.cos(alp))/(sw*cmath.sqrt(2))) - (ee*complex(0,1)*complexconjugate(UU21)*complexconjugate(VV12)*cmath.sin(alp))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1477 = Coupling(name = 'GC_1477',
                   value = '-((ee*complex(0,1)*complexconjugate(UU11)*complexconjugate(VV22)*cmath.cos(alp))/(sw*cmath.sqrt(2))) + (ee*complex(0,1)*complexconjugate(UU12)*complexconjugate(VV21)*cmath.sin(alp))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1478 = Coupling(name = 'GC_1478',
                   value = '-((ee*complex(0,1)*complexconjugate(UU21)*complexconjugate(VV22)*cmath.cos(alp))/(sw*cmath.sqrt(2))) + (ee*complex(0,1)*complexconjugate(UU22)*complexconjugate(VV21)*cmath.sin(alp))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1479 = Coupling(name = 'GC_1479',
                   value = '-((ee*complex(0,1)*complexconjugate(UU12)*complexconjugate(VV21)*cmath.cos(alp))/(sw*cmath.sqrt(2))) - (ee*complex(0,1)*complexconjugate(UU11)*complexconjugate(VV22)*cmath.sin(alp))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1480 = Coupling(name = 'GC_1480',
                   value = '-((ee*complex(0,1)*complexconjugate(UU22)*complexconjugate(VV21)*cmath.cos(alp))/(sw*cmath.sqrt(2))) - (ee*complex(0,1)*complexconjugate(UU21)*complexconjugate(VV22)*cmath.sin(alp))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1481 = Coupling(name = 'GC_1481',
                   value = '(2*ee**2*complex(0,1)*I148x11*cmath.cos(alp)*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I148x11*cmath.cos(alp)*cmath.sin(alp))/(2.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1482 = Coupling(name = 'GC_1482',
                   value = '(2*ee**2*complex(0,1)*I148x22*cmath.cos(alp)*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I148x22*cmath.cos(alp)*cmath.sin(alp))/(2.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1483 = Coupling(name = 'GC_1483',
                   value = '-(ee**2*complex(0,1)*I15x11*cmath.cos(alp)*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15x11*cmath.cos(alp)*cmath.sin(alp))/(2.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1484 = Coupling(name = 'GC_1484',
                   value = '-(ee**2*complex(0,1)*I15x22*cmath.cos(alp)*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15x22*cmath.cos(alp)*cmath.sin(alp))/(2.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1485 = Coupling(name = 'GC_1485',
                   value = '-((ee**2*complex(0,1)*I53x11*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw))) + (ee**2*complex(0,1)*I53x11*cmath.cos(alp)*cmath.sin(alp))/(2.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1486 = Coupling(name = 'GC_1486',
                   value = '-((ee**2*complex(0,1)*I53x22*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw))) + (ee**2*complex(0,1)*I53x22*cmath.cos(alp)*cmath.sin(alp))/(2.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1487 = Coupling(name = 'GC_1487',
                   value = '(2*ee**2*complex(0,1)*I148x33*cmath.cos(alp)*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I149x33*cmath.cos(alp)*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I156x33*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I157x33*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I148x33*cmath.cos(alp)*cmath.sin(alp))/(2.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I156x33*sw**2*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I157x33*sw**2*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1488 = Coupling(name = 'GC_1488',
                   value = '(2*ee**2*complex(0,1)*I148x36*cmath.cos(alp)*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I149x36*cmath.cos(alp)*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I156x36*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I157x36*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I148x36*cmath.cos(alp)*cmath.sin(alp))/(2.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I156x36*sw**2*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I157x36*sw**2*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1489 = Coupling(name = 'GC_1489',
                   value = '(2*ee**2*complex(0,1)*I148x63*cmath.cos(alp)*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I149x63*cmath.cos(alp)*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I156x63*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I157x63*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I148x63*cmath.cos(alp)*cmath.sin(alp))/(2.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I156x63*sw**2*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I157x63*sw**2*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1490 = Coupling(name = 'GC_1490',
                   value = '(2*ee**2*complex(0,1)*I148x66*cmath.cos(alp)*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I149x66*cmath.cos(alp)*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I156x66*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I157x66*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I148x66*cmath.cos(alp)*cmath.sin(alp))/(2.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I156x66*sw**2*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I157x66*sw**2*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1491 = Coupling(name = 'GC_1491',
                   value = '-(ee**2*complex(0,1)*I15x33*cmath.cos(alp)*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I16x33*cmath.cos(alp)*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I23x33*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I24x33*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15x33*cmath.cos(alp)*cmath.sin(alp))/(2.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*I23x33*sw**2*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I24x33*sw**2*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1492 = Coupling(name = 'GC_1492',
                   value = '-(ee**2*complex(0,1)*I15x36*cmath.cos(alp)*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I16x36*cmath.cos(alp)*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I23x36*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I24x36*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15x36*cmath.cos(alp)*cmath.sin(alp))/(2.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*I23x36*sw**2*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I24x36*sw**2*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1493 = Coupling(name = 'GC_1493',
                   value = '-(ee**2*complex(0,1)*I15x63*cmath.cos(alp)*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I16x63*cmath.cos(alp)*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I23x63*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I24x63*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15x63*cmath.cos(alp)*cmath.sin(alp))/(2.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*I23x63*sw**2*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I24x63*sw**2*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1494 = Coupling(name = 'GC_1494',
                   value = '-(ee**2*complex(0,1)*I15x66*cmath.cos(alp)*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I16x66*cmath.cos(alp)*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I23x66*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I24x66*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15x66*cmath.cos(alp)*cmath.sin(alp))/(2.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*I23x66*sw**2*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I24x66*sw**2*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1495 = Coupling(name = 'GC_1495',
                   value = '-((ee**2*complex(0,1)*I53x33*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw))) + (ee**2*complex(0,1)*I54x33*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I61x33*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I62x33*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I53x33*cmath.cos(alp)*cmath.sin(alp))/(2.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*I61x33*sw**2*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I62x33*sw**2*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1496 = Coupling(name = 'GC_1496',
                   value = '-((ee**2*complex(0,1)*I53x36*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw))) + (ee**2*complex(0,1)*I54x36*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I61x36*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I62x36*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I53x36*cmath.cos(alp)*cmath.sin(alp))/(2.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*I61x36*sw**2*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I62x36*sw**2*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1497 = Coupling(name = 'GC_1497',
                   value = '-((ee**2*complex(0,1)*I53x63*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw))) + (ee**2*complex(0,1)*I54x63*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I61x63*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I62x63*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I53x63*cmath.cos(alp)*cmath.sin(alp))/(2.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*I61x63*sw**2*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I62x63*sw**2*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1498 = Coupling(name = 'GC_1498',
                   value = '-((ee**2*complex(0,1)*I53x66*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw))) + (ee**2*complex(0,1)*I54x66*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I61x66*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I62x66*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I53x66*cmath.cos(alp)*cmath.sin(alp))/(2.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*I61x66*sw**2*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I62x66*sw**2*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1499 = Coupling(name = 'GC_1499',
                   value = '(ee**2*complex(0,1)*cmath.cos(alp)**2)/(2.*sw**2) + (ee**2*complex(0,1)*cmath.sin(alp)**2)/(2.*sw**2)',
                   order = {'QED':2})

GC_1500 = Coupling(name = 'GC_1500',
                   value = '(ee**2*complex(0,1)*I149x44*cmath.cos(alp)**2)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I149x44*cmath.sin(alp)**2)/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1501 = Coupling(name = 'GC_1501',
                   value = '-(ee**2*complex(0,1)*I149x44*cmath.cos(alp)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I149x44*cmath.sin(alp)**2)/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1502 = Coupling(name = 'GC_1502',
                   value = '(ee**2*complex(0,1)*I149x55*cmath.cos(alp)**2)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I149x55*cmath.sin(alp)**2)/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1503 = Coupling(name = 'GC_1503',
                   value = '-(ee**2*complex(0,1)*I149x55*cmath.cos(alp)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I149x55*cmath.sin(alp)**2)/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1504 = Coupling(name = 'GC_1504',
                   value = '(ee**2*complex(0,1)*I16x44*cmath.cos(alp)**2)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16x44*cmath.sin(alp)**2)/(6.*(-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1505 = Coupling(name = 'GC_1505',
                   value = '-(ee**2*complex(0,1)*I16x44*cmath.cos(alp)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I16x44*cmath.sin(alp)**2)/(6.*(-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1506 = Coupling(name = 'GC_1506',
                   value = '(ee**2*complex(0,1)*I16x55*cmath.cos(alp)**2)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16x55*cmath.sin(alp)**2)/(6.*(-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1507 = Coupling(name = 'GC_1507',
                   value = '-(ee**2*complex(0,1)*I16x55*cmath.cos(alp)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I16x55*cmath.sin(alp)**2)/(6.*(-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1508 = Coupling(name = 'GC_1508',
                   value = '(ee**2*complex(0,1)*I54x44*cmath.cos(alp)**2)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I54x44*cmath.sin(alp)**2)/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1509 = Coupling(name = 'GC_1509',
                   value = '-(ee**2*complex(0,1)*I54x44*cmath.cos(alp)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I54x44*cmath.sin(alp)**2)/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1510 = Coupling(name = 'GC_1510',
                   value = '(ee**2*complex(0,1)*I54x55*cmath.cos(alp)**2)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I54x55*cmath.sin(alp)**2)/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1511 = Coupling(name = 'GC_1511',
                   value = '-(ee**2*complex(0,1)*I54x55*cmath.cos(alp)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I54x55*cmath.sin(alp)**2)/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1512 = Coupling(name = 'GC_1512',
                   value = '(ee**2*complex(0,1)*cmath.cos(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1513 = Coupling(name = 'GC_1513',
                   value = '-(ee**2*complex(0,1)*cmath.cos(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1514 = Coupling(name = 'GC_1514',
                   value = '-(ee**2*complex(0,1)*cmath.cos(alp)**2)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*cmath.sin(alp)**2)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1515 = Coupling(name = 'GC_1515',
                   value = '-(ee**2*complex(0,1)*I148x11*cmath.cos(alp)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I148x11*cmath.cos(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I148x11*cmath.sin(alp)**2)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I148x11*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1516 = Coupling(name = 'GC_1516',
                   value = '(ee**2*complex(0,1)*I148x11*cmath.cos(alp)**2)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I148x11*cmath.cos(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*I148x11*cmath.sin(alp)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I148x11*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1517 = Coupling(name = 'GC_1517',
                   value = '-(ee**2*complex(0,1)*I148x22*cmath.cos(alp)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I148x22*cmath.cos(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I148x22*cmath.sin(alp)**2)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I148x22*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1518 = Coupling(name = 'GC_1518',
                   value = '(ee**2*complex(0,1)*I148x22*cmath.cos(alp)**2)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I148x22*cmath.cos(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*I148x22*cmath.sin(alp)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I148x22*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1519 = Coupling(name = 'GC_1519',
                   value = '(ee**2*complex(0,1)*I148x33*cmath.cos(alp)**2)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I149x33*cmath.cos(alp)**2)/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I156x33*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I157x33*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I148x33*cmath.cos(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I156x33*sw**2*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I157x33*sw**2*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I148x33*cmath.sin(alp)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I149x33*cmath.sin(alp)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I148x33*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1520 = Coupling(name = 'GC_1520',
                   value = '(ee**2*complex(0,1)*I148x36*cmath.cos(alp)**2)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I149x36*cmath.cos(alp)**2)/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I156x36*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I157x36*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I148x36*cmath.cos(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I156x36*sw**2*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I157x36*sw**2*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I148x36*cmath.sin(alp)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I149x36*cmath.sin(alp)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I148x36*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1521 = Coupling(name = 'GC_1521',
                   value = '(ee**2*complex(0,1)*I148x63*cmath.cos(alp)**2)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I149x63*cmath.cos(alp)**2)/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I156x63*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I157x63*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I148x63*cmath.cos(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I156x63*sw**2*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I157x63*sw**2*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I148x63*cmath.sin(alp)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I149x63*cmath.sin(alp)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I148x63*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1522 = Coupling(name = 'GC_1522',
                   value = '(ee**2*complex(0,1)*I148x66*cmath.cos(alp)**2)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I149x66*cmath.cos(alp)**2)/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I156x66*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I157x66*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I148x66*cmath.cos(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I156x66*sw**2*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I157x66*sw**2*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I148x66*cmath.sin(alp)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I149x66*cmath.sin(alp)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I148x66*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1523 = Coupling(name = 'GC_1523',
                   value = '-(ee**2*complex(0,1)*I15x11*cmath.cos(alp)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15x11*cmath.cos(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I15x11*cmath.sin(alp)**2)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I15x11*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1524 = Coupling(name = 'GC_1524',
                   value = '(ee**2*complex(0,1)*I15x11*cmath.cos(alp)**2)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I15x11*cmath.cos(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*I15x11*cmath.sin(alp)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15x11*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1525 = Coupling(name = 'GC_1525',
                   value = '-(ee**2*complex(0,1)*I15x22*cmath.cos(alp)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15x22*cmath.cos(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I15x22*cmath.sin(alp)**2)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I15x22*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1526 = Coupling(name = 'GC_1526',
                   value = '(ee**2*complex(0,1)*I15x22*cmath.cos(alp)**2)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I15x22*cmath.cos(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*I15x22*cmath.sin(alp)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15x22*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1527 = Coupling(name = 'GC_1527',
                   value = '(ee**2*complex(0,1)*I15x33*cmath.cos(alp)**2)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16x33*cmath.cos(alp)**2)/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I23x33*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I24x33*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I15x33*cmath.cos(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I23x33*sw**2*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I24x33*sw**2*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I15x33*cmath.sin(alp)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I16x33*cmath.sin(alp)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15x33*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1528 = Coupling(name = 'GC_1528',
                   value = '(ee**2*complex(0,1)*I15x36*cmath.cos(alp)**2)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16x36*cmath.cos(alp)**2)/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I23x36*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I24x36*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I15x36*cmath.cos(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I23x36*sw**2*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I24x36*sw**2*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I15x36*cmath.sin(alp)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I16x36*cmath.sin(alp)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15x36*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1529 = Coupling(name = 'GC_1529',
                   value = '(ee**2*complex(0,1)*I15x63*cmath.cos(alp)**2)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16x63*cmath.cos(alp)**2)/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I23x63*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I24x63*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I15x63*cmath.cos(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I23x63*sw**2*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I24x63*sw**2*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I15x63*cmath.sin(alp)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I16x63*cmath.sin(alp)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15x63*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1530 = Coupling(name = 'GC_1530',
                   value = '(ee**2*complex(0,1)*I15x66*cmath.cos(alp)**2)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16x66*cmath.cos(alp)**2)/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I23x66*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I24x66*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I15x66*cmath.cos(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I23x66*sw**2*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I24x66*sw**2*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I15x66*cmath.sin(alp)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I16x66*cmath.sin(alp)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15x66*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1531 = Coupling(name = 'GC_1531',
                   value = '-(ee**2*complex(0,1)*I53x11*cmath.cos(alp)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I53x11*cmath.cos(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I53x11*cmath.sin(alp)**2)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I53x11*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1532 = Coupling(name = 'GC_1532',
                   value = '(ee**2*complex(0,1)*I53x11*cmath.cos(alp)**2)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I53x11*cmath.cos(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*I53x11*cmath.sin(alp)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I53x11*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1533 = Coupling(name = 'GC_1533',
                   value = '-(ee**2*complex(0,1)*I53x22*cmath.cos(alp)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I53x22*cmath.cos(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I53x22*cmath.sin(alp)**2)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I53x22*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1534 = Coupling(name = 'GC_1534',
                   value = '(ee**2*complex(0,1)*I53x22*cmath.cos(alp)**2)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I53x22*cmath.cos(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*I53x22*cmath.sin(alp)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I53x22*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1535 = Coupling(name = 'GC_1535',
                   value = '(ee**2*complex(0,1)*I53x33*cmath.cos(alp)**2)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I54x33*cmath.cos(alp)**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I61x33*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I62x33*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I53x33*cmath.cos(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I61x33*sw**2*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I62x33*sw**2*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I53x33*cmath.sin(alp)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I54x33*cmath.sin(alp)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I53x33*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1536 = Coupling(name = 'GC_1536',
                   value = '(ee**2*complex(0,1)*I53x36*cmath.cos(alp)**2)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I54x36*cmath.cos(alp)**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I61x36*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I62x36*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I53x36*cmath.cos(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I61x36*sw**2*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I62x36*sw**2*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I53x36*cmath.sin(alp)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I54x36*cmath.sin(alp)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I53x36*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1537 = Coupling(name = 'GC_1537',
                   value = '(ee**2*complex(0,1)*I53x63*cmath.cos(alp)**2)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I54x63*cmath.cos(alp)**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I61x63*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I62x63*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I53x63*cmath.cos(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I61x63*sw**2*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I62x63*sw**2*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I53x63*cmath.sin(alp)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I54x63*cmath.sin(alp)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I53x63*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1538 = Coupling(name = 'GC_1538',
                   value = '(ee**2*complex(0,1)*I53x66*cmath.cos(alp)**2)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I54x66*cmath.cos(alp)**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I61x66*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I62x66*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I53x66*cmath.cos(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I61x66*sw**2*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I62x66*sw**2*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I53x66*cmath.sin(alp)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I54x66*cmath.sin(alp)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I53x66*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1539 = Coupling(name = 'GC_1539',
                   value = '-(ee**2*complex(0,1)*I148x33*cmath.cos(alp)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I149x33*cmath.cos(alp)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I148x33*cmath.cos(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I148x33*cmath.sin(alp)**2)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I149x33*cmath.sin(alp)**2)/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I156x33*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I157x33*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I148x33*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I156x33*sw**2*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I157x33*sw**2*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1540 = Coupling(name = 'GC_1540',
                   value = '-(ee**2*complex(0,1)*I148x36*cmath.cos(alp)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I149x36*cmath.cos(alp)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I148x36*cmath.cos(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I148x36*cmath.sin(alp)**2)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I149x36*cmath.sin(alp)**2)/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I156x36*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I157x36*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I148x36*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I156x36*sw**2*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I157x36*sw**2*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1541 = Coupling(name = 'GC_1541',
                   value = '-(ee**2*complex(0,1)*I148x63*cmath.cos(alp)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I149x63*cmath.cos(alp)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I148x63*cmath.cos(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I148x63*cmath.sin(alp)**2)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I149x63*cmath.sin(alp)**2)/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I156x63*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I157x63*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I148x63*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I156x63*sw**2*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I157x63*sw**2*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1542 = Coupling(name = 'GC_1542',
                   value = '-(ee**2*complex(0,1)*I148x66*cmath.cos(alp)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I149x66*cmath.cos(alp)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I148x66*cmath.cos(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I148x66*cmath.sin(alp)**2)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I149x66*cmath.sin(alp)**2)/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I156x66*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I157x66*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I148x66*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I156x66*sw**2*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I157x66*sw**2*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1543 = Coupling(name = 'GC_1543',
                   value = '-(ee**2*complex(0,1)*I15x33*cmath.cos(alp)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I16x33*cmath.cos(alp)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15x33*cmath.cos(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I15x33*cmath.sin(alp)**2)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16x33*cmath.sin(alp)**2)/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I23x33*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I24x33*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I15x33*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I23x33*sw**2*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I24x33*sw**2*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1544 = Coupling(name = 'GC_1544',
                   value = '-(ee**2*complex(0,1)*I15x36*cmath.cos(alp)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I16x36*cmath.cos(alp)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15x36*cmath.cos(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I15x36*cmath.sin(alp)**2)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16x36*cmath.sin(alp)**2)/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I23x36*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I24x36*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I15x36*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I23x36*sw**2*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I24x36*sw**2*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1545 = Coupling(name = 'GC_1545',
                   value = '-(ee**2*complex(0,1)*I15x63*cmath.cos(alp)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I16x63*cmath.cos(alp)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15x63*cmath.cos(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I15x63*cmath.sin(alp)**2)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16x63*cmath.sin(alp)**2)/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I23x63*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I24x63*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I15x63*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I23x63*sw**2*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I24x63*sw**2*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1546 = Coupling(name = 'GC_1546',
                   value = '-(ee**2*complex(0,1)*I15x66*cmath.cos(alp)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I16x66*cmath.cos(alp)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15x66*cmath.cos(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I15x66*cmath.sin(alp)**2)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16x66*cmath.sin(alp)**2)/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I23x66*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I24x66*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I15x66*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I23x66*sw**2*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I24x66*sw**2*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1547 = Coupling(name = 'GC_1547',
                   value = '-(ee**2*complex(0,1)*I53x33*cmath.cos(alp)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I54x33*cmath.cos(alp)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I53x33*cmath.cos(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I53x33*cmath.sin(alp)**2)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I54x33*cmath.sin(alp)**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I61x33*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I62x33*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I53x33*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I61x33*sw**2*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I62x33*sw**2*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1548 = Coupling(name = 'GC_1548',
                   value = '-(ee**2*complex(0,1)*I53x36*cmath.cos(alp)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I54x36*cmath.cos(alp)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I53x36*cmath.cos(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I53x36*cmath.sin(alp)**2)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I54x36*cmath.sin(alp)**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I61x36*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I62x36*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I53x36*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I61x36*sw**2*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I62x36*sw**2*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1549 = Coupling(name = 'GC_1549',
                   value = '-(ee**2*complex(0,1)*I53x63*cmath.cos(alp)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I54x63*cmath.cos(alp)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I53x63*cmath.cos(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I53x63*cmath.sin(alp)**2)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I54x63*cmath.sin(alp)**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I61x63*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I62x63*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I53x63*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I61x63*sw**2*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I62x63*sw**2*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1550 = Coupling(name = 'GC_1550',
                   value = '-(ee**2*complex(0,1)*I53x66*cmath.cos(alp)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I54x66*cmath.cos(alp)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I53x66*cmath.cos(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I53x66*cmath.sin(alp)**2)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I54x66*cmath.sin(alp)**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I61x66*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I62x66*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I53x66*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I61x66*sw**2*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I62x66*sw**2*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1551 = Coupling(name = 'GC_1551',
                   value = '-(ee**2*complex(0,1)*vu*cmath.cos(alp)**3)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (5*ee**2*complex(0,1)*vd*cmath.cos(alp)**2*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) + (5*ee**2*complex(0,1)*vu*cmath.cos(alp)*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*vd*cmath.sin(alp)**3)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':1})

GC_1552 = Coupling(name = 'GC_1552',
                   value = '(3*ee**2*complex(0,1)*vu*cmath.cos(alp)**3)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (3*ee**2*complex(0,1)*vd*cmath.cos(alp)**2*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (3*ee**2*complex(0,1)*vu*cmath.cos(alp)*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (3*ee**2*complex(0,1)*vd*cmath.sin(alp)**3)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':1})

GC_1553 = Coupling(name = 'GC_1553',
                   value = '-(ee**2*complex(0,1)*vd*cmath.cos(alp)**3)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (5*ee**2*complex(0,1)*vu*cmath.cos(alp)**2*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) + (5*ee**2*complex(0,1)*vd*cmath.cos(alp)*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*vu*cmath.sin(alp)**3)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':1})

GC_1554 = Coupling(name = 'GC_1554',
                   value = '(3*ee**2*complex(0,1)*vd*cmath.cos(alp)**3)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (3*ee**2*complex(0,1)*vu*cmath.cos(alp)**2*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (3*ee**2*complex(0,1)*vd*cmath.cos(alp)*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (3*ee**2*complex(0,1)*vu*cmath.sin(alp)**3)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':1})

GC_1555 = Coupling(name = 'GC_1555',
                   value = '(3*ee**2*complex(0,1)*cmath.cos(alp)**3*cmath.sin(alp))/(2.*(-1 + sw)*sw**2*(1 + sw)) - (3*ee**2*complex(0,1)*cmath.cos(alp)*cmath.sin(alp)**3)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1556 = Coupling(name = 'GC_1556',
                   value = '(-3*ee**2*complex(0,1)*cmath.cos(alp)**3*cmath.sin(alp))/(2.*(-1 + sw)*sw**2*(1 + sw)) + (3*ee**2*complex(0,1)*cmath.cos(alp)*cmath.sin(alp)**3)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1557 = Coupling(name = 'GC_1557',
                   value = '-(ee**2*complex(0,1)*cmath.cos(alp)**4)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (5*ee**2*complex(0,1)*cmath.cos(alp)**2*cmath.sin(alp)**2)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*cmath.sin(alp)**4)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1558 = Coupling(name = 'GC_1558',
                   value = '(3*ee**2*complex(0,1)*cmath.cos(alp)**4)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (3*ee**2*complex(0,1)*cmath.cos(alp)**2*cmath.sin(alp)**2)/(2.*(-1 + sw)*sw**2*(1 + sw)) + (3*ee**2*complex(0,1)*cmath.sin(alp)**4)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1559 = Coupling(name = 'GC_1559',
                   value = 'complex(0,1)*I1x33*cmath.sin(beta)',
                   order = {'QED':1})

GC_1560 = Coupling(name = 'GC_1560',
                   value = 'complex(0,1)*I202x33*cmath.sin(beta)',
                   order = {'QED':1})

GC_1561 = Coupling(name = 'GC_1561',
                   value = 'complex(0,1)*I2x33*cmath.sin(beta)',
                   order = {'QED':1})

GC_1562 = Coupling(name = 'GC_1562',
                   value = 'complex(0,1)*I3x33*cmath.sin(beta)',
                   order = {'QED':1})

GC_1563 = Coupling(name = 'GC_1563',
                   value = 'complex(0,1)*I4x33*cmath.sin(beta)',
                   order = {'QED':1})

GC_1564 = Coupling(name = 'GC_1564',
                   value = 'complex(0,1)*I5x33*cmath.sin(beta)',
                   order = {'QED':1})

GC_1565 = Coupling(name = 'GC_1565',
                   value = '(yd33*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1566 = Coupling(name = 'GC_1566',
                   value = '(ye33*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1567 = Coupling(name = 'GC_1567',
                   value = '(yu33*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1568 = Coupling(name = 'GC_1568',
                   value = '-((complexconjugate(yd33)*cmath.sin(beta))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1569 = Coupling(name = 'GC_1569',
                   value = '-((complexconjugate(ye33)*cmath.sin(beta))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1570 = Coupling(name = 'GC_1570',
                   value = '-((complexconjugate(yu33)*cmath.sin(beta))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1571 = Coupling(name = 'GC_1571',
                   value = '-((ee**2*I102x11*cmath.cos(beta)*cmath.sin(beta))/(sw**2*cmath.sqrt(2)))',
                   order = {'QED':2})

GC_1572 = Coupling(name = 'GC_1572',
                   value = '-((ee**2*I102x22*cmath.cos(beta)*cmath.sin(beta))/(sw**2*cmath.sqrt(2)))',
                   order = {'QED':2})

GC_1573 = Coupling(name = 'GC_1573',
                   value = '(ee**2*I123x11*cmath.cos(beta)*cmath.sin(beta))/(sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1574 = Coupling(name = 'GC_1574',
                   value = '(ee**2*I123x22*cmath.cos(beta)*cmath.sin(beta))/(sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1575 = Coupling(name = 'GC_1575',
                   value = '-((ee**2*I144x11*cmath.cos(beta)*cmath.sin(beta))/(sw**2*cmath.sqrt(2)))',
                   order = {'QED':2})

GC_1576 = Coupling(name = 'GC_1576',
                   value = '-((ee**2*I144x22*cmath.cos(beta)*cmath.sin(beta))/(sw**2*cmath.sqrt(2)))',
                   order = {'QED':2})

GC_1577 = Coupling(name = 'GC_1577',
                   value = '(ee**2*I94x11*cmath.cos(beta)*cmath.sin(beta))/(sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1578 = Coupling(name = 'GC_1578',
                   value = '(ee**2*I94x22*cmath.cos(beta)*cmath.sin(beta))/(sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1579 = Coupling(name = 'GC_1579',
                   value = '(-2*ee**2*complex(0,1)*I149x44*cmath.cos(beta)*cmath.sin(beta))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1580 = Coupling(name = 'GC_1580',
                   value = '(-2*ee**2*complex(0,1)*I149x55*cmath.cos(beta)*cmath.sin(beta))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1581 = Coupling(name = 'GC_1581',
                   value = '(ee**2*complex(0,1)*I16x44*cmath.cos(beta)*cmath.sin(beta))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1582 = Coupling(name = 'GC_1582',
                   value = '(ee**2*complex(0,1)*I16x55*cmath.cos(beta)*cmath.sin(beta))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1583 = Coupling(name = 'GC_1583',
                   value = '(ee**2*complex(0,1)*I54x44*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1584 = Coupling(name = 'GC_1584',
                   value = '(ee**2*complex(0,1)*I54x55*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1585 = Coupling(name = 'GC_1585',
                   value = '-(ee**2*complex(0,1)*cmath.cos(beta)*cmath.sin(beta))/(2.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1586 = Coupling(name = 'GC_1586',
                   value = '-(ee**2*complex(0,1)*I53x11*cmath.cos(beta)*cmath.sin(beta))/(2.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1587 = Coupling(name = 'GC_1587',
                   value = '-(ee**2*complex(0,1)*I53x22*cmath.cos(beta)*cmath.sin(beta))/(2.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1588 = Coupling(name = 'GC_1588',
                   value = '(ee**2*complex(0,1)*cmath.cos(alp)*cmath.cos(beta)*cmath.sin(alp)*cmath.sin(beta))/((-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1589 = Coupling(name = 'GC_1589',
                   value = '(2*ee**2*complex(0,1)*cmath.cos(beta)**2*cmath.sin(beta)**2)/((-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1590 = Coupling(name = 'GC_1590',
                   value = '(I150x33*MUH*cmath.cos(beta))/cmath.sqrt(2) - (I153x33*complexconjugate(MUH)*cmath.cos(beta))/cmath.sqrt(2) - (I151x33*cmath.sin(beta))/cmath.sqrt(2) + (I152x33*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1591 = Coupling(name = 'GC_1591',
                   value = '(I150x36*MUH*cmath.cos(beta))/cmath.sqrt(2) - (I153x36*complexconjugate(MUH)*cmath.cos(beta))/cmath.sqrt(2) - (I151x36*cmath.sin(beta))/cmath.sqrt(2) + (I152x36*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1592 = Coupling(name = 'GC_1592',
                   value = '(I150x63*MUH*cmath.cos(beta))/cmath.sqrt(2) - (I153x63*complexconjugate(MUH)*cmath.cos(beta))/cmath.sqrt(2) - (I151x63*cmath.sin(beta))/cmath.sqrt(2) + (I152x63*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1593 = Coupling(name = 'GC_1593',
                   value = '(I150x66*MUH*cmath.cos(beta))/cmath.sqrt(2) - (I153x66*complexconjugate(MUH)*cmath.cos(beta))/cmath.sqrt(2) - (I151x66*cmath.sin(beta))/cmath.sqrt(2) + (I152x66*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1594 = Coupling(name = 'GC_1594',
                   value = '-((I18x33*MUH*cmath.cos(beta))/cmath.sqrt(2)) + (I21x33*complexconjugate(MUH)*cmath.cos(beta))/cmath.sqrt(2) - (I17x33*cmath.sin(beta))/cmath.sqrt(2) + (I19x33*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1595 = Coupling(name = 'GC_1595',
                   value = '-((I18x36*MUH*cmath.cos(beta))/cmath.sqrt(2)) + (I21x36*complexconjugate(MUH)*cmath.cos(beta))/cmath.sqrt(2) - (I17x36*cmath.sin(beta))/cmath.sqrt(2) + (I19x36*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1596 = Coupling(name = 'GC_1596',
                   value = '-((I18x63*MUH*cmath.cos(beta))/cmath.sqrt(2)) + (I21x63*complexconjugate(MUH)*cmath.cos(beta))/cmath.sqrt(2) - (I17x63*cmath.sin(beta))/cmath.sqrt(2) + (I19x63*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1597 = Coupling(name = 'GC_1597',
                   value = '-((I18x66*MUH*cmath.cos(beta))/cmath.sqrt(2)) + (I21x66*complexconjugate(MUH)*cmath.cos(beta))/cmath.sqrt(2) - (I17x66*cmath.sin(beta))/cmath.sqrt(2) + (I19x66*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1598 = Coupling(name = 'GC_1598',
                   value = '-((I56x33*MUH*cmath.cos(beta))/cmath.sqrt(2)) + (I59x33*complexconjugate(MUH)*cmath.cos(beta))/cmath.sqrt(2) - (I55x33*cmath.sin(beta))/cmath.sqrt(2) + (I57x33*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1599 = Coupling(name = 'GC_1599',
                   value = '-((I56x36*MUH*cmath.cos(beta))/cmath.sqrt(2)) + (I59x36*complexconjugate(MUH)*cmath.cos(beta))/cmath.sqrt(2) - (I55x36*cmath.sin(beta))/cmath.sqrt(2) + (I57x36*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1600 = Coupling(name = 'GC_1600',
                   value = '-((I56x63*MUH*cmath.cos(beta))/cmath.sqrt(2)) + (I59x63*complexconjugate(MUH)*cmath.cos(beta))/cmath.sqrt(2) - (I55x63*cmath.sin(beta))/cmath.sqrt(2) + (I57x63*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1601 = Coupling(name = 'GC_1601',
                   value = '-((I56x66*MUH*cmath.cos(beta))/cmath.sqrt(2)) + (I59x66*complexconjugate(MUH)*cmath.cos(beta))/cmath.sqrt(2) - (I55x66*cmath.sin(beta))/cmath.sqrt(2) + (I57x66*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1602 = Coupling(name = 'GC_1602',
                   value = '-((cw*ee*NN11*NN14*cmath.cos(beta))/((-1 + sw)*(1 + sw))) + (ee*NN12*NN14*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*NN12*NN14*sw*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*NN11*NN13*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (ee*NN12*NN13*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) + (ee*NN12*NN13*sw*cmath.sin(beta))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1603 = Coupling(name = 'GC_1603',
                   value = '-((cw*ee*NN11*NN13*cmath.cos(beta))/((-1 + sw)*(1 + sw))) + (ee*NN12*NN13*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*NN12*NN13*sw*cmath.cos(beta))/((-1 + sw)*(1 + sw)) - (cw*ee*NN11*NN14*cmath.sin(beta))/((-1 + sw)*(1 + sw)) + (ee*NN12*NN14*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*NN12*NN14*sw*cmath.sin(beta))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1604 = Coupling(name = 'GC_1604',
                   value = '-(cw*ee*NN14*NN21*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*NN11*NN24*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee*NN14*NN22*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN12*NN24*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN14*NN22*sw*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*NN12*NN24*sw*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*NN13*NN21*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*NN11*NN23*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*NN13*NN22*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN12*NN23*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN13*NN22*sw*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee*NN12*NN23*sw*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1605 = Coupling(name = 'GC_1605',
                   value = '-((cw*ee*NN21*NN24*cmath.cos(beta))/((-1 + sw)*(1 + sw))) + (ee*NN22*NN24*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*NN22*NN24*sw*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*NN21*NN23*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (ee*NN22*NN23*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) + (ee*NN22*NN23*sw*cmath.sin(beta))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1606 = Coupling(name = 'GC_1606',
                   value = '-(cw*ee*NN13*NN21*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*NN11*NN23*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee*NN13*NN22*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN12*NN23*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN13*NN22*sw*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*NN12*NN23*sw*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*NN14*NN21*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*NN11*NN24*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee*NN14*NN22*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN12*NN24*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN14*NN22*sw*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*NN12*NN24*sw*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1607 = Coupling(name = 'GC_1607',
                   value = '-((cw*ee*NN21*NN23*cmath.cos(beta))/((-1 + sw)*(1 + sw))) + (ee*NN22*NN23*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*NN22*NN23*sw*cmath.cos(beta))/((-1 + sw)*(1 + sw)) - (cw*ee*NN21*NN24*cmath.sin(beta))/((-1 + sw)*(1 + sw)) + (ee*NN22*NN24*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*NN22*NN24*sw*cmath.sin(beta))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1608 = Coupling(name = 'GC_1608',
                   value = '-(cw*ee*NN14*NN31*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*NN11*NN34*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee*NN14*NN32*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN12*NN34*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN14*NN32*sw*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*NN12*NN34*sw*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*NN13*NN31*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*NN11*NN33*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*NN13*NN32*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN12*NN33*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN13*NN32*sw*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee*NN12*NN33*sw*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1609 = Coupling(name = 'GC_1609',
                   value = '-(cw*ee*NN24*NN31*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*NN21*NN34*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee*NN24*NN32*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN22*NN34*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN24*NN32*sw*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*NN22*NN34*sw*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*NN23*NN31*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*NN21*NN33*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*NN23*NN32*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN22*NN33*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN23*NN32*sw*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee*NN22*NN33*sw*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1610 = Coupling(name = 'GC_1610',
                   value = '-((cw*ee*NN31*NN34*cmath.cos(beta))/((-1 + sw)*(1 + sw))) + (ee*NN32*NN34*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*NN32*NN34*sw*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*NN31*NN33*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (ee*NN32*NN33*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) + (ee*NN32*NN33*sw*cmath.sin(beta))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1611 = Coupling(name = 'GC_1611',
                   value = '-(cw*ee*NN13*NN31*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*NN11*NN33*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee*NN13*NN32*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN12*NN33*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN13*NN32*sw*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*NN12*NN33*sw*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*NN14*NN31*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*NN11*NN34*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee*NN14*NN32*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN12*NN34*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN14*NN32*sw*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*NN12*NN34*sw*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1612 = Coupling(name = 'GC_1612',
                   value = '-(cw*ee*NN23*NN31*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*NN21*NN33*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee*NN23*NN32*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN22*NN33*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN23*NN32*sw*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*NN22*NN33*sw*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*NN24*NN31*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*NN21*NN34*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee*NN24*NN32*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN22*NN34*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN24*NN32*sw*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*NN22*NN34*sw*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1613 = Coupling(name = 'GC_1613',
                   value = '-((cw*ee*NN31*NN33*cmath.cos(beta))/((-1 + sw)*(1 + sw))) + (ee*NN32*NN33*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*NN32*NN33*sw*cmath.cos(beta))/((-1 + sw)*(1 + sw)) - (cw*ee*NN31*NN34*cmath.sin(beta))/((-1 + sw)*(1 + sw)) + (ee*NN32*NN34*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*NN32*NN34*sw*cmath.sin(beta))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1614 = Coupling(name = 'GC_1614',
                   value = '-(cw*ee*NN14*NN41*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*NN11*NN44*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee*NN14*NN42*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN12*NN44*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN14*NN42*sw*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*NN12*NN44*sw*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*NN13*NN41*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*NN11*NN43*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*NN13*NN42*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN12*NN43*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN13*NN42*sw*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee*NN12*NN43*sw*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1615 = Coupling(name = 'GC_1615',
                   value = '-(cw*ee*NN24*NN41*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*NN21*NN44*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee*NN24*NN42*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN22*NN44*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN24*NN42*sw*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*NN22*NN44*sw*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*NN23*NN41*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*NN21*NN43*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*NN23*NN42*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN22*NN43*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN23*NN42*sw*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee*NN22*NN43*sw*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1616 = Coupling(name = 'GC_1616',
                   value = '-(cw*ee*NN34*NN41*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*NN31*NN44*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee*NN34*NN42*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN32*NN44*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN34*NN42*sw*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*NN32*NN44*sw*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*NN33*NN41*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*NN31*NN43*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*NN33*NN42*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN32*NN43*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN33*NN42*sw*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee*NN32*NN43*sw*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1617 = Coupling(name = 'GC_1617',
                   value = '-((cw*ee*NN41*NN44*cmath.cos(beta))/((-1 + sw)*(1 + sw))) + (ee*NN42*NN44*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*NN42*NN44*sw*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*NN41*NN43*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (ee*NN42*NN43*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) + (ee*NN42*NN43*sw*cmath.sin(beta))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1618 = Coupling(name = 'GC_1618',
                   value = '-(cw*ee*NN13*NN41*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*NN11*NN43*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee*NN13*NN42*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN12*NN43*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN13*NN42*sw*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*NN12*NN43*sw*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*NN14*NN41*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*NN11*NN44*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee*NN14*NN42*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN12*NN44*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN14*NN42*sw*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*NN12*NN44*sw*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1619 = Coupling(name = 'GC_1619',
                   value = '-(cw*ee*NN23*NN41*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*NN21*NN43*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee*NN23*NN42*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN22*NN43*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN23*NN42*sw*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*NN22*NN43*sw*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*NN24*NN41*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*NN21*NN44*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee*NN24*NN42*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN22*NN44*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN24*NN42*sw*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*NN22*NN44*sw*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1620 = Coupling(name = 'GC_1620',
                   value = '-(cw*ee*NN33*NN41*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*NN31*NN43*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee*NN33*NN42*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN32*NN43*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN33*NN42*sw*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*NN32*NN43*sw*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*NN34*NN41*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*NN31*NN44*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee*NN34*NN42*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN32*NN44*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN34*NN42*sw*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*NN32*NN44*sw*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1621 = Coupling(name = 'GC_1621',
                   value = '-((cw*ee*NN41*NN43*cmath.cos(beta))/((-1 + sw)*(1 + sw))) + (ee*NN42*NN43*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*NN42*NN43*sw*cmath.cos(beta))/((-1 + sw)*(1 + sw)) - (cw*ee*NN41*NN44*cmath.sin(beta))/((-1 + sw)*(1 + sw)) + (ee*NN42*NN44*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*NN42*NN44*sw*cmath.sin(beta))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1622 = Coupling(name = 'GC_1622',
                   value = '(ee*complex(0,1)*NN13*UU11*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN13*sw*UU11*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN11*UU12*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN12*UU12*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN12*sw*UU12*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1623 = Coupling(name = 'GC_1623',
                   value = '(ee*complex(0,1)*NN23*UU11*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN23*sw*UU11*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN21*UU12*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN22*UU12*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN22*sw*UU12*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1624 = Coupling(name = 'GC_1624',
                   value = '(ee*complex(0,1)*NN33*UU11*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN33*sw*UU11*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN31*UU12*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN32*UU12*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN32*sw*UU12*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1625 = Coupling(name = 'GC_1625',
                   value = '(ee*complex(0,1)*NN43*UU11*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN43*sw*UU11*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN41*UU12*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN42*UU12*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN42*sw*UU12*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1626 = Coupling(name = 'GC_1626',
                   value = '(ee*complex(0,1)*NN13*UU21*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN13*sw*UU21*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN11*UU22*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN12*UU22*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN12*sw*UU22*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1627 = Coupling(name = 'GC_1627',
                   value = '(ee*complex(0,1)*NN23*UU21*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN23*sw*UU21*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN21*UU22*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN22*UU22*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN22*sw*UU22*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1628 = Coupling(name = 'GC_1628',
                   value = '(ee*complex(0,1)*NN33*UU21*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN33*sw*UU21*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN31*UU22*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN32*UU22*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN32*sw*UU22*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1629 = Coupling(name = 'GC_1629',
                   value = '(ee*complex(0,1)*NN43*UU21*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN43*sw*UU21*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN41*UU22*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN42*UU22*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN42*sw*UU22*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1630 = Coupling(name = 'GC_1630',
                   value = '(ee**2*vu*cmath.cos(beta))/(4.*sw**2) - (ee**2*vd*cmath.sin(beta))/(4.*sw**2)',
                   order = {'QED':1})

GC_1631 = Coupling(name = 'GC_1631',
                   value = '-(ee**2*vu*cmath.cos(beta))/(4.*sw**2) + (ee**2*vd*cmath.sin(beta))/(4.*sw**2)',
                   order = {'QED':1})

GC_1632 = Coupling(name = 'GC_1632',
                   value = '(ee**2*complex(0,1)*vu*cmath.cos(beta))/(4.*cw) + (cw*ee**2*complex(0,1)*vu*cmath.cos(beta))/(4.*sw**2) - (ee**2*complex(0,1)*vd*cmath.sin(beta))/(4.*cw) - (cw*ee**2*complex(0,1)*vd*cmath.sin(beta))/(4.*sw**2)',
                   order = {'QED':1})

GC_1633 = Coupling(name = 'GC_1633',
                   value = '(ee**2*complex(0,1)*vu*cmath.cos(beta))/(4.*cw) - (cw*ee**2*complex(0,1)*vu*cmath.cos(beta))/(4.*sw**2) - (ee**2*complex(0,1)*vd*cmath.sin(beta))/(4.*cw) + (cw*ee**2*complex(0,1)*vd*cmath.sin(beta))/(4.*sw**2)',
                   order = {'QED':1})

GC_1634 = Coupling(name = 'GC_1634',
                   value = '-(ee**2*complex(0,1)*I115x11*vu*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) - (ee**2*complex(0,1)*I115x11*vd*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1635 = Coupling(name = 'GC_1635',
                   value = '-(ee**2*complex(0,1)*I115x22*vu*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) - (ee**2*complex(0,1)*I115x22*vd*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1636 = Coupling(name = 'GC_1636',
                   value = '-(ee**2*complex(0,1)*I136x11*vu*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) - (ee**2*complex(0,1)*I136x11*vd*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1637 = Coupling(name = 'GC_1637',
                   value = '-(ee**2*complex(0,1)*I136x22*vu*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) - (ee**2*complex(0,1)*I136x22*vd*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1638 = Coupling(name = 'GC_1638',
                   value = '-(ee**2*complex(0,1)*I90x11*vu*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) - (ee**2*complex(0,1)*I90x11*vd*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1639 = Coupling(name = 'GC_1639',
                   value = '-(ee**2*complex(0,1)*I90x22*vu*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) - (ee**2*complex(0,1)*I90x22*vd*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1640 = Coupling(name = 'GC_1640',
                   value = 'complex(0,1)*I93x33*complexconjugate(MUH)*cmath.cos(beta) - (ee**2*complex(0,1)*I90x33*vu*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) + complex(0,1)*I91x33*cmath.sin(beta) + (complex(0,1)*I92x33*vd*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I90x33*vd*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1641 = Coupling(name = 'GC_1641',
                   value = 'complex(0,1)*I93x36*complexconjugate(MUH)*cmath.cos(beta) - (ee**2*complex(0,1)*I90x36*vu*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) + complex(0,1)*I91x36*cmath.sin(beta) + (complex(0,1)*I92x36*vd*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I90x36*vd*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1642 = Coupling(name = 'GC_1642',
                   value = '-(ee**2*complex(0,1)*I98x11*vu*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) - (ee**2*complex(0,1)*I98x11*vd*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1643 = Coupling(name = 'GC_1643',
                   value = '-(ee**2*complex(0,1)*I98x22*vu*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) - (ee**2*complex(0,1)*I98x22*vd*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1644 = Coupling(name = 'GC_1644',
                   value = 'complex(0,1)*I100x33*MUH*cmath.cos(beta) - (ee**2*complex(0,1)*I98x33*vu*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) + complex(0,1)*I99x33*cmath.sin(beta) + (complex(0,1)*I101x33*vd*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I98x33*vd*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1645 = Coupling(name = 'GC_1645',
                   value = 'complex(0,1)*I100x36*MUH*cmath.cos(beta) - (ee**2*complex(0,1)*I98x36*vu*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) + complex(0,1)*I99x36*cmath.sin(beta) + (complex(0,1)*I101x36*vd*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I98x36*vd*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1646 = Coupling(name = 'GC_1646',
                   value = '(ee**2*complex(0,1)*vu*cmath.cos(beta))/(2.*sw) - (ee**2*complex(0,1)*vd*cmath.sin(beta))/(2.*sw)',
                   order = {'QED':1})

GC_1647 = Coupling(name = 'GC_1647',
                   value = '-(ee**2*complex(0,1)*vu*cmath.cos(beta))/(2.*sw) + (ee**2*complex(0,1)*vd*cmath.sin(beta))/(2.*sw)',
                   order = {'QED':1})

GC_1648 = Coupling(name = 'GC_1648',
                   value = '(cw*ee**2*complex(0,1)*vu*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee**2*complex(0,1)*vd*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1649 = Coupling(name = 'GC_1649',
                   value = 'complex(0,1)*I117x33*cmath.cos(beta) + complex(0,1)*I120x33*complexconjugate(MUH)*cmath.cos(beta) + (complex(0,1)*I121x33*vd*cmath.cos(beta))/cmath.sqrt(2) + (complex(0,1)*I122x33*vu*cmath.cos(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I115x33*vu*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) + complex(0,1)*I118x33*cmath.sin(beta) + complex(0,1)*I116x33*MUH*cmath.sin(beta) + (complex(0,1)*I119x33*vd*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I115x33*vd*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2)) + (complex(0,1)*I121x33*vu*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1650 = Coupling(name = 'GC_1650',
                   value = 'complex(0,1)*I117x36*cmath.cos(beta) + complex(0,1)*I120x36*complexconjugate(MUH)*cmath.cos(beta) + (complex(0,1)*I121x36*vd*cmath.cos(beta))/cmath.sqrt(2) + (complex(0,1)*I122x36*vu*cmath.cos(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I115x36*vu*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) + complex(0,1)*I118x36*cmath.sin(beta) + complex(0,1)*I116x36*MUH*cmath.sin(beta) + (complex(0,1)*I119x36*vd*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I115x36*vd*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2)) + (complex(0,1)*I121x36*vu*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1651 = Coupling(name = 'GC_1651',
                   value = 'complex(0,1)*I117x63*cmath.cos(beta) + complex(0,1)*I120x63*complexconjugate(MUH)*cmath.cos(beta) + (complex(0,1)*I121x63*vd*cmath.cos(beta))/cmath.sqrt(2) + (complex(0,1)*I122x63*vu*cmath.cos(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I115x63*vu*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) + complex(0,1)*I118x63*cmath.sin(beta) + complex(0,1)*I116x63*MUH*cmath.sin(beta) + (complex(0,1)*I119x63*vd*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I115x63*vd*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2)) + (complex(0,1)*I121x63*vu*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1652 = Coupling(name = 'GC_1652',
                   value = 'complex(0,1)*I117x66*cmath.cos(beta) + complex(0,1)*I120x66*complexconjugate(MUH)*cmath.cos(beta) + (complex(0,1)*I121x66*vd*cmath.cos(beta))/cmath.sqrt(2) + (complex(0,1)*I122x66*vu*cmath.cos(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I115x66*vu*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) + complex(0,1)*I118x66*cmath.sin(beta) + complex(0,1)*I116x66*MUH*cmath.sin(beta) + (complex(0,1)*I119x66*vd*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I115x66*vd*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2)) + (complex(0,1)*I121x66*vu*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1653 = Coupling(name = 'GC_1653',
                   value = '-(ee**2*vd*cmath.cos(beta))/(4.*sw**2) - (ee**2*vu*cmath.sin(beta))/(4.*sw**2)',
                   order = {'QED':1})

GC_1654 = Coupling(name = 'GC_1654',
                   value = '(ee**2*vd*cmath.cos(beta))/(4.*sw**2) + (ee**2*vu*cmath.sin(beta))/(4.*sw**2)',
                   order = {'QED':1})

GC_1655 = Coupling(name = 'GC_1655',
                   value = '(ee**2*complex(0,1)*vd*cmath.cos(beta))/(4.*cw) - (cw*ee**2*complex(0,1)*vd*cmath.cos(beta))/(4.*sw**2) + (ee**2*complex(0,1)*vu*cmath.sin(beta))/(4.*cw) - (cw*ee**2*complex(0,1)*vu*cmath.sin(beta))/(4.*sw**2)',
                   order = {'QED':1})

GC_1656 = Coupling(name = 'GC_1656',
                   value = '(ee**2*complex(0,1)*vd*cmath.cos(beta))/(4.*cw) + (cw*ee**2*complex(0,1)*vd*cmath.cos(beta))/(4.*sw**2) + (ee**2*complex(0,1)*vu*cmath.sin(beta))/(4.*cw) + (cw*ee**2*complex(0,1)*vu*cmath.sin(beta))/(4.*sw**2)',
                   order = {'QED':1})

GC_1657 = Coupling(name = 'GC_1657',
                   value = '(ee**2*complex(0,1)*I115x11*vd*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) - (ee**2*complex(0,1)*I115x11*vu*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1658 = Coupling(name = 'GC_1658',
                   value = '(ee**2*complex(0,1)*I115x22*vd*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) - (ee**2*complex(0,1)*I115x22*vu*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1659 = Coupling(name = 'GC_1659',
                   value = '(ee**2*complex(0,1)*I136x11*vd*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) - (ee**2*complex(0,1)*I136x11*vu*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1660 = Coupling(name = 'GC_1660',
                   value = '(ee**2*complex(0,1)*I136x22*vd*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) - (ee**2*complex(0,1)*I136x22*vu*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1661 = Coupling(name = 'GC_1661',
                   value = '-(complex(0,1)*I137x33*cmath.cos(beta)) - complex(0,1)*I141x33*complexconjugate(MUH)*cmath.cos(beta) - (complex(0,1)*I140x33*vd*cmath.cos(beta))/cmath.sqrt(2) + (ee**2*complex(0,1)*I136x33*vd*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) - (complex(0,1)*I143x33*vu*cmath.cos(beta))/cmath.sqrt(2) + complex(0,1)*I139x33*cmath.sin(beta) + complex(0,1)*I138x33*MUH*cmath.sin(beta) + (complex(0,1)*I143x33*vd*cmath.sin(beta))/cmath.sqrt(2) + (complex(0,1)*I142x33*vu*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I136x33*vu*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1662 = Coupling(name = 'GC_1662',
                   value = '-(complex(0,1)*I137x36*cmath.cos(beta)) - complex(0,1)*I141x36*complexconjugate(MUH)*cmath.cos(beta) - (complex(0,1)*I140x36*vd*cmath.cos(beta))/cmath.sqrt(2) + (ee**2*complex(0,1)*I136x36*vd*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) - (complex(0,1)*I143x36*vu*cmath.cos(beta))/cmath.sqrt(2) + complex(0,1)*I139x36*cmath.sin(beta) + complex(0,1)*I138x36*MUH*cmath.sin(beta) + (complex(0,1)*I143x36*vd*cmath.sin(beta))/cmath.sqrt(2) + (complex(0,1)*I142x36*vu*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I136x36*vu*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1663 = Coupling(name = 'GC_1663',
                   value = '-(complex(0,1)*I137x63*cmath.cos(beta)) - complex(0,1)*I141x63*complexconjugate(MUH)*cmath.cos(beta) - (complex(0,1)*I140x63*vd*cmath.cos(beta))/cmath.sqrt(2) + (ee**2*complex(0,1)*I136x63*vd*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) - (complex(0,1)*I143x63*vu*cmath.cos(beta))/cmath.sqrt(2) + complex(0,1)*I139x63*cmath.sin(beta) + complex(0,1)*I138x63*MUH*cmath.sin(beta) + (complex(0,1)*I143x63*vd*cmath.sin(beta))/cmath.sqrt(2) + (complex(0,1)*I142x63*vu*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I136x63*vu*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1664 = Coupling(name = 'GC_1664',
                   value = '-(complex(0,1)*I137x66*cmath.cos(beta)) - complex(0,1)*I141x66*complexconjugate(MUH)*cmath.cos(beta) - (complex(0,1)*I140x66*vd*cmath.cos(beta))/cmath.sqrt(2) + (ee**2*complex(0,1)*I136x66*vd*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) - (complex(0,1)*I143x66*vu*cmath.cos(beta))/cmath.sqrt(2) + complex(0,1)*I139x66*cmath.sin(beta) + complex(0,1)*I138x66*MUH*cmath.sin(beta) + (complex(0,1)*I143x66*vd*cmath.sin(beta))/cmath.sqrt(2) + (complex(0,1)*I142x66*vu*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I136x66*vu*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1665 = Coupling(name = 'GC_1665',
                   value = '(ee**2*complex(0,1)*I90x11*vd*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) - (ee**2*complex(0,1)*I90x11*vu*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1666 = Coupling(name = 'GC_1666',
                   value = '(ee**2*complex(0,1)*I90x22*vd*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) - (ee**2*complex(0,1)*I90x22*vu*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1667 = Coupling(name = 'GC_1667',
                   value = '(ee**2*complex(0,1)*I98x11*vd*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) - (ee**2*complex(0,1)*I98x11*vu*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1668 = Coupling(name = 'GC_1668',
                   value = '(ee**2*complex(0,1)*I98x22*vd*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) - (ee**2*complex(0,1)*I98x22*vu*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1669 = Coupling(name = 'GC_1669',
                   value = '-(complex(0,1)*I99x33*cmath.cos(beta)) - (complex(0,1)*I101x33*vd*cmath.cos(beta))/cmath.sqrt(2) + (ee**2*complex(0,1)*I98x33*vd*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) + complex(0,1)*I100x33*MUH*cmath.sin(beta) - (ee**2*complex(0,1)*I98x33*vu*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1670 = Coupling(name = 'GC_1670',
                   value = '-(complex(0,1)*I99x36*cmath.cos(beta)) - (complex(0,1)*I101x36*vd*cmath.cos(beta))/cmath.sqrt(2) + (ee**2*complex(0,1)*I98x36*vd*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) + complex(0,1)*I100x36*MUH*cmath.sin(beta) - (ee**2*complex(0,1)*I98x36*vu*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1671 = Coupling(name = 'GC_1671',
                   value = '-(ee**2*complex(0,1)*vd*cmath.cos(beta))/(2.*sw) - (ee**2*complex(0,1)*vu*cmath.sin(beta))/(2.*sw)',
                   order = {'QED':1})

GC_1672 = Coupling(name = 'GC_1672',
                   value = '(ee**2*complex(0,1)*vd*cmath.cos(beta))/(2.*sw) + (ee**2*complex(0,1)*vu*cmath.sin(beta))/(2.*sw)',
                   order = {'QED':1})

GC_1673 = Coupling(name = 'GC_1673',
                   value = '(cw*ee**2*complex(0,1)*vd*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee**2*complex(0,1)*vu*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1674 = Coupling(name = 'GC_1674',
                   value = '(ee*UU11*VV12*cmath.cos(beta))/(sw*cmath.sqrt(2)) + (ee*UU12*VV11*cmath.sin(beta))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1675 = Coupling(name = 'GC_1675',
                   value = '(ee*UU21*VV12*cmath.cos(beta))/(sw*cmath.sqrt(2)) + (ee*UU22*VV11*cmath.sin(beta))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1676 = Coupling(name = 'GC_1676',
                   value = '(ee*complex(0,1)*NN14*VV11*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN14*sw*VV11*cmath.sin(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN11*VV12*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN12*VV12*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN12*sw*VV12*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1677 = Coupling(name = 'GC_1677',
                   value = '(ee*complex(0,1)*NN24*VV11*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN24*sw*VV11*cmath.sin(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN21*VV12*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN22*VV12*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN22*sw*VV12*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1678 = Coupling(name = 'GC_1678',
                   value = '(ee*complex(0,1)*NN34*VV11*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN34*sw*VV11*cmath.sin(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN31*VV12*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN32*VV12*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN32*sw*VV12*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1679 = Coupling(name = 'GC_1679',
                   value = '(ee*complex(0,1)*NN44*VV11*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN44*sw*VV11*cmath.sin(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN41*VV12*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN42*VV12*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN42*sw*VV12*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1680 = Coupling(name = 'GC_1680',
                   value = '-((ee*UU12*VV11*cmath.cos(beta))/(sw*cmath.sqrt(2))) + (ee*UU11*VV12*cmath.sin(beta))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1681 = Coupling(name = 'GC_1681',
                   value = '-((ee*UU22*VV11*cmath.cos(beta))/(sw*cmath.sqrt(2))) + (ee*UU21*VV12*cmath.sin(beta))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1682 = Coupling(name = 'GC_1682',
                   value = '(ee*UU11*VV22*cmath.cos(beta))/(sw*cmath.sqrt(2)) + (ee*UU12*VV21*cmath.sin(beta))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1683 = Coupling(name = 'GC_1683',
                   value = '(ee*UU21*VV22*cmath.cos(beta))/(sw*cmath.sqrt(2)) + (ee*UU22*VV21*cmath.sin(beta))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1684 = Coupling(name = 'GC_1684',
                   value = '(ee*complex(0,1)*NN14*VV21*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN14*sw*VV21*cmath.sin(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN11*VV22*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN12*VV22*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN12*sw*VV22*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1685 = Coupling(name = 'GC_1685',
                   value = '(ee*complex(0,1)*NN24*VV21*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN24*sw*VV21*cmath.sin(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN21*VV22*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN22*VV22*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN22*sw*VV22*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1686 = Coupling(name = 'GC_1686',
                   value = '(ee*complex(0,1)*NN34*VV21*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN34*sw*VV21*cmath.sin(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN31*VV22*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN32*VV22*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN32*sw*VV22*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1687 = Coupling(name = 'GC_1687',
                   value = '(ee*complex(0,1)*NN44*VV21*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN44*sw*VV21*cmath.sin(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN41*VV22*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN42*VV22*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN42*sw*VV22*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1688 = Coupling(name = 'GC_1688',
                   value = '-((ee*UU12*VV21*cmath.cos(beta))/(sw*cmath.sqrt(2))) + (ee*UU11*VV22*cmath.sin(beta))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1689 = Coupling(name = 'GC_1689',
                   value = '-((ee*UU22*VV21*cmath.cos(beta))/(sw*cmath.sqrt(2))) + (ee*UU21*VV22*cmath.sin(beta))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1690 = Coupling(name = 'GC_1690',
                   value = '-(complex(0,1)*I118x33*cmath.cos(beta)) - complex(0,1)*I116x33*MUH*cmath.cos(beta) - (complex(0,1)*I119x33*vd*cmath.cos(beta))/cmath.sqrt(2) + (ee**2*complex(0,1)*I115x33*vd*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) - (complex(0,1)*I121x33*vu*cmath.cos(beta))/cmath.sqrt(2) + complex(0,1)*I117x33*cmath.sin(beta) + complex(0,1)*I120x33*complexconjugate(MUH)*cmath.sin(beta) + (complex(0,1)*I121x33*vd*cmath.sin(beta))/cmath.sqrt(2) + (complex(0,1)*I122x33*vu*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I115x33*vu*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1691 = Coupling(name = 'GC_1691',
                   value = '-(complex(0,1)*I118x36*cmath.cos(beta)) - complex(0,1)*I116x36*MUH*cmath.cos(beta) - (complex(0,1)*I119x36*vd*cmath.cos(beta))/cmath.sqrt(2) + (ee**2*complex(0,1)*I115x36*vd*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) - (complex(0,1)*I121x36*vu*cmath.cos(beta))/cmath.sqrt(2) + complex(0,1)*I117x36*cmath.sin(beta) + complex(0,1)*I120x36*complexconjugate(MUH)*cmath.sin(beta) + (complex(0,1)*I121x36*vd*cmath.sin(beta))/cmath.sqrt(2) + (complex(0,1)*I122x36*vu*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I115x36*vu*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1692 = Coupling(name = 'GC_1692',
                   value = '-(complex(0,1)*I118x63*cmath.cos(beta)) - complex(0,1)*I116x63*MUH*cmath.cos(beta) - (complex(0,1)*I119x63*vd*cmath.cos(beta))/cmath.sqrt(2) + (ee**2*complex(0,1)*I115x63*vd*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) - (complex(0,1)*I121x63*vu*cmath.cos(beta))/cmath.sqrt(2) + complex(0,1)*I117x63*cmath.sin(beta) + complex(0,1)*I120x63*complexconjugate(MUH)*cmath.sin(beta) + (complex(0,1)*I121x63*vd*cmath.sin(beta))/cmath.sqrt(2) + (complex(0,1)*I122x63*vu*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I115x63*vu*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1693 = Coupling(name = 'GC_1693',
                   value = '-(complex(0,1)*I118x66*cmath.cos(beta)) - complex(0,1)*I116x66*MUH*cmath.cos(beta) - (complex(0,1)*I119x66*vd*cmath.cos(beta))/cmath.sqrt(2) + (ee**2*complex(0,1)*I115x66*vd*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) - (complex(0,1)*I121x66*vu*cmath.cos(beta))/cmath.sqrt(2) + complex(0,1)*I117x66*cmath.sin(beta) + complex(0,1)*I120x66*complexconjugate(MUH)*cmath.sin(beta) + (complex(0,1)*I121x66*vd*cmath.sin(beta))/cmath.sqrt(2) + (complex(0,1)*I122x66*vu*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I115x66*vu*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1694 = Coupling(name = 'GC_1694',
                   value = 'complex(0,1)*I139x33*cmath.cos(beta) + complex(0,1)*I138x33*MUH*cmath.cos(beta) + (complex(0,1)*I143x33*vd*cmath.cos(beta))/cmath.sqrt(2) + (complex(0,1)*I142x33*vu*cmath.cos(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I136x33*vu*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) + complex(0,1)*I137x33*cmath.sin(beta) + complex(0,1)*I141x33*complexconjugate(MUH)*cmath.sin(beta) + (complex(0,1)*I140x33*vd*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I136x33*vd*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2)) + (complex(0,1)*I143x33*vu*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1695 = Coupling(name = 'GC_1695',
                   value = 'complex(0,1)*I139x36*cmath.cos(beta) + complex(0,1)*I138x36*MUH*cmath.cos(beta) + (complex(0,1)*I143x36*vd*cmath.cos(beta))/cmath.sqrt(2) + (complex(0,1)*I142x36*vu*cmath.cos(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I136x36*vu*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) + complex(0,1)*I137x36*cmath.sin(beta) + complex(0,1)*I141x36*complexconjugate(MUH)*cmath.sin(beta) + (complex(0,1)*I140x36*vd*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I136x36*vd*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2)) + (complex(0,1)*I143x36*vu*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1696 = Coupling(name = 'GC_1696',
                   value = 'complex(0,1)*I139x63*cmath.cos(beta) + complex(0,1)*I138x63*MUH*cmath.cos(beta) + (complex(0,1)*I143x63*vd*cmath.cos(beta))/cmath.sqrt(2) + (complex(0,1)*I142x63*vu*cmath.cos(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I136x63*vu*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) + complex(0,1)*I137x63*cmath.sin(beta) + complex(0,1)*I141x63*complexconjugate(MUH)*cmath.sin(beta) + (complex(0,1)*I140x63*vd*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I136x63*vd*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2)) + (complex(0,1)*I143x63*vu*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1697 = Coupling(name = 'GC_1697',
                   value = 'complex(0,1)*I139x66*cmath.cos(beta) + complex(0,1)*I138x66*MUH*cmath.cos(beta) + (complex(0,1)*I143x66*vd*cmath.cos(beta))/cmath.sqrt(2) + (complex(0,1)*I142x66*vu*cmath.cos(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I136x66*vu*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) + complex(0,1)*I137x66*cmath.sin(beta) + complex(0,1)*I141x66*complexconjugate(MUH)*cmath.sin(beta) + (complex(0,1)*I140x66*vd*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I136x66*vd*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2)) + (complex(0,1)*I143x66*vu*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1698 = Coupling(name = 'GC_1698',
                   value = '-((I151x33*cmath.cos(beta))/cmath.sqrt(2)) + (I152x33*cmath.cos(beta))/cmath.sqrt(2) - (I150x33*MUH*cmath.sin(beta))/cmath.sqrt(2) + (I153x33*complexconjugate(MUH)*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1699 = Coupling(name = 'GC_1699',
                   value = '-((I151x36*cmath.cos(beta))/cmath.sqrt(2)) + (I152x36*cmath.cos(beta))/cmath.sqrt(2) - (I150x36*MUH*cmath.sin(beta))/cmath.sqrt(2) + (I153x36*complexconjugate(MUH)*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1700 = Coupling(name = 'GC_1700',
                   value = '-((I151x63*cmath.cos(beta))/cmath.sqrt(2)) + (I152x63*cmath.cos(beta))/cmath.sqrt(2) - (I150x63*MUH*cmath.sin(beta))/cmath.sqrt(2) + (I153x63*complexconjugate(MUH)*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1701 = Coupling(name = 'GC_1701',
                   value = '-((I151x66*cmath.cos(beta))/cmath.sqrt(2)) + (I152x66*cmath.cos(beta))/cmath.sqrt(2) - (I150x66*MUH*cmath.sin(beta))/cmath.sqrt(2) + (I153x66*complexconjugate(MUH)*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1702 = Coupling(name = 'GC_1702',
                   value = '(I17x33*cmath.cos(beta))/cmath.sqrt(2) - (I19x33*cmath.cos(beta))/cmath.sqrt(2) - (I18x33*MUH*cmath.sin(beta))/cmath.sqrt(2) + (I21x33*complexconjugate(MUH)*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1703 = Coupling(name = 'GC_1703',
                   value = '(I17x36*cmath.cos(beta))/cmath.sqrt(2) - (I19x36*cmath.cos(beta))/cmath.sqrt(2) - (I18x36*MUH*cmath.sin(beta))/cmath.sqrt(2) + (I21x36*complexconjugate(MUH)*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1704 = Coupling(name = 'GC_1704',
                   value = '(I17x63*cmath.cos(beta))/cmath.sqrt(2) - (I19x63*cmath.cos(beta))/cmath.sqrt(2) - (I18x63*MUH*cmath.sin(beta))/cmath.sqrt(2) + (I21x63*complexconjugate(MUH)*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1705 = Coupling(name = 'GC_1705',
                   value = '(I17x66*cmath.cos(beta))/cmath.sqrt(2) - (I19x66*cmath.cos(beta))/cmath.sqrt(2) - (I18x66*MUH*cmath.sin(beta))/cmath.sqrt(2) + (I21x66*complexconjugate(MUH)*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1706 = Coupling(name = 'GC_1706',
                   value = '(I55x33*cmath.cos(beta))/cmath.sqrt(2) - (I57x33*cmath.cos(beta))/cmath.sqrt(2) - (I56x33*MUH*cmath.sin(beta))/cmath.sqrt(2) + (I59x33*complexconjugate(MUH)*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1707 = Coupling(name = 'GC_1707',
                   value = '(I55x36*cmath.cos(beta))/cmath.sqrt(2) - (I57x36*cmath.cos(beta))/cmath.sqrt(2) - (I56x36*MUH*cmath.sin(beta))/cmath.sqrt(2) + (I59x36*complexconjugate(MUH)*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1708 = Coupling(name = 'GC_1708',
                   value = '(I55x63*cmath.cos(beta))/cmath.sqrt(2) - (I57x63*cmath.cos(beta))/cmath.sqrt(2) - (I56x63*MUH*cmath.sin(beta))/cmath.sqrt(2) + (I59x63*complexconjugate(MUH)*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1709 = Coupling(name = 'GC_1709',
                   value = '(I55x66*cmath.cos(beta))/cmath.sqrt(2) - (I57x66*cmath.cos(beta))/cmath.sqrt(2) - (I56x66*MUH*cmath.sin(beta))/cmath.sqrt(2) + (I59x66*complexconjugate(MUH)*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1710 = Coupling(name = 'GC_1710',
                   value = '-(complex(0,1)*I91x33*cmath.cos(beta)) - (complex(0,1)*I92x33*vd*cmath.cos(beta))/cmath.sqrt(2) + (ee**2*complex(0,1)*I90x33*vd*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) + complex(0,1)*I93x33*complexconjugate(MUH)*cmath.sin(beta) - (ee**2*complex(0,1)*I90x33*vu*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1711 = Coupling(name = 'GC_1711',
                   value = '-(complex(0,1)*I91x36*cmath.cos(beta)) - (complex(0,1)*I92x36*vd*cmath.cos(beta))/cmath.sqrt(2) + (ee**2*complex(0,1)*I90x36*vd*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) + complex(0,1)*I93x36*complexconjugate(MUH)*cmath.sin(beta) - (ee**2*complex(0,1)*I90x36*vu*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1712 = Coupling(name = 'GC_1712',
                   value = '(cw*ee*complexconjugate(NN11)*complexconjugate(NN14)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) - (ee*complexconjugate(NN12)*complexconjugate(NN14)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) + (ee*sw*complexconjugate(NN12)*complexconjugate(NN14)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) - (cw*ee*complexconjugate(NN11)*complexconjugate(NN13)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) + (ee*complexconjugate(NN12)*complexconjugate(NN13)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*sw*complexconjugate(NN12)*complexconjugate(NN13)*cmath.sin(beta))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1713 = Coupling(name = 'GC_1713',
                   value = '(cw*ee*complexconjugate(NN11)*complexconjugate(NN13)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) - (ee*complexconjugate(NN12)*complexconjugate(NN13)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) + (ee*sw*complexconjugate(NN12)*complexconjugate(NN13)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complexconjugate(NN11)*complexconjugate(NN14)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (ee*complexconjugate(NN12)*complexconjugate(NN14)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) + (ee*sw*complexconjugate(NN12)*complexconjugate(NN14)*cmath.sin(beta))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1714 = Coupling(name = 'GC_1714',
                   value = '(cw*ee*complexconjugate(NN14)*complexconjugate(NN21)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*complexconjugate(NN14)*complexconjugate(NN22)*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*complexconjugate(NN14)*complexconjugate(NN22)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complexconjugate(NN11)*complexconjugate(NN24)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*complexconjugate(NN12)*complexconjugate(NN24)*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*complexconjugate(NN12)*complexconjugate(NN24)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complexconjugate(NN13)*complexconjugate(NN21)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee*complexconjugate(NN13)*complexconjugate(NN22)*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*sw*complexconjugate(NN13)*complexconjugate(NN22)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complexconjugate(NN11)*complexconjugate(NN23)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee*complexconjugate(NN12)*complexconjugate(NN23)*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*sw*complexconjugate(NN12)*complexconjugate(NN23)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1715 = Coupling(name = 'GC_1715',
                   value = '(cw*ee*complexconjugate(NN21)*complexconjugate(NN24)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) - (ee*complexconjugate(NN22)*complexconjugate(NN24)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) + (ee*sw*complexconjugate(NN22)*complexconjugate(NN24)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) - (cw*ee*complexconjugate(NN21)*complexconjugate(NN23)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) + (ee*complexconjugate(NN22)*complexconjugate(NN23)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*sw*complexconjugate(NN22)*complexconjugate(NN23)*cmath.sin(beta))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1716 = Coupling(name = 'GC_1716',
                   value = '(cw*ee*complexconjugate(NN13)*complexconjugate(NN21)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*complexconjugate(NN13)*complexconjugate(NN22)*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*complexconjugate(NN13)*complexconjugate(NN22)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complexconjugate(NN11)*complexconjugate(NN23)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*complexconjugate(NN12)*complexconjugate(NN23)*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*complexconjugate(NN12)*complexconjugate(NN23)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complexconjugate(NN14)*complexconjugate(NN21)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*complexconjugate(NN14)*complexconjugate(NN22)*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*complexconjugate(NN14)*complexconjugate(NN22)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complexconjugate(NN11)*complexconjugate(NN24)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*complexconjugate(NN12)*complexconjugate(NN24)*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*complexconjugate(NN12)*complexconjugate(NN24)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1717 = Coupling(name = 'GC_1717',
                   value = '(cw*ee*complexconjugate(NN21)*complexconjugate(NN23)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) - (ee*complexconjugate(NN22)*complexconjugate(NN23)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) + (ee*sw*complexconjugate(NN22)*complexconjugate(NN23)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complexconjugate(NN21)*complexconjugate(NN24)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (ee*complexconjugate(NN22)*complexconjugate(NN24)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) + (ee*sw*complexconjugate(NN22)*complexconjugate(NN24)*cmath.sin(beta))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1718 = Coupling(name = 'GC_1718',
                   value = '(cw*ee*complexconjugate(NN14)*complexconjugate(NN31)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*complexconjugate(NN14)*complexconjugate(NN32)*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*complexconjugate(NN14)*complexconjugate(NN32)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complexconjugate(NN11)*complexconjugate(NN34)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*complexconjugate(NN12)*complexconjugate(NN34)*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*complexconjugate(NN12)*complexconjugate(NN34)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complexconjugate(NN13)*complexconjugate(NN31)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee*complexconjugate(NN13)*complexconjugate(NN32)*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*sw*complexconjugate(NN13)*complexconjugate(NN32)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complexconjugate(NN11)*complexconjugate(NN33)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee*complexconjugate(NN12)*complexconjugate(NN33)*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*sw*complexconjugate(NN12)*complexconjugate(NN33)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1719 = Coupling(name = 'GC_1719',
                   value = '(cw*ee*complexconjugate(NN24)*complexconjugate(NN31)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*complexconjugate(NN24)*complexconjugate(NN32)*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*complexconjugate(NN24)*complexconjugate(NN32)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complexconjugate(NN21)*complexconjugate(NN34)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*complexconjugate(NN22)*complexconjugate(NN34)*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*complexconjugate(NN22)*complexconjugate(NN34)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complexconjugate(NN23)*complexconjugate(NN31)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee*complexconjugate(NN23)*complexconjugate(NN32)*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*sw*complexconjugate(NN23)*complexconjugate(NN32)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complexconjugate(NN21)*complexconjugate(NN33)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee*complexconjugate(NN22)*complexconjugate(NN33)*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*sw*complexconjugate(NN22)*complexconjugate(NN33)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1720 = Coupling(name = 'GC_1720',
                   value = '(cw*ee*complexconjugate(NN31)*complexconjugate(NN34)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) - (ee*complexconjugate(NN32)*complexconjugate(NN34)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) + (ee*sw*complexconjugate(NN32)*complexconjugate(NN34)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) - (cw*ee*complexconjugate(NN31)*complexconjugate(NN33)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) + (ee*complexconjugate(NN32)*complexconjugate(NN33)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*sw*complexconjugate(NN32)*complexconjugate(NN33)*cmath.sin(beta))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1721 = Coupling(name = 'GC_1721',
                   value = '(cw*ee*complexconjugate(NN13)*complexconjugate(NN31)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*complexconjugate(NN13)*complexconjugate(NN32)*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*complexconjugate(NN13)*complexconjugate(NN32)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complexconjugate(NN11)*complexconjugate(NN33)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*complexconjugate(NN12)*complexconjugate(NN33)*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*complexconjugate(NN12)*complexconjugate(NN33)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complexconjugate(NN14)*complexconjugate(NN31)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*complexconjugate(NN14)*complexconjugate(NN32)*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*complexconjugate(NN14)*complexconjugate(NN32)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complexconjugate(NN11)*complexconjugate(NN34)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*complexconjugate(NN12)*complexconjugate(NN34)*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*complexconjugate(NN12)*complexconjugate(NN34)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1722 = Coupling(name = 'GC_1722',
                   value = '(cw*ee*complexconjugate(NN23)*complexconjugate(NN31)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*complexconjugate(NN23)*complexconjugate(NN32)*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*complexconjugate(NN23)*complexconjugate(NN32)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complexconjugate(NN21)*complexconjugate(NN33)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*complexconjugate(NN22)*complexconjugate(NN33)*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*complexconjugate(NN22)*complexconjugate(NN33)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complexconjugate(NN24)*complexconjugate(NN31)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*complexconjugate(NN24)*complexconjugate(NN32)*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*complexconjugate(NN24)*complexconjugate(NN32)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complexconjugate(NN21)*complexconjugate(NN34)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*complexconjugate(NN22)*complexconjugate(NN34)*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*complexconjugate(NN22)*complexconjugate(NN34)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1723 = Coupling(name = 'GC_1723',
                   value = '(cw*ee*complexconjugate(NN31)*complexconjugate(NN33)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) - (ee*complexconjugate(NN32)*complexconjugate(NN33)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) + (ee*sw*complexconjugate(NN32)*complexconjugate(NN33)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complexconjugate(NN31)*complexconjugate(NN34)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (ee*complexconjugate(NN32)*complexconjugate(NN34)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) + (ee*sw*complexconjugate(NN32)*complexconjugate(NN34)*cmath.sin(beta))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1724 = Coupling(name = 'GC_1724',
                   value = '(cw*ee*complexconjugate(NN14)*complexconjugate(NN41)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*complexconjugate(NN14)*complexconjugate(NN42)*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*complexconjugate(NN14)*complexconjugate(NN42)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complexconjugate(NN11)*complexconjugate(NN44)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*complexconjugate(NN12)*complexconjugate(NN44)*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*complexconjugate(NN12)*complexconjugate(NN44)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complexconjugate(NN13)*complexconjugate(NN41)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee*complexconjugate(NN13)*complexconjugate(NN42)*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*sw*complexconjugate(NN13)*complexconjugate(NN42)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complexconjugate(NN11)*complexconjugate(NN43)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee*complexconjugate(NN12)*complexconjugate(NN43)*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*sw*complexconjugate(NN12)*complexconjugate(NN43)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1725 = Coupling(name = 'GC_1725',
                   value = '(cw*ee*complexconjugate(NN24)*complexconjugate(NN41)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*complexconjugate(NN24)*complexconjugate(NN42)*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*complexconjugate(NN24)*complexconjugate(NN42)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complexconjugate(NN21)*complexconjugate(NN44)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*complexconjugate(NN22)*complexconjugate(NN44)*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*complexconjugate(NN22)*complexconjugate(NN44)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complexconjugate(NN23)*complexconjugate(NN41)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee*complexconjugate(NN23)*complexconjugate(NN42)*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*sw*complexconjugate(NN23)*complexconjugate(NN42)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complexconjugate(NN21)*complexconjugate(NN43)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee*complexconjugate(NN22)*complexconjugate(NN43)*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*sw*complexconjugate(NN22)*complexconjugate(NN43)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1726 = Coupling(name = 'GC_1726',
                   value = '(cw*ee*complexconjugate(NN34)*complexconjugate(NN41)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*complexconjugate(NN34)*complexconjugate(NN42)*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*complexconjugate(NN34)*complexconjugate(NN42)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complexconjugate(NN31)*complexconjugate(NN44)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*complexconjugate(NN32)*complexconjugate(NN44)*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*complexconjugate(NN32)*complexconjugate(NN44)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complexconjugate(NN33)*complexconjugate(NN41)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee*complexconjugate(NN33)*complexconjugate(NN42)*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*sw*complexconjugate(NN33)*complexconjugate(NN42)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complexconjugate(NN31)*complexconjugate(NN43)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee*complexconjugate(NN32)*complexconjugate(NN43)*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*sw*complexconjugate(NN32)*complexconjugate(NN43)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1727 = Coupling(name = 'GC_1727',
                   value = '(cw*ee*complexconjugate(NN41)*complexconjugate(NN44)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) - (ee*complexconjugate(NN42)*complexconjugate(NN44)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) + (ee*sw*complexconjugate(NN42)*complexconjugate(NN44)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) - (cw*ee*complexconjugate(NN41)*complexconjugate(NN43)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) + (ee*complexconjugate(NN42)*complexconjugate(NN43)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*sw*complexconjugate(NN42)*complexconjugate(NN43)*cmath.sin(beta))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1728 = Coupling(name = 'GC_1728',
                   value = '(cw*ee*complexconjugate(NN13)*complexconjugate(NN41)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*complexconjugate(NN13)*complexconjugate(NN42)*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*complexconjugate(NN13)*complexconjugate(NN42)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complexconjugate(NN11)*complexconjugate(NN43)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*complexconjugate(NN12)*complexconjugate(NN43)*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*complexconjugate(NN12)*complexconjugate(NN43)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complexconjugate(NN14)*complexconjugate(NN41)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*complexconjugate(NN14)*complexconjugate(NN42)*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*complexconjugate(NN14)*complexconjugate(NN42)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complexconjugate(NN11)*complexconjugate(NN44)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*complexconjugate(NN12)*complexconjugate(NN44)*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*complexconjugate(NN12)*complexconjugate(NN44)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1729 = Coupling(name = 'GC_1729',
                   value = '(cw*ee*complexconjugate(NN23)*complexconjugate(NN41)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*complexconjugate(NN23)*complexconjugate(NN42)*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*complexconjugate(NN23)*complexconjugate(NN42)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complexconjugate(NN21)*complexconjugate(NN43)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*complexconjugate(NN22)*complexconjugate(NN43)*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*complexconjugate(NN22)*complexconjugate(NN43)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complexconjugate(NN24)*complexconjugate(NN41)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*complexconjugate(NN24)*complexconjugate(NN42)*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*complexconjugate(NN24)*complexconjugate(NN42)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complexconjugate(NN21)*complexconjugate(NN44)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*complexconjugate(NN22)*complexconjugate(NN44)*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*complexconjugate(NN22)*complexconjugate(NN44)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1730 = Coupling(name = 'GC_1730',
                   value = '(cw*ee*complexconjugate(NN33)*complexconjugate(NN41)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*complexconjugate(NN33)*complexconjugate(NN42)*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*complexconjugate(NN33)*complexconjugate(NN42)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complexconjugate(NN31)*complexconjugate(NN43)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*complexconjugate(NN32)*complexconjugate(NN43)*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*complexconjugate(NN32)*complexconjugate(NN43)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complexconjugate(NN34)*complexconjugate(NN41)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*complexconjugate(NN34)*complexconjugate(NN42)*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*complexconjugate(NN34)*complexconjugate(NN42)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complexconjugate(NN31)*complexconjugate(NN44)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*complexconjugate(NN32)*complexconjugate(NN44)*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*complexconjugate(NN32)*complexconjugate(NN44)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1731 = Coupling(name = 'GC_1731',
                   value = '(cw*ee*complexconjugate(NN41)*complexconjugate(NN43)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) - (ee*complexconjugate(NN42)*complexconjugate(NN43)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) + (ee*sw*complexconjugate(NN42)*complexconjugate(NN43)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complexconjugate(NN41)*complexconjugate(NN44)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (ee*complexconjugate(NN42)*complexconjugate(NN44)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) + (ee*sw*complexconjugate(NN42)*complexconjugate(NN44)*cmath.sin(beta))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1732 = Coupling(name = 'GC_1732',
                   value = '(ee*complex(0,1)*complexconjugate(NN13)*complexconjugate(UU11)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN13)*complexconjugate(UU11)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*complexconjugate(NN11)*complexconjugate(UU12)*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*complexconjugate(NN12)*complexconjugate(UU12)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*sw*complexconjugate(NN12)*complexconjugate(UU12)*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1733 = Coupling(name = 'GC_1733',
                   value = '(ee*complex(0,1)*complexconjugate(NN23)*complexconjugate(UU11)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN23)*complexconjugate(UU11)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*complexconjugate(NN21)*complexconjugate(UU12)*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*complexconjugate(NN22)*complexconjugate(UU12)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*sw*complexconjugate(NN22)*complexconjugate(UU12)*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1734 = Coupling(name = 'GC_1734',
                   value = '(ee*complex(0,1)*complexconjugate(NN33)*complexconjugate(UU11)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN33)*complexconjugate(UU11)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*complexconjugate(NN31)*complexconjugate(UU12)*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*complexconjugate(NN32)*complexconjugate(UU12)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*sw*complexconjugate(NN32)*complexconjugate(UU12)*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1735 = Coupling(name = 'GC_1735',
                   value = '(ee*complex(0,1)*complexconjugate(NN43)*complexconjugate(UU11)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN43)*complexconjugate(UU11)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*complexconjugate(NN41)*complexconjugate(UU12)*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*complexconjugate(NN42)*complexconjugate(UU12)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*sw*complexconjugate(NN42)*complexconjugate(UU12)*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1736 = Coupling(name = 'GC_1736',
                   value = '(ee*complex(0,1)*complexconjugate(NN13)*complexconjugate(UU21)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN13)*complexconjugate(UU21)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*complexconjugate(NN11)*complexconjugate(UU22)*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*complexconjugate(NN12)*complexconjugate(UU22)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*sw*complexconjugate(NN12)*complexconjugate(UU22)*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1737 = Coupling(name = 'GC_1737',
                   value = '(ee*complex(0,1)*complexconjugate(NN23)*complexconjugate(UU21)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN23)*complexconjugate(UU21)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*complexconjugate(NN21)*complexconjugate(UU22)*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*complexconjugate(NN22)*complexconjugate(UU22)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*sw*complexconjugate(NN22)*complexconjugate(UU22)*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1738 = Coupling(name = 'GC_1738',
                   value = '(ee*complex(0,1)*complexconjugate(NN33)*complexconjugate(UU21)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN33)*complexconjugate(UU21)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*complexconjugate(NN31)*complexconjugate(UU22)*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*complexconjugate(NN32)*complexconjugate(UU22)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*sw*complexconjugate(NN32)*complexconjugate(UU22)*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1739 = Coupling(name = 'GC_1739',
                   value = '(ee*complex(0,1)*complexconjugate(NN43)*complexconjugate(UU21)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN43)*complexconjugate(UU21)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*complexconjugate(NN41)*complexconjugate(UU22)*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*complexconjugate(NN42)*complexconjugate(UU22)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*sw*complexconjugate(NN42)*complexconjugate(UU22)*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1740 = Coupling(name = 'GC_1740',
                   value = '-((ee*complexconjugate(UU11)*complexconjugate(VV12)*cmath.cos(beta))/(sw*cmath.sqrt(2))) - (ee*complexconjugate(UU12)*complexconjugate(VV11)*cmath.sin(beta))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1741 = Coupling(name = 'GC_1741',
                   value = '-((ee*complexconjugate(UU21)*complexconjugate(VV12)*cmath.cos(beta))/(sw*cmath.sqrt(2))) - (ee*complexconjugate(UU22)*complexconjugate(VV11)*cmath.sin(beta))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1742 = Coupling(name = 'GC_1742',
                   value = '(ee*complex(0,1)*complexconjugate(NN14)*complexconjugate(VV11)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN14)*complexconjugate(VV11)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN11)*complexconjugate(VV12)*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*complexconjugate(NN12)*complexconjugate(VV12)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*sw*complexconjugate(NN12)*complexconjugate(VV12)*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1743 = Coupling(name = 'GC_1743',
                   value = '(ee*complex(0,1)*complexconjugate(NN24)*complexconjugate(VV11)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN24)*complexconjugate(VV11)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN21)*complexconjugate(VV12)*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*complexconjugate(NN22)*complexconjugate(VV12)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*sw*complexconjugate(NN22)*complexconjugate(VV12)*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1744 = Coupling(name = 'GC_1744',
                   value = '(ee*complex(0,1)*complexconjugate(NN34)*complexconjugate(VV11)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN34)*complexconjugate(VV11)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN31)*complexconjugate(VV12)*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*complexconjugate(NN32)*complexconjugate(VV12)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*sw*complexconjugate(NN32)*complexconjugate(VV12)*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1745 = Coupling(name = 'GC_1745',
                   value = '(ee*complex(0,1)*complexconjugate(NN44)*complexconjugate(VV11)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN44)*complexconjugate(VV11)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN41)*complexconjugate(VV12)*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*complexconjugate(NN42)*complexconjugate(VV12)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*sw*complexconjugate(NN42)*complexconjugate(VV12)*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1746 = Coupling(name = 'GC_1746',
                   value = '(ee*complexconjugate(UU12)*complexconjugate(VV11)*cmath.cos(beta))/(sw*cmath.sqrt(2)) - (ee*complexconjugate(UU11)*complexconjugate(VV12)*cmath.sin(beta))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1747 = Coupling(name = 'GC_1747',
                   value = '(ee*complexconjugate(UU22)*complexconjugate(VV11)*cmath.cos(beta))/(sw*cmath.sqrt(2)) - (ee*complexconjugate(UU21)*complexconjugate(VV12)*cmath.sin(beta))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1748 = Coupling(name = 'GC_1748',
                   value = '-((ee*complexconjugate(UU11)*complexconjugate(VV22)*cmath.cos(beta))/(sw*cmath.sqrt(2))) - (ee*complexconjugate(UU12)*complexconjugate(VV21)*cmath.sin(beta))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1749 = Coupling(name = 'GC_1749',
                   value = '-((ee*complexconjugate(UU21)*complexconjugate(VV22)*cmath.cos(beta))/(sw*cmath.sqrt(2))) - (ee*complexconjugate(UU22)*complexconjugate(VV21)*cmath.sin(beta))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1750 = Coupling(name = 'GC_1750',
                   value = '(ee*complex(0,1)*complexconjugate(NN14)*complexconjugate(VV21)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN14)*complexconjugate(VV21)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN11)*complexconjugate(VV22)*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*complexconjugate(NN12)*complexconjugate(VV22)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*sw*complexconjugate(NN12)*complexconjugate(VV22)*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1751 = Coupling(name = 'GC_1751',
                   value = '(ee*complex(0,1)*complexconjugate(NN24)*complexconjugate(VV21)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN24)*complexconjugate(VV21)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN21)*complexconjugate(VV22)*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*complexconjugate(NN22)*complexconjugate(VV22)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*sw*complexconjugate(NN22)*complexconjugate(VV22)*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1752 = Coupling(name = 'GC_1752',
                   value = '(ee*complex(0,1)*complexconjugate(NN34)*complexconjugate(VV21)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN34)*complexconjugate(VV21)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN31)*complexconjugate(VV22)*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*complexconjugate(NN32)*complexconjugate(VV22)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*sw*complexconjugate(NN32)*complexconjugate(VV22)*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1753 = Coupling(name = 'GC_1753',
                   value = '(ee*complex(0,1)*complexconjugate(NN44)*complexconjugate(VV21)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN44)*complexconjugate(VV21)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN41)*complexconjugate(VV22)*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*complexconjugate(NN42)*complexconjugate(VV22)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*sw*complexconjugate(NN42)*complexconjugate(VV22)*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1754 = Coupling(name = 'GC_1754',
                   value = '(ee*complexconjugate(UU12)*complexconjugate(VV21)*cmath.cos(beta))/(sw*cmath.sqrt(2)) - (ee*complexconjugate(UU11)*complexconjugate(VV22)*cmath.sin(beta))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1755 = Coupling(name = 'GC_1755',
                   value = '(ee*complexconjugate(UU22)*complexconjugate(VV21)*cmath.cos(beta))/(sw*cmath.sqrt(2)) - (ee*complexconjugate(UU21)*complexconjugate(VV22)*cmath.sin(beta))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1756 = Coupling(name = 'GC_1756',
                   value = '-(ee**2*complex(0,1)*I102x11*cmath.cos(beta)*cmath.sin(alp))/(2.*sw**2*cmath.sqrt(2)) - (ee**2*complex(0,1)*I102x11*cmath.cos(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1757 = Coupling(name = 'GC_1757',
                   value = '-(ee**2*complex(0,1)*I102x22*cmath.cos(beta)*cmath.sin(alp))/(2.*sw**2*cmath.sqrt(2)) - (ee**2*complex(0,1)*I102x22*cmath.cos(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1758 = Coupling(name = 'GC_1758',
                   value = '(complex(0,1)*I103x33*cmath.cos(beta)*cmath.sin(alp))/cmath.sqrt(2) - (ee**2*complex(0,1)*I102x33*cmath.cos(beta)*cmath.sin(alp))/(2.*sw**2*cmath.sqrt(2)) - (ee**2*complex(0,1)*I102x33*cmath.cos(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1759 = Coupling(name = 'GC_1759',
                   value = '-(ee**2*complex(0,1)*I102x33*cmath.cos(beta)*cmath.sin(alp))/(2.*sw**2*cmath.sqrt(2)) + (complex(0,1)*I103x33*cmath.cos(alp)*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I102x33*cmath.cos(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1760 = Coupling(name = 'GC_1760',
                   value = '(complex(0,1)*I103x36*cmath.cos(beta)*cmath.sin(alp))/cmath.sqrt(2) - (ee**2*complex(0,1)*I102x36*cmath.cos(beta)*cmath.sin(alp))/(2.*sw**2*cmath.sqrt(2)) - (ee**2*complex(0,1)*I102x36*cmath.cos(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1761 = Coupling(name = 'GC_1761',
                   value = '-(ee**2*complex(0,1)*I102x36*cmath.cos(beta)*cmath.sin(alp))/(2.*sw**2*cmath.sqrt(2)) + (complex(0,1)*I103x36*cmath.cos(alp)*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I102x36*cmath.cos(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1762 = Coupling(name = 'GC_1762',
                   value = '-(ee**2*complex(0,1)*I123x11*cmath.cos(beta)*cmath.sin(alp))/(2.*sw**2*cmath.sqrt(2)) - (ee**2*complex(0,1)*I123x11*cmath.cos(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1763 = Coupling(name = 'GC_1763',
                   value = '-(ee**2*complex(0,1)*I123x22*cmath.cos(beta)*cmath.sin(alp))/(2.*sw**2*cmath.sqrt(2)) - (ee**2*complex(0,1)*I123x22*cmath.cos(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1764 = Coupling(name = 'GC_1764',
                   value = '-(ee**2*complex(0,1)*I144x11*cmath.cos(beta)*cmath.sin(alp))/(2.*sw**2*cmath.sqrt(2)) - (ee**2*complex(0,1)*I144x11*cmath.cos(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1765 = Coupling(name = 'GC_1765',
                   value = '-(ee**2*complex(0,1)*I144x22*cmath.cos(beta)*cmath.sin(alp))/(2.*sw**2*cmath.sqrt(2)) - (ee**2*complex(0,1)*I144x22*cmath.cos(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1766 = Coupling(name = 'GC_1766',
                   value = '-(ee**2*complex(0,1)*I94x11*cmath.cos(beta)*cmath.sin(alp))/(2.*sw**2*cmath.sqrt(2)) - (ee**2*complex(0,1)*I94x11*cmath.cos(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1767 = Coupling(name = 'GC_1767',
                   value = '-(ee**2*complex(0,1)*I94x22*cmath.cos(beta)*cmath.sin(alp))/(2.*sw**2*cmath.sqrt(2)) - (ee**2*complex(0,1)*I94x22*cmath.cos(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1768 = Coupling(name = 'GC_1768',
                   value = '(complex(0,1)*I95x33*cmath.cos(beta)*cmath.sin(alp))/cmath.sqrt(2) - (ee**2*complex(0,1)*I94x33*cmath.cos(beta)*cmath.sin(alp))/(2.*sw**2*cmath.sqrt(2)) - (ee**2*complex(0,1)*I94x33*cmath.cos(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1769 = Coupling(name = 'GC_1769',
                   value = '-(ee**2*complex(0,1)*I94x33*cmath.cos(beta)*cmath.sin(alp))/(2.*sw**2*cmath.sqrt(2)) + (complex(0,1)*I95x33*cmath.cos(alp)*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I94x33*cmath.cos(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1770 = Coupling(name = 'GC_1770',
                   value = '(complex(0,1)*I95x36*cmath.cos(beta)*cmath.sin(alp))/cmath.sqrt(2) - (ee**2*complex(0,1)*I94x36*cmath.cos(beta)*cmath.sin(alp))/(2.*sw**2*cmath.sqrt(2)) - (ee**2*complex(0,1)*I94x36*cmath.cos(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1771 = Coupling(name = 'GC_1771',
                   value = '-(ee**2*complex(0,1)*I94x36*cmath.cos(beta)*cmath.sin(alp))/(2.*sw**2*cmath.sqrt(2)) + (complex(0,1)*I95x36*cmath.cos(alp)*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I94x36*cmath.cos(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1772 = Coupling(name = 'GC_1772',
                   value = '(ee*complex(0,1)*cmath.cos(beta)*cmath.sin(alp))/(2.*sw) - (ee*complex(0,1)*cmath.cos(alp)*cmath.sin(beta))/(2.*sw)',
                   order = {'QED':1})

GC_1773 = Coupling(name = 'GC_1773',
                   value = '-(ee*complex(0,1)*cmath.cos(beta)*cmath.sin(alp))/(2.*sw) + (ee*complex(0,1)*cmath.cos(alp)*cmath.sin(beta))/(2.*sw)',
                   order = {'QED':1})

GC_1774 = Coupling(name = 'GC_1774',
                   value = '(ee**2*complex(0,1)*cmath.cos(beta)*cmath.sin(alp))/(2.*sw) - (ee**2*complex(0,1)*cmath.cos(alp)*cmath.sin(beta))/(2.*sw)',
                   order = {'QED':2})

GC_1775 = Coupling(name = 'GC_1775',
                   value = '-(ee**2*complex(0,1)*cmath.cos(beta)*cmath.sin(alp))/(2.*sw) + (ee**2*complex(0,1)*cmath.cos(alp)*cmath.sin(beta))/(2.*sw)',
                   order = {'QED':2})

GC_1776 = Coupling(name = 'GC_1776',
                   value = '(cw*ee**2*complex(0,1)*cmath.cos(beta)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee**2*complex(0,1)*cmath.cos(alp)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1777 = Coupling(name = 'GC_1777',
                   value = '-(cw*ee**2*complex(0,1)*cmath.cos(beta)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee**2*complex(0,1)*cmath.cos(alp)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1778 = Coupling(name = 'GC_1778',
                   value = '(cw*ee*cmath.cos(beta)*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (cw*ee*cmath.cos(alp)*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1})

GC_1779 = Coupling(name = 'GC_1779',
                   value = '-(cw*ee*cmath.cos(beta)*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*cmath.cos(alp)*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1})

GC_1780 = Coupling(name = 'GC_1780',
                   value = '(I103x33*cmath.cos(beta)*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*I102x33*cmath.cos(beta)*cmath.sin(beta))/(sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1781 = Coupling(name = 'GC_1781',
                   value = '(I103x36*cmath.cos(beta)*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*I102x36*cmath.cos(beta)*cmath.sin(beta))/(sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1782 = Coupling(name = 'GC_1782',
                   value = '-((I95x33*cmath.cos(beta)*cmath.sin(beta))/cmath.sqrt(2)) + (ee**2*I94x33*cmath.cos(beta)*cmath.sin(beta))/(sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1783 = Coupling(name = 'GC_1783',
                   value = '-((I95x36*cmath.cos(beta)*cmath.sin(beta))/cmath.sqrt(2)) + (ee**2*I94x36*cmath.cos(beta)*cmath.sin(beta))/(sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1784 = Coupling(name = 'GC_1784',
                   value = '-((ee**2*complex(0,1)*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw))) + (ee**2*complex(0,1)*cmath.cos(beta)*cmath.sin(beta))/(2.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1785 = Coupling(name = 'GC_1785',
                   value = '(2*ee**2*complex(0,1)*I148x11*cmath.cos(beta)*cmath.sin(beta))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I148x11*cmath.cos(beta)*cmath.sin(beta))/(2.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1786 = Coupling(name = 'GC_1786',
                   value = '-(ee**2*complex(0,1)*I148x11*cmath.cos(beta)*cmath.sin(beta))/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I148x11*cmath.cos(beta)*cmath.sin(beta))/(2.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1787 = Coupling(name = 'GC_1787',
                   value = '(2*ee**2*complex(0,1)*I148x22*cmath.cos(beta)*cmath.sin(beta))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I148x22*cmath.cos(beta)*cmath.sin(beta))/(2.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1788 = Coupling(name = 'GC_1788',
                   value = '-(ee**2*complex(0,1)*I148x22*cmath.cos(beta)*cmath.sin(beta))/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I148x22*cmath.cos(beta)*cmath.sin(beta))/(2.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1789 = Coupling(name = 'GC_1789',
                   value = '(2*ee**2*complex(0,1)*I15x11*cmath.cos(beta)*cmath.sin(beta))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I15x11*cmath.cos(beta)*cmath.sin(beta))/(2.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1790 = Coupling(name = 'GC_1790',
                   value = '-(ee**2*complex(0,1)*I15x11*cmath.cos(beta)*cmath.sin(beta))/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15x11*cmath.cos(beta)*cmath.sin(beta))/(2.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1791 = Coupling(name = 'GC_1791',
                   value = '(2*ee**2*complex(0,1)*I15x22*cmath.cos(beta)*cmath.sin(beta))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I15x22*cmath.cos(beta)*cmath.sin(beta))/(2.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1792 = Coupling(name = 'GC_1792',
                   value = '-(ee**2*complex(0,1)*I15x22*cmath.cos(beta)*cmath.sin(beta))/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15x22*cmath.cos(beta)*cmath.sin(beta))/(2.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1793 = Coupling(name = 'GC_1793',
                   value = '-((ee**2*complex(0,1)*I53x11*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw))) + (ee**2*complex(0,1)*I53x11*cmath.cos(beta)*cmath.sin(beta))/(2.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1794 = Coupling(name = 'GC_1794',
                   value = '-((ee**2*complex(0,1)*I53x22*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw))) + (ee**2*complex(0,1)*I53x22*cmath.cos(beta)*cmath.sin(beta))/(2.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1795 = Coupling(name = 'GC_1795',
                   value = '-((ee**2*complex(0,1)*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw))) - (complex(0,1)*I104x33*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*cmath.cos(beta)*cmath.sin(beta))/(2.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*I104x33*sw**2*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1796 = Coupling(name = 'GC_1796',
                   value = '(2*ee**2*complex(0,1)*I148x33*cmath.cos(beta)*cmath.sin(beta))/(3.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I149x33*cmath.cos(beta)*cmath.sin(beta))/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I156x33*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I157x33*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I148x33*cmath.cos(beta)*cmath.sin(beta))/(2.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I156x33*sw**2*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I157x33*sw**2*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1797 = Coupling(name = 'GC_1797',
                   value = '(2*ee**2*complex(0,1)*I148x36*cmath.cos(beta)*cmath.sin(beta))/(3.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I149x36*cmath.cos(beta)*cmath.sin(beta))/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I156x36*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I157x36*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I148x36*cmath.cos(beta)*cmath.sin(beta))/(2.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I156x36*sw**2*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I157x36*sw**2*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1798 = Coupling(name = 'GC_1798',
                   value = '(2*ee**2*complex(0,1)*I148x63*cmath.cos(beta)*cmath.sin(beta))/(3.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I149x63*cmath.cos(beta)*cmath.sin(beta))/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I156x63*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I157x63*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I148x63*cmath.cos(beta)*cmath.sin(beta))/(2.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I156x63*sw**2*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I157x63*sw**2*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1799 = Coupling(name = 'GC_1799',
                   value = '(2*ee**2*complex(0,1)*I148x66*cmath.cos(beta)*cmath.sin(beta))/(3.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I149x66*cmath.cos(beta)*cmath.sin(beta))/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I156x66*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I157x66*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I148x66*cmath.cos(beta)*cmath.sin(beta))/(2.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I156x66*sw**2*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I157x66*sw**2*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1800 = Coupling(name = 'GC_1800',
                   value = '-(ee**2*complex(0,1)*I148x33*cmath.cos(beta)*cmath.sin(beta))/(3.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I149x33*cmath.cos(beta)*cmath.sin(beta))/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I157x33*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I158x33*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I148x33*cmath.cos(beta)*cmath.sin(beta))/(2.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I157x33*sw**2*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I158x33*sw**2*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1801 = Coupling(name = 'GC_1801',
                   value = '-(ee**2*complex(0,1)*I148x36*cmath.cos(beta)*cmath.sin(beta))/(3.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I149x36*cmath.cos(beta)*cmath.sin(beta))/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I157x36*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I158x36*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I148x36*cmath.cos(beta)*cmath.sin(beta))/(2.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I157x36*sw**2*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I158x36*sw**2*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1802 = Coupling(name = 'GC_1802',
                   value = '-(ee**2*complex(0,1)*I148x63*cmath.cos(beta)*cmath.sin(beta))/(3.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I149x63*cmath.cos(beta)*cmath.sin(beta))/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I157x63*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I158x63*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I148x63*cmath.cos(beta)*cmath.sin(beta))/(2.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I157x63*sw**2*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I158x63*sw**2*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1803 = Coupling(name = 'GC_1803',
                   value = '-(ee**2*complex(0,1)*I148x66*cmath.cos(beta)*cmath.sin(beta))/(3.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I149x66*cmath.cos(beta)*cmath.sin(beta))/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I157x66*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I158x66*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I148x66*cmath.cos(beta)*cmath.sin(beta))/(2.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I157x66*sw**2*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I158x66*sw**2*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1804 = Coupling(name = 'GC_1804',
                   value = '-(ee**2*complex(0,1)*I15x33*cmath.cos(beta)*cmath.sin(beta))/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I16x33*cmath.cos(beta)*cmath.sin(beta))/(3.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I23x33*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I24x33*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15x33*cmath.cos(beta)*cmath.sin(beta))/(2.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*I23x33*sw**2*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I24x33*sw**2*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1805 = Coupling(name = 'GC_1805',
                   value = '-(ee**2*complex(0,1)*I15x36*cmath.cos(beta)*cmath.sin(beta))/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I16x36*cmath.cos(beta)*cmath.sin(beta))/(3.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I23x36*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I24x36*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15x36*cmath.cos(beta)*cmath.sin(beta))/(2.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*I23x36*sw**2*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I24x36*sw**2*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1806 = Coupling(name = 'GC_1806',
                   value = '-(ee**2*complex(0,1)*I15x63*cmath.cos(beta)*cmath.sin(beta))/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I16x63*cmath.cos(beta)*cmath.sin(beta))/(3.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I23x63*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I24x63*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15x63*cmath.cos(beta)*cmath.sin(beta))/(2.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*I23x63*sw**2*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I24x63*sw**2*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1807 = Coupling(name = 'GC_1807',
                   value = '-(ee**2*complex(0,1)*I15x66*cmath.cos(beta)*cmath.sin(beta))/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I16x66*cmath.cos(beta)*cmath.sin(beta))/(3.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I23x66*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I24x66*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15x66*cmath.cos(beta)*cmath.sin(beta))/(2.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*I23x66*sw**2*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I24x66*sw**2*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1808 = Coupling(name = 'GC_1808',
                   value = '(2*ee**2*complex(0,1)*I15x33*cmath.cos(beta)*cmath.sin(beta))/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I16x33*cmath.cos(beta)*cmath.sin(beta))/(3.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I24x33*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I25x33*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I15x33*cmath.cos(beta)*cmath.sin(beta))/(2.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*I24x33*sw**2*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I25x33*sw**2*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1809 = Coupling(name = 'GC_1809',
                   value = '(2*ee**2*complex(0,1)*I15x36*cmath.cos(beta)*cmath.sin(beta))/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I16x36*cmath.cos(beta)*cmath.sin(beta))/(3.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I24x36*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I25x36*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I15x36*cmath.cos(beta)*cmath.sin(beta))/(2.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*I24x36*sw**2*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I25x36*sw**2*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1810 = Coupling(name = 'GC_1810',
                   value = '(2*ee**2*complex(0,1)*I15x63*cmath.cos(beta)*cmath.sin(beta))/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I16x63*cmath.cos(beta)*cmath.sin(beta))/(3.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I24x63*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I25x63*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I15x63*cmath.cos(beta)*cmath.sin(beta))/(2.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*I24x63*sw**2*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I25x63*sw**2*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1811 = Coupling(name = 'GC_1811',
                   value = '(2*ee**2*complex(0,1)*I15x66*cmath.cos(beta)*cmath.sin(beta))/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I16x66*cmath.cos(beta)*cmath.sin(beta))/(3.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I24x66*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I25x66*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I15x66*cmath.cos(beta)*cmath.sin(beta))/(2.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*I24x66*sw**2*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I25x66*sw**2*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1812 = Coupling(name = 'GC_1812',
                   value = '(ee**2*complex(0,1)*I54x33*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I62x33*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I53x33*cmath.cos(beta)*cmath.sin(beta))/(2.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*I62x33*sw**2*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1813 = Coupling(name = 'GC_1813',
                   value = '-((ee**2*complex(0,1)*I53x33*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw))) + (ee**2*complex(0,1)*I54x33*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I61x33*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I62x33*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I53x33*cmath.cos(beta)*cmath.sin(beta))/(2.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*I61x33*sw**2*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I62x33*sw**2*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1814 = Coupling(name = 'GC_1814',
                   value = '(ee**2*complex(0,1)*I54x36*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I62x36*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I53x36*cmath.cos(beta)*cmath.sin(beta))/(2.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*I62x36*sw**2*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1815 = Coupling(name = 'GC_1815',
                   value = '-((ee**2*complex(0,1)*I53x36*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw))) + (ee**2*complex(0,1)*I54x36*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I61x36*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I62x36*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I53x36*cmath.cos(beta)*cmath.sin(beta))/(2.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*I61x36*sw**2*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I62x36*sw**2*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1816 = Coupling(name = 'GC_1816',
                   value = '(ee**2*complex(0,1)*I54x63*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I62x63*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I53x63*cmath.cos(beta)*cmath.sin(beta))/(2.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*I62x63*sw**2*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1817 = Coupling(name = 'GC_1817',
                   value = '-((ee**2*complex(0,1)*I53x63*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw))) + (ee**2*complex(0,1)*I54x63*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I61x63*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I62x63*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I53x63*cmath.cos(beta)*cmath.sin(beta))/(2.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*I61x63*sw**2*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I62x63*sw**2*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1818 = Coupling(name = 'GC_1818',
                   value = '(ee**2*complex(0,1)*I54x66*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I62x66*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I53x66*cmath.cos(beta)*cmath.sin(beta))/(2.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*I62x66*sw**2*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1819 = Coupling(name = 'GC_1819',
                   value = '-((ee**2*complex(0,1)*I53x66*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw))) + (ee**2*complex(0,1)*I54x66*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I61x66*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I62x66*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I53x66*cmath.cos(beta)*cmath.sin(beta))/(2.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*I61x66*sw**2*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I62x66*sw**2*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1820 = Coupling(name = 'GC_1820',
                   value = '-((complex(0,1)*I125x33*cmath.cos(alp)*cmath.cos(beta))/cmath.sqrt(2)) + (complex(0,1)*I124x33*cmath.cos(beta)*cmath.sin(alp))/cmath.sqrt(2) - (ee**2*complex(0,1)*I123x33*cmath.cos(beta)*cmath.sin(alp))/(2.*sw**2*cmath.sqrt(2)) + (complex(0,1)*I126x33*cmath.cos(alp)*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I123x33*cmath.cos(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2)) - (complex(0,1)*I125x33*cmath.sin(alp)*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':2})

GC_1821 = Coupling(name = 'GC_1821',
                   value = '(complex(0,1)*I125x33*cmath.cos(alp)*cmath.cos(beta))/cmath.sqrt(2) + (complex(0,1)*I126x33*cmath.cos(beta)*cmath.sin(alp))/cmath.sqrt(2) - (ee**2*complex(0,1)*I123x33*cmath.cos(beta)*cmath.sin(alp))/(2.*sw**2*cmath.sqrt(2)) + (complex(0,1)*I124x33*cmath.cos(alp)*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I123x33*cmath.cos(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2)) + (complex(0,1)*I125x33*cmath.sin(alp)*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':2})

GC_1822 = Coupling(name = 'GC_1822',
                   value = '-((complex(0,1)*I125x36*cmath.cos(alp)*cmath.cos(beta))/cmath.sqrt(2)) + (complex(0,1)*I124x36*cmath.cos(beta)*cmath.sin(alp))/cmath.sqrt(2) - (ee**2*complex(0,1)*I123x36*cmath.cos(beta)*cmath.sin(alp))/(2.*sw**2*cmath.sqrt(2)) + (complex(0,1)*I126x36*cmath.cos(alp)*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I123x36*cmath.cos(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2)) - (complex(0,1)*I125x36*cmath.sin(alp)*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':2})

GC_1823 = Coupling(name = 'GC_1823',
                   value = '(complex(0,1)*I125x36*cmath.cos(alp)*cmath.cos(beta))/cmath.sqrt(2) + (complex(0,1)*I126x36*cmath.cos(beta)*cmath.sin(alp))/cmath.sqrt(2) - (ee**2*complex(0,1)*I123x36*cmath.cos(beta)*cmath.sin(alp))/(2.*sw**2*cmath.sqrt(2)) + (complex(0,1)*I124x36*cmath.cos(alp)*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I123x36*cmath.cos(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2)) + (complex(0,1)*I125x36*cmath.sin(alp)*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':2})

GC_1824 = Coupling(name = 'GC_1824',
                   value = '-((complex(0,1)*I125x63*cmath.cos(alp)*cmath.cos(beta))/cmath.sqrt(2)) + (complex(0,1)*I124x63*cmath.cos(beta)*cmath.sin(alp))/cmath.sqrt(2) - (ee**2*complex(0,1)*I123x63*cmath.cos(beta)*cmath.sin(alp))/(2.*sw**2*cmath.sqrt(2)) + (complex(0,1)*I126x63*cmath.cos(alp)*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I123x63*cmath.cos(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2)) - (complex(0,1)*I125x63*cmath.sin(alp)*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':2})

GC_1825 = Coupling(name = 'GC_1825',
                   value = '(complex(0,1)*I125x63*cmath.cos(alp)*cmath.cos(beta))/cmath.sqrt(2) + (complex(0,1)*I126x63*cmath.cos(beta)*cmath.sin(alp))/cmath.sqrt(2) - (ee**2*complex(0,1)*I123x63*cmath.cos(beta)*cmath.sin(alp))/(2.*sw**2*cmath.sqrt(2)) + (complex(0,1)*I124x63*cmath.cos(alp)*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I123x63*cmath.cos(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2)) + (complex(0,1)*I125x63*cmath.sin(alp)*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':2})

GC_1826 = Coupling(name = 'GC_1826',
                   value = '-((complex(0,1)*I125x66*cmath.cos(alp)*cmath.cos(beta))/cmath.sqrt(2)) + (complex(0,1)*I124x66*cmath.cos(beta)*cmath.sin(alp))/cmath.sqrt(2) - (ee**2*complex(0,1)*I123x66*cmath.cos(beta)*cmath.sin(alp))/(2.*sw**2*cmath.sqrt(2)) + (complex(0,1)*I126x66*cmath.cos(alp)*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I123x66*cmath.cos(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2)) - (complex(0,1)*I125x66*cmath.sin(alp)*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':2})

GC_1827 = Coupling(name = 'GC_1827',
                   value = '(complex(0,1)*I125x66*cmath.cos(alp)*cmath.cos(beta))/cmath.sqrt(2) + (complex(0,1)*I126x66*cmath.cos(beta)*cmath.sin(alp))/cmath.sqrt(2) - (ee**2*complex(0,1)*I123x66*cmath.cos(beta)*cmath.sin(alp))/(2.*sw**2*cmath.sqrt(2)) + (complex(0,1)*I124x66*cmath.cos(alp)*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I123x66*cmath.cos(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2)) + (complex(0,1)*I125x66*cmath.sin(alp)*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':2})

GC_1828 = Coupling(name = 'GC_1828',
                   value = '-((complex(0,1)*I147x33*cmath.cos(alp)*cmath.cos(beta))/cmath.sqrt(2)) + (complex(0,1)*I145x33*cmath.cos(beta)*cmath.sin(alp))/cmath.sqrt(2) - (ee**2*complex(0,1)*I144x33*cmath.cos(beta)*cmath.sin(alp))/(2.*sw**2*cmath.sqrt(2)) + (complex(0,1)*I146x33*cmath.cos(alp)*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I144x33*cmath.cos(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2)) - (complex(0,1)*I147x33*cmath.sin(alp)*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':2})

GC_1829 = Coupling(name = 'GC_1829',
                   value = '(complex(0,1)*I147x33*cmath.cos(alp)*cmath.cos(beta))/cmath.sqrt(2) + (complex(0,1)*I146x33*cmath.cos(beta)*cmath.sin(alp))/cmath.sqrt(2) - (ee**2*complex(0,1)*I144x33*cmath.cos(beta)*cmath.sin(alp))/(2.*sw**2*cmath.sqrt(2)) + (complex(0,1)*I145x33*cmath.cos(alp)*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I144x33*cmath.cos(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2)) + (complex(0,1)*I147x33*cmath.sin(alp)*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':2})

GC_1830 = Coupling(name = 'GC_1830',
                   value = '-((complex(0,1)*I147x36*cmath.cos(alp)*cmath.cos(beta))/cmath.sqrt(2)) + (complex(0,1)*I145x36*cmath.cos(beta)*cmath.sin(alp))/cmath.sqrt(2) - (ee**2*complex(0,1)*I144x36*cmath.cos(beta)*cmath.sin(alp))/(2.*sw**2*cmath.sqrt(2)) + (complex(0,1)*I146x36*cmath.cos(alp)*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I144x36*cmath.cos(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2)) - (complex(0,1)*I147x36*cmath.sin(alp)*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':2})

GC_1831 = Coupling(name = 'GC_1831',
                   value = '(complex(0,1)*I147x36*cmath.cos(alp)*cmath.cos(beta))/cmath.sqrt(2) + (complex(0,1)*I146x36*cmath.cos(beta)*cmath.sin(alp))/cmath.sqrt(2) - (ee**2*complex(0,1)*I144x36*cmath.cos(beta)*cmath.sin(alp))/(2.*sw**2*cmath.sqrt(2)) + (complex(0,1)*I145x36*cmath.cos(alp)*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I144x36*cmath.cos(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2)) + (complex(0,1)*I147x36*cmath.sin(alp)*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':2})

GC_1832 = Coupling(name = 'GC_1832',
                   value = '-((complex(0,1)*I147x63*cmath.cos(alp)*cmath.cos(beta))/cmath.sqrt(2)) + (complex(0,1)*I145x63*cmath.cos(beta)*cmath.sin(alp))/cmath.sqrt(2) - (ee**2*complex(0,1)*I144x63*cmath.cos(beta)*cmath.sin(alp))/(2.*sw**2*cmath.sqrt(2)) + (complex(0,1)*I146x63*cmath.cos(alp)*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I144x63*cmath.cos(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2)) - (complex(0,1)*I147x63*cmath.sin(alp)*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':2})

GC_1833 = Coupling(name = 'GC_1833',
                   value = '(complex(0,1)*I147x63*cmath.cos(alp)*cmath.cos(beta))/cmath.sqrt(2) + (complex(0,1)*I146x63*cmath.cos(beta)*cmath.sin(alp))/cmath.sqrt(2) - (ee**2*complex(0,1)*I144x63*cmath.cos(beta)*cmath.sin(alp))/(2.*sw**2*cmath.sqrt(2)) + (complex(0,1)*I145x63*cmath.cos(alp)*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I144x63*cmath.cos(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2)) + (complex(0,1)*I147x63*cmath.sin(alp)*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':2})

GC_1834 = Coupling(name = 'GC_1834',
                   value = '-((complex(0,1)*I147x66*cmath.cos(alp)*cmath.cos(beta))/cmath.sqrt(2)) + (complex(0,1)*I145x66*cmath.cos(beta)*cmath.sin(alp))/cmath.sqrt(2) - (ee**2*complex(0,1)*I144x66*cmath.cos(beta)*cmath.sin(alp))/(2.*sw**2*cmath.sqrt(2)) + (complex(0,1)*I146x66*cmath.cos(alp)*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I144x66*cmath.cos(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2)) - (complex(0,1)*I147x66*cmath.sin(alp)*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':2})

GC_1835 = Coupling(name = 'GC_1835',
                   value = '(complex(0,1)*I147x66*cmath.cos(alp)*cmath.cos(beta))/cmath.sqrt(2) + (complex(0,1)*I146x66*cmath.cos(beta)*cmath.sin(alp))/cmath.sqrt(2) - (ee**2*complex(0,1)*I144x66*cmath.cos(beta)*cmath.sin(alp))/(2.*sw**2*cmath.sqrt(2)) + (complex(0,1)*I145x66*cmath.cos(alp)*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I144x66*cmath.cos(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2)) + (complex(0,1)*I147x66*cmath.sin(alp)*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':2})

GC_1836 = Coupling(name = 'GC_1836',
                   value = '(ee**2*complex(0,1)*I102x11*cmath.cos(alp)*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) - (ee**2*complex(0,1)*I102x11*cmath.sin(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1837 = Coupling(name = 'GC_1837',
                   value = '-(ee**2*complex(0,1)*I102x11*cmath.cos(alp)*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) + (ee**2*complex(0,1)*I102x11*cmath.sin(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1838 = Coupling(name = 'GC_1838',
                   value = '(ee**2*complex(0,1)*I102x22*cmath.cos(alp)*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) - (ee**2*complex(0,1)*I102x22*cmath.sin(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1839 = Coupling(name = 'GC_1839',
                   value = '-(ee**2*complex(0,1)*I102x22*cmath.cos(alp)*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) + (ee**2*complex(0,1)*I102x22*cmath.sin(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1840 = Coupling(name = 'GC_1840',
                   value = '-((complex(0,1)*I103x33*cmath.cos(alp)*cmath.cos(beta))/cmath.sqrt(2)) + (ee**2*complex(0,1)*I102x33*cmath.cos(alp)*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) - (ee**2*complex(0,1)*I102x33*cmath.sin(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1841 = Coupling(name = 'GC_1841',
                   value = '-(ee**2*complex(0,1)*I102x33*cmath.cos(alp)*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) - (complex(0,1)*I103x33*cmath.sin(alp)*cmath.sin(beta))/cmath.sqrt(2) + (ee**2*complex(0,1)*I102x33*cmath.sin(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1842 = Coupling(name = 'GC_1842',
                   value = '-((complex(0,1)*I103x36*cmath.cos(alp)*cmath.cos(beta))/cmath.sqrt(2)) + (ee**2*complex(0,1)*I102x36*cmath.cos(alp)*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) - (ee**2*complex(0,1)*I102x36*cmath.sin(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1843 = Coupling(name = 'GC_1843',
                   value = '-(ee**2*complex(0,1)*I102x36*cmath.cos(alp)*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) - (complex(0,1)*I103x36*cmath.sin(alp)*cmath.sin(beta))/cmath.sqrt(2) + (ee**2*complex(0,1)*I102x36*cmath.sin(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1844 = Coupling(name = 'GC_1844',
                   value = '(ee**2*complex(0,1)*I123x11*cmath.cos(alp)*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) - (ee**2*complex(0,1)*I123x11*cmath.sin(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1845 = Coupling(name = 'GC_1845',
                   value = '-(ee**2*complex(0,1)*I123x11*cmath.cos(alp)*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) + (ee**2*complex(0,1)*I123x11*cmath.sin(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1846 = Coupling(name = 'GC_1846',
                   value = '(ee**2*complex(0,1)*I123x22*cmath.cos(alp)*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) - (ee**2*complex(0,1)*I123x22*cmath.sin(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1847 = Coupling(name = 'GC_1847',
                   value = '-(ee**2*complex(0,1)*I123x22*cmath.cos(alp)*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) + (ee**2*complex(0,1)*I123x22*cmath.sin(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1848 = Coupling(name = 'GC_1848',
                   value = '-((complex(0,1)*I124x33*cmath.cos(alp)*cmath.cos(beta))/cmath.sqrt(2)) + (ee**2*complex(0,1)*I123x33*cmath.cos(alp)*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) - (complex(0,1)*I125x33*cmath.cos(beta)*cmath.sin(alp))/cmath.sqrt(2) + (complex(0,1)*I125x33*cmath.cos(alp)*cmath.sin(beta))/cmath.sqrt(2) + (complex(0,1)*I126x33*cmath.sin(alp)*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I123x33*cmath.sin(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1849 = Coupling(name = 'GC_1849',
                   value = '(complex(0,1)*I126x33*cmath.cos(alp)*cmath.cos(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I123x33*cmath.cos(alp)*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) - (complex(0,1)*I125x33*cmath.cos(beta)*cmath.sin(alp))/cmath.sqrt(2) + (complex(0,1)*I125x33*cmath.cos(alp)*cmath.sin(beta))/cmath.sqrt(2) - (complex(0,1)*I124x33*cmath.sin(alp)*cmath.sin(beta))/cmath.sqrt(2) + (ee**2*complex(0,1)*I123x33*cmath.sin(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1850 = Coupling(name = 'GC_1850',
                   value = '-((complex(0,1)*I124x36*cmath.cos(alp)*cmath.cos(beta))/cmath.sqrt(2)) + (ee**2*complex(0,1)*I123x36*cmath.cos(alp)*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) - (complex(0,1)*I125x36*cmath.cos(beta)*cmath.sin(alp))/cmath.sqrt(2) + (complex(0,1)*I125x36*cmath.cos(alp)*cmath.sin(beta))/cmath.sqrt(2) + (complex(0,1)*I126x36*cmath.sin(alp)*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I123x36*cmath.sin(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1851 = Coupling(name = 'GC_1851',
                   value = '(complex(0,1)*I126x36*cmath.cos(alp)*cmath.cos(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I123x36*cmath.cos(alp)*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) - (complex(0,1)*I125x36*cmath.cos(beta)*cmath.sin(alp))/cmath.sqrt(2) + (complex(0,1)*I125x36*cmath.cos(alp)*cmath.sin(beta))/cmath.sqrt(2) - (complex(0,1)*I124x36*cmath.sin(alp)*cmath.sin(beta))/cmath.sqrt(2) + (ee**2*complex(0,1)*I123x36*cmath.sin(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1852 = Coupling(name = 'GC_1852',
                   value = '-((complex(0,1)*I124x63*cmath.cos(alp)*cmath.cos(beta))/cmath.sqrt(2)) + (ee**2*complex(0,1)*I123x63*cmath.cos(alp)*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) - (complex(0,1)*I125x63*cmath.cos(beta)*cmath.sin(alp))/cmath.sqrt(2) + (complex(0,1)*I125x63*cmath.cos(alp)*cmath.sin(beta))/cmath.sqrt(2) + (complex(0,1)*I126x63*cmath.sin(alp)*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I123x63*cmath.sin(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1853 = Coupling(name = 'GC_1853',
                   value = '(complex(0,1)*I126x63*cmath.cos(alp)*cmath.cos(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I123x63*cmath.cos(alp)*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) - (complex(0,1)*I125x63*cmath.cos(beta)*cmath.sin(alp))/cmath.sqrt(2) + (complex(0,1)*I125x63*cmath.cos(alp)*cmath.sin(beta))/cmath.sqrt(2) - (complex(0,1)*I124x63*cmath.sin(alp)*cmath.sin(beta))/cmath.sqrt(2) + (ee**2*complex(0,1)*I123x63*cmath.sin(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1854 = Coupling(name = 'GC_1854',
                   value = '-((complex(0,1)*I124x66*cmath.cos(alp)*cmath.cos(beta))/cmath.sqrt(2)) + (ee**2*complex(0,1)*I123x66*cmath.cos(alp)*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) - (complex(0,1)*I125x66*cmath.cos(beta)*cmath.sin(alp))/cmath.sqrt(2) + (complex(0,1)*I125x66*cmath.cos(alp)*cmath.sin(beta))/cmath.sqrt(2) + (complex(0,1)*I126x66*cmath.sin(alp)*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I123x66*cmath.sin(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1855 = Coupling(name = 'GC_1855',
                   value = '(complex(0,1)*I126x66*cmath.cos(alp)*cmath.cos(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I123x66*cmath.cos(alp)*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) - (complex(0,1)*I125x66*cmath.cos(beta)*cmath.sin(alp))/cmath.sqrt(2) + (complex(0,1)*I125x66*cmath.cos(alp)*cmath.sin(beta))/cmath.sqrt(2) - (complex(0,1)*I124x66*cmath.sin(alp)*cmath.sin(beta))/cmath.sqrt(2) + (ee**2*complex(0,1)*I123x66*cmath.sin(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1856 = Coupling(name = 'GC_1856',
                   value = '(ee**2*complex(0,1)*I144x11*cmath.cos(alp)*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) - (ee**2*complex(0,1)*I144x11*cmath.sin(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1857 = Coupling(name = 'GC_1857',
                   value = '-(ee**2*complex(0,1)*I144x11*cmath.cos(alp)*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) + (ee**2*complex(0,1)*I144x11*cmath.sin(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1858 = Coupling(name = 'GC_1858',
                   value = '(ee**2*complex(0,1)*I144x22*cmath.cos(alp)*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) - (ee**2*complex(0,1)*I144x22*cmath.sin(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1859 = Coupling(name = 'GC_1859',
                   value = '-(ee**2*complex(0,1)*I144x22*cmath.cos(alp)*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) + (ee**2*complex(0,1)*I144x22*cmath.sin(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1860 = Coupling(name = 'GC_1860',
                   value = '-((complex(0,1)*I145x33*cmath.cos(alp)*cmath.cos(beta))/cmath.sqrt(2)) + (ee**2*complex(0,1)*I144x33*cmath.cos(alp)*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) - (complex(0,1)*I147x33*cmath.cos(beta)*cmath.sin(alp))/cmath.sqrt(2) + (complex(0,1)*I147x33*cmath.cos(alp)*cmath.sin(beta))/cmath.sqrt(2) + (complex(0,1)*I146x33*cmath.sin(alp)*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I144x33*cmath.sin(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1861 = Coupling(name = 'GC_1861',
                   value = '(complex(0,1)*I146x33*cmath.cos(alp)*cmath.cos(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I144x33*cmath.cos(alp)*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) - (complex(0,1)*I147x33*cmath.cos(beta)*cmath.sin(alp))/cmath.sqrt(2) + (complex(0,1)*I147x33*cmath.cos(alp)*cmath.sin(beta))/cmath.sqrt(2) - (complex(0,1)*I145x33*cmath.sin(alp)*cmath.sin(beta))/cmath.sqrt(2) + (ee**2*complex(0,1)*I144x33*cmath.sin(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1862 = Coupling(name = 'GC_1862',
                   value = '-((complex(0,1)*I145x36*cmath.cos(alp)*cmath.cos(beta))/cmath.sqrt(2)) + (ee**2*complex(0,1)*I144x36*cmath.cos(alp)*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) - (complex(0,1)*I147x36*cmath.cos(beta)*cmath.sin(alp))/cmath.sqrt(2) + (complex(0,1)*I147x36*cmath.cos(alp)*cmath.sin(beta))/cmath.sqrt(2) + (complex(0,1)*I146x36*cmath.sin(alp)*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I144x36*cmath.sin(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1863 = Coupling(name = 'GC_1863',
                   value = '(complex(0,1)*I146x36*cmath.cos(alp)*cmath.cos(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I144x36*cmath.cos(alp)*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) - (complex(0,1)*I147x36*cmath.cos(beta)*cmath.sin(alp))/cmath.sqrt(2) + (complex(0,1)*I147x36*cmath.cos(alp)*cmath.sin(beta))/cmath.sqrt(2) - (complex(0,1)*I145x36*cmath.sin(alp)*cmath.sin(beta))/cmath.sqrt(2) + (ee**2*complex(0,1)*I144x36*cmath.sin(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1864 = Coupling(name = 'GC_1864',
                   value = '-((complex(0,1)*I145x63*cmath.cos(alp)*cmath.cos(beta))/cmath.sqrt(2)) + (ee**2*complex(0,1)*I144x63*cmath.cos(alp)*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) - (complex(0,1)*I147x63*cmath.cos(beta)*cmath.sin(alp))/cmath.sqrt(2) + (complex(0,1)*I147x63*cmath.cos(alp)*cmath.sin(beta))/cmath.sqrt(2) + (complex(0,1)*I146x63*cmath.sin(alp)*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I144x63*cmath.sin(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1865 = Coupling(name = 'GC_1865',
                   value = '(complex(0,1)*I146x63*cmath.cos(alp)*cmath.cos(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I144x63*cmath.cos(alp)*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) - (complex(0,1)*I147x63*cmath.cos(beta)*cmath.sin(alp))/cmath.sqrt(2) + (complex(0,1)*I147x63*cmath.cos(alp)*cmath.sin(beta))/cmath.sqrt(2) - (complex(0,1)*I145x63*cmath.sin(alp)*cmath.sin(beta))/cmath.sqrt(2) + (ee**2*complex(0,1)*I144x63*cmath.sin(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1866 = Coupling(name = 'GC_1866',
                   value = '-((complex(0,1)*I145x66*cmath.cos(alp)*cmath.cos(beta))/cmath.sqrt(2)) + (ee**2*complex(0,1)*I144x66*cmath.cos(alp)*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) - (complex(0,1)*I147x66*cmath.cos(beta)*cmath.sin(alp))/cmath.sqrt(2) + (complex(0,1)*I147x66*cmath.cos(alp)*cmath.sin(beta))/cmath.sqrt(2) + (complex(0,1)*I146x66*cmath.sin(alp)*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I144x66*cmath.sin(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1867 = Coupling(name = 'GC_1867',
                   value = '(complex(0,1)*I146x66*cmath.cos(alp)*cmath.cos(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I144x66*cmath.cos(alp)*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) - (complex(0,1)*I147x66*cmath.cos(beta)*cmath.sin(alp))/cmath.sqrt(2) + (complex(0,1)*I147x66*cmath.cos(alp)*cmath.sin(beta))/cmath.sqrt(2) - (complex(0,1)*I145x66*cmath.sin(alp)*cmath.sin(beta))/cmath.sqrt(2) + (ee**2*complex(0,1)*I144x66*cmath.sin(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1868 = Coupling(name = 'GC_1868',
                   value = '(ee**2*complex(0,1)*I94x11*cmath.cos(alp)*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) - (ee**2*complex(0,1)*I94x11*cmath.sin(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1869 = Coupling(name = 'GC_1869',
                   value = '-(ee**2*complex(0,1)*I94x11*cmath.cos(alp)*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) + (ee**2*complex(0,1)*I94x11*cmath.sin(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1870 = Coupling(name = 'GC_1870',
                   value = '(ee**2*complex(0,1)*I94x22*cmath.cos(alp)*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) - (ee**2*complex(0,1)*I94x22*cmath.sin(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1871 = Coupling(name = 'GC_1871',
                   value = '-(ee**2*complex(0,1)*I94x22*cmath.cos(alp)*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) + (ee**2*complex(0,1)*I94x22*cmath.sin(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1872 = Coupling(name = 'GC_1872',
                   value = '-((complex(0,1)*I95x33*cmath.cos(alp)*cmath.cos(beta))/cmath.sqrt(2)) + (ee**2*complex(0,1)*I94x33*cmath.cos(alp)*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) - (ee**2*complex(0,1)*I94x33*cmath.sin(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1873 = Coupling(name = 'GC_1873',
                   value = '-(ee**2*complex(0,1)*I94x33*cmath.cos(alp)*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) - (complex(0,1)*I95x33*cmath.sin(alp)*cmath.sin(beta))/cmath.sqrt(2) + (ee**2*complex(0,1)*I94x33*cmath.sin(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1874 = Coupling(name = 'GC_1874',
                   value = '-((complex(0,1)*I95x36*cmath.cos(alp)*cmath.cos(beta))/cmath.sqrt(2)) + (ee**2*complex(0,1)*I94x36*cmath.cos(alp)*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) - (ee**2*complex(0,1)*I94x36*cmath.sin(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1875 = Coupling(name = 'GC_1875',
                   value = '-(ee**2*complex(0,1)*I94x36*cmath.cos(alp)*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) - (complex(0,1)*I95x36*cmath.sin(alp)*cmath.sin(beta))/cmath.sqrt(2) + (ee**2*complex(0,1)*I94x36*cmath.sin(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1876 = Coupling(name = 'GC_1876',
                   value = '-(ee*complex(0,1)*cmath.cos(alp)*cmath.cos(beta))/(2.*sw) - (ee*complex(0,1)*cmath.sin(alp)*cmath.sin(beta))/(2.*sw)',
                   order = {'QED':1})

GC_1877 = Coupling(name = 'GC_1877',
                   value = '(ee*complex(0,1)*cmath.cos(alp)*cmath.cos(beta))/(2.*sw) + (ee*complex(0,1)*cmath.sin(alp)*cmath.sin(beta))/(2.*sw)',
                   order = {'QED':1})

GC_1878 = Coupling(name = 'GC_1878',
                   value = '(ee**2*complex(0,1)*cmath.cos(alp)*cmath.cos(beta))/(2.*sw) + (ee**2*complex(0,1)*cmath.sin(alp)*cmath.sin(beta))/(2.*sw)',
                   order = {'QED':2})

GC_1879 = Coupling(name = 'GC_1879',
                   value = '(cw*ee**2*complex(0,1)*cmath.cos(alp)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee**2*complex(0,1)*cmath.sin(alp)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1880 = Coupling(name = 'GC_1880',
                   value = '(cw*ee*cmath.cos(alp)*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*cmath.sin(alp)*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1})

GC_1881 = Coupling(name = 'GC_1881',
                   value = '(ee**2*complex(0,1)*vu*cmath.cos(alp)*cmath.cos(beta)*cmath.sin(beta))/(2.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*vd*cmath.cos(beta)*cmath.sin(alp)*cmath.sin(beta))/(2.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':1})

GC_1882 = Coupling(name = 'GC_1882',
                   value = '-(ee**2*complex(0,1)*vd*cmath.cos(alp)*cmath.cos(beta)*cmath.sin(beta))/(2.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*vu*cmath.cos(beta)*cmath.sin(alp)*cmath.sin(beta))/(2.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':1})

GC_1883 = Coupling(name = 'GC_1883',
                   value = '(ee**2*complex(0,1)*cmath.cos(alp)**2*cmath.cos(beta)*cmath.sin(beta))/(2.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*cmath.cos(beta)*cmath.sin(alp)**2*cmath.sin(beta))/(2.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1884 = Coupling(name = 'GC_1884',
                   value = '-(ee**2*complex(0,1)*cmath.cos(alp)**2*cmath.cos(beta)*cmath.sin(beta))/(2.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*cmath.cos(beta)*cmath.sin(alp)**2*cmath.sin(beta))/(2.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1885 = Coupling(name = 'GC_1885',
                   value = '-(ee*complex(0,1)*cmath.cos(beta)**2) - ee*complex(0,1)*cmath.sin(beta)**2',
                   order = {'QED':1})

GC_1886 = Coupling(name = 'GC_1886',
                   value = '2*ee**2*complex(0,1)*cmath.cos(beta)**2 + 2*ee**2*complex(0,1)*cmath.sin(beta)**2',
                   order = {'QED':2})

GC_1887 = Coupling(name = 'GC_1887',
                   value = '-((I125x33*cmath.cos(beta)**2)/cmath.sqrt(2)) - (I124x33*cmath.cos(beta)*cmath.sin(beta))/cmath.sqrt(2) - (I126x33*cmath.cos(beta)*cmath.sin(beta))/cmath.sqrt(2) + (ee**2*I123x33*cmath.cos(beta)*cmath.sin(beta))/(sw**2*cmath.sqrt(2)) - (I125x33*cmath.sin(beta)**2)/cmath.sqrt(2)',
                   order = {'QED':2})

GC_1888 = Coupling(name = 'GC_1888',
                   value = '(I125x33*cmath.cos(beta)**2)/cmath.sqrt(2) - (I124x33*cmath.cos(beta)*cmath.sin(beta))/cmath.sqrt(2) - (I126x33*cmath.cos(beta)*cmath.sin(beta))/cmath.sqrt(2) + (ee**2*I123x33*cmath.cos(beta)*cmath.sin(beta))/(sw**2*cmath.sqrt(2)) + (I125x33*cmath.sin(beta)**2)/cmath.sqrt(2)',
                   order = {'QED':2})

GC_1889 = Coupling(name = 'GC_1889',
                   value = '-((I125x36*cmath.cos(beta)**2)/cmath.sqrt(2)) - (I124x36*cmath.cos(beta)*cmath.sin(beta))/cmath.sqrt(2) - (I126x36*cmath.cos(beta)*cmath.sin(beta))/cmath.sqrt(2) + (ee**2*I123x36*cmath.cos(beta)*cmath.sin(beta))/(sw**2*cmath.sqrt(2)) - (I125x36*cmath.sin(beta)**2)/cmath.sqrt(2)',
                   order = {'QED':2})

GC_1890 = Coupling(name = 'GC_1890',
                   value = '(I125x36*cmath.cos(beta)**2)/cmath.sqrt(2) - (I124x36*cmath.cos(beta)*cmath.sin(beta))/cmath.sqrt(2) - (I126x36*cmath.cos(beta)*cmath.sin(beta))/cmath.sqrt(2) + (ee**2*I123x36*cmath.cos(beta)*cmath.sin(beta))/(sw**2*cmath.sqrt(2)) + (I125x36*cmath.sin(beta)**2)/cmath.sqrt(2)',
                   order = {'QED':2})

GC_1891 = Coupling(name = 'GC_1891',
                   value = '-((I125x63*cmath.cos(beta)**2)/cmath.sqrt(2)) - (I124x63*cmath.cos(beta)*cmath.sin(beta))/cmath.sqrt(2) - (I126x63*cmath.cos(beta)*cmath.sin(beta))/cmath.sqrt(2) + (ee**2*I123x63*cmath.cos(beta)*cmath.sin(beta))/(sw**2*cmath.sqrt(2)) - (I125x63*cmath.sin(beta)**2)/cmath.sqrt(2)',
                   order = {'QED':2})

GC_1892 = Coupling(name = 'GC_1892',
                   value = '(I125x63*cmath.cos(beta)**2)/cmath.sqrt(2) - (I124x63*cmath.cos(beta)*cmath.sin(beta))/cmath.sqrt(2) - (I126x63*cmath.cos(beta)*cmath.sin(beta))/cmath.sqrt(2) + (ee**2*I123x63*cmath.cos(beta)*cmath.sin(beta))/(sw**2*cmath.sqrt(2)) + (I125x63*cmath.sin(beta)**2)/cmath.sqrt(2)',
                   order = {'QED':2})

GC_1893 = Coupling(name = 'GC_1893',
                   value = '-((I125x66*cmath.cos(beta)**2)/cmath.sqrt(2)) - (I124x66*cmath.cos(beta)*cmath.sin(beta))/cmath.sqrt(2) - (I126x66*cmath.cos(beta)*cmath.sin(beta))/cmath.sqrt(2) + (ee**2*I123x66*cmath.cos(beta)*cmath.sin(beta))/(sw**2*cmath.sqrt(2)) - (I125x66*cmath.sin(beta)**2)/cmath.sqrt(2)',
                   order = {'QED':2})

GC_1894 = Coupling(name = 'GC_1894',
                   value = '(I125x66*cmath.cos(beta)**2)/cmath.sqrt(2) - (I124x66*cmath.cos(beta)*cmath.sin(beta))/cmath.sqrt(2) - (I126x66*cmath.cos(beta)*cmath.sin(beta))/cmath.sqrt(2) + (ee**2*I123x66*cmath.cos(beta)*cmath.sin(beta))/(sw**2*cmath.sqrt(2)) + (I125x66*cmath.sin(beta)**2)/cmath.sqrt(2)',
                   order = {'QED':2})

GC_1895 = Coupling(name = 'GC_1895',
                   value = '-((I147x33*cmath.cos(beta)**2)/cmath.sqrt(2)) + (I145x33*cmath.cos(beta)*cmath.sin(beta))/cmath.sqrt(2) + (I146x33*cmath.cos(beta)*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*I144x33*cmath.cos(beta)*cmath.sin(beta))/(sw**2*cmath.sqrt(2)) - (I147x33*cmath.sin(beta)**2)/cmath.sqrt(2)',
                   order = {'QED':2})

GC_1896 = Coupling(name = 'GC_1896',
                   value = '(I147x33*cmath.cos(beta)**2)/cmath.sqrt(2) + (I145x33*cmath.cos(beta)*cmath.sin(beta))/cmath.sqrt(2) + (I146x33*cmath.cos(beta)*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*I144x33*cmath.cos(beta)*cmath.sin(beta))/(sw**2*cmath.sqrt(2)) + (I147x33*cmath.sin(beta)**2)/cmath.sqrt(2)',
                   order = {'QED':2})

GC_1897 = Coupling(name = 'GC_1897',
                   value = '-((I147x36*cmath.cos(beta)**2)/cmath.sqrt(2)) + (I145x36*cmath.cos(beta)*cmath.sin(beta))/cmath.sqrt(2) + (I146x36*cmath.cos(beta)*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*I144x36*cmath.cos(beta)*cmath.sin(beta))/(sw**2*cmath.sqrt(2)) - (I147x36*cmath.sin(beta)**2)/cmath.sqrt(2)',
                   order = {'QED':2})

GC_1898 = Coupling(name = 'GC_1898',
                   value = '(I147x36*cmath.cos(beta)**2)/cmath.sqrt(2) + (I145x36*cmath.cos(beta)*cmath.sin(beta))/cmath.sqrt(2) + (I146x36*cmath.cos(beta)*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*I144x36*cmath.cos(beta)*cmath.sin(beta))/(sw**2*cmath.sqrt(2)) + (I147x36*cmath.sin(beta)**2)/cmath.sqrt(2)',
                   order = {'QED':2})

GC_1899 = Coupling(name = 'GC_1899',
                   value = '-((I147x63*cmath.cos(beta)**2)/cmath.sqrt(2)) + (I145x63*cmath.cos(beta)*cmath.sin(beta))/cmath.sqrt(2) + (I146x63*cmath.cos(beta)*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*I144x63*cmath.cos(beta)*cmath.sin(beta))/(sw**2*cmath.sqrt(2)) - (I147x63*cmath.sin(beta)**2)/cmath.sqrt(2)',
                   order = {'QED':2})

GC_1900 = Coupling(name = 'GC_1900',
                   value = '(I147x63*cmath.cos(beta)**2)/cmath.sqrt(2) + (I145x63*cmath.cos(beta)*cmath.sin(beta))/cmath.sqrt(2) + (I146x63*cmath.cos(beta)*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*I144x63*cmath.cos(beta)*cmath.sin(beta))/(sw**2*cmath.sqrt(2)) + (I147x63*cmath.sin(beta)**2)/cmath.sqrt(2)',
                   order = {'QED':2})

GC_1901 = Coupling(name = 'GC_1901',
                   value = '-((I147x66*cmath.cos(beta)**2)/cmath.sqrt(2)) + (I145x66*cmath.cos(beta)*cmath.sin(beta))/cmath.sqrt(2) + (I146x66*cmath.cos(beta)*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*I144x66*cmath.cos(beta)*cmath.sin(beta))/(sw**2*cmath.sqrt(2)) - (I147x66*cmath.sin(beta)**2)/cmath.sqrt(2)',
                   order = {'QED':2})

GC_1902 = Coupling(name = 'GC_1902',
                   value = '(I147x66*cmath.cos(beta)**2)/cmath.sqrt(2) + (I145x66*cmath.cos(beta)*cmath.sin(beta))/cmath.sqrt(2) + (I146x66*cmath.cos(beta)*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*I144x66*cmath.cos(beta)*cmath.sin(beta))/(sw**2*cmath.sqrt(2)) + (I147x66*cmath.sin(beta)**2)/cmath.sqrt(2)',
                   order = {'QED':2})

GC_1903 = Coupling(name = 'GC_1903',
                   value = '(ee**2*complex(0,1)*cmath.cos(beta)**2)/(2.*sw**2) + (ee**2*complex(0,1)*cmath.sin(beta)**2)/(2.*sw**2)',
                   order = {'QED':2})

GC_1904 = Coupling(name = 'GC_1904',
                   value = '(ee**2*I102x11*cmath.cos(beta)**2)/(2.*sw**2*cmath.sqrt(2)) - (ee**2*I102x11*cmath.sin(beta)**2)/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1905 = Coupling(name = 'GC_1905',
                   value = '-(ee**2*I102x11*cmath.cos(beta)**2)/(2.*sw**2*cmath.sqrt(2)) + (ee**2*I102x11*cmath.sin(beta)**2)/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1906 = Coupling(name = 'GC_1906',
                   value = '(ee**2*I102x22*cmath.cos(beta)**2)/(2.*sw**2*cmath.sqrt(2)) - (ee**2*I102x22*cmath.sin(beta)**2)/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1907 = Coupling(name = 'GC_1907',
                   value = '-(ee**2*I102x22*cmath.cos(beta)**2)/(2.*sw**2*cmath.sqrt(2)) + (ee**2*I102x22*cmath.sin(beta)**2)/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1908 = Coupling(name = 'GC_1908',
                   value = '-((I103x33*cmath.cos(beta)**2)/cmath.sqrt(2)) + (ee**2*I102x33*cmath.cos(beta)**2)/(2.*sw**2*cmath.sqrt(2)) - (ee**2*I102x33*cmath.sin(beta)**2)/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1909 = Coupling(name = 'GC_1909',
                   value = '-(ee**2*I102x33*cmath.cos(beta)**2)/(2.*sw**2*cmath.sqrt(2)) - (I103x33*cmath.sin(beta)**2)/cmath.sqrt(2) + (ee**2*I102x33*cmath.sin(beta)**2)/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1910 = Coupling(name = 'GC_1910',
                   value = '-((I103x36*cmath.cos(beta)**2)/cmath.sqrt(2)) + (ee**2*I102x36*cmath.cos(beta)**2)/(2.*sw**2*cmath.sqrt(2)) - (ee**2*I102x36*cmath.sin(beta)**2)/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1911 = Coupling(name = 'GC_1911',
                   value = '-(ee**2*I102x36*cmath.cos(beta)**2)/(2.*sw**2*cmath.sqrt(2)) - (I103x36*cmath.sin(beta)**2)/cmath.sqrt(2) + (ee**2*I102x36*cmath.sin(beta)**2)/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1912 = Coupling(name = 'GC_1912',
                   value = '(ee**2*I123x11*cmath.cos(beta)**2)/(2.*sw**2*cmath.sqrt(2)) - (ee**2*I123x11*cmath.sin(beta)**2)/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1913 = Coupling(name = 'GC_1913',
                   value = '-(ee**2*I123x11*cmath.cos(beta)**2)/(2.*sw**2*cmath.sqrt(2)) + (ee**2*I123x11*cmath.sin(beta)**2)/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1914 = Coupling(name = 'GC_1914',
                   value = '(ee**2*I123x22*cmath.cos(beta)**2)/(2.*sw**2*cmath.sqrt(2)) - (ee**2*I123x22*cmath.sin(beta)**2)/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1915 = Coupling(name = 'GC_1915',
                   value = '-(ee**2*I123x22*cmath.cos(beta)**2)/(2.*sw**2*cmath.sqrt(2)) + (ee**2*I123x22*cmath.sin(beta)**2)/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1916 = Coupling(name = 'GC_1916',
                   value = '-((I126x33*cmath.cos(beta)**2)/cmath.sqrt(2)) + (ee**2*I123x33*cmath.cos(beta)**2)/(2.*sw**2*cmath.sqrt(2)) + (I124x33*cmath.sin(beta)**2)/cmath.sqrt(2) - (ee**2*I123x33*cmath.sin(beta)**2)/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1917 = Coupling(name = 'GC_1917',
                   value = '(I124x33*cmath.cos(beta)**2)/cmath.sqrt(2) - (ee**2*I123x33*cmath.cos(beta)**2)/(2.*sw**2*cmath.sqrt(2)) - (I126x33*cmath.sin(beta)**2)/cmath.sqrt(2) + (ee**2*I123x33*cmath.sin(beta)**2)/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1918 = Coupling(name = 'GC_1918',
                   value = '-((I126x36*cmath.cos(beta)**2)/cmath.sqrt(2)) + (ee**2*I123x36*cmath.cos(beta)**2)/(2.*sw**2*cmath.sqrt(2)) + (I124x36*cmath.sin(beta)**2)/cmath.sqrt(2) - (ee**2*I123x36*cmath.sin(beta)**2)/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1919 = Coupling(name = 'GC_1919',
                   value = '(I124x36*cmath.cos(beta)**2)/cmath.sqrt(2) - (ee**2*I123x36*cmath.cos(beta)**2)/(2.*sw**2*cmath.sqrt(2)) - (I126x36*cmath.sin(beta)**2)/cmath.sqrt(2) + (ee**2*I123x36*cmath.sin(beta)**2)/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1920 = Coupling(name = 'GC_1920',
                   value = '-((I126x63*cmath.cos(beta)**2)/cmath.sqrt(2)) + (ee**2*I123x63*cmath.cos(beta)**2)/(2.*sw**2*cmath.sqrt(2)) + (I124x63*cmath.sin(beta)**2)/cmath.sqrt(2) - (ee**2*I123x63*cmath.sin(beta)**2)/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1921 = Coupling(name = 'GC_1921',
                   value = '(I124x63*cmath.cos(beta)**2)/cmath.sqrt(2) - (ee**2*I123x63*cmath.cos(beta)**2)/(2.*sw**2*cmath.sqrt(2)) - (I126x63*cmath.sin(beta)**2)/cmath.sqrt(2) + (ee**2*I123x63*cmath.sin(beta)**2)/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1922 = Coupling(name = 'GC_1922',
                   value = '-((I126x66*cmath.cos(beta)**2)/cmath.sqrt(2)) + (ee**2*I123x66*cmath.cos(beta)**2)/(2.*sw**2*cmath.sqrt(2)) + (I124x66*cmath.sin(beta)**2)/cmath.sqrt(2) - (ee**2*I123x66*cmath.sin(beta)**2)/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1923 = Coupling(name = 'GC_1923',
                   value = '(I124x66*cmath.cos(beta)**2)/cmath.sqrt(2) - (ee**2*I123x66*cmath.cos(beta)**2)/(2.*sw**2*cmath.sqrt(2)) - (I126x66*cmath.sin(beta)**2)/cmath.sqrt(2) + (ee**2*I123x66*cmath.sin(beta)**2)/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1924 = Coupling(name = 'GC_1924',
                   value = '(ee**2*I144x11*cmath.cos(beta)**2)/(2.*sw**2*cmath.sqrt(2)) - (ee**2*I144x11*cmath.sin(beta)**2)/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1925 = Coupling(name = 'GC_1925',
                   value = '-(ee**2*I144x11*cmath.cos(beta)**2)/(2.*sw**2*cmath.sqrt(2)) + (ee**2*I144x11*cmath.sin(beta)**2)/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1926 = Coupling(name = 'GC_1926',
                   value = '(ee**2*I144x22*cmath.cos(beta)**2)/(2.*sw**2*cmath.sqrt(2)) - (ee**2*I144x22*cmath.sin(beta)**2)/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1927 = Coupling(name = 'GC_1927',
                   value = '-(ee**2*I144x22*cmath.cos(beta)**2)/(2.*sw**2*cmath.sqrt(2)) + (ee**2*I144x22*cmath.sin(beta)**2)/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1928 = Coupling(name = 'GC_1928',
                   value = '-((I145x33*cmath.cos(beta)**2)/cmath.sqrt(2)) + (ee**2*I144x33*cmath.cos(beta)**2)/(2.*sw**2*cmath.sqrt(2)) + (I146x33*cmath.sin(beta)**2)/cmath.sqrt(2) - (ee**2*I144x33*cmath.sin(beta)**2)/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1929 = Coupling(name = 'GC_1929',
                   value = '(I146x33*cmath.cos(beta)**2)/cmath.sqrt(2) - (ee**2*I144x33*cmath.cos(beta)**2)/(2.*sw**2*cmath.sqrt(2)) - (I145x33*cmath.sin(beta)**2)/cmath.sqrt(2) + (ee**2*I144x33*cmath.sin(beta)**2)/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1930 = Coupling(name = 'GC_1930',
                   value = '-((I145x36*cmath.cos(beta)**2)/cmath.sqrt(2)) + (ee**2*I144x36*cmath.cos(beta)**2)/(2.*sw**2*cmath.sqrt(2)) + (I146x36*cmath.sin(beta)**2)/cmath.sqrt(2) - (ee**2*I144x36*cmath.sin(beta)**2)/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1931 = Coupling(name = 'GC_1931',
                   value = '(I146x36*cmath.cos(beta)**2)/cmath.sqrt(2) - (ee**2*I144x36*cmath.cos(beta)**2)/(2.*sw**2*cmath.sqrt(2)) - (I145x36*cmath.sin(beta)**2)/cmath.sqrt(2) + (ee**2*I144x36*cmath.sin(beta)**2)/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1932 = Coupling(name = 'GC_1932',
                   value = '-((I145x63*cmath.cos(beta)**2)/cmath.sqrt(2)) + (ee**2*I144x63*cmath.cos(beta)**2)/(2.*sw**2*cmath.sqrt(2)) + (I146x63*cmath.sin(beta)**2)/cmath.sqrt(2) - (ee**2*I144x63*cmath.sin(beta)**2)/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1933 = Coupling(name = 'GC_1933',
                   value = '(I146x63*cmath.cos(beta)**2)/cmath.sqrt(2) - (ee**2*I144x63*cmath.cos(beta)**2)/(2.*sw**2*cmath.sqrt(2)) - (I145x63*cmath.sin(beta)**2)/cmath.sqrt(2) + (ee**2*I144x63*cmath.sin(beta)**2)/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1934 = Coupling(name = 'GC_1934',
                   value = '-((I145x66*cmath.cos(beta)**2)/cmath.sqrt(2)) + (ee**2*I144x66*cmath.cos(beta)**2)/(2.*sw**2*cmath.sqrt(2)) + (I146x66*cmath.sin(beta)**2)/cmath.sqrt(2) - (ee**2*I144x66*cmath.sin(beta)**2)/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1935 = Coupling(name = 'GC_1935',
                   value = '(I146x66*cmath.cos(beta)**2)/cmath.sqrt(2) - (ee**2*I144x66*cmath.cos(beta)**2)/(2.*sw**2*cmath.sqrt(2)) - (I145x66*cmath.sin(beta)**2)/cmath.sqrt(2) + (ee**2*I144x66*cmath.sin(beta)**2)/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1936 = Coupling(name = 'GC_1936',
                   value = '(ee**2*I94x11*cmath.cos(beta)**2)/(2.*sw**2*cmath.sqrt(2)) - (ee**2*I94x11*cmath.sin(beta)**2)/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1937 = Coupling(name = 'GC_1937',
                   value = '-(ee**2*I94x11*cmath.cos(beta)**2)/(2.*sw**2*cmath.sqrt(2)) + (ee**2*I94x11*cmath.sin(beta)**2)/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1938 = Coupling(name = 'GC_1938',
                   value = '(ee**2*I94x22*cmath.cos(beta)**2)/(2.*sw**2*cmath.sqrt(2)) - (ee**2*I94x22*cmath.sin(beta)**2)/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1939 = Coupling(name = 'GC_1939',
                   value = '-(ee**2*I94x22*cmath.cos(beta)**2)/(2.*sw**2*cmath.sqrt(2)) + (ee**2*I94x22*cmath.sin(beta)**2)/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1940 = Coupling(name = 'GC_1940',
                   value = '(ee**2*I94x33*cmath.cos(beta)**2)/(2.*sw**2*cmath.sqrt(2)) + (I95x33*cmath.sin(beta)**2)/cmath.sqrt(2) - (ee**2*I94x33*cmath.sin(beta)**2)/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1941 = Coupling(name = 'GC_1941',
                   value = '(I95x33*cmath.cos(beta)**2)/cmath.sqrt(2) - (ee**2*I94x33*cmath.cos(beta)**2)/(2.*sw**2*cmath.sqrt(2)) + (ee**2*I94x33*cmath.sin(beta)**2)/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1942 = Coupling(name = 'GC_1942',
                   value = '(ee**2*I94x36*cmath.cos(beta)**2)/(2.*sw**2*cmath.sqrt(2)) + (I95x36*cmath.sin(beta)**2)/cmath.sqrt(2) - (ee**2*I94x36*cmath.sin(beta)**2)/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1943 = Coupling(name = 'GC_1943',
                   value = '(I95x36*cmath.cos(beta)**2)/cmath.sqrt(2) - (ee**2*I94x36*cmath.cos(beta)**2)/(2.*sw**2*cmath.sqrt(2)) + (ee**2*I94x36*cmath.sin(beta)**2)/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1944 = Coupling(name = 'GC_1944',
                   value = '(ee*cmath.cos(beta)**2)/(2.*sw) + (ee*cmath.sin(beta)**2)/(2.*sw)',
                   order = {'QED':1})

GC_1945 = Coupling(name = 'GC_1945',
                   value = '-(ee**2*cmath.cos(beta)**2)/(2.*sw) - (ee**2*cmath.sin(beta)**2)/(2.*sw)',
                   order = {'QED':2})

GC_1946 = Coupling(name = 'GC_1946',
                   value = '(ee**2*cmath.cos(beta)**2)/(2.*sw) + (ee**2*cmath.sin(beta)**2)/(2.*sw)',
                   order = {'QED':2})

GC_1947 = Coupling(name = 'GC_1947',
                   value = '-(cw*ee**2*cmath.cos(beta)**2)/(2.*(-1 + sw)*(1 + sw)) - (cw*ee**2*cmath.sin(beta)**2)/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1948 = Coupling(name = 'GC_1948',
                   value = '(cw*ee**2*cmath.cos(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (cw*ee**2*cmath.sin(beta)**2)/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1949 = Coupling(name = 'GC_1949',
                   value = '(ee**2*complex(0,1)*I149x44*cmath.cos(beta)**2)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I149x44*cmath.sin(beta)**2)/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1950 = Coupling(name = 'GC_1950',
                   value = '-(ee**2*complex(0,1)*I149x44*cmath.cos(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I149x44*cmath.sin(beta)**2)/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1951 = Coupling(name = 'GC_1951',
                   value = '(ee**2*complex(0,1)*I149x55*cmath.cos(beta)**2)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I149x55*cmath.sin(beta)**2)/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1952 = Coupling(name = 'GC_1952',
                   value = '-(ee**2*complex(0,1)*I149x55*cmath.cos(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I149x55*cmath.sin(beta)**2)/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1953 = Coupling(name = 'GC_1953',
                   value = '(ee**2*complex(0,1)*I16x44*cmath.cos(beta)**2)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16x44*cmath.sin(beta)**2)/(6.*(-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1954 = Coupling(name = 'GC_1954',
                   value = '-(ee**2*complex(0,1)*I16x44*cmath.cos(beta)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I16x44*cmath.sin(beta)**2)/(6.*(-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1955 = Coupling(name = 'GC_1955',
                   value = '(ee**2*complex(0,1)*I16x55*cmath.cos(beta)**2)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16x55*cmath.sin(beta)**2)/(6.*(-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1956 = Coupling(name = 'GC_1956',
                   value = '-(ee**2*complex(0,1)*I16x55*cmath.cos(beta)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I16x55*cmath.sin(beta)**2)/(6.*(-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1957 = Coupling(name = 'GC_1957',
                   value = '(ee**2*complex(0,1)*I54x44*cmath.cos(beta)**2)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I54x44*cmath.sin(beta)**2)/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1958 = Coupling(name = 'GC_1958',
                   value = '-(ee**2*complex(0,1)*I54x44*cmath.cos(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I54x44*cmath.sin(beta)**2)/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1959 = Coupling(name = 'GC_1959',
                   value = '(ee**2*complex(0,1)*I54x55*cmath.cos(beta)**2)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I54x55*cmath.sin(beta)**2)/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1960 = Coupling(name = 'GC_1960',
                   value = '-(ee**2*complex(0,1)*I54x55*cmath.cos(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I54x55*cmath.sin(beta)**2)/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1961 = Coupling(name = 'GC_1961',
                   value = '(ee**2*complex(0,1)*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1962 = Coupling(name = 'GC_1962',
                   value = '-(ee**2*complex(0,1)*cmath.cos(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*cmath.sin(beta)**2)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1963 = Coupling(name = 'GC_1963',
                   value = '-(ee**2*complex(0,1)*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1964 = Coupling(name = 'GC_1964',
                   value = '(ee**2*complex(0,1)*cmath.cos(beta)**2)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*cmath.sin(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1965 = Coupling(name = 'GC_1965',
                   value = '(ee**2*complex(0,1)*cmath.cos(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I104x33*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I104x33*sw**2*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*cmath.sin(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1966 = Coupling(name = 'GC_1966',
                   value = '-(ee**2*complex(0,1)*cmath.cos(beta)**2)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*cmath.sin(beta)**2)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1967 = Coupling(name = 'GC_1967',
                   value = '-(ee**2*complex(0,1)*I148x11*cmath.cos(beta)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I148x11*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I148x11*cmath.sin(beta)**2)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I148x11*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1968 = Coupling(name = 'GC_1968',
                   value = '-(ee**2*complex(0,1)*I148x11*cmath.cos(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I148x11*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I148x11*cmath.sin(beta)**2)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I148x11*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1969 = Coupling(name = 'GC_1969',
                   value = '(ee**2*complex(0,1)*I148x11*cmath.cos(beta)**2)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I148x11*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*I148x11*cmath.sin(beta)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I148x11*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1970 = Coupling(name = 'GC_1970',
                   value = '(ee**2*complex(0,1)*I148x11*cmath.cos(beta)**2)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I148x11*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*I148x11*cmath.sin(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I148x11*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1971 = Coupling(name = 'GC_1971',
                   value = '-(ee**2*complex(0,1)*I148x22*cmath.cos(beta)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I148x22*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I148x22*cmath.sin(beta)**2)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I148x22*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1972 = Coupling(name = 'GC_1972',
                   value = '-(ee**2*complex(0,1)*I148x22*cmath.cos(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I148x22*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I148x22*cmath.sin(beta)**2)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I148x22*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1973 = Coupling(name = 'GC_1973',
                   value = '(ee**2*complex(0,1)*I148x22*cmath.cos(beta)**2)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I148x22*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*I148x22*cmath.sin(beta)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I148x22*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1974 = Coupling(name = 'GC_1974',
                   value = '(ee**2*complex(0,1)*I148x22*cmath.cos(beta)**2)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I148x22*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*I148x22*cmath.sin(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I148x22*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1975 = Coupling(name = 'GC_1975',
                   value = '(ee**2*complex(0,1)*I148x33*cmath.cos(beta)**2)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I149x33*cmath.cos(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I156x33*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I157x33*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I148x33*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I156x33*sw**2*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I157x33*sw**2*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I148x33*cmath.sin(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I149x33*cmath.sin(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I148x33*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1976 = Coupling(name = 'GC_1976',
                   value = '(ee**2*complex(0,1)*I148x36*cmath.cos(beta)**2)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I149x36*cmath.cos(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I156x36*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I157x36*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I148x36*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I156x36*sw**2*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I157x36*sw**2*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I148x36*cmath.sin(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I149x36*cmath.sin(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I148x36*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1977 = Coupling(name = 'GC_1977',
                   value = '(ee**2*complex(0,1)*I148x63*cmath.cos(beta)**2)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I149x63*cmath.cos(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I156x63*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I157x63*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I148x63*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I156x63*sw**2*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I157x63*sw**2*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I148x63*cmath.sin(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I149x63*cmath.sin(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I148x63*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1978 = Coupling(name = 'GC_1978',
                   value = '(ee**2*complex(0,1)*I148x66*cmath.cos(beta)**2)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I149x66*cmath.cos(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I156x66*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I157x66*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I148x66*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I156x66*sw**2*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I157x66*sw**2*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I148x66*cmath.sin(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I149x66*cmath.sin(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I148x66*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1979 = Coupling(name = 'GC_1979',
                   value = '-(ee**2*complex(0,1)*I15x11*cmath.cos(beta)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15x11*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I15x11*cmath.sin(beta)**2)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I15x11*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1980 = Coupling(name = 'GC_1980',
                   value = '-(ee**2*complex(0,1)*I15x11*cmath.cos(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15x11*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I15x11*cmath.sin(beta)**2)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I15x11*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1981 = Coupling(name = 'GC_1981',
                   value = '(ee**2*complex(0,1)*I15x11*cmath.cos(beta)**2)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I15x11*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*I15x11*cmath.sin(beta)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15x11*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1982 = Coupling(name = 'GC_1982',
                   value = '(ee**2*complex(0,1)*I15x11*cmath.cos(beta)**2)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I15x11*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*I15x11*cmath.sin(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15x11*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1983 = Coupling(name = 'GC_1983',
                   value = '-(ee**2*complex(0,1)*I15x22*cmath.cos(beta)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15x22*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I15x22*cmath.sin(beta)**2)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I15x22*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1984 = Coupling(name = 'GC_1984',
                   value = '-(ee**2*complex(0,1)*I15x22*cmath.cos(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15x22*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I15x22*cmath.sin(beta)**2)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I15x22*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1985 = Coupling(name = 'GC_1985',
                   value = '(ee**2*complex(0,1)*I15x22*cmath.cos(beta)**2)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I15x22*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*I15x22*cmath.sin(beta)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15x22*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1986 = Coupling(name = 'GC_1986',
                   value = '(ee**2*complex(0,1)*I15x22*cmath.cos(beta)**2)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I15x22*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*I15x22*cmath.sin(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15x22*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1987 = Coupling(name = 'GC_1987',
                   value = '(ee**2*complex(0,1)*I15x33*cmath.cos(beta)**2)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16x33*cmath.cos(beta)**2)/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I23x33*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I24x33*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I15x33*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I23x33*sw**2*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I24x33*sw**2*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I15x33*cmath.sin(beta)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I16x33*cmath.sin(beta)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15x33*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1988 = Coupling(name = 'GC_1988',
                   value = '(ee**2*complex(0,1)*I15x36*cmath.cos(beta)**2)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16x36*cmath.cos(beta)**2)/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I23x36*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I24x36*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I15x36*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I23x36*sw**2*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I24x36*sw**2*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I15x36*cmath.sin(beta)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I16x36*cmath.sin(beta)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15x36*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1989 = Coupling(name = 'GC_1989',
                   value = '(ee**2*complex(0,1)*I15x63*cmath.cos(beta)**2)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16x63*cmath.cos(beta)**2)/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I23x63*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I24x63*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I15x63*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I23x63*sw**2*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I24x63*sw**2*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I15x63*cmath.sin(beta)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I16x63*cmath.sin(beta)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15x63*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1990 = Coupling(name = 'GC_1990',
                   value = '(ee**2*complex(0,1)*I15x66*cmath.cos(beta)**2)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16x66*cmath.cos(beta)**2)/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I23x66*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I24x66*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I15x66*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I23x66*sw**2*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I24x66*sw**2*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I15x66*cmath.sin(beta)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I16x66*cmath.sin(beta)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15x66*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1991 = Coupling(name = 'GC_1991',
                   value = '(ee**2*complex(0,1)*I53x11*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*I53x11*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1992 = Coupling(name = 'GC_1992',
                   value = '-(ee**2*complex(0,1)*I53x11*cmath.cos(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I53x11*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I53x11*cmath.sin(beta)**2)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I53x11*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1993 = Coupling(name = 'GC_1993',
                   value = '-(ee**2*complex(0,1)*I53x11*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I53x11*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1994 = Coupling(name = 'GC_1994',
                   value = '(ee**2*complex(0,1)*I53x11*cmath.cos(beta)**2)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I53x11*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*I53x11*cmath.sin(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I53x11*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1995 = Coupling(name = 'GC_1995',
                   value = '(ee**2*complex(0,1)*I53x22*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*I53x22*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1996 = Coupling(name = 'GC_1996',
                   value = '-(ee**2*complex(0,1)*I53x22*cmath.cos(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I53x22*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I53x22*cmath.sin(beta)**2)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I53x22*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1997 = Coupling(name = 'GC_1997',
                   value = '-(ee**2*complex(0,1)*I53x22*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I53x22*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1998 = Coupling(name = 'GC_1998',
                   value = '(ee**2*complex(0,1)*I53x22*cmath.cos(beta)**2)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I53x22*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*I53x22*cmath.sin(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I53x22*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1999 = Coupling(name = 'GC_1999',
                   value = '-(ee**2*complex(0,1)*I54x33*cmath.cos(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I62x33*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I53x33*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I62x33*sw**2*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I54x33*cmath.sin(beta)**2)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I53x33*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_2000 = Coupling(name = 'GC_2000',
                   value = '(ee**2*complex(0,1)*I53x33*cmath.cos(beta)**2)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I54x33*cmath.cos(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I61x33*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I62x33*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I53x33*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I61x33*sw**2*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I62x33*sw**2*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I53x33*cmath.sin(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I54x33*cmath.sin(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I53x33*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_2001 = Coupling(name = 'GC_2001',
                   value = '-(ee**2*complex(0,1)*I54x36*cmath.cos(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I62x36*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I53x36*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I62x36*sw**2*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I54x36*cmath.sin(beta)**2)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I53x36*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_2002 = Coupling(name = 'GC_2002',
                   value = '(ee**2*complex(0,1)*I53x36*cmath.cos(beta)**2)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I54x36*cmath.cos(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I61x36*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I62x36*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I53x36*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I61x36*sw**2*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I62x36*sw**2*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I53x36*cmath.sin(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I54x36*cmath.sin(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I53x36*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_2003 = Coupling(name = 'GC_2003',
                   value = '-(ee**2*complex(0,1)*I54x63*cmath.cos(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I62x63*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I53x63*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I62x63*sw**2*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I54x63*cmath.sin(beta)**2)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I53x63*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_2004 = Coupling(name = 'GC_2004',
                   value = '(ee**2*complex(0,1)*I53x63*cmath.cos(beta)**2)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I54x63*cmath.cos(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I61x63*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I62x63*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I53x63*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I61x63*sw**2*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I62x63*sw**2*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I53x63*cmath.sin(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I54x63*cmath.sin(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I53x63*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_2005 = Coupling(name = 'GC_2005',
                   value = '-(ee**2*complex(0,1)*I54x66*cmath.cos(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I62x66*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I53x66*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I62x66*sw**2*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I54x66*cmath.sin(beta)**2)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I53x66*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_2006 = Coupling(name = 'GC_2006',
                   value = '(ee**2*complex(0,1)*I53x66*cmath.cos(beta)**2)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I54x66*cmath.cos(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I61x66*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I62x66*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I53x66*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I61x66*sw**2*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I62x66*sw**2*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I53x66*cmath.sin(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I54x66*cmath.sin(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I53x66*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_2007 = Coupling(name = 'GC_2007',
                   value = '(cw*ee*complex(0,1)*cmath.cos(beta)**2)/(2.*(-1 + sw)*sw*(1 + sw)) - (cw*ee*complex(0,1)*sw*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*cmath.sin(beta)**2)/(2.*(-1 + sw)*sw*(1 + sw)) - (cw*ee*complex(0,1)*sw*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_2008 = Coupling(name = 'GC_2008',
                   value = '-((cw*ee**2*complex(0,1)*cmath.cos(beta)**2)/((-1 + sw)*sw*(1 + sw))) + (2*cw*ee**2*complex(0,1)*sw*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) - (cw*ee**2*complex(0,1)*cmath.sin(beta)**2)/((-1 + sw)*sw*(1 + sw)) + (2*cw*ee**2*complex(0,1)*sw*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_2009 = Coupling(name = 'GC_2009',
                   value = '(2*ee**2*complex(0,1)*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*cmath.cos(beta)**2)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (2*ee**2*complex(0,1)*sw**2*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) + (2*ee**2*complex(0,1)*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*cmath.sin(beta)**2)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (2*ee**2*complex(0,1)*sw**2*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_2010 = Coupling(name = 'GC_2010',
                   value = '-(ee**2*complex(0,1)*cmath.cos(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*cmath.sin(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I104x33*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I104x33*sw**2*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_2011 = Coupling(name = 'GC_2011',
                   value = '(ee**2*complex(0,1)*I148x33*cmath.cos(beta)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I149x33*cmath.cos(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I158x33*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I148x33*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I158x33*sw**2*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I148x33*cmath.sin(beta)**2)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I149x33*cmath.sin(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I157x33*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I148x33*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I157x33*sw**2*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_2012 = Coupling(name = 'GC_2012',
                   value = '-(ee**2*complex(0,1)*I148x33*cmath.cos(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I149x33*cmath.cos(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I148x33*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I148x33*cmath.sin(beta)**2)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I149x33*cmath.sin(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I156x33*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I157x33*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I148x33*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I156x33*sw**2*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I157x33*sw**2*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_2013 = Coupling(name = 'GC_2013',
                   value = '(ee**2*complex(0,1)*I148x36*cmath.cos(beta)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I149x36*cmath.cos(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I158x36*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I148x36*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I158x36*sw**2*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I148x36*cmath.sin(beta)**2)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I149x36*cmath.sin(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I157x36*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I148x36*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I157x36*sw**2*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_2014 = Coupling(name = 'GC_2014',
                   value = '-(ee**2*complex(0,1)*I148x36*cmath.cos(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I149x36*cmath.cos(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I148x36*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I148x36*cmath.sin(beta)**2)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I149x36*cmath.sin(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I156x36*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I157x36*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I148x36*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I156x36*sw**2*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I157x36*sw**2*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_2015 = Coupling(name = 'GC_2015',
                   value = '(ee**2*complex(0,1)*I148x63*cmath.cos(beta)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I149x63*cmath.cos(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I158x63*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I148x63*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I158x63*sw**2*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I148x63*cmath.sin(beta)**2)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I149x63*cmath.sin(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I157x63*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I148x63*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I157x63*sw**2*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_2016 = Coupling(name = 'GC_2016',
                   value = '-(ee**2*complex(0,1)*I148x63*cmath.cos(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I149x63*cmath.cos(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I148x63*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I148x63*cmath.sin(beta)**2)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I149x63*cmath.sin(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I156x63*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I157x63*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I148x63*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I156x63*sw**2*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I157x63*sw**2*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_2017 = Coupling(name = 'GC_2017',
                   value = '(ee**2*complex(0,1)*I148x66*cmath.cos(beta)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I149x66*cmath.cos(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I158x66*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I148x66*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I158x66*sw**2*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I148x66*cmath.sin(beta)**2)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I149x66*cmath.sin(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I157x66*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I148x66*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I157x66*sw**2*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_2018 = Coupling(name = 'GC_2018',
                   value = '-(ee**2*complex(0,1)*I148x66*cmath.cos(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I149x66*cmath.cos(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I148x66*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I148x66*cmath.sin(beta)**2)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I149x66*cmath.sin(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I156x66*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I157x66*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I148x66*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I156x66*sw**2*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I157x66*sw**2*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_2019 = Coupling(name = 'GC_2019',
                   value = '-(ee**2*complex(0,1)*I148x33*cmath.cos(beta)**2)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I149x33*cmath.cos(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I157x33*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I148x33*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I157x33*sw**2*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I148x33*cmath.sin(beta)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I149x33*cmath.sin(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I158x33*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I148x33*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I158x33*sw**2*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_2020 = Coupling(name = 'GC_2020',
                   value = '-(ee**2*complex(0,1)*I148x36*cmath.cos(beta)**2)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I149x36*cmath.cos(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I157x36*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I148x36*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I157x36*sw**2*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I148x36*cmath.sin(beta)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I149x36*cmath.sin(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I158x36*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I148x36*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I158x36*sw**2*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_2021 = Coupling(name = 'GC_2021',
                   value = '-(ee**2*complex(0,1)*I148x63*cmath.cos(beta)**2)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I149x63*cmath.cos(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I157x63*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I148x63*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I157x63*sw**2*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I148x63*cmath.sin(beta)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I149x63*cmath.sin(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I158x63*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I148x63*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I158x63*sw**2*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_2022 = Coupling(name = 'GC_2022',
                   value = '-(ee**2*complex(0,1)*I148x66*cmath.cos(beta)**2)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I149x66*cmath.cos(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I157x66*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I148x66*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I157x66*sw**2*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I148x66*cmath.sin(beta)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I149x66*cmath.sin(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I158x66*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I148x66*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I158x66*sw**2*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_2023 = Coupling(name = 'GC_2023',
                   value = '(ee**2*complex(0,1)*I15x33*cmath.cos(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I16x33*cmath.cos(beta)**2)/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I25x33*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I15x33*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I25x33*sw**2*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I15x33*cmath.sin(beta)**2)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16x33*cmath.sin(beta)**2)/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I24x33*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15x33*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I24x33*sw**2*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_2024 = Coupling(name = 'GC_2024',
                   value = '-(ee**2*complex(0,1)*I15x33*cmath.cos(beta)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I16x33*cmath.cos(beta)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15x33*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I15x33*cmath.sin(beta)**2)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16x33*cmath.sin(beta)**2)/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I23x33*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I24x33*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I15x33*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I23x33*sw**2*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I24x33*sw**2*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_2025 = Coupling(name = 'GC_2025',
                   value = '(ee**2*complex(0,1)*I15x36*cmath.cos(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I16x36*cmath.cos(beta)**2)/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I25x36*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I15x36*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I25x36*sw**2*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I15x36*cmath.sin(beta)**2)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16x36*cmath.sin(beta)**2)/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I24x36*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15x36*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I24x36*sw**2*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_2026 = Coupling(name = 'GC_2026',
                   value = '-(ee**2*complex(0,1)*I15x36*cmath.cos(beta)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I16x36*cmath.cos(beta)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15x36*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I15x36*cmath.sin(beta)**2)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16x36*cmath.sin(beta)**2)/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I23x36*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I24x36*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I15x36*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I23x36*sw**2*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I24x36*sw**2*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_2027 = Coupling(name = 'GC_2027',
                   value = '(ee**2*complex(0,1)*I15x63*cmath.cos(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I16x63*cmath.cos(beta)**2)/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I25x63*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I15x63*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I25x63*sw**2*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I15x63*cmath.sin(beta)**2)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16x63*cmath.sin(beta)**2)/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I24x63*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15x63*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I24x63*sw**2*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_2028 = Coupling(name = 'GC_2028',
                   value = '-(ee**2*complex(0,1)*I15x63*cmath.cos(beta)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I16x63*cmath.cos(beta)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15x63*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I15x63*cmath.sin(beta)**2)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16x63*cmath.sin(beta)**2)/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I23x63*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I24x63*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I15x63*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I23x63*sw**2*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I24x63*sw**2*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_2029 = Coupling(name = 'GC_2029',
                   value = '(ee**2*complex(0,1)*I15x66*cmath.cos(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I16x66*cmath.cos(beta)**2)/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I25x66*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I15x66*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I25x66*sw**2*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I15x66*cmath.sin(beta)**2)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16x66*cmath.sin(beta)**2)/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I24x66*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15x66*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I24x66*sw**2*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_2030 = Coupling(name = 'GC_2030',
                   value = '-(ee**2*complex(0,1)*I15x66*cmath.cos(beta)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I16x66*cmath.cos(beta)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15x66*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I15x66*cmath.sin(beta)**2)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16x66*cmath.sin(beta)**2)/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I23x66*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I24x66*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I15x66*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I23x66*sw**2*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I24x66*sw**2*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_2031 = Coupling(name = 'GC_2031',
                   value = '-(ee**2*complex(0,1)*I15x33*cmath.cos(beta)**2)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16x33*cmath.cos(beta)**2)/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I24x33*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15x33*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I24x33*sw**2*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15x33*cmath.sin(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I16x33*cmath.sin(beta)**2)/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I25x33*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I15x33*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I25x33*sw**2*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_2032 = Coupling(name = 'GC_2032',
                   value = '-(ee**2*complex(0,1)*I15x36*cmath.cos(beta)**2)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16x36*cmath.cos(beta)**2)/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I24x36*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15x36*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I24x36*sw**2*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15x36*cmath.sin(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I16x36*cmath.sin(beta)**2)/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I25x36*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I15x36*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I25x36*sw**2*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_2033 = Coupling(name = 'GC_2033',
                   value = '-(ee**2*complex(0,1)*I15x63*cmath.cos(beta)**2)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16x63*cmath.cos(beta)**2)/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I24x63*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15x63*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I24x63*sw**2*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15x63*cmath.sin(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I16x63*cmath.sin(beta)**2)/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I25x63*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I15x63*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I25x63*sw**2*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_2034 = Coupling(name = 'GC_2034',
                   value = '-(ee**2*complex(0,1)*I15x66*cmath.cos(beta)**2)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16x66*cmath.cos(beta)**2)/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I24x66*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15x66*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I24x66*sw**2*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15x66*cmath.sin(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I16x66*cmath.sin(beta)**2)/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I25x66*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I15x66*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I25x66*sw**2*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_2035 = Coupling(name = 'GC_2035',
                   value = '(ee**2*complex(0,1)*I54x33*cmath.cos(beta)**2)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I53x33*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*I54x33*cmath.sin(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I62x33*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I53x33*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I62x33*sw**2*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_2036 = Coupling(name = 'GC_2036',
                   value = '-(ee**2*complex(0,1)*I53x33*cmath.cos(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I54x33*cmath.cos(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I53x33*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I53x33*cmath.sin(beta)**2)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I54x33*cmath.sin(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I61x33*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I62x33*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I53x33*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I61x33*sw**2*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I62x33*sw**2*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_2037 = Coupling(name = 'GC_2037',
                   value = '(ee**2*complex(0,1)*I54x36*cmath.cos(beta)**2)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I53x36*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*I54x36*cmath.sin(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I62x36*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I53x36*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I62x36*sw**2*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_2038 = Coupling(name = 'GC_2038',
                   value = '-(ee**2*complex(0,1)*I53x36*cmath.cos(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I54x36*cmath.cos(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I53x36*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I53x36*cmath.sin(beta)**2)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I54x36*cmath.sin(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I61x36*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I62x36*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I53x36*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I61x36*sw**2*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I62x36*sw**2*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_2039 = Coupling(name = 'GC_2039',
                   value = '(ee**2*complex(0,1)*I54x63*cmath.cos(beta)**2)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I53x63*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*I54x63*cmath.sin(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I62x63*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I53x63*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I62x63*sw**2*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_2040 = Coupling(name = 'GC_2040',
                   value = '-(ee**2*complex(0,1)*I53x63*cmath.cos(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I54x63*cmath.cos(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I53x63*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I53x63*cmath.sin(beta)**2)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I54x63*cmath.sin(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I61x63*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I62x63*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I53x63*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I61x63*sw**2*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I62x63*sw**2*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_2041 = Coupling(name = 'GC_2041',
                   value = '(ee**2*complex(0,1)*I54x66*cmath.cos(beta)**2)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I53x66*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*I54x66*cmath.sin(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I62x66*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I53x66*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I62x66*sw**2*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_2042 = Coupling(name = 'GC_2042',
                   value = '-(ee**2*complex(0,1)*I53x66*cmath.cos(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I54x66*cmath.cos(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I53x66*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I53x66*cmath.sin(beta)**2)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I54x66*cmath.sin(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I61x66*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I62x66*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I53x66*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I61x66*sw**2*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I62x66*sw**2*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_2043 = Coupling(name = 'GC_2043',
                   value = '(ee**2*complex(0,1)*vu*cmath.cos(alp)*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*vd*cmath.cos(beta)**2*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*vu*cmath.cos(alp)*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*vd*cmath.sin(alp)*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':1})

GC_2044 = Coupling(name = 'GC_2044',
                   value = '(ee**2*complex(0,1)*vu*cmath.cos(alp)*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*vd*cmath.cos(beta)**2*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*vd*cmath.cos(beta)**2*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*vd*cmath.cos(alp)*cmath.cos(beta)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*vd*cmath.cos(alp)*cmath.cos(beta)*cmath.sin(beta))/(2.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*vu*cmath.cos(beta)*cmath.sin(alp)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*vu*cmath.cos(beta)*cmath.sin(alp)*cmath.sin(beta))/(2.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*vu*cmath.cos(alp)*cmath.sin(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*vu*cmath.cos(alp)*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*vd*cmath.sin(alp)*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':1})

GC_2045 = Coupling(name = 'GC_2045',
                   value = '-(ee**2*complex(0,1)*vu*cmath.cos(alp)*cmath.cos(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*vu*cmath.cos(alp)*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*vd*cmath.cos(beta)**2*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*vd*cmath.cos(alp)*cmath.cos(beta)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*vd*cmath.cos(alp)*cmath.cos(beta)*cmath.sin(beta))/(2.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*vu*cmath.cos(beta)*cmath.sin(alp)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*vu*cmath.cos(beta)*cmath.sin(alp)*cmath.sin(beta))/(2.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*vu*cmath.cos(alp)*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*vd*cmath.sin(alp)*cmath.sin(beta)**2)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*vd*cmath.sin(alp)*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':1})

GC_2046 = Coupling(name = 'GC_2046',
                   value = '-(ee**2*complex(0,1)*vu*cmath.cos(alp)*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*vd*cmath.cos(beta)**2*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*vu*cmath.cos(alp)*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*vd*cmath.sin(alp)*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':1})

GC_2047 = Coupling(name = 'GC_2047',
                   value = '(ee**2*complex(0,1)*vu*cmath.cos(alp)*cmath.cos(beta)**2)/(4.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*vu*cmath.cos(alp)*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*vd*cmath.cos(beta)**2*cmath.sin(alp))/(4.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*vd*cmath.cos(beta)**2*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*vd*cmath.cos(alp)*cmath.cos(beta)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*vu*cmath.cos(beta)*cmath.sin(alp)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*vu*cmath.cos(alp)*cmath.sin(beta)**2)/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*vu*cmath.cos(alp)*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*vd*cmath.sin(alp)*cmath.sin(beta)**2)/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*vd*cmath.sin(alp)*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':1})

GC_2048 = Coupling(name = 'GC_2048',
                   value = '-(ee**2*complex(0,1)*vd*cmath.cos(alp)*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*vu*cmath.cos(beta)**2*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*vd*cmath.cos(alp)*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*vu*cmath.sin(alp)*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':1})

GC_2049 = Coupling(name = 'GC_2049',
                   value = '(ee**2*complex(0,1)*vd*cmath.cos(alp)*cmath.cos(beta)**2)/(4.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*vd*cmath.cos(alp)*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*vu*cmath.cos(beta)**2*cmath.sin(alp))/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*vu*cmath.cos(beta)**2*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*vu*cmath.cos(alp)*cmath.cos(beta)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*vd*cmath.cos(beta)*cmath.sin(alp)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*vd*cmath.cos(alp)*cmath.sin(beta)**2)/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*vd*cmath.cos(alp)*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*vu*cmath.sin(alp)*cmath.sin(beta)**2)/(4.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*vu*cmath.sin(alp)*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':1})

GC_2050 = Coupling(name = 'GC_2050',
                   value = '(ee**2*complex(0,1)*vd*cmath.cos(alp)*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*vu*cmath.cos(beta)**2*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*vd*cmath.cos(alp)*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*vu*cmath.sin(alp)*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':1})

GC_2051 = Coupling(name = 'GC_2051',
                   value = '(ee**2*complex(0,1)*vd*cmath.cos(alp)*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*vu*cmath.cos(beta)**2*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*vu*cmath.cos(beta)**2*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*vu*cmath.cos(alp)*cmath.cos(beta)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*vu*cmath.cos(alp)*cmath.cos(beta)*cmath.sin(beta))/(2.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*vd*cmath.cos(beta)*cmath.sin(alp)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*vd*cmath.cos(beta)*cmath.sin(alp)*cmath.sin(beta))/(2.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*vd*cmath.cos(alp)*cmath.sin(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*vd*cmath.cos(alp)*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*vu*cmath.sin(alp)*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':1})

GC_2052 = Coupling(name = 'GC_2052',
                   value = '-(ee**2*complex(0,1)*vd*cmath.cos(alp)*cmath.cos(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*vd*cmath.cos(alp)*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*vu*cmath.cos(beta)**2*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*vu*cmath.cos(alp)*cmath.cos(beta)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*vu*cmath.cos(alp)*cmath.cos(beta)*cmath.sin(beta))/(2.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*vd*cmath.cos(beta)*cmath.sin(alp)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*vd*cmath.cos(beta)*cmath.sin(alp)*cmath.sin(beta))/(2.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*vd*cmath.cos(alp)*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*vu*cmath.sin(alp)*cmath.sin(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*vu*cmath.sin(alp)*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':1})

GC_2053 = Coupling(name = 'GC_2053',
                   value = '(ee**2*complex(0,1)*cmath.cos(alp)*cmath.cos(beta)**2*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*cmath.cos(alp)**2*cmath.cos(beta)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*cmath.cos(alp)**2*cmath.cos(beta)*cmath.sin(beta))/(2.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*cmath.cos(beta)*cmath.sin(alp)**2*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*cmath.cos(beta)*cmath.sin(alp)**2*cmath.sin(beta))/(2.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*cmath.cos(alp)*cmath.sin(alp)*cmath.sin(beta)**2)/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_2054 = Coupling(name = 'GC_2054',
                   value = '-(ee**2*complex(0,1)*cmath.cos(alp)*cmath.cos(beta)**2*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*cmath.cos(alp)**2*cmath.cos(beta)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*cmath.cos(alp)**2*cmath.cos(beta)*cmath.sin(beta))/(2.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*cmath.cos(beta)*cmath.sin(alp)**2*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*cmath.cos(beta)*cmath.sin(alp)**2*cmath.sin(beta))/(2.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*cmath.cos(alp)*cmath.sin(alp)*cmath.sin(beta)**2)/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_2055 = Coupling(name = 'GC_2055',
                   value = '(ee**2*complex(0,1)*cmath.cos(alp)*cmath.cos(beta)**2*cmath.sin(alp))/(2.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*cmath.cos(alp)*cmath.sin(alp)*cmath.sin(beta)**2)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_2056 = Coupling(name = 'GC_2056',
                   value = '-(ee**2*complex(0,1)*cmath.cos(alp)*cmath.cos(beta)**2*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*cmath.cos(alp)*cmath.cos(beta)**2*cmath.sin(alp))/(2.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*cmath.cos(alp)**2*cmath.cos(beta)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*cmath.cos(beta)*cmath.sin(alp)**2*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*cmath.cos(alp)*cmath.sin(alp)*cmath.sin(beta)**2)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*cmath.cos(alp)*cmath.sin(alp)*cmath.sin(beta)**2)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_2057 = Coupling(name = 'GC_2057',
                   value = '-(ee**2*complex(0,1)*cmath.cos(alp)*cmath.cos(beta)**2*cmath.sin(alp))/(2.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*cmath.cos(alp)*cmath.sin(alp)*cmath.sin(beta)**2)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_2058 = Coupling(name = 'GC_2058',
                   value = '(ee**2*complex(0,1)*cmath.cos(alp)*cmath.cos(beta)**2*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*cmath.cos(alp)*cmath.cos(beta)**2*cmath.sin(alp))/(2.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*cmath.cos(alp)**2*cmath.cos(beta)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*cmath.cos(beta)*cmath.sin(alp)**2*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*cmath.cos(alp)*cmath.sin(alp)*cmath.sin(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*cmath.cos(alp)*cmath.sin(alp)*cmath.sin(beta)**2)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_2059 = Coupling(name = 'GC_2059',
                   value = '-(ee**2*complex(0,1)*cmath.cos(alp)**2*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*cmath.cos(beta)**2*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*cmath.cos(alp)**2*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*cmath.sin(alp)**2*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_2060 = Coupling(name = 'GC_2060',
                   value = '(ee**2*complex(0,1)*cmath.cos(alp)**2*cmath.cos(beta)**2)/(4.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*cmath.cos(alp)**2*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*cmath.cos(beta)**2*cmath.sin(alp)**2)/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*cmath.cos(beta)**2*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*cmath.cos(alp)*cmath.cos(beta)*cmath.sin(alp)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*cmath.cos(alp)**2*cmath.sin(beta)**2)/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*cmath.cos(alp)**2*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*cmath.sin(alp)**2*cmath.sin(beta)**2)/(4.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*cmath.sin(alp)**2*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_2061 = Coupling(name = 'GC_2061',
                   value = '(ee**2*complex(0,1)*cmath.cos(alp)**2*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*cmath.cos(beta)**2*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*cmath.cos(alp)**2*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*cmath.sin(alp)**2*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_2062 = Coupling(name = 'GC_2062',
                   value = '(ee**2*complex(0,1)*cmath.cos(alp)**2*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*cmath.cos(beta)**2*cmath.sin(alp)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*cmath.cos(beta)**2*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*cmath.cos(alp)*cmath.cos(beta)*cmath.sin(alp)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*cmath.cos(alp)*cmath.cos(beta)*cmath.sin(alp)*cmath.sin(beta))/((-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*cmath.cos(alp)**2*cmath.sin(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*cmath.cos(alp)**2*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*cmath.sin(alp)**2*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_2063 = Coupling(name = 'GC_2063',
                   value = '-(ee**2*complex(0,1)*cmath.cos(alp)**2*cmath.cos(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*cmath.cos(alp)**2*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*cmath.cos(beta)**2*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*cmath.cos(alp)*cmath.cos(beta)*cmath.sin(alp)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*cmath.cos(alp)*cmath.cos(beta)*cmath.sin(alp)*cmath.sin(beta))/((-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*cmath.cos(alp)**2*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*cmath.sin(alp)**2*cmath.sin(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*cmath.sin(alp)**2*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_2064 = Coupling(name = 'GC_2064',
                   value = '(ee**2*vu*cmath.cos(beta)**3)/(4.*sw**2) - (ee**2*vd*cmath.cos(beta)**2*cmath.sin(beta))/(4.*sw**2) + (ee**2*vu*cmath.cos(beta)*cmath.sin(beta)**2)/(4.*sw**2) - (ee**2*vd*cmath.sin(beta)**3)/(4.*sw**2)',
                   order = {'QED':1})

GC_2065 = Coupling(name = 'GC_2065',
                   value = '-(ee**2*vu*cmath.cos(beta)**3)/(4.*sw**2) + (ee**2*vd*cmath.cos(beta)**2*cmath.sin(beta))/(4.*sw**2) - (ee**2*vu*cmath.cos(beta)*cmath.sin(beta)**2)/(4.*sw**2) + (ee**2*vd*cmath.sin(beta)**3)/(4.*sw**2)',
                   order = {'QED':1})

GC_2066 = Coupling(name = 'GC_2066',
                   value = '-(ee**2*vd*cmath.cos(beta)**3)/(4.*sw**2) - (ee**2*vu*cmath.cos(beta)**2*cmath.sin(beta))/(4.*sw**2) - (ee**2*vd*cmath.cos(beta)*cmath.sin(beta)**2)/(4.*sw**2) - (ee**2*vu*cmath.sin(beta)**3)/(4.*sw**2)',
                   order = {'QED':1})

GC_2067 = Coupling(name = 'GC_2067',
                   value = '(ee**2*vd*cmath.cos(beta)**3)/(4.*sw**2) + (ee**2*vu*cmath.cos(beta)**2*cmath.sin(beta))/(4.*sw**2) + (ee**2*vd*cmath.cos(beta)*cmath.sin(beta)**2)/(4.*sw**2) + (ee**2*vu*cmath.sin(beta)**3)/(4.*sw**2)',
                   order = {'QED':1})

GC_2068 = Coupling(name = 'GC_2068',
                   value = '(ee**2*cmath.cos(beta)**3*cmath.sin(alp))/(4.*sw**2) - (ee**2*cmath.cos(alp)*cmath.cos(beta)**2*cmath.sin(beta))/(4.*sw**2) + (ee**2*cmath.cos(beta)*cmath.sin(alp)*cmath.sin(beta)**2)/(4.*sw**2) - (ee**2*cmath.cos(alp)*cmath.sin(beta)**3)/(4.*sw**2)',
                   order = {'QED':2})

GC_2069 = Coupling(name = 'GC_2069',
                   value = '-(ee**2*cmath.cos(beta)**3*cmath.sin(alp))/(4.*sw**2) + (ee**2*cmath.cos(alp)*cmath.cos(beta)**2*cmath.sin(beta))/(4.*sw**2) - (ee**2*cmath.cos(beta)*cmath.sin(alp)*cmath.sin(beta)**2)/(4.*sw**2) + (ee**2*cmath.cos(alp)*cmath.sin(beta)**3)/(4.*sw**2)',
                   order = {'QED':2})

GC_2070 = Coupling(name = 'GC_2070',
                   value = '(ee**2*complex(0,1)*cmath.cos(beta)**3*cmath.sin(beta))/(2.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*cmath.cos(beta)*cmath.sin(beta)**3)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_2071 = Coupling(name = 'GC_2071',
                   value = '-(ee**2*complex(0,1)*cmath.cos(beta)**3*cmath.sin(beta))/(2.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*cmath.cos(beta)*cmath.sin(beta)**3)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_2072 = Coupling(name = 'GC_2072',
                   value = '(ee**2*complex(0,1)*cmath.cos(beta)**3*cmath.sin(beta))/((-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*cmath.cos(beta)*cmath.sin(beta)**3)/((-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_2073 = Coupling(name = 'GC_2073',
                   value = '-((ee**2*complex(0,1)*cmath.cos(beta)**3*cmath.sin(beta))/((-1 + sw)*sw**2*(1 + sw))) + (ee**2*complex(0,1)*cmath.cos(beta)*cmath.sin(beta)**3)/((-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_2074 = Coupling(name = 'GC_2074',
                   value = '(3*ee**2*complex(0,1)*cmath.cos(beta)**3*cmath.sin(beta))/(2.*(-1 + sw)*sw**2*(1 + sw)) - (3*ee**2*complex(0,1)*cmath.cos(beta)*cmath.sin(beta)**3)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_2075 = Coupling(name = 'GC_2075',
                   value = '(-3*ee**2*complex(0,1)*cmath.cos(beta)**3*cmath.sin(beta))/(2.*(-1 + sw)*sw**2*(1 + sw)) + (3*ee**2*complex(0,1)*cmath.cos(beta)*cmath.sin(beta)**3)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_2076 = Coupling(name = 'GC_2076',
                   value = '-(ee**2*cmath.cos(alp)*cmath.cos(beta)**3)/(4.*sw**2) - (ee**2*cmath.cos(beta)**2*cmath.sin(alp)*cmath.sin(beta))/(4.*sw**2) - (ee**2*cmath.cos(alp)*cmath.cos(beta)*cmath.sin(beta)**2)/(4.*sw**2) - (ee**2*cmath.sin(alp)*cmath.sin(beta)**3)/(4.*sw**2)',
                   order = {'QED':2})

GC_2077 = Coupling(name = 'GC_2077',
                   value = '(ee**2*cmath.cos(alp)*cmath.cos(beta)**3)/(4.*sw**2) + (ee**2*cmath.cos(beta)**2*cmath.sin(alp)*cmath.sin(beta))/(4.*sw**2) + (ee**2*cmath.cos(alp)*cmath.cos(beta)*cmath.sin(beta)**2)/(4.*sw**2) + (ee**2*cmath.sin(alp)*cmath.sin(beta)**3)/(4.*sw**2)',
                   order = {'QED':2})

GC_2078 = Coupling(name = 'GC_2078',
                   value = '-(ee**2*complex(0,1)*cmath.cos(beta)**4)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (3*ee**2*complex(0,1)*cmath.cos(beta)**2*cmath.sin(beta)**2)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*cmath.sin(beta)**4)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_2079 = Coupling(name = 'GC_2079',
                   value = '-(ee**2*complex(0,1)*cmath.cos(beta)**4)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (5*ee**2*complex(0,1)*cmath.cos(beta)**2*cmath.sin(beta)**2)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*cmath.sin(beta)**4)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_2080 = Coupling(name = 'GC_2080',
                   value = '(ee**2*complex(0,1)*cmath.cos(beta)**4)/(4.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*cmath.cos(beta)**4)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*cmath.cos(beta)**2*cmath.sin(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*cmath.cos(beta)**2*cmath.sin(beta)**2)/(2.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*cmath.sin(beta)**4)/(4.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*cmath.sin(beta)**4)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_2081 = Coupling(name = 'GC_2081',
                   value = '(ee**2*complex(0,1)*cmath.cos(beta)**4)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*cmath.cos(beta)**2*cmath.sin(beta)**2)/(2.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*cmath.sin(beta)**4)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_2082 = Coupling(name = 'GC_2082',
                   value = '-(ee**2*complex(0,1)*cmath.cos(beta)**4)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*cmath.cos(beta)**4)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*cmath.cos(beta)**2*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) + (3*ee**2*complex(0,1)*cmath.cos(beta)**2*cmath.sin(beta)**2)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*cmath.sin(beta)**4)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*cmath.sin(beta)**4)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_2083 = Coupling(name = 'GC_2083',
                   value = '(ee**2*complex(0,1)*cmath.cos(beta)**4)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*cmath.cos(beta)**2*cmath.sin(beta)**2)/((-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*cmath.sin(beta)**4)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_2084 = Coupling(name = 'GC_2084',
                   value = '(3*ee**2*complex(0,1)*cmath.cos(beta)**4)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (3*ee**2*complex(0,1)*cmath.cos(beta)**2*cmath.sin(beta)**2)/(2.*(-1 + sw)*sw**2*(1 + sw)) + (3*ee**2*complex(0,1)*cmath.sin(beta)**4)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

