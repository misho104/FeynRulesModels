# This file was automatically created by FeynRules $Revision: 634 $
# Mathematica version: 7.0 for Linux x86 (32-bit) (April 23, 2009)
# Date: Tue 22 Nov 2011 02:10:03


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
                 value = '(-2*ee*complex(0,1)*I11311)/3.',
                 order = {'QED':1})

GC_11 = Coupling(name = 'GC_11',
                 value = '-(complex(0,1)*G*I11311)',
                 order = {'QCD':1})

GC_12 = Coupling(name = 'GC_12',
                 value = '(-2*ee*complex(0,1)*I11322)/3.',
                 order = {'QED':1})

GC_13 = Coupling(name = 'GC_13',
                 value = '-(complex(0,1)*G*I11322)',
                 order = {'QCD':1})

GC_14 = Coupling(name = 'GC_14',
                 value = '(-2*ee*complex(0,1)*I11333)/3. - (2*ee*complex(0,1)*I11433)/3.',
                 order = {'QED':1})

GC_15 = Coupling(name = 'GC_15',
                 value = '-(complex(0,1)*G*I11333) - complex(0,1)*G*I11433',
                 order = {'QCD':1})

GC_16 = Coupling(name = 'GC_16',
                 value = '(-2*ee*complex(0,1)*I11336)/3. - (2*ee*complex(0,1)*I11436)/3.',
                 order = {'QED':1})

GC_17 = Coupling(name = 'GC_17',
                 value = '-(complex(0,1)*G*I11336) - complex(0,1)*G*I11436',
                 order = {'QCD':1})

GC_18 = Coupling(name = 'GC_18',
                 value = '(-2*ee*complex(0,1)*I11444)/3.',
                 order = {'QED':1})

GC_19 = Coupling(name = 'GC_19',
                 value = '-(complex(0,1)*G*I11444)',
                 order = {'QCD':1})

GC_20 = Coupling(name = 'GC_20',
                 value = '(-2*ee*complex(0,1)*I11455)/3.',
                 order = {'QED':1})

GC_21 = Coupling(name = 'GC_21',
                 value = '-(complex(0,1)*G*I11455)',
                 order = {'QCD':1})

GC_22 = Coupling(name = 'GC_22',
                 value = '(2*ee*complex(0,1)*I11363)/3. + (2*ee*complex(0,1)*I11463)/3.',
                 order = {'QED':1})

GC_23 = Coupling(name = 'GC_23',
                 value = 'complex(0,1)*G*I11363 + complex(0,1)*G*I11463',
                 order = {'QCD':1})

GC_24 = Coupling(name = 'GC_24',
                 value = '(-2*ee*complex(0,1)*I11366)/3. - (2*ee*complex(0,1)*I11466)/3.',
                 order = {'QED':1})

GC_25 = Coupling(name = 'GC_25',
                 value = '-(complex(0,1)*G*I11366) - complex(0,1)*G*I11466',
                 order = {'QCD':1})

GC_26 = Coupling(name = 'GC_26',
                 value = '(2*ee**2*complex(0,1)*I1211)/9.',
                 order = {'QED':2})

GC_27 = Coupling(name = 'GC_27',
                 value = '(-2*ee*complex(0,1)*G*I1211)/3.',
                 order = {'QCD':1,'QED':1})

GC_28 = Coupling(name = 'GC_28',
                 value = 'complex(0,1)*G**2*I1211',
                 order = {'QCD':2})

GC_29 = Coupling(name = 'GC_29',
                 value = '(2*ee**2*complex(0,1)*I1222)/9.',
                 order = {'QED':2})

GC_30 = Coupling(name = 'GC_30',
                 value = '(-2*ee*complex(0,1)*G*I1222)/3.',
                 order = {'QCD':1,'QED':1})

GC_31 = Coupling(name = 'GC_31',
                 value = 'complex(0,1)*G**2*I1222',
                 order = {'QCD':2})

GC_32 = Coupling(name = 'GC_32',
                 value = '(2*ee**2*complex(0,1)*I1233)/9. + (2*ee**2*complex(0,1)*I1333)/9.',
                 order = {'QED':2})

GC_33 = Coupling(name = 'GC_33',
                 value = '(-2*ee*complex(0,1)*G*I1233)/3. - (2*ee*complex(0,1)*G*I1333)/3.',
                 order = {'QCD':1,'QED':1})

GC_34 = Coupling(name = 'GC_34',
                 value = 'complex(0,1)*G**2*I1233 + complex(0,1)*G**2*I1333',
                 order = {'QCD':2})

GC_35 = Coupling(name = 'GC_35',
                 value = '(2*ee**2*complex(0,1)*I1236)/9. + (2*ee**2*complex(0,1)*I1336)/9.',
                 order = {'QED':2})

GC_36 = Coupling(name = 'GC_36',
                 value = '(-2*ee*complex(0,1)*G*I1236)/3. - (2*ee*complex(0,1)*G*I1336)/3.',
                 order = {'QCD':1,'QED':1})

GC_37 = Coupling(name = 'GC_37',
                 value = 'complex(0,1)*G**2*I1236 + complex(0,1)*G**2*I1336',
                 order = {'QCD':2})

GC_38 = Coupling(name = 'GC_38',
                 value = '(2*ee**2*complex(0,1)*I1344)/9.',
                 order = {'QED':2})

GC_39 = Coupling(name = 'GC_39',
                 value = '(-2*ee*complex(0,1)*G*I1344)/3.',
                 order = {'QCD':1,'QED':1})

GC_40 = Coupling(name = 'GC_40',
                 value = 'complex(0,1)*G**2*I1344',
                 order = {'QCD':2})

GC_41 = Coupling(name = 'GC_41',
                 value = '(2*ee**2*complex(0,1)*I1355)/9.',
                 order = {'QED':2})

GC_42 = Coupling(name = 'GC_42',
                 value = '(-2*ee*complex(0,1)*G*I1355)/3.',
                 order = {'QCD':1,'QED':1})

GC_43 = Coupling(name = 'GC_43',
                 value = 'complex(0,1)*G**2*I1355',
                 order = {'QCD':2})

GC_44 = Coupling(name = 'GC_44',
                 value = '(2*ee**2*complex(0,1)*I1263)/9. + (2*ee**2*complex(0,1)*I1363)/9.',
                 order = {'QED':2})

GC_45 = Coupling(name = 'GC_45',
                 value = '(-2*ee*complex(0,1)*G*I1263)/3. - (2*ee*complex(0,1)*G*I1363)/3.',
                 order = {'QCD':1,'QED':1})

GC_46 = Coupling(name = 'GC_46',
                 value = 'complex(0,1)*G**2*I1263 + complex(0,1)*G**2*I1363',
                 order = {'QCD':2})

GC_47 = Coupling(name = 'GC_47',
                 value = '(2*ee**2*complex(0,1)*I1266)/9. + (2*ee**2*complex(0,1)*I1366)/9.',
                 order = {'QED':2})

GC_48 = Coupling(name = 'GC_48',
                 value = '(-2*ee*complex(0,1)*G*I1266)/3. - (2*ee*complex(0,1)*G*I1366)/3.',
                 order = {'QCD':1,'QED':1})

GC_49 = Coupling(name = 'GC_49',
                 value = 'complex(0,1)*G**2*I1266 + complex(0,1)*G**2*I1366',
                 order = {'QCD':2})

GC_50 = Coupling(name = 'GC_50',
                 value = '(8*ee**2*complex(0,1)*I14811)/9.',
                 order = {'QED':2})

GC_51 = Coupling(name = 'GC_51',
                 value = '(4*ee*complex(0,1)*G*I14811)/3.',
                 order = {'QCD':1,'QED':1})

GC_52 = Coupling(name = 'GC_52',
                 value = 'complex(0,1)*G**2*I14811',
                 order = {'QCD':2})

GC_53 = Coupling(name = 'GC_53',
                 value = '(8*ee**2*complex(0,1)*I14822)/9.',
                 order = {'QED':2})

GC_54 = Coupling(name = 'GC_54',
                 value = '(4*ee*complex(0,1)*G*I14822)/3.',
                 order = {'QCD':1,'QED':1})

GC_55 = Coupling(name = 'GC_55',
                 value = 'complex(0,1)*G**2*I14822',
                 order = {'QCD':2})

GC_56 = Coupling(name = 'GC_56',
                 value = '(8*ee**2*complex(0,1)*I14833)/9. + (8*ee**2*complex(0,1)*I14933)/9.',
                 order = {'QED':2})

GC_57 = Coupling(name = 'GC_57',
                 value = '(4*ee*complex(0,1)*G*I14833)/3. + (4*ee*complex(0,1)*G*I14933)/3.',
                 order = {'QCD':1,'QED':1})

GC_58 = Coupling(name = 'GC_58',
                 value = 'complex(0,1)*G**2*I14833 + complex(0,1)*G**2*I14933',
                 order = {'QCD':2})

GC_59 = Coupling(name = 'GC_59',
                 value = '(8*ee**2*complex(0,1)*I14836)/9. + (8*ee**2*complex(0,1)*I14936)/9.',
                 order = {'QED':2})

GC_60 = Coupling(name = 'GC_60',
                 value = '(4*ee*complex(0,1)*G*I14836)/3. + (4*ee*complex(0,1)*G*I14936)/3.',
                 order = {'QCD':1,'QED':1})

GC_61 = Coupling(name = 'GC_61',
                 value = 'complex(0,1)*G**2*I14836 + complex(0,1)*G**2*I14936',
                 order = {'QCD':2})

GC_62 = Coupling(name = 'GC_62',
                 value = '(8*ee**2*complex(0,1)*I14944)/9.',
                 order = {'QED':2})

GC_63 = Coupling(name = 'GC_63',
                 value = '(4*ee*complex(0,1)*G*I14944)/3.',
                 order = {'QCD':1,'QED':1})

GC_64 = Coupling(name = 'GC_64',
                 value = 'complex(0,1)*G**2*I14944',
                 order = {'QCD':2})

GC_65 = Coupling(name = 'GC_65',
                 value = '(8*ee**2*complex(0,1)*I14955)/9.',
                 order = {'QED':2})

GC_66 = Coupling(name = 'GC_66',
                 value = '(4*ee*complex(0,1)*G*I14955)/3.',
                 order = {'QCD':1,'QED':1})

GC_67 = Coupling(name = 'GC_67',
                 value = 'complex(0,1)*G**2*I14955',
                 order = {'QCD':2})

GC_68 = Coupling(name = 'GC_68',
                 value = '(8*ee**2*complex(0,1)*I14863)/9. + (8*ee**2*complex(0,1)*I14963)/9.',
                 order = {'QED':2})

GC_69 = Coupling(name = 'GC_69',
                 value = '(4*ee*complex(0,1)*G*I14863)/3. + (4*ee*complex(0,1)*G*I14963)/3.',
                 order = {'QCD':1,'QED':1})

GC_70 = Coupling(name = 'GC_70',
                 value = 'complex(0,1)*G**2*I14863 + complex(0,1)*G**2*I14963',
                 order = {'QCD':2})

GC_71 = Coupling(name = 'GC_71',
                 value = '(8*ee**2*complex(0,1)*I14866)/9. + (8*ee**2*complex(0,1)*I14966)/9.',
                 order = {'QED':2})

GC_72 = Coupling(name = 'GC_72',
                 value = '(4*ee*complex(0,1)*G*I14866)/3. + (4*ee*complex(0,1)*G*I14966)/3.',
                 order = {'QCD':1,'QED':1})

GC_73 = Coupling(name = 'GC_73',
                 value = 'complex(0,1)*G**2*I14866 + complex(0,1)*G**2*I14966',
                 order = {'QCD':2})

GC_74 = Coupling(name = 'GC_74',
                 value = 'ee*complex(0,1)*I4711',
                 order = {'QED':1})

GC_75 = Coupling(name = 'GC_75',
                 value = 'ee*complex(0,1)*I4722',
                 order = {'QED':1})

GC_76 = Coupling(name = 'GC_76',
                 value = 'ee*complex(0,1)*I4733 + ee*complex(0,1)*I4833',
                 order = {'QED':1})

GC_77 = Coupling(name = 'GC_77',
                 value = 'ee*complex(0,1)*I4736 + ee*complex(0,1)*I4836',
                 order = {'QED':1})

GC_78 = Coupling(name = 'GC_78',
                 value = 'ee*complex(0,1)*I4844',
                 order = {'QED':1})

GC_79 = Coupling(name = 'GC_79',
                 value = 'ee*complex(0,1)*I4855',
                 order = {'QED':1})

GC_80 = Coupling(name = 'GC_80',
                 value = '-(ee*complex(0,1)*I4763) - ee*complex(0,1)*I4863',
                 order = {'QED':1})

GC_81 = Coupling(name = 'GC_81',
                 value = 'ee*complex(0,1)*I4766 + ee*complex(0,1)*I4866',
                 order = {'QED':1})

GC_82 = Coupling(name = 'GC_82',
                 value = '(ee*complex(0,1)*I511)/3.',
                 order = {'QED':1})

GC_83 = Coupling(name = 'GC_83',
                 value = '-(complex(0,1)*G*I511)',
                 order = {'QCD':1})

GC_84 = Coupling(name = 'GC_84',
                 value = '(ee*complex(0,1)*I522)/3.',
                 order = {'QED':1})

GC_85 = Coupling(name = 'GC_85',
                 value = '-(complex(0,1)*G*I522)',
                 order = {'QCD':1})

GC_86 = Coupling(name = 'GC_86',
                 value = '2*ee**2*complex(0,1)*I5311',
                 order = {'QED':2})

GC_87 = Coupling(name = 'GC_87',
                 value = '2*ee**2*complex(0,1)*I5322',
                 order = {'QED':2})

GC_88 = Coupling(name = 'GC_88',
                 value = '2*ee**2*complex(0,1)*I5333 + 2*ee**2*complex(0,1)*I5433',
                 order = {'QED':2})

GC_89 = Coupling(name = 'GC_89',
                 value = '2*ee**2*complex(0,1)*I5336 + 2*ee**2*complex(0,1)*I5436',
                 order = {'QED':2})

GC_90 = Coupling(name = 'GC_90',
                 value = '2*ee**2*complex(0,1)*I5444',
                 order = {'QED':2})

GC_91 = Coupling(name = 'GC_91',
                 value = '2*ee**2*complex(0,1)*I5455',
                 order = {'QED':2})

GC_92 = Coupling(name = 'GC_92',
                 value = '2*ee**2*complex(0,1)*I5363 + 2*ee**2*complex(0,1)*I5463',
                 order = {'QED':2})

GC_93 = Coupling(name = 'GC_93',
                 value = '2*ee**2*complex(0,1)*I5366 + 2*ee**2*complex(0,1)*I5466',
                 order = {'QED':2})

GC_94 = Coupling(name = 'GC_94',
                 value = '(ee*complex(0,1)*I533)/3. + (ee*complex(0,1)*I633)/3.',
                 order = {'QED':1})

GC_95 = Coupling(name = 'GC_95',
                 value = '-(complex(0,1)*G*I533) - complex(0,1)*G*I633',
                 order = {'QCD':1})

GC_96 = Coupling(name = 'GC_96',
                 value = '(ee*complex(0,1)*I536)/3. + (ee*complex(0,1)*I636)/3.',
                 order = {'QED':1})

GC_97 = Coupling(name = 'GC_97',
                 value = '-(complex(0,1)*G*I536) - complex(0,1)*G*I636',
                 order = {'QCD':1})

GC_98 = Coupling(name = 'GC_98',
                 value = '(ee*complex(0,1)*I644)/3.',
                 order = {'QED':1})

GC_99 = Coupling(name = 'GC_99',
                 value = '-(complex(0,1)*G*I644)',
                 order = {'QCD':1})

GC_100 = Coupling(name = 'GC_100',
                  value = '(ee*complex(0,1)*I655)/3.',
                  order = {'QED':1})

GC_101 = Coupling(name = 'GC_101',
                  value = '-(complex(0,1)*G*I655)',
                  order = {'QCD':1})

GC_102 = Coupling(name = 'GC_102',
                  value = '-(ee*complex(0,1)*I563)/3. - (ee*complex(0,1)*I663)/3.',
                  order = {'QED':1})

GC_103 = Coupling(name = 'GC_103',
                  value = 'complex(0,1)*G*I563 + complex(0,1)*G*I663',
                  order = {'QCD':1})

GC_104 = Coupling(name = 'GC_104',
                  value = '(ee*complex(0,1)*I566)/3. + (ee*complex(0,1)*I666)/3.',
                  order = {'QED':1})

GC_105 = Coupling(name = 'GC_105',
                  value = '-(complex(0,1)*G*I566) - complex(0,1)*G*I666',
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
                  value = '-(complex(0,1)*I12933*I13033) - (ee**2*complex(0,1)*I12733*I12833)/(2.*sw**2)',
                  order = {'QED':2})

GC_124 = Coupling(name = 'GC_124',
                  value = '-(complex(0,1)*I12933*I13036) - (ee**2*complex(0,1)*I12736*I12833)/(2.*sw**2)',
                  order = {'QED':2})

GC_125 = Coupling(name = 'GC_125',
                  value = '-(complex(0,1)*I12933*I13063) - (ee**2*complex(0,1)*I12763*I12833)/(2.*sw**2)',
                  order = {'QED':2})

GC_126 = Coupling(name = 'GC_126',
                  value = '-(complex(0,1)*I12933*I13066) - (ee**2*complex(0,1)*I12766*I12833)/(2.*sw**2)',
                  order = {'QED':2})

GC_127 = Coupling(name = 'GC_127',
                  value = '-(complex(0,1)*I12936*I13033) - (ee**2*complex(0,1)*I12733*I12836)/(2.*sw**2)',
                  order = {'QED':2})

GC_128 = Coupling(name = 'GC_128',
                  value = '-(complex(0,1)*I12936*I13036) - (ee**2*complex(0,1)*I12736*I12836)/(2.*sw**2)',
                  order = {'QED':2})

GC_129 = Coupling(name = 'GC_129',
                  value = '-(complex(0,1)*I12936*I13063) - (ee**2*complex(0,1)*I12763*I12836)/(2.*sw**2)',
                  order = {'QED':2})

GC_130 = Coupling(name = 'GC_130',
                  value = '-(complex(0,1)*I12936*I13066) - (ee**2*complex(0,1)*I12766*I12836)/(2.*sw**2)',
                  order = {'QED':2})

GC_131 = Coupling(name = 'GC_131',
                  value = '-(complex(0,1)*I11033*I16033) - (ee**2*complex(0,1)*I10733*I15933)/(2.*sw**2)',
                  order = {'QED':2})

GC_132 = Coupling(name = 'GC_132',
                  value = '-(complex(0,1)*I11036*I16033) - (ee**2*complex(0,1)*I10736*I15933)/(2.*sw**2)',
                  order = {'QED':2})

GC_133 = Coupling(name = 'GC_133',
                  value = '-(complex(0,1)*I11033*I16036) - (ee**2*complex(0,1)*I10733*I15936)/(2.*sw**2)',
                  order = {'QED':2})

GC_134 = Coupling(name = 'GC_134',
                  value = '-(complex(0,1)*I11036*I16036) - (ee**2*complex(0,1)*I10736*I15936)/(2.*sw**2)',
                  order = {'QED':2})

GC_135 = Coupling(name = 'GC_135',
                  value = '-(complex(0,1)*I11033*I16063) - (ee**2*complex(0,1)*I10733*I15963)/(2.*sw**2)',
                  order = {'QED':2})

GC_136 = Coupling(name = 'GC_136',
                  value = '-(complex(0,1)*I11036*I16063) - (ee**2*complex(0,1)*I10736*I15963)/(2.*sw**2)',
                  order = {'QED':2})

GC_137 = Coupling(name = 'GC_137',
                  value = '-(complex(0,1)*I11033*I16066) - (ee**2*complex(0,1)*I10733*I15966)/(2.*sw**2)',
                  order = {'QED':2})

GC_138 = Coupling(name = 'GC_138',
                  value = '-(complex(0,1)*I11036*I16066) - (ee**2*complex(0,1)*I10736*I15966)/(2.*sw**2)',
                  order = {'QED':2})

GC_139 = Coupling(name = 'GC_139',
                  value = '(ee**2*complex(0,1))/(2.*sw**2)',
                  order = {'QED':2})

GC_140 = Coupling(name = 'GC_140',
                  value = '-((ee**2*complex(0,1))/sw**2)',
                  order = {'QED':2})

GC_141 = Coupling(name = 'GC_141',
                  value = '(ee**2*complex(0,1)*I10511)/(2.*sw**2)',
                  order = {'QED':2})

GC_142 = Coupling(name = 'GC_142',
                  value = '(ee**2*complex(0,1)*I10522)/(2.*sw**2)',
                  order = {'QED':2})

GC_143 = Coupling(name = 'GC_143',
                  value = '(ee**2*complex(0,1)*I10533)/(2.*sw**2)',
                  order = {'QED':2})

GC_144 = Coupling(name = 'GC_144',
                  value = '(ee**2*complex(0,1)*I10536)/(2.*sw**2)',
                  order = {'QED':2})

GC_145 = Coupling(name = 'GC_145',
                  value = '(ee**2*complex(0,1)*I10563)/(2.*sw**2)',
                  order = {'QED':2})

GC_146 = Coupling(name = 'GC_146',
                  value = '(ee**2*complex(0,1)*I10566)/(2.*sw**2)',
                  order = {'QED':2})

GC_147 = Coupling(name = 'GC_147',
                  value = '-(ee**2*complex(0,1)*I12711*I12811)/(2.*sw**2)',
                  order = {'QED':2})

GC_148 = Coupling(name = 'GC_148',
                  value = '-(ee**2*complex(0,1)*I12722*I12811)/(2.*sw**2)',
                  order = {'QED':2})

GC_149 = Coupling(name = 'GC_149',
                  value = '-(ee**2*complex(0,1)*I12733*I12811)/(2.*sw**2)',
                  order = {'QED':2})

GC_150 = Coupling(name = 'GC_150',
                  value = '-(ee**2*complex(0,1)*I12736*I12811)/(2.*sw**2)',
                  order = {'QED':2})

GC_151 = Coupling(name = 'GC_151',
                  value = '-(ee**2*complex(0,1)*I12763*I12811)/(2.*sw**2)',
                  order = {'QED':2})

GC_152 = Coupling(name = 'GC_152',
                  value = '-(ee**2*complex(0,1)*I12766*I12811)/(2.*sw**2)',
                  order = {'QED':2})

GC_153 = Coupling(name = 'GC_153',
                  value = '-(ee**2*complex(0,1)*I12711*I12822)/(2.*sw**2)',
                  order = {'QED':2})

GC_154 = Coupling(name = 'GC_154',
                  value = '-(ee**2*complex(0,1)*I12722*I12822)/(2.*sw**2)',
                  order = {'QED':2})

GC_155 = Coupling(name = 'GC_155',
                  value = '-(ee**2*complex(0,1)*I12733*I12822)/(2.*sw**2)',
                  order = {'QED':2})

GC_156 = Coupling(name = 'GC_156',
                  value = '-(ee**2*complex(0,1)*I12736*I12822)/(2.*sw**2)',
                  order = {'QED':2})

GC_157 = Coupling(name = 'GC_157',
                  value = '-(ee**2*complex(0,1)*I12763*I12822)/(2.*sw**2)',
                  order = {'QED':2})

GC_158 = Coupling(name = 'GC_158',
                  value = '-(ee**2*complex(0,1)*I12766*I12822)/(2.*sw**2)',
                  order = {'QED':2})

GC_159 = Coupling(name = 'GC_159',
                  value = '-(ee**2*complex(0,1)*I12711*I12833)/(2.*sw**2)',
                  order = {'QED':2})

GC_160 = Coupling(name = 'GC_160',
                  value = '-(ee**2*complex(0,1)*I12722*I12833)/(2.*sw**2)',
                  order = {'QED':2})

GC_161 = Coupling(name = 'GC_161',
                  value = '-(ee**2*complex(0,1)*I12711*I12836)/(2.*sw**2)',
                  order = {'QED':2})

GC_162 = Coupling(name = 'GC_162',
                  value = '-(ee**2*complex(0,1)*I12722*I12836)/(2.*sw**2)',
                  order = {'QED':2})

GC_163 = Coupling(name = 'GC_163',
                  value = '-(ee**2*complex(0,1)*I10711*I15911)/(2.*sw**2)',
                  order = {'QED':2})

GC_164 = Coupling(name = 'GC_164',
                  value = '-(ee**2*complex(0,1)*I10722*I15911)/(2.*sw**2)',
                  order = {'QED':2})

GC_165 = Coupling(name = 'GC_165',
                  value = '-(ee**2*complex(0,1)*I10733*I15911)/(2.*sw**2)',
                  order = {'QED':2})

GC_166 = Coupling(name = 'GC_166',
                  value = '-(ee**2*complex(0,1)*I10736*I15911)/(2.*sw**2)',
                  order = {'QED':2})

GC_167 = Coupling(name = 'GC_167',
                  value = '-(ee**2*complex(0,1)*I10711*I15922)/(2.*sw**2)',
                  order = {'QED':2})

GC_168 = Coupling(name = 'GC_168',
                  value = '-(ee**2*complex(0,1)*I10722*I15922)/(2.*sw**2)',
                  order = {'QED':2})

GC_169 = Coupling(name = 'GC_169',
                  value = '-(ee**2*complex(0,1)*I10733*I15922)/(2.*sw**2)',
                  order = {'QED':2})

GC_170 = Coupling(name = 'GC_170',
                  value = '-(ee**2*complex(0,1)*I10736*I15922)/(2.*sw**2)',
                  order = {'QED':2})

GC_171 = Coupling(name = 'GC_171',
                  value = '-(ee**2*complex(0,1)*I10711*I15933)/(2.*sw**2)',
                  order = {'QED':2})

GC_172 = Coupling(name = 'GC_172',
                  value = '-(ee**2*complex(0,1)*I10722*I15933)/(2.*sw**2)',
                  order = {'QED':2})

GC_173 = Coupling(name = 'GC_173',
                  value = '-(ee**2*complex(0,1)*I10711*I15936)/(2.*sw**2)',
                  order = {'QED':2})

GC_174 = Coupling(name = 'GC_174',
                  value = '-(ee**2*complex(0,1)*I10722*I15936)/(2.*sw**2)',
                  order = {'QED':2})

GC_175 = Coupling(name = 'GC_175',
                  value = '-(ee**2*complex(0,1)*I10711*I15963)/(2.*sw**2)',
                  order = {'QED':2})

GC_176 = Coupling(name = 'GC_176',
                  value = '-(ee**2*complex(0,1)*I10722*I15963)/(2.*sw**2)',
                  order = {'QED':2})

GC_177 = Coupling(name = 'GC_177',
                  value = '-(ee**2*complex(0,1)*I10711*I15966)/(2.*sw**2)',
                  order = {'QED':2})

GC_178 = Coupling(name = 'GC_178',
                  value = '-(ee**2*complex(0,1)*I10722*I15966)/(2.*sw**2)',
                  order = {'QED':2})

GC_179 = Coupling(name = 'GC_179',
                  value = '(ee**2*complex(0,1)*I20111)/(2.*sw**2)',
                  order = {'QED':2})

GC_180 = Coupling(name = 'GC_180',
                  value = '(ee**2*complex(0,1)*I20122)/(2.*sw**2)',
                  order = {'QED':2})

GC_181 = Coupling(name = 'GC_181',
                  value = '(ee**2*complex(0,1)*I20133)/(2.*sw**2)',
                  order = {'QED':2})

GC_182 = Coupling(name = 'GC_182',
                  value = '(ee**2*complex(0,1)*I20136)/(2.*sw**2)',
                  order = {'QED':2})

GC_183 = Coupling(name = 'GC_183',
                  value = '(ee**2*complex(0,1)*I20163)/(2.*sw**2)',
                  order = {'QED':2})

GC_184 = Coupling(name = 'GC_184',
                  value = '(ee**2*complex(0,1)*I20166)/(2.*sw**2)',
                  order = {'QED':2})

GC_185 = Coupling(name = 'GC_185',
                  value = '(ee**2*complex(0,1)*I6511)/(2.*sw**2)',
                  order = {'QED':2})

GC_186 = Coupling(name = 'GC_186',
                  value = '(ee**2*complex(0,1)*I6522)/(2.*sw**2)',
                  order = {'QED':2})

GC_187 = Coupling(name = 'GC_187',
                  value = '(ee**2*complex(0,1)*I6533)/(2.*sw**2)',
                  order = {'QED':2})

GC_188 = Coupling(name = 'GC_188',
                  value = '(ee**2*complex(0,1)*I6536)/(2.*sw**2)',
                  order = {'QED':2})

GC_189 = Coupling(name = 'GC_189',
                  value = '(ee**2*complex(0,1)*I6563)/(2.*sw**2)',
                  order = {'QED':2})

GC_190 = Coupling(name = 'GC_190',
                  value = '(ee**2*complex(0,1)*I6566)/(2.*sw**2)',
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
                  value = '(cw*ee*complex(0,1))/sw',
                  order = {'QED':1})

GC_196 = Coupling(name = 'GC_196',
                  value = '(-2*cw*ee**2*complex(0,1))/sw',
                  order = {'QED':2})

GC_197 = Coupling(name = 'GC_197',
                  value = '(ee**2*complex(0,1)*I11511)/(3.*sw*cmath.sqrt(2))',
                  order = {'QED':2})

GC_198 = Coupling(name = 'GC_198',
                  value = '(ee*complex(0,1)*G*I11511*cmath.sqrt(2))/sw',
                  order = {'QCD':1,'QED':1})

GC_199 = Coupling(name = 'GC_199',
                  value = '(ee**2*complex(0,1)*I11522)/(3.*sw*cmath.sqrt(2))',
                  order = {'QED':2})

GC_200 = Coupling(name = 'GC_200',
                  value = '(ee*complex(0,1)*G*I11522*cmath.sqrt(2))/sw',
                  order = {'QCD':1,'QED':1})

GC_201 = Coupling(name = 'GC_201',
                  value = '(ee**2*complex(0,1)*I11533)/(3.*sw*cmath.sqrt(2))',
                  order = {'QED':2})

GC_202 = Coupling(name = 'GC_202',
                  value = '(ee*complex(0,1)*G*I11533*cmath.sqrt(2))/sw',
                  order = {'QCD':1,'QED':1})

GC_203 = Coupling(name = 'GC_203',
                  value = '(ee**2*complex(0,1)*I11536)/(3.*sw*cmath.sqrt(2))',
                  order = {'QED':2})

GC_204 = Coupling(name = 'GC_204',
                  value = '(ee*complex(0,1)*G*I11536*cmath.sqrt(2))/sw',
                  order = {'QCD':1,'QED':1})

GC_205 = Coupling(name = 'GC_205',
                  value = '(ee**2*complex(0,1)*I11563)/(3.*sw*cmath.sqrt(2))',
                  order = {'QED':2})

GC_206 = Coupling(name = 'GC_206',
                  value = '(ee*complex(0,1)*G*I11563*cmath.sqrt(2))/sw',
                  order = {'QCD':1,'QED':1})

GC_207 = Coupling(name = 'GC_207',
                  value = '(ee**2*complex(0,1)*I11566)/(3.*sw*cmath.sqrt(2))',
                  order = {'QED':2})

GC_208 = Coupling(name = 'GC_208',
                  value = '(ee*complex(0,1)*G*I11566*cmath.sqrt(2))/sw',
                  order = {'QCD':1,'QED':1})

GC_209 = Coupling(name = 'GC_209',
                  value = '(ee**2*complex(0,1)*I13611)/(3.*sw*cmath.sqrt(2))',
                  order = {'QED':2})

GC_210 = Coupling(name = 'GC_210',
                  value = '(ee*complex(0,1)*G*I13611*cmath.sqrt(2))/sw',
                  order = {'QCD':1,'QED':1})

GC_211 = Coupling(name = 'GC_211',
                  value = '(ee**2*complex(0,1)*I13622)/(3.*sw*cmath.sqrt(2))',
                  order = {'QED':2})

GC_212 = Coupling(name = 'GC_212',
                  value = '(ee*complex(0,1)*G*I13622*cmath.sqrt(2))/sw',
                  order = {'QCD':1,'QED':1})

GC_213 = Coupling(name = 'GC_213',
                  value = '(ee**2*complex(0,1)*I13633)/(3.*sw*cmath.sqrt(2))',
                  order = {'QED':2})

GC_214 = Coupling(name = 'GC_214',
                  value = '(ee*complex(0,1)*G*I13633*cmath.sqrt(2))/sw',
                  order = {'QCD':1,'QED':1})

GC_215 = Coupling(name = 'GC_215',
                  value = '(ee**2*complex(0,1)*I13636)/(3.*sw*cmath.sqrt(2))',
                  order = {'QED':2})

GC_216 = Coupling(name = 'GC_216',
                  value = '(ee*complex(0,1)*G*I13636*cmath.sqrt(2))/sw',
                  order = {'QCD':1,'QED':1})

GC_217 = Coupling(name = 'GC_217',
                  value = '(ee**2*complex(0,1)*I13663)/(3.*sw*cmath.sqrt(2))',
                  order = {'QED':2})

GC_218 = Coupling(name = 'GC_218',
                  value = '(ee*complex(0,1)*G*I13663*cmath.sqrt(2))/sw',
                  order = {'QCD':1,'QED':1})

GC_219 = Coupling(name = 'GC_219',
                  value = '(ee**2*complex(0,1)*I13666)/(3.*sw*cmath.sqrt(2))',
                  order = {'QED':2})

GC_220 = Coupling(name = 'GC_220',
                  value = '(ee*complex(0,1)*G*I13666*cmath.sqrt(2))/sw',
                  order = {'QCD':1,'QED':1})

GC_221 = Coupling(name = 'GC_221',
                  value = '-((ee*complex(0,1)*I19711)/(sw*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_222 = Coupling(name = 'GC_222',
                  value = '-((ee*complex(0,1)*I19722)/(sw*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_223 = Coupling(name = 'GC_223',
                  value = '-((ee*complex(0,1)*I19733)/(sw*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_224 = Coupling(name = 'GC_224',
                  value = '-((ee*complex(0,1)*I19736)/(sw*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_225 = Coupling(name = 'GC_225',
                  value = '-((ee*complex(0,1)*I19763)/(sw*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_226 = Coupling(name = 'GC_226',
                  value = '-((ee*complex(0,1)*I19766)/(sw*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_227 = Coupling(name = 'GC_227',
                  value = '-((ee*complex(0,1)*I19811)/(sw*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_228 = Coupling(name = 'GC_228',
                  value = '-((ee*complex(0,1)*I19822)/(sw*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_229 = Coupling(name = 'GC_229',
                  value = '-((ee*complex(0,1)*I19833)/(sw*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_230 = Coupling(name = 'GC_230',
                  value = '-((ee*complex(0,1)*I19836)/(sw*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_231 = Coupling(name = 'GC_231',
                  value = '(ee*complex(0,1)*I19911)/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_232 = Coupling(name = 'GC_232',
                  value = '(ee*complex(0,1)*I19922)/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_233 = Coupling(name = 'GC_233',
                  value = '(ee*complex(0,1)*I19933)/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_234 = Coupling(name = 'GC_234',
                  value = '(ee*complex(0,1)*I19936)/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_235 = Coupling(name = 'GC_235',
                  value = '(ee*complex(0,1)*I19963)/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_236 = Coupling(name = 'GC_236',
                  value = '(ee*complex(0,1)*I19966)/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_237 = Coupling(name = 'GC_237',
                  value = '(ee*complex(0,1)*I20011)/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_238 = Coupling(name = 'GC_238',
                  value = '(ee*complex(0,1)*I20022)/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_239 = Coupling(name = 'GC_239',
                  value = '(ee*complex(0,1)*I20033)/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_240 = Coupling(name = 'GC_240',
                  value = '(ee*complex(0,1)*I20036)/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_241 = Coupling(name = 'GC_241',
                  value = '-((ee**2*complex(0,1)*I9011)/(sw*cmath.sqrt(2)))',
                  order = {'QED':2})

GC_242 = Coupling(name = 'GC_242',
                  value = '-((ee**2*complex(0,1)*I9022)/(sw*cmath.sqrt(2)))',
                  order = {'QED':2})

GC_243 = Coupling(name = 'GC_243',
                  value = '-((ee**2*complex(0,1)*I9033)/(sw*cmath.sqrt(2)))',
                  order = {'QED':2})

GC_244 = Coupling(name = 'GC_244',
                  value = '-((ee**2*complex(0,1)*I9036)/(sw*cmath.sqrt(2)))',
                  order = {'QED':2})

GC_245 = Coupling(name = 'GC_245',
                  value = '-((ee**2*complex(0,1)*I9811)/(sw*cmath.sqrt(2)))',
                  order = {'QED':2})

GC_246 = Coupling(name = 'GC_246',
                  value = '-((ee**2*complex(0,1)*I9822)/(sw*cmath.sqrt(2)))',
                  order = {'QED':2})

GC_247 = Coupling(name = 'GC_247',
                  value = '-((ee**2*complex(0,1)*I9833)/(sw*cmath.sqrt(2)))',
                  order = {'QED':2})

GC_248 = Coupling(name = 'GC_248',
                  value = '-((ee**2*complex(0,1)*I9836)/(sw*cmath.sqrt(2)))',
                  order = {'QED':2})

GC_249 = Coupling(name = 'GC_249',
                  value = '-(ee**2*complex(0,1)*I10644)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_250 = Coupling(name = 'GC_250',
                  value = '-(ee**2*complex(0,1)*I10655)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_251 = Coupling(name = 'GC_251',
                  value = '(ee**2*complex(0,1)*I14944)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_252 = Coupling(name = 'GC_252',
                  value = '(ee**2*complex(0,1)*I14955)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_253 = Coupling(name = 'GC_253',
                  value = '(ee**2*complex(0,1)*I10644*I16111)/(6.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_254 = Coupling(name = 'GC_254',
                  value = '(ee**2*complex(0,1)*I10655*I16111)/(6.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_255 = Coupling(name = 'GC_255',
                  value = '(ee**2*complex(0,1)*I10644*I16122)/(6.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_256 = Coupling(name = 'GC_256',
                  value = '(ee**2*complex(0,1)*I10655*I16122)/(6.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_257 = Coupling(name = 'GC_257',
                  value = '(ee**2*complex(0,1)*I10511*I16244)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_258 = Coupling(name = 'GC_258',
                  value = '(ee**2*complex(0,1)*I10522*I16244)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_259 = Coupling(name = 'GC_259',
                  value = '(-2*ee**2*complex(0,1)*I10644*I16244)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_260 = Coupling(name = 'GC_260',
                  value = '(-2*ee**2*complex(0,1)*I10655*I16244)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_261 = Coupling(name = 'GC_261',
                  value = '(ee**2*complex(0,1)*I10511*I16255)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_262 = Coupling(name = 'GC_262',
                  value = '(ee**2*complex(0,1)*I10522*I16255)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_263 = Coupling(name = 'GC_263',
                  value = '(-2*ee**2*complex(0,1)*I10644*I16255)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_264 = Coupling(name = 'GC_264',
                  value = '(-2*ee**2*complex(0,1)*I10655*I16255)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_265 = Coupling(name = 'GC_265',
                  value = '(4*ee**2*complex(0,1)*I17244*I17744)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_266 = Coupling(name = 'GC_266',
                  value = '(4*ee**2*complex(0,1)*I17255*I17755)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_267 = Coupling(name = 'GC_267',
                  value = '(4*ee**2*complex(0,1)*I17644*I17844)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_268 = Coupling(name = 'GC_268',
                  value = '(4*ee**2*complex(0,1)*I17655*I17855)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_269 = Coupling(name = 'GC_269',
                  value = '(cw*ee**2*complex(0,1)*I19711)/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':2})

GC_270 = Coupling(name = 'GC_270',
                  value = '(cw*ee**2*complex(0,1)*I19722)/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':2})

GC_271 = Coupling(name = 'GC_271',
                  value = '(cw*ee**2*complex(0,1)*I19733)/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':2})

GC_272 = Coupling(name = 'GC_272',
                  value = '(cw*ee**2*complex(0,1)*I19736)/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':2})

GC_273 = Coupling(name = 'GC_273',
                  value = '(cw*ee**2*complex(0,1)*I19763)/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':2})

GC_274 = Coupling(name = 'GC_274',
                  value = '(cw*ee**2*complex(0,1)*I19766)/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':2})

GC_275 = Coupling(name = 'GC_275',
                  value = '-((cw*ee**2*complex(0,1)*I19811)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)))',
                  order = {'QED':2})

GC_276 = Coupling(name = 'GC_276',
                  value = '-((cw*ee**2*complex(0,1)*I19822)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)))',
                  order = {'QED':2})

GC_277 = Coupling(name = 'GC_277',
                  value = '-((cw*ee**2*complex(0,1)*I19833)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)))',
                  order = {'QED':2})

GC_278 = Coupling(name = 'GC_278',
                  value = '-((cw*ee**2*complex(0,1)*I19836)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)))',
                  order = {'QED':2})

GC_279 = Coupling(name = 'GC_279',
                  value = '(cw*ee**2*complex(0,1)*I19911)/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':2})

GC_280 = Coupling(name = 'GC_280',
                  value = '(cw*ee**2*complex(0,1)*I19922)/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':2})

GC_281 = Coupling(name = 'GC_281',
                  value = '(cw*ee**2*complex(0,1)*I19933)/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':2})

GC_282 = Coupling(name = 'GC_282',
                  value = '(cw*ee**2*complex(0,1)*I19936)/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':2})

GC_283 = Coupling(name = 'GC_283',
                  value = '(cw*ee**2*complex(0,1)*I19963)/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':2})

GC_284 = Coupling(name = 'GC_284',
                  value = '(cw*ee**2*complex(0,1)*I19966)/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':2})

GC_285 = Coupling(name = 'GC_285',
                  value = '-((cw*ee**2*complex(0,1)*I20011)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)))',
                  order = {'QED':2})

GC_286 = Coupling(name = 'GC_286',
                  value = '-((cw*ee**2*complex(0,1)*I20022)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)))',
                  order = {'QED':2})

GC_287 = Coupling(name = 'GC_287',
                  value = '-((cw*ee**2*complex(0,1)*I20033)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)))',
                  order = {'QED':2})

GC_288 = Coupling(name = 'GC_288',
                  value = '-((cw*ee**2*complex(0,1)*I20036)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)))',
                  order = {'QED':2})

GC_289 = Coupling(name = 'GC_289',
                  value = '(ee**2*complex(0,1)*I2744*I3044)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_290 = Coupling(name = 'GC_290',
                  value = '(ee**2*complex(0,1)*I2755*I3055)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_291 = Coupling(name = 'GC_291',
                  value = '(ee**2*complex(0,1)*I3144*I3244)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_292 = Coupling(name = 'GC_292',
                  value = '(ee**2*complex(0,1)*I3155*I3255)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_293 = Coupling(name = 'GC_293',
                  value = '-(ee**2*complex(0,1)*I6344)/(6.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_294 = Coupling(name = 'GC_294',
                  value = '(ee**2*complex(0,1)*I16111*I6344)/(18.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_295 = Coupling(name = 'GC_295',
                  value = '(ee**2*complex(0,1)*I16122*I6344)/(18.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_296 = Coupling(name = 'GC_296',
                  value = '(-2*ee**2*complex(0,1)*I16244*I6344)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_297 = Coupling(name = 'GC_297',
                  value = '(-2*ee**2*complex(0,1)*I16255*I6344)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_298 = Coupling(name = 'GC_298',
                  value = '-(ee**2*complex(0,1)*I6355)/(6.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_299 = Coupling(name = 'GC_299',
                  value = '(ee**2*complex(0,1)*I16111*I6355)/(18.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_300 = Coupling(name = 'GC_300',
                  value = '(ee**2*complex(0,1)*I16122*I6355)/(18.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_301 = Coupling(name = 'GC_301',
                  value = '(-2*ee**2*complex(0,1)*I16244*I6355)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_302 = Coupling(name = 'GC_302',
                  value = '(-2*ee**2*complex(0,1)*I16255*I6355)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_303 = Coupling(name = 'GC_303',
                  value = '-(ee**2*complex(0,1)*I6344*I6411)/(6.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_304 = Coupling(name = 'GC_304',
                  value = '-(ee**2*complex(0,1)*I6355*I6411)/(6.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_305 = Coupling(name = 'GC_305',
                  value = '-(ee**2*complex(0,1)*I6344*I6422)/(6.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_306 = Coupling(name = 'GC_306',
                  value = '-(ee**2*complex(0,1)*I6355*I6422)/(6.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_307 = Coupling(name = 'GC_307',
                  value = '-(ee**2*complex(0,1)*I16244*I6511)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_308 = Coupling(name = 'GC_308',
                  value = '-(ee**2*complex(0,1)*I16255*I6511)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_309 = Coupling(name = 'GC_309',
                  value = '-(ee**2*complex(0,1)*I16244*I6522)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_310 = Coupling(name = 'GC_310',
                  value = '-(ee**2*complex(0,1)*I16255*I6522)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_311 = Coupling(name = 'GC_311',
                  value = '(ee**2*complex(0,1)*I6344*I6644)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_312 = Coupling(name = 'GC_312',
                  value = '(ee**2*complex(0,1)*I6355*I6644)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_313 = Coupling(name = 'GC_313',
                  value = '(ee**2*complex(0,1)*I6511*I6644)/(6.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_314 = Coupling(name = 'GC_314',
                  value = '(ee**2*complex(0,1)*I6522*I6644)/(6.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_315 = Coupling(name = 'GC_315',
                  value = '(ee**2*complex(0,1)*I6344*I6655)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_316 = Coupling(name = 'GC_316',
                  value = '(ee**2*complex(0,1)*I6355*I6655)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_317 = Coupling(name = 'GC_317',
                  value = '(ee**2*complex(0,1)*I6511*I6655)/(6.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_318 = Coupling(name = 'GC_318',
                  value = '(ee**2*complex(0,1)*I6522*I6655)/(6.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_319 = Coupling(name = 'GC_319',
                  value = '(cw*ee*complex(0,1)*NN11*Rd44*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_320 = Coupling(name = 'GC_320',
                  value = '(cw*ee*complex(0,1)*NN21*Rd44*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_321 = Coupling(name = 'GC_321',
                  value = '(cw*ee*complex(0,1)*NN31*Rd44*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_322 = Coupling(name = 'GC_322',
                  value = '(cw*ee*complex(0,1)*NN41*Rd44*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_323 = Coupling(name = 'GC_323',
                  value = '(cw*ee*complex(0,1)*NN11*Rd55*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_324 = Coupling(name = 'GC_324',
                  value = '(cw*ee*complex(0,1)*NN21*Rd55*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_325 = Coupling(name = 'GC_325',
                  value = '(cw*ee*complex(0,1)*NN31*Rd55*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_326 = Coupling(name = 'GC_326',
                  value = '(cw*ee*complex(0,1)*NN41*Rd55*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_327 = Coupling(name = 'GC_327',
                  value = '(cw*ee*complex(0,1)*NN11*Rl44*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_328 = Coupling(name = 'GC_328',
                  value = '(cw*ee*complex(0,1)*NN21*Rl44*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_329 = Coupling(name = 'GC_329',
                  value = '(cw*ee*complex(0,1)*NN31*Rl44*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_330 = Coupling(name = 'GC_330',
                  value = '(cw*ee*complex(0,1)*NN41*Rl44*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_331 = Coupling(name = 'GC_331',
                  value = '(cw*ee*complex(0,1)*NN11*Rl55*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_332 = Coupling(name = 'GC_332',
                  value = '(cw*ee*complex(0,1)*NN21*Rl55*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_333 = Coupling(name = 'GC_333',
                  value = '(cw*ee*complex(0,1)*NN31*Rl55*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_334 = Coupling(name = 'GC_334',
                  value = '(cw*ee*complex(0,1)*NN41*Rl55*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_335 = Coupling(name = 'GC_335',
                  value = '(-2*cw*ee*complex(0,1)*NN11*Ru44*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_336 = Coupling(name = 'GC_336',
                  value = '(-2*cw*ee*complex(0,1)*NN21*Ru44*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_337 = Coupling(name = 'GC_337',
                  value = '(-2*cw*ee*complex(0,1)*NN31*Ru44*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_338 = Coupling(name = 'GC_338',
                  value = '(-2*cw*ee*complex(0,1)*NN41*Ru44*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_339 = Coupling(name = 'GC_339',
                  value = '(-2*cw*ee*complex(0,1)*NN11*Ru55*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_340 = Coupling(name = 'GC_340',
                  value = '(-2*cw*ee*complex(0,1)*NN21*Ru55*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_341 = Coupling(name = 'GC_341',
                  value = '(-2*cw*ee*complex(0,1)*NN31*Ru55*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_342 = Coupling(name = 'GC_342',
                  value = '(-2*cw*ee*complex(0,1)*NN41*Ru55*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_343 = Coupling(name = 'GC_343',
                  value = '(ee**2*complex(0,1))/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_344 = Coupling(name = 'GC_344',
                  value = '-(ee**2*complex(0,1))/(2.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_345 = Coupling(name = 'GC_345',
                  value = '(ee**2*complex(0,1))/(2.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_346 = Coupling(name = 'GC_346',
                  value = '-(cw*ee*complex(0,1))/(2.*(-1 + sw)*sw*(1 + sw))',
                  order = {'QED':1})

GC_347 = Coupling(name = 'GC_347',
                  value = '(cw*ee*complex(0,1))/(2.*(-1 + sw)*sw*(1 + sw))',
                  order = {'QED':1})

GC_348 = Coupling(name = 'GC_348',
                  value = '-(cw*ee*complex(0,1)*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_349 = Coupling(name = 'GC_349',
                  value = '(2*cw*ee*complex(0,1)*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_350 = Coupling(name = 'GC_350',
                  value = '-((cw*ee*complex(0,1)*sw)/((-1 + sw)*(1 + sw)))',
                  order = {'QED':1})

GC_351 = Coupling(name = 'GC_351',
                  value = '(cw*ee*complex(0,1)*I10644*sw)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_352 = Coupling(name = 'GC_352',
                  value = '(cw*ee*complex(0,1)*I10655*sw)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_353 = Coupling(name = 'GC_353',
                  value = '(8*cw*ee**2*complex(0,1)*I11444*sw)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_354 = Coupling(name = 'GC_354',
                  value = '(4*cw*ee*complex(0,1)*G*I11444*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':1,'QED':1})

GC_355 = Coupling(name = 'GC_355',
                  value = '(8*cw*ee**2*complex(0,1)*I11455*sw)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_356 = Coupling(name = 'GC_356',
                  value = '(4*cw*ee*complex(0,1)*G*I11455*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':1,'QED':1})

GC_357 = Coupling(name = 'GC_357',
                  value = '(-2*cw*ee*complex(0,1)*I20344*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_358 = Coupling(name = 'GC_358',
                  value = '(-2*cw*ee*complex(0,1)*I20355*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_359 = Coupling(name = 'GC_359',
                  value = '(2*cw*ee**2*complex(0,1)*I4844*sw)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_360 = Coupling(name = 'GC_360',
                  value = '(2*cw*ee**2*complex(0,1)*I4855*sw)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_361 = Coupling(name = 'GC_361',
                  value = '(cw*ee*complex(0,1)*I6344*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_362 = Coupling(name = 'GC_362',
                  value = '(cw*ee*complex(0,1)*I6355*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_363 = Coupling(name = 'GC_363',
                  value = '(2*cw*ee**2*complex(0,1)*I644*sw)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_364 = Coupling(name = 'GC_364',
                  value = '(-2*cw*ee*complex(0,1)*G*I644*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':1,'QED':1})

GC_365 = Coupling(name = 'GC_365',
                  value = '(2*cw*ee**2*complex(0,1)*I655*sw)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_366 = Coupling(name = 'GC_366',
                  value = '(-2*cw*ee*complex(0,1)*G*I655*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':1,'QED':1})

GC_367 = Coupling(name = 'GC_367',
                  value = '(-2*ee**2*complex(0,1)*I10644*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_368 = Coupling(name = 'GC_368',
                  value = '(-2*ee**2*complex(0,1)*I10655*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_369 = Coupling(name = 'GC_369',
                  value = '(-8*ee**2*complex(0,1)*I20344*sw**2)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_370 = Coupling(name = 'GC_370',
                  value = '(-8*ee**2*complex(0,1)*I20355*sw**2)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_371 = Coupling(name = 'GC_371',
                  value = '(-2*ee**2*complex(0,1)*I6344*sw**2)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_372 = Coupling(name = 'GC_372',
                  value = '(-2*ee**2*complex(0,1)*I6355*sw**2)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_373 = Coupling(name = 'GC_373',
                  value = '(ee**2*complex(0,1)*I10644*I16133)/(6.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I10644*I16233)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_374 = Coupling(name = 'GC_374',
                  value = '(ee**2*complex(0,1)*I10655*I16133)/(6.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I10655*I16233)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_375 = Coupling(name = 'GC_375',
                  value = '(ee**2*complex(0,1)*I10644*I16136)/(6.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I10644*I16236)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_376 = Coupling(name = 'GC_376',
                  value = '(ee**2*complex(0,1)*I10655*I16136)/(6.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I10655*I16236)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_377 = Coupling(name = 'GC_377',
                  value = '(ee**2*complex(0,1)*I10533*I16244)/(3.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I10633*I16244)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_378 = Coupling(name = 'GC_378',
                  value = '(ee**2*complex(0,1)*I10536*I16244)/(3.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I10636*I16244)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_379 = Coupling(name = 'GC_379',
                  value = '(ee**2*complex(0,1)*I10563*I16244)/(3.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I10663*I16244)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_380 = Coupling(name = 'GC_380',
                  value = '(ee**2*complex(0,1)*I10566*I16244)/(3.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I10666*I16244)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_381 = Coupling(name = 'GC_381',
                  value = '(ee**2*complex(0,1)*I10533*I16255)/(3.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I10633*I16255)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_382 = Coupling(name = 'GC_382',
                  value = '(ee**2*complex(0,1)*I10536*I16255)/(3.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I10636*I16255)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_383 = Coupling(name = 'GC_383',
                  value = '(ee**2*complex(0,1)*I10563*I16255)/(3.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I10663*I16255)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_384 = Coupling(name = 'GC_384',
                  value = '(ee**2*complex(0,1)*I10566*I16255)/(3.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I10666*I16255)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_385 = Coupling(name = 'GC_385',
                  value = '(ee**2*complex(0,1)*I10644*I16163)/(6.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I10644*I16263)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_386 = Coupling(name = 'GC_386',
                  value = '(ee**2*complex(0,1)*I10655*I16163)/(6.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I10655*I16263)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_387 = Coupling(name = 'GC_387',
                  value = '(ee**2*complex(0,1)*I10644*I16166)/(6.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I10644*I16266)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_388 = Coupling(name = 'GC_388',
                  value = '(ee**2*complex(0,1)*I10655*I16166)/(6.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I10655*I16266)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_389 = Coupling(name = 'GC_389',
                  value = '-(ee**2*complex(0,1)*I16911*I17244)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17311*I17444)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I11311*I17544)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17011*I17644)/(36.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_390 = Coupling(name = 'GC_390',
                  value = '-(ee**2*complex(0,1)*I16922*I17244)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17322*I17444)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I11322*I17544)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17022*I17644)/(36.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_391 = Coupling(name = 'GC_391',
                  value = '-(ee**2*complex(0,1)*I16911*I17255)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17311*I17455)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I11311*I17555)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17011*I17655)/(36.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_392 = Coupling(name = 'GC_392',
                  value = '-(ee**2*complex(0,1)*I16922*I17255)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17322*I17455)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I11322*I17555)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17022*I17655)/(36.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_393 = Coupling(name = 'GC_393',
                  value = '-(ee**2*complex(0,1)*I16933*I17244)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17333*I17444)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I11333*I17544)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17033*I17644)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I17244*I17733)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I17233*I17744)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I17644*I17833)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I17633*I17844)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_394 = Coupling(name = 'GC_394',
                  value = '-(ee**2*complex(0,1)*I16936*I17244)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17336*I17444)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I11336*I17544)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17036*I17644)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I17244*I17736)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I17236*I17744)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I17644*I17836)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I17636*I17844)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_395 = Coupling(name = 'GC_395',
                  value = '-(ee**2*complex(0,1)*I16933*I17255)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17333*I17455)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I11333*I17555)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17033*I17655)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I17255*I17733)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I17233*I17755)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I17655*I17833)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I17633*I17855)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_396 = Coupling(name = 'GC_396',
                  value = '-(ee**2*complex(0,1)*I16936*I17255)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17336*I17455)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I11336*I17555)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17036*I17655)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I17255*I17736)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I17236*I17755)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I17655*I17836)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I17636*I17855)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_397 = Coupling(name = 'GC_397',
                  value = '(ee**2*complex(0,1)*I17255*I17744)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I17244*I17755)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I17655*I17844)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I17644*I17855)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_398 = Coupling(name = 'GC_398',
                  value = '-(ee**2*complex(0,1)*I16963*I17244)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17363*I17444)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I11363*I17544)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17063*I17644)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I17263*I17744)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I17244*I17763)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I17663*I17844)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I17644*I17863)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_399 = Coupling(name = 'GC_399',
                  value = '-(ee**2*complex(0,1)*I16963*I17255)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17363*I17455)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I11363*I17555)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17063*I17655)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I17263*I17755)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I17255*I17763)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I17663*I17855)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I17655*I17863)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_400 = Coupling(name = 'GC_400',
                  value = '-(ee**2*complex(0,1)*I16966*I17244)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17366*I17444)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I11366*I17544)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17066*I17644)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I17266*I17744)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I17244*I17766)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I17666*I17844)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I17644*I17866)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_401 = Coupling(name = 'GC_401',
                  value = '-(ee**2*complex(0,1)*I16966*I17255)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17366*I17455)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I11366*I17555)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17066*I17655)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I17266*I17755)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I17255*I17766)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I17666*I17855)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I17655*I17866)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_402 = Coupling(name = 'GC_402',
                  value = '(ee**2*complex(0,1)*I2755*I3044)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2744*I3055)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I3155*I3244)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I3144*I3255)/(36.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_403 = Coupling(name = 'GC_403',
                  value = '(ee**2*complex(0,1)*I2411*I2744)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2811*I2944)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2511*I3244)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I3344*I511)/(72.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_404 = Coupling(name = 'GC_404',
                  value = '(ee**2*complex(0,1)*I2411*I2755)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2811*I2955)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2511*I3255)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I3355*I511)/(72.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_405 = Coupling(name = 'GC_405',
                  value = '(ee**2*complex(0,1)*I2422*I2744)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2822*I2944)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2522*I3244)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I3344*I522)/(72.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_406 = Coupling(name = 'GC_406',
                  value = '(ee**2*complex(0,1)*I2422*I2755)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2822*I2955)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2522*I3255)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I3355*I522)/(72.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_407 = Coupling(name = 'GC_407',
                  value = '(ee**2*complex(0,1)*I2433*I2744)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2833*I2944)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2744*I3033)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2733*I3044)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I3144*I3233)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2533*I3244)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I3133*I3244)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I3344*I533)/(72.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_408 = Coupling(name = 'GC_408',
                  value = '(ee**2*complex(0,1)*I2433*I2755)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2833*I2955)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2755*I3033)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2733*I3055)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I3155*I3233)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2533*I3255)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I3133*I3255)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I3355*I533)/(72.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_409 = Coupling(name = 'GC_409',
                  value = '(ee**2*complex(0,1)*I2436*I2744)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2836*I2944)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2744*I3036)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2736*I3044)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I3144*I3236)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2536*I3244)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I3136*I3244)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I3344*I536)/(72.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_410 = Coupling(name = 'GC_410',
                  value = '(ee**2*complex(0,1)*I2436*I2755)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2836*I2955)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2755*I3036)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2736*I3055)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I3155*I3236)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2536*I3255)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I3136*I3255)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I3355*I536)/(72.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_411 = Coupling(name = 'GC_411',
                  value = '(ee**2*complex(0,1)*I2463*I2744)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2863*I2944)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2763*I3044)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2744*I3063)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2563*I3244)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I3163*I3244)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I3144*I3263)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I3344*I563)/(72.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_412 = Coupling(name = 'GC_412',
                  value = '(ee**2*complex(0,1)*I2463*I2755)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2863*I2955)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2763*I3055)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2755*I3063)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2563*I3255)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I3163*I3255)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I3155*I3263)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I3355*I563)/(72.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_413 = Coupling(name = 'GC_413',
                  value = '(ee**2*complex(0,1)*I2466*I2744)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2866*I2944)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2766*I3044)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2744*I3066)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2566*I3244)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I3166*I3244)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I3144*I3266)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I3344*I566)/(72.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_414 = Coupling(name = 'GC_414',
                  value = '(ee**2*complex(0,1)*I2466*I2755)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2866*I2955)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2766*I3055)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2755*I3066)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2566*I3255)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I3166*I3255)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I3155*I3266)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I3355*I566)/(72.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_415 = Coupling(name = 'GC_415',
                  value = '(ee**2*complex(0,1)*I16133*I6344)/(18.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I16233*I6344)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_416 = Coupling(name = 'GC_416',
                  value = '(ee**2*complex(0,1)*I16136*I6344)/(18.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I16236*I6344)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_417 = Coupling(name = 'GC_417',
                  value = '(ee**2*complex(0,1)*I16163*I6344)/(18.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I16263*I6344)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_418 = Coupling(name = 'GC_418',
                  value = '(ee**2*complex(0,1)*I16166*I6344)/(18.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I16266*I6344)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_419 = Coupling(name = 'GC_419',
                  value = '(ee**2*complex(0,1)*I16133*I6355)/(18.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I16233*I6355)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_420 = Coupling(name = 'GC_420',
                  value = '(ee**2*complex(0,1)*I16136*I6355)/(18.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I16236*I6355)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_421 = Coupling(name = 'GC_421',
                  value = '(ee**2*complex(0,1)*I16163*I6355)/(18.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I16263*I6355)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_422 = Coupling(name = 'GC_422',
                  value = '(ee**2*complex(0,1)*I16166*I6355)/(18.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I16266*I6355)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_423 = Coupling(name = 'GC_423',
                  value = '(-2*ee**2*complex(0,1)*I16244*I6333)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16244*I6533)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_424 = Coupling(name = 'GC_424',
                  value = '(-2*ee**2*complex(0,1)*I16255*I6333)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16255*I6533)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_425 = Coupling(name = 'GC_425',
                  value = '(-2*ee**2*complex(0,1)*I16244*I6336)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16244*I6536)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_426 = Coupling(name = 'GC_426',
                  value = '(-2*ee**2*complex(0,1)*I16255*I6336)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16255*I6536)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_427 = Coupling(name = 'GC_427',
                  value = '(-2*ee**2*complex(0,1)*I16244*I6363)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16244*I6563)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_428 = Coupling(name = 'GC_428',
                  value = '(-2*ee**2*complex(0,1)*I16255*I6363)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16255*I6563)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_429 = Coupling(name = 'GC_429',
                  value = '(-2*ee**2*complex(0,1)*I16244*I6366)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16244*I6566)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_430 = Coupling(name = 'GC_430',
                  value = '(-2*ee**2*complex(0,1)*I16255*I6366)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16255*I6566)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_431 = Coupling(name = 'GC_431',
                  value = '-(ee**2*complex(0,1)*I6344*I6433)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6344*I6633)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_432 = Coupling(name = 'GC_432',
                  value = '-(ee**2*complex(0,1)*I6355*I6433)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6355*I6633)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_433 = Coupling(name = 'GC_433',
                  value = '-(ee**2*complex(0,1)*I6344*I6436)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6344*I6636)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_434 = Coupling(name = 'GC_434',
                  value = '-(ee**2*complex(0,1)*I6355*I6436)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6355*I6636)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_435 = Coupling(name = 'GC_435',
                  value = '(ee**2*complex(0,1)*I6333*I6644)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6533*I6644)/(6.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_436 = Coupling(name = 'GC_436',
                  value = '(ee**2*complex(0,1)*I6336*I6644)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6536*I6644)/(6.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_437 = Coupling(name = 'GC_437',
                  value = '(ee**2*complex(0,1)*I6363*I6644)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6563*I6644)/(6.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_438 = Coupling(name = 'GC_438',
                  value = '(ee**2*complex(0,1)*I6366*I6644)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6566*I6644)/(6.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_439 = Coupling(name = 'GC_439',
                  value = '(ee**2*complex(0,1)*I6333*I6655)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6533*I6655)/(6.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_440 = Coupling(name = 'GC_440',
                  value = '(ee**2*complex(0,1)*I6336*I6655)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6536*I6655)/(6.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_441 = Coupling(name = 'GC_441',
                  value = '(ee**2*complex(0,1)*I6363*I6655)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6563*I6655)/(6.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_442 = Coupling(name = 'GC_442',
                  value = '(ee**2*complex(0,1)*I6366*I6655)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6566*I6655)/(6.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_443 = Coupling(name = 'GC_443',
                  value = '-(ee**2*complex(0,1)*I6344*I6463)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6344*I6663)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_444 = Coupling(name = 'GC_444',
                  value = '-(ee**2*complex(0,1)*I6355*I6463)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6355*I6663)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_445 = Coupling(name = 'GC_445',
                  value = '-(ee**2*complex(0,1)*I6344*I6466)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6344*I6666)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_446 = Coupling(name = 'GC_446',
                  value = '-(ee**2*complex(0,1)*I6355*I6466)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6355*I6666)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_447 = Coupling(name = 'GC_447',
                  value = '-(ee**2*complex(0,1)*I7511*I7644)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I7411*I7744)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I4711*I7844)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I7111*I7944)/(8.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_448 = Coupling(name = 'GC_448',
                  value = '-(ee**2*complex(0,1)*I7522*I7644)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I7422*I7744)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I4722*I7844)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I7122*I7944)/(8.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_449 = Coupling(name = 'GC_449',
                  value = '-(ee**2*complex(0,1)*I7511*I7655)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I7411*I7755)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I4711*I7855)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I7111*I7955)/(8.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_450 = Coupling(name = 'GC_450',
                  value = '-(ee**2*complex(0,1)*I7522*I7655)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I7422*I7755)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I4722*I7855)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I7122*I7955)/(8.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_451 = Coupling(name = 'GC_451',
                  value = '-(ee**2*complex(0,1)*I7533*I7644)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I7433*I7744)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I4733*I7844)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I7133*I7944)/(8.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I7944*I8033)/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I7933*I8044)/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I7744*I8133)/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I7733*I8144)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_452 = Coupling(name = 'GC_452',
                  value = '-(ee**2*complex(0,1)*I7536*I7644)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I7436*I7744)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I4736*I7844)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I7136*I7944)/(8.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I7944*I8036)/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I7936*I8044)/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I7744*I8136)/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I7736*I8144)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_453 = Coupling(name = 'GC_453',
                  value = '(ee**2*complex(0,1)*I7944*I8044)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I7744*I8144)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_454 = Coupling(name = 'GC_454',
                  value = '-(ee**2*complex(0,1)*I7533*I7655)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I7433*I7755)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I4733*I7855)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I7133*I7955)/(8.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I7955*I8033)/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I7933*I8055)/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I7755*I8133)/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I7733*I8155)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_455 = Coupling(name = 'GC_455',
                  value = '-(ee**2*complex(0,1)*I7536*I7655)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I7436*I7755)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I4736*I7855)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I7136*I7955)/(8.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I7955*I8036)/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I7936*I8055)/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I7755*I8136)/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I7736*I8155)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_456 = Coupling(name = 'GC_456',
                  value = '(ee**2*complex(0,1)*I7955*I8044)/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I7944*I8055)/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I7755*I8144)/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I7744*I8155)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_457 = Coupling(name = 'GC_457',
                  value = '(ee**2*complex(0,1)*I7955*I8055)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I7755*I8155)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_458 = Coupling(name = 'GC_458',
                  value = '-(ee**2*complex(0,1)*I7563*I7644)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I7463*I7744)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I4763*I7844)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I7163*I7944)/(8.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I7963*I8044)/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I7944*I8063)/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I7763*I8144)/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I7744*I8163)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_459 = Coupling(name = 'GC_459',
                  value = '-(ee**2*complex(0,1)*I7563*I7655)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I7463*I7755)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I4763*I7855)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I7163*I7955)/(8.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I7963*I8055)/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I7955*I8063)/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I7763*I8155)/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I7755*I8163)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_460 = Coupling(name = 'GC_460',
                  value = '-(ee**2*complex(0,1)*I7566*I7644)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I7466*I7744)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I4766*I7844)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I7166*I7944)/(8.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I7966*I8044)/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I7944*I8066)/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I7766*I8144)/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I7744*I8166)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_461 = Coupling(name = 'GC_461',
                  value = '-(ee**2*complex(0,1)*I7566*I7655)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I7466*I7755)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I4766*I7855)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I7166*I7955)/(8.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I7966*I8055)/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I7955*I8066)/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I7766*I8155)/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I7755*I8166)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_462 = Coupling(name = 'GC_462',
                  value = '(ee**2*complex(0,1)*I10511)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I10511)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_463 = Coupling(name = 'GC_463',
                  value = '(ee**2*complex(0,1)*I10522)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I10522)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_464 = Coupling(name = 'GC_464',
                  value = '(ee**2*complex(0,1)*I10533)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I10633)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I10533)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_465 = Coupling(name = 'GC_465',
                  value = '(ee**2*complex(0,1)*I10536)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I10636)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I10536)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_466 = Coupling(name = 'GC_466',
                  value = '(ee**2*complex(0,1)*I10563)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I10663)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I10563)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_467 = Coupling(name = 'GC_467',
                  value = '(ee**2*complex(0,1)*I10566)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I10666)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I10566)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_468 = Coupling(name = 'GC_468',
                  value = '(ee**2*complex(0,1)*I10511)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I10711*I10811)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I10511)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I10711*I10811)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_469 = Coupling(name = 'GC_469',
                  value = '-(ee**2*complex(0,1)*I10722*I10811)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I10722*I10811)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_470 = Coupling(name = 'GC_470',
                  value = '-(ee**2*complex(0,1)*I10733*I10811)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I10733*I10811)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_471 = Coupling(name = 'GC_471',
                  value = '-(ee**2*complex(0,1)*I10736*I10811)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I10736*I10811)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_472 = Coupling(name = 'GC_472',
                  value = '-(ee**2*complex(0,1)*I10711*I10822)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I10711*I10822)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_473 = Coupling(name = 'GC_473',
                  value = '(ee**2*complex(0,1)*I10522)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I10722*I10822)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I10522)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I10722*I10822)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_474 = Coupling(name = 'GC_474',
                  value = '-(ee**2*complex(0,1)*I10733*I10822)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I10733*I10822)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_475 = Coupling(name = 'GC_475',
                  value = '-(ee**2*complex(0,1)*I10736*I10822)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I10736*I10822)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_476 = Coupling(name = 'GC_476',
                  value = '-(ee**2*complex(0,1)*I10711*I10833)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I10711*I10833)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_477 = Coupling(name = 'GC_477',
                  value = '-(ee**2*complex(0,1)*I10722*I10833)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I10722*I10833)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_478 = Coupling(name = 'GC_478',
                  value = '-(ee**2*complex(0,1)*I10711*I10836)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I10711*I10836)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_479 = Coupling(name = 'GC_479',
                  value = '-(ee**2*complex(0,1)*I10722*I10836)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I10722*I10836)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_480 = Coupling(name = 'GC_480',
                  value = '-(ee**2*complex(0,1)*I14811)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I14811)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_481 = Coupling(name = 'GC_481',
                  value = '-(ee**2*complex(0,1)*I14822)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I14822)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_482 = Coupling(name = 'GC_482',
                  value = '-(ee**2*complex(0,1)*I14833)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I14933)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I14833)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_483 = Coupling(name = 'GC_483',
                  value = '-(ee**2*complex(0,1)*I14836)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I14936)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I14836)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_484 = Coupling(name = 'GC_484',
                  value = '-(ee**2*complex(0,1)*I14863)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I14963)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I14863)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_485 = Coupling(name = 'GC_485',
                  value = '-(ee**2*complex(0,1)*I14866)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I14966)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I14866)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_486 = Coupling(name = 'GC_486',
                  value = '(ee**2*complex(0,1)*I10511*I16111)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I10511*I16111)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_487 = Coupling(name = 'GC_487',
                  value = '(ee**2*complex(0,1)*I10522*I16111)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I10522*I16111)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_488 = Coupling(name = 'GC_488',
                  value = '(ee**2*complex(0,1)*I10533*I16111)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I10633*I16111)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I10533*I16111)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_489 = Coupling(name = 'GC_489',
                  value = '(ee**2*complex(0,1)*I10536*I16111)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I10636*I16111)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I10536*I16111)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_490 = Coupling(name = 'GC_490',
                  value = '(ee**2*complex(0,1)*I10563*I16111)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I10663*I16111)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I10563*I16111)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_491 = Coupling(name = 'GC_491',
                  value = '(ee**2*complex(0,1)*I10566*I16111)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I10666*I16111)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I10566*I16111)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_492 = Coupling(name = 'GC_492',
                  value = '(ee**2*complex(0,1)*I10511*I16122)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I10511*I16122)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_493 = Coupling(name = 'GC_493',
                  value = '(ee**2*complex(0,1)*I10522*I16122)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I10522*I16122)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_494 = Coupling(name = 'GC_494',
                  value = '(ee**2*complex(0,1)*I10533*I16122)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I10633*I16122)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I10533*I16122)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_495 = Coupling(name = 'GC_495',
                  value = '(ee**2*complex(0,1)*I10536*I16122)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I10636*I16122)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I10536*I16122)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_496 = Coupling(name = 'GC_496',
                  value = '(ee**2*complex(0,1)*I10563*I16122)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I10663*I16122)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I10563*I16122)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_497 = Coupling(name = 'GC_497',
                  value = '(ee**2*complex(0,1)*I10566*I16122)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I10666*I16122)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I10566*I16122)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_498 = Coupling(name = 'GC_498',
                  value = '(ee**2*complex(0,1)*I10511*I16133)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I10511*I16233)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I10511*I16133)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_499 = Coupling(name = 'GC_499',
                  value = '(ee**2*complex(0,1)*I10522*I16133)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I10522*I16233)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I10522*I16133)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_500 = Coupling(name = 'GC_500',
                  value = '(ee**2*complex(0,1)*I10533*I16133)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I10633*I16133)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I10533*I16233)/(3.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I10633*I16233)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I10533*I16133)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_501 = Coupling(name = 'GC_501',
                  value = '(ee**2*complex(0,1)*I10536*I16133)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I10636*I16133)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I10536*I16233)/(3.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I10636*I16233)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I10536*I16133)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_502 = Coupling(name = 'GC_502',
                  value = '(ee**2*complex(0,1)*I10563*I16133)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I10663*I16133)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I10563*I16233)/(3.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I10663*I16233)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I10563*I16133)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_503 = Coupling(name = 'GC_503',
                  value = '(ee**2*complex(0,1)*I10566*I16133)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I10666*I16133)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I10566*I16233)/(3.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I10666*I16233)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I10566*I16133)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_504 = Coupling(name = 'GC_504',
                  value = '(ee**2*complex(0,1)*I10511*I16136)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I10511*I16236)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I10511*I16136)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_505 = Coupling(name = 'GC_505',
                  value = '(ee**2*complex(0,1)*I10522*I16136)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I10522*I16236)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I10522*I16136)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_506 = Coupling(name = 'GC_506',
                  value = '(ee**2*complex(0,1)*I10533*I16136)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I10633*I16136)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I10533*I16236)/(3.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I10633*I16236)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I10533*I16136)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_507 = Coupling(name = 'GC_507',
                  value = '(ee**2*complex(0,1)*I10536*I16136)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I10636*I16136)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I10536*I16236)/(3.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I10636*I16236)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I10536*I16136)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_508 = Coupling(name = 'GC_508',
                  value = '(ee**2*complex(0,1)*I10563*I16136)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I10663*I16136)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I10563*I16236)/(3.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I10663*I16236)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I10563*I16136)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_509 = Coupling(name = 'GC_509',
                  value = '(ee**2*complex(0,1)*I10566*I16136)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I10666*I16136)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I10566*I16236)/(3.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I10666*I16236)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I10566*I16136)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_510 = Coupling(name = 'GC_510',
                  value = '(ee**2*complex(0,1)*I10511*I16163)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I10511*I16263)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I10511*I16163)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_511 = Coupling(name = 'GC_511',
                  value = '(ee**2*complex(0,1)*I10522*I16163)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I10522*I16263)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I10522*I16163)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_512 = Coupling(name = 'GC_512',
                  value = '(ee**2*complex(0,1)*I10533*I16163)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I10633*I16163)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I10533*I16263)/(3.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I10633*I16263)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I10533*I16163)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_513 = Coupling(name = 'GC_513',
                  value = '(ee**2*complex(0,1)*I10536*I16163)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I10636*I16163)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I10536*I16263)/(3.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I10636*I16263)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I10536*I16163)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_514 = Coupling(name = 'GC_514',
                  value = '(ee**2*complex(0,1)*I10563*I16163)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I10663*I16163)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I10563*I16263)/(3.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I10663*I16263)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I10563*I16163)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_515 = Coupling(name = 'GC_515',
                  value = '(ee**2*complex(0,1)*I10566*I16163)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I10666*I16163)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I10566*I16263)/(3.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I10666*I16263)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I10566*I16163)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_516 = Coupling(name = 'GC_516',
                  value = '(ee**2*complex(0,1)*I10511*I16166)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I10511*I16266)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I10511*I16166)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_517 = Coupling(name = 'GC_517',
                  value = '(ee**2*complex(0,1)*I10522*I16166)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I10522*I16266)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I10522*I16166)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_518 = Coupling(name = 'GC_518',
                  value = '(ee**2*complex(0,1)*I10533*I16166)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I10633*I16166)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I10533*I16266)/(3.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I10633*I16266)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I10533*I16166)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_519 = Coupling(name = 'GC_519',
                  value = '(ee**2*complex(0,1)*I10536*I16166)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I10636*I16166)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I10536*I16266)/(3.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I10636*I16266)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I10536*I16166)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_520 = Coupling(name = 'GC_520',
                  value = '(ee**2*complex(0,1)*I10563*I16166)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I10663*I16166)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I10563*I16266)/(3.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I10663*I16266)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I10563*I16166)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_521 = Coupling(name = 'GC_521',
                  value = '(ee**2*complex(0,1)*I10566*I16166)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I10666*I16166)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I10566*I16266)/(3.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I10666*I16266)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I10566*I16166)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_522 = Coupling(name = 'GC_522',
                  value = '-(ee**2*complex(0,1)*I15911*I16311)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15911*I16311)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_523 = Coupling(name = 'GC_523',
                  value = '-(ee**2*complex(0,1)*I15922*I16311)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15922*I16311)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_524 = Coupling(name = 'GC_524',
                  value = '-(ee**2*complex(0,1)*I15933*I16311)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15933*I16311)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_525 = Coupling(name = 'GC_525',
                  value = '-(ee**2*complex(0,1)*I15936*I16311)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15936*I16311)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_526 = Coupling(name = 'GC_526',
                  value = '-(ee**2*complex(0,1)*I15963*I16311)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15963*I16311)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_527 = Coupling(name = 'GC_527',
                  value = '-(ee**2*complex(0,1)*I15966*I16311)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15966*I16311)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_528 = Coupling(name = 'GC_528',
                  value = '-(ee**2*complex(0,1)*I15911*I16322)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15911*I16322)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_529 = Coupling(name = 'GC_529',
                  value = '-(ee**2*complex(0,1)*I15922*I16322)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15922*I16322)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_530 = Coupling(name = 'GC_530',
                  value = '-(ee**2*complex(0,1)*I15933*I16322)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15933*I16322)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_531 = Coupling(name = 'GC_531',
                  value = '-(ee**2*complex(0,1)*I15936*I16322)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15936*I16322)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_532 = Coupling(name = 'GC_532',
                  value = '-(ee**2*complex(0,1)*I15963*I16322)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15963*I16322)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_533 = Coupling(name = 'GC_533',
                  value = '-(ee**2*complex(0,1)*I15966*I16322)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15966*I16322)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_534 = Coupling(name = 'GC_534',
                  value = '-(ee**2*complex(0,1)*I15911*I16333)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15911*I16333)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_535 = Coupling(name = 'GC_535',
                  value = '-(ee**2*complex(0,1)*I15922*I16333)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15922*I16333)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_536 = Coupling(name = 'GC_536',
                  value = '-(ee**2*complex(0,1)*I15911*I16336)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15911*I16336)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_537 = Coupling(name = 'GC_537',
                  value = '-(ee**2*complex(0,1)*I15922*I16336)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15922*I16336)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_538 = Coupling(name = 'GC_538',
                  value = '-(ee**2*complex(0,1)*I15911*I16363)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15911*I16363)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_539 = Coupling(name = 'GC_539',
                  value = '-(ee**2*complex(0,1)*I15922*I16363)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15922*I16363)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_540 = Coupling(name = 'GC_540',
                  value = '-(ee**2*complex(0,1)*I15911*I16366)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15911*I16366)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_541 = Coupling(name = 'GC_541',
                  value = '-(ee**2*complex(0,1)*I15922*I16366)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15922*I16366)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_542 = Coupling(name = 'GC_542',
                  value = '(-2*ee**2*complex(0,1)*I16811*I16911)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I16811*I16911)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_543 = Coupling(name = 'GC_543',
                  value = '(-2*ee**2*complex(0,1)*I16822*I16922)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I16822*I16922)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_544 = Coupling(name = 'GC_544',
                  value = '(-2*ee**2*complex(0,1)*I17011*I17111)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I17011*I17111)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_545 = Coupling(name = 'GC_545',
                  value = '-(ee**2*complex(0,1)*I16822*I16911)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16811*I16922)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17022*I17111)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17011*I17122)/(18.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I16822*I16911)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I16811*I16922)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I17022*I17111)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I17011*I17122)/(16.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_546 = Coupling(name = 'GC_546',
                  value = '(-2*ee**2*complex(0,1)*I17022*I17122)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I17022*I17122)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_547 = Coupling(name = 'GC_547',
                  value = '-(ee**2*complex(0,1)*I16833*I16911)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16811*I16933)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17033*I17111)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17011*I17133)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16911*I17233)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17311*I17433)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I11311*I17533)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17011*I17633)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I16833*I16911)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I16811*I16933)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I17033*I17111)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I17011*I17133)/(16.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_548 = Coupling(name = 'GC_548',
                  value = '-(ee**2*complex(0,1)*I16833*I16922)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16822*I16933)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17033*I17122)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17022*I17133)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16922*I17233)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17322*I17433)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I11322*I17533)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17022*I17633)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I16833*I16922)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I16822*I16933)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I17033*I17122)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I17022*I17133)/(16.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_549 = Coupling(name = 'GC_549',
                  value = '-(ee**2*complex(0,1)*I16836*I16911)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16811*I16936)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17036*I17111)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17011*I17136)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16911*I17236)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17311*I17436)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I11311*I17536)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17011*I17636)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I16836*I16911)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I16811*I16936)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I17036*I17111)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I17011*I17136)/(16.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_550 = Coupling(name = 'GC_550',
                  value = '-(ee**2*complex(0,1)*I16836*I16922)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16822*I16936)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17036*I17122)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17022*I17136)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16922*I17236)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17322*I17436)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I11322*I17536)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17022*I17636)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I16836*I16922)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I16822*I16936)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I17036*I17122)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I17022*I17136)/(16.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_551 = Coupling(name = 'GC_551',
                  value = '-(ee**2*complex(0,1)*I16863*I16911)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16811*I16963)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17063*I17111)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17011*I17163)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16911*I17263)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17311*I17463)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I11311*I17563)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17011*I17663)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I16863*I16911)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I16811*I16963)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I17063*I17111)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I17011*I17163)/(16.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_552 = Coupling(name = 'GC_552',
                  value = '-(ee**2*complex(0,1)*I16863*I16922)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16822*I16963)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17063*I17122)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17022*I17163)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16922*I17263)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17322*I17463)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I11322*I17563)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17022*I17663)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I16863*I16922)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I16822*I16963)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I17063*I17122)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I17022*I17163)/(16.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_553 = Coupling(name = 'GC_553',
                  value = '-(ee**2*complex(0,1)*I16866*I16911)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16811*I16966)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17066*I17111)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17011*I17166)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16911*I17266)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17311*I17466)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I11311*I17566)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17011*I17666)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I16866*I16911)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I16811*I16966)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I17066*I17111)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I17011*I17166)/(16.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_554 = Coupling(name = 'GC_554',
                  value = '-(ee**2*complex(0,1)*I16866*I16922)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16822*I16966)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17066*I17122)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17022*I17166)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16922*I17266)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17322*I17466)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I11322*I17566)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17022*I17666)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I16866*I16922)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I16822*I16966)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I17066*I17122)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I17022*I17166)/(16.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_555 = Coupling(name = 'GC_555',
                  value = '(-2*ee**2*complex(0,1)*I2311*I2411)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2311*I2411)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_556 = Coupling(name = 'GC_556',
                  value = '(-2*ee**2*complex(0,1)*I2322*I2422)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2322*I2422)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_557 = Coupling(name = 'GC_557',
                  value = '(-2*ee**2*complex(0,1)*I2511*I2611)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2511*I2611)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_558 = Coupling(name = 'GC_558',
                  value = '-(ee**2*complex(0,1)*I2322*I2411)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I2311*I2422)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I2522*I2611)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I2511*I2622)/(18.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2322*I2411)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I2311*I2422)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I2522*I2611)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I2511*I2622)/(16.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_559 = Coupling(name = 'GC_559',
                  value = '(-2*ee**2*complex(0,1)*I2522*I2622)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2522*I2622)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_560 = Coupling(name = 'GC_560',
                  value = '-(ee**2*complex(0,1)*I2333*I2411)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I2311*I2433)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I2533*I2611)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I2511*I2633)/(18.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2411*I2733)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2811*I2933)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2511*I3233)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I3333*I511)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2333*I2411)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I2311*I2433)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I2533*I2611)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I2511*I2633)/(16.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_561 = Coupling(name = 'GC_561',
                  value = '-(ee**2*complex(0,1)*I2333*I2422)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I2322*I2433)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I2533*I2622)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I2522*I2633)/(18.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2422*I2733)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2822*I2933)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2522*I3233)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I3333*I522)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2333*I2422)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I2322*I2433)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I2533*I2622)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I2522*I2633)/(16.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_562 = Coupling(name = 'GC_562',
                  value = '-(ee**2*complex(0,1)*I2336*I2411)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I2311*I2436)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I2536*I2611)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I2511*I2636)/(18.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2411*I2736)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2811*I2936)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2511*I3236)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I3336*I511)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2336*I2411)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I2311*I2436)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I2536*I2611)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I2511*I2636)/(16.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_563 = Coupling(name = 'GC_563',
                  value = '-(ee**2*complex(0,1)*I2336*I2422)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I2322*I2436)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I2536*I2622)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I2522*I2636)/(18.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2422*I2736)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2822*I2936)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2522*I3236)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I3336*I522)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2336*I2422)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I2322*I2436)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I2536*I2622)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I2522*I2636)/(16.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_564 = Coupling(name = 'GC_564',
                  value = '-(ee**2*complex(0,1)*I2363*I2411)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I2311*I2463)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I2563*I2611)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I2511*I2663)/(18.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2411*I2763)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2811*I2963)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2511*I3263)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I3363*I511)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2363*I2411)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I2311*I2463)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I2563*I2611)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I2511*I2663)/(16.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_565 = Coupling(name = 'GC_565',
                  value = '-(ee**2*complex(0,1)*I2363*I2422)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I2322*I2463)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I2563*I2622)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I2522*I2663)/(18.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2422*I2763)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2822*I2963)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2522*I3263)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I3363*I522)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2363*I2422)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I2322*I2463)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I2563*I2622)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I2522*I2663)/(16.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_566 = Coupling(name = 'GC_566',
                  value = '-(ee**2*complex(0,1)*I2366*I2411)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I2311*I2466)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I2566*I2611)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I2511*I2666)/(18.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2411*I2766)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2811*I2966)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2511*I3266)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I3366*I511)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2366*I2411)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I2311*I2466)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I2566*I2611)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I2511*I2666)/(16.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_567 = Coupling(name = 'GC_567',
                  value = '-(ee**2*complex(0,1)*I2366*I2422)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I2322*I2466)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I2566*I2622)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I2522*I2666)/(18.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2422*I2766)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2822*I2966)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2522*I3266)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I3366*I522)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2366*I2422)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I2322*I2466)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I2566*I2622)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I2522*I2666)/(16.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_568 = Coupling(name = 'GC_568',
                  value = '(ee**2*complex(0,1)*I6511)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I6511)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_569 = Coupling(name = 'GC_569',
                  value = '(5*ee**2*complex(0,1)*I16111*I6511)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16111*I6511)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_570 = Coupling(name = 'GC_570',
                  value = '(5*ee**2*complex(0,1)*I16122*I6511)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16122*I6511)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_571 = Coupling(name = 'GC_571',
                  value = '(5*ee**2*complex(0,1)*I16133*I6511)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16233*I6511)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16133*I6511)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_572 = Coupling(name = 'GC_572',
                  value = '(5*ee**2*complex(0,1)*I16136*I6511)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16236*I6511)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16136*I6511)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_573 = Coupling(name = 'GC_573',
                  value = '(5*ee**2*complex(0,1)*I16163*I6511)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16263*I6511)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16163*I6511)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_574 = Coupling(name = 'GC_574',
                  value = '(5*ee**2*complex(0,1)*I16166*I6511)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16266*I6511)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16166*I6511)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_575 = Coupling(name = 'GC_575',
                  value = '-(ee**2*complex(0,1)*I6411*I6511)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6411*I6511)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_576 = Coupling(name = 'GC_576',
                  value = '-(ee**2*complex(0,1)*I6422*I6511)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6422*I6511)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_577 = Coupling(name = 'GC_577',
                  value = '-(ee**2*complex(0,1)*I6433*I6511)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6511*I6633)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6433*I6511)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_578 = Coupling(name = 'GC_578',
                  value = '-(ee**2*complex(0,1)*I6436*I6511)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6511*I6636)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6436*I6511)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_579 = Coupling(name = 'GC_579',
                  value = '-(ee**2*complex(0,1)*I6463*I6511)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6511*I6663)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6463*I6511)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_580 = Coupling(name = 'GC_580',
                  value = '-(ee**2*complex(0,1)*I6466*I6511)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6511*I6666)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6466*I6511)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_581 = Coupling(name = 'GC_581',
                  value = '(ee**2*complex(0,1)*I6522)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I6522)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_582 = Coupling(name = 'GC_582',
                  value = '(5*ee**2*complex(0,1)*I16111*I6522)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16111*I6522)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_583 = Coupling(name = 'GC_583',
                  value = '(5*ee**2*complex(0,1)*I16122*I6522)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16122*I6522)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_584 = Coupling(name = 'GC_584',
                  value = '(5*ee**2*complex(0,1)*I16133*I6522)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16233*I6522)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16133*I6522)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_585 = Coupling(name = 'GC_585',
                  value = '(5*ee**2*complex(0,1)*I16136*I6522)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16236*I6522)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16136*I6522)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_586 = Coupling(name = 'GC_586',
                  value = '(5*ee**2*complex(0,1)*I16163*I6522)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16263*I6522)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16163*I6522)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_587 = Coupling(name = 'GC_587',
                  value = '(5*ee**2*complex(0,1)*I16166*I6522)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16266*I6522)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16166*I6522)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_588 = Coupling(name = 'GC_588',
                  value = '-(ee**2*complex(0,1)*I6411*I6522)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6411*I6522)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_589 = Coupling(name = 'GC_589',
                  value = '-(ee**2*complex(0,1)*I6422*I6522)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6422*I6522)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_590 = Coupling(name = 'GC_590',
                  value = '-(ee**2*complex(0,1)*I6433*I6522)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6522*I6633)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6433*I6522)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_591 = Coupling(name = 'GC_591',
                  value = '-(ee**2*complex(0,1)*I6436*I6522)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6522*I6636)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6436*I6522)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_592 = Coupling(name = 'GC_592',
                  value = '-(ee**2*complex(0,1)*I6463*I6522)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6522*I6663)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6463*I6522)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_593 = Coupling(name = 'GC_593',
                  value = '-(ee**2*complex(0,1)*I6466*I6522)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6522*I6666)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6466*I6522)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_594 = Coupling(name = 'GC_594',
                  value = '-(ee**2*complex(0,1)*I6333)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6533)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I6533)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_595 = Coupling(name = 'GC_595',
                  value = '(ee**2*complex(0,1)*I16111*I6333)/(18.*(-1 + sw)*(1 + sw)) + (5*ee**2*complex(0,1)*I16111*I6533)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16111*I6533)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_596 = Coupling(name = 'GC_596',
                  value = '(ee**2*complex(0,1)*I16122*I6333)/(18.*(-1 + sw)*(1 + sw)) + (5*ee**2*complex(0,1)*I16122*I6533)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16122*I6533)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_597 = Coupling(name = 'GC_597',
                  value = '(ee**2*complex(0,1)*I16133*I6333)/(18.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I16233*I6333)/(9.*(-1 + sw)*(1 + sw)) + (5*ee**2*complex(0,1)*I16133*I6533)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16233*I6533)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16133*I6533)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_598 = Coupling(name = 'GC_598',
                  value = '(ee**2*complex(0,1)*I16136*I6333)/(18.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I16236*I6333)/(9.*(-1 + sw)*(1 + sw)) + (5*ee**2*complex(0,1)*I16136*I6533)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16236*I6533)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16136*I6533)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_599 = Coupling(name = 'GC_599',
                  value = '(ee**2*complex(0,1)*I16163*I6333)/(18.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I16263*I6333)/(9.*(-1 + sw)*(1 + sw)) + (5*ee**2*complex(0,1)*I16163*I6533)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16263*I6533)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16163*I6533)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_600 = Coupling(name = 'GC_600',
                  value = '(ee**2*complex(0,1)*I16166*I6333)/(18.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I16266*I6333)/(9.*(-1 + sw)*(1 + sw)) + (5*ee**2*complex(0,1)*I16166*I6533)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16266*I6533)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16166*I6533)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_601 = Coupling(name = 'GC_601',
                  value = '-(ee**2*complex(0,1)*I6333*I6411)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I6411*I6533)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6411*I6533)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_602 = Coupling(name = 'GC_602',
                  value = '-(ee**2*complex(0,1)*I6333*I6422)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I6422*I6533)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6422*I6533)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_603 = Coupling(name = 'GC_603',
                  value = '-(ee**2*complex(0,1)*I6336)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6536)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I6536)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_604 = Coupling(name = 'GC_604',
                  value = '(ee**2*complex(0,1)*I16111*I6336)/(18.*(-1 + sw)*(1 + sw)) + (5*ee**2*complex(0,1)*I16111*I6536)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16111*I6536)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_605 = Coupling(name = 'GC_605',
                  value = '(ee**2*complex(0,1)*I16122*I6336)/(18.*(-1 + sw)*(1 + sw)) + (5*ee**2*complex(0,1)*I16122*I6536)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16122*I6536)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_606 = Coupling(name = 'GC_606',
                  value = '(ee**2*complex(0,1)*I16133*I6336)/(18.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I16233*I6336)/(9.*(-1 + sw)*(1 + sw)) + (5*ee**2*complex(0,1)*I16133*I6536)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16233*I6536)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16133*I6536)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_607 = Coupling(name = 'GC_607',
                  value = '(ee**2*complex(0,1)*I16136*I6336)/(18.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I16236*I6336)/(9.*(-1 + sw)*(1 + sw)) + (5*ee**2*complex(0,1)*I16136*I6536)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16236*I6536)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16136*I6536)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_608 = Coupling(name = 'GC_608',
                  value = '(ee**2*complex(0,1)*I16163*I6336)/(18.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I16263*I6336)/(9.*(-1 + sw)*(1 + sw)) + (5*ee**2*complex(0,1)*I16163*I6536)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16263*I6536)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16163*I6536)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_609 = Coupling(name = 'GC_609',
                  value = '(ee**2*complex(0,1)*I16166*I6336)/(18.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I16266*I6336)/(9.*(-1 + sw)*(1 + sw)) + (5*ee**2*complex(0,1)*I16166*I6536)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16266*I6536)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16166*I6536)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_610 = Coupling(name = 'GC_610',
                  value = '-(ee**2*complex(0,1)*I6336*I6411)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I6411*I6536)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6411*I6536)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_611 = Coupling(name = 'GC_611',
                  value = '-(ee**2*complex(0,1)*I6336*I6422)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I6422*I6536)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6422*I6536)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_612 = Coupling(name = 'GC_612',
                  value = '-(ee**2*complex(0,1)*I6363)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6563)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I6563)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_613 = Coupling(name = 'GC_613',
                  value = '(ee**2*complex(0,1)*I16111*I6363)/(18.*(-1 + sw)*(1 + sw)) + (5*ee**2*complex(0,1)*I16111*I6563)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16111*I6563)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_614 = Coupling(name = 'GC_614',
                  value = '(ee**2*complex(0,1)*I16122*I6363)/(18.*(-1 + sw)*(1 + sw)) + (5*ee**2*complex(0,1)*I16122*I6563)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16122*I6563)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_615 = Coupling(name = 'GC_615',
                  value = '(ee**2*complex(0,1)*I16133*I6363)/(18.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I16233*I6363)/(9.*(-1 + sw)*(1 + sw)) + (5*ee**2*complex(0,1)*I16133*I6563)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16233*I6563)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16133*I6563)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_616 = Coupling(name = 'GC_616',
                  value = '(ee**2*complex(0,1)*I16136*I6363)/(18.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I16236*I6363)/(9.*(-1 + sw)*(1 + sw)) + (5*ee**2*complex(0,1)*I16136*I6563)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16236*I6563)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16136*I6563)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_617 = Coupling(name = 'GC_617',
                  value = '(ee**2*complex(0,1)*I16163*I6363)/(18.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I16263*I6363)/(9.*(-1 + sw)*(1 + sw)) + (5*ee**2*complex(0,1)*I16163*I6563)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16263*I6563)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16163*I6563)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_618 = Coupling(name = 'GC_618',
                  value = '(ee**2*complex(0,1)*I16166*I6363)/(18.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I16266*I6363)/(9.*(-1 + sw)*(1 + sw)) + (5*ee**2*complex(0,1)*I16166*I6563)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16266*I6563)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16166*I6563)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_619 = Coupling(name = 'GC_619',
                  value = '-(ee**2*complex(0,1)*I6363*I6411)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I6411*I6563)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6411*I6563)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_620 = Coupling(name = 'GC_620',
                  value = '-(ee**2*complex(0,1)*I6363*I6422)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I6422*I6563)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6422*I6563)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_621 = Coupling(name = 'GC_621',
                  value = '-(ee**2*complex(0,1)*I6366)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6566)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I6566)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_622 = Coupling(name = 'GC_622',
                  value = '(ee**2*complex(0,1)*I16111*I6366)/(18.*(-1 + sw)*(1 + sw)) + (5*ee**2*complex(0,1)*I16111*I6566)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16111*I6566)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_623 = Coupling(name = 'GC_623',
                  value = '(ee**2*complex(0,1)*I16122*I6366)/(18.*(-1 + sw)*(1 + sw)) + (5*ee**2*complex(0,1)*I16122*I6566)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16122*I6566)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_624 = Coupling(name = 'GC_624',
                  value = '(ee**2*complex(0,1)*I16133*I6366)/(18.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I16233*I6366)/(9.*(-1 + sw)*(1 + sw)) + (5*ee**2*complex(0,1)*I16133*I6566)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16233*I6566)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16133*I6566)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_625 = Coupling(name = 'GC_625',
                  value = '(ee**2*complex(0,1)*I16136*I6366)/(18.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I16236*I6366)/(9.*(-1 + sw)*(1 + sw)) + (5*ee**2*complex(0,1)*I16136*I6566)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16236*I6566)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16136*I6566)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_626 = Coupling(name = 'GC_626',
                  value = '(ee**2*complex(0,1)*I16163*I6366)/(18.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I16263*I6366)/(9.*(-1 + sw)*(1 + sw)) + (5*ee**2*complex(0,1)*I16163*I6566)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16263*I6566)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16163*I6566)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_627 = Coupling(name = 'GC_627',
                  value = '(ee**2*complex(0,1)*I16166*I6366)/(18.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I16266*I6366)/(9.*(-1 + sw)*(1 + sw)) + (5*ee**2*complex(0,1)*I16166*I6566)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16266*I6566)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16166*I6566)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_628 = Coupling(name = 'GC_628',
                  value = '-(ee**2*complex(0,1)*I6366*I6411)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I6411*I6566)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6411*I6566)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_629 = Coupling(name = 'GC_629',
                  value = '-(ee**2*complex(0,1)*I6366*I6422)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I6422*I6566)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6422*I6566)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_630 = Coupling(name = 'GC_630',
                  value = '(ee**2*complex(0,1)*I7111*I7211)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I7311*I7411)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_631 = Coupling(name = 'GC_631',
                  value = '(ee**2*complex(0,1)*I7122*I7211)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I7111*I7222)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I7322*I7411)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I7311*I7422)/(16.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_632 = Coupling(name = 'GC_632',
                  value = '(ee**2*complex(0,1)*I7122*I7222)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I7322*I7422)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_633 = Coupling(name = 'GC_633',
                  value = '-(ee**2*complex(0,1)*I7511*I7633)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I7411*I7733)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I4711*I7833)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I7111*I7933)/(8.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I7133*I7211)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I7111*I7233)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I7333*I7411)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I7311*I7433)/(16.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_634 = Coupling(name = 'GC_634',
                  value = '-(ee**2*complex(0,1)*I7522*I7633)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I7422*I7733)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I4722*I7833)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I7122*I7933)/(8.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I7133*I7222)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I7122*I7233)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I7333*I7422)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I7322*I7433)/(16.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_635 = Coupling(name = 'GC_635',
                  value = '-(ee**2*complex(0,1)*I7511*I7636)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I7411*I7736)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I4711*I7836)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I7111*I7936)/(8.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I7136*I7211)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I7111*I7236)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I7336*I7411)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I7311*I7436)/(16.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_636 = Coupling(name = 'GC_636',
                  value = '-(ee**2*complex(0,1)*I7522*I7636)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I7422*I7736)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I4722*I7836)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I7122*I7936)/(8.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I7136*I7222)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I7122*I7236)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I7336*I7422)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I7322*I7436)/(16.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_637 = Coupling(name = 'GC_637',
                  value = '-(ee**2*complex(0,1)*I7511*I7663)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I7411*I7763)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I4711*I7863)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I7111*I7963)/(8.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I7163*I7211)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I7111*I7263)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I7363*I7411)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I7311*I7463)/(16.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_638 = Coupling(name = 'GC_638',
                  value = '-(ee**2*complex(0,1)*I7522*I7663)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I7422*I7763)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I4722*I7863)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I7122*I7963)/(8.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I7163*I7222)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I7122*I7263)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I7363*I7422)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I7322*I7463)/(16.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_639 = Coupling(name = 'GC_639',
                  value = '-(ee**2*complex(0,1)*I7511*I7666)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I7411*I7766)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I4711*I7866)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I7111*I7966)/(8.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I7166*I7211)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I7111*I7266)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I7366*I7411)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I7311*I7466)/(16.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_640 = Coupling(name = 'GC_640',
                  value = '-(ee**2*complex(0,1)*I7522*I7666)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I7422*I7766)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I4722*I7866)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I7122*I7966)/(8.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I7166*I7222)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I7122*I7266)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I7366*I7422)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I7322*I7466)/(16.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_641 = Coupling(name = 'GC_641',
                  value = '-(cw*ee*complex(0,1)*I10511)/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*I10511*sw)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_642 = Coupling(name = 'GC_642',
                  value = '-(cw*ee*complex(0,1)*I10522)/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*I10522*sw)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_643 = Coupling(name = 'GC_643',
                  value = '-(cw*ee*complex(0,1)*I10533)/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*I10533*sw)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*I10633*sw)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_644 = Coupling(name = 'GC_644',
                  value = '-(cw*ee*complex(0,1)*I10536)/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*I10536*sw)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*I10636*sw)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_645 = Coupling(name = 'GC_645',
                  value = '(cw*ee*complex(0,1)*I10563)/(2.*(-1 + sw)*sw*(1 + sw)) - (cw*ee*complex(0,1)*I10563*sw)/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*I10663*sw)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_646 = Coupling(name = 'GC_646',
                  value = '-(cw*ee*complex(0,1)*I10566)/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*I10566*sw)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*I10666*sw)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_647 = Coupling(name = 'GC_647',
                  value = '(-2*cw*ee**2*complex(0,1)*I11311)/(3.*(-1 + sw)*sw*(1 + sw)) + (8*cw*ee**2*complex(0,1)*I11311*sw)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_648 = Coupling(name = 'GC_648',
                  value = '-((cw*ee*complex(0,1)*G*I11311)/((-1 + sw)*sw*(1 + sw))) + (4*cw*ee*complex(0,1)*G*I11311*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':1,'QED':1})

GC_649 = Coupling(name = 'GC_649',
                  value = '(-2*cw*ee**2*complex(0,1)*I11322)/(3.*(-1 + sw)*sw*(1 + sw)) + (8*cw*ee**2*complex(0,1)*I11322*sw)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_650 = Coupling(name = 'GC_650',
                  value = '-((cw*ee*complex(0,1)*G*I11322)/((-1 + sw)*sw*(1 + sw))) + (4*cw*ee*complex(0,1)*G*I11322*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':1,'QED':1})

GC_651 = Coupling(name = 'GC_651',
                  value = '(-2*cw*ee**2*complex(0,1)*I11333)/(3.*(-1 + sw)*sw*(1 + sw)) + (8*cw*ee**2*complex(0,1)*I11333*sw)/(9.*(-1 + sw)*(1 + sw)) + (8*cw*ee**2*complex(0,1)*I11433*sw)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_652 = Coupling(name = 'GC_652',
                  value = '-((cw*ee*complex(0,1)*G*I11333)/((-1 + sw)*sw*(1 + sw))) + (4*cw*ee*complex(0,1)*G*I11333*sw)/(3.*(-1 + sw)*(1 + sw)) + (4*cw*ee*complex(0,1)*G*I11433*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':1,'QED':1})

GC_653 = Coupling(name = 'GC_653',
                  value = '(-2*cw*ee**2*complex(0,1)*I11336)/(3.*(-1 + sw)*sw*(1 + sw)) + (8*cw*ee**2*complex(0,1)*I11336*sw)/(9.*(-1 + sw)*(1 + sw)) + (8*cw*ee**2*complex(0,1)*I11436*sw)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_654 = Coupling(name = 'GC_654',
                  value = '-((cw*ee*complex(0,1)*G*I11336)/((-1 + sw)*sw*(1 + sw))) + (4*cw*ee*complex(0,1)*G*I11336*sw)/(3.*(-1 + sw)*(1 + sw)) + (4*cw*ee*complex(0,1)*G*I11436*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':1,'QED':1})

GC_655 = Coupling(name = 'GC_655',
                  value = '(-2*cw*ee**2*complex(0,1)*I11363)/(3.*(-1 + sw)*sw*(1 + sw)) + (8*cw*ee**2*complex(0,1)*I11363*sw)/(9.*(-1 + sw)*(1 + sw)) + (8*cw*ee**2*complex(0,1)*I11463*sw)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_656 = Coupling(name = 'GC_656',
                  value = '-((cw*ee*complex(0,1)*G*I11363)/((-1 + sw)*sw*(1 + sw))) + (4*cw*ee*complex(0,1)*G*I11363*sw)/(3.*(-1 + sw)*(1 + sw)) + (4*cw*ee*complex(0,1)*G*I11463*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':1,'QED':1})

GC_657 = Coupling(name = 'GC_657',
                  value = '(-2*cw*ee**2*complex(0,1)*I11366)/(3.*(-1 + sw)*sw*(1 + sw)) + (8*cw*ee**2*complex(0,1)*I11366*sw)/(9.*(-1 + sw)*(1 + sw)) + (8*cw*ee**2*complex(0,1)*I11466*sw)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_658 = Coupling(name = 'GC_658',
                  value = '-((cw*ee*complex(0,1)*G*I11366)/((-1 + sw)*sw*(1 + sw))) + (4*cw*ee*complex(0,1)*G*I11366*sw)/(3.*(-1 + sw)*(1 + sw)) + (4*cw*ee*complex(0,1)*G*I11466*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':1,'QED':1})

GC_659 = Coupling(name = 'GC_659',
                  value = '(cw*ee*complex(0,1)*I20111)/(2.*(-1 + sw)*sw*(1 + sw)) - (2*cw*ee*complex(0,1)*I20111*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_660 = Coupling(name = 'GC_660',
                  value = '(cw*ee*complex(0,1)*I20122)/(2.*(-1 + sw)*sw*(1 + sw)) - (2*cw*ee*complex(0,1)*I20122*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_661 = Coupling(name = 'GC_661',
                  value = '(cw*ee*complex(0,1)*I20133)/(2.*(-1 + sw)*sw*(1 + sw)) - (2*cw*ee*complex(0,1)*I20133*sw)/(3.*(-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*I20333*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_662 = Coupling(name = 'GC_662',
                  value = '(cw*ee*complex(0,1)*I20136)/(2.*(-1 + sw)*sw*(1 + sw)) - (2*cw*ee*complex(0,1)*I20136*sw)/(3.*(-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*I20336*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_663 = Coupling(name = 'GC_663',
                  value = '-(cw*ee*complex(0,1)*I20163)/(2.*(-1 + sw)*sw*(1 + sw)) + (2*cw*ee*complex(0,1)*I20163*sw)/(3.*(-1 + sw)*(1 + sw)) + (2*cw*ee*complex(0,1)*I20363*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_664 = Coupling(name = 'GC_664',
                  value = '(cw*ee*complex(0,1)*I20166)/(2.*(-1 + sw)*sw*(1 + sw)) - (2*cw*ee*complex(0,1)*I20166*sw)/(3.*(-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*I20366*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_665 = Coupling(name = 'GC_665',
                  value = '-((cw*ee**2*complex(0,1)*I4711)/((-1 + sw)*sw*(1 + sw))) + (2*cw*ee**2*complex(0,1)*I4711*sw)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_666 = Coupling(name = 'GC_666',
                  value = '-((cw*ee**2*complex(0,1)*I4722)/((-1 + sw)*sw*(1 + sw))) + (2*cw*ee**2*complex(0,1)*I4722*sw)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_667 = Coupling(name = 'GC_667',
                  value = '-((cw*ee**2*complex(0,1)*I4733)/((-1 + sw)*sw*(1 + sw))) + (2*cw*ee**2*complex(0,1)*I4733*sw)/((-1 + sw)*(1 + sw)) + (2*cw*ee**2*complex(0,1)*I4833*sw)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_668 = Coupling(name = 'GC_668',
                  value = '-((cw*ee**2*complex(0,1)*I4736)/((-1 + sw)*sw*(1 + sw))) + (2*cw*ee**2*complex(0,1)*I4736*sw)/((-1 + sw)*(1 + sw)) + (2*cw*ee**2*complex(0,1)*I4836*sw)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_669 = Coupling(name = 'GC_669',
                  value = '-((cw*ee**2*complex(0,1)*I4763)/((-1 + sw)*sw*(1 + sw))) + (2*cw*ee**2*complex(0,1)*I4763*sw)/((-1 + sw)*(1 + sw)) + (2*cw*ee**2*complex(0,1)*I4863*sw)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_670 = Coupling(name = 'GC_670',
                  value = '-((cw*ee**2*complex(0,1)*I4766)/((-1 + sw)*sw*(1 + sw))) + (2*cw*ee**2*complex(0,1)*I4766*sw)/((-1 + sw)*(1 + sw)) + (2*cw*ee**2*complex(0,1)*I4866*sw)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_671 = Coupling(name = 'GC_671',
                  value = '-(cw*ee**2*complex(0,1)*I511)/(3.*(-1 + sw)*sw*(1 + sw)) + (2*cw*ee**2*complex(0,1)*I511*sw)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_672 = Coupling(name = 'GC_672',
                  value = '(cw*ee*complex(0,1)*G*I511)/((-1 + sw)*sw*(1 + sw)) - (2*cw*ee*complex(0,1)*G*I511*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':1,'QED':1})

GC_673 = Coupling(name = 'GC_673',
                  value = '-(cw*ee**2*complex(0,1)*I522)/(3.*(-1 + sw)*sw*(1 + sw)) + (2*cw*ee**2*complex(0,1)*I522*sw)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_674 = Coupling(name = 'GC_674',
                  value = '(cw*ee*complex(0,1)*G*I522)/((-1 + sw)*sw*(1 + sw)) - (2*cw*ee*complex(0,1)*G*I522*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':1,'QED':1})

GC_675 = Coupling(name = 'GC_675',
                  value = '-(cw*ee**2*complex(0,1)*I533)/(3.*(-1 + sw)*sw*(1 + sw)) + (2*cw*ee**2*complex(0,1)*I533*sw)/(9.*(-1 + sw)*(1 + sw)) + (2*cw*ee**2*complex(0,1)*I633*sw)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_676 = Coupling(name = 'GC_676',
                  value = '(cw*ee*complex(0,1)*G*I533)/((-1 + sw)*sw*(1 + sw)) - (2*cw*ee*complex(0,1)*G*I533*sw)/(3.*(-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*G*I633*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':1,'QED':1})

GC_677 = Coupling(name = 'GC_677',
                  value = '-(cw*ee**2*complex(0,1)*I536)/(3.*(-1 + sw)*sw*(1 + sw)) + (2*cw*ee**2*complex(0,1)*I536*sw)/(9.*(-1 + sw)*(1 + sw)) + (2*cw*ee**2*complex(0,1)*I636*sw)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_678 = Coupling(name = 'GC_678',
                  value = '(cw*ee*complex(0,1)*G*I536)/((-1 + sw)*sw*(1 + sw)) - (2*cw*ee*complex(0,1)*G*I536*sw)/(3.*(-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*G*I636*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':1,'QED':1})

GC_679 = Coupling(name = 'GC_679',
                  value = '-(cw*ee*complex(0,1)*I6511)/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*I6511*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_680 = Coupling(name = 'GC_680',
                  value = '-(cw*ee*complex(0,1)*I6522)/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*I6522*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_681 = Coupling(name = 'GC_681',
                  value = '-(cw*ee*complex(0,1)*I6533)/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*I6333*sw)/(3.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*I6533*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_682 = Coupling(name = 'GC_682',
                  value = '-(cw*ee*complex(0,1)*I6536)/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*I6336*sw)/(3.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*I6536*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_683 = Coupling(name = 'GC_683',
                  value = '(cw*ee*complex(0,1)*I6563)/(2.*(-1 + sw)*sw*(1 + sw)) - (cw*ee*complex(0,1)*I6363*sw)/(3.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*I6563*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_684 = Coupling(name = 'GC_684',
                  value = '-(cw*ee*complex(0,1)*I6566)/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*I6366*sw)/(3.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*I6566*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_685 = Coupling(name = 'GC_685',
                  value = '-(cw*ee**2*complex(0,1)*I563)/(3.*(-1 + sw)*sw*(1 + sw)) + (2*cw*ee**2*complex(0,1)*I563*sw)/(9.*(-1 + sw)*(1 + sw)) + (2*cw*ee**2*complex(0,1)*I663*sw)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_686 = Coupling(name = 'GC_686',
                  value = '(cw*ee*complex(0,1)*G*I563)/((-1 + sw)*sw*(1 + sw)) - (2*cw*ee*complex(0,1)*G*I563*sw)/(3.*(-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*G*I663*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':1,'QED':1})

GC_687 = Coupling(name = 'GC_687',
                  value = '-(cw*ee**2*complex(0,1)*I566)/(3.*(-1 + sw)*sw*(1 + sw)) + (2*cw*ee**2*complex(0,1)*I566*sw)/(9.*(-1 + sw)*(1 + sw)) + (2*cw*ee**2*complex(0,1)*I666*sw)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_688 = Coupling(name = 'GC_688',
                  value = '(cw*ee*complex(0,1)*G*I566)/((-1 + sw)*sw*(1 + sw)) - (2*cw*ee*complex(0,1)*G*I566*sw)/(3.*(-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*G*I666*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':1,'QED':1})

GC_689 = Coupling(name = 'GC_689',
                  value = '(2*ee**2*complex(0,1)*I10511)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I10511)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (2*ee**2*complex(0,1)*I10511*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_690 = Coupling(name = 'GC_690',
                  value = '(2*ee**2*complex(0,1)*I10522)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I10522)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (2*ee**2*complex(0,1)*I10522*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_691 = Coupling(name = 'GC_691',
                  value = '(2*ee**2*complex(0,1)*I10533)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I10533)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (2*ee**2*complex(0,1)*I10533*sw**2)/((-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I10633*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_692 = Coupling(name = 'GC_692',
                  value = '(2*ee**2*complex(0,1)*I10536)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I10536)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (2*ee**2*complex(0,1)*I10536*sw**2)/((-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I10636*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_693 = Coupling(name = 'GC_693',
                  value = '(2*ee**2*complex(0,1)*I10563)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I10563)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (2*ee**2*complex(0,1)*I10563*sw**2)/((-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I10663*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_694 = Coupling(name = 'GC_694',
                  value = '(2*ee**2*complex(0,1)*I10566)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I10566)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (2*ee**2*complex(0,1)*I10566*sw**2)/((-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I10666*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_695 = Coupling(name = 'GC_695',
                  value = '(ee**2*complex(0,1)*I10533)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I10633)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I10733*I10833)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I10933*I11033)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I10533)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I10733*I10833)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I10933*I11033*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_696 = Coupling(name = 'GC_696',
                  value = '(ee**2*complex(0,1)*I10563)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I10663)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I10733*I10836)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I10936*I11033)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I10563)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I10733*I10836)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I10936*I11033*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_697 = Coupling(name = 'GC_697',
                  value = '(ee**2*complex(0,1)*I10536)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I10636)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I10736*I10833)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I10933*I11036)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I10536)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I10736*I10833)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I10933*I11036*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_698 = Coupling(name = 'GC_698',
                  value = '(ee**2*complex(0,1)*I10566)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I10666)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I10736*I10836)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I10936*I11036)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I10566)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I10736*I10836)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I10936*I11036*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_699 = Coupling(name = 'GC_699',
                  value = '-(ee**2*complex(0,1)*I15933*I16333)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I16433*I16533)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I16633*I16733)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15933*I16333)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I16433*I16533*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I16633*I16733*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_700 = Coupling(name = 'GC_700',
                  value = '-(ee**2*complex(0,1)*I15933*I16336)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I16433*I16536)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I16636*I16733)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15933*I16336)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I16433*I16536*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I16636*I16733*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_701 = Coupling(name = 'GC_701',
                  value = '-(ee**2*complex(0,1)*I15933*I16363)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I16433*I16563)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I16663*I16733)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15933*I16363)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I16433*I16563*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I16663*I16733*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_702 = Coupling(name = 'GC_702',
                  value = '-(ee**2*complex(0,1)*I15933*I16366)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I16433*I16566)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I16666*I16733)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15933*I16366)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I16433*I16566*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I16666*I16733*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_703 = Coupling(name = 'GC_703',
                  value = '-(ee**2*complex(0,1)*I15936*I16333)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I16436*I16533)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I16633*I16736)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15936*I16333)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I16436*I16533*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I16633*I16736*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_704 = Coupling(name = 'GC_704',
                  value = '-(ee**2*complex(0,1)*I15936*I16336)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I16436*I16536)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I16636*I16736)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15936*I16336)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I16436*I16536*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I16636*I16736*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_705 = Coupling(name = 'GC_705',
                  value = '-(ee**2*complex(0,1)*I15936*I16363)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I16436*I16563)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I16663*I16736)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15936*I16363)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I16436*I16563*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I16663*I16736*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_706 = Coupling(name = 'GC_706',
                  value = '-(ee**2*complex(0,1)*I15936*I16366)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I16436*I16566)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I16666*I16736)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15936*I16366)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I16436*I16566*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I16666*I16736*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_707 = Coupling(name = 'GC_707',
                  value = '-(ee**2*complex(0,1)*I15963*I16333)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I16463*I16533)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I16633*I16763)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15963*I16333)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I16463*I16533*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I16633*I16763*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_708 = Coupling(name = 'GC_708',
                  value = '-(ee**2*complex(0,1)*I15963*I16336)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I16463*I16536)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I16636*I16763)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15963*I16336)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I16463*I16536*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I16636*I16763*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_709 = Coupling(name = 'GC_709',
                  value = '-(ee**2*complex(0,1)*I15963*I16363)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I16463*I16563)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I16663*I16763)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15963*I16363)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I16463*I16563*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I16663*I16763*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_710 = Coupling(name = 'GC_710',
                  value = '-(ee**2*complex(0,1)*I15963*I16366)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I16463*I16566)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I16666*I16763)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15963*I16366)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I16463*I16566*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I16666*I16763*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_711 = Coupling(name = 'GC_711',
                  value = '-(ee**2*complex(0,1)*I15966*I16333)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I16466*I16533)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I16633*I16766)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15966*I16333)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I16466*I16533*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I16633*I16766*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_712 = Coupling(name = 'GC_712',
                  value = '-(ee**2*complex(0,1)*I15966*I16336)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I16466*I16536)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I16636*I16766)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15966*I16336)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I16466*I16536*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I16636*I16766*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_713 = Coupling(name = 'GC_713',
                  value = '-(ee**2*complex(0,1)*I15966*I16363)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I16466*I16563)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I16663*I16766)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15966*I16363)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I16466*I16563*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I16663*I16766*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_714 = Coupling(name = 'GC_714',
                  value = '-(ee**2*complex(0,1)*I15966*I16366)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I16466*I16566)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I16666*I16766)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I15966*I16366)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I16466*I16566*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I16666*I16766*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_715 = Coupling(name = 'GC_715',
                  value = '(complex(0,1)*G**2*I16811*I16911)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16811*I16911*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_716 = Coupling(name = 'GC_716',
                  value = '(complex(0,1)*G**2*I16822*I16922)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16822*I16922*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_717 = Coupling(name = 'GC_717',
                  value = '(complex(0,1)*G**2*I17011*I17111)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17011*I17111*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_718 = Coupling(name = 'GC_718',
                  value = '(complex(0,1)*G**2*I16822*I16911)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16811*I16922)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17022*I17111)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17011*I17122)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16822*I16911*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16811*I16922*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17022*I17111*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17011*I17122*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_719 = Coupling(name = 'GC_719',
                  value = '(complex(0,1)*G**2*I17022*I17122)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17022*I17122*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_720 = Coupling(name = 'GC_720',
                  value = '(complex(0,1)*G**2*I16833*I16911)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16811*I16933)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17033*I17111)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17011*I17133)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16911*I17233)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17311*I17433)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I11311*I17533)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17011*I17633)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16833*I16911*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16811*I16933*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17033*I17111*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17011*I17133*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16911*I17233*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17311*I17433*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I11311*I17533*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17011*I17633*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_721 = Coupling(name = 'GC_721',
                  value = '(complex(0,1)*G**2*I16833*I16922)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16822*I16933)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17033*I17122)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17022*I17133)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16922*I17233)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17322*I17433)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I11322*I17533)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17022*I17633)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16833*I16922*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16822*I16933*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17033*I17122*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17022*I17133*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16922*I17233*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17322*I17433*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I11322*I17533*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17022*I17633*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_722 = Coupling(name = 'GC_722',
                  value = '(complex(0,1)*G**2*I16836*I16911)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16811*I16936)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17036*I17111)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17011*I17136)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16911*I17236)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17311*I17436)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I11311*I17536)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17011*I17636)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16836*I16911*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16811*I16936*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17036*I17111*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17011*I17136*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16911*I17236*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17311*I17436*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I11311*I17536*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17011*I17636*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_723 = Coupling(name = 'GC_723',
                  value = '(complex(0,1)*G**2*I16836*I16922)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16822*I16936)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17036*I17122)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17022*I17136)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16922*I17236)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17322*I17436)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I11322*I17536)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17022*I17636)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16836*I16922*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16822*I16936*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17036*I17122*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17022*I17136*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16922*I17236*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17322*I17436*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I11322*I17536*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17022*I17636*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_724 = Coupling(name = 'GC_724',
                  value = '-(complex(0,1)*G**2*I16911*I17244)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17311*I17444)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I11311*I17544)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17011*I17644)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16911*I17244*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17311*I17444*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I11311*I17544*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17011*I17644*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_725 = Coupling(name = 'GC_725',
                  value = '-(complex(0,1)*G**2*I16922*I17244)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17322*I17444)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I11322*I17544)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17022*I17644)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16922*I17244*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17322*I17444*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I11322*I17544*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17022*I17644*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_726 = Coupling(name = 'GC_726',
                  value = '-(complex(0,1)*G**2*I16911*I17255)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17311*I17455)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I11311*I17555)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17011*I17655)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16911*I17255*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17311*I17455*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I11311*I17555*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17011*I17655*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_727 = Coupling(name = 'GC_727',
                  value = '-(complex(0,1)*G**2*I16922*I17255)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17322*I17455)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I11322*I17555)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17022*I17655)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16922*I17255*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17322*I17455*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I11322*I17555*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17022*I17655*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_728 = Coupling(name = 'GC_728',
                  value = '(complex(0,1)*G**2*I16863*I16911)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16811*I16963)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17063*I17111)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17011*I17163)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16911*I17263)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17311*I17463)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I11311*I17563)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17011*I17663)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16863*I16911*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16811*I16963*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17063*I17111*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17011*I17163*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16911*I17263*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17311*I17463*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I11311*I17563*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17011*I17663*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_729 = Coupling(name = 'GC_729',
                  value = '(complex(0,1)*G**2*I16863*I16922)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16822*I16963)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17063*I17122)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17022*I17163)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16922*I17263)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17322*I17463)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I11322*I17563)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17022*I17663)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16863*I16922*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16822*I16963*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17063*I17122*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17022*I17163*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16922*I17263*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17322*I17463*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I11322*I17563*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17022*I17663*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_730 = Coupling(name = 'GC_730',
                  value = '(complex(0,1)*G**2*I16866*I16911)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16811*I16966)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17066*I17111)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17011*I17166)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16911*I17266)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17311*I17466)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I11311*I17566)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17011*I17666)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16866*I16911*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16811*I16966*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17066*I17111*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17011*I17166*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16911*I17266*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17311*I17466*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I11311*I17566*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17011*I17666*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_731 = Coupling(name = 'GC_731',
                  value = '(complex(0,1)*G**2*I16866*I16922)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16822*I16966)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17066*I17122)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17022*I17166)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16922*I17266)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17322*I17466)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I11322*I17566)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17022*I17666)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16866*I16922*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16822*I16966*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17066*I17122*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17022*I17166*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16922*I17266*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17322*I17466*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I11322*I17566*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17022*I17666*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_732 = Coupling(name = 'GC_732',
                  value = '(complex(0,1)*G**2*I16833*I16933)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16933*I17233)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I11333*I17533)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17233*I17733)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16833*I16933*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16933*I17233*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I11333*I17533*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17233*I17733*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_733 = Coupling(name = 'GC_733',
                  value = '(complex(0,1)*G**2*I16836*I16936)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16936*I17236)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I11336*I17536)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17236*I17736)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16836*I16936*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16936*I17236*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I11336*I17536*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17236*I17736*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_734 = Coupling(name = 'GC_734',
                  value = '(complex(0,1)*G**2*I17244*I17744)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17244*I17744*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_735 = Coupling(name = 'GC_735',
                  value = '(complex(0,1)*G**2*I17255*I17755)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17255*I17755*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_736 = Coupling(name = 'GC_736',
                  value = '(complex(0,1)*G**2*I16863*I16963)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16963*I17263)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I11363*I17563)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17263*I17763)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16863*I16963*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16963*I17263*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I11363*I17563*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17263*I17763*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_737 = Coupling(name = 'GC_737',
                  value = '(complex(0,1)*G**2*I16866*I16966)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16966*I17266)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I11366*I17566)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17266*I17766)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16866*I16966*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16966*I17266*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I11366*I17566*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17266*I17766*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_738 = Coupling(name = 'GC_738',
                  value = '(complex(0,1)*G**2*I17033*I17133)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17333*I17433)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17033*I17633)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17633*I17833)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17033*I17133*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17333*I17433*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17033*I17633*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17633*I17833*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_739 = Coupling(name = 'GC_739',
                  value = '(complex(0,1)*G**2*I16836*I16933)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17033*I17136)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16933*I17236)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17336*I17433)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I11336*I17533)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17033*I17636)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17236*I17733)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17636*I17833)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16836*I16933*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17033*I17136*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16933*I17236*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17336*I17433*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I11336*I17533*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17033*I17636*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17236*I17733*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17636*I17833*sw**2)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_740 = Coupling(name = 'GC_740',
                  value = '(complex(0,1)*G**2*I16833*I16963)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17033*I17163)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16963*I17233)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17363*I17433)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I11333*I17563)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17033*I17663)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17233*I17763)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17663*I17833)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16833*I16963*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17033*I17163*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16963*I17233*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17363*I17433*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I11333*I17563*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17033*I17663*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17233*I17763*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17663*I17833*sw**2)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_741 = Coupling(name = 'GC_741',
                  value = '(complex(0,1)*G**2*I16833*I16936)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17036*I17133)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16936*I17233)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17333*I17436)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I11333*I17536)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17036*I17633)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17233*I17736)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17633*I17836)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16833*I16936*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17036*I17133*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16936*I17233*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17333*I17436*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I11333*I17536*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17036*I17633*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17233*I17736*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17633*I17836*sw**2)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_742 = Coupling(name = 'GC_742',
                  value = '(complex(0,1)*G**2*I17036*I17136)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17336*I17436)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17036*I17636)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17636*I17836)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17036*I17136*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17336*I17436*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17036*I17636*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17636*I17836*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_743 = Coupling(name = 'GC_743',
                  value = '(complex(0,1)*G**2*I16836*I16966)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17036*I17166)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16966*I17236)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17366*I17436)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I11336*I17566)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17036*I17666)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17236*I17766)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17666*I17836)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16836*I16966*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17036*I17166*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16966*I17236*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17366*I17436*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I11336*I17566*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17036*I17666*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17236*I17766*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17666*I17836*sw**2)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_744 = Coupling(name = 'GC_744',
                  value = '-(complex(0,1)*G**2*I16933*I17244)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17333*I17444)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I11333*I17544)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17033*I17644)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17244*I17733)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17233*I17744)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17644*I17833)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17633*I17844)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16933*I17244*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17333*I17444*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I11333*I17544*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17033*I17644*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17244*I17733*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17233*I17744*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17644*I17833*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17633*I17844*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_745 = Coupling(name = 'GC_745',
                  value = '-(complex(0,1)*G**2*I16936*I17244)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17336*I17444)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I11336*I17544)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17036*I17644)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17244*I17736)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17236*I17744)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17644*I17836)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17636*I17844)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16936*I17244*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17336*I17444*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I11336*I17544*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17036*I17644*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17244*I17736*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17236*I17744*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17644*I17836*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17636*I17844*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_746 = Coupling(name = 'GC_746',
                  value = '(complex(0,1)*G**2*I17644*I17844)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17644*I17844*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_747 = Coupling(name = 'GC_747',
                  value = '-(complex(0,1)*G**2*I16933*I17255)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17333*I17455)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I11333*I17555)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17033*I17655)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17255*I17733)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17233*I17755)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17655*I17833)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17633*I17855)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16933*I17255*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17333*I17455*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I11333*I17555*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17033*I17655*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17255*I17733*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17233*I17755*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17655*I17833*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17633*I17855*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_748 = Coupling(name = 'GC_748',
                  value = '-(complex(0,1)*G**2*I16936*I17255)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17336*I17455)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I11336*I17555)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17036*I17655)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17255*I17736)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17236*I17755)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17655*I17836)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17636*I17855)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16936*I17255*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17336*I17455*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I11336*I17555*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17036*I17655*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17255*I17736*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17236*I17755*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17655*I17836*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17636*I17855*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_749 = Coupling(name = 'GC_749',
                  value = '(complex(0,1)*G**2*I17255*I17744)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17244*I17755)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17655*I17844)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17644*I17855)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17255*I17744*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17244*I17755*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17655*I17844*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17644*I17855*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_750 = Coupling(name = 'GC_750',
                  value = '(complex(0,1)*G**2*I17655*I17855)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17655*I17855*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_751 = Coupling(name = 'GC_751',
                  value = '(complex(0,1)*G**2*I16863*I16933)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17063*I17133)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16933*I17263)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17333*I17463)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I11363*I17533)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17063*I17633)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17263*I17733)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17633*I17863)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16863*I16933*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17063*I17133*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16933*I17263*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17333*I17463*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I11363*I17533*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17063*I17633*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17263*I17733*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17633*I17863*sw**2)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_752 = Coupling(name = 'GC_752',
                  value = '(complex(0,1)*G**2*I16863*I16936)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16836*I16963)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17063*I17136)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17036*I17163)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16963*I17236)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16936*I17263)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17363*I17436)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17336*I17463)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I11363*I17536)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I11336*I17563)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17063*I17636)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17036*I17663)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17263*I17736)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17236*I17763)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17663*I17836)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17636*I17863)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16863*I16936*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16836*I16963*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17063*I17136*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17036*I17163*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16963*I17236*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16936*I17263*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17363*I17436*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17336*I17463*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I11363*I17536*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I11336*I17563*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17063*I17636*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17036*I17663*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17263*I17736*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17236*I17763*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17663*I17836*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17636*I17863*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_753 = Coupling(name = 'GC_753',
                  value = '-(complex(0,1)*G**2*I16963*I17244)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17363*I17444)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I11363*I17544)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17063*I17644)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17263*I17744)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17244*I17763)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17663*I17844)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17644*I17863)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16963*I17244*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17363*I17444*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I11363*I17544*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17063*I17644*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17263*I17744*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17244*I17763*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17663*I17844*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17644*I17863*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_754 = Coupling(name = 'GC_754',
                  value = '-(complex(0,1)*G**2*I16963*I17255)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17363*I17455)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I11363*I17555)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17063*I17655)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17263*I17755)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17255*I17763)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17663*I17855)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17655*I17863)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16963*I17255*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17363*I17455*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I11363*I17555*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17063*I17655*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17263*I17755*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17255*I17763*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17663*I17855*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17655*I17863*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_755 = Coupling(name = 'GC_755',
                  value = '(complex(0,1)*G**2*I17063*I17163)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17363*I17463)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17063*I17663)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17663*I17863)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17063*I17163*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17363*I17463*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17063*I17663*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17663*I17863*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_756 = Coupling(name = 'GC_756',
                  value = '(complex(0,1)*G**2*I16866*I16963)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17063*I17166)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16963*I17266)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17366*I17463)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I11366*I17563)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17063*I17666)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17266*I17763)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17666*I17863)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16866*I16963*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17063*I17166*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16963*I17266*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17366*I17463*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I11366*I17563*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17063*I17666*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17266*I17763*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17666*I17863*sw**2)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_757 = Coupling(name = 'GC_757',
                  value = '(complex(0,1)*G**2*I16866*I16933)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16833*I16966)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17066*I17133)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17033*I17166)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16966*I17233)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16933*I17266)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17366*I17433)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17333*I17466)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I11366*I17533)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I11333*I17566)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17066*I17633)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17033*I17666)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17266*I17733)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17233*I17766)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17666*I17833)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17633*I17866)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16866*I16933*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16833*I16966*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17066*I17133*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17033*I17166*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16966*I17233*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16933*I17266*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17366*I17433*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17333*I17466*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I11366*I17533*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I11333*I17566*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17066*I17633*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17033*I17666*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17266*I17733*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17233*I17766*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17666*I17833*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17633*I17866*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_758 = Coupling(name = 'GC_758',
                  value = '(complex(0,1)*G**2*I16866*I16936)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17066*I17136)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16936*I17266)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17336*I17466)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I11366*I17536)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17066*I17636)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17266*I17736)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17636*I17866)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16866*I16936*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17066*I17136*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16936*I17266*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17336*I17466*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I11366*I17536*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17066*I17636*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17266*I17736*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17636*I17866*sw**2)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_759 = Coupling(name = 'GC_759',
                  value = '-(complex(0,1)*G**2*I16966*I17244)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17366*I17444)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I11366*I17544)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17066*I17644)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17266*I17744)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17244*I17766)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17666*I17844)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17644*I17866)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16966*I17244*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17366*I17444*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I11366*I17544*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17066*I17644*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17266*I17744*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17244*I17766*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17666*I17844*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17644*I17866*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_760 = Coupling(name = 'GC_760',
                  value = '-(complex(0,1)*G**2*I16966*I17255)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17366*I17455)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I11366*I17555)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17066*I17655)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17266*I17755)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17255*I17766)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17666*I17855)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17655*I17866)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16966*I17255*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17366*I17455*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I11366*I17555*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17066*I17655*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17266*I17755*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17255*I17766*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17666*I17855*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17655*I17866*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_761 = Coupling(name = 'GC_761',
                  value = '(complex(0,1)*G**2*I16863*I16966)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17066*I17163)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16966*I17263)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17363*I17466)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I11363*I17566)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17066*I17663)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17263*I17766)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17663*I17866)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16863*I16966*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17066*I17163*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16966*I17263*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17363*I17466*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I11363*I17566*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17066*I17663*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17263*I17766*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17663*I17866*sw**2)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_762 = Coupling(name = 'GC_762',
                  value = '(complex(0,1)*G**2*I17066*I17166)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17366*I17466)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17066*I17666)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17666*I17866)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17066*I17166*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17366*I17466*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I17066*I17666*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I17666*I17866*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_763 = Coupling(name = 'GC_763',
                  value = '(-2*ee**2*complex(0,1)*I16833*I16933)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16933*I17233)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I11333*I17533)/(9.*(-1 + sw)*(1 + sw)) + (4*ee**2*complex(0,1)*I17233*I17733)/(9.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I17933*I18033)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I18333*I18433)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I16833*I16933)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I17933*I18033*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I18333*I18433*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_764 = Coupling(name = 'GC_764',
                  value = '(-2*ee**2*complex(0,1)*I16836*I16936)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16936*I17236)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I11336*I17536)/(9.*(-1 + sw)*(1 + sw)) + (4*ee**2*complex(0,1)*I17236*I17736)/(9.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I17936*I18036)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I18336*I18436)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I16836*I16936)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I17936*I18036*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I18336*I18436*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_765 = Coupling(name = 'GC_765',
                  value = '(-2*ee**2*complex(0,1)*I16863*I16963)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16963*I17263)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I11363*I17563)/(9.*(-1 + sw)*(1 + sw)) + (4*ee**2*complex(0,1)*I17263*I17763)/(9.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I17963*I18063)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I18363*I18463)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I16863*I16963)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I17963*I18063*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I18363*I18463*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_766 = Coupling(name = 'GC_766',
                  value = '(-2*ee**2*complex(0,1)*I16866*I16966)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16966*I17266)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I11366*I17566)/(9.*(-1 + sw)*(1 + sw)) + (4*ee**2*complex(0,1)*I17266*I17766)/(9.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I17966*I18066)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I18366*I18466)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I16866*I16966)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I17966*I18066*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I18366*I18466*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_767 = Coupling(name = 'GC_767',
                  value = '(-2*ee**2*complex(0,1)*I17033*I17133)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17333*I17433)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17033*I17633)/(9.*(-1 + sw)*(1 + sw)) + (4*ee**2*complex(0,1)*I17633*I17833)/(9.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I18133*I18233)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I18533*I18633)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I17033*I17133)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I18133*I18233*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I18533*I18633*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_768 = Coupling(name = 'GC_768',
                  value = '-(ee**2*complex(0,1)*I16833*I16936)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17036*I17133)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16936*I17233)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17333*I17436)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I11333*I17536)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17036*I17633)/(18.*(-1 + sw)*(1 + sw)) + (2*ee**2*complex(0,1)*I17233*I17736)/(9.*(-1 + sw)*(1 + sw)) + (2*ee**2*complex(0,1)*I17633*I17836)/(9.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I17936*I18033)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I18133*I18236)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I18333*I18436)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I18536*I18633)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I16833*I16936)/(8.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I17036*I17133)/(8.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I17936*I18033*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I18133*I18236*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I18333*I18436*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I18536*I18633*sw**2)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_769 = Coupling(name = 'GC_769',
                  value = '-(ee**2*complex(0,1)*I16863*I16933)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17063*I17133)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16933*I17263)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17333*I17463)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I11363*I17533)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17063*I17633)/(18.*(-1 + sw)*(1 + sw)) + (2*ee**2*complex(0,1)*I17263*I17733)/(9.*(-1 + sw)*(1 + sw)) + (2*ee**2*complex(0,1)*I17633*I17863)/(9.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I17933*I18063)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I18133*I18263)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I18363*I18433)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I18563*I18633)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I16863*I16933)/(8.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I17063*I17133)/(8.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I17933*I18063*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I18133*I18263*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I18363*I18433*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I18563*I18633*sw**2)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_770 = Coupling(name = 'GC_770',
                  value = '-(ee**2*complex(0,1)*I16836*I16933)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17033*I17136)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16933*I17236)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17336*I17433)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I11336*I17533)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17033*I17636)/(18.*(-1 + sw)*(1 + sw)) + (2*ee**2*complex(0,1)*I17236*I17733)/(9.*(-1 + sw)*(1 + sw)) + (2*ee**2*complex(0,1)*I17636*I17833)/(9.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I17933*I18036)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I18136*I18233)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I18336*I18433)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I18533*I18636)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I16836*I16933)/(8.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I17033*I17136)/(8.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I17933*I18036*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I18136*I18233*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I18336*I18433*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I18533*I18636*sw**2)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_771 = Coupling(name = 'GC_771',
                  value = '(-2*ee**2*complex(0,1)*I17036*I17136)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17336*I17436)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17036*I17636)/(9.*(-1 + sw)*(1 + sw)) + (4*ee**2*complex(0,1)*I17636*I17836)/(9.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I18136*I18236)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I18536*I18636)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I17036*I17136)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I18136*I18236*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I18536*I18636*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_772 = Coupling(name = 'GC_772',
                  value = '-(ee**2*complex(0,1)*I16866*I16936)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17066*I17136)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16936*I17266)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17336*I17466)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I11366*I17536)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17066*I17636)/(18.*(-1 + sw)*(1 + sw)) + (2*ee**2*complex(0,1)*I17266*I17736)/(9.*(-1 + sw)*(1 + sw)) + (2*ee**2*complex(0,1)*I17636*I17866)/(9.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I17936*I18066)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I18136*I18266)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I18366*I18436)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I18566*I18636)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I16866*I16936)/(8.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I17066*I17136)/(8.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I17936*I18066*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I18136*I18266*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I18366*I18436*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I18566*I18636*sw**2)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_773 = Coupling(name = 'GC_773',
                  value = '-(ee**2*complex(0,1)*I16833*I16963)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17033*I17163)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16963*I17233)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17363*I17433)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I11333*I17563)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17033*I17663)/(18.*(-1 + sw)*(1 + sw)) + (2*ee**2*complex(0,1)*I17233*I17763)/(9.*(-1 + sw)*(1 + sw)) + (2*ee**2*complex(0,1)*I17663*I17833)/(9.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I17963*I18033)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I18163*I18233)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I18333*I18463)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I18533*I18663)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I16833*I16963)/(8.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I17033*I17163)/(8.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I17963*I18033*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I18163*I18233*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I18333*I18463*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I18533*I18663*sw**2)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_774 = Coupling(name = 'GC_774',
                  value = '-(ee**2*complex(0,1)*I16863*I16936)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16836*I16963)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17063*I17136)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17036*I17163)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16963*I17236)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16936*I17263)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17363*I17436)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17336*I17463)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I11363*I17536)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I11336*I17563)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17063*I17636)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17036*I17663)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I17263*I17736)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I17236*I17763)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I17663*I17836)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I17636*I17863)/(9.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I17963*I18036)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I17936*I18063)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I18163*I18236)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I18136*I18263)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I18363*I18436)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I18336*I18463)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I18563*I18636)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I18536*I18663)/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I16863*I16936)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I16836*I16963)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I17063*I17136)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I17036*I17163)/(16.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I17963*I18036*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I17936*I18063*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I18163*I18236*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I18136*I18263*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I18363*I18436*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I18336*I18463*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I18563*I18636*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I18536*I18663*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_775 = Coupling(name = 'GC_775',
                  value = '(-2*ee**2*complex(0,1)*I17063*I17163)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17363*I17463)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17063*I17663)/(9.*(-1 + sw)*(1 + sw)) + (4*ee**2*complex(0,1)*I17663*I17863)/(9.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I18163*I18263)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I18563*I18663)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I17063*I17163)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I18163*I18263*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I18563*I18663*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_776 = Coupling(name = 'GC_776',
                  value = '-(ee**2*complex(0,1)*I16863*I16966)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17066*I17163)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16966*I17263)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17363*I17466)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I11363*I17566)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17066*I17663)/(18.*(-1 + sw)*(1 + sw)) + (2*ee**2*complex(0,1)*I17263*I17766)/(9.*(-1 + sw)*(1 + sw)) + (2*ee**2*complex(0,1)*I17663*I17866)/(9.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I17966*I18063)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I18163*I18266)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I18363*I18466)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I18566*I18663)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I16863*I16966)/(8.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I17066*I17163)/(8.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I17966*I18063*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I18163*I18266*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I18363*I18466*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I18566*I18663*sw**2)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_777 = Coupling(name = 'GC_777',
                  value = '-(ee**2*complex(0,1)*I16866*I16933)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16833*I16966)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17066*I17133)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17033*I17166)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16966*I17233)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16933*I17266)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17366*I17433)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17333*I17466)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I11366*I17533)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I11333*I17566)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17066*I17633)/(36.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17033*I17666)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I17266*I17733)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I17233*I17766)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I17666*I17833)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I17633*I17866)/(9.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I17966*I18033)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I17933*I18066)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I18166*I18233)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I18133*I18266)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I18366*I18433)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I18333*I18466)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I18566*I18633)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I18533*I18666)/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I16866*I16933)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I16833*I16966)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I17066*I17133)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I17033*I17166)/(16.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I17966*I18033*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I17933*I18066*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I18166*I18233*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I18133*I18266*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I18366*I18433*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I18333*I18466*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I18566*I18633*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I18533*I18666*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_778 = Coupling(name = 'GC_778',
                  value = '-(ee**2*complex(0,1)*I16836*I16966)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17036*I17166)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16966*I17236)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17366*I17436)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I11336*I17566)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17036*I17666)/(18.*(-1 + sw)*(1 + sw)) + (2*ee**2*complex(0,1)*I17236*I17766)/(9.*(-1 + sw)*(1 + sw)) + (2*ee**2*complex(0,1)*I17666*I17836)/(9.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I17966*I18036)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I18166*I18236)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I18336*I18466)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I18536*I18666)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I16836*I16966)/(8.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I17036*I17166)/(8.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I17966*I18036*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I18166*I18236*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I18336*I18466*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I18536*I18666*sw**2)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_779 = Coupling(name = 'GC_779',
                  value = '-(ee**2*complex(0,1)*I16866*I16963)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17063*I17166)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I16963*I17266)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17366*I17463)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I11366*I17563)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17063*I17666)/(18.*(-1 + sw)*(1 + sw)) + (2*ee**2*complex(0,1)*I17266*I17763)/(9.*(-1 + sw)*(1 + sw)) + (2*ee**2*complex(0,1)*I17666*I17863)/(9.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I17963*I18066)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I18166*I18263)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I18366*I18463)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I18563*I18666)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I16866*I16963)/(8.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I17063*I17166)/(8.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I17963*I18066*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I18166*I18263*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I18366*I18463*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I18563*I18666*sw**2)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_780 = Coupling(name = 'GC_780',
                  value = '(-2*ee**2*complex(0,1)*I17066*I17166)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17366*I17466)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I17066*I17666)/(9.*(-1 + sw)*(1 + sw)) + (4*ee**2*complex(0,1)*I17666*I17866)/(9.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I18166*I18266)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I18566*I18666)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I17066*I17166)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I18166*I18266*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I18566*I18666*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_781 = Coupling(name = 'GC_781',
                  value = '(4*ee**2*complex(0,1)*I20111)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I20111)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (8*ee**2*complex(0,1)*I20111*sw**2)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_782 = Coupling(name = 'GC_782',
                  value = '(4*ee**2*complex(0,1)*I20122)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I20122)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (8*ee**2*complex(0,1)*I20122*sw**2)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_783 = Coupling(name = 'GC_783',
                  value = '(4*ee**2*complex(0,1)*I20133)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I20133)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (8*ee**2*complex(0,1)*I20133*sw**2)/(9.*(-1 + sw)*(1 + sw)) - (8*ee**2*complex(0,1)*I20333*sw**2)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_784 = Coupling(name = 'GC_784',
                  value = '(4*ee**2*complex(0,1)*I20136)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I20136)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (8*ee**2*complex(0,1)*I20136*sw**2)/(9.*(-1 + sw)*(1 + sw)) - (8*ee**2*complex(0,1)*I20336*sw**2)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_785 = Coupling(name = 'GC_785',
                  value = '(4*ee**2*complex(0,1)*I20163)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I20163)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (8*ee**2*complex(0,1)*I20163*sw**2)/(9.*(-1 + sw)*(1 + sw)) - (8*ee**2*complex(0,1)*I20363*sw**2)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_786 = Coupling(name = 'GC_786',
                  value = '(4*ee**2*complex(0,1)*I20166)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I20166)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (8*ee**2*complex(0,1)*I20166*sw**2)/(9.*(-1 + sw)*(1 + sw)) - (8*ee**2*complex(0,1)*I20366*sw**2)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_787 = Coupling(name = 'GC_787',
                  value = '(complex(0,1)*G**2*I2311*I2411)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2311*I2411*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_788 = Coupling(name = 'GC_788',
                  value = '(complex(0,1)*G**2*I2322*I2422)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2322*I2422*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_789 = Coupling(name = 'GC_789',
                  value = '(complex(0,1)*G**2*I2511*I2611)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2511*I2611*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_790 = Coupling(name = 'GC_790',
                  value = '(complex(0,1)*G**2*I2322*I2411)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2311*I2422)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2522*I2611)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2511*I2622)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2322*I2411*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2311*I2422*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2522*I2611*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2511*I2622*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_791 = Coupling(name = 'GC_791',
                  value = '(complex(0,1)*G**2*I2522*I2622)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2522*I2622*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_792 = Coupling(name = 'GC_792',
                  value = '(complex(0,1)*G**2*I2744*I3044)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2744*I3044*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_793 = Coupling(name = 'GC_793',
                  value = '(complex(0,1)*G**2*I2755*I3055)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2755*I3055*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_794 = Coupling(name = 'GC_794',
                  value = '(complex(0,1)*G**2*I2533*I2633)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2833*I2933)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2533*I3233)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I3133*I3233)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2533*I2633*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2833*I2933*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2533*I3233*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I3133*I3233*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_795 = Coupling(name = 'GC_795',
                  value = '(complex(0,1)*G**2*I2536*I2636)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2836*I2936)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2536*I3236)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I3136*I3236)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2536*I2636*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2836*I2936*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2536*I3236*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I3136*I3236*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_796 = Coupling(name = 'GC_796',
                  value = '(complex(0,1)*G**2*I3144*I3244)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I3144*I3244*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_797 = Coupling(name = 'GC_797',
                  value = '(complex(0,1)*G**2*I2755*I3044)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2744*I3055)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I3155*I3244)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I3144*I3255)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2755*I3044*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2744*I3055*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I3155*I3244*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I3144*I3255*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_798 = Coupling(name = 'GC_798',
                  value = '(complex(0,1)*G**2*I3155*I3255)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I3155*I3255*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_799 = Coupling(name = 'GC_799',
                  value = '(complex(0,1)*G**2*I2563*I2663)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2863*I2963)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2563*I3263)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I3163*I3263)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2563*I2663*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2863*I2963*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2563*I3263*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I3163*I3263*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_800 = Coupling(name = 'GC_800',
                  value = '(complex(0,1)*G**2*I2566*I2666)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2866*I2966)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2566*I3266)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I3166*I3266)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2566*I2666*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2866*I2966*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2566*I3266*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I3166*I3266*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_801 = Coupling(name = 'GC_801',
                  value = '(-2*ee**2*complex(0,1)*I2333*I2433)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2433*I2733)/(18.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2733*I3033)/(9.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I3433*I3533)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I3833*I3933)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I3333*I533)/(18.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2333*I2433)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I3433*I3533*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I3833*I3933*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_802 = Coupling(name = 'GC_802',
                  value = '(-2*ee**2*complex(0,1)*I2336*I2436)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2436*I2736)/(18.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2736*I3036)/(9.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I3436*I3536)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I3836*I3936)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I3336*I536)/(18.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2336*I2436)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I3436*I3536*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I3836*I3936*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_803 = Coupling(name = 'GC_803',
                  value = '(-2*ee**2*complex(0,1)*I2363*I2463)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2463*I2763)/(18.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2763*I3063)/(9.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I3463*I3563)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I3863*I3963)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I3363*I563)/(18.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2363*I2463)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I3463*I3563*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I3863*I3963*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_804 = Coupling(name = 'GC_804',
                  value = '(-2*ee**2*complex(0,1)*I2366*I2466)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2466*I2766)/(18.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2766*I3066)/(9.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I3466*I3566)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I3866*I3966)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I3366*I566)/(18.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2366*I2466)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I3466*I3566*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I3866*I3966*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_805 = Coupling(name = 'GC_805',
                  value = '(-2*ee**2*complex(0,1)*I2533*I2633)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2833*I2933)/(18.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2533*I3233)/(18.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I3133*I3233)/(9.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I3633*I3733)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I4033*I4133)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2533*I2633)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I3633*I3733*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I4033*I4133*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_806 = Coupling(name = 'GC_806',
                  value = '-(ee**2*complex(0,1)*I2333*I2436)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I2536*I2633)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2436*I2733)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2833*I2936)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2733*I3036)/(18.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2536*I3233)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I3136*I3233)/(18.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I3436*I3533)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I3633*I3736)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I3833*I3936)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I4036*I4133)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I3336*I533)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2333*I2436)/(8.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I2536*I2633)/(8.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I3436*I3533*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I3633*I3736*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I3833*I3936*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I4036*I4133*sw**2)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_807 = Coupling(name = 'GC_807',
                  value = '-(ee**2*complex(0,1)*I2363*I2433)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I2563*I2633)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2433*I2763)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2833*I2963)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2763*I3033)/(18.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2563*I3233)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I3163*I3233)/(18.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I3433*I3563)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I3633*I3763)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I3863*I3933)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I4063*I4133)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I3333*I563)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2363*I2433)/(8.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I2563*I2633)/(8.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I3433*I3563*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I3633*I3763*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I3863*I3933*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I4063*I4133*sw**2)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_808 = Coupling(name = 'GC_808',
                  value = '-(ee**2*complex(0,1)*I2336*I2433)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I2533*I2636)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2433*I2736)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2836*I2933)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2736*I3033)/(18.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2533*I3236)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I3133*I3236)/(18.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I3433*I3536)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I3636*I3733)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I3836*I3933)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I4033*I4136)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I3333*I536)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2336*I2433)/(8.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I2533*I2636)/(8.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I3433*I3536*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I3636*I3733*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I3836*I3933*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I4033*I4136*sw**2)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_809 = Coupling(name = 'GC_809',
                  value = '(-2*ee**2*complex(0,1)*I2536*I2636)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2836*I2936)/(18.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2536*I3236)/(18.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I3136*I3236)/(9.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I3636*I3736)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I4036*I4136)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2536*I2636)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I3636*I3736*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I4036*I4136*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_810 = Coupling(name = 'GC_810',
                  value = '-(ee**2*complex(0,1)*I2366*I2436)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I2566*I2636)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2436*I2766)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2836*I2966)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2766*I3036)/(18.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2566*I3236)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I3166*I3236)/(18.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I3436*I3566)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I3636*I3766)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I3866*I3936)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I4066*I4136)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I3336*I566)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2366*I2436)/(8.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I2566*I2636)/(8.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I3436*I3566*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I3636*I3766*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I3866*I3936*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I4066*I4136*sw**2)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_811 = Coupling(name = 'GC_811',
                  value = '-(ee**2*complex(0,1)*I2333*I2463)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I2533*I2663)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2463*I2733)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2863*I2933)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2733*I3063)/(18.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2533*I3263)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I3133*I3263)/(18.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I3463*I3533)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I3663*I3733)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I3833*I3963)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I4033*I4163)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I3363*I533)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2333*I2463)/(8.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I2533*I2663)/(8.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I3463*I3533*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I3663*I3733*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I3833*I3963*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I4033*I4163*sw**2)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_812 = Coupling(name = 'GC_812',
                  value = '-(ee**2*complex(0,1)*I2363*I2436)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I2336*I2463)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I2563*I2636)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I2536*I2663)/(18.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2463*I2736)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2436*I2763)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2863*I2936)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2836*I2963)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2763*I3036)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2736*I3063)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2563*I3236)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I3163*I3236)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2536*I3263)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I3136*I3263)/(36.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I3463*I3536)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I3436*I3563)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I3663*I3736)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I3636*I3763)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I3863*I3936)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I3836*I3963)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I4063*I4136)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I4036*I4163)/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I3363*I536)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I3336*I563)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2363*I2436)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I2336*I2463)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I2563*I2636)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I2536*I2663)/(16.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I3463*I3536*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I3436*I3563*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I3663*I3736*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I3636*I3763*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I3863*I3936*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I3836*I3963*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I4063*I4136*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I4036*I4163*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_813 = Coupling(name = 'GC_813',
                  value = '(-2*ee**2*complex(0,1)*I2563*I2663)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2863*I2963)/(18.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2563*I3263)/(18.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I3163*I3263)/(9.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I3663*I3763)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I4063*I4163)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2563*I2663)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I3663*I3763*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I4063*I4163*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_814 = Coupling(name = 'GC_814',
                  value = '-(ee**2*complex(0,1)*I2363*I2466)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I2566*I2663)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2466*I2763)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2863*I2966)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2763*I3066)/(18.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2566*I3263)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I3166*I3263)/(18.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I3466*I3563)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I3663*I3766)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I3863*I3966)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I4066*I4163)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I3366*I563)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2363*I2466)/(8.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I2566*I2663)/(8.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I3466*I3563*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I3663*I3766*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I3863*I3966*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I4066*I4163*sw**2)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_815 = Coupling(name = 'GC_815',
                  value = '-(ee**2*complex(0,1)*I2366*I2433)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I2333*I2466)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I2566*I2633)/(18.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I2533*I2666)/(18.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2466*I2733)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2433*I2766)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2866*I2933)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2833*I2966)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2766*I3033)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2733*I3066)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2566*I3233)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I3166*I3233)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2533*I3266)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I3133*I3266)/(36.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I3466*I3533)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I3433*I3566)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I3666*I3733)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I3633*I3766)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I3866*I3933)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I3833*I3966)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I4066*I4133)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I4033*I4166)/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I3366*I533)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I3333*I566)/(72.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2366*I2433)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I2333*I2466)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I2566*I2633)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I2533*I2666)/(16.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I3466*I3533*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I3433*I3566*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I3666*I3733*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I3633*I3766*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I3866*I3933*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I3833*I3966*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I4066*I4133*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I4033*I4166*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_816 = Coupling(name = 'GC_816',
                  value = '-(ee**2*complex(0,1)*I2336*I2466)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I2536*I2666)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2466*I2736)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2866*I2936)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2736*I3066)/(18.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2536*I3266)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I3136*I3266)/(18.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I3466*I3536)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I3666*I3736)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I3836*I3966)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I4036*I4166)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I3366*I536)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2336*I2466)/(8.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I2536*I2666)/(8.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I3466*I3536*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I3666*I3736*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I3836*I3966*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I4036*I4166*sw**2)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_817 = Coupling(name = 'GC_817',
                  value = '-(ee**2*complex(0,1)*I2366*I2463)/(9.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I2563*I2666)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2463*I2766)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2866*I2963)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2766*I3063)/(18.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2563*I3266)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I3163*I3266)/(18.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I3463*I3566)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I3666*I3763)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I3866*I3963)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I4063*I4166)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I3363*I566)/(36.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2366*I2463)/(8.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I2563*I2666)/(8.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I3463*I3566*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I3666*I3763*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I3866*I3963*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I4063*I4166*sw**2)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_818 = Coupling(name = 'GC_818',
                  value = '(-2*ee**2*complex(0,1)*I2566*I2666)/(9.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2866*I2966)/(18.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2566*I3266)/(18.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I3166*I3266)/(9.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I3666*I3766)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I4066*I4166)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I2566*I2666)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I3666*I3766*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I4066*I4166*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_819 = Coupling(name = 'GC_819',
                  value = '(complex(0,1)*G**2*I2333*I2411)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2311*I2433)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2533*I2611)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2511*I2633)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2411*I2733)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2811*I2933)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2511*I3233)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I3333*I511)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2333*I2411*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2311*I2433*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2533*I2611*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2511*I2633*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2411*I2733*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2811*I2933*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2511*I3233*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I3333*I511*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_820 = Coupling(name = 'GC_820',
                  value = '(complex(0,1)*G**2*I2336*I2411)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2311*I2436)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2536*I2611)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2511*I2636)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2411*I2736)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2811*I2936)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2511*I3236)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I3336*I511)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2336*I2411*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2311*I2436*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2536*I2611*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2511*I2636*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2411*I2736*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2811*I2936*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2511*I3236*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I3336*I511*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_821 = Coupling(name = 'GC_821',
                  value = '-(complex(0,1)*G**2*I2411*I2744)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2811*I2944)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2511*I3244)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I3344*I511)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2411*I2744*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2811*I2944*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2511*I3244*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I3344*I511*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_822 = Coupling(name = 'GC_822',
                  value = '-(complex(0,1)*G**2*I2411*I2755)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2811*I2955)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2511*I3255)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I3355*I511)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2411*I2755*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2811*I2955*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2511*I3255*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I3355*I511*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_823 = Coupling(name = 'GC_823',
                  value = '(complex(0,1)*G**2*I2363*I2411)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2311*I2463)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2563*I2611)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2511*I2663)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2411*I2763)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2811*I2963)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2511*I3263)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I3363*I511)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2363*I2411*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2311*I2463*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2563*I2611*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2511*I2663*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2411*I2763*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2811*I2963*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2511*I3263*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I3363*I511*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_824 = Coupling(name = 'GC_824',
                  value = '(complex(0,1)*G**2*I2366*I2411)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2311*I2466)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2566*I2611)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2511*I2666)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2411*I2766)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2811*I2966)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2511*I3266)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I3366*I511)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2366*I2411*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2311*I2466*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2566*I2611*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2511*I2666*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2411*I2766*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2811*I2966*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2511*I3266*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I3366*I511*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_825 = Coupling(name = 'GC_825',
                  value = '(complex(0,1)*G**2*I2333*I2422)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2322*I2433)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2533*I2622)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2522*I2633)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2422*I2733)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2822*I2933)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2522*I3233)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I3333*I522)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2333*I2422*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2322*I2433*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2533*I2622*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2522*I2633*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2422*I2733*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2822*I2933*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2522*I3233*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I3333*I522*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_826 = Coupling(name = 'GC_826',
                  value = '(complex(0,1)*G**2*I2336*I2422)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2322*I2436)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2536*I2622)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2522*I2636)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2422*I2736)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2822*I2936)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2522*I3236)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I3336*I522)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2336*I2422*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2322*I2436*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2536*I2622*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2522*I2636*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2422*I2736*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2822*I2936*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2522*I3236*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I3336*I522*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_827 = Coupling(name = 'GC_827',
                  value = '-(complex(0,1)*G**2*I2422*I2744)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2822*I2944)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2522*I3244)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I3344*I522)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2422*I2744*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2822*I2944*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2522*I3244*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I3344*I522*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_828 = Coupling(name = 'GC_828',
                  value = '-(complex(0,1)*G**2*I2422*I2755)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2822*I2955)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2522*I3255)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I3355*I522)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2422*I2755*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2822*I2955*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2522*I3255*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I3355*I522*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_829 = Coupling(name = 'GC_829',
                  value = '(complex(0,1)*G**2*I2363*I2422)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2322*I2463)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2563*I2622)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2522*I2663)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2422*I2763)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2822*I2963)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2522*I3263)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I3363*I522)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2363*I2422*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2322*I2463*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2563*I2622*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2522*I2663*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2422*I2763*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2822*I2963*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2522*I3263*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I3363*I522*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_830 = Coupling(name = 'GC_830',
                  value = '(complex(0,1)*G**2*I2366*I2422)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2322*I2466)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2566*I2622)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2522*I2666)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2422*I2766)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2822*I2966)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2522*I3266)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I3366*I522)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2366*I2422*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2322*I2466*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2566*I2622*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2522*I2666*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2422*I2766*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2822*I2966*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2522*I3266*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I3366*I522*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_831 = Coupling(name = 'GC_831',
                  value = '(complex(0,1)*G**2*I2333*I2433)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2433*I2733)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2733*I3033)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I3333*I533)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2333*I2433*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2433*I2733*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2733*I3033*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I3333*I533*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_832 = Coupling(name = 'GC_832',
                  value = '(complex(0,1)*G**2*I2333*I2436)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2536*I2633)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2436*I2733)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2833*I2936)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2733*I3036)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2536*I3233)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I3136*I3233)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I3336*I533)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2333*I2436*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2536*I2633*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2436*I2733*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2833*I2936*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2733*I3036*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2536*I3233*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I3136*I3233*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I3336*I533*sw**2)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_833 = Coupling(name = 'GC_833',
                  value = '-(complex(0,1)*G**2*I2433*I2744)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2833*I2944)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2744*I3033)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2733*I3044)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I3144*I3233)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2533*I3244)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I3133*I3244)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I3344*I533)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2433*I2744*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2833*I2944*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2744*I3033*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2733*I3044*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I3144*I3233*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2533*I3244*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I3133*I3244*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I3344*I533*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_834 = Coupling(name = 'GC_834',
                  value = '-(complex(0,1)*G**2*I2433*I2755)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2833*I2955)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2755*I3033)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2733*I3055)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I3155*I3233)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2533*I3255)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I3133*I3255)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I3355*I533)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2433*I2755*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2833*I2955*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2755*I3033*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2733*I3055*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I3155*I3233*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2533*I3255*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I3133*I3255*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I3355*I533*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_835 = Coupling(name = 'GC_835',
                  value = '(complex(0,1)*G**2*I2333*I2463)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2533*I2663)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2463*I2733)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2863*I2933)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2733*I3063)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2533*I3263)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I3133*I3263)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I3363*I533)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2333*I2463*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2533*I2663*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2463*I2733*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2863*I2933*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2733*I3063*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2533*I3263*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I3133*I3263*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I3363*I533*sw**2)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_836 = Coupling(name = 'GC_836',
                  value = '(complex(0,1)*G**2*I2336*I2433)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2533*I2636)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2433*I2736)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2836*I2933)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2736*I3033)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2533*I3236)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I3133*I3236)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I3333*I536)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2336*I2433*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2533*I2636*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2433*I2736*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2836*I2933*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2736*I3033*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2533*I3236*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I3133*I3236*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I3333*I536*sw**2)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_837 = Coupling(name = 'GC_837',
                  value = '(complex(0,1)*G**2*I2336*I2436)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2436*I2736)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2736*I3036)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I3336*I536)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2336*I2436*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2436*I2736*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2736*I3036*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I3336*I536*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_838 = Coupling(name = 'GC_838',
                  value = '-(complex(0,1)*G**2*I2436*I2744)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2836*I2944)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2744*I3036)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2736*I3044)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I3144*I3236)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2536*I3244)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I3136*I3244)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I3344*I536)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2436*I2744*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2836*I2944*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2744*I3036*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2736*I3044*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I3144*I3236*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2536*I3244*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I3136*I3244*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I3344*I536*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_839 = Coupling(name = 'GC_839',
                  value = '-(complex(0,1)*G**2*I2436*I2755)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2836*I2955)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2755*I3036)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2736*I3055)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I3155*I3236)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2536*I3255)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I3136*I3255)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I3355*I536)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2436*I2755*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2836*I2955*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2755*I3036*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2736*I3055*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I3155*I3236*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2536*I3255*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I3136*I3255*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I3355*I536*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_840 = Coupling(name = 'GC_840',
                  value = '(complex(0,1)*G**2*I2336*I2466)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2536*I2666)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2466*I2736)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2866*I2936)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2736*I3066)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2536*I3266)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I3136*I3266)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I3366*I536)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2336*I2466*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2536*I2666*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2466*I2736*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2866*I2936*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2736*I3066*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2536*I3266*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I3136*I3266*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I3366*I536*sw**2)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_841 = Coupling(name = 'GC_841',
                  value = '(complex(0,1)*G**2*I2363*I2433)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2563*I2633)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2433*I2763)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2833*I2963)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2763*I3033)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2563*I3233)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I3163*I3233)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I3333*I563)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2363*I2433*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2563*I2633*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2433*I2763*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2833*I2963*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2763*I3033*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2563*I3233*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I3163*I3233*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I3333*I563*sw**2)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_842 = Coupling(name = 'GC_842',
                  value = '(complex(0,1)*G**2*I2363*I2436)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2336*I2463)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2563*I2636)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2536*I2663)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2463*I2736)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2436*I2763)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2863*I2936)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2836*I2963)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2763*I3036)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2736*I3063)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2563*I3236)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I3163*I3236)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2536*I3263)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I3136*I3263)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I3363*I536)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I3336*I563)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2363*I2436*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2336*I2463*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2563*I2636*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2536*I2663*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2463*I2736*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2436*I2763*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2863*I2936*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2836*I2963*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2763*I3036*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2736*I3063*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2563*I3236*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I3163*I3236*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2536*I3263*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I3136*I3263*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I3363*I536*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I3336*I563*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_843 = Coupling(name = 'GC_843',
                  value = '-(complex(0,1)*G**2*I2463*I2744)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2863*I2944)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2763*I3044)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2744*I3063)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2563*I3244)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I3163*I3244)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I3144*I3263)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I3344*I563)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2463*I2744*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2863*I2944*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2763*I3044*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2744*I3063*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2563*I3244*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I3163*I3244*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I3144*I3263*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I3344*I563*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_844 = Coupling(name = 'GC_844',
                  value = '-(complex(0,1)*G**2*I2463*I2755)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2863*I2955)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2763*I3055)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2755*I3063)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2563*I3255)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I3163*I3255)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I3155*I3263)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I3355*I563)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2463*I2755*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2863*I2955*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2763*I3055*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2755*I3063*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2563*I3255*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I3163*I3255*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I3155*I3263*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I3355*I563*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_845 = Coupling(name = 'GC_845',
                  value = '(complex(0,1)*G**2*I2363*I2463)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2463*I2763)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2763*I3063)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I3363*I563)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2363*I2463*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2463*I2763*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2763*I3063*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I3363*I563*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_846 = Coupling(name = 'GC_846',
                  value = '(complex(0,1)*G**2*I2363*I2466)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2566*I2663)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2466*I2763)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2863*I2966)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2763*I3066)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2566*I3263)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I3166*I3263)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I3366*I563)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2363*I2466*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2566*I2663*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2466*I2763*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2863*I2966*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2763*I3066*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2566*I3263*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I3166*I3263*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I3366*I563*sw**2)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_847 = Coupling(name = 'GC_847',
                  value = '(complex(0,1)*G**2*I2366*I2433)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2333*I2466)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2566*I2633)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2533*I2666)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2466*I2733)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2433*I2766)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2866*I2933)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2833*I2966)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2766*I3033)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2733*I3066)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2566*I3233)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I3166*I3233)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2533*I3266)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I3133*I3266)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I3366*I533)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I3333*I566)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2366*I2433*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2333*I2466*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2566*I2633*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2533*I2666*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2466*I2733*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2433*I2766*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2866*I2933*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2833*I2966*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2766*I3033*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2733*I3066*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2566*I3233*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I3166*I3233*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2533*I3266*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I3133*I3266*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I3366*I533*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I3333*I566*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_848 = Coupling(name = 'GC_848',
                  value = '(complex(0,1)*G**2*I2366*I2436)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2566*I2636)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2436*I2766)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2836*I2966)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2766*I3036)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2566*I3236)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I3166*I3236)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I3336*I566)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2366*I2436*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2566*I2636*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2436*I2766*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2836*I2966*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2766*I3036*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2566*I3236*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I3166*I3236*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I3336*I566*sw**2)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_849 = Coupling(name = 'GC_849',
                  value = '-(complex(0,1)*G**2*I2466*I2744)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2866*I2944)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2766*I3044)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2744*I3066)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2566*I3244)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I3166*I3244)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I3144*I3266)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I3344*I566)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2466*I2744*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2866*I2944*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2766*I3044*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2744*I3066*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2566*I3244*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I3166*I3244*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I3144*I3266*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I3344*I566*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_850 = Coupling(name = 'GC_850',
                  value = '-(complex(0,1)*G**2*I2466*I2755)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2866*I2955)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2766*I3055)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2755*I3066)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2566*I3255)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I3166*I3255)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I3155*I3266)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I3355*I566)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2466*I2755*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2866*I2955*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2766*I3055*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2755*I3066*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2566*I3255*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I3166*I3255*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I3155*I3266*sw**2)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I3355*I566*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_851 = Coupling(name = 'GC_851',
                  value = '(complex(0,1)*G**2*I2366*I2463)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2563*I2666)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2463*I2766)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2866*I2963)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2766*I3063)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2563*I3266)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I3163*I3266)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I3363*I566)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2366*I2463*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2563*I2666*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2463*I2766*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2866*I2963*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2766*I3063*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2563*I3266*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I3163*I3266*sw**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I3363*I566*sw**2)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_852 = Coupling(name = 'GC_852',
                  value = '(complex(0,1)*G**2*I2366*I2466)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2466*I2766)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2766*I3066)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I3366*I566)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2366*I2466*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I2466*I2766*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I2766*I3066*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I3366*I566*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_853 = Coupling(name = 'GC_853',
                  value = '-((complex(0,1)*G**2*I16111*I6344)/((-1 + sw)*(1 + sw))) + (complex(0,1)*G**2*I16111*I6344*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_854 = Coupling(name = 'GC_854',
                  value = '-((complex(0,1)*G**2*I16122*I6344)/((-1 + sw)*(1 + sw))) + (complex(0,1)*G**2*I16122*I6344*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_855 = Coupling(name = 'GC_855',
                  value = '-((complex(0,1)*G**2*I16133*I6344)/((-1 + sw)*(1 + sw))) + (complex(0,1)*G**2*I16233*I6344)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16133*I6344*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16233*I6344*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_856 = Coupling(name = 'GC_856',
                  value = '-((complex(0,1)*G**2*I16136*I6344)/((-1 + sw)*(1 + sw))) + (complex(0,1)*G**2*I16236*I6344)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16136*I6344*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16236*I6344*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_857 = Coupling(name = 'GC_857',
                  value = '(complex(0,1)*G**2*I16244*I6344)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16244*I6344*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_858 = Coupling(name = 'GC_858',
                  value = '(complex(0,1)*G**2*I16255*I6344)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16255*I6344*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_859 = Coupling(name = 'GC_859',
                  value = '-((complex(0,1)*G**2*I16163*I6344)/((-1 + sw)*(1 + sw))) + (complex(0,1)*G**2*I16263*I6344)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16163*I6344*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16263*I6344*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_860 = Coupling(name = 'GC_860',
                  value = '-((complex(0,1)*G**2*I16166*I6344)/((-1 + sw)*(1 + sw))) + (complex(0,1)*G**2*I16266*I6344)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16166*I6344*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16266*I6344*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_861 = Coupling(name = 'GC_861',
                  value = '-((complex(0,1)*G**2*I16111*I6355)/((-1 + sw)*(1 + sw))) + (complex(0,1)*G**2*I16111*I6355*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_862 = Coupling(name = 'GC_862',
                  value = '-((complex(0,1)*G**2*I16122*I6355)/((-1 + sw)*(1 + sw))) + (complex(0,1)*G**2*I16122*I6355*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_863 = Coupling(name = 'GC_863',
                  value = '-((complex(0,1)*G**2*I16133*I6355)/((-1 + sw)*(1 + sw))) + (complex(0,1)*G**2*I16233*I6355)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16133*I6355*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16233*I6355*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_864 = Coupling(name = 'GC_864',
                  value = '-((complex(0,1)*G**2*I16136*I6355)/((-1 + sw)*(1 + sw))) + (complex(0,1)*G**2*I16236*I6355)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16136*I6355*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16236*I6355*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_865 = Coupling(name = 'GC_865',
                  value = '(complex(0,1)*G**2*I16244*I6355)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16244*I6355*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_866 = Coupling(name = 'GC_866',
                  value = '(complex(0,1)*G**2*I16255*I6355)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16255*I6355*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_867 = Coupling(name = 'GC_867',
                  value = '-((complex(0,1)*G**2*I16163*I6355)/((-1 + sw)*(1 + sw))) + (complex(0,1)*G**2*I16263*I6355)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16163*I6355*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16263*I6355*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_868 = Coupling(name = 'GC_868',
                  value = '-((complex(0,1)*G**2*I16166*I6355)/((-1 + sw)*(1 + sw))) + (complex(0,1)*G**2*I16266*I6355)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16166*I6355*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16266*I6355*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_869 = Coupling(name = 'GC_869',
                  value = '(2*ee**2*complex(0,1)*I6511)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I6511)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (2*ee**2*complex(0,1)*I6511*sw**2)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_870 = Coupling(name = 'GC_870',
                  value = '(complex(0,1)*G**2*I16111*I6511)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16111*I6511*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_871 = Coupling(name = 'GC_871',
                  value = '(complex(0,1)*G**2*I16122*I6511)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16122*I6511*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_872 = Coupling(name = 'GC_872',
                  value = '(complex(0,1)*G**2*I16133*I6511)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16233*I6511)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16133*I6511*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16233*I6511*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_873 = Coupling(name = 'GC_873',
                  value = '(complex(0,1)*G**2*I16136*I6511)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16236*I6511)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16136*I6511*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16236*I6511*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_874 = Coupling(name = 'GC_874',
                  value = '-((complex(0,1)*G**2*I16244*I6511)/((-1 + sw)*(1 + sw))) + (complex(0,1)*G**2*I16244*I6511*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_875 = Coupling(name = 'GC_875',
                  value = '-((complex(0,1)*G**2*I16255*I6511)/((-1 + sw)*(1 + sw))) + (complex(0,1)*G**2*I16255*I6511*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_876 = Coupling(name = 'GC_876',
                  value = '(complex(0,1)*G**2*I16163*I6511)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16263*I6511)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16163*I6511*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16263*I6511*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_877 = Coupling(name = 'GC_877',
                  value = '(complex(0,1)*G**2*I16166*I6511)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16266*I6511)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16166*I6511*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16266*I6511*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_878 = Coupling(name = 'GC_878',
                  value = '(2*ee**2*complex(0,1)*I6522)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I6522)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (2*ee**2*complex(0,1)*I6522*sw**2)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_879 = Coupling(name = 'GC_879',
                  value = '(complex(0,1)*G**2*I16111*I6522)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16111*I6522*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_880 = Coupling(name = 'GC_880',
                  value = '(complex(0,1)*G**2*I16122*I6522)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16122*I6522*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_881 = Coupling(name = 'GC_881',
                  value = '(complex(0,1)*G**2*I16133*I6522)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16233*I6522)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16133*I6522*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16233*I6522*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_882 = Coupling(name = 'GC_882',
                  value = '(complex(0,1)*G**2*I16136*I6522)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16236*I6522)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16136*I6522*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16236*I6522*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_883 = Coupling(name = 'GC_883',
                  value = '-((complex(0,1)*G**2*I16244*I6522)/((-1 + sw)*(1 + sw))) + (complex(0,1)*G**2*I16244*I6522*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_884 = Coupling(name = 'GC_884',
                  value = '-((complex(0,1)*G**2*I16255*I6522)/((-1 + sw)*(1 + sw))) + (complex(0,1)*G**2*I16255*I6522*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_885 = Coupling(name = 'GC_885',
                  value = '(complex(0,1)*G**2*I16163*I6522)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16263*I6522)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16163*I6522*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16263*I6522*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_886 = Coupling(name = 'GC_886',
                  value = '(complex(0,1)*G**2*I16166*I6522)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16266*I6522)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16166*I6522*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16266*I6522*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_887 = Coupling(name = 'GC_887',
                  value = '(2*ee**2*complex(0,1)*I6533)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I6533)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (2*ee**2*complex(0,1)*I6333*sw**2)/(9.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I6533*sw**2)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_888 = Coupling(name = 'GC_888',
                  value = '-((complex(0,1)*G**2*I16111*I6333)/((-1 + sw)*(1 + sw))) + (complex(0,1)*G**2*I16111*I6533)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16111*I6333*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16111*I6533*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_889 = Coupling(name = 'GC_889',
                  value = '-((complex(0,1)*G**2*I16122*I6333)/((-1 + sw)*(1 + sw))) + (complex(0,1)*G**2*I16122*I6533)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16122*I6333*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16122*I6533*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_890 = Coupling(name = 'GC_890',
                  value = '-((complex(0,1)*G**2*I16133*I6333)/((-1 + sw)*(1 + sw))) + (complex(0,1)*G**2*I16233*I6333)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16133*I6533)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16233*I6533)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16133*I6333*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16233*I6333*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16133*I6533*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16233*I6533*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_891 = Coupling(name = 'GC_891',
                  value = '-((complex(0,1)*G**2*I16136*I6333)/((-1 + sw)*(1 + sw))) + (complex(0,1)*G**2*I16236*I6333)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16136*I6533)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16236*I6533)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16136*I6333*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16236*I6333*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16136*I6533*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16236*I6533*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_892 = Coupling(name = 'GC_892',
                  value = '(complex(0,1)*G**2*I16244*I6333)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16244*I6533)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16244*I6333*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16244*I6533*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_893 = Coupling(name = 'GC_893',
                  value = '(complex(0,1)*G**2*I16255*I6333)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16255*I6533)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16255*I6333*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16255*I6533*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_894 = Coupling(name = 'GC_894',
                  value = '-((complex(0,1)*G**2*I16163*I6333)/((-1 + sw)*(1 + sw))) + (complex(0,1)*G**2*I16263*I6333)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16163*I6533)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16263*I6533)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16163*I6333*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16263*I6333*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16163*I6533*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16263*I6533*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_895 = Coupling(name = 'GC_895',
                  value = '-((complex(0,1)*G**2*I16166*I6333)/((-1 + sw)*(1 + sw))) + (complex(0,1)*G**2*I16266*I6333)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16166*I6533)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16266*I6533)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16166*I6333*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16266*I6333*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16166*I6533*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16266*I6533*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_896 = Coupling(name = 'GC_896',
                  value = '(2*ee**2*complex(0,1)*I6536)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I6536)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (2*ee**2*complex(0,1)*I6336*sw**2)/(9.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I6536*sw**2)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_897 = Coupling(name = 'GC_897',
                  value = '-((complex(0,1)*G**2*I16111*I6336)/((-1 + sw)*(1 + sw))) + (complex(0,1)*G**2*I16111*I6536)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16111*I6336*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16111*I6536*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_898 = Coupling(name = 'GC_898',
                  value = '-((complex(0,1)*G**2*I16122*I6336)/((-1 + sw)*(1 + sw))) + (complex(0,1)*G**2*I16122*I6536)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16122*I6336*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16122*I6536*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_899 = Coupling(name = 'GC_899',
                  value = '-((complex(0,1)*G**2*I16133*I6336)/((-1 + sw)*(1 + sw))) + (complex(0,1)*G**2*I16233*I6336)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16133*I6536)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16233*I6536)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16133*I6336*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16233*I6336*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16133*I6536*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16233*I6536*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_900 = Coupling(name = 'GC_900',
                  value = '-((complex(0,1)*G**2*I16136*I6336)/((-1 + sw)*(1 + sw))) + (complex(0,1)*G**2*I16236*I6336)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16136*I6536)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16236*I6536)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16136*I6336*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16236*I6336*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16136*I6536*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16236*I6536*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_901 = Coupling(name = 'GC_901',
                  value = '(complex(0,1)*G**2*I16244*I6336)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16244*I6536)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16244*I6336*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16244*I6536*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_902 = Coupling(name = 'GC_902',
                  value = '(complex(0,1)*G**2*I16255*I6336)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16255*I6536)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16255*I6336*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16255*I6536*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_903 = Coupling(name = 'GC_903',
                  value = '-((complex(0,1)*G**2*I16163*I6336)/((-1 + sw)*(1 + sw))) + (complex(0,1)*G**2*I16263*I6336)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16163*I6536)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16263*I6536)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16163*I6336*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16263*I6336*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16163*I6536*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16263*I6536*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_904 = Coupling(name = 'GC_904',
                  value = '-((complex(0,1)*G**2*I16166*I6336)/((-1 + sw)*(1 + sw))) + (complex(0,1)*G**2*I16266*I6336)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16166*I6536)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16266*I6536)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16166*I6336*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16266*I6336*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16166*I6536*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16266*I6536*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_905 = Coupling(name = 'GC_905',
                  value = '(2*ee**2*complex(0,1)*I6563)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I6563)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (2*ee**2*complex(0,1)*I6363*sw**2)/(9.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I6563*sw**2)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_906 = Coupling(name = 'GC_906',
                  value = '-((complex(0,1)*G**2*I16111*I6363)/((-1 + sw)*(1 + sw))) + (complex(0,1)*G**2*I16111*I6563)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16111*I6363*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16111*I6563*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_907 = Coupling(name = 'GC_907',
                  value = '-((complex(0,1)*G**2*I16122*I6363)/((-1 + sw)*(1 + sw))) + (complex(0,1)*G**2*I16122*I6563)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16122*I6363*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16122*I6563*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_908 = Coupling(name = 'GC_908',
                  value = '-((complex(0,1)*G**2*I16133*I6363)/((-1 + sw)*(1 + sw))) + (complex(0,1)*G**2*I16233*I6363)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16133*I6563)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16233*I6563)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16133*I6363*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16233*I6363*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16133*I6563*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16233*I6563*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_909 = Coupling(name = 'GC_909',
                  value = '-((complex(0,1)*G**2*I16136*I6363)/((-1 + sw)*(1 + sw))) + (complex(0,1)*G**2*I16236*I6363)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16136*I6563)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16236*I6563)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16136*I6363*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16236*I6363*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16136*I6563*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16236*I6563*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_910 = Coupling(name = 'GC_910',
                  value = '(complex(0,1)*G**2*I16244*I6363)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16244*I6563)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16244*I6363*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16244*I6563*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_911 = Coupling(name = 'GC_911',
                  value = '(complex(0,1)*G**2*I16255*I6363)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16255*I6563)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16255*I6363*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16255*I6563*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_912 = Coupling(name = 'GC_912',
                  value = '-((complex(0,1)*G**2*I16163*I6363)/((-1 + sw)*(1 + sw))) + (complex(0,1)*G**2*I16263*I6363)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16163*I6563)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16263*I6563)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16163*I6363*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16263*I6363*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16163*I6563*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16263*I6563*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_913 = Coupling(name = 'GC_913',
                  value = '-((complex(0,1)*G**2*I16166*I6363)/((-1 + sw)*(1 + sw))) + (complex(0,1)*G**2*I16266*I6363)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16166*I6563)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16266*I6563)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16166*I6363*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16266*I6363*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16166*I6563*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16266*I6563*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_914 = Coupling(name = 'GC_914',
                  value = '(2*ee**2*complex(0,1)*I6566)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I6566)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (2*ee**2*complex(0,1)*I6366*sw**2)/(9.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I6566*sw**2)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_915 = Coupling(name = 'GC_915',
                  value = '-((complex(0,1)*G**2*I16111*I6366)/((-1 + sw)*(1 + sw))) + (complex(0,1)*G**2*I16111*I6566)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16111*I6366*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16111*I6566*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_916 = Coupling(name = 'GC_916',
                  value = '-((complex(0,1)*G**2*I16122*I6366)/((-1 + sw)*(1 + sw))) + (complex(0,1)*G**2*I16122*I6566)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16122*I6366*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16122*I6566*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_917 = Coupling(name = 'GC_917',
                  value = '-((complex(0,1)*G**2*I16133*I6366)/((-1 + sw)*(1 + sw))) + (complex(0,1)*G**2*I16233*I6366)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16133*I6566)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16233*I6566)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16133*I6366*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16233*I6366*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16133*I6566*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16233*I6566*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_918 = Coupling(name = 'GC_918',
                  value = '-((complex(0,1)*G**2*I16136*I6366)/((-1 + sw)*(1 + sw))) + (complex(0,1)*G**2*I16236*I6366)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16136*I6566)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16236*I6566)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16136*I6366*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16236*I6366*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16136*I6566*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16236*I6566*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_919 = Coupling(name = 'GC_919',
                  value = '(complex(0,1)*G**2*I16244*I6366)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16244*I6566)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16244*I6366*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16244*I6566*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_920 = Coupling(name = 'GC_920',
                  value = '(complex(0,1)*G**2*I16255*I6366)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16255*I6566)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16255*I6366*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16255*I6566*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_921 = Coupling(name = 'GC_921',
                  value = '-((complex(0,1)*G**2*I16163*I6366)/((-1 + sw)*(1 + sw))) + (complex(0,1)*G**2*I16263*I6366)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16163*I6566)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16263*I6566)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16163*I6366*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16263*I6366*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16163*I6566*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16263*I6566*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_922 = Coupling(name = 'GC_922',
                  value = '-((complex(0,1)*G**2*I16166*I6366)/((-1 + sw)*(1 + sw))) + (complex(0,1)*G**2*I16266*I6366)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16166*I6566)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16266*I6566)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16166*I6366*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16266*I6366*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*G**2*I16166*I6566*sw**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*G**2*I16266*I6566*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QCD':2})

GC_923 = Coupling(name = 'GC_923',
                  value = '-(ee**2*complex(0,1)*I6333*I6433)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I6433*I6533)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6333*I6633)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6533*I6633)/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I6733*I6833)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I6933*I7033)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6433*I6533)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I6733*I6833*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I6933*I7033*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_924 = Coupling(name = 'GC_924',
                  value = '-(ee**2*complex(0,1)*I6336*I6433)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I6433*I6536)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6336*I6633)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6536*I6633)/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I6733*I6836)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I6936*I7033)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6433*I6536)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I6733*I6836*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I6936*I7033*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_925 = Coupling(name = 'GC_925',
                  value = '-(ee**2*complex(0,1)*I6363*I6433)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I6433*I6563)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6363*I6633)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6563*I6633)/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I6733*I6863)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I6963*I7033)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6433*I6563)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I6733*I6863*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I6963*I7033*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_926 = Coupling(name = 'GC_926',
                  value = '-(ee**2*complex(0,1)*I6366*I6433)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I6433*I6566)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6366*I6633)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6566*I6633)/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I6733*I6866)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I6966*I7033)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6433*I6566)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I6733*I6866*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I6966*I7033*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_927 = Coupling(name = 'GC_927',
                  value = '-(ee**2*complex(0,1)*I6333*I6436)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I6436*I6533)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6333*I6636)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6533*I6636)/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I6736*I6833)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I6933*I7036)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6436*I6533)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I6736*I6833*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I6933*I7036*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_928 = Coupling(name = 'GC_928',
                  value = '-(ee**2*complex(0,1)*I6336*I6436)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I6436*I6536)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6336*I6636)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6536*I6636)/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I6736*I6836)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I6936*I7036)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6436*I6536)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I6736*I6836*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I6936*I7036*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_929 = Coupling(name = 'GC_929',
                  value = '-(ee**2*complex(0,1)*I6363*I6436)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I6436*I6563)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6363*I6636)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6563*I6636)/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I6736*I6863)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I6963*I7036)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6436*I6563)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I6736*I6863*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I6963*I7036*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_930 = Coupling(name = 'GC_930',
                  value = '-(ee**2*complex(0,1)*I6366*I6436)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I6436*I6566)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6366*I6636)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6566*I6636)/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I6736*I6866)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I6966*I7036)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6436*I6566)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I6736*I6866*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I6966*I7036*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_931 = Coupling(name = 'GC_931',
                  value = '-(ee**2*complex(0,1)*I6333*I6463)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I6463*I6533)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6333*I6663)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6533*I6663)/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I6763*I6833)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I6933*I7063)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6463*I6533)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I6763*I6833*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I6933*I7063*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_932 = Coupling(name = 'GC_932',
                  value = '-(ee**2*complex(0,1)*I6336*I6463)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I6463*I6536)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6336*I6663)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6536*I6663)/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I6763*I6836)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I6936*I7063)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6463*I6536)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I6763*I6836*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I6936*I7063*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_933 = Coupling(name = 'GC_933',
                  value = '-(ee**2*complex(0,1)*I6363*I6463)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I6463*I6563)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6363*I6663)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6563*I6663)/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I6763*I6863)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I6963*I7063)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6463*I6563)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I6763*I6863*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I6963*I7063*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_934 = Coupling(name = 'GC_934',
                  value = '-(ee**2*complex(0,1)*I6366*I6463)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I6463*I6566)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6366*I6663)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6566*I6663)/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I6763*I6866)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I6966*I7063)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6463*I6566)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I6763*I6866*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I6966*I7063*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_935 = Coupling(name = 'GC_935',
                  value = '-(ee**2*complex(0,1)*I6333*I6466)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I6466*I6533)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6333*I6666)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6533*I6666)/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I6766*I6833)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I6933*I7066)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6466*I6533)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I6766*I6833*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I6933*I7066*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_936 = Coupling(name = 'GC_936',
                  value = '-(ee**2*complex(0,1)*I6336*I6466)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I6466*I6536)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6336*I6666)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6536*I6666)/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I6766*I6836)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I6936*I7066)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6466*I6536)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I6766*I6836*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I6936*I7066*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_937 = Coupling(name = 'GC_937',
                  value = '-(ee**2*complex(0,1)*I6363*I6466)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I6466*I6563)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6363*I6666)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6563*I6666)/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I6766*I6863)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I6963*I7066)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6466*I6563)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I6766*I6863*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I6963*I7066*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_938 = Coupling(name = 'GC_938',
                  value = '-(ee**2*complex(0,1)*I6366*I6466)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I6466*I6566)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6366*I6666)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6566*I6666)/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I6766*I6866)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I6966*I7066)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6466*I6566)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I6766*I6866*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I6966*I7066*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_939 = Coupling(name = 'GC_939',
                  value = '-(ee**2*complex(0,1)*I7533*I7633)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I7433*I7733)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I4733*I7833)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I7133*I7933)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I7933*I8033)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I7733*I8133)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I8233*I8333)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I8433*I8533)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I8633*I8733)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I8833*I8933)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I7133*I7233)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I7333*I7433)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I8233*I8333*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I8433*I8533*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I8633*I8733*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I8833*I8933*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_940 = Coupling(name = 'GC_940',
                  value = '-(ee**2*complex(0,1)*I7536*I7633)/(4.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I7533*I7636)/(4.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I7436*I7733)/(4.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I7433*I7736)/(4.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I4736*I7833)/(4.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I4733*I7836)/(4.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I7136*I7933)/(4.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I7133*I7936)/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I7936*I8033)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I7933*I8036)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I7736*I8133)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I7733*I8136)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I8236*I8333)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I8233*I8336)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I8436*I8533)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I8433*I8536)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I8636*I8733)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I8633*I8736)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I8836*I8933)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I8833*I8936)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I7136*I7233)/(8.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I7133*I7236)/(8.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I7336*I7433)/(8.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I7333*I7436)/(8.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I8236*I8333*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I8233*I8336*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I8436*I8533*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I8433*I8536*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I8636*I8733*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I8633*I8736*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I8836*I8933*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I8833*I8936*sw**2)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_941 = Coupling(name = 'GC_941',
                  value = '-(ee**2*complex(0,1)*I7536*I7636)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I7436*I7736)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I4736*I7836)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I7136*I7936)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I7936*I8036)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I7736*I8136)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I8236*I8336)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I8436*I8536)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I8636*I8736)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I8836*I8936)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I7136*I7236)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I7336*I7436)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I8236*I8336*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I8436*I8536*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I8636*I8736*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I8836*I8936*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_942 = Coupling(name = 'GC_942',
                  value = '-(ee**2*complex(0,1)*I7563*I7633)/(4.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I7533*I7663)/(4.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I7463*I7733)/(4.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I7433*I7763)/(4.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I4763*I7833)/(4.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I4733*I7863)/(4.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I7163*I7933)/(4.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I7133*I7963)/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I7963*I8033)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I7933*I8063)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I7763*I8133)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I7733*I8163)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I8263*I8333)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I8233*I8363)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I8463*I8533)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I8433*I8563)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I8663*I8733)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I8633*I8763)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I8863*I8933)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I8833*I8963)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I7163*I7233)/(8.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I7133*I7263)/(8.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I7363*I7433)/(8.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I7333*I7463)/(8.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I8263*I8333*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I8233*I8363*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I8463*I8533*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I8433*I8563*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I8663*I8733*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I8633*I8763*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I8863*I8933*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I8833*I8963*sw**2)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_943 = Coupling(name = 'GC_943',
                  value = '-(ee**2*complex(0,1)*I7563*I7663)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I7463*I7763)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I4763*I7863)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I7163*I7963)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I7963*I8063)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I7763*I8163)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I8263*I8363)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I8463*I8563)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I8663*I8763)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I8863*I8963)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I7163*I7263)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I7363*I7463)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I8263*I8363*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I8463*I8563*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I8663*I8763*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I8863*I8963*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_944 = Coupling(name = 'GC_944',
                  value = '-(ee**2*complex(0,1)*I7566*I7633)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I7563*I7636)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I7536*I7663)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I7533*I7666)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I7466*I7733)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I7463*I7736)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I7436*I7763)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I7433*I7766)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I4766*I7833)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I4763*I7836)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I4736*I7863)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I4733*I7866)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I7166*I7933)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I7163*I7936)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I7136*I7963)/(8.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I7133*I7966)/(8.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I7966*I8033)/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I7963*I8036)/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I7936*I8063)/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I7933*I8066)/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I7766*I8133)/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I7763*I8136)/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I7736*I8163)/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I7733*I8166)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I8266*I8333)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I8263*I8336)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I8236*I8363)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I8233*I8366)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I8466*I8533)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I8463*I8536)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I8436*I8563)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I8433*I8566)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I8666*I8733)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I8663*I8736)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I8636*I8763)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I8633*I8766)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I8866*I8933)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I8863*I8936)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I8836*I8963)/(4.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I8833*I8966)/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I7166*I7233)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I7163*I7236)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I7136*I7263)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I7133*I7266)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I7366*I7433)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I7363*I7436)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I7336*I7463)/(16.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I7333*I7466)/(16.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I8266*I8333*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I8263*I8336*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I8236*I8363*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I8233*I8366*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I8466*I8533*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I8463*I8536*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I8436*I8563*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I8433*I8566*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I8666*I8733*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I8663*I8736*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I8636*I8763*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I8633*I8766*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I8866*I8933*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I8863*I8936*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I8836*I8963*sw**2)/(4.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I8833*I8966*sw**2)/(4.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_945 = Coupling(name = 'GC_945',
                  value = '-(ee**2*complex(0,1)*I7566*I7636)/(4.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I7536*I7666)/(4.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I7466*I7736)/(4.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I7436*I7766)/(4.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I4766*I7836)/(4.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I4736*I7866)/(4.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I7166*I7936)/(4.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I7136*I7966)/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I7966*I8036)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I7936*I8066)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I7766*I8136)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I7736*I8166)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I8266*I8336)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I8236*I8366)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I8466*I8536)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I8436*I8566)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I8666*I8736)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I8636*I8766)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I8866*I8936)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I8836*I8966)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I7166*I7236)/(8.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I7136*I7266)/(8.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I7366*I7436)/(8.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I7336*I7466)/(8.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I8266*I8336*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I8236*I8366*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I8466*I8536*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I8436*I8566*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I8666*I8736*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I8636*I8766*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I8866*I8936*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I8836*I8966*sw**2)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_946 = Coupling(name = 'GC_946',
                  value = '-(ee**2*complex(0,1)*I7566*I7663)/(4.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I7563*I7666)/(4.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I7466*I7763)/(4.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I7463*I7766)/(4.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I4766*I7863)/(4.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I4763*I7866)/(4.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I7166*I7963)/(4.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I7163*I7966)/(4.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I7966*I8063)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I7963*I8066)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I7766*I8163)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I7763*I8166)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I8266*I8363)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I8263*I8366)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I8466*I8563)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I8463*I8566)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I8666*I8763)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I8663*I8766)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I8866*I8963)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I8863*I8966)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I7166*I7263)/(8.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I7163*I7266)/(8.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I7366*I7463)/(8.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I7363*I7466)/(8.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I8266*I8363*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I8263*I8366*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I8466*I8563*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I8463*I8566*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I8666*I8763*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I8663*I8766*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I8866*I8963*sw**2)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I8863*I8966*sw**2)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_947 = Coupling(name = 'GC_947',
                  value = '-(ee**2*complex(0,1)*I7566*I7666)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I7466*I7766)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I4766*I7866)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I7166*I7966)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I7966*I8066)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I7766*I8166)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I8266*I8366)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I8466*I8566)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I8666*I8766)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I8866*I8966)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I7166*I7266)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I7366*I7466)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I8266*I8366*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I8466*I8566*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I8666*I8766*sw**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I8866*I8966*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_948 = Coupling(name = 'GC_948',
                  value = '(complex(0,1)*I1033*NN13)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I1033*NN13*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN11*Rd36*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_949 = Coupling(name = 'GC_949',
                  value = '(complex(0,1)*I1036*NN13)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I1036*NN13*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN11*Rd66*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_950 = Coupling(name = 'GC_950',
                  value = '(complex(0,1)*I4933*NN13)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I4933*NN13*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN11*Rl36*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_951 = Coupling(name = 'GC_951',
                  value = '(complex(0,1)*I4936*NN13)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I4936*NN13*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN11*Rl66*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_952 = Coupling(name = 'GC_952',
                  value = '(complex(0,1)*I13133*NN14)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I13133*NN14*sw**2)/((-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*NN11*Ru36*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_953 = Coupling(name = 'GC_953',
                  value = '(complex(0,1)*I13136*NN14)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I13136*NN14*sw**2)/((-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*NN11*Ru66*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_954 = Coupling(name = 'GC_954',
                  value = '(complex(0,1)*I1033*NN23)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I1033*NN23*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN21*Rd36*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_955 = Coupling(name = 'GC_955',
                  value = '(complex(0,1)*I1036*NN23)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I1036*NN23*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN21*Rd66*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_956 = Coupling(name = 'GC_956',
                  value = '(complex(0,1)*I4933*NN23)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I4933*NN23*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN21*Rl36*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_957 = Coupling(name = 'GC_957',
                  value = '(complex(0,1)*I4936*NN23)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I4936*NN23*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN21*Rl66*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_958 = Coupling(name = 'GC_958',
                  value = '(complex(0,1)*I13133*NN24)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I13133*NN24*sw**2)/((-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*NN21*Ru36*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_959 = Coupling(name = 'GC_959',
                  value = '(complex(0,1)*I13136*NN24)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I13136*NN24*sw**2)/((-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*NN21*Ru66*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_960 = Coupling(name = 'GC_960',
                  value = '(complex(0,1)*I1033*NN33)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I1033*NN33*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN31*Rd36*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_961 = Coupling(name = 'GC_961',
                  value = '(complex(0,1)*I1036*NN33)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I1036*NN33*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN31*Rd66*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_962 = Coupling(name = 'GC_962',
                  value = '(complex(0,1)*I4933*NN33)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I4933*NN33*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN31*Rl36*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_963 = Coupling(name = 'GC_963',
                  value = '(complex(0,1)*I4936*NN33)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I4936*NN33*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN31*Rl66*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_964 = Coupling(name = 'GC_964',
                  value = '(complex(0,1)*I13133*NN34)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I13133*NN34*sw**2)/((-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*NN31*Ru36*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_965 = Coupling(name = 'GC_965',
                  value = '(complex(0,1)*I13136*NN34)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I13136*NN34*sw**2)/((-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*NN31*Ru66*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_966 = Coupling(name = 'GC_966',
                  value = '(complex(0,1)*I1033*NN43)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I1033*NN43*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN41*Rd36*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_967 = Coupling(name = 'GC_967',
                  value = '(complex(0,1)*I1036*NN43)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I1036*NN43*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN41*Rd66*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_968 = Coupling(name = 'GC_968',
                  value = '(complex(0,1)*I4933*NN43)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I4933*NN43*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN41*Rl36*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_969 = Coupling(name = 'GC_969',
                  value = '(complex(0,1)*I4936*NN43)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I4936*NN43*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN41*Rl66*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_970 = Coupling(name = 'GC_970',
                  value = '(complex(0,1)*I13133*NN44)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I13133*NN44*sw**2)/((-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*NN41*Ru36*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_971 = Coupling(name = 'GC_971',
                  value = '(complex(0,1)*I13136*NN44)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I13136*NN44*sw**2)/((-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*NN41*Ru66*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_972 = Coupling(name = 'GC_972',
                  value = '-((ee*complex(0,1)*I18711*UU11)/sw)',
                  order = {'QED':1})

GC_973 = Coupling(name = 'GC_973',
                  value = '-((ee*complex(0,1)*I18722*UU11)/sw)',
                  order = {'QED':1})

GC_974 = Coupling(name = 'GC_974',
                  value = '-((ee*complex(0,1)*I19011*UU11)/sw)',
                  order = {'QED':1})

GC_975 = Coupling(name = 'GC_975',
                  value = '-((ee*complex(0,1)*I19022*UU11)/sw)',
                  order = {'QED':1})

GC_976 = Coupling(name = 'GC_976',
                  value = 'complex(0,1)*I13433*UU12',
                  order = {'QED':1})

GC_977 = Coupling(name = 'GC_977',
                  value = 'complex(0,1)*I13436*UU12',
                  order = {'QED':1})

GC_978 = Coupling(name = 'GC_978',
                  value = 'complex(0,1)*I9733*UU12',
                  order = {'QED':1})

GC_979 = Coupling(name = 'GC_979',
                  value = '-((ee*complex(0,1)*I18733*UU11)/sw) + complex(0,1)*I18833*UU12',
                  order = {'QED':1})

GC_980 = Coupling(name = 'GC_980',
                  value = '-((ee*complex(0,1)*I18736*UU11)/sw) + complex(0,1)*I18836*UU12',
                  order = {'QED':1})

GC_981 = Coupling(name = 'GC_981',
                  value = '-((ee*complex(0,1)*I19033*UU11)/sw) + complex(0,1)*I19133*UU12',
                  order = {'QED':1})

GC_982 = Coupling(name = 'GC_982',
                  value = '-((ee*complex(0,1)*I19036*UU11)/sw) + complex(0,1)*I19136*UU12',
                  order = {'QED':1})

GC_983 = Coupling(name = 'GC_983',
                  value = '-((ee*complex(0,1)*I18711*UU21)/sw)',
                  order = {'QED':1})

GC_984 = Coupling(name = 'GC_984',
                  value = '-((ee*complex(0,1)*I18722*UU21)/sw)',
                  order = {'QED':1})

GC_985 = Coupling(name = 'GC_985',
                  value = '-((ee*complex(0,1)*I19011*UU21)/sw)',
                  order = {'QED':1})

GC_986 = Coupling(name = 'GC_986',
                  value = '-((ee*complex(0,1)*I19022*UU21)/sw)',
                  order = {'QED':1})

GC_987 = Coupling(name = 'GC_987',
                  value = 'complex(0,1)*I13433*UU22',
                  order = {'QED':1})

GC_988 = Coupling(name = 'GC_988',
                  value = 'complex(0,1)*I13436*UU22',
                  order = {'QED':1})

GC_989 = Coupling(name = 'GC_989',
                  value = 'complex(0,1)*I9733*UU22',
                  order = {'QED':1})

GC_990 = Coupling(name = 'GC_990',
                  value = '-((ee*complex(0,1)*I18733*UU21)/sw) + complex(0,1)*I18833*UU22',
                  order = {'QED':1})

GC_991 = Coupling(name = 'GC_991',
                  value = '-((ee*complex(0,1)*I18736*UU21)/sw) + complex(0,1)*I18836*UU22',
                  order = {'QED':1})

GC_992 = Coupling(name = 'GC_992',
                  value = '-((ee*complex(0,1)*I19033*UU21)/sw) + complex(0,1)*I19133*UU22',
                  order = {'QED':1})

GC_993 = Coupling(name = 'GC_993',
                  value = '-((ee*complex(0,1)*I19036*UU21)/sw) + complex(0,1)*I19136*UU22',
                  order = {'QED':1})

GC_994 = Coupling(name = 'GC_994',
                  value = '-((ee*complex(0,1)*I19211*VV11)/sw)',
                  order = {'QED':1})

GC_995 = Coupling(name = 'GC_995',
                  value = '-((ee*complex(0,1)*I19222*VV11)/sw)',
                  order = {'QED':1})

GC_996 = Coupling(name = 'GC_996',
                  value = '-((ee*complex(0,1)*I19233*VV11)/sw)',
                  order = {'QED':1})

GC_997 = Coupling(name = 'GC_997',
                  value = '-((ee*complex(0,1)*I19411*VV11)/sw)',
                  order = {'QED':1})

GC_998 = Coupling(name = 'GC_998',
                  value = '-((ee*complex(0,1)*I19422*VV11)/sw)',
                  order = {'QED':1})

GC_999 = Coupling(name = 'GC_999',
                  value = 'complex(0,1)*I833*VV12',
                  order = {'QED':1})

GC_1000 = Coupling(name = 'GC_1000',
                   value = 'complex(0,1)*I836*VV12',
                   order = {'QED':1})

GC_1001 = Coupling(name = 'GC_1001',
                   value = '-((ee*complex(0,1)*I19433*VV11)/sw) + complex(0,1)*I19533*VV12',
                   order = {'QED':1})

GC_1002 = Coupling(name = 'GC_1002',
                   value = '-((ee*complex(0,1)*I19436*VV11)/sw) + complex(0,1)*I19536*VV12',
                   order = {'QED':1})

GC_1003 = Coupling(name = 'GC_1003',
                   value = '-((ee*complex(0,1)*I19211*VV21)/sw)',
                   order = {'QED':1})

GC_1004 = Coupling(name = 'GC_1004',
                   value = '-((ee*complex(0,1)*I19222*VV21)/sw)',
                   order = {'QED':1})

GC_1005 = Coupling(name = 'GC_1005',
                   value = '-((ee*complex(0,1)*I19233*VV21)/sw)',
                   order = {'QED':1})

GC_1006 = Coupling(name = 'GC_1006',
                   value = '-((ee*complex(0,1)*I19411*VV21)/sw)',
                   order = {'QED':1})

GC_1007 = Coupling(name = 'GC_1007',
                   value = '-((ee*complex(0,1)*I19422*VV21)/sw)',
                   order = {'QED':1})

GC_1008 = Coupling(name = 'GC_1008',
                   value = 'complex(0,1)*I833*VV22',
                   order = {'QED':1})

GC_1009 = Coupling(name = 'GC_1009',
                   value = 'complex(0,1)*I836*VV22',
                   order = {'QED':1})

GC_1010 = Coupling(name = 'GC_1010',
                   value = '-((ee*complex(0,1)*I19433*VV21)/sw) + complex(0,1)*I19533*VV22',
                   order = {'QED':1})

GC_1011 = Coupling(name = 'GC_1011',
                   value = '-((ee*complex(0,1)*I19436*VV21)/sw) + complex(0,1)*I19536*VV22',
                   order = {'QED':1})

GC_1012 = Coupling(name = 'GC_1012',
                   value = '(ee*complex(0,1)*complexconjugate(CKM11))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1013 = Coupling(name = 'GC_1013',
                   value = '(ee*complex(0,1)*complexconjugate(CKM22))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1014 = Coupling(name = 'GC_1014',
                   value = '(ee*complex(0,1)*complexconjugate(CKM33))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1015 = Coupling(name = 'GC_1015',
                   value = '(cw*ee*complex(0,1)*Rd11*complexconjugate(NN11))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rd11*complexconjugate(NN12))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rd11*sw*complexconjugate(NN12))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1016 = Coupling(name = 'GC_1016',
                   value = '(cw*ee*complex(0,1)*Rd22*complexconjugate(NN11))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rd22*complexconjugate(NN12))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rd22*sw*complexconjugate(NN12))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1017 = Coupling(name = 'GC_1017',
                   value = '-((cw*ee*complex(0,1)*Rl11*complexconjugate(NN11))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) - (ee*complex(0,1)*Rl11*complexconjugate(NN12))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rl11*sw*complexconjugate(NN12))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1018 = Coupling(name = 'GC_1018',
                   value = '-((cw*ee*complex(0,1)*Rl22*complexconjugate(NN11))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) - (ee*complex(0,1)*Rl22*complexconjugate(NN12))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rl22*sw*complexconjugate(NN12))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1019 = Coupling(name = 'GC_1019',
                   value = '-((cw*ee*complex(0,1)*Rn11*complexconjugate(NN11))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*Rn11*complexconjugate(NN12))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rn11*sw*complexconjugate(NN12))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1020 = Coupling(name = 'GC_1020',
                   value = '-((cw*ee*complex(0,1)*Rn22*complexconjugate(NN11))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*Rn22*complexconjugate(NN12))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rn22*sw*complexconjugate(NN12))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1021 = Coupling(name = 'GC_1021',
                   value = '-((cw*ee*complex(0,1)*Rn33*complexconjugate(NN11))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*Rn33*complexconjugate(NN12))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rn33*sw*complexconjugate(NN12))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1022 = Coupling(name = 'GC_1022',
                   value = '(cw*ee*complex(0,1)*Ru11*complexconjugate(NN11))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Ru11*complexconjugate(NN12))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Ru11*sw*complexconjugate(NN12))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1023 = Coupling(name = 'GC_1023',
                   value = '(cw*ee*complex(0,1)*Ru22*complexconjugate(NN11))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Ru22*complexconjugate(NN12))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Ru22*sw*complexconjugate(NN12))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1024 = Coupling(name = 'GC_1024',
                   value = '(complex(0,1)*I1133*complexconjugate(NN13))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I1133*sw**2*complexconjugate(NN13))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*Rd33*complexconjugate(NN11))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rd33*complexconjugate(NN12))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rd33*sw*complexconjugate(NN12))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1025 = Coupling(name = 'GC_1025',
                   value = '(complex(0,1)*I1136*complexconjugate(NN13))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I1136*sw**2*complexconjugate(NN13))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*Rd63*complexconjugate(NN11))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rd63*complexconjugate(NN12))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rd63*sw*complexconjugate(NN12))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1026 = Coupling(name = 'GC_1026',
                   value = '(complex(0,1)*I5033*complexconjugate(NN13))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I5033*sw**2*complexconjugate(NN13))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*Rl33*complexconjugate(NN11))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rl33*complexconjugate(NN12))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rl33*sw*complexconjugate(NN12))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1027 = Coupling(name = 'GC_1027',
                   value = '(complex(0,1)*I5036*complexconjugate(NN13))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I5036*sw**2*complexconjugate(NN13))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*Rl63*complexconjugate(NN11))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rl63*complexconjugate(NN12))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rl63*sw*complexconjugate(NN12))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1028 = Coupling(name = 'GC_1028',
                   value = '-((ee*complex(0,1)*UU11*complexconjugate(NN12))/sw) - (ee*complex(0,1)*UU12*complexconjugate(NN13))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1029 = Coupling(name = 'GC_1029',
                   value = '-((ee*complex(0,1)*UU21*complexconjugate(NN12))/sw) - (ee*complex(0,1)*UU22*complexconjugate(NN13))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1030 = Coupling(name = 'GC_1030',
                   value = '-(cw*ee*complex(0,1)*NN13*complexconjugate(NN13))/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*NN14*complexconjugate(NN14))/(2.*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1})

GC_1031 = Coupling(name = 'GC_1031',
                   value = '(cw*ee*complex(0,1)*NN23*complexconjugate(NN13))/(2.*(-1 + sw)*sw*(1 + sw)) - (cw*ee*complex(0,1)*NN24*complexconjugate(NN14))/(2.*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1})

GC_1032 = Coupling(name = 'GC_1032',
                   value = '(cw*ee*complex(0,1)*NN33*complexconjugate(NN13))/(2.*(-1 + sw)*sw*(1 + sw)) - (cw*ee*complex(0,1)*NN34*complexconjugate(NN14))/(2.*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1})

GC_1033 = Coupling(name = 'GC_1033',
                   value = '(cw*ee*complex(0,1)*NN43*complexconjugate(NN13))/(2.*(-1 + sw)*sw*(1 + sw)) - (cw*ee*complex(0,1)*NN44*complexconjugate(NN14))/(2.*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1})

GC_1034 = Coupling(name = 'GC_1034',
                   value = '(complex(0,1)*I13233*complexconjugate(NN14))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I13233*sw**2*complexconjugate(NN14))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*Ru33*complexconjugate(NN11))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Ru33*complexconjugate(NN12))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Ru33*sw*complexconjugate(NN12))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1035 = Coupling(name = 'GC_1035',
                   value = '(complex(0,1)*I13236*complexconjugate(NN14))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I13236*sw**2*complexconjugate(NN14))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*Ru63*complexconjugate(NN11))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Ru63*complexconjugate(NN12))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Ru63*sw*complexconjugate(NN12))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1036 = Coupling(name = 'GC_1036',
                   value = '-((ee*complex(0,1)*VV11*complexconjugate(NN12))/sw) + (ee*complex(0,1)*VV12*complexconjugate(NN14))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1037 = Coupling(name = 'GC_1037',
                   value = '-((ee*complex(0,1)*VV21*complexconjugate(NN12))/sw) + (ee*complex(0,1)*VV22*complexconjugate(NN14))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1038 = Coupling(name = 'GC_1038',
                   value = '(cw*ee*complex(0,1)*Rd11*complexconjugate(NN21))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rd11*complexconjugate(NN22))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rd11*sw*complexconjugate(NN22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1039 = Coupling(name = 'GC_1039',
                   value = '(cw*ee*complex(0,1)*Rd22*complexconjugate(NN21))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rd22*complexconjugate(NN22))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rd22*sw*complexconjugate(NN22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1040 = Coupling(name = 'GC_1040',
                   value = '-((cw*ee*complex(0,1)*Rl11*complexconjugate(NN21))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) - (ee*complex(0,1)*Rl11*complexconjugate(NN22))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rl11*sw*complexconjugate(NN22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1041 = Coupling(name = 'GC_1041',
                   value = '-((cw*ee*complex(0,1)*Rl22*complexconjugate(NN21))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) - (ee*complex(0,1)*Rl22*complexconjugate(NN22))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rl22*sw*complexconjugate(NN22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1042 = Coupling(name = 'GC_1042',
                   value = '-((cw*ee*complex(0,1)*Rn11*complexconjugate(NN21))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*Rn11*complexconjugate(NN22))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rn11*sw*complexconjugate(NN22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1043 = Coupling(name = 'GC_1043',
                   value = '-((cw*ee*complex(0,1)*Rn22*complexconjugate(NN21))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*Rn22*complexconjugate(NN22))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rn22*sw*complexconjugate(NN22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1044 = Coupling(name = 'GC_1044',
                   value = '-((cw*ee*complex(0,1)*Rn33*complexconjugate(NN21))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*Rn33*complexconjugate(NN22))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rn33*sw*complexconjugate(NN22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1045 = Coupling(name = 'GC_1045',
                   value = '(cw*ee*complex(0,1)*Ru11*complexconjugate(NN21))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Ru11*complexconjugate(NN22))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Ru11*sw*complexconjugate(NN22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1046 = Coupling(name = 'GC_1046',
                   value = '(cw*ee*complex(0,1)*Ru22*complexconjugate(NN21))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Ru22*complexconjugate(NN22))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Ru22*sw*complexconjugate(NN22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1047 = Coupling(name = 'GC_1047',
                   value = '(complex(0,1)*I1133*complexconjugate(NN23))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I1133*sw**2*complexconjugate(NN23))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*Rd33*complexconjugate(NN21))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rd33*complexconjugate(NN22))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rd33*sw*complexconjugate(NN22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1048 = Coupling(name = 'GC_1048',
                   value = '(complex(0,1)*I1136*complexconjugate(NN23))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I1136*sw**2*complexconjugate(NN23))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*Rd63*complexconjugate(NN21))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rd63*complexconjugate(NN22))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rd63*sw*complexconjugate(NN22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1049 = Coupling(name = 'GC_1049',
                   value = '(complex(0,1)*I5033*complexconjugate(NN23))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I5033*sw**2*complexconjugate(NN23))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*Rl33*complexconjugate(NN21))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rl33*complexconjugate(NN22))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rl33*sw*complexconjugate(NN22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1050 = Coupling(name = 'GC_1050',
                   value = '(complex(0,1)*I5036*complexconjugate(NN23))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I5036*sw**2*complexconjugate(NN23))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*Rl63*complexconjugate(NN21))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rl63*complexconjugate(NN22))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rl63*sw*complexconjugate(NN22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1051 = Coupling(name = 'GC_1051',
                   value = '-((ee*complex(0,1)*UU11*complexconjugate(NN22))/sw) - (ee*complex(0,1)*UU12*complexconjugate(NN23))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1052 = Coupling(name = 'GC_1052',
                   value = '-((ee*complex(0,1)*UU21*complexconjugate(NN22))/sw) - (ee*complex(0,1)*UU22*complexconjugate(NN23))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1053 = Coupling(name = 'GC_1053',
                   value = '-(cw*ee*complex(0,1)*NN13*complexconjugate(NN23))/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*NN14*complexconjugate(NN24))/(2.*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1})

GC_1054 = Coupling(name = 'GC_1054',
                   value = '-(cw*ee*complex(0,1)*NN23*complexconjugate(NN23))/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*NN24*complexconjugate(NN24))/(2.*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1})

GC_1055 = Coupling(name = 'GC_1055',
                   value = '(cw*ee*complex(0,1)*NN33*complexconjugate(NN23))/(2.*(-1 + sw)*sw*(1 + sw)) - (cw*ee*complex(0,1)*NN34*complexconjugate(NN24))/(2.*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1})

GC_1056 = Coupling(name = 'GC_1056',
                   value = '(cw*ee*complex(0,1)*NN43*complexconjugate(NN23))/(2.*(-1 + sw)*sw*(1 + sw)) - (cw*ee*complex(0,1)*NN44*complexconjugate(NN24))/(2.*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1})

GC_1057 = Coupling(name = 'GC_1057',
                   value = '(complex(0,1)*I13233*complexconjugate(NN24))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I13233*sw**2*complexconjugate(NN24))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*Ru33*complexconjugate(NN21))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Ru33*complexconjugate(NN22))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Ru33*sw*complexconjugate(NN22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1058 = Coupling(name = 'GC_1058',
                   value = '(complex(0,1)*I13236*complexconjugate(NN24))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I13236*sw**2*complexconjugate(NN24))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*Ru63*complexconjugate(NN21))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Ru63*complexconjugate(NN22))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Ru63*sw*complexconjugate(NN22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1059 = Coupling(name = 'GC_1059',
                   value = '-((ee*complex(0,1)*VV11*complexconjugate(NN22))/sw) + (ee*complex(0,1)*VV12*complexconjugate(NN24))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1060 = Coupling(name = 'GC_1060',
                   value = '-((ee*complex(0,1)*VV21*complexconjugate(NN22))/sw) + (ee*complex(0,1)*VV22*complexconjugate(NN24))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1061 = Coupling(name = 'GC_1061',
                   value = '(cw*ee*complex(0,1)*Rd11*complexconjugate(NN31))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rd11*complexconjugate(NN32))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rd11*sw*complexconjugate(NN32))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1062 = Coupling(name = 'GC_1062',
                   value = '(cw*ee*complex(0,1)*Rd22*complexconjugate(NN31))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rd22*complexconjugate(NN32))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rd22*sw*complexconjugate(NN32))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1063 = Coupling(name = 'GC_1063',
                   value = '-((cw*ee*complex(0,1)*Rl11*complexconjugate(NN31))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) - (ee*complex(0,1)*Rl11*complexconjugate(NN32))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rl11*sw*complexconjugate(NN32))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1064 = Coupling(name = 'GC_1064',
                   value = '-((cw*ee*complex(0,1)*Rl22*complexconjugate(NN31))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) - (ee*complex(0,1)*Rl22*complexconjugate(NN32))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rl22*sw*complexconjugate(NN32))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1065 = Coupling(name = 'GC_1065',
                   value = '-((cw*ee*complex(0,1)*Rn11*complexconjugate(NN31))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*Rn11*complexconjugate(NN32))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rn11*sw*complexconjugate(NN32))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1066 = Coupling(name = 'GC_1066',
                   value = '-((cw*ee*complex(0,1)*Rn22*complexconjugate(NN31))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*Rn22*complexconjugate(NN32))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rn22*sw*complexconjugate(NN32))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1067 = Coupling(name = 'GC_1067',
                   value = '-((cw*ee*complex(0,1)*Rn33*complexconjugate(NN31))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*Rn33*complexconjugate(NN32))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rn33*sw*complexconjugate(NN32))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1068 = Coupling(name = 'GC_1068',
                   value = '(cw*ee*complex(0,1)*Ru11*complexconjugate(NN31))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Ru11*complexconjugate(NN32))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Ru11*sw*complexconjugate(NN32))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1069 = Coupling(name = 'GC_1069',
                   value = '(cw*ee*complex(0,1)*Ru22*complexconjugate(NN31))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Ru22*complexconjugate(NN32))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Ru22*sw*complexconjugate(NN32))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1070 = Coupling(name = 'GC_1070',
                   value = '(complex(0,1)*I1133*complexconjugate(NN33))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I1133*sw**2*complexconjugate(NN33))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*Rd33*complexconjugate(NN31))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rd33*complexconjugate(NN32))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rd33*sw*complexconjugate(NN32))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1071 = Coupling(name = 'GC_1071',
                   value = '(complex(0,1)*I1136*complexconjugate(NN33))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I1136*sw**2*complexconjugate(NN33))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*Rd63*complexconjugate(NN31))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rd63*complexconjugate(NN32))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rd63*sw*complexconjugate(NN32))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1072 = Coupling(name = 'GC_1072',
                   value = '(complex(0,1)*I5033*complexconjugate(NN33))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I5033*sw**2*complexconjugate(NN33))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*Rl33*complexconjugate(NN31))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rl33*complexconjugate(NN32))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rl33*sw*complexconjugate(NN32))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1073 = Coupling(name = 'GC_1073',
                   value = '(complex(0,1)*I5036*complexconjugate(NN33))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I5036*sw**2*complexconjugate(NN33))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*Rl63*complexconjugate(NN31))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rl63*complexconjugate(NN32))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rl63*sw*complexconjugate(NN32))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1074 = Coupling(name = 'GC_1074',
                   value = '-((ee*complex(0,1)*UU11*complexconjugate(NN32))/sw) - (ee*complex(0,1)*UU12*complexconjugate(NN33))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1075 = Coupling(name = 'GC_1075',
                   value = '-((ee*complex(0,1)*UU21*complexconjugate(NN32))/sw) - (ee*complex(0,1)*UU22*complexconjugate(NN33))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1076 = Coupling(name = 'GC_1076',
                   value = '-(cw*ee*complex(0,1)*NN13*complexconjugate(NN33))/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*NN14*complexconjugate(NN34))/(2.*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1})

GC_1077 = Coupling(name = 'GC_1077',
                   value = '-(cw*ee*complex(0,1)*NN23*complexconjugate(NN33))/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*NN24*complexconjugate(NN34))/(2.*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1})

GC_1078 = Coupling(name = 'GC_1078',
                   value = '-(cw*ee*complex(0,1)*NN33*complexconjugate(NN33))/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*NN34*complexconjugate(NN34))/(2.*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1})

GC_1079 = Coupling(name = 'GC_1079',
                   value = '(cw*ee*complex(0,1)*NN43*complexconjugate(NN33))/(2.*(-1 + sw)*sw*(1 + sw)) - (cw*ee*complex(0,1)*NN44*complexconjugate(NN34))/(2.*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1})

GC_1080 = Coupling(name = 'GC_1080',
                   value = '(complex(0,1)*I13233*complexconjugate(NN34))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I13233*sw**2*complexconjugate(NN34))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*Ru33*complexconjugate(NN31))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Ru33*complexconjugate(NN32))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Ru33*sw*complexconjugate(NN32))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1081 = Coupling(name = 'GC_1081',
                   value = '(complex(0,1)*I13236*complexconjugate(NN34))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I13236*sw**2*complexconjugate(NN34))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*Ru63*complexconjugate(NN31))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Ru63*complexconjugate(NN32))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Ru63*sw*complexconjugate(NN32))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1082 = Coupling(name = 'GC_1082',
                   value = '-((ee*complex(0,1)*VV11*complexconjugate(NN32))/sw) + (ee*complex(0,1)*VV12*complexconjugate(NN34))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1083 = Coupling(name = 'GC_1083',
                   value = '-((ee*complex(0,1)*VV21*complexconjugate(NN32))/sw) + (ee*complex(0,1)*VV22*complexconjugate(NN34))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1084 = Coupling(name = 'GC_1084',
                   value = '(cw*ee*complex(0,1)*Rd11*complexconjugate(NN41))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rd11*complexconjugate(NN42))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rd11*sw*complexconjugate(NN42))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1085 = Coupling(name = 'GC_1085',
                   value = '(cw*ee*complex(0,1)*Rd22*complexconjugate(NN41))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rd22*complexconjugate(NN42))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rd22*sw*complexconjugate(NN42))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1086 = Coupling(name = 'GC_1086',
                   value = '-((cw*ee*complex(0,1)*Rl11*complexconjugate(NN41))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) - (ee*complex(0,1)*Rl11*complexconjugate(NN42))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rl11*sw*complexconjugate(NN42))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1087 = Coupling(name = 'GC_1087',
                   value = '-((cw*ee*complex(0,1)*Rl22*complexconjugate(NN41))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) - (ee*complex(0,1)*Rl22*complexconjugate(NN42))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rl22*sw*complexconjugate(NN42))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1088 = Coupling(name = 'GC_1088',
                   value = '-((cw*ee*complex(0,1)*Rn11*complexconjugate(NN41))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*Rn11*complexconjugate(NN42))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rn11*sw*complexconjugate(NN42))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1089 = Coupling(name = 'GC_1089',
                   value = '-((cw*ee*complex(0,1)*Rn22*complexconjugate(NN41))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*Rn22*complexconjugate(NN42))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rn22*sw*complexconjugate(NN42))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1090 = Coupling(name = 'GC_1090',
                   value = '-((cw*ee*complex(0,1)*Rn33*complexconjugate(NN41))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*Rn33*complexconjugate(NN42))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rn33*sw*complexconjugate(NN42))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1091 = Coupling(name = 'GC_1091',
                   value = '(cw*ee*complex(0,1)*Ru11*complexconjugate(NN41))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Ru11*complexconjugate(NN42))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Ru11*sw*complexconjugate(NN42))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1092 = Coupling(name = 'GC_1092',
                   value = '(cw*ee*complex(0,1)*Ru22*complexconjugate(NN41))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Ru22*complexconjugate(NN42))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Ru22*sw*complexconjugate(NN42))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1093 = Coupling(name = 'GC_1093',
                   value = '(complex(0,1)*I1133*complexconjugate(NN43))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I1133*sw**2*complexconjugate(NN43))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*Rd33*complexconjugate(NN41))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rd33*complexconjugate(NN42))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rd33*sw*complexconjugate(NN42))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1094 = Coupling(name = 'GC_1094',
                   value = '(complex(0,1)*I1136*complexconjugate(NN43))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I1136*sw**2*complexconjugate(NN43))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*Rd63*complexconjugate(NN41))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rd63*complexconjugate(NN42))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rd63*sw*complexconjugate(NN42))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1095 = Coupling(name = 'GC_1095',
                   value = '(complex(0,1)*I5033*complexconjugate(NN43))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I5033*sw**2*complexconjugate(NN43))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*Rl33*complexconjugate(NN41))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rl33*complexconjugate(NN42))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rl33*sw*complexconjugate(NN42))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1096 = Coupling(name = 'GC_1096',
                   value = '(complex(0,1)*I5036*complexconjugate(NN43))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I5036*sw**2*complexconjugate(NN43))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*Rl63*complexconjugate(NN41))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rl63*complexconjugate(NN42))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rl63*sw*complexconjugate(NN42))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1097 = Coupling(name = 'GC_1097',
                   value = '-((ee*complex(0,1)*UU11*complexconjugate(NN42))/sw) - (ee*complex(0,1)*UU12*complexconjugate(NN43))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1098 = Coupling(name = 'GC_1098',
                   value = '-((ee*complex(0,1)*UU21*complexconjugate(NN42))/sw) - (ee*complex(0,1)*UU22*complexconjugate(NN43))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1099 = Coupling(name = 'GC_1099',
                   value = '-(cw*ee*complex(0,1)*NN13*complexconjugate(NN43))/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*NN14*complexconjugate(NN44))/(2.*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1})

GC_1100 = Coupling(name = 'GC_1100',
                   value = '-(cw*ee*complex(0,1)*NN23*complexconjugate(NN43))/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*NN24*complexconjugate(NN44))/(2.*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1})

GC_1101 = Coupling(name = 'GC_1101',
                   value = '-(cw*ee*complex(0,1)*NN33*complexconjugate(NN43))/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*NN34*complexconjugate(NN44))/(2.*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1})

GC_1102 = Coupling(name = 'GC_1102',
                   value = '-(cw*ee*complex(0,1)*NN43*complexconjugate(NN43))/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*NN44*complexconjugate(NN44))/(2.*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1})

GC_1103 = Coupling(name = 'GC_1103',
                   value = '(complex(0,1)*I13233*complexconjugate(NN44))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I13233*sw**2*complexconjugate(NN44))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*Ru33*complexconjugate(NN41))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Ru33*complexconjugate(NN42))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Ru33*sw*complexconjugate(NN42))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1104 = Coupling(name = 'GC_1104',
                   value = '(complex(0,1)*I13236*complexconjugate(NN44))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I13236*sw**2*complexconjugate(NN44))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*Ru63*complexconjugate(NN41))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Ru63*complexconjugate(NN42))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Ru63*sw*complexconjugate(NN42))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1105 = Coupling(name = 'GC_1105',
                   value = '-((ee*complex(0,1)*VV11*complexconjugate(NN42))/sw) + (ee*complex(0,1)*VV12*complexconjugate(NN44))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1106 = Coupling(name = 'GC_1106',
                   value = '-((ee*complex(0,1)*VV21*complexconjugate(NN42))/sw) + (ee*complex(0,1)*VV22*complexconjugate(NN44))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1107 = Coupling(name = 'GC_1107',
                   value = '-(complex(0,1)*G*complexconjugate(Rd11)*cmath.sqrt(2))',
                   order = {'QCD':1})

GC_1108 = Coupling(name = 'GC_1108',
                   value = '(cw*ee*complex(0,1)*NN11*complexconjugate(Rd11))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN12*complexconjugate(Rd11))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN12*sw*complexconjugate(Rd11))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1109 = Coupling(name = 'GC_1109',
                   value = '(cw*ee*complex(0,1)*NN21*complexconjugate(Rd11))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN22*complexconjugate(Rd11))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN22*sw*complexconjugate(Rd11))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1110 = Coupling(name = 'GC_1110',
                   value = '(cw*ee*complex(0,1)*NN31*complexconjugate(Rd11))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN32*complexconjugate(Rd11))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN32*sw*complexconjugate(Rd11))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1111 = Coupling(name = 'GC_1111',
                   value = '(cw*ee*complex(0,1)*NN41*complexconjugate(Rd11))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN42*complexconjugate(Rd11))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN42*sw*complexconjugate(Rd11))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1112 = Coupling(name = 'GC_1112',
                   value = '-(complex(0,1)*G*complexconjugate(Rd22)*cmath.sqrt(2))',
                   order = {'QCD':1})

GC_1113 = Coupling(name = 'GC_1113',
                   value = '(cw*ee*complex(0,1)*NN11*complexconjugate(Rd22))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN12*complexconjugate(Rd22))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN12*sw*complexconjugate(Rd22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1114 = Coupling(name = 'GC_1114',
                   value = '(cw*ee*complex(0,1)*NN21*complexconjugate(Rd22))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN22*complexconjugate(Rd22))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN22*sw*complexconjugate(Rd22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1115 = Coupling(name = 'GC_1115',
                   value = '(cw*ee*complex(0,1)*NN31*complexconjugate(Rd22))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN32*complexconjugate(Rd22))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN32*sw*complexconjugate(Rd22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1116 = Coupling(name = 'GC_1116',
                   value = '(cw*ee*complex(0,1)*NN41*complexconjugate(Rd22))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN42*complexconjugate(Rd22))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN42*sw*complexconjugate(Rd22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1117 = Coupling(name = 'GC_1117',
                   value = '-(complex(0,1)*G*complexconjugate(Rd33)*cmath.sqrt(2))',
                   order = {'QCD':1})

GC_1118 = Coupling(name = 'GC_1118',
                   value = '(complex(0,1)*I333*NN13)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I333*NN13*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN11*complexconjugate(Rd33))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN12*complexconjugate(Rd33))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN12*sw*complexconjugate(Rd33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1119 = Coupling(name = 'GC_1119',
                   value = '(complex(0,1)*I333*NN23)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I333*NN23*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN21*complexconjugate(Rd33))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN22*complexconjugate(Rd33))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN22*sw*complexconjugate(Rd33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1120 = Coupling(name = 'GC_1120',
                   value = '(complex(0,1)*I333*NN33)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I333*NN33*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN31*complexconjugate(Rd33))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN32*complexconjugate(Rd33))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN32*sw*complexconjugate(Rd33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1121 = Coupling(name = 'GC_1121',
                   value = '(complex(0,1)*I333*NN43)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I333*NN43*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN41*complexconjugate(Rd33))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN42*complexconjugate(Rd33))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN42*sw*complexconjugate(Rd33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1122 = Coupling(name = 'GC_1122',
                   value = 'complex(0,1)*G*complexconjugate(Rd36)*cmath.sqrt(2)',
                   order = {'QCD':1})

GC_1123 = Coupling(name = 'GC_1123',
                   value = '(complex(0,1)*I433*complexconjugate(NN13))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I433*sw**2*complexconjugate(NN13))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN11)*complexconjugate(Rd36)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1124 = Coupling(name = 'GC_1124',
                   value = '(complex(0,1)*I433*complexconjugate(NN23))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I433*sw**2*complexconjugate(NN23))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN21)*complexconjugate(Rd36)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1125 = Coupling(name = 'GC_1125',
                   value = '(complex(0,1)*I433*complexconjugate(NN33))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I433*sw**2*complexconjugate(NN33))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN31)*complexconjugate(Rd36)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1126 = Coupling(name = 'GC_1126',
                   value = '(complex(0,1)*I433*complexconjugate(NN43))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I433*sw**2*complexconjugate(NN43))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN41)*complexconjugate(Rd36)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1127 = Coupling(name = 'GC_1127',
                   value = 'complex(0,1)*G*complexconjugate(Rd44)*cmath.sqrt(2)',
                   order = {'QCD':1})

GC_1128 = Coupling(name = 'GC_1128',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN11)*complexconjugate(Rd44)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1129 = Coupling(name = 'GC_1129',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN21)*complexconjugate(Rd44)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1130 = Coupling(name = 'GC_1130',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN31)*complexconjugate(Rd44)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1131 = Coupling(name = 'GC_1131',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN41)*complexconjugate(Rd44)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1132 = Coupling(name = 'GC_1132',
                   value = 'complex(0,1)*G*complexconjugate(Rd55)*cmath.sqrt(2)',
                   order = {'QCD':1})

GC_1133 = Coupling(name = 'GC_1133',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN11)*complexconjugate(Rd55)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1134 = Coupling(name = 'GC_1134',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN21)*complexconjugate(Rd55)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1135 = Coupling(name = 'GC_1135',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN31)*complexconjugate(Rd55)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1136 = Coupling(name = 'GC_1136',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN41)*complexconjugate(Rd55)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1137 = Coupling(name = 'GC_1137',
                   value = '-(complex(0,1)*G*complexconjugate(Rd63)*cmath.sqrt(2))',
                   order = {'QCD':1})

GC_1138 = Coupling(name = 'GC_1138',
                   value = '(complex(0,1)*I336*NN13)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I336*NN13*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN11*complexconjugate(Rd63))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN12*complexconjugate(Rd63))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN12*sw*complexconjugate(Rd63))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1139 = Coupling(name = 'GC_1139',
                   value = '(complex(0,1)*I336*NN23)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I336*NN23*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN21*complexconjugate(Rd63))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN22*complexconjugate(Rd63))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN22*sw*complexconjugate(Rd63))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1140 = Coupling(name = 'GC_1140',
                   value = '(complex(0,1)*I336*NN33)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I336*NN33*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN31*complexconjugate(Rd63))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN32*complexconjugate(Rd63))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN32*sw*complexconjugate(Rd63))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1141 = Coupling(name = 'GC_1141',
                   value = '(complex(0,1)*I336*NN43)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I336*NN43*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN41*complexconjugate(Rd63))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN42*complexconjugate(Rd63))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN42*sw*complexconjugate(Rd63))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1142 = Coupling(name = 'GC_1142',
                   value = 'complex(0,1)*G*complexconjugate(Rd66)*cmath.sqrt(2)',
                   order = {'QCD':1})

GC_1143 = Coupling(name = 'GC_1143',
                   value = '(complex(0,1)*I436*complexconjugate(NN13))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I436*sw**2*complexconjugate(NN13))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN11)*complexconjugate(Rd66)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1144 = Coupling(name = 'GC_1144',
                   value = '(complex(0,1)*I436*complexconjugate(NN23))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I436*sw**2*complexconjugate(NN23))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN21)*complexconjugate(Rd66)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1145 = Coupling(name = 'GC_1145',
                   value = '(complex(0,1)*I436*complexconjugate(NN33))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I436*sw**2*complexconjugate(NN33))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN31)*complexconjugate(Rd66)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1146 = Coupling(name = 'GC_1146',
                   value = '(complex(0,1)*I436*complexconjugate(NN43))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I436*sw**2*complexconjugate(NN43))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN41)*complexconjugate(Rd66)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1147 = Coupling(name = 'GC_1147',
                   value = '-((cw*ee*complex(0,1)*NN11*complexconjugate(Rl11))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) - (ee*complex(0,1)*NN12*complexconjugate(Rl11))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN12*sw*complexconjugate(Rl11))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1148 = Coupling(name = 'GC_1148',
                   value = '-((cw*ee*complex(0,1)*NN21*complexconjugate(Rl11))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) - (ee*complex(0,1)*NN22*complexconjugate(Rl11))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN22*sw*complexconjugate(Rl11))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1149 = Coupling(name = 'GC_1149',
                   value = '-((cw*ee*complex(0,1)*NN31*complexconjugate(Rl11))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) - (ee*complex(0,1)*NN32*complexconjugate(Rl11))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN32*sw*complexconjugate(Rl11))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1150 = Coupling(name = 'GC_1150',
                   value = '-((cw*ee*complex(0,1)*NN41*complexconjugate(Rl11))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) - (ee*complex(0,1)*NN42*complexconjugate(Rl11))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN42*sw*complexconjugate(Rl11))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1151 = Coupling(name = 'GC_1151',
                   value = '-((cw*ee*complex(0,1)*NN11*complexconjugate(Rl22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) - (ee*complex(0,1)*NN12*complexconjugate(Rl22))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN12*sw*complexconjugate(Rl22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1152 = Coupling(name = 'GC_1152',
                   value = '-((cw*ee*complex(0,1)*NN21*complexconjugate(Rl22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) - (ee*complex(0,1)*NN22*complexconjugate(Rl22))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN22*sw*complexconjugate(Rl22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1153 = Coupling(name = 'GC_1153',
                   value = '-((cw*ee*complex(0,1)*NN31*complexconjugate(Rl22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) - (ee*complex(0,1)*NN32*complexconjugate(Rl22))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN32*sw*complexconjugate(Rl22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1154 = Coupling(name = 'GC_1154',
                   value = '-((cw*ee*complex(0,1)*NN41*complexconjugate(Rl22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) - (ee*complex(0,1)*NN42*complexconjugate(Rl22))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN42*sw*complexconjugate(Rl22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1155 = Coupling(name = 'GC_1155',
                   value = '(complex(0,1)*I4533*NN13)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I4533*NN13*sw**2)/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN11*complexconjugate(Rl33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN12*complexconjugate(Rl33))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN12*sw*complexconjugate(Rl33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1156 = Coupling(name = 'GC_1156',
                   value = '(complex(0,1)*I4533*NN23)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I4533*NN23*sw**2)/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN21*complexconjugate(Rl33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN22*complexconjugate(Rl33))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN22*sw*complexconjugate(Rl33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1157 = Coupling(name = 'GC_1157',
                   value = '(complex(0,1)*I4533*NN33)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I4533*NN33*sw**2)/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN31*complexconjugate(Rl33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN32*complexconjugate(Rl33))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN32*sw*complexconjugate(Rl33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1158 = Coupling(name = 'GC_1158',
                   value = '(complex(0,1)*I4533*NN43)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I4533*NN43*sw**2)/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN41*complexconjugate(Rl33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN42*complexconjugate(Rl33))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN42*sw*complexconjugate(Rl33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1159 = Coupling(name = 'GC_1159',
                   value = '(complex(0,1)*I4633*complexconjugate(NN13))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I4633*sw**2*complexconjugate(NN13))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN11)*complexconjugate(Rl36)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1160 = Coupling(name = 'GC_1160',
                   value = '(complex(0,1)*I4633*complexconjugate(NN23))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I4633*sw**2*complexconjugate(NN23))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN21)*complexconjugate(Rl36)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1161 = Coupling(name = 'GC_1161',
                   value = '(complex(0,1)*I4633*complexconjugate(NN33))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I4633*sw**2*complexconjugate(NN33))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN31)*complexconjugate(Rl36)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1162 = Coupling(name = 'GC_1162',
                   value = '(complex(0,1)*I4633*complexconjugate(NN43))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I4633*sw**2*complexconjugate(NN43))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN41)*complexconjugate(Rl36)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1163 = Coupling(name = 'GC_1163',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN11)*complexconjugate(Rl44)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1164 = Coupling(name = 'GC_1164',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN21)*complexconjugate(Rl44)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1165 = Coupling(name = 'GC_1165',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN31)*complexconjugate(Rl44)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1166 = Coupling(name = 'GC_1166',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN41)*complexconjugate(Rl44)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1167 = Coupling(name = 'GC_1167',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN11)*complexconjugate(Rl55)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1168 = Coupling(name = 'GC_1168',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN21)*complexconjugate(Rl55)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1169 = Coupling(name = 'GC_1169',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN31)*complexconjugate(Rl55)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1170 = Coupling(name = 'GC_1170',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN41)*complexconjugate(Rl55)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1171 = Coupling(name = 'GC_1171',
                   value = '(complex(0,1)*I4536*NN13)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I4536*NN13*sw**2)/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN11*complexconjugate(Rl63))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN12*complexconjugate(Rl63))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN12*sw*complexconjugate(Rl63))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1172 = Coupling(name = 'GC_1172',
                   value = '(complex(0,1)*I4536*NN23)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I4536*NN23*sw**2)/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN21*complexconjugate(Rl63))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN22*complexconjugate(Rl63))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN22*sw*complexconjugate(Rl63))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1173 = Coupling(name = 'GC_1173',
                   value = '(complex(0,1)*I4536*NN33)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I4536*NN33*sw**2)/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN31*complexconjugate(Rl63))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN32*complexconjugate(Rl63))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN32*sw*complexconjugate(Rl63))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1174 = Coupling(name = 'GC_1174',
                   value = '(complex(0,1)*I4536*NN43)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I4536*NN43*sw**2)/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN41*complexconjugate(Rl63))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN42*complexconjugate(Rl63))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN42*sw*complexconjugate(Rl63))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1175 = Coupling(name = 'GC_1175',
                   value = '(complex(0,1)*I4636*complexconjugate(NN13))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I4636*sw**2*complexconjugate(NN13))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN11)*complexconjugate(Rl66)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1176 = Coupling(name = 'GC_1176',
                   value = '(complex(0,1)*I4636*complexconjugate(NN23))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I4636*sw**2*complexconjugate(NN23))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN21)*complexconjugate(Rl66)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1177 = Coupling(name = 'GC_1177',
                   value = '(complex(0,1)*I4636*complexconjugate(NN33))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I4636*sw**2*complexconjugate(NN33))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN31)*complexconjugate(Rl66)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1178 = Coupling(name = 'GC_1178',
                   value = '(complex(0,1)*I4636*complexconjugate(NN43))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I4636*sw**2*complexconjugate(NN43))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN41)*complexconjugate(Rl66)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1179 = Coupling(name = 'GC_1179',
                   value = '-((cw*ee*complex(0,1)*NN11*complexconjugate(Rn11))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*NN12*complexconjugate(Rn11))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN12*sw*complexconjugate(Rn11))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1180 = Coupling(name = 'GC_1180',
                   value = '-((cw*ee*complex(0,1)*NN21*complexconjugate(Rn11))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*NN22*complexconjugate(Rn11))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN22*sw*complexconjugate(Rn11))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1181 = Coupling(name = 'GC_1181',
                   value = '-((cw*ee*complex(0,1)*NN31*complexconjugate(Rn11))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*NN32*complexconjugate(Rn11))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN32*sw*complexconjugate(Rn11))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1182 = Coupling(name = 'GC_1182',
                   value = '-((cw*ee*complex(0,1)*NN41*complexconjugate(Rn11))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*NN42*complexconjugate(Rn11))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN42*sw*complexconjugate(Rn11))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1183 = Coupling(name = 'GC_1183',
                   value = '-((cw*ee*complex(0,1)*NN11*complexconjugate(Rn22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*NN12*complexconjugate(Rn22))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN12*sw*complexconjugate(Rn22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1184 = Coupling(name = 'GC_1184',
                   value = '-((cw*ee*complex(0,1)*NN21*complexconjugate(Rn22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*NN22*complexconjugate(Rn22))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN22*sw*complexconjugate(Rn22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1185 = Coupling(name = 'GC_1185',
                   value = '-((cw*ee*complex(0,1)*NN31*complexconjugate(Rn22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*NN32*complexconjugate(Rn22))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN32*sw*complexconjugate(Rn22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1186 = Coupling(name = 'GC_1186',
                   value = '-((cw*ee*complex(0,1)*NN41*complexconjugate(Rn22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*NN42*complexconjugate(Rn22))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN42*sw*complexconjugate(Rn22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1187 = Coupling(name = 'GC_1187',
                   value = '-((cw*ee*complex(0,1)*NN11*complexconjugate(Rn33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*NN12*complexconjugate(Rn33))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN12*sw*complexconjugate(Rn33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1188 = Coupling(name = 'GC_1188',
                   value = '-((cw*ee*complex(0,1)*NN21*complexconjugate(Rn33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*NN22*complexconjugate(Rn33))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN22*sw*complexconjugate(Rn33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1189 = Coupling(name = 'GC_1189',
                   value = '-((cw*ee*complex(0,1)*NN31*complexconjugate(Rn33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*NN32*complexconjugate(Rn33))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN32*sw*complexconjugate(Rn33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1190 = Coupling(name = 'GC_1190',
                   value = '-((cw*ee*complex(0,1)*NN41*complexconjugate(Rn33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*NN42*complexconjugate(Rn33))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN42*sw*complexconjugate(Rn33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1191 = Coupling(name = 'GC_1191',
                   value = '-(complex(0,1)*G*complexconjugate(Ru11)*cmath.sqrt(2))',
                   order = {'QCD':1})

GC_1192 = Coupling(name = 'GC_1192',
                   value = '(cw*ee*complex(0,1)*NN11*complexconjugate(Ru11))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN12*complexconjugate(Ru11))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN12*sw*complexconjugate(Ru11))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1193 = Coupling(name = 'GC_1193',
                   value = '(cw*ee*complex(0,1)*NN21*complexconjugate(Ru11))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN22*complexconjugate(Ru11))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN22*sw*complexconjugate(Ru11))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1194 = Coupling(name = 'GC_1194',
                   value = '(cw*ee*complex(0,1)*NN31*complexconjugate(Ru11))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN32*complexconjugate(Ru11))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN32*sw*complexconjugate(Ru11))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1195 = Coupling(name = 'GC_1195',
                   value = '(cw*ee*complex(0,1)*NN41*complexconjugate(Ru11))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN42*complexconjugate(Ru11))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN42*sw*complexconjugate(Ru11))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1196 = Coupling(name = 'GC_1196',
                   value = '-(complex(0,1)*G*complexconjugate(Ru22)*cmath.sqrt(2))',
                   order = {'QCD':1})

GC_1197 = Coupling(name = 'GC_1197',
                   value = '(cw*ee*complex(0,1)*NN11*complexconjugate(Ru22))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN12*complexconjugate(Ru22))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN12*sw*complexconjugate(Ru22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1198 = Coupling(name = 'GC_1198',
                   value = '(cw*ee*complex(0,1)*NN21*complexconjugate(Ru22))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN22*complexconjugate(Ru22))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN22*sw*complexconjugate(Ru22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1199 = Coupling(name = 'GC_1199',
                   value = '(cw*ee*complex(0,1)*NN31*complexconjugate(Ru22))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN32*complexconjugate(Ru22))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN32*sw*complexconjugate(Ru22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1200 = Coupling(name = 'GC_1200',
                   value = '(cw*ee*complex(0,1)*NN41*complexconjugate(Ru22))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN42*complexconjugate(Ru22))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN42*sw*complexconjugate(Ru22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1201 = Coupling(name = 'GC_1201',
                   value = '-(complex(0,1)*G*complexconjugate(Ru33)*cmath.sqrt(2))',
                   order = {'QCD':1})

GC_1202 = Coupling(name = 'GC_1202',
                   value = '(complex(0,1)*I11133*NN14)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I11133*NN14*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN11*complexconjugate(Ru33))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN12*complexconjugate(Ru33))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN12*sw*complexconjugate(Ru33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1203 = Coupling(name = 'GC_1203',
                   value = '(complex(0,1)*I11133*NN24)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I11133*NN24*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN21*complexconjugate(Ru33))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN22*complexconjugate(Ru33))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN22*sw*complexconjugate(Ru33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1204 = Coupling(name = 'GC_1204',
                   value = '(complex(0,1)*I11133*NN34)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I11133*NN34*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN31*complexconjugate(Ru33))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN32*complexconjugate(Ru33))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN32*sw*complexconjugate(Ru33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1205 = Coupling(name = 'GC_1205',
                   value = '(complex(0,1)*I11133*NN44)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I11133*NN44*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN41*complexconjugate(Ru33))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN42*complexconjugate(Ru33))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN42*sw*complexconjugate(Ru33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1206 = Coupling(name = 'GC_1206',
                   value = 'complex(0,1)*G*complexconjugate(Ru36)*cmath.sqrt(2)',
                   order = {'QCD':1})

GC_1207 = Coupling(name = 'GC_1207',
                   value = '(complex(0,1)*I11233*complexconjugate(NN14))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I11233*sw**2*complexconjugate(NN14))/((-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*complexconjugate(NN11)*complexconjugate(Ru36)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1208 = Coupling(name = 'GC_1208',
                   value = '(complex(0,1)*I11233*complexconjugate(NN24))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I11233*sw**2*complexconjugate(NN24))/((-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*complexconjugate(NN21)*complexconjugate(Ru36)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1209 = Coupling(name = 'GC_1209',
                   value = '(complex(0,1)*I11233*complexconjugate(NN34))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I11233*sw**2*complexconjugate(NN34))/((-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*complexconjugate(NN31)*complexconjugate(Ru36)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1210 = Coupling(name = 'GC_1210',
                   value = '(complex(0,1)*I11233*complexconjugate(NN44))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I11233*sw**2*complexconjugate(NN44))/((-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*complexconjugate(NN41)*complexconjugate(Ru36)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1211 = Coupling(name = 'GC_1211',
                   value = 'complex(0,1)*G*complexconjugate(Ru44)*cmath.sqrt(2)',
                   order = {'QCD':1})

GC_1212 = Coupling(name = 'GC_1212',
                   value = '(-2*cw*ee*complex(0,1)*complexconjugate(NN11)*complexconjugate(Ru44)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1213 = Coupling(name = 'GC_1213',
                   value = '(-2*cw*ee*complex(0,1)*complexconjugate(NN21)*complexconjugate(Ru44)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1214 = Coupling(name = 'GC_1214',
                   value = '(-2*cw*ee*complex(0,1)*complexconjugate(NN31)*complexconjugate(Ru44)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1215 = Coupling(name = 'GC_1215',
                   value = '(-2*cw*ee*complex(0,1)*complexconjugate(NN41)*complexconjugate(Ru44)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1216 = Coupling(name = 'GC_1216',
                   value = 'complex(0,1)*G*complexconjugate(Ru55)*cmath.sqrt(2)',
                   order = {'QCD':1})

GC_1217 = Coupling(name = 'GC_1217',
                   value = '(-2*cw*ee*complex(0,1)*complexconjugate(NN11)*complexconjugate(Ru55)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1218 = Coupling(name = 'GC_1218',
                   value = '(-2*cw*ee*complex(0,1)*complexconjugate(NN21)*complexconjugate(Ru55)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1219 = Coupling(name = 'GC_1219',
                   value = '(-2*cw*ee*complex(0,1)*complexconjugate(NN31)*complexconjugate(Ru55)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1220 = Coupling(name = 'GC_1220',
                   value = '(-2*cw*ee*complex(0,1)*complexconjugate(NN41)*complexconjugate(Ru55)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1221 = Coupling(name = 'GC_1221',
                   value = '-(complex(0,1)*G*complexconjugate(Ru63)*cmath.sqrt(2))',
                   order = {'QCD':1})

GC_1222 = Coupling(name = 'GC_1222',
                   value = '(complex(0,1)*I11136*NN14)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I11136*NN14*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN11*complexconjugate(Ru63))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN12*complexconjugate(Ru63))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN12*sw*complexconjugate(Ru63))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1223 = Coupling(name = 'GC_1223',
                   value = '(complex(0,1)*I11136*NN24)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I11136*NN24*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN21*complexconjugate(Ru63))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN22*complexconjugate(Ru63))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN22*sw*complexconjugate(Ru63))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1224 = Coupling(name = 'GC_1224',
                   value = '(complex(0,1)*I11136*NN34)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I11136*NN34*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN31*complexconjugate(Ru63))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN32*complexconjugate(Ru63))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN32*sw*complexconjugate(Ru63))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1225 = Coupling(name = 'GC_1225',
                   value = '(complex(0,1)*I11136*NN44)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I11136*NN44*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN41*complexconjugate(Ru63))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN42*complexconjugate(Ru63))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN42*sw*complexconjugate(Ru63))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1226 = Coupling(name = 'GC_1226',
                   value = 'complex(0,1)*G*complexconjugate(Ru66)*cmath.sqrt(2)',
                   order = {'QCD':1})

GC_1227 = Coupling(name = 'GC_1227',
                   value = '(complex(0,1)*I11236*complexconjugate(NN14))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I11236*sw**2*complexconjugate(NN14))/((-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*complexconjugate(NN11)*complexconjugate(Ru66)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1228 = Coupling(name = 'GC_1228',
                   value = '(complex(0,1)*I11236*complexconjugate(NN24))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I11236*sw**2*complexconjugate(NN24))/((-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*complexconjugate(NN21)*complexconjugate(Ru66)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1229 = Coupling(name = 'GC_1229',
                   value = '(complex(0,1)*I11236*complexconjugate(NN34))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I11236*sw**2*complexconjugate(NN34))/((-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*complexconjugate(NN31)*complexconjugate(Ru66)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1230 = Coupling(name = 'GC_1230',
                   value = '(complex(0,1)*I11236*complexconjugate(NN44))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I11236*sw**2*complexconjugate(NN44))/((-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*complexconjugate(NN41)*complexconjugate(Ru66)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1231 = Coupling(name = 'GC_1231',
                   value = '-((ee*complex(0,1)*I5111*complexconjugate(UU11))/sw)',
                   order = {'QED':1})

GC_1232 = Coupling(name = 'GC_1232',
                   value = '-((ee*complex(0,1)*I5122*complexconjugate(UU11))/sw)',
                   order = {'QED':1})

GC_1233 = Coupling(name = 'GC_1233',
                   value = '-((ee*complex(0,1)*I711*complexconjugate(UU11))/sw)',
                   order = {'QED':1})

GC_1234 = Coupling(name = 'GC_1234',
                   value = '-((ee*complex(0,1)*I722*complexconjugate(UU11))/sw)',
                   order = {'QED':1})

GC_1235 = Coupling(name = 'GC_1235',
                   value = 'complex(0,1)*I19333*complexconjugate(UU12)',
                   order = {'QED':1})

GC_1236 = Coupling(name = 'GC_1236',
                   value = 'complex(0,1)*I19633*complexconjugate(UU12)',
                   order = {'QED':1})

GC_1237 = Coupling(name = 'GC_1237',
                   value = 'complex(0,1)*I19636*complexconjugate(UU12)',
                   order = {'QED':1})

GC_1238 = Coupling(name = 'GC_1238',
                   value = '-((ee*complex(0,1)*I5133*complexconjugate(UU11))/sw) + complex(0,1)*I5233*complexconjugate(UU12)',
                   order = {'QED':1})

GC_1239 = Coupling(name = 'GC_1239',
                   value = '-((ee*complex(0,1)*I5136*complexconjugate(UU11))/sw) + complex(0,1)*I5236*complexconjugate(UU12)',
                   order = {'QED':1})

GC_1240 = Coupling(name = 'GC_1240',
                   value = '-((ee*complex(0,1)*I733*complexconjugate(UU11))/sw) + complex(0,1)*I933*complexconjugate(UU12)',
                   order = {'QED':1})

GC_1241 = Coupling(name = 'GC_1241',
                   value = '-((ee*complex(0,1)*I736*complexconjugate(UU11))/sw) + complex(0,1)*I936*complexconjugate(UU12)',
                   order = {'QED':1})

GC_1242 = Coupling(name = 'GC_1242',
                   value = '-((ee*complex(0,1)*NN12*complexconjugate(UU11))/sw) - (ee*complex(0,1)*NN13*complexconjugate(UU12))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1243 = Coupling(name = 'GC_1243',
                   value = '-((ee*complex(0,1)*NN22*complexconjugate(UU11))/sw) - (ee*complex(0,1)*NN23*complexconjugate(UU12))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1244 = Coupling(name = 'GC_1244',
                   value = '-((ee*complex(0,1)*NN32*complexconjugate(UU11))/sw) - (ee*complex(0,1)*NN33*complexconjugate(UU12))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1245 = Coupling(name = 'GC_1245',
                   value = '-((ee*complex(0,1)*NN42*complexconjugate(UU11))/sw) - (ee*complex(0,1)*NN43*complexconjugate(UU12))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1246 = Coupling(name = 'GC_1246',
                   value = 'ee*complex(0,1)*UU11*complexconjugate(UU11) + ee*complex(0,1)*UU12*complexconjugate(UU12)',
                   order = {'QED':1})

GC_1247 = Coupling(name = 'GC_1247',
                   value = '-((cw*ee*complex(0,1)*UU11*complexconjugate(UU11))/((-1 + sw)*sw*(1 + sw))) + (cw*ee*complex(0,1)*sw*UU11*complexconjugate(UU11))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*UU12*complexconjugate(UU12))/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*sw*UU12*complexconjugate(UU12))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1248 = Coupling(name = 'GC_1248',
                   value = 'ee*complex(0,1)*UU21*complexconjugate(UU11) + ee*complex(0,1)*UU22*complexconjugate(UU12)',
                   order = {'QED':1})

GC_1249 = Coupling(name = 'GC_1249',
                   value = '-((cw*ee*complex(0,1)*UU21*complexconjugate(UU11))/((-1 + sw)*sw*(1 + sw))) + (cw*ee*complex(0,1)*sw*UU21*complexconjugate(UU11))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*UU22*complexconjugate(UU12))/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*sw*UU22*complexconjugate(UU12))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1250 = Coupling(name = 'GC_1250',
                   value = '-((ee*complex(0,1)*I5111*complexconjugate(UU21))/sw)',
                   order = {'QED':1})

GC_1251 = Coupling(name = 'GC_1251',
                   value = '-((ee*complex(0,1)*I5122*complexconjugate(UU21))/sw)',
                   order = {'QED':1})

GC_1252 = Coupling(name = 'GC_1252',
                   value = '-((ee*complex(0,1)*I711*complexconjugate(UU21))/sw)',
                   order = {'QED':1})

GC_1253 = Coupling(name = 'GC_1253',
                   value = '-((ee*complex(0,1)*I722*complexconjugate(UU21))/sw)',
                   order = {'QED':1})

GC_1254 = Coupling(name = 'GC_1254',
                   value = 'complex(0,1)*I19333*complexconjugate(UU22)',
                   order = {'QED':1})

GC_1255 = Coupling(name = 'GC_1255',
                   value = 'complex(0,1)*I19633*complexconjugate(UU22)',
                   order = {'QED':1})

GC_1256 = Coupling(name = 'GC_1256',
                   value = 'complex(0,1)*I19636*complexconjugate(UU22)',
                   order = {'QED':1})

GC_1257 = Coupling(name = 'GC_1257',
                   value = '-((ee*complex(0,1)*I5133*complexconjugate(UU21))/sw) + complex(0,1)*I5233*complexconjugate(UU22)',
                   order = {'QED':1})

GC_1258 = Coupling(name = 'GC_1258',
                   value = '-((ee*complex(0,1)*I5136*complexconjugate(UU21))/sw) + complex(0,1)*I5236*complexconjugate(UU22)',
                   order = {'QED':1})

GC_1259 = Coupling(name = 'GC_1259',
                   value = '-((ee*complex(0,1)*I733*complexconjugate(UU21))/sw) + complex(0,1)*I933*complexconjugate(UU22)',
                   order = {'QED':1})

GC_1260 = Coupling(name = 'GC_1260',
                   value = '-((ee*complex(0,1)*I736*complexconjugate(UU21))/sw) + complex(0,1)*I936*complexconjugate(UU22)',
                   order = {'QED':1})

GC_1261 = Coupling(name = 'GC_1261',
                   value = '-((ee*complex(0,1)*NN12*complexconjugate(UU21))/sw) - (ee*complex(0,1)*NN13*complexconjugate(UU22))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1262 = Coupling(name = 'GC_1262',
                   value = '-((ee*complex(0,1)*NN22*complexconjugate(UU21))/sw) - (ee*complex(0,1)*NN23*complexconjugate(UU22))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1263 = Coupling(name = 'GC_1263',
                   value = '-((ee*complex(0,1)*NN32*complexconjugate(UU21))/sw) - (ee*complex(0,1)*NN33*complexconjugate(UU22))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1264 = Coupling(name = 'GC_1264',
                   value = '-((ee*complex(0,1)*NN42*complexconjugate(UU21))/sw) - (ee*complex(0,1)*NN43*complexconjugate(UU22))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1265 = Coupling(name = 'GC_1265',
                   value = 'ee*complex(0,1)*UU11*complexconjugate(UU21) + ee*complex(0,1)*UU12*complexconjugate(UU22)',
                   order = {'QED':1})

GC_1266 = Coupling(name = 'GC_1266',
                   value = '-((cw*ee*complex(0,1)*UU11*complexconjugate(UU21))/((-1 + sw)*sw*(1 + sw))) + (cw*ee*complex(0,1)*sw*UU11*complexconjugate(UU21))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*UU12*complexconjugate(UU22))/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*sw*UU12*complexconjugate(UU22))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1267 = Coupling(name = 'GC_1267',
                   value = 'ee*complex(0,1)*UU21*complexconjugate(UU21) + ee*complex(0,1)*UU22*complexconjugate(UU22)',
                   order = {'QED':1})

GC_1268 = Coupling(name = 'GC_1268',
                   value = '-((cw*ee*complex(0,1)*UU21*complexconjugate(UU21))/((-1 + sw)*sw*(1 + sw))) + (cw*ee*complex(0,1)*sw*UU21*complexconjugate(UU21))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*UU22*complexconjugate(UU22))/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*sw*UU22*complexconjugate(UU22))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1269 = Coupling(name = 'GC_1269',
                   value = '-((ee*complex(0,1)*I13311*complexconjugate(VV11))/sw)',
                   order = {'QED':1})

GC_1270 = Coupling(name = 'GC_1270',
                   value = '-((ee*complex(0,1)*I13322*complexconjugate(VV11))/sw)',
                   order = {'QED':1})

GC_1271 = Coupling(name = 'GC_1271',
                   value = '-((ee*complex(0,1)*I9611*complexconjugate(VV11))/sw)',
                   order = {'QED':1})

GC_1272 = Coupling(name = 'GC_1272',
                   value = '-((ee*complex(0,1)*I9622*complexconjugate(VV11))/sw)',
                   order = {'QED':1})

GC_1273 = Coupling(name = 'GC_1273',
                   value = '-((ee*complex(0,1)*I9633*complexconjugate(VV11))/sw)',
                   order = {'QED':1})

GC_1274 = Coupling(name = 'GC_1274',
                   value = 'complex(0,1)*I18933*complexconjugate(VV12)',
                   order = {'QED':1})

GC_1275 = Coupling(name = 'GC_1275',
                   value = 'complex(0,1)*I18936*complexconjugate(VV12)',
                   order = {'QED':1})

GC_1276 = Coupling(name = 'GC_1276',
                   value = '-((ee*complex(0,1)*I13333*complexconjugate(VV11))/sw) + complex(0,1)*I13533*complexconjugate(VV12)',
                   order = {'QED':1})

GC_1277 = Coupling(name = 'GC_1277',
                   value = '-((ee*complex(0,1)*I13336*complexconjugate(VV11))/sw) + complex(0,1)*I13536*complexconjugate(VV12)',
                   order = {'QED':1})

GC_1278 = Coupling(name = 'GC_1278',
                   value = '-((ee*complex(0,1)*NN12*complexconjugate(VV11))/sw) + (ee*complex(0,1)*NN14*complexconjugate(VV12))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1279 = Coupling(name = 'GC_1279',
                   value = '-((ee*complex(0,1)*NN22*complexconjugate(VV11))/sw) + (ee*complex(0,1)*NN24*complexconjugate(VV12))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1280 = Coupling(name = 'GC_1280',
                   value = '-((ee*complex(0,1)*NN32*complexconjugate(VV11))/sw) + (ee*complex(0,1)*NN34*complexconjugate(VV12))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1281 = Coupling(name = 'GC_1281',
                   value = '-((ee*complex(0,1)*NN42*complexconjugate(VV11))/sw) + (ee*complex(0,1)*NN44*complexconjugate(VV12))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1282 = Coupling(name = 'GC_1282',
                   value = 'ee*complex(0,1)*VV11*complexconjugate(VV11) + ee*complex(0,1)*VV12*complexconjugate(VV12)',
                   order = {'QED':1})

GC_1283 = Coupling(name = 'GC_1283',
                   value = '-((cw*ee*complex(0,1)*VV11*complexconjugate(VV11))/((-1 + sw)*sw*(1 + sw))) + (cw*ee*complex(0,1)*sw*VV11*complexconjugate(VV11))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*VV12*complexconjugate(VV12))/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*sw*VV12*complexconjugate(VV12))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1284 = Coupling(name = 'GC_1284',
                   value = 'ee*complex(0,1)*VV21*complexconjugate(VV11) + ee*complex(0,1)*VV22*complexconjugate(VV12)',
                   order = {'QED':1})

GC_1285 = Coupling(name = 'GC_1285',
                   value = '-((cw*ee*complex(0,1)*VV21*complexconjugate(VV11))/((-1 + sw)*sw*(1 + sw))) + (cw*ee*complex(0,1)*sw*VV21*complexconjugate(VV11))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*VV22*complexconjugate(VV12))/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*sw*VV22*complexconjugate(VV12))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1286 = Coupling(name = 'GC_1286',
                   value = '-((ee*complex(0,1)*I13311*complexconjugate(VV21))/sw)',
                   order = {'QED':1})

GC_1287 = Coupling(name = 'GC_1287',
                   value = '-((ee*complex(0,1)*I13322*complexconjugate(VV21))/sw)',
                   order = {'QED':1})

GC_1288 = Coupling(name = 'GC_1288',
                   value = '-((ee*complex(0,1)*I9611*complexconjugate(VV21))/sw)',
                   order = {'QED':1})

GC_1289 = Coupling(name = 'GC_1289',
                   value = '-((ee*complex(0,1)*I9622*complexconjugate(VV21))/sw)',
                   order = {'QED':1})

GC_1290 = Coupling(name = 'GC_1290',
                   value = '-((ee*complex(0,1)*I9633*complexconjugate(VV21))/sw)',
                   order = {'QED':1})

GC_1291 = Coupling(name = 'GC_1291',
                   value = 'complex(0,1)*I18933*complexconjugate(VV22)',
                   order = {'QED':1})

GC_1292 = Coupling(name = 'GC_1292',
                   value = 'complex(0,1)*I18936*complexconjugate(VV22)',
                   order = {'QED':1})

GC_1293 = Coupling(name = 'GC_1293',
                   value = '-((ee*complex(0,1)*I13333*complexconjugate(VV21))/sw) + complex(0,1)*I13533*complexconjugate(VV22)',
                   order = {'QED':1})

GC_1294 = Coupling(name = 'GC_1294',
                   value = '-((ee*complex(0,1)*I13336*complexconjugate(VV21))/sw) + complex(0,1)*I13536*complexconjugate(VV22)',
                   order = {'QED':1})

GC_1295 = Coupling(name = 'GC_1295',
                   value = '-((ee*complex(0,1)*NN12*complexconjugate(VV21))/sw) + (ee*complex(0,1)*NN14*complexconjugate(VV22))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1296 = Coupling(name = 'GC_1296',
                   value = '-((ee*complex(0,1)*NN22*complexconjugate(VV21))/sw) + (ee*complex(0,1)*NN24*complexconjugate(VV22))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1297 = Coupling(name = 'GC_1297',
                   value = '-((ee*complex(0,1)*NN32*complexconjugate(VV21))/sw) + (ee*complex(0,1)*NN34*complexconjugate(VV22))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1298 = Coupling(name = 'GC_1298',
                   value = '-((ee*complex(0,1)*NN42*complexconjugate(VV21))/sw) + (ee*complex(0,1)*NN44*complexconjugate(VV22))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1299 = Coupling(name = 'GC_1299',
                   value = 'ee*complex(0,1)*VV11*complexconjugate(VV21) + ee*complex(0,1)*VV12*complexconjugate(VV22)',
                   order = {'QED':1})

GC_1300 = Coupling(name = 'GC_1300',
                   value = '-((cw*ee*complex(0,1)*VV11*complexconjugate(VV21))/((-1 + sw)*sw*(1 + sw))) + (cw*ee*complex(0,1)*sw*VV11*complexconjugate(VV21))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*VV12*complexconjugate(VV22))/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*sw*VV12*complexconjugate(VV22))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1301 = Coupling(name = 'GC_1301',
                   value = 'ee*complex(0,1)*VV21*complexconjugate(VV21) + ee*complex(0,1)*VV22*complexconjugate(VV22)',
                   order = {'QED':1})

GC_1302 = Coupling(name = 'GC_1302',
                   value = '-((cw*ee*complex(0,1)*VV21*complexconjugate(VV21))/((-1 + sw)*sw*(1 + sw))) + (cw*ee*complex(0,1)*sw*VV21*complexconjugate(VV21))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*VV22*complexconjugate(VV22))/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*sw*VV22*complexconjugate(VV22))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1303 = Coupling(name = 'GC_1303',
                   value = '-((complex(0,1)*yd33*cmath.cos(alp))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1304 = Coupling(name = 'GC_1304',
                   value = '-((complex(0,1)*ye33*cmath.cos(alp))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1305 = Coupling(name = 'GC_1305',
                   value = '-((complex(0,1)*yu33*cmath.cos(alp))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1306 = Coupling(name = 'GC_1306',
                   value = '-((complex(0,1)*complexconjugate(yd33)*cmath.cos(alp))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1307 = Coupling(name = 'GC_1307',
                   value = '-((complex(0,1)*complexconjugate(ye33)*cmath.cos(alp))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1308 = Coupling(name = 'GC_1308',
                   value = '-((complex(0,1)*complexconjugate(yu33)*cmath.cos(alp))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1309 = Coupling(name = 'GC_1309',
                   value = 'complex(0,1)*I133*cmath.cos(beta)',
                   order = {'QED':1})

GC_1310 = Coupling(name = 'GC_1310',
                   value = 'complex(0,1)*I4333*cmath.cos(beta)',
                   order = {'QED':1})

GC_1311 = Coupling(name = 'GC_1311',
                   value = '(yu33*cmath.cos(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1312 = Coupling(name = 'GC_1312',
                   value = '-((complexconjugate(yu33)*cmath.cos(beta))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1313 = Coupling(name = 'GC_1313',
                   value = '(ee*complex(0,1)*NN14*VV11*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN14*sw*VV11*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN11*VV12*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN12*VV12*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN12*sw*VV12*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1314 = Coupling(name = 'GC_1314',
                   value = '(ee*complex(0,1)*NN24*VV11*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN24*sw*VV11*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN21*VV12*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN22*VV12*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN22*sw*VV12*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1315 = Coupling(name = 'GC_1315',
                   value = '(ee*complex(0,1)*NN34*VV11*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN34*sw*VV11*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN31*VV12*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN32*VV12*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN32*sw*VV12*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1316 = Coupling(name = 'GC_1316',
                   value = '(ee*complex(0,1)*NN44*VV11*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN44*sw*VV11*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN41*VV12*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN42*VV12*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN42*sw*VV12*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1317 = Coupling(name = 'GC_1317',
                   value = '(ee*complex(0,1)*NN14*VV21*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN14*sw*VV21*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN11*VV22*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN12*VV22*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN12*sw*VV22*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1318 = Coupling(name = 'GC_1318',
                   value = '(ee*complex(0,1)*NN24*VV21*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN24*sw*VV21*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN21*VV22*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN22*VV22*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN22*sw*VV22*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1319 = Coupling(name = 'GC_1319',
                   value = '(ee*complex(0,1)*NN34*VV21*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN34*sw*VV21*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN31*VV22*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN32*VV22*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN32*sw*VV22*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1320 = Coupling(name = 'GC_1320',
                   value = '(ee*complex(0,1)*NN44*VV21*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN44*sw*VV21*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN41*VV22*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN42*VV22*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN42*sw*VV22*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1321 = Coupling(name = 'GC_1321',
                   value = '(ee*complex(0,1)*complexconjugate(NN14)*complexconjugate(VV11)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN14)*complexconjugate(VV11)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN11)*complexconjugate(VV12)*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*complexconjugate(NN12)*complexconjugate(VV12)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*sw*complexconjugate(NN12)*complexconjugate(VV12)*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1322 = Coupling(name = 'GC_1322',
                   value = '(ee*complex(0,1)*complexconjugate(NN24)*complexconjugate(VV11)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN24)*complexconjugate(VV11)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN21)*complexconjugate(VV12)*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*complexconjugate(NN22)*complexconjugate(VV12)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*sw*complexconjugate(NN22)*complexconjugate(VV12)*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1323 = Coupling(name = 'GC_1323',
                   value = '(ee*complex(0,1)*complexconjugate(NN34)*complexconjugate(VV11)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN34)*complexconjugate(VV11)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN31)*complexconjugate(VV12)*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*complexconjugate(NN32)*complexconjugate(VV12)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*sw*complexconjugate(NN32)*complexconjugate(VV12)*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1324 = Coupling(name = 'GC_1324',
                   value = '(ee*complex(0,1)*complexconjugate(NN44)*complexconjugate(VV11)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN44)*complexconjugate(VV11)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN41)*complexconjugate(VV12)*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*complexconjugate(NN42)*complexconjugate(VV12)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*sw*complexconjugate(NN42)*complexconjugate(VV12)*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1325 = Coupling(name = 'GC_1325',
                   value = '(ee*complex(0,1)*complexconjugate(NN14)*complexconjugate(VV21)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN14)*complexconjugate(VV21)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN11)*complexconjugate(VV22)*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*complexconjugate(NN12)*complexconjugate(VV22)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*sw*complexconjugate(NN12)*complexconjugate(VV22)*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1326 = Coupling(name = 'GC_1326',
                   value = '(ee*complex(0,1)*complexconjugate(NN24)*complexconjugate(VV21)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN24)*complexconjugate(VV21)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN21)*complexconjugate(VV22)*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*complexconjugate(NN22)*complexconjugate(VV22)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*sw*complexconjugate(NN22)*complexconjugate(VV22)*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1327 = Coupling(name = 'GC_1327',
                   value = '(ee*complex(0,1)*complexconjugate(NN34)*complexconjugate(VV21)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN34)*complexconjugate(VV21)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN31)*complexconjugate(VV22)*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*complexconjugate(NN32)*complexconjugate(VV22)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*sw*complexconjugate(NN32)*complexconjugate(VV22)*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1328 = Coupling(name = 'GC_1328',
                   value = '(ee*complex(0,1)*complexconjugate(NN44)*complexconjugate(VV21)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN44)*complexconjugate(VV21)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN41)*complexconjugate(VV22)*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*complexconjugate(NN42)*complexconjugate(VV22)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*sw*complexconjugate(NN42)*complexconjugate(VV22)*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1329 = Coupling(name = 'GC_1329',
                   value = '(complex(0,1)*yd33*cmath.sin(alp))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1330 = Coupling(name = 'GC_1330',
                   value = '(complex(0,1)*ye33*cmath.sin(alp))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1331 = Coupling(name = 'GC_1331',
                   value = '-((complex(0,1)*yu33*cmath.sin(alp))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1332 = Coupling(name = 'GC_1332',
                   value = '(complex(0,1)*complexconjugate(yd33)*cmath.sin(alp))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1333 = Coupling(name = 'GC_1333',
                   value = '(complex(0,1)*complexconjugate(ye33)*cmath.sin(alp))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1334 = Coupling(name = 'GC_1334',
                   value = '-((complex(0,1)*complexconjugate(yu33)*cmath.sin(alp))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1335 = Coupling(name = 'GC_1335',
                   value = '(ee**2*complex(0,1)*I1344*cmath.cos(alp)*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1336 = Coupling(name = 'GC_1336',
                   value = '(ee**2*complex(0,1)*I1355*cmath.cos(alp)*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1337 = Coupling(name = 'GC_1337',
                   value = '(-2*ee**2*complex(0,1)*I14944*cmath.cos(alp)*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1338 = Coupling(name = 'GC_1338',
                   value = '(-2*ee**2*complex(0,1)*I14955*cmath.cos(alp)*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1339 = Coupling(name = 'GC_1339',
                   value = '(ee**2*complex(0,1)*I5444*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1340 = Coupling(name = 'GC_1340',
                   value = '(ee**2*complex(0,1)*I5455*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1341 = Coupling(name = 'GC_1341',
                   value = '-(ee**2*complex(0,1)*cmath.cos(alp)*cmath.sin(alp))/(2.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1342 = Coupling(name = 'GC_1342',
                   value = '(cw*ee*complex(0,1)*NN11*NN14*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN12*NN14*cmath.cos(alp))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN12*NN14*sw*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN11*NN13*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN12*NN13*cmath.sin(alp))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN12*NN13*sw*cmath.sin(alp))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1343 = Coupling(name = 'GC_1343',
                   value = '-((cw*ee*complex(0,1)*NN11*NN13*cmath.cos(alp))/((-1 + sw)*(1 + sw))) + (ee*complex(0,1)*NN12*NN13*cmath.cos(alp))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN12*NN13*sw*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN11*NN14*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN12*NN14*cmath.sin(alp))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN12*NN14*sw*cmath.sin(alp))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1344 = Coupling(name = 'GC_1344',
                   value = '(cw*ee*complex(0,1)*NN14*NN21*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN11*NN24*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN14*NN22*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN12*NN24*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN14*NN22*sw*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN12*NN24*sw*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN13*NN21*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN11*NN23*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN13*NN22*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN12*NN23*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN13*NN22*sw*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN12*NN23*sw*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1345 = Coupling(name = 'GC_1345',
                   value = '(cw*ee*complex(0,1)*NN21*NN24*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN22*NN24*cmath.cos(alp))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN22*NN24*sw*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN21*NN23*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN22*NN23*cmath.sin(alp))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN22*NN23*sw*cmath.sin(alp))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1346 = Coupling(name = 'GC_1346',
                   value = '-(cw*ee*complex(0,1)*NN13*NN21*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN11*NN23*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN13*NN22*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN12*NN23*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN13*NN22*sw*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN12*NN23*sw*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN14*NN21*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN11*NN24*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN14*NN22*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN12*NN24*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN14*NN22*sw*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN12*NN24*sw*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1347 = Coupling(name = 'GC_1347',
                   value = '-((cw*ee*complex(0,1)*NN21*NN23*cmath.cos(alp))/((-1 + sw)*(1 + sw))) + (ee*complex(0,1)*NN22*NN23*cmath.cos(alp))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN22*NN23*sw*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN21*NN24*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN22*NN24*cmath.sin(alp))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN22*NN24*sw*cmath.sin(alp))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1348 = Coupling(name = 'GC_1348',
                   value = '(cw*ee*complex(0,1)*NN14*NN31*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN11*NN34*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN14*NN32*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN12*NN34*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN14*NN32*sw*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN12*NN34*sw*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN13*NN31*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN11*NN33*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN13*NN32*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN12*NN33*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN13*NN32*sw*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN12*NN33*sw*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1349 = Coupling(name = 'GC_1349',
                   value = '(cw*ee*complex(0,1)*NN24*NN31*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN21*NN34*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN24*NN32*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN22*NN34*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN24*NN32*sw*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN22*NN34*sw*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN23*NN31*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN21*NN33*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN23*NN32*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN22*NN33*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN23*NN32*sw*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN22*NN33*sw*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1350 = Coupling(name = 'GC_1350',
                   value = '(cw*ee*complex(0,1)*NN31*NN34*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN32*NN34*cmath.cos(alp))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN32*NN34*sw*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN31*NN33*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN32*NN33*cmath.sin(alp))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN32*NN33*sw*cmath.sin(alp))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1351 = Coupling(name = 'GC_1351',
                   value = '-(cw*ee*complex(0,1)*NN13*NN31*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN11*NN33*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN13*NN32*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN12*NN33*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN13*NN32*sw*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN12*NN33*sw*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN14*NN31*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN11*NN34*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN14*NN32*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN12*NN34*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN14*NN32*sw*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN12*NN34*sw*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1352 = Coupling(name = 'GC_1352',
                   value = '-(cw*ee*complex(0,1)*NN23*NN31*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN21*NN33*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN23*NN32*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN22*NN33*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN23*NN32*sw*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN22*NN33*sw*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN24*NN31*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN21*NN34*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN24*NN32*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN22*NN34*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN24*NN32*sw*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN22*NN34*sw*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1353 = Coupling(name = 'GC_1353',
                   value = '-((cw*ee*complex(0,1)*NN31*NN33*cmath.cos(alp))/((-1 + sw)*(1 + sw))) + (ee*complex(0,1)*NN32*NN33*cmath.cos(alp))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN32*NN33*sw*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN31*NN34*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN32*NN34*cmath.sin(alp))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN32*NN34*sw*cmath.sin(alp))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1354 = Coupling(name = 'GC_1354',
                   value = '(cw*ee*complex(0,1)*NN14*NN41*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN11*NN44*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN14*NN42*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN12*NN44*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN14*NN42*sw*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN12*NN44*sw*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN13*NN41*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN11*NN43*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN13*NN42*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN12*NN43*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN13*NN42*sw*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN12*NN43*sw*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1355 = Coupling(name = 'GC_1355',
                   value = '(cw*ee*complex(0,1)*NN24*NN41*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN21*NN44*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN24*NN42*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN22*NN44*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN24*NN42*sw*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN22*NN44*sw*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN23*NN41*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN21*NN43*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN23*NN42*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN22*NN43*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN23*NN42*sw*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN22*NN43*sw*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1356 = Coupling(name = 'GC_1356',
                   value = '(cw*ee*complex(0,1)*NN34*NN41*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN31*NN44*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN34*NN42*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN32*NN44*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN34*NN42*sw*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN32*NN44*sw*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN33*NN41*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN31*NN43*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN33*NN42*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN32*NN43*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN33*NN42*sw*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN32*NN43*sw*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1357 = Coupling(name = 'GC_1357',
                   value = '(cw*ee*complex(0,1)*NN41*NN44*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN42*NN44*cmath.cos(alp))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN42*NN44*sw*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN41*NN43*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN42*NN43*cmath.sin(alp))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN42*NN43*sw*cmath.sin(alp))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1358 = Coupling(name = 'GC_1358',
                   value = '-(cw*ee*complex(0,1)*NN13*NN41*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN11*NN43*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN13*NN42*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN12*NN43*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN13*NN42*sw*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN12*NN43*sw*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN14*NN41*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN11*NN44*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN14*NN42*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN12*NN44*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN14*NN42*sw*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN12*NN44*sw*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1359 = Coupling(name = 'GC_1359',
                   value = '-(cw*ee*complex(0,1)*NN23*NN41*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN21*NN43*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN23*NN42*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN22*NN43*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN23*NN42*sw*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN22*NN43*sw*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN24*NN41*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN21*NN44*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN24*NN42*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN22*NN44*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN24*NN42*sw*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN22*NN44*sw*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1360 = Coupling(name = 'GC_1360',
                   value = '-(cw*ee*complex(0,1)*NN33*NN41*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN31*NN43*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN33*NN42*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN32*NN43*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN33*NN42*sw*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN32*NN43*sw*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN34*NN41*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN31*NN44*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN34*NN42*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN32*NN44*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN34*NN42*sw*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN32*NN44*sw*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1361 = Coupling(name = 'GC_1361',
                   value = '-((cw*ee*complex(0,1)*NN41*NN43*cmath.cos(alp))/((-1 + sw)*(1 + sw))) + (ee*complex(0,1)*NN42*NN43*cmath.cos(alp))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN42*NN43*sw*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN41*NN44*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN42*NN44*cmath.sin(alp))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN42*NN44*sw*cmath.sin(alp))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1362 = Coupling(name = 'GC_1362',
                   value = '(ee**2*complex(0,1)*vu*cmath.cos(alp))/(2.*sw**2) - (ee**2*complex(0,1)*vd*cmath.sin(alp))/(2.*sw**2)',
                   order = {'QED':1})

GC_1363 = Coupling(name = 'GC_1363',
                   value = '-(ee**2*complex(0,1)*I11444*vu*cmath.cos(alp))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I11444*vd*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1364 = Coupling(name = 'GC_1364',
                   value = '-(ee**2*complex(0,1)*I11455*vu*cmath.cos(alp))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I11455*vd*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1365 = Coupling(name = 'GC_1365',
                   value = '(ee**2*complex(0,1)*I4844*vu*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I4844*vd*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1366 = Coupling(name = 'GC_1366',
                   value = '(ee**2*complex(0,1)*I4855*vu*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I4855*vd*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1367 = Coupling(name = 'GC_1367',
                   value = '(ee**2*complex(0,1)*I644*vu*cmath.cos(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I644*vd*cmath.sin(alp))/(6.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1368 = Coupling(name = 'GC_1368',
                   value = '(ee**2*complex(0,1)*I655*vu*cmath.cos(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I655*vd*cmath.sin(alp))/(6.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1369 = Coupling(name = 'GC_1369',
                   value = '-(ee**2*complex(0,1)*vu*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*vd*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':1})

GC_1370 = Coupling(name = 'GC_1370',
                   value = '-(ee**2*complex(0,1)*vu*cmath.cos(alp))/(2.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*vd*cmath.sin(alp))/(2.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':1})

GC_1371 = Coupling(name = 'GC_1371',
                   value = '(ee**2*complex(0,1)*I11311*vu*cmath.cos(alp))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I11311*vu*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I11311*vd*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I11311*vd*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':1})

GC_1372 = Coupling(name = 'GC_1372',
                   value = '(ee**2*complex(0,1)*I11322*vu*cmath.cos(alp))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I11322*vu*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I11322*vd*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I11322*vd*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':1})

GC_1373 = Coupling(name = 'GC_1373',
                   value = '-(ee**2*complex(0,1)*I4711*vu*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I4711*vu*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*I4711*vd*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I4711*vd*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':1})

GC_1374 = Coupling(name = 'GC_1374',
                   value = '-(ee**2*complex(0,1)*I4722*vu*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I4722*vu*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*I4722*vd*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I4722*vd*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':1})

GC_1375 = Coupling(name = 'GC_1375',
                   value = '-(ee**2*complex(0,1)*I511*vu*cmath.cos(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I511*vu*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*I511*vd*cmath.sin(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I511*vd*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':1})

GC_1376 = Coupling(name = 'GC_1376',
                   value = '-(ee**2*complex(0,1)*I522*vu*cmath.cos(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I522*vu*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*I522*vd*cmath.sin(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I522*vd*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':1})

GC_1377 = Coupling(name = 'GC_1377',
                   value = '-(ee**2*complex(0,1)*I533*vu*cmath.cos(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I633*vu*cmath.cos(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I533*vu*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I1533*MUH*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I1533*MUH*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I1733*complexconjugate(MUH)*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I1733*sw**2*complexconjugate(MUH)*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I1833*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I1933*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I533*vd*cmath.sin(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I633*vd*cmath.sin(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I533*vd*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*I1833*sw**2*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I1933*sw**2*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I1433*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I1633*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I1433*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I1633*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1378 = Coupling(name = 'GC_1378',
                   value = '-(ee**2*complex(0,1)*I536*vu*cmath.cos(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I636*vu*cmath.cos(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I536*vu*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I1536*MUH*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I1536*MUH*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I1736*complexconjugate(MUH)*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I1736*sw**2*complexconjugate(MUH)*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I1836*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I1936*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I536*vd*cmath.sin(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I636*vd*cmath.sin(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I536*vd*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*I1836*sw**2*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I1936*sw**2*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I1436*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I1636*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I1436*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I1636*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1379 = Coupling(name = 'GC_1379',
                   value = '-(ee**2*complex(0,1)*I563*vu*cmath.cos(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I663*vu*cmath.cos(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I563*vu*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I1563*MUH*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I1563*MUH*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I1763*complexconjugate(MUH)*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I1763*sw**2*complexconjugate(MUH)*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I1863*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I1963*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I563*vd*cmath.sin(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I663*vd*cmath.sin(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I563*vd*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*I1863*sw**2*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I1963*sw**2*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I1463*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I1663*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I1463*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I1663*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1380 = Coupling(name = 'GC_1380',
                   value = '-(ee**2*complex(0,1)*I566*vu*cmath.cos(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I666*vu*cmath.cos(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I566*vu*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I1566*MUH*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I1566*MUH*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I1766*complexconjugate(MUH)*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I1766*sw**2*complexconjugate(MUH)*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I1866*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I1966*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I566*vd*cmath.sin(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I666*vd*cmath.sin(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I566*vd*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*I1866*sw**2*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I1966*sw**2*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I1466*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I1666*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I1466*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I1666*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1381 = Coupling(name = 'GC_1381',
                   value = '-(ee**2*complex(0,1)*I4733*vu*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I4833*vu*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I4733*vu*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I5633*MUH*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I5633*MUH*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I5933*complexconjugate(MUH)*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I5933*sw**2*complexconjugate(MUH)*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee**2*complex(0,1)*I4733*vd*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I4833*vd*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I5833*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I6033*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I4733*vd*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*I5833*sw**2*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I6033*sw**2*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I5533*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I5733*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I5533*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I5733*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1382 = Coupling(name = 'GC_1382',
                   value = '-(ee**2*complex(0,1)*I4736*vu*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I4836*vu*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I4736*vu*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I5636*MUH*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I5636*MUH*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I5936*complexconjugate(MUH)*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I5936*sw**2*complexconjugate(MUH)*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee**2*complex(0,1)*I4736*vd*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I4836*vd*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I5836*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I6036*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I4736*vd*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*I5836*sw**2*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I6036*sw**2*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I5536*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I5736*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I5536*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I5736*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1383 = Coupling(name = 'GC_1383',
                   value = '-(ee**2*complex(0,1)*I4763*vu*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I4863*vu*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I4763*vu*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I5663*MUH*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I5663*MUH*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I5963*complexconjugate(MUH)*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I5963*sw**2*complexconjugate(MUH)*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee**2*complex(0,1)*I4763*vd*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I4863*vd*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I5863*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I6063*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I4763*vd*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*I5863*sw**2*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I6063*sw**2*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I5563*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I5763*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I5563*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I5763*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1384 = Coupling(name = 'GC_1384',
                   value = '-(ee**2*complex(0,1)*I4766*vu*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I4866*vu*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I4766*vu*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I5666*MUH*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I5666*MUH*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I5966*complexconjugate(MUH)*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I5966*sw**2*complexconjugate(MUH)*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee**2*complex(0,1)*I4766*vd*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I4866*vd*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I5866*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I6066*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I4766*vd*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*I5866*sw**2*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I6066*sw**2*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I5566*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I5766*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I5566*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I5766*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1385 = Coupling(name = 'GC_1385',
                   value = '(ee**2*complex(0,1)*vd*cmath.cos(alp))/(2.*sw**2) + (ee**2*complex(0,1)*vu*cmath.sin(alp))/(2.*sw**2)',
                   order = {'QED':1})

GC_1386 = Coupling(name = 'GC_1386',
                   value = '(ee**2*complex(0,1)*I11444*vd*cmath.cos(alp))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I11444*vu*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1387 = Coupling(name = 'GC_1387',
                   value = '(ee**2*complex(0,1)*I11455*vd*cmath.cos(alp))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I11455*vu*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1388 = Coupling(name = 'GC_1388',
                   value = '-(ee**2*complex(0,1)*I4844*vd*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I4844*vu*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1389 = Coupling(name = 'GC_1389',
                   value = '-(ee**2*complex(0,1)*I4855*vd*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I4855*vu*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1390 = Coupling(name = 'GC_1390',
                   value = '-(ee**2*complex(0,1)*I644*vd*cmath.cos(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I644*vu*cmath.sin(alp))/(6.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1391 = Coupling(name = 'GC_1391',
                   value = '-(ee**2*complex(0,1)*I655*vd*cmath.cos(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I655*vu*cmath.sin(alp))/(6.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1392 = Coupling(name = 'GC_1392',
                   value = '(ee**2*complex(0,1)*vd*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*vu*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':1})

GC_1393 = Coupling(name = 'GC_1393',
                   value = '-(ee**2*complex(0,1)*vd*cmath.cos(alp))/(2.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*vu*cmath.sin(alp))/(2.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':1})

GC_1394 = Coupling(name = 'GC_1394',
                   value = '-(ee**2*complex(0,1)*I11311*vd*cmath.cos(alp))/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I11311*vd*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I11311*vu*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I11311*vu*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':1})

GC_1395 = Coupling(name = 'GC_1395',
                   value = '-(ee**2*complex(0,1)*I11322*vd*cmath.cos(alp))/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I11322*vd*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I11322*vu*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I11322*vu*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':1})

GC_1396 = Coupling(name = 'GC_1396',
                   value = '(ee**2*complex(0,1)*I4711*vd*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I4711*vd*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*I4711*vu*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I4711*vu*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':1})

GC_1397 = Coupling(name = 'GC_1397',
                   value = '(ee**2*complex(0,1)*I4722*vd*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I4722*vd*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*I4722*vu*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I4722*vu*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':1})

GC_1398 = Coupling(name = 'GC_1398',
                   value = '(ee**2*complex(0,1)*I511*vd*cmath.cos(alp))/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I511*vd*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*I511*vu*cmath.sin(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I511*vu*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':1})

GC_1399 = Coupling(name = 'GC_1399',
                   value = '(ee**2*complex(0,1)*I522*vd*cmath.cos(alp))/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I522*vd*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*I522*vu*cmath.sin(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I522*vu*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':1})

GC_1400 = Coupling(name = 'GC_1400',
                   value = '-(ee**2*complex(0,1)*I11333*vd*cmath.cos(alp))/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I11433*vd*cmath.cos(alp))/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I11333*vd*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I15033*MUH*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I15033*MUH*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I15333*complexconjugate(MUH)*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I15333*sw**2*complexconjugate(MUH)*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee**2*complex(0,1)*I11333*vu*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I11433*vu*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I15433*vu*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I15533*vu*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I11333*vu*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I15433*sw**2*vu*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I15533*sw**2*vu*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I15133*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I15233*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I15133*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I15233*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1401 = Coupling(name = 'GC_1401',
                   value = '-(ee**2*complex(0,1)*I11336*vd*cmath.cos(alp))/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I11436*vd*cmath.cos(alp))/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I11336*vd*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I15036*MUH*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I15036*MUH*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I15336*complexconjugate(MUH)*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I15336*sw**2*complexconjugate(MUH)*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee**2*complex(0,1)*I11336*vu*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I11436*vu*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I15436*vu*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I15536*vu*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I11336*vu*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I15436*sw**2*vu*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I15536*sw**2*vu*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I15136*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I15236*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I15136*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I15236*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1402 = Coupling(name = 'GC_1402',
                   value = '-(ee**2*complex(0,1)*I11363*vd*cmath.cos(alp))/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I11463*vd*cmath.cos(alp))/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I11363*vd*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I15063*MUH*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I15063*MUH*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I15363*complexconjugate(MUH)*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I15363*sw**2*complexconjugate(MUH)*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee**2*complex(0,1)*I11363*vu*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I11463*vu*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I15463*vu*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I15563*vu*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I11363*vu*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I15463*sw**2*vu*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I15563*sw**2*vu*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I15163*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I15263*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I15163*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I15263*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1403 = Coupling(name = 'GC_1403',
                   value = '-(ee**2*complex(0,1)*I11366*vd*cmath.cos(alp))/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I11466*vd*cmath.cos(alp))/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I11366*vd*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I15066*MUH*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I15066*MUH*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I15366*complexconjugate(MUH)*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I15366*sw**2*complexconjugate(MUH)*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee**2*complex(0,1)*I11366*vu*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I11466*vu*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I15466*vu*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I15566*vu*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I11366*vu*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I15466*sw**2*vu*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I15566*sw**2*vu*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I15166*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I15266*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I15166*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I15266*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1404 = Coupling(name = 'GC_1404',
                   value = '-((ee*complex(0,1)*UU11*VV12*cmath.cos(alp))/(sw*cmath.sqrt(2))) + (ee*complex(0,1)*UU12*VV11*cmath.sin(alp))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1405 = Coupling(name = 'GC_1405',
                   value = '-((ee*complex(0,1)*UU21*VV12*cmath.cos(alp))/(sw*cmath.sqrt(2))) + (ee*complex(0,1)*UU22*VV11*cmath.sin(alp))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1406 = Coupling(name = 'GC_1406',
                   value = '-((ee*complex(0,1)*UU12*VV11*cmath.cos(alp))/(sw*cmath.sqrt(2))) - (ee*complex(0,1)*UU11*VV12*cmath.sin(alp))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1407 = Coupling(name = 'GC_1407',
                   value = '-((ee*complex(0,1)*UU22*VV11*cmath.cos(alp))/(sw*cmath.sqrt(2))) - (ee*complex(0,1)*UU21*VV12*cmath.sin(alp))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1408 = Coupling(name = 'GC_1408',
                   value = '-((ee*complex(0,1)*UU11*VV22*cmath.cos(alp))/(sw*cmath.sqrt(2))) + (ee*complex(0,1)*UU12*VV21*cmath.sin(alp))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1409 = Coupling(name = 'GC_1409',
                   value = '-((ee*complex(0,1)*UU21*VV22*cmath.cos(alp))/(sw*cmath.sqrt(2))) + (ee*complex(0,1)*UU22*VV21*cmath.sin(alp))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1410 = Coupling(name = 'GC_1410',
                   value = '-((ee*complex(0,1)*UU12*VV21*cmath.cos(alp))/(sw*cmath.sqrt(2))) - (ee*complex(0,1)*UU11*VV22*cmath.sin(alp))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1411 = Coupling(name = 'GC_1411',
                   value = '-((ee*complex(0,1)*UU22*VV21*cmath.cos(alp))/(sw*cmath.sqrt(2))) - (ee*complex(0,1)*UU21*VV22*cmath.sin(alp))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1412 = Coupling(name = 'GC_1412',
                   value = '(ee**2*complex(0,1)*I11333*vu*cmath.cos(alp))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I11433*vu*cmath.cos(alp))/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I15433*vu*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I15533*vu*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I11333*vu*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I15433*sw**2*vu*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I15533*sw**2*vu*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I15133*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I15233*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I15133*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I15233*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee**2*complex(0,1)*I11333*vd*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I11433*vd*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I11333*vd*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*I15033*MUH*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I15033*MUH*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I15333*complexconjugate(MUH)*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I15333*sw**2*complexconjugate(MUH)*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1413 = Coupling(name = 'GC_1413',
                   value = '(ee**2*complex(0,1)*I11336*vu*cmath.cos(alp))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I11436*vu*cmath.cos(alp))/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I15436*vu*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I15536*vu*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I11336*vu*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I15436*sw**2*vu*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I15536*sw**2*vu*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I15136*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I15236*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I15136*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I15236*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee**2*complex(0,1)*I11336*vd*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I11436*vd*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I11336*vd*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*I15036*MUH*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I15036*MUH*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I15336*complexconjugate(MUH)*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I15336*sw**2*complexconjugate(MUH)*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1414 = Coupling(name = 'GC_1414',
                   value = '(ee**2*complex(0,1)*I11363*vu*cmath.cos(alp))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I11463*vu*cmath.cos(alp))/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I15463*vu*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I15563*vu*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I11363*vu*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I15463*sw**2*vu*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I15563*sw**2*vu*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I15163*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I15263*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I15163*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I15263*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee**2*complex(0,1)*I11363*vd*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I11463*vd*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I11363*vd*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*I15063*MUH*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I15063*MUH*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I15363*complexconjugate(MUH)*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I15363*sw**2*complexconjugate(MUH)*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1415 = Coupling(name = 'GC_1415',
                   value = '(ee**2*complex(0,1)*I11366*vu*cmath.cos(alp))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I11466*vu*cmath.cos(alp))/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I15466*vu*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I15566*vu*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I11366*vu*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I15466*sw**2*vu*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I15566*sw**2*vu*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I15166*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I15266*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I15166*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I15266*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee**2*complex(0,1)*I11366*vd*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I11466*vd*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I11366*vd*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*I15066*MUH*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I15066*MUH*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I15366*complexconjugate(MUH)*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I15366*sw**2*complexconjugate(MUH)*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1416 = Coupling(name = 'GC_1416',
                   value = '(complex(0,1)*I1833*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I1933*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I533*vd*cmath.cos(alp))/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I633*vd*cmath.cos(alp))/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I533*vd*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I1833*sw**2*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I1933*sw**2*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I1433*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I1633*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I1433*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I1633*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee**2*complex(0,1)*I533*vu*cmath.sin(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I633*vu*cmath.sin(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I533*vu*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I1533*MUH*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I1533*MUH*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I1733*complexconjugate(MUH)*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I1733*sw**2*complexconjugate(MUH)*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1417 = Coupling(name = 'GC_1417',
                   value = '(complex(0,1)*I1836*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I1936*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I536*vd*cmath.cos(alp))/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I636*vd*cmath.cos(alp))/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I536*vd*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I1836*sw**2*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I1936*sw**2*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I1436*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I1636*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I1436*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I1636*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee**2*complex(0,1)*I536*vu*cmath.sin(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I636*vu*cmath.sin(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I536*vu*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I1536*MUH*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I1536*MUH*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I1736*complexconjugate(MUH)*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I1736*sw**2*complexconjugate(MUH)*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1418 = Coupling(name = 'GC_1418',
                   value = '(complex(0,1)*I1863*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I1963*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I563*vd*cmath.cos(alp))/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I663*vd*cmath.cos(alp))/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I563*vd*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I1863*sw**2*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I1963*sw**2*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I1463*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I1663*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I1463*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I1663*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee**2*complex(0,1)*I563*vu*cmath.sin(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I663*vu*cmath.sin(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I563*vu*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I1563*MUH*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I1563*MUH*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I1763*complexconjugate(MUH)*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I1763*sw**2*complexconjugate(MUH)*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1419 = Coupling(name = 'GC_1419',
                   value = '(complex(0,1)*I1866*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I1966*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I566*vd*cmath.cos(alp))/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I666*vd*cmath.cos(alp))/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I566*vd*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I1866*sw**2*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I1966*sw**2*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I1466*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I1666*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I1466*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I1666*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee**2*complex(0,1)*I566*vu*cmath.sin(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I666*vu*cmath.sin(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I566*vu*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I1566*MUH*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I1566*MUH*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I1766*complexconjugate(MUH)*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I1766*sw**2*complexconjugate(MUH)*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1420 = Coupling(name = 'GC_1420',
                   value = '(ee**2*complex(0,1)*I4733*vd*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I4833*vd*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I5833*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I6033*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I4733*vd*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I5833*sw**2*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I6033*sw**2*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I5533*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I5733*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I5533*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I5733*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee**2*complex(0,1)*I4733*vu*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I4833*vu*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I4733*vu*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I5633*MUH*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I5633*MUH*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I5933*complexconjugate(MUH)*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I5933*sw**2*complexconjugate(MUH)*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1421 = Coupling(name = 'GC_1421',
                   value = '(ee**2*complex(0,1)*I4736*vd*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I4836*vd*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I5836*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I6036*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I4736*vd*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I5836*sw**2*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I6036*sw**2*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I5536*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I5736*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I5536*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I5736*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee**2*complex(0,1)*I4736*vu*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I4836*vu*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I4736*vu*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I5636*MUH*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I5636*MUH*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I5936*complexconjugate(MUH)*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I5936*sw**2*complexconjugate(MUH)*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1422 = Coupling(name = 'GC_1422',
                   value = '(ee**2*complex(0,1)*I4763*vd*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I4863*vd*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I5863*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I6063*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I4763*vd*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I5863*sw**2*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I6063*sw**2*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I5563*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I5763*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I5563*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I5763*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee**2*complex(0,1)*I4763*vu*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I4863*vu*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I4763*vu*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I5663*MUH*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I5663*MUH*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I5963*complexconjugate(MUH)*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I5963*sw**2*complexconjugate(MUH)*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1423 = Coupling(name = 'GC_1423',
                   value = '(ee**2*complex(0,1)*I4766*vd*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I4866*vd*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I5866*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I6066*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I4766*vd*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I5866*sw**2*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I6066*sw**2*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I5566*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I5766*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I5566*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I5766*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee**2*complex(0,1)*I4766*vu*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I4866*vu*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I4766*vu*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I5666*MUH*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I5666*MUH*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I5966*complexconjugate(MUH)*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I5966*sw**2*complexconjugate(MUH)*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1424 = Coupling(name = 'GC_1424',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN11)*complexconjugate(NN14)*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN12)*complexconjugate(NN14)*cmath.cos(alp))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN12)*complexconjugate(NN14)*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN11)*complexconjugate(NN13)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN12)*complexconjugate(NN13)*cmath.sin(alp))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN12)*complexconjugate(NN13)*cmath.sin(alp))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1425 = Coupling(name = 'GC_1425',
                   value = '-((cw*ee*complex(0,1)*complexconjugate(NN11)*complexconjugate(NN13)*cmath.cos(alp))/((-1 + sw)*(1 + sw))) + (ee*complex(0,1)*complexconjugate(NN12)*complexconjugate(NN13)*cmath.cos(alp))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN12)*complexconjugate(NN13)*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN11)*complexconjugate(NN14)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN12)*complexconjugate(NN14)*cmath.sin(alp))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN12)*complexconjugate(NN14)*cmath.sin(alp))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1426 = Coupling(name = 'GC_1426',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN14)*complexconjugate(NN21)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN14)*complexconjugate(NN22)*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN14)*complexconjugate(NN22)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN11)*complexconjugate(NN24)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN12)*complexconjugate(NN24)*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN12)*complexconjugate(NN24)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN13)*complexconjugate(NN21)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN13)*complexconjugate(NN22)*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN13)*complexconjugate(NN22)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN11)*complexconjugate(NN23)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN12)*complexconjugate(NN23)*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN12)*complexconjugate(NN23)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1427 = Coupling(name = 'GC_1427',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN21)*complexconjugate(NN24)*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN22)*complexconjugate(NN24)*cmath.cos(alp))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN22)*complexconjugate(NN24)*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN21)*complexconjugate(NN23)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN22)*complexconjugate(NN23)*cmath.sin(alp))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN22)*complexconjugate(NN23)*cmath.sin(alp))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1428 = Coupling(name = 'GC_1428',
                   value = '-(cw*ee*complex(0,1)*complexconjugate(NN13)*complexconjugate(NN21)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*complexconjugate(NN13)*complexconjugate(NN22)*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN13)*complexconjugate(NN22)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*complexconjugate(NN11)*complexconjugate(NN23)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*complexconjugate(NN12)*complexconjugate(NN23)*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN12)*complexconjugate(NN23)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN14)*complexconjugate(NN21)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN14)*complexconjugate(NN22)*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN14)*complexconjugate(NN22)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN11)*complexconjugate(NN24)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN12)*complexconjugate(NN24)*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN12)*complexconjugate(NN24)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1429 = Coupling(name = 'GC_1429',
                   value = '-((cw*ee*complex(0,1)*complexconjugate(NN21)*complexconjugate(NN23)*cmath.cos(alp))/((-1 + sw)*(1 + sw))) + (ee*complex(0,1)*complexconjugate(NN22)*complexconjugate(NN23)*cmath.cos(alp))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN22)*complexconjugate(NN23)*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN21)*complexconjugate(NN24)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN22)*complexconjugate(NN24)*cmath.sin(alp))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN22)*complexconjugate(NN24)*cmath.sin(alp))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1430 = Coupling(name = 'GC_1430',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN14)*complexconjugate(NN31)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN14)*complexconjugate(NN32)*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN14)*complexconjugate(NN32)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN11)*complexconjugate(NN34)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN12)*complexconjugate(NN34)*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN12)*complexconjugate(NN34)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN13)*complexconjugate(NN31)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN13)*complexconjugate(NN32)*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN13)*complexconjugate(NN32)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN11)*complexconjugate(NN33)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN12)*complexconjugate(NN33)*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN12)*complexconjugate(NN33)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1431 = Coupling(name = 'GC_1431',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN24)*complexconjugate(NN31)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN24)*complexconjugate(NN32)*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN24)*complexconjugate(NN32)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN21)*complexconjugate(NN34)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN22)*complexconjugate(NN34)*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN22)*complexconjugate(NN34)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN23)*complexconjugate(NN31)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN23)*complexconjugate(NN32)*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN23)*complexconjugate(NN32)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN21)*complexconjugate(NN33)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN22)*complexconjugate(NN33)*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN22)*complexconjugate(NN33)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1432 = Coupling(name = 'GC_1432',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN31)*complexconjugate(NN34)*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN32)*complexconjugate(NN34)*cmath.cos(alp))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN32)*complexconjugate(NN34)*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN31)*complexconjugate(NN33)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN32)*complexconjugate(NN33)*cmath.sin(alp))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN32)*complexconjugate(NN33)*cmath.sin(alp))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1433 = Coupling(name = 'GC_1433',
                   value = '-(cw*ee*complex(0,1)*complexconjugate(NN13)*complexconjugate(NN31)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*complexconjugate(NN13)*complexconjugate(NN32)*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN13)*complexconjugate(NN32)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*complexconjugate(NN11)*complexconjugate(NN33)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*complexconjugate(NN12)*complexconjugate(NN33)*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN12)*complexconjugate(NN33)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN14)*complexconjugate(NN31)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN14)*complexconjugate(NN32)*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN14)*complexconjugate(NN32)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN11)*complexconjugate(NN34)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN12)*complexconjugate(NN34)*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN12)*complexconjugate(NN34)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1434 = Coupling(name = 'GC_1434',
                   value = '-(cw*ee*complex(0,1)*complexconjugate(NN23)*complexconjugate(NN31)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*complexconjugate(NN23)*complexconjugate(NN32)*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN23)*complexconjugate(NN32)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*complexconjugate(NN21)*complexconjugate(NN33)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*complexconjugate(NN22)*complexconjugate(NN33)*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN22)*complexconjugate(NN33)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN24)*complexconjugate(NN31)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN24)*complexconjugate(NN32)*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN24)*complexconjugate(NN32)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN21)*complexconjugate(NN34)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN22)*complexconjugate(NN34)*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN22)*complexconjugate(NN34)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1435 = Coupling(name = 'GC_1435',
                   value = '-((cw*ee*complex(0,1)*complexconjugate(NN31)*complexconjugate(NN33)*cmath.cos(alp))/((-1 + sw)*(1 + sw))) + (ee*complex(0,1)*complexconjugate(NN32)*complexconjugate(NN33)*cmath.cos(alp))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN32)*complexconjugate(NN33)*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN31)*complexconjugate(NN34)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN32)*complexconjugate(NN34)*cmath.sin(alp))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN32)*complexconjugate(NN34)*cmath.sin(alp))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1436 = Coupling(name = 'GC_1436',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN14)*complexconjugate(NN41)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN14)*complexconjugate(NN42)*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN14)*complexconjugate(NN42)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN11)*complexconjugate(NN44)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN12)*complexconjugate(NN44)*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN12)*complexconjugate(NN44)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN13)*complexconjugate(NN41)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN13)*complexconjugate(NN42)*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN13)*complexconjugate(NN42)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN11)*complexconjugate(NN43)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN12)*complexconjugate(NN43)*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN12)*complexconjugate(NN43)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1437 = Coupling(name = 'GC_1437',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN24)*complexconjugate(NN41)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN24)*complexconjugate(NN42)*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN24)*complexconjugate(NN42)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN21)*complexconjugate(NN44)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN22)*complexconjugate(NN44)*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN22)*complexconjugate(NN44)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN23)*complexconjugate(NN41)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN23)*complexconjugate(NN42)*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN23)*complexconjugate(NN42)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN21)*complexconjugate(NN43)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN22)*complexconjugate(NN43)*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN22)*complexconjugate(NN43)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1438 = Coupling(name = 'GC_1438',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN34)*complexconjugate(NN41)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN34)*complexconjugate(NN42)*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN34)*complexconjugate(NN42)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN31)*complexconjugate(NN44)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN32)*complexconjugate(NN44)*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN32)*complexconjugate(NN44)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN33)*complexconjugate(NN41)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN33)*complexconjugate(NN42)*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN33)*complexconjugate(NN42)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN31)*complexconjugate(NN43)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN32)*complexconjugate(NN43)*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN32)*complexconjugate(NN43)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1439 = Coupling(name = 'GC_1439',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN41)*complexconjugate(NN44)*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN42)*complexconjugate(NN44)*cmath.cos(alp))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN42)*complexconjugate(NN44)*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN41)*complexconjugate(NN43)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN42)*complexconjugate(NN43)*cmath.sin(alp))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN42)*complexconjugate(NN43)*cmath.sin(alp))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1440 = Coupling(name = 'GC_1440',
                   value = '-(cw*ee*complex(0,1)*complexconjugate(NN13)*complexconjugate(NN41)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*complexconjugate(NN13)*complexconjugate(NN42)*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN13)*complexconjugate(NN42)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*complexconjugate(NN11)*complexconjugate(NN43)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*complexconjugate(NN12)*complexconjugate(NN43)*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN12)*complexconjugate(NN43)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN14)*complexconjugate(NN41)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN14)*complexconjugate(NN42)*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN14)*complexconjugate(NN42)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN11)*complexconjugate(NN44)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN12)*complexconjugate(NN44)*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN12)*complexconjugate(NN44)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1441 = Coupling(name = 'GC_1441',
                   value = '-(cw*ee*complex(0,1)*complexconjugate(NN23)*complexconjugate(NN41)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*complexconjugate(NN23)*complexconjugate(NN42)*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN23)*complexconjugate(NN42)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*complexconjugate(NN21)*complexconjugate(NN43)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*complexconjugate(NN22)*complexconjugate(NN43)*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN22)*complexconjugate(NN43)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN24)*complexconjugate(NN41)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN24)*complexconjugate(NN42)*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN24)*complexconjugate(NN42)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN21)*complexconjugate(NN44)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN22)*complexconjugate(NN44)*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN22)*complexconjugate(NN44)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1442 = Coupling(name = 'GC_1442',
                   value = '-(cw*ee*complex(0,1)*complexconjugate(NN33)*complexconjugate(NN41)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*complexconjugate(NN33)*complexconjugate(NN42)*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN33)*complexconjugate(NN42)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*complexconjugate(NN31)*complexconjugate(NN43)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*complexconjugate(NN32)*complexconjugate(NN43)*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN32)*complexconjugate(NN43)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN34)*complexconjugate(NN41)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN34)*complexconjugate(NN42)*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN34)*complexconjugate(NN42)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN31)*complexconjugate(NN44)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN32)*complexconjugate(NN44)*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN32)*complexconjugate(NN44)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1443 = Coupling(name = 'GC_1443',
                   value = '-((cw*ee*complex(0,1)*complexconjugate(NN41)*complexconjugate(NN43)*cmath.cos(alp))/((-1 + sw)*(1 + sw))) + (ee*complex(0,1)*complexconjugate(NN42)*complexconjugate(NN43)*cmath.cos(alp))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN42)*complexconjugate(NN43)*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN41)*complexconjugate(NN44)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN42)*complexconjugate(NN44)*cmath.sin(alp))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN42)*complexconjugate(NN44)*cmath.sin(alp))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1444 = Coupling(name = 'GC_1444',
                   value = '-((ee*complex(0,1)*complexconjugate(UU11)*complexconjugate(VV12)*cmath.cos(alp))/(sw*cmath.sqrt(2))) + (ee*complex(0,1)*complexconjugate(UU12)*complexconjugate(VV11)*cmath.sin(alp))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1445 = Coupling(name = 'GC_1445',
                   value = '-((ee*complex(0,1)*complexconjugate(UU21)*complexconjugate(VV12)*cmath.cos(alp))/(sw*cmath.sqrt(2))) + (ee*complex(0,1)*complexconjugate(UU22)*complexconjugate(VV11)*cmath.sin(alp))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1446 = Coupling(name = 'GC_1446',
                   value = '-((ee*complex(0,1)*complexconjugate(UU12)*complexconjugate(VV11)*cmath.cos(alp))/(sw*cmath.sqrt(2))) - (ee*complex(0,1)*complexconjugate(UU11)*complexconjugate(VV12)*cmath.sin(alp))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1447 = Coupling(name = 'GC_1447',
                   value = '-((ee*complex(0,1)*complexconjugate(UU22)*complexconjugate(VV11)*cmath.cos(alp))/(sw*cmath.sqrt(2))) - (ee*complex(0,1)*complexconjugate(UU21)*complexconjugate(VV12)*cmath.sin(alp))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1448 = Coupling(name = 'GC_1448',
                   value = '-((ee*complex(0,1)*complexconjugate(UU11)*complexconjugate(VV22)*cmath.cos(alp))/(sw*cmath.sqrt(2))) + (ee*complex(0,1)*complexconjugate(UU12)*complexconjugate(VV21)*cmath.sin(alp))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1449 = Coupling(name = 'GC_1449',
                   value = '-((ee*complex(0,1)*complexconjugate(UU21)*complexconjugate(VV22)*cmath.cos(alp))/(sw*cmath.sqrt(2))) + (ee*complex(0,1)*complexconjugate(UU22)*complexconjugate(VV21)*cmath.sin(alp))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1450 = Coupling(name = 'GC_1450',
                   value = '-((ee*complex(0,1)*complexconjugate(UU12)*complexconjugate(VV21)*cmath.cos(alp))/(sw*cmath.sqrt(2))) - (ee*complex(0,1)*complexconjugate(UU11)*complexconjugate(VV22)*cmath.sin(alp))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1451 = Coupling(name = 'GC_1451',
                   value = '-((ee*complex(0,1)*complexconjugate(UU22)*complexconjugate(VV21)*cmath.cos(alp))/(sw*cmath.sqrt(2))) - (ee*complex(0,1)*complexconjugate(UU21)*complexconjugate(VV22)*cmath.sin(alp))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1452 = Coupling(name = 'GC_1452',
                   value = '-(ee**2*complex(0,1)*I1211*cmath.cos(alp)*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I1211*cmath.cos(alp)*cmath.sin(alp))/(2.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1453 = Coupling(name = 'GC_1453',
                   value = '-(ee**2*complex(0,1)*I1222*cmath.cos(alp)*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I1222*cmath.cos(alp)*cmath.sin(alp))/(2.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1454 = Coupling(name = 'GC_1454',
                   value = '(2*ee**2*complex(0,1)*I14811*cmath.cos(alp)*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I14811*cmath.cos(alp)*cmath.sin(alp))/(2.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1455 = Coupling(name = 'GC_1455',
                   value = '(2*ee**2*complex(0,1)*I14822*cmath.cos(alp)*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I14822*cmath.cos(alp)*cmath.sin(alp))/(2.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1456 = Coupling(name = 'GC_1456',
                   value = '-((ee**2*complex(0,1)*I5311*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw))) + (ee**2*complex(0,1)*I5311*cmath.cos(alp)*cmath.sin(alp))/(2.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1457 = Coupling(name = 'GC_1457',
                   value = '-((ee**2*complex(0,1)*I5322*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw))) + (ee**2*complex(0,1)*I5322*cmath.cos(alp)*cmath.sin(alp))/(2.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1458 = Coupling(name = 'GC_1458',
                   value = '(2*ee**2*complex(0,1)*I14833*cmath.cos(alp)*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I14933*cmath.cos(alp)*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I15633*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I15733*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I14833*cmath.cos(alp)*cmath.sin(alp))/(2.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I15633*sw**2*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I15733*sw**2*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1459 = Coupling(name = 'GC_1459',
                   value = '(2*ee**2*complex(0,1)*I14836*cmath.cos(alp)*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I14936*cmath.cos(alp)*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I15636*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I15736*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I14836*cmath.cos(alp)*cmath.sin(alp))/(2.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I15636*sw**2*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I15736*sw**2*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1460 = Coupling(name = 'GC_1460',
                   value = '(2*ee**2*complex(0,1)*I14863*cmath.cos(alp)*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I14963*cmath.cos(alp)*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I15663*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I15763*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I14863*cmath.cos(alp)*cmath.sin(alp))/(2.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I15663*sw**2*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I15763*sw**2*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1461 = Coupling(name = 'GC_1461',
                   value = '(2*ee**2*complex(0,1)*I14866*cmath.cos(alp)*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I14966*cmath.cos(alp)*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I15666*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I15766*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I14866*cmath.cos(alp)*cmath.sin(alp))/(2.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I15666*sw**2*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I15766*sw**2*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1462 = Coupling(name = 'GC_1462',
                   value = '-(ee**2*complex(0,1)*I1233*cmath.cos(alp)*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I1333*cmath.cos(alp)*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I2033*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I2133*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I1233*cmath.cos(alp)*cmath.sin(alp))/(2.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*I2033*sw**2*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I2133*sw**2*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1463 = Coupling(name = 'GC_1463',
                   value = '-(ee**2*complex(0,1)*I1236*cmath.cos(alp)*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I1336*cmath.cos(alp)*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I2036*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I2136*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I1236*cmath.cos(alp)*cmath.sin(alp))/(2.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*I2036*sw**2*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I2136*sw**2*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1464 = Coupling(name = 'GC_1464',
                   value = '-(ee**2*complex(0,1)*I1263*cmath.cos(alp)*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I1363*cmath.cos(alp)*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I2063*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I2163*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I1263*cmath.cos(alp)*cmath.sin(alp))/(2.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*I2063*sw**2*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I2163*sw**2*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1465 = Coupling(name = 'GC_1465',
                   value = '-(ee**2*complex(0,1)*I1266*cmath.cos(alp)*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I1366*cmath.cos(alp)*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I2066*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I2166*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I1266*cmath.cos(alp)*cmath.sin(alp))/(2.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*I2066*sw**2*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I2166*sw**2*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1466 = Coupling(name = 'GC_1466',
                   value = '-((ee**2*complex(0,1)*I5333*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw))) + (ee**2*complex(0,1)*I5433*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I6133*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I6233*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I5333*cmath.cos(alp)*cmath.sin(alp))/(2.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*I6133*sw**2*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I6233*sw**2*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1467 = Coupling(name = 'GC_1467',
                   value = '-((ee**2*complex(0,1)*I5336*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw))) + (ee**2*complex(0,1)*I5436*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I6136*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I6236*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I5336*cmath.cos(alp)*cmath.sin(alp))/(2.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*I6136*sw**2*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I6236*sw**2*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1468 = Coupling(name = 'GC_1468',
                   value = '-((ee**2*complex(0,1)*I5363*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw))) + (ee**2*complex(0,1)*I5463*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I6163*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I6263*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I5363*cmath.cos(alp)*cmath.sin(alp))/(2.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*I6163*sw**2*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I6263*sw**2*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1469 = Coupling(name = 'GC_1469',
                   value = '-((ee**2*complex(0,1)*I5366*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw))) + (ee**2*complex(0,1)*I5466*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I6166*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I6266*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I5366*cmath.cos(alp)*cmath.sin(alp))/(2.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*I6166*sw**2*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I6266*sw**2*cmath.cos(alp)*cmath.sin(alp))/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1470 = Coupling(name = 'GC_1470',
                   value = '(ee**2*complex(0,1)*cmath.cos(alp)**2)/(2.*sw**2) + (ee**2*complex(0,1)*cmath.sin(alp)**2)/(2.*sw**2)',
                   order = {'QED':2})

GC_1471 = Coupling(name = 'GC_1471',
                   value = '(ee**2*complex(0,1)*I1344*cmath.cos(alp)**2)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I1344*cmath.sin(alp)**2)/(6.*(-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1472 = Coupling(name = 'GC_1472',
                   value = '-(ee**2*complex(0,1)*I1344*cmath.cos(alp)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I1344*cmath.sin(alp)**2)/(6.*(-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1473 = Coupling(name = 'GC_1473',
                   value = '(ee**2*complex(0,1)*I1355*cmath.cos(alp)**2)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I1355*cmath.sin(alp)**2)/(6.*(-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1474 = Coupling(name = 'GC_1474',
                   value = '-(ee**2*complex(0,1)*I1355*cmath.cos(alp)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I1355*cmath.sin(alp)**2)/(6.*(-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1475 = Coupling(name = 'GC_1475',
                   value = '(ee**2*complex(0,1)*I14944*cmath.cos(alp)**2)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I14944*cmath.sin(alp)**2)/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1476 = Coupling(name = 'GC_1476',
                   value = '-(ee**2*complex(0,1)*I14944*cmath.cos(alp)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I14944*cmath.sin(alp)**2)/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1477 = Coupling(name = 'GC_1477',
                   value = '(ee**2*complex(0,1)*I14955*cmath.cos(alp)**2)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I14955*cmath.sin(alp)**2)/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1478 = Coupling(name = 'GC_1478',
                   value = '-(ee**2*complex(0,1)*I14955*cmath.cos(alp)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I14955*cmath.sin(alp)**2)/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1479 = Coupling(name = 'GC_1479',
                   value = '(ee**2*complex(0,1)*I5444*cmath.cos(alp)**2)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I5444*cmath.sin(alp)**2)/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1480 = Coupling(name = 'GC_1480',
                   value = '-(ee**2*complex(0,1)*I5444*cmath.cos(alp)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I5444*cmath.sin(alp)**2)/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1481 = Coupling(name = 'GC_1481',
                   value = '(ee**2*complex(0,1)*I5455*cmath.cos(alp)**2)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I5455*cmath.sin(alp)**2)/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1482 = Coupling(name = 'GC_1482',
                   value = '-(ee**2*complex(0,1)*I5455*cmath.cos(alp)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I5455*cmath.sin(alp)**2)/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1483 = Coupling(name = 'GC_1483',
                   value = '(ee**2*complex(0,1)*cmath.cos(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1484 = Coupling(name = 'GC_1484',
                   value = '-(ee**2*complex(0,1)*cmath.cos(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1485 = Coupling(name = 'GC_1485',
                   value = '-(ee**2*complex(0,1)*cmath.cos(alp)**2)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*cmath.sin(alp)**2)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1486 = Coupling(name = 'GC_1486',
                   value = '-(ee**2*complex(0,1)*I1211*cmath.cos(alp)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I1211*cmath.cos(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I1211*cmath.sin(alp)**2)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I1211*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1487 = Coupling(name = 'GC_1487',
                   value = '(ee**2*complex(0,1)*I1211*cmath.cos(alp)**2)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I1211*cmath.cos(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*I1211*cmath.sin(alp)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I1211*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1488 = Coupling(name = 'GC_1488',
                   value = '-(ee**2*complex(0,1)*I1222*cmath.cos(alp)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I1222*cmath.cos(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I1222*cmath.sin(alp)**2)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I1222*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1489 = Coupling(name = 'GC_1489',
                   value = '(ee**2*complex(0,1)*I1222*cmath.cos(alp)**2)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I1222*cmath.cos(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*I1222*cmath.sin(alp)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I1222*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1490 = Coupling(name = 'GC_1490',
                   value = '(ee**2*complex(0,1)*I1233*cmath.cos(alp)**2)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I1333*cmath.cos(alp)**2)/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I2033*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I2133*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I1233*cmath.cos(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I2033*sw**2*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I2133*sw**2*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I1233*cmath.sin(alp)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I1333*cmath.sin(alp)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I1233*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1491 = Coupling(name = 'GC_1491',
                   value = '(ee**2*complex(0,1)*I1236*cmath.cos(alp)**2)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I1336*cmath.cos(alp)**2)/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I2036*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I2136*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I1236*cmath.cos(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I2036*sw**2*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I2136*sw**2*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I1236*cmath.sin(alp)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I1336*cmath.sin(alp)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I1236*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1492 = Coupling(name = 'GC_1492',
                   value = '(ee**2*complex(0,1)*I1263*cmath.cos(alp)**2)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I1363*cmath.cos(alp)**2)/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I2063*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I2163*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I1263*cmath.cos(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I2063*sw**2*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I2163*sw**2*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I1263*cmath.sin(alp)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I1363*cmath.sin(alp)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I1263*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1493 = Coupling(name = 'GC_1493',
                   value = '(ee**2*complex(0,1)*I1266*cmath.cos(alp)**2)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I1366*cmath.cos(alp)**2)/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I2066*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I2166*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I1266*cmath.cos(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I2066*sw**2*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I2166*sw**2*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I1266*cmath.sin(alp)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I1366*cmath.sin(alp)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I1266*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1494 = Coupling(name = 'GC_1494',
                   value = '-(ee**2*complex(0,1)*I14811*cmath.cos(alp)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I14811*cmath.cos(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I14811*cmath.sin(alp)**2)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I14811*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1495 = Coupling(name = 'GC_1495',
                   value = '(ee**2*complex(0,1)*I14811*cmath.cos(alp)**2)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I14811*cmath.cos(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*I14811*cmath.sin(alp)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I14811*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1496 = Coupling(name = 'GC_1496',
                   value = '-(ee**2*complex(0,1)*I14822*cmath.cos(alp)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I14822*cmath.cos(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I14822*cmath.sin(alp)**2)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I14822*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1497 = Coupling(name = 'GC_1497',
                   value = '(ee**2*complex(0,1)*I14822*cmath.cos(alp)**2)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I14822*cmath.cos(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*I14822*cmath.sin(alp)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I14822*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1498 = Coupling(name = 'GC_1498',
                   value = '(ee**2*complex(0,1)*I14833*cmath.cos(alp)**2)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I14933*cmath.cos(alp)**2)/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I15633*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I15733*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I14833*cmath.cos(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I15633*sw**2*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I15733*sw**2*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I14833*cmath.sin(alp)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I14933*cmath.sin(alp)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I14833*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1499 = Coupling(name = 'GC_1499',
                   value = '(ee**2*complex(0,1)*I14836*cmath.cos(alp)**2)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I14936*cmath.cos(alp)**2)/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I15636*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I15736*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I14836*cmath.cos(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I15636*sw**2*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I15736*sw**2*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I14836*cmath.sin(alp)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I14936*cmath.sin(alp)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I14836*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1500 = Coupling(name = 'GC_1500',
                   value = '(ee**2*complex(0,1)*I14863*cmath.cos(alp)**2)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I14963*cmath.cos(alp)**2)/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I15663*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I15763*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I14863*cmath.cos(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I15663*sw**2*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I15763*sw**2*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I14863*cmath.sin(alp)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I14963*cmath.sin(alp)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I14863*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1501 = Coupling(name = 'GC_1501',
                   value = '(ee**2*complex(0,1)*I14866*cmath.cos(alp)**2)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I14966*cmath.cos(alp)**2)/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I15666*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I15766*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I14866*cmath.cos(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I15666*sw**2*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I15766*sw**2*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I14866*cmath.sin(alp)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I14966*cmath.sin(alp)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I14866*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1502 = Coupling(name = 'GC_1502',
                   value = '-(ee**2*complex(0,1)*I5311*cmath.cos(alp)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I5311*cmath.cos(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I5311*cmath.sin(alp)**2)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I5311*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1503 = Coupling(name = 'GC_1503',
                   value = '(ee**2*complex(0,1)*I5311*cmath.cos(alp)**2)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I5311*cmath.cos(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*I5311*cmath.sin(alp)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I5311*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1504 = Coupling(name = 'GC_1504',
                   value = '-(ee**2*complex(0,1)*I5322*cmath.cos(alp)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I5322*cmath.cos(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I5322*cmath.sin(alp)**2)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I5322*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1505 = Coupling(name = 'GC_1505',
                   value = '(ee**2*complex(0,1)*I5322*cmath.cos(alp)**2)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I5322*cmath.cos(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*I5322*cmath.sin(alp)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I5322*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1506 = Coupling(name = 'GC_1506',
                   value = '(ee**2*complex(0,1)*I5333*cmath.cos(alp)**2)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I5433*cmath.cos(alp)**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I6133*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I6233*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I5333*cmath.cos(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I6133*sw**2*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I6233*sw**2*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I5333*cmath.sin(alp)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I5433*cmath.sin(alp)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I5333*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1507 = Coupling(name = 'GC_1507',
                   value = '(ee**2*complex(0,1)*I5336*cmath.cos(alp)**2)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I5436*cmath.cos(alp)**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I6136*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I6236*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I5336*cmath.cos(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I6136*sw**2*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I6236*sw**2*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I5336*cmath.sin(alp)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I5436*cmath.sin(alp)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I5336*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1508 = Coupling(name = 'GC_1508',
                   value = '(ee**2*complex(0,1)*I5363*cmath.cos(alp)**2)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I5463*cmath.cos(alp)**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I6163*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I6263*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I5363*cmath.cos(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I6163*sw**2*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I6263*sw**2*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I5363*cmath.sin(alp)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I5463*cmath.sin(alp)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I5363*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1509 = Coupling(name = 'GC_1509',
                   value = '(ee**2*complex(0,1)*I5366*cmath.cos(alp)**2)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I5466*cmath.cos(alp)**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I6166*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I6266*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I5366*cmath.cos(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I6166*sw**2*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I6266*sw**2*cmath.cos(alp)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I5366*cmath.sin(alp)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I5466*cmath.sin(alp)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I5366*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1510 = Coupling(name = 'GC_1510',
                   value = '-(ee**2*complex(0,1)*I14833*cmath.cos(alp)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I14933*cmath.cos(alp)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I14833*cmath.cos(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I14833*cmath.sin(alp)**2)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I14933*cmath.sin(alp)**2)/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I15633*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I15733*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I14833*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I15633*sw**2*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I15733*sw**2*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1511 = Coupling(name = 'GC_1511',
                   value = '-(ee**2*complex(0,1)*I14836*cmath.cos(alp)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I14936*cmath.cos(alp)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I14836*cmath.cos(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I14836*cmath.sin(alp)**2)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I14936*cmath.sin(alp)**2)/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I15636*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I15736*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I14836*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I15636*sw**2*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I15736*sw**2*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1512 = Coupling(name = 'GC_1512',
                   value = '-(ee**2*complex(0,1)*I14863*cmath.cos(alp)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I14963*cmath.cos(alp)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I14863*cmath.cos(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I14863*cmath.sin(alp)**2)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I14963*cmath.sin(alp)**2)/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I15663*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I15763*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I14863*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I15663*sw**2*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I15763*sw**2*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1513 = Coupling(name = 'GC_1513',
                   value = '-(ee**2*complex(0,1)*I14866*cmath.cos(alp)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I14966*cmath.cos(alp)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I14866*cmath.cos(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I14866*cmath.sin(alp)**2)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I14966*cmath.sin(alp)**2)/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I15666*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I15766*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I14866*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I15666*sw**2*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I15766*sw**2*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1514 = Coupling(name = 'GC_1514',
                   value = '-(ee**2*complex(0,1)*I1233*cmath.cos(alp)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I1333*cmath.cos(alp)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I1233*cmath.cos(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I1233*cmath.sin(alp)**2)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I1333*cmath.sin(alp)**2)/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I2033*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I2133*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I1233*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I2033*sw**2*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I2133*sw**2*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1515 = Coupling(name = 'GC_1515',
                   value = '-(ee**2*complex(0,1)*I1236*cmath.cos(alp)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I1336*cmath.cos(alp)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I1236*cmath.cos(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I1236*cmath.sin(alp)**2)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I1336*cmath.sin(alp)**2)/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I2036*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I2136*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I1236*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I2036*sw**2*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I2136*sw**2*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1516 = Coupling(name = 'GC_1516',
                   value = '-(ee**2*complex(0,1)*I1263*cmath.cos(alp)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I1363*cmath.cos(alp)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I1263*cmath.cos(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I1263*cmath.sin(alp)**2)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I1363*cmath.sin(alp)**2)/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I2063*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I2163*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I1263*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I2063*sw**2*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I2163*sw**2*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1517 = Coupling(name = 'GC_1517',
                   value = '-(ee**2*complex(0,1)*I1266*cmath.cos(alp)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I1366*cmath.cos(alp)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I1266*cmath.cos(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I1266*cmath.sin(alp)**2)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I1366*cmath.sin(alp)**2)/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I2066*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I2166*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I1266*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I2066*sw**2*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I2166*sw**2*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1518 = Coupling(name = 'GC_1518',
                   value = '-(ee**2*complex(0,1)*I5333*cmath.cos(alp)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I5433*cmath.cos(alp)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I5333*cmath.cos(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I5333*cmath.sin(alp)**2)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I5433*cmath.sin(alp)**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I6133*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I6233*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I5333*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I6133*sw**2*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I6233*sw**2*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1519 = Coupling(name = 'GC_1519',
                   value = '-(ee**2*complex(0,1)*I5336*cmath.cos(alp)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I5436*cmath.cos(alp)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I5336*cmath.cos(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I5336*cmath.sin(alp)**2)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I5436*cmath.sin(alp)**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I6136*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I6236*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I5336*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I6136*sw**2*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I6236*sw**2*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1520 = Coupling(name = 'GC_1520',
                   value = '-(ee**2*complex(0,1)*I5363*cmath.cos(alp)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I5463*cmath.cos(alp)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I5363*cmath.cos(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I5363*cmath.sin(alp)**2)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I5463*cmath.sin(alp)**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I6163*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I6263*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I5363*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I6163*sw**2*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I6263*sw**2*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1521 = Coupling(name = 'GC_1521',
                   value = '-(ee**2*complex(0,1)*I5366*cmath.cos(alp)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I5466*cmath.cos(alp)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I5366*cmath.cos(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I5366*cmath.sin(alp)**2)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I5466*cmath.sin(alp)**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I6166*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I6266*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I5366*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I6166*sw**2*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I6266*sw**2*cmath.sin(alp)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1522 = Coupling(name = 'GC_1522',
                   value = '-(ee**2*complex(0,1)*vu*cmath.cos(alp)**3)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (5*ee**2*complex(0,1)*vd*cmath.cos(alp)**2*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) + (5*ee**2*complex(0,1)*vu*cmath.cos(alp)*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*vd*cmath.sin(alp)**3)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':1})

GC_1523 = Coupling(name = 'GC_1523',
                   value = '(3*ee**2*complex(0,1)*vu*cmath.cos(alp)**3)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (3*ee**2*complex(0,1)*vd*cmath.cos(alp)**2*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (3*ee**2*complex(0,1)*vu*cmath.cos(alp)*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (3*ee**2*complex(0,1)*vd*cmath.sin(alp)**3)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':1})

GC_1524 = Coupling(name = 'GC_1524',
                   value = '-(ee**2*complex(0,1)*vd*cmath.cos(alp)**3)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (5*ee**2*complex(0,1)*vu*cmath.cos(alp)**2*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) + (5*ee**2*complex(0,1)*vd*cmath.cos(alp)*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*vu*cmath.sin(alp)**3)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':1})

GC_1525 = Coupling(name = 'GC_1525',
                   value = '(3*ee**2*complex(0,1)*vd*cmath.cos(alp)**3)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (3*ee**2*complex(0,1)*vu*cmath.cos(alp)**2*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (3*ee**2*complex(0,1)*vd*cmath.cos(alp)*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (3*ee**2*complex(0,1)*vu*cmath.sin(alp)**3)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':1})

GC_1526 = Coupling(name = 'GC_1526',
                   value = '(3*ee**2*complex(0,1)*cmath.cos(alp)**3*cmath.sin(alp))/(2.*(-1 + sw)*sw**2*(1 + sw)) - (3*ee**2*complex(0,1)*cmath.cos(alp)*cmath.sin(alp)**3)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1527 = Coupling(name = 'GC_1527',
                   value = '(-3*ee**2*complex(0,1)*cmath.cos(alp)**3*cmath.sin(alp))/(2.*(-1 + sw)*sw**2*(1 + sw)) + (3*ee**2*complex(0,1)*cmath.cos(alp)*cmath.sin(alp)**3)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1528 = Coupling(name = 'GC_1528',
                   value = '-(ee**2*complex(0,1)*cmath.cos(alp)**4)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (5*ee**2*complex(0,1)*cmath.cos(alp)**2*cmath.sin(alp)**2)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*cmath.sin(alp)**4)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1529 = Coupling(name = 'GC_1529',
                   value = '(3*ee**2*complex(0,1)*cmath.cos(alp)**4)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (3*ee**2*complex(0,1)*cmath.cos(alp)**2*cmath.sin(alp)**2)/(2.*(-1 + sw)*sw**2*(1 + sw)) + (3*ee**2*complex(0,1)*cmath.sin(alp)**4)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1530 = Coupling(name = 'GC_1530',
                   value = 'complex(0,1)*I20233*cmath.sin(beta)',
                   order = {'QED':1})

GC_1531 = Coupling(name = 'GC_1531',
                   value = 'complex(0,1)*I233*cmath.sin(beta)',
                   order = {'QED':1})

GC_1532 = Coupling(name = 'GC_1532',
                   value = 'complex(0,1)*I4233*cmath.sin(beta)',
                   order = {'QED':1})

GC_1533 = Coupling(name = 'GC_1533',
                   value = 'complex(0,1)*I4433*cmath.sin(beta)',
                   order = {'QED':1})

GC_1534 = Coupling(name = 'GC_1534',
                   value = '(yd33*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1535 = Coupling(name = 'GC_1535',
                   value = '(ye33*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1536 = Coupling(name = 'GC_1536',
                   value = '-((complexconjugate(yd33)*cmath.sin(beta))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1537 = Coupling(name = 'GC_1537',
                   value = '-((complexconjugate(ye33)*cmath.sin(beta))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1538 = Coupling(name = 'GC_1538',
                   value = '-((I1533*MUH*cmath.cos(beta))/cmath.sqrt(2)) + (I1733*complexconjugate(MUH)*cmath.cos(beta))/cmath.sqrt(2) - (I1433*cmath.sin(beta))/cmath.sqrt(2) + (I1633*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1539 = Coupling(name = 'GC_1539',
                   value = '-((I1536*MUH*cmath.cos(beta))/cmath.sqrt(2)) + (I1736*complexconjugate(MUH)*cmath.cos(beta))/cmath.sqrt(2) - (I1436*cmath.sin(beta))/cmath.sqrt(2) + (I1636*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1540 = Coupling(name = 'GC_1540',
                   value = '-((I1563*MUH*cmath.cos(beta))/cmath.sqrt(2)) + (I1763*complexconjugate(MUH)*cmath.cos(beta))/cmath.sqrt(2) - (I1463*cmath.sin(beta))/cmath.sqrt(2) + (I1663*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1541 = Coupling(name = 'GC_1541',
                   value = '-((I1566*MUH*cmath.cos(beta))/cmath.sqrt(2)) + (I1766*complexconjugate(MUH)*cmath.cos(beta))/cmath.sqrt(2) - (I1466*cmath.sin(beta))/cmath.sqrt(2) + (I1666*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1542 = Coupling(name = 'GC_1542',
                   value = '-((I5633*MUH*cmath.cos(beta))/cmath.sqrt(2)) + (I5933*complexconjugate(MUH)*cmath.cos(beta))/cmath.sqrt(2) - (I5533*cmath.sin(beta))/cmath.sqrt(2) + (I5733*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1543 = Coupling(name = 'GC_1543',
                   value = '-((I5636*MUH*cmath.cos(beta))/cmath.sqrt(2)) + (I5936*complexconjugate(MUH)*cmath.cos(beta))/cmath.sqrt(2) - (I5536*cmath.sin(beta))/cmath.sqrt(2) + (I5736*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1544 = Coupling(name = 'GC_1544',
                   value = '-((I5663*MUH*cmath.cos(beta))/cmath.sqrt(2)) + (I5963*complexconjugate(MUH)*cmath.cos(beta))/cmath.sqrt(2) - (I5563*cmath.sin(beta))/cmath.sqrt(2) + (I5763*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1545 = Coupling(name = 'GC_1545',
                   value = '-((I5666*MUH*cmath.cos(beta))/cmath.sqrt(2)) + (I5966*complexconjugate(MUH)*cmath.cos(beta))/cmath.sqrt(2) - (I5566*cmath.sin(beta))/cmath.sqrt(2) + (I5766*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1546 = Coupling(name = 'GC_1546',
                   value = '-((cw*ee*NN11*NN14*cmath.cos(beta))/((-1 + sw)*(1 + sw))) + (ee*NN12*NN14*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*NN12*NN14*sw*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*NN11*NN13*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (ee*NN12*NN13*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) + (ee*NN12*NN13*sw*cmath.sin(beta))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1547 = Coupling(name = 'GC_1547',
                   value = '-(cw*ee*NN14*NN21*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*NN11*NN24*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee*NN14*NN22*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN12*NN24*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN14*NN22*sw*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*NN12*NN24*sw*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*NN13*NN21*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*NN11*NN23*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*NN13*NN22*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN12*NN23*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN13*NN22*sw*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee*NN12*NN23*sw*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1548 = Coupling(name = 'GC_1548',
                   value = '-((cw*ee*NN21*NN24*cmath.cos(beta))/((-1 + sw)*(1 + sw))) + (ee*NN22*NN24*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*NN22*NN24*sw*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*NN21*NN23*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (ee*NN22*NN23*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) + (ee*NN22*NN23*sw*cmath.sin(beta))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1549 = Coupling(name = 'GC_1549',
                   value = '-(cw*ee*NN14*NN31*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*NN11*NN34*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee*NN14*NN32*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN12*NN34*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN14*NN32*sw*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*NN12*NN34*sw*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*NN13*NN31*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*NN11*NN33*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*NN13*NN32*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN12*NN33*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN13*NN32*sw*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee*NN12*NN33*sw*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1550 = Coupling(name = 'GC_1550',
                   value = '-(cw*ee*NN24*NN31*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*NN21*NN34*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee*NN24*NN32*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN22*NN34*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN24*NN32*sw*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*NN22*NN34*sw*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*NN23*NN31*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*NN21*NN33*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*NN23*NN32*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN22*NN33*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN23*NN32*sw*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee*NN22*NN33*sw*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1551 = Coupling(name = 'GC_1551',
                   value = '-((cw*ee*NN31*NN34*cmath.cos(beta))/((-1 + sw)*(1 + sw))) + (ee*NN32*NN34*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*NN32*NN34*sw*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*NN31*NN33*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (ee*NN32*NN33*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) + (ee*NN32*NN33*sw*cmath.sin(beta))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1552 = Coupling(name = 'GC_1552',
                   value = '-(cw*ee*NN14*NN41*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*NN11*NN44*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee*NN14*NN42*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN12*NN44*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN14*NN42*sw*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*NN12*NN44*sw*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*NN13*NN41*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*NN11*NN43*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*NN13*NN42*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN12*NN43*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN13*NN42*sw*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee*NN12*NN43*sw*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1553 = Coupling(name = 'GC_1553',
                   value = '-(cw*ee*NN24*NN41*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*NN21*NN44*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee*NN24*NN42*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN22*NN44*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN24*NN42*sw*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*NN22*NN44*sw*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*NN23*NN41*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*NN21*NN43*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*NN23*NN42*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN22*NN43*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN23*NN42*sw*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee*NN22*NN43*sw*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1554 = Coupling(name = 'GC_1554',
                   value = '-(cw*ee*NN34*NN41*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*NN31*NN44*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee*NN34*NN42*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN32*NN44*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN34*NN42*sw*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*NN32*NN44*sw*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*NN33*NN41*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*NN31*NN43*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*NN33*NN42*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN32*NN43*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN33*NN42*sw*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee*NN32*NN43*sw*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1555 = Coupling(name = 'GC_1555',
                   value = '-((cw*ee*NN41*NN44*cmath.cos(beta))/((-1 + sw)*(1 + sw))) + (ee*NN42*NN44*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*NN42*NN44*sw*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*NN41*NN43*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (ee*NN42*NN43*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) + (ee*NN42*NN43*sw*cmath.sin(beta))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1556 = Coupling(name = 'GC_1556',
                   value = '(ee*complex(0,1)*NN13*UU11*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN13*sw*UU11*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN11*UU12*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN12*UU12*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN12*sw*UU12*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1557 = Coupling(name = 'GC_1557',
                   value = '(ee*complex(0,1)*NN23*UU11*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN23*sw*UU11*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN21*UU12*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN22*UU12*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN22*sw*UU12*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1558 = Coupling(name = 'GC_1558',
                   value = '(ee*complex(0,1)*NN33*UU11*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN33*sw*UU11*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN31*UU12*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN32*UU12*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN32*sw*UU12*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1559 = Coupling(name = 'GC_1559',
                   value = '(ee*complex(0,1)*NN43*UU11*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN43*sw*UU11*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN41*UU12*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN42*UU12*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN42*sw*UU12*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1560 = Coupling(name = 'GC_1560',
                   value = '(ee*complex(0,1)*NN13*UU21*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN13*sw*UU21*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN11*UU22*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN12*UU22*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN12*sw*UU22*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1561 = Coupling(name = 'GC_1561',
                   value = '(ee*complex(0,1)*NN23*UU21*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN23*sw*UU21*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN21*UU22*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN22*UU22*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN22*sw*UU22*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1562 = Coupling(name = 'GC_1562',
                   value = '(ee*complex(0,1)*NN33*UU21*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN33*sw*UU21*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN31*UU22*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN32*UU22*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN32*sw*UU22*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1563 = Coupling(name = 'GC_1563',
                   value = '(ee*complex(0,1)*NN43*UU21*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN43*sw*UU21*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN41*UU22*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN42*UU22*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN42*sw*UU22*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1564 = Coupling(name = 'GC_1564',
                   value = '-(ee**2*complex(0,1)*I11511*vu*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) - (ee**2*complex(0,1)*I11511*vd*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1565 = Coupling(name = 'GC_1565',
                   value = '-(ee**2*complex(0,1)*I11522*vu*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) - (ee**2*complex(0,1)*I11522*vd*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1566 = Coupling(name = 'GC_1566',
                   value = '-(ee**2*complex(0,1)*I13611*vu*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) - (ee**2*complex(0,1)*I13611*vd*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1567 = Coupling(name = 'GC_1567',
                   value = '-(ee**2*complex(0,1)*I13622*vu*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) - (ee**2*complex(0,1)*I13622*vd*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1568 = Coupling(name = 'GC_1568',
                   value = '-(ee**2*complex(0,1)*I9011*vu*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) - (ee**2*complex(0,1)*I9011*vd*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1569 = Coupling(name = 'GC_1569',
                   value = '-(ee**2*complex(0,1)*I9022*vu*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) - (ee**2*complex(0,1)*I9022*vd*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1570 = Coupling(name = 'GC_1570',
                   value = 'complex(0,1)*I9333*complexconjugate(MUH)*cmath.cos(beta) - (ee**2*complex(0,1)*I9033*vu*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) + complex(0,1)*I9133*cmath.sin(beta) + (complex(0,1)*I9233*vd*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I9033*vd*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1571 = Coupling(name = 'GC_1571',
                   value = 'complex(0,1)*I9336*complexconjugate(MUH)*cmath.cos(beta) - (ee**2*complex(0,1)*I9036*vu*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) + complex(0,1)*I9136*cmath.sin(beta) + (complex(0,1)*I9236*vd*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I9036*vd*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1572 = Coupling(name = 'GC_1572',
                   value = '-(ee**2*complex(0,1)*I9811*vu*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) - (ee**2*complex(0,1)*I9811*vd*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1573 = Coupling(name = 'GC_1573',
                   value = '-(ee**2*complex(0,1)*I9822*vu*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) - (ee**2*complex(0,1)*I9822*vd*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1574 = Coupling(name = 'GC_1574',
                   value = 'complex(0,1)*I9933*MUH*cmath.cos(beta) - (ee**2*complex(0,1)*I9833*vu*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) + complex(0,1)*I10033*cmath.sin(beta) + (complex(0,1)*I10133*vd*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I9833*vd*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1575 = Coupling(name = 'GC_1575',
                   value = 'complex(0,1)*I9936*MUH*cmath.cos(beta) - (ee**2*complex(0,1)*I9836*vu*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) + complex(0,1)*I10036*cmath.sin(beta) + (complex(0,1)*I10136*vd*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I9836*vd*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1576 = Coupling(name = 'GC_1576',
                   value = '(ee**2*complex(0,1)*vu*cmath.cos(beta))/(2.*sw) - (ee**2*complex(0,1)*vd*cmath.sin(beta))/(2.*sw)',
                   order = {'QED':1})

GC_1577 = Coupling(name = 'GC_1577',
                   value = '(cw*ee**2*complex(0,1)*vu*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee**2*complex(0,1)*vd*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1578 = Coupling(name = 'GC_1578',
                   value = 'complex(0,1)*I11633*cmath.cos(beta) + complex(0,1)*I12033*complexconjugate(MUH)*cmath.cos(beta) + (complex(0,1)*I12133*vd*cmath.cos(beta))/cmath.sqrt(2) + (complex(0,1)*I12233*vu*cmath.cos(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I11533*vu*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) + complex(0,1)*I11833*cmath.sin(beta) + complex(0,1)*I11733*MUH*cmath.sin(beta) + (complex(0,1)*I11933*vd*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I11533*vd*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2)) + (complex(0,1)*I12133*vu*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1579 = Coupling(name = 'GC_1579',
                   value = 'complex(0,1)*I11636*cmath.cos(beta) + complex(0,1)*I12036*complexconjugate(MUH)*cmath.cos(beta) + (complex(0,1)*I12136*vd*cmath.cos(beta))/cmath.sqrt(2) + (complex(0,1)*I12236*vu*cmath.cos(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I11536*vu*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) + complex(0,1)*I11836*cmath.sin(beta) + complex(0,1)*I11736*MUH*cmath.sin(beta) + (complex(0,1)*I11936*vd*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I11536*vd*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2)) + (complex(0,1)*I12136*vu*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1580 = Coupling(name = 'GC_1580',
                   value = 'complex(0,1)*I11663*cmath.cos(beta) + complex(0,1)*I12063*complexconjugate(MUH)*cmath.cos(beta) + (complex(0,1)*I12163*vd*cmath.cos(beta))/cmath.sqrt(2) + (complex(0,1)*I12263*vu*cmath.cos(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I11563*vu*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) + complex(0,1)*I11863*cmath.sin(beta) + complex(0,1)*I11763*MUH*cmath.sin(beta) + (complex(0,1)*I11963*vd*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I11563*vd*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2)) + (complex(0,1)*I12163*vu*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1581 = Coupling(name = 'GC_1581',
                   value = 'complex(0,1)*I11666*cmath.cos(beta) + complex(0,1)*I12066*complexconjugate(MUH)*cmath.cos(beta) + (complex(0,1)*I12166*vd*cmath.cos(beta))/cmath.sqrt(2) + (complex(0,1)*I12266*vu*cmath.cos(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I11566*vu*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) + complex(0,1)*I11866*cmath.sin(beta) + complex(0,1)*I11766*MUH*cmath.sin(beta) + (complex(0,1)*I11966*vd*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I11566*vd*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2)) + (complex(0,1)*I12166*vu*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1582 = Coupling(name = 'GC_1582',
                   value = '(ee*UU11*VV12*cmath.cos(beta))/(sw*cmath.sqrt(2)) + (ee*UU12*VV11*cmath.sin(beta))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1583 = Coupling(name = 'GC_1583',
                   value = '(ee*UU21*VV12*cmath.cos(beta))/(sw*cmath.sqrt(2)) + (ee*UU22*VV11*cmath.sin(beta))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1584 = Coupling(name = 'GC_1584',
                   value = '(ee*UU11*VV22*cmath.cos(beta))/(sw*cmath.sqrt(2)) + (ee*UU12*VV21*cmath.sin(beta))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1585 = Coupling(name = 'GC_1585',
                   value = '(ee*UU21*VV22*cmath.cos(beta))/(sw*cmath.sqrt(2)) + (ee*UU22*VV21*cmath.sin(beta))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1586 = Coupling(name = 'GC_1586',
                   value = 'complex(0,1)*I13933*cmath.cos(beta) + complex(0,1)*I13733*MUH*cmath.cos(beta) + (complex(0,1)*I14133*vd*cmath.cos(beta))/cmath.sqrt(2) + (complex(0,1)*I14233*vu*cmath.cos(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I13633*vu*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) + complex(0,1)*I13833*cmath.sin(beta) + complex(0,1)*I14333*complexconjugate(MUH)*cmath.sin(beta) + (complex(0,1)*I14033*vd*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I13633*vd*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2)) + (complex(0,1)*I14133*vu*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1587 = Coupling(name = 'GC_1587',
                   value = 'complex(0,1)*I13936*cmath.cos(beta) + complex(0,1)*I13736*MUH*cmath.cos(beta) + (complex(0,1)*I14136*vd*cmath.cos(beta))/cmath.sqrt(2) + (complex(0,1)*I14236*vu*cmath.cos(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I13636*vu*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) + complex(0,1)*I13836*cmath.sin(beta) + complex(0,1)*I14336*complexconjugate(MUH)*cmath.sin(beta) + (complex(0,1)*I14036*vd*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I13636*vd*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2)) + (complex(0,1)*I14136*vu*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1588 = Coupling(name = 'GC_1588',
                   value = 'complex(0,1)*I13963*cmath.cos(beta) + complex(0,1)*I13763*MUH*cmath.cos(beta) + (complex(0,1)*I14163*vd*cmath.cos(beta))/cmath.sqrt(2) + (complex(0,1)*I14263*vu*cmath.cos(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I13663*vu*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) + complex(0,1)*I13863*cmath.sin(beta) + complex(0,1)*I14363*complexconjugate(MUH)*cmath.sin(beta) + (complex(0,1)*I14063*vd*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I13663*vd*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2)) + (complex(0,1)*I14163*vu*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1589 = Coupling(name = 'GC_1589',
                   value = 'complex(0,1)*I13966*cmath.cos(beta) + complex(0,1)*I13766*MUH*cmath.cos(beta) + (complex(0,1)*I14166*vd*cmath.cos(beta))/cmath.sqrt(2) + (complex(0,1)*I14266*vu*cmath.cos(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I13666*vu*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) + complex(0,1)*I13866*cmath.sin(beta) + complex(0,1)*I14366*complexconjugate(MUH)*cmath.sin(beta) + (complex(0,1)*I14066*vd*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I13666*vd*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2)) + (complex(0,1)*I14166*vu*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1590 = Coupling(name = 'GC_1590',
                   value = '-((I15133*cmath.cos(beta))/cmath.sqrt(2)) + (I15233*cmath.cos(beta))/cmath.sqrt(2) - (I15033*MUH*cmath.sin(beta))/cmath.sqrt(2) + (I15333*complexconjugate(MUH)*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1591 = Coupling(name = 'GC_1591',
                   value = '-((I15136*cmath.cos(beta))/cmath.sqrt(2)) + (I15236*cmath.cos(beta))/cmath.sqrt(2) - (I15036*MUH*cmath.sin(beta))/cmath.sqrt(2) + (I15336*complexconjugate(MUH)*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1592 = Coupling(name = 'GC_1592',
                   value = '-((I15163*cmath.cos(beta))/cmath.sqrt(2)) + (I15263*cmath.cos(beta))/cmath.sqrt(2) - (I15063*MUH*cmath.sin(beta))/cmath.sqrt(2) + (I15363*complexconjugate(MUH)*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1593 = Coupling(name = 'GC_1593',
                   value = '-((I15166*cmath.cos(beta))/cmath.sqrt(2)) + (I15266*cmath.cos(beta))/cmath.sqrt(2) - (I15066*MUH*cmath.sin(beta))/cmath.sqrt(2) + (I15366*complexconjugate(MUH)*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1594 = Coupling(name = 'GC_1594',
                   value = '(cw*ee*complexconjugate(NN11)*complexconjugate(NN14)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) - (ee*complexconjugate(NN12)*complexconjugate(NN14)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) + (ee*sw*complexconjugate(NN12)*complexconjugate(NN14)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) - (cw*ee*complexconjugate(NN11)*complexconjugate(NN13)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) + (ee*complexconjugate(NN12)*complexconjugate(NN13)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*sw*complexconjugate(NN12)*complexconjugate(NN13)*cmath.sin(beta))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1595 = Coupling(name = 'GC_1595',
                   value = '(cw*ee*complexconjugate(NN14)*complexconjugate(NN21)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*complexconjugate(NN14)*complexconjugate(NN22)*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*complexconjugate(NN14)*complexconjugate(NN22)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complexconjugate(NN11)*complexconjugate(NN24)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*complexconjugate(NN12)*complexconjugate(NN24)*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*complexconjugate(NN12)*complexconjugate(NN24)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complexconjugate(NN13)*complexconjugate(NN21)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee*complexconjugate(NN13)*complexconjugate(NN22)*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*sw*complexconjugate(NN13)*complexconjugate(NN22)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complexconjugate(NN11)*complexconjugate(NN23)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee*complexconjugate(NN12)*complexconjugate(NN23)*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*sw*complexconjugate(NN12)*complexconjugate(NN23)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1596 = Coupling(name = 'GC_1596',
                   value = '(cw*ee*complexconjugate(NN21)*complexconjugate(NN24)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) - (ee*complexconjugate(NN22)*complexconjugate(NN24)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) + (ee*sw*complexconjugate(NN22)*complexconjugate(NN24)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) - (cw*ee*complexconjugate(NN21)*complexconjugate(NN23)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) + (ee*complexconjugate(NN22)*complexconjugate(NN23)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*sw*complexconjugate(NN22)*complexconjugate(NN23)*cmath.sin(beta))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1597 = Coupling(name = 'GC_1597',
                   value = '(cw*ee*complexconjugate(NN14)*complexconjugate(NN31)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*complexconjugate(NN14)*complexconjugate(NN32)*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*complexconjugate(NN14)*complexconjugate(NN32)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complexconjugate(NN11)*complexconjugate(NN34)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*complexconjugate(NN12)*complexconjugate(NN34)*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*complexconjugate(NN12)*complexconjugate(NN34)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complexconjugate(NN13)*complexconjugate(NN31)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee*complexconjugate(NN13)*complexconjugate(NN32)*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*sw*complexconjugate(NN13)*complexconjugate(NN32)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complexconjugate(NN11)*complexconjugate(NN33)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee*complexconjugate(NN12)*complexconjugate(NN33)*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*sw*complexconjugate(NN12)*complexconjugate(NN33)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1598 = Coupling(name = 'GC_1598',
                   value = '(cw*ee*complexconjugate(NN24)*complexconjugate(NN31)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*complexconjugate(NN24)*complexconjugate(NN32)*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*complexconjugate(NN24)*complexconjugate(NN32)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complexconjugate(NN21)*complexconjugate(NN34)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*complexconjugate(NN22)*complexconjugate(NN34)*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*complexconjugate(NN22)*complexconjugate(NN34)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complexconjugate(NN23)*complexconjugate(NN31)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee*complexconjugate(NN23)*complexconjugate(NN32)*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*sw*complexconjugate(NN23)*complexconjugate(NN32)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complexconjugate(NN21)*complexconjugate(NN33)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee*complexconjugate(NN22)*complexconjugate(NN33)*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*sw*complexconjugate(NN22)*complexconjugate(NN33)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1599 = Coupling(name = 'GC_1599',
                   value = '(cw*ee*complexconjugate(NN31)*complexconjugate(NN34)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) - (ee*complexconjugate(NN32)*complexconjugate(NN34)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) + (ee*sw*complexconjugate(NN32)*complexconjugate(NN34)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) - (cw*ee*complexconjugate(NN31)*complexconjugate(NN33)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) + (ee*complexconjugate(NN32)*complexconjugate(NN33)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*sw*complexconjugate(NN32)*complexconjugate(NN33)*cmath.sin(beta))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1600 = Coupling(name = 'GC_1600',
                   value = '(cw*ee*complexconjugate(NN14)*complexconjugate(NN41)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*complexconjugate(NN14)*complexconjugate(NN42)*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*complexconjugate(NN14)*complexconjugate(NN42)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complexconjugate(NN11)*complexconjugate(NN44)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*complexconjugate(NN12)*complexconjugate(NN44)*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*complexconjugate(NN12)*complexconjugate(NN44)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complexconjugate(NN13)*complexconjugate(NN41)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee*complexconjugate(NN13)*complexconjugate(NN42)*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*sw*complexconjugate(NN13)*complexconjugate(NN42)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complexconjugate(NN11)*complexconjugate(NN43)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee*complexconjugate(NN12)*complexconjugate(NN43)*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*sw*complexconjugate(NN12)*complexconjugate(NN43)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1601 = Coupling(name = 'GC_1601',
                   value = '(cw*ee*complexconjugate(NN24)*complexconjugate(NN41)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*complexconjugate(NN24)*complexconjugate(NN42)*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*complexconjugate(NN24)*complexconjugate(NN42)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complexconjugate(NN21)*complexconjugate(NN44)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*complexconjugate(NN22)*complexconjugate(NN44)*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*complexconjugate(NN22)*complexconjugate(NN44)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complexconjugate(NN23)*complexconjugate(NN41)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee*complexconjugate(NN23)*complexconjugate(NN42)*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*sw*complexconjugate(NN23)*complexconjugate(NN42)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complexconjugate(NN21)*complexconjugate(NN43)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee*complexconjugate(NN22)*complexconjugate(NN43)*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*sw*complexconjugate(NN22)*complexconjugate(NN43)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1602 = Coupling(name = 'GC_1602',
                   value = '(cw*ee*complexconjugate(NN34)*complexconjugate(NN41)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*complexconjugate(NN34)*complexconjugate(NN42)*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*complexconjugate(NN34)*complexconjugate(NN42)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complexconjugate(NN31)*complexconjugate(NN44)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*complexconjugate(NN32)*complexconjugate(NN44)*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*complexconjugate(NN32)*complexconjugate(NN44)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complexconjugate(NN33)*complexconjugate(NN41)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee*complexconjugate(NN33)*complexconjugate(NN42)*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*sw*complexconjugate(NN33)*complexconjugate(NN42)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complexconjugate(NN31)*complexconjugate(NN43)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee*complexconjugate(NN32)*complexconjugate(NN43)*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*sw*complexconjugate(NN32)*complexconjugate(NN43)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1603 = Coupling(name = 'GC_1603',
                   value = '(cw*ee*complexconjugate(NN41)*complexconjugate(NN44)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) - (ee*complexconjugate(NN42)*complexconjugate(NN44)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) + (ee*sw*complexconjugate(NN42)*complexconjugate(NN44)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) - (cw*ee*complexconjugate(NN41)*complexconjugate(NN43)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) + (ee*complexconjugate(NN42)*complexconjugate(NN43)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*sw*complexconjugate(NN42)*complexconjugate(NN43)*cmath.sin(beta))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1604 = Coupling(name = 'GC_1604',
                   value = '(ee*complex(0,1)*complexconjugate(NN13)*complexconjugate(UU11)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN13)*complexconjugate(UU11)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*complexconjugate(NN11)*complexconjugate(UU12)*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*complexconjugate(NN12)*complexconjugate(UU12)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*sw*complexconjugate(NN12)*complexconjugate(UU12)*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1605 = Coupling(name = 'GC_1605',
                   value = '(ee*complex(0,1)*complexconjugate(NN23)*complexconjugate(UU11)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN23)*complexconjugate(UU11)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*complexconjugate(NN21)*complexconjugate(UU12)*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*complexconjugate(NN22)*complexconjugate(UU12)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*sw*complexconjugate(NN22)*complexconjugate(UU12)*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1606 = Coupling(name = 'GC_1606',
                   value = '(ee*complex(0,1)*complexconjugate(NN33)*complexconjugate(UU11)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN33)*complexconjugate(UU11)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*complexconjugate(NN31)*complexconjugate(UU12)*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*complexconjugate(NN32)*complexconjugate(UU12)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*sw*complexconjugate(NN32)*complexconjugate(UU12)*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1607 = Coupling(name = 'GC_1607',
                   value = '(ee*complex(0,1)*complexconjugate(NN43)*complexconjugate(UU11)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN43)*complexconjugate(UU11)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*complexconjugate(NN41)*complexconjugate(UU12)*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*complexconjugate(NN42)*complexconjugate(UU12)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*sw*complexconjugate(NN42)*complexconjugate(UU12)*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1608 = Coupling(name = 'GC_1608',
                   value = '(ee*complex(0,1)*complexconjugate(NN13)*complexconjugate(UU21)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN13)*complexconjugate(UU21)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*complexconjugate(NN11)*complexconjugate(UU22)*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*complexconjugate(NN12)*complexconjugate(UU22)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*sw*complexconjugate(NN12)*complexconjugate(UU22)*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1609 = Coupling(name = 'GC_1609',
                   value = '(ee*complex(0,1)*complexconjugate(NN23)*complexconjugate(UU21)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN23)*complexconjugate(UU21)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*complexconjugate(NN21)*complexconjugate(UU22)*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*complexconjugate(NN22)*complexconjugate(UU22)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*sw*complexconjugate(NN22)*complexconjugate(UU22)*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1610 = Coupling(name = 'GC_1610',
                   value = '(ee*complex(0,1)*complexconjugate(NN33)*complexconjugate(UU21)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN33)*complexconjugate(UU21)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*complexconjugate(NN31)*complexconjugate(UU22)*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*complexconjugate(NN32)*complexconjugate(UU22)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*sw*complexconjugate(NN32)*complexconjugate(UU22)*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1611 = Coupling(name = 'GC_1611',
                   value = '(ee*complex(0,1)*complexconjugate(NN43)*complexconjugate(UU21)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN43)*complexconjugate(UU21)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*complexconjugate(NN41)*complexconjugate(UU22)*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*complexconjugate(NN42)*complexconjugate(UU22)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*sw*complexconjugate(NN42)*complexconjugate(UU22)*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1612 = Coupling(name = 'GC_1612',
                   value = '-((ee*complexconjugate(UU11)*complexconjugate(VV12)*cmath.cos(beta))/(sw*cmath.sqrt(2))) - (ee*complexconjugate(UU12)*complexconjugate(VV11)*cmath.sin(beta))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1613 = Coupling(name = 'GC_1613',
                   value = '-((ee*complexconjugate(UU21)*complexconjugate(VV12)*cmath.cos(beta))/(sw*cmath.sqrt(2))) - (ee*complexconjugate(UU22)*complexconjugate(VV11)*cmath.sin(beta))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1614 = Coupling(name = 'GC_1614',
                   value = '-((ee*complexconjugate(UU11)*complexconjugate(VV22)*cmath.cos(beta))/(sw*cmath.sqrt(2))) - (ee*complexconjugate(UU12)*complexconjugate(VV21)*cmath.sin(beta))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1615 = Coupling(name = 'GC_1615',
                   value = '-((ee*complexconjugate(UU21)*complexconjugate(VV22)*cmath.cos(beta))/(sw*cmath.sqrt(2))) - (ee*complexconjugate(UU22)*complexconjugate(VV21)*cmath.sin(beta))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1616 = Coupling(name = 'GC_1616',
                   value = '-(ee**2*complex(0,1)*I10211*cmath.cos(beta)*cmath.sin(alp))/(2.*sw**2*cmath.sqrt(2)) - (ee**2*complex(0,1)*I10211*cmath.cos(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1617 = Coupling(name = 'GC_1617',
                   value = '-(ee**2*complex(0,1)*I10222*cmath.cos(beta)*cmath.sin(alp))/(2.*sw**2*cmath.sqrt(2)) - (ee**2*complex(0,1)*I10222*cmath.cos(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1618 = Coupling(name = 'GC_1618',
                   value = '-(ee**2*complex(0,1)*I10233*cmath.cos(beta)*cmath.sin(alp))/(2.*sw**2*cmath.sqrt(2)) + (complex(0,1)*I10333*cmath.cos(alp)*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I10233*cmath.cos(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1619 = Coupling(name = 'GC_1619',
                   value = '-(ee**2*complex(0,1)*I10236*cmath.cos(beta)*cmath.sin(alp))/(2.*sw**2*cmath.sqrt(2)) + (complex(0,1)*I10336*cmath.cos(alp)*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I10236*cmath.cos(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1620 = Coupling(name = 'GC_1620',
                   value = '-(ee**2*complex(0,1)*I12311*cmath.cos(beta)*cmath.sin(alp))/(2.*sw**2*cmath.sqrt(2)) - (ee**2*complex(0,1)*I12311*cmath.cos(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1621 = Coupling(name = 'GC_1621',
                   value = '-(ee**2*complex(0,1)*I12322*cmath.cos(beta)*cmath.sin(alp))/(2.*sw**2*cmath.sqrt(2)) - (ee**2*complex(0,1)*I12322*cmath.cos(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1622 = Coupling(name = 'GC_1622',
                   value = '-(ee**2*complex(0,1)*I14411*cmath.cos(beta)*cmath.sin(alp))/(2.*sw**2*cmath.sqrt(2)) - (ee**2*complex(0,1)*I14411*cmath.cos(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1623 = Coupling(name = 'GC_1623',
                   value = '-(ee**2*complex(0,1)*I14422*cmath.cos(beta)*cmath.sin(alp))/(2.*sw**2*cmath.sqrt(2)) - (ee**2*complex(0,1)*I14422*cmath.cos(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1624 = Coupling(name = 'GC_1624',
                   value = '-(ee**2*complex(0,1)*I9411*cmath.cos(beta)*cmath.sin(alp))/(2.*sw**2*cmath.sqrt(2)) - (ee**2*complex(0,1)*I9411*cmath.cos(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1625 = Coupling(name = 'GC_1625',
                   value = '-(ee**2*complex(0,1)*I9422*cmath.cos(beta)*cmath.sin(alp))/(2.*sw**2*cmath.sqrt(2)) - (ee**2*complex(0,1)*I9422*cmath.cos(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1626 = Coupling(name = 'GC_1626',
                   value = '-(ee**2*complex(0,1)*I9433*cmath.cos(beta)*cmath.sin(alp))/(2.*sw**2*cmath.sqrt(2)) + (complex(0,1)*I9533*cmath.cos(alp)*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I9433*cmath.cos(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1627 = Coupling(name = 'GC_1627',
                   value = '-(ee**2*complex(0,1)*I9436*cmath.cos(beta)*cmath.sin(alp))/(2.*sw**2*cmath.sqrt(2)) + (complex(0,1)*I9536*cmath.cos(alp)*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I9436*cmath.cos(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1628 = Coupling(name = 'GC_1628',
                   value = '-(ee*complex(0,1)*cmath.cos(beta)*cmath.sin(alp))/(2.*sw) + (ee*complex(0,1)*cmath.cos(alp)*cmath.sin(beta))/(2.*sw)',
                   order = {'QED':1})

GC_1629 = Coupling(name = 'GC_1629',
                   value = '(ee**2*complex(0,1)*cmath.cos(beta)*cmath.sin(alp))/(2.*sw) - (ee**2*complex(0,1)*cmath.cos(alp)*cmath.sin(beta))/(2.*sw)',
                   order = {'QED':2})

GC_1630 = Coupling(name = 'GC_1630',
                   value = '(cw*ee**2*complex(0,1)*cmath.cos(beta)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee**2*complex(0,1)*cmath.cos(alp)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1631 = Coupling(name = 'GC_1631',
                   value = '(cw*ee*cmath.cos(beta)*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (cw*ee*cmath.cos(alp)*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1})

GC_1632 = Coupling(name = 'GC_1632',
                   value = '(complex(0,1)*I12433*cmath.cos(alp)*cmath.cos(beta))/cmath.sqrt(2) + (complex(0,1)*I12633*cmath.cos(beta)*cmath.sin(alp))/cmath.sqrt(2) - (ee**2*complex(0,1)*I12333*cmath.cos(beta)*cmath.sin(alp))/(2.*sw**2*cmath.sqrt(2)) + (complex(0,1)*I12533*cmath.cos(alp)*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I12333*cmath.cos(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2)) + (complex(0,1)*I12433*cmath.sin(alp)*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':2})

GC_1633 = Coupling(name = 'GC_1633',
                   value = '(complex(0,1)*I12436*cmath.cos(alp)*cmath.cos(beta))/cmath.sqrt(2) + (complex(0,1)*I12636*cmath.cos(beta)*cmath.sin(alp))/cmath.sqrt(2) - (ee**2*complex(0,1)*I12336*cmath.cos(beta)*cmath.sin(alp))/(2.*sw**2*cmath.sqrt(2)) + (complex(0,1)*I12536*cmath.cos(alp)*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I12336*cmath.cos(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2)) + (complex(0,1)*I12436*cmath.sin(alp)*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':2})

GC_1634 = Coupling(name = 'GC_1634',
                   value = '(complex(0,1)*I12463*cmath.cos(alp)*cmath.cos(beta))/cmath.sqrt(2) + (complex(0,1)*I12663*cmath.cos(beta)*cmath.sin(alp))/cmath.sqrt(2) - (ee**2*complex(0,1)*I12363*cmath.cos(beta)*cmath.sin(alp))/(2.*sw**2*cmath.sqrt(2)) + (complex(0,1)*I12563*cmath.cos(alp)*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I12363*cmath.cos(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2)) + (complex(0,1)*I12463*cmath.sin(alp)*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':2})

GC_1635 = Coupling(name = 'GC_1635',
                   value = '(complex(0,1)*I12466*cmath.cos(alp)*cmath.cos(beta))/cmath.sqrt(2) + (complex(0,1)*I12666*cmath.cos(beta)*cmath.sin(alp))/cmath.sqrt(2) - (ee**2*complex(0,1)*I12366*cmath.cos(beta)*cmath.sin(alp))/(2.*sw**2*cmath.sqrt(2)) + (complex(0,1)*I12566*cmath.cos(alp)*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I12366*cmath.cos(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2)) + (complex(0,1)*I12466*cmath.sin(alp)*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':2})

GC_1636 = Coupling(name = 'GC_1636',
                   value = '(complex(0,1)*I14733*cmath.cos(alp)*cmath.cos(beta))/cmath.sqrt(2) + (complex(0,1)*I14633*cmath.cos(beta)*cmath.sin(alp))/cmath.sqrt(2) - (ee**2*complex(0,1)*I14433*cmath.cos(beta)*cmath.sin(alp))/(2.*sw**2*cmath.sqrt(2)) + (complex(0,1)*I14533*cmath.cos(alp)*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I14433*cmath.cos(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2)) + (complex(0,1)*I14733*cmath.sin(alp)*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':2})

GC_1637 = Coupling(name = 'GC_1637',
                   value = '(complex(0,1)*I14736*cmath.cos(alp)*cmath.cos(beta))/cmath.sqrt(2) + (complex(0,1)*I14636*cmath.cos(beta)*cmath.sin(alp))/cmath.sqrt(2) - (ee**2*complex(0,1)*I14436*cmath.cos(beta)*cmath.sin(alp))/(2.*sw**2*cmath.sqrt(2)) + (complex(0,1)*I14536*cmath.cos(alp)*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I14436*cmath.cos(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2)) + (complex(0,1)*I14736*cmath.sin(alp)*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':2})

GC_1638 = Coupling(name = 'GC_1638',
                   value = '(complex(0,1)*I14763*cmath.cos(alp)*cmath.cos(beta))/cmath.sqrt(2) + (complex(0,1)*I14663*cmath.cos(beta)*cmath.sin(alp))/cmath.sqrt(2) - (ee**2*complex(0,1)*I14463*cmath.cos(beta)*cmath.sin(alp))/(2.*sw**2*cmath.sqrt(2)) + (complex(0,1)*I14563*cmath.cos(alp)*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I14463*cmath.cos(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2)) + (complex(0,1)*I14763*cmath.sin(alp)*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':2})

GC_1639 = Coupling(name = 'GC_1639',
                   value = '(complex(0,1)*I14766*cmath.cos(alp)*cmath.cos(beta))/cmath.sqrt(2) + (complex(0,1)*I14666*cmath.cos(beta)*cmath.sin(alp))/cmath.sqrt(2) - (ee**2*complex(0,1)*I14466*cmath.cos(beta)*cmath.sin(alp))/(2.*sw**2*cmath.sqrt(2)) + (complex(0,1)*I14566*cmath.cos(alp)*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I14466*cmath.cos(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2)) + (complex(0,1)*I14766*cmath.sin(alp)*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':2})

GC_1640 = Coupling(name = 'GC_1640',
                   value = '-(ee**2*complex(0,1)*I10211*cmath.cos(alp)*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) + (ee**2*complex(0,1)*I10211*cmath.sin(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1641 = Coupling(name = 'GC_1641',
                   value = '-(ee**2*complex(0,1)*I10222*cmath.cos(alp)*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) + (ee**2*complex(0,1)*I10222*cmath.sin(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1642 = Coupling(name = 'GC_1642',
                   value = '-(ee**2*complex(0,1)*I10233*cmath.cos(alp)*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) - (complex(0,1)*I10333*cmath.sin(alp)*cmath.sin(beta))/cmath.sqrt(2) + (ee**2*complex(0,1)*I10233*cmath.sin(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1643 = Coupling(name = 'GC_1643',
                   value = '-(ee**2*complex(0,1)*I10236*cmath.cos(alp)*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) - (complex(0,1)*I10336*cmath.sin(alp)*cmath.sin(beta))/cmath.sqrt(2) + (ee**2*complex(0,1)*I10236*cmath.sin(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1644 = Coupling(name = 'GC_1644',
                   value = '-(ee**2*complex(0,1)*I12311*cmath.cos(alp)*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) + (ee**2*complex(0,1)*I12311*cmath.sin(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1645 = Coupling(name = 'GC_1645',
                   value = '-(ee**2*complex(0,1)*I12322*cmath.cos(alp)*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) + (ee**2*complex(0,1)*I12322*cmath.sin(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1646 = Coupling(name = 'GC_1646',
                   value = '(complex(0,1)*I12633*cmath.cos(alp)*cmath.cos(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I12333*cmath.cos(alp)*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) - (complex(0,1)*I12433*cmath.cos(beta)*cmath.sin(alp))/cmath.sqrt(2) + (complex(0,1)*I12433*cmath.cos(alp)*cmath.sin(beta))/cmath.sqrt(2) - (complex(0,1)*I12533*cmath.sin(alp)*cmath.sin(beta))/cmath.sqrt(2) + (ee**2*complex(0,1)*I12333*cmath.sin(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1647 = Coupling(name = 'GC_1647',
                   value = '(complex(0,1)*I12636*cmath.cos(alp)*cmath.cos(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I12336*cmath.cos(alp)*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) - (complex(0,1)*I12436*cmath.cos(beta)*cmath.sin(alp))/cmath.sqrt(2) + (complex(0,1)*I12436*cmath.cos(alp)*cmath.sin(beta))/cmath.sqrt(2) - (complex(0,1)*I12536*cmath.sin(alp)*cmath.sin(beta))/cmath.sqrt(2) + (ee**2*complex(0,1)*I12336*cmath.sin(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1648 = Coupling(name = 'GC_1648',
                   value = '(complex(0,1)*I12663*cmath.cos(alp)*cmath.cos(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I12363*cmath.cos(alp)*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) - (complex(0,1)*I12463*cmath.cos(beta)*cmath.sin(alp))/cmath.sqrt(2) + (complex(0,1)*I12463*cmath.cos(alp)*cmath.sin(beta))/cmath.sqrt(2) - (complex(0,1)*I12563*cmath.sin(alp)*cmath.sin(beta))/cmath.sqrt(2) + (ee**2*complex(0,1)*I12363*cmath.sin(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1649 = Coupling(name = 'GC_1649',
                   value = '(complex(0,1)*I12666*cmath.cos(alp)*cmath.cos(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I12366*cmath.cos(alp)*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) - (complex(0,1)*I12466*cmath.cos(beta)*cmath.sin(alp))/cmath.sqrt(2) + (complex(0,1)*I12466*cmath.cos(alp)*cmath.sin(beta))/cmath.sqrt(2) - (complex(0,1)*I12566*cmath.sin(alp)*cmath.sin(beta))/cmath.sqrt(2) + (ee**2*complex(0,1)*I12366*cmath.sin(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1650 = Coupling(name = 'GC_1650',
                   value = '-(ee**2*complex(0,1)*I14411*cmath.cos(alp)*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) + (ee**2*complex(0,1)*I14411*cmath.sin(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1651 = Coupling(name = 'GC_1651',
                   value = '-(ee**2*complex(0,1)*I14422*cmath.cos(alp)*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) + (ee**2*complex(0,1)*I14422*cmath.sin(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1652 = Coupling(name = 'GC_1652',
                   value = '(complex(0,1)*I14633*cmath.cos(alp)*cmath.cos(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I14433*cmath.cos(alp)*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) - (complex(0,1)*I14733*cmath.cos(beta)*cmath.sin(alp))/cmath.sqrt(2) + (complex(0,1)*I14733*cmath.cos(alp)*cmath.sin(beta))/cmath.sqrt(2) - (complex(0,1)*I14533*cmath.sin(alp)*cmath.sin(beta))/cmath.sqrt(2) + (ee**2*complex(0,1)*I14433*cmath.sin(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1653 = Coupling(name = 'GC_1653',
                   value = '(complex(0,1)*I14636*cmath.cos(alp)*cmath.cos(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I14436*cmath.cos(alp)*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) - (complex(0,1)*I14736*cmath.cos(beta)*cmath.sin(alp))/cmath.sqrt(2) + (complex(0,1)*I14736*cmath.cos(alp)*cmath.sin(beta))/cmath.sqrt(2) - (complex(0,1)*I14536*cmath.sin(alp)*cmath.sin(beta))/cmath.sqrt(2) + (ee**2*complex(0,1)*I14436*cmath.sin(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1654 = Coupling(name = 'GC_1654',
                   value = '(complex(0,1)*I14663*cmath.cos(alp)*cmath.cos(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I14463*cmath.cos(alp)*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) - (complex(0,1)*I14763*cmath.cos(beta)*cmath.sin(alp))/cmath.sqrt(2) + (complex(0,1)*I14763*cmath.cos(alp)*cmath.sin(beta))/cmath.sqrt(2) - (complex(0,1)*I14563*cmath.sin(alp)*cmath.sin(beta))/cmath.sqrt(2) + (ee**2*complex(0,1)*I14463*cmath.sin(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1655 = Coupling(name = 'GC_1655',
                   value = '(complex(0,1)*I14666*cmath.cos(alp)*cmath.cos(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I14466*cmath.cos(alp)*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) - (complex(0,1)*I14766*cmath.cos(beta)*cmath.sin(alp))/cmath.sqrt(2) + (complex(0,1)*I14766*cmath.cos(alp)*cmath.sin(beta))/cmath.sqrt(2) - (complex(0,1)*I14566*cmath.sin(alp)*cmath.sin(beta))/cmath.sqrt(2) + (ee**2*complex(0,1)*I14466*cmath.sin(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1656 = Coupling(name = 'GC_1656',
                   value = '-(ee**2*complex(0,1)*I9411*cmath.cos(alp)*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) + (ee**2*complex(0,1)*I9411*cmath.sin(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1657 = Coupling(name = 'GC_1657',
                   value = '-(ee**2*complex(0,1)*I9422*cmath.cos(alp)*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) + (ee**2*complex(0,1)*I9422*cmath.sin(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1658 = Coupling(name = 'GC_1658',
                   value = '-(ee**2*complex(0,1)*I9433*cmath.cos(alp)*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) - (complex(0,1)*I9533*cmath.sin(alp)*cmath.sin(beta))/cmath.sqrt(2) + (ee**2*complex(0,1)*I9433*cmath.sin(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1659 = Coupling(name = 'GC_1659',
                   value = '-(ee**2*complex(0,1)*I9436*cmath.cos(alp)*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) - (complex(0,1)*I9536*cmath.sin(alp)*cmath.sin(beta))/cmath.sqrt(2) + (ee**2*complex(0,1)*I9436*cmath.sin(alp)*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1660 = Coupling(name = 'GC_1660',
                   value = '-(ee*complex(0,1)*cmath.cos(alp)*cmath.cos(beta))/(2.*sw) - (ee*complex(0,1)*cmath.sin(alp)*cmath.sin(beta))/(2.*sw)',
                   order = {'QED':1})

GC_1661 = Coupling(name = 'GC_1661',
                   value = '(ee**2*complex(0,1)*cmath.cos(alp)*cmath.cos(beta))/(2.*sw) + (ee**2*complex(0,1)*cmath.sin(alp)*cmath.sin(beta))/(2.*sw)',
                   order = {'QED':2})

GC_1662 = Coupling(name = 'GC_1662',
                   value = '(cw*ee**2*complex(0,1)*cmath.cos(alp)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee**2*complex(0,1)*cmath.sin(alp)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1663 = Coupling(name = 'GC_1663',
                   value = '(cw*ee*cmath.cos(alp)*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*cmath.sin(alp)*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1})

GC_1664 = Coupling(name = 'GC_1664',
                   value = '-(ee*complex(0,1)*cmath.cos(beta)**2) - ee*complex(0,1)*cmath.sin(beta)**2',
                   order = {'QED':1})

GC_1665 = Coupling(name = 'GC_1665',
                   value = '2*ee**2*complex(0,1)*cmath.cos(beta)**2 + 2*ee**2*complex(0,1)*cmath.sin(beta)**2',
                   order = {'QED':2})

GC_1666 = Coupling(name = 'GC_1666',
                   value = '(ee**2*complex(0,1)*cmath.cos(beta)**2)/(2.*sw**2) + (ee**2*complex(0,1)*cmath.sin(beta)**2)/(2.*sw**2)',
                   order = {'QED':2})

GC_1667 = Coupling(name = 'GC_1667',
                   value = '-(ee**2*I10211*cmath.cos(beta)**2)/(2.*sw**2*cmath.sqrt(2)) + (ee**2*I10211*cmath.sin(beta)**2)/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1668 = Coupling(name = 'GC_1668',
                   value = '-(ee**2*I10222*cmath.cos(beta)**2)/(2.*sw**2*cmath.sqrt(2)) + (ee**2*I10222*cmath.sin(beta)**2)/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1669 = Coupling(name = 'GC_1669',
                   value = '-(ee**2*I10233*cmath.cos(beta)**2)/(2.*sw**2*cmath.sqrt(2)) - (I10333*cmath.sin(beta)**2)/cmath.sqrt(2) + (ee**2*I10233*cmath.sin(beta)**2)/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1670 = Coupling(name = 'GC_1670',
                   value = '-(ee**2*I10236*cmath.cos(beta)**2)/(2.*sw**2*cmath.sqrt(2)) - (I10336*cmath.sin(beta)**2)/cmath.sqrt(2) + (ee**2*I10236*cmath.sin(beta)**2)/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1671 = Coupling(name = 'GC_1671',
                   value = '(ee**2*I12311*cmath.cos(beta)**2)/(2.*sw**2*cmath.sqrt(2)) - (ee**2*I12311*cmath.sin(beta)**2)/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1672 = Coupling(name = 'GC_1672',
                   value = '(ee**2*I12322*cmath.cos(beta)**2)/(2.*sw**2*cmath.sqrt(2)) - (ee**2*I12322*cmath.sin(beta)**2)/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1673 = Coupling(name = 'GC_1673',
                   value = '-((I12633*cmath.cos(beta)**2)/cmath.sqrt(2)) + (ee**2*I12333*cmath.cos(beta)**2)/(2.*sw**2*cmath.sqrt(2)) + (I12533*cmath.sin(beta)**2)/cmath.sqrt(2) - (ee**2*I12333*cmath.sin(beta)**2)/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1674 = Coupling(name = 'GC_1674',
                   value = '-((I12636*cmath.cos(beta)**2)/cmath.sqrt(2)) + (ee**2*I12336*cmath.cos(beta)**2)/(2.*sw**2*cmath.sqrt(2)) + (I12536*cmath.sin(beta)**2)/cmath.sqrt(2) - (ee**2*I12336*cmath.sin(beta)**2)/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1675 = Coupling(name = 'GC_1675',
                   value = '-((I12663*cmath.cos(beta)**2)/cmath.sqrt(2)) + (ee**2*I12363*cmath.cos(beta)**2)/(2.*sw**2*cmath.sqrt(2)) + (I12563*cmath.sin(beta)**2)/cmath.sqrt(2) - (ee**2*I12363*cmath.sin(beta)**2)/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1676 = Coupling(name = 'GC_1676',
                   value = '-((I12666*cmath.cos(beta)**2)/cmath.sqrt(2)) + (ee**2*I12366*cmath.cos(beta)**2)/(2.*sw**2*cmath.sqrt(2)) + (I12566*cmath.sin(beta)**2)/cmath.sqrt(2) - (ee**2*I12366*cmath.sin(beta)**2)/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1677 = Coupling(name = 'GC_1677',
                   value = '-(ee**2*I14411*cmath.cos(beta)**2)/(2.*sw**2*cmath.sqrt(2)) + (ee**2*I14411*cmath.sin(beta)**2)/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1678 = Coupling(name = 'GC_1678',
                   value = '-(ee**2*I14422*cmath.cos(beta)**2)/(2.*sw**2*cmath.sqrt(2)) + (ee**2*I14422*cmath.sin(beta)**2)/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1679 = Coupling(name = 'GC_1679',
                   value = '(I14633*cmath.cos(beta)**2)/cmath.sqrt(2) - (ee**2*I14433*cmath.cos(beta)**2)/(2.*sw**2*cmath.sqrt(2)) - (I14533*cmath.sin(beta)**2)/cmath.sqrt(2) + (ee**2*I14433*cmath.sin(beta)**2)/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1680 = Coupling(name = 'GC_1680',
                   value = '(I14636*cmath.cos(beta)**2)/cmath.sqrt(2) - (ee**2*I14436*cmath.cos(beta)**2)/(2.*sw**2*cmath.sqrt(2)) - (I14536*cmath.sin(beta)**2)/cmath.sqrt(2) + (ee**2*I14436*cmath.sin(beta)**2)/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1681 = Coupling(name = 'GC_1681',
                   value = '(I14663*cmath.cos(beta)**2)/cmath.sqrt(2) - (ee**2*I14463*cmath.cos(beta)**2)/(2.*sw**2*cmath.sqrt(2)) - (I14563*cmath.sin(beta)**2)/cmath.sqrt(2) + (ee**2*I14463*cmath.sin(beta)**2)/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1682 = Coupling(name = 'GC_1682',
                   value = '(I14666*cmath.cos(beta)**2)/cmath.sqrt(2) - (ee**2*I14466*cmath.cos(beta)**2)/(2.*sw**2*cmath.sqrt(2)) - (I14566*cmath.sin(beta)**2)/cmath.sqrt(2) + (ee**2*I14466*cmath.sin(beta)**2)/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1683 = Coupling(name = 'GC_1683',
                   value = '(ee**2*I9411*cmath.cos(beta)**2)/(2.*sw**2*cmath.sqrt(2)) - (ee**2*I9411*cmath.sin(beta)**2)/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1684 = Coupling(name = 'GC_1684',
                   value = '(ee**2*I9422*cmath.cos(beta)**2)/(2.*sw**2*cmath.sqrt(2)) - (ee**2*I9422*cmath.sin(beta)**2)/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1685 = Coupling(name = 'GC_1685',
                   value = '(ee**2*I9433*cmath.cos(beta)**2)/(2.*sw**2*cmath.sqrt(2)) + (I9533*cmath.sin(beta)**2)/cmath.sqrt(2) - (ee**2*I9433*cmath.sin(beta)**2)/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1686 = Coupling(name = 'GC_1686',
                   value = '(ee**2*I9436*cmath.cos(beta)**2)/(2.*sw**2*cmath.sqrt(2)) + (I9536*cmath.sin(beta)**2)/cmath.sqrt(2) - (ee**2*I9436*cmath.sin(beta)**2)/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':2})

GC_1687 = Coupling(name = 'GC_1687',
                   value = '(ee*cmath.cos(beta)**2)/(2.*sw) + (ee*cmath.sin(beta)**2)/(2.*sw)',
                   order = {'QED':1})

GC_1688 = Coupling(name = 'GC_1688',
                   value = '-(ee**2*cmath.cos(beta)**2)/(2.*sw) - (ee**2*cmath.sin(beta)**2)/(2.*sw)',
                   order = {'QED':2})

GC_1689 = Coupling(name = 'GC_1689',
                   value = '(ee**2*cmath.cos(beta)**2)/(2.*sw) + (ee**2*cmath.sin(beta)**2)/(2.*sw)',
                   order = {'QED':2})

GC_1690 = Coupling(name = 'GC_1690',
                   value = '-(cw*ee**2*cmath.cos(beta)**2)/(2.*(-1 + sw)*(1 + sw)) - (cw*ee**2*cmath.sin(beta)**2)/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1691 = Coupling(name = 'GC_1691',
                   value = '(cw*ee**2*cmath.cos(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (cw*ee**2*cmath.sin(beta)**2)/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1692 = Coupling(name = 'GC_1692',
                   value = '(ee**2*complex(0,1)*I1344*cmath.cos(beta)**2)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I1344*cmath.sin(beta)**2)/(6.*(-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1693 = Coupling(name = 'GC_1693',
                   value = '(ee**2*complex(0,1)*I1355*cmath.cos(beta)**2)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I1355*cmath.sin(beta)**2)/(6.*(-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1694 = Coupling(name = 'GC_1694',
                   value = '-(ee**2*complex(0,1)*I14944*cmath.cos(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I14944*cmath.sin(beta)**2)/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1695 = Coupling(name = 'GC_1695',
                   value = '-(ee**2*complex(0,1)*I14955*cmath.cos(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I14955*cmath.sin(beta)**2)/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1696 = Coupling(name = 'GC_1696',
                   value = '(ee**2*complex(0,1)*I5444*cmath.cos(beta)**2)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I5444*cmath.sin(beta)**2)/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1697 = Coupling(name = 'GC_1697',
                   value = '(ee**2*complex(0,1)*I5455*cmath.cos(beta)**2)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I5455*cmath.sin(beta)**2)/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1698 = Coupling(name = 'GC_1698',
                   value = '-(ee**2*complex(0,1)*cmath.cos(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*cmath.sin(beta)**2)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1699 = Coupling(name = 'GC_1699',
                   value = '-(ee**2*complex(0,1)*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1700 = Coupling(name = 'GC_1700',
                   value = '-(ee**2*complex(0,1)*cmath.cos(beta)**2)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*cmath.sin(beta)**2)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1701 = Coupling(name = 'GC_1701',
                   value = '-(ee**2*complex(0,1)*I1211*cmath.cos(beta)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I1211*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I1211*cmath.sin(beta)**2)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I1211*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1702 = Coupling(name = 'GC_1702',
                   value = '(ee**2*complex(0,1)*I1211*cmath.cos(beta)**2)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I1211*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*I1211*cmath.sin(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I1211*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1703 = Coupling(name = 'GC_1703',
                   value = '-(ee**2*complex(0,1)*I1222*cmath.cos(beta)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I1222*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I1222*cmath.sin(beta)**2)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I1222*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1704 = Coupling(name = 'GC_1704',
                   value = '(ee**2*complex(0,1)*I1222*cmath.cos(beta)**2)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I1222*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*I1222*cmath.sin(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I1222*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1705 = Coupling(name = 'GC_1705',
                   value = '-(ee**2*complex(0,1)*I14811*cmath.cos(beta)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I14811*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I14811*cmath.sin(beta)**2)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I14811*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1706 = Coupling(name = 'GC_1706',
                   value = '(ee**2*complex(0,1)*I14811*cmath.cos(beta)**2)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I14811*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*I14811*cmath.sin(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I14811*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1707 = Coupling(name = 'GC_1707',
                   value = '-(ee**2*complex(0,1)*I14822*cmath.cos(beta)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I14822*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I14822*cmath.sin(beta)**2)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I14822*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1708 = Coupling(name = 'GC_1708',
                   value = '(ee**2*complex(0,1)*I14822*cmath.cos(beta)**2)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I14822*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*I14822*cmath.sin(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I14822*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1709 = Coupling(name = 'GC_1709',
                   value = '(ee**2*complex(0,1)*I14833*cmath.cos(beta)**2)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I14933*cmath.cos(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I15633*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I15733*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I14833*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I15633*sw**2*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I15733*sw**2*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I14833*cmath.sin(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I14933*cmath.sin(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I14833*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1710 = Coupling(name = 'GC_1710',
                   value = '(ee**2*complex(0,1)*I14836*cmath.cos(beta)**2)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I14936*cmath.cos(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I15636*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I15736*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I14836*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I15636*sw**2*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I15736*sw**2*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I14836*cmath.sin(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I14936*cmath.sin(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I14836*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1711 = Coupling(name = 'GC_1711',
                   value = '(ee**2*complex(0,1)*I14863*cmath.cos(beta)**2)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I14963*cmath.cos(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I15663*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I15763*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I14863*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I15663*sw**2*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I15763*sw**2*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I14863*cmath.sin(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I14963*cmath.sin(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I14863*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1712 = Coupling(name = 'GC_1712',
                   value = '(ee**2*complex(0,1)*I14866*cmath.cos(beta)**2)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I14966*cmath.cos(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I15666*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I15766*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I14866*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I15666*sw**2*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I15766*sw**2*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I14866*cmath.sin(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I14966*cmath.sin(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I14866*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1713 = Coupling(name = 'GC_1713',
                   value = '-(ee**2*complex(0,1)*I5311*cmath.cos(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I5311*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I5311*cmath.sin(beta)**2)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I5311*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1714 = Coupling(name = 'GC_1714',
                   value = '-(ee**2*complex(0,1)*I5311*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I5311*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1715 = Coupling(name = 'GC_1715',
                   value = '-(ee**2*complex(0,1)*I5322*cmath.cos(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I5322*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I5322*cmath.sin(beta)**2)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I5322*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1716 = Coupling(name = 'GC_1716',
                   value = '-(ee**2*complex(0,1)*I5322*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I5322*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1717 = Coupling(name = 'GC_1717',
                   value = '(cw*ee*complex(0,1)*cmath.cos(beta)**2)/(2.*(-1 + sw)*sw*(1 + sw)) - (cw*ee*complex(0,1)*sw*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*cmath.sin(beta)**2)/(2.*(-1 + sw)*sw*(1 + sw)) - (cw*ee*complex(0,1)*sw*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1718 = Coupling(name = 'GC_1718',
                   value = '-((cw*ee**2*complex(0,1)*cmath.cos(beta)**2)/((-1 + sw)*sw*(1 + sw))) + (2*cw*ee**2*complex(0,1)*sw*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) - (cw*ee**2*complex(0,1)*cmath.sin(beta)**2)/((-1 + sw)*sw*(1 + sw)) + (2*cw*ee**2*complex(0,1)*sw*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1719 = Coupling(name = 'GC_1719',
                   value = '(2*ee**2*complex(0,1)*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*cmath.cos(beta)**2)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (2*ee**2*complex(0,1)*sw**2*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) + (2*ee**2*complex(0,1)*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*cmath.sin(beta)**2)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (2*ee**2*complex(0,1)*sw**2*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1720 = Coupling(name = 'GC_1720',
                   value = '-(ee**2*complex(0,1)*cmath.cos(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*cmath.sin(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I10433*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I10433*sw**2*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1721 = Coupling(name = 'GC_1721',
                   value = '-(ee**2*complex(0,1)*I14833*cmath.cos(beta)**2)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I14933*cmath.cos(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I15733*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I14833*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I15733*sw**2*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I14833*cmath.sin(beta)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I14933*cmath.sin(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I15833*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I14833*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I15833*sw**2*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1722 = Coupling(name = 'GC_1722',
                   value = '-(ee**2*complex(0,1)*I14836*cmath.cos(beta)**2)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I14936*cmath.cos(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I15736*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I14836*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I15736*sw**2*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I14836*cmath.sin(beta)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I14936*cmath.sin(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I15836*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I14836*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I15836*sw**2*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1723 = Coupling(name = 'GC_1723',
                   value = '-(ee**2*complex(0,1)*I14863*cmath.cos(beta)**2)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I14963*cmath.cos(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I15763*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I14863*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I15763*sw**2*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I14863*cmath.sin(beta)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I14963*cmath.sin(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I15863*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I14863*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I15863*sw**2*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1724 = Coupling(name = 'GC_1724',
                   value = '-(ee**2*complex(0,1)*I14866*cmath.cos(beta)**2)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I14966*cmath.cos(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I15766*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I14866*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I15766*sw**2*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I14866*cmath.sin(beta)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I14966*cmath.sin(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I15866*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I14866*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I15866*sw**2*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1725 = Coupling(name = 'GC_1725',
                   value = '(ee**2*complex(0,1)*I1233*cmath.cos(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I1333*cmath.cos(beta)**2)/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I2233*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I1233*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I2233*sw**2*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I1233*cmath.sin(beta)**2)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I1333*cmath.sin(beta)**2)/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I2033*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I1233*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I2033*sw**2*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1726 = Coupling(name = 'GC_1726',
                   value = '(ee**2*complex(0,1)*I1236*cmath.cos(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I1336*cmath.cos(beta)**2)/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I2236*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I1236*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I2236*sw**2*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I1236*cmath.sin(beta)**2)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I1336*cmath.sin(beta)**2)/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I2036*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I1236*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I2036*sw**2*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1727 = Coupling(name = 'GC_1727',
                   value = '(ee**2*complex(0,1)*I1263*cmath.cos(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I1363*cmath.cos(beta)**2)/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I2263*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I1263*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I2263*sw**2*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I1263*cmath.sin(beta)**2)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I1363*cmath.sin(beta)**2)/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I2063*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I1263*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I2063*sw**2*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1728 = Coupling(name = 'GC_1728',
                   value = '(ee**2*complex(0,1)*I1266*cmath.cos(beta)**2)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I1366*cmath.cos(beta)**2)/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I2266*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I1266*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I2266*sw**2*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I1266*cmath.sin(beta)**2)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I1366*cmath.sin(beta)**2)/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I2066*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I1266*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I2066*sw**2*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1729 = Coupling(name = 'GC_1729',
                   value = '-(ee**2*complex(0,1)*I1233*cmath.cos(beta)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I1333*cmath.cos(beta)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I1233*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I1233*cmath.sin(beta)**2)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I1333*cmath.sin(beta)**2)/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I2033*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I2133*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I1233*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I2033*sw**2*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I2133*sw**2*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1730 = Coupling(name = 'GC_1730',
                   value = '-(ee**2*complex(0,1)*I1236*cmath.cos(beta)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I1336*cmath.cos(beta)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I1236*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I1236*cmath.sin(beta)**2)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I1336*cmath.sin(beta)**2)/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I2036*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I2136*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I1236*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I2036*sw**2*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I2136*sw**2*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1731 = Coupling(name = 'GC_1731',
                   value = '-(ee**2*complex(0,1)*I1263*cmath.cos(beta)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I1363*cmath.cos(beta)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I1263*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I1263*cmath.sin(beta)**2)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I1363*cmath.sin(beta)**2)/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I2063*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I2163*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I1263*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I2063*sw**2*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I2163*sw**2*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1732 = Coupling(name = 'GC_1732',
                   value = '-(ee**2*complex(0,1)*I1266*cmath.cos(beta)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I1366*cmath.cos(beta)**2)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I1266*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I1266*cmath.sin(beta)**2)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I1366*cmath.sin(beta)**2)/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I2066*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I2166*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I1266*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I2066*sw**2*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I2166*sw**2*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1733 = Coupling(name = 'GC_1733',
                   value = '(ee**2*complex(0,1)*I5433*cmath.cos(beta)**2)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I5333*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*I5433*cmath.sin(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I6233*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I5333*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I6233*sw**2*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1734 = Coupling(name = 'GC_1734',
                   value = '-(ee**2*complex(0,1)*I5333*cmath.cos(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I5433*cmath.cos(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I5333*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I5333*cmath.sin(beta)**2)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I5433*cmath.sin(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I6133*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I6233*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I5333*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I6133*sw**2*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I6233*sw**2*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1735 = Coupling(name = 'GC_1735',
                   value = '(ee**2*complex(0,1)*I5436*cmath.cos(beta)**2)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I5336*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*I5436*cmath.sin(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I6236*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I5336*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I6236*sw**2*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1736 = Coupling(name = 'GC_1736',
                   value = '-(ee**2*complex(0,1)*I5336*cmath.cos(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I5436*cmath.cos(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I5336*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I5336*cmath.sin(beta)**2)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I5436*cmath.sin(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I6136*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I6236*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I5336*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I6136*sw**2*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I6236*sw**2*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1737 = Coupling(name = 'GC_1737',
                   value = '(ee**2*complex(0,1)*I5463*cmath.cos(beta)**2)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I5363*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*I5463*cmath.sin(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I6263*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I5363*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I6263*sw**2*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1738 = Coupling(name = 'GC_1738',
                   value = '-(ee**2*complex(0,1)*I5363*cmath.cos(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I5463*cmath.cos(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I5363*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I5363*cmath.sin(beta)**2)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I5463*cmath.sin(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I6163*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I6263*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I5363*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I6163*sw**2*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I6263*sw**2*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1739 = Coupling(name = 'GC_1739',
                   value = '(ee**2*complex(0,1)*I5466*cmath.cos(beta)**2)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I5366*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*I5466*cmath.sin(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I6266*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I5366*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I6266*sw**2*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1740 = Coupling(name = 'GC_1740',
                   value = '-(ee**2*complex(0,1)*I5366*cmath.cos(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I5466*cmath.cos(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I5366*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I5366*cmath.sin(beta)**2)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I5466*cmath.sin(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I6166*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I6266*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I5366*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I6166*sw**2*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I6266*sw**2*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1741 = Coupling(name = 'GC_1741',
                   value = '(ee**2*complex(0,1)*vu*cmath.cos(alp)*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*vd*cmath.cos(beta)**2*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*vu*cmath.cos(alp)*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*vd*cmath.sin(alp)*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':1})

GC_1742 = Coupling(name = 'GC_1742',
                   value = '(ee**2*complex(0,1)*vu*cmath.cos(alp)*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*vd*cmath.cos(beta)**2*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*vd*cmath.cos(beta)**2*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*vd*cmath.cos(alp)*cmath.cos(beta)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*vd*cmath.cos(alp)*cmath.cos(beta)*cmath.sin(beta))/(2.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*vu*cmath.cos(beta)*cmath.sin(alp)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*vu*cmath.cos(beta)*cmath.sin(alp)*cmath.sin(beta))/(2.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*vu*cmath.cos(alp)*cmath.sin(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*vu*cmath.cos(alp)*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*vd*cmath.sin(alp)*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':1})

GC_1743 = Coupling(name = 'GC_1743',
                   value = '-(ee**2*complex(0,1)*vd*cmath.cos(alp)*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*vu*cmath.cos(beta)**2*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*vd*cmath.cos(alp)*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*vu*cmath.sin(alp)*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':1})

GC_1744 = Coupling(name = 'GC_1744',
                   value = '-(ee**2*complex(0,1)*vd*cmath.cos(alp)*cmath.cos(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*vd*cmath.cos(alp)*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*vu*cmath.cos(beta)**2*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*vu*cmath.cos(alp)*cmath.cos(beta)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*vu*cmath.cos(alp)*cmath.cos(beta)*cmath.sin(beta))/(2.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*vd*cmath.cos(beta)*cmath.sin(alp)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*vd*cmath.cos(beta)*cmath.sin(alp)*cmath.sin(beta))/(2.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*vd*cmath.cos(alp)*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*vu*cmath.sin(alp)*cmath.sin(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*vu*cmath.sin(alp)*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':1})

GC_1745 = Coupling(name = 'GC_1745',
                   value = '(ee**2*complex(0,1)*cmath.cos(alp)*cmath.cos(beta)**2*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*cmath.cos(alp)**2*cmath.cos(beta)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*cmath.cos(alp)**2*cmath.cos(beta)*cmath.sin(beta))/(2.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*cmath.cos(beta)*cmath.sin(alp)**2*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*cmath.cos(beta)*cmath.sin(alp)**2*cmath.sin(beta))/(2.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*cmath.cos(alp)*cmath.sin(alp)*cmath.sin(beta)**2)/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1746 = Coupling(name = 'GC_1746',
                   value = '(ee**2*complex(0,1)*cmath.cos(alp)*cmath.cos(beta)**2*cmath.sin(alp))/(2.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*cmath.cos(alp)*cmath.sin(alp)*cmath.sin(beta)**2)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1747 = Coupling(name = 'GC_1747',
                   value = '-(ee**2*complex(0,1)*cmath.cos(alp)**2*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*cmath.cos(beta)**2*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*cmath.cos(alp)**2*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*cmath.sin(alp)**2*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1748 = Coupling(name = 'GC_1748',
                   value = '(ee**2*complex(0,1)*cmath.cos(alp)**2*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*cmath.cos(beta)**2*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*cmath.cos(alp)**2*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*cmath.sin(alp)**2*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1749 = Coupling(name = 'GC_1749',
                   value = '(ee**2*complex(0,1)*cmath.cos(alp)**2*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*cmath.cos(beta)**2*cmath.sin(alp)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*cmath.cos(beta)**2*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*cmath.cos(alp)*cmath.cos(beta)*cmath.sin(alp)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*cmath.cos(alp)*cmath.cos(beta)*cmath.sin(alp)*cmath.sin(beta))/((-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*cmath.cos(alp)**2*cmath.sin(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*cmath.cos(alp)**2*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*cmath.sin(alp)**2*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1750 = Coupling(name = 'GC_1750',
                   value = '-(ee**2*complex(0,1)*cmath.cos(alp)**2*cmath.cos(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*cmath.cos(alp)**2*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*cmath.cos(beta)**2*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*cmath.cos(alp)*cmath.cos(beta)*cmath.sin(alp)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*cmath.cos(alp)*cmath.cos(beta)*cmath.sin(alp)*cmath.sin(beta))/((-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*cmath.cos(alp)**2*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*cmath.sin(alp)**2*cmath.sin(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*cmath.sin(alp)**2*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1751 = Coupling(name = 'GC_1751',
                   value = '(ee**2*complex(0,1)*cmath.cos(beta)**4)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*cmath.cos(beta)**2*cmath.sin(beta)**2)/(2.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*cmath.sin(beta)**4)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1752 = Coupling(name = 'GC_1752',
                   value = '(ee**2*complex(0,1)*cmath.cos(beta)**4)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*cmath.cos(beta)**2*cmath.sin(beta)**2)/((-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*cmath.sin(beta)**4)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_1753 = Coupling(name = 'GC_1753',
                   value = '(3*ee**2*complex(0,1)*cmath.cos(beta)**4)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (3*ee**2*complex(0,1)*cmath.cos(beta)**2*cmath.sin(beta)**2)/(2.*(-1 + sw)*sw**2*(1 + sw)) + (3*ee**2*complex(0,1)*cmath.sin(beta)**4)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

