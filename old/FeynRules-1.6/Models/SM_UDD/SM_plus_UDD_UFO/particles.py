# This file was automatically created by FeynRules $Revision: 535 $
# Mathematica version: 7.0 for Microsoft Windows (32-bit) (April 23, 2009)
# Date: Wed 6 Apr 2011 01:53:58


from __future__ import division
from object_library import all_particles, Particle
import parameters as Param

ve = Particle(pdg_code = 12,
              name = 've',
              antiname = 've~',
              spin = 2,
              color = 1,
              mass = Param.ZERO,
              width = Param.ZERO,
              texname = 've',
              antitexname = 've',
              charge = 0,
              LeptonNumber = 1,
              GhostNumber = 0)

ve__tilde__ = ve.anti()

vm = Particle(pdg_code = 14,
              name = 'vm',
              antiname = 'vm~',
              spin = 2,
              color = 1,
              mass = Param.ZERO,
              width = Param.ZERO,
              texname = 'vm',
              antitexname = 'vm',
              charge = 0,
              LeptonNumber = 1,
              GhostNumber = 0)

vm__tilde__ = vm.anti()

vt = Particle(pdg_code = 16,
              name = 'vt',
              antiname = 'vt~',
              spin = 2,
              color = 1,
              mass = Param.ZERO,
              width = Param.ZERO,
              texname = 'vt',
              antitexname = 'vt',
              charge = 0,
              LeptonNumber = 1,
              GhostNumber = 0)

vt__tilde__ = vt.anti()

e__minus__ = Particle(pdg_code = 11,
                      name = 'e-',
                      antiname = 'e+',
                      spin = 2,
                      color = 1,
                      mass = Param.Me,
                      width = Param.ZERO,
                      texname = 'e-',
                      antitexname = 'e-',
                      charge = -1,
                      LeptonNumber = 1,
                      GhostNumber = 0)

e__plus__ = e__minus__.anti()

m__minus__ = Particle(pdg_code = 13,
                      name = 'm-',
                      antiname = 'm+',
                      spin = 2,
                      color = 1,
                      mass = Param.MM,
                      width = Param.ZERO,
                      texname = 'm-',
                      antitexname = 'm-',
                      charge = -1,
                      LeptonNumber = 1,
                      GhostNumber = 0)

m__plus__ = m__minus__.anti()

tt__minus__ = Particle(pdg_code = 15,
                       name = 'tt-',
                       antiname = 'tt+',
                       spin = 2,
                       color = 1,
                       mass = Param.MTA,
                       width = Param.ZERO,
                       texname = 'tt-',
                       antitexname = 'tt-',
                       charge = -1,
                       LeptonNumber = 1,
                       GhostNumber = 0)

tt__plus__ = tt__minus__.anti()

u = Particle(pdg_code = 2,
             name = 'u',
             antiname = 'u~',
             spin = 2,
             color = 3,
             mass = Param.MU,
             width = Param.ZERO,
             texname = 'u',
             antitexname = 'u',
             charge = 2/3,
             LeptonNumber = 0,
             GhostNumber = 0)

u__tilde__ = u.anti()

c = Particle(pdg_code = 4,
             name = 'c',
             antiname = 'c~',
             spin = 2,
             color = 3,
             mass = Param.MC,
             width = Param.ZERO,
             texname = 'c',
             antitexname = 'c',
             charge = 2/3,
             LeptonNumber = 0,
             GhostNumber = 0)

c__tilde__ = c.anti()

t = Particle(pdg_code = 6,
             name = 't',
             antiname = 't~',
             spin = 2,
             color = 3,
             mass = Param.MT,
             width = Param.WT,
             texname = 't',
             antitexname = 't',
             charge = 2/3,
             LeptonNumber = 0,
             GhostNumber = 0)

t__tilde__ = t.anti()

d = Particle(pdg_code = 1,
             name = 'd',
             antiname = 'd~',
             spin = 2,
             color = 3,
             mass = Param.MD,
             width = Param.ZERO,
             texname = 'd',
             antitexname = 'd',
             charge = -1/3,
             LeptonNumber = 0,
             GhostNumber = 0)

d__tilde__ = d.anti()

s = Particle(pdg_code = 3,
             name = 's',
             antiname = 's~',
             spin = 2,
             color = 3,
             mass = Param.MS,
             width = Param.ZERO,
             texname = 's',
             antitexname = 's',
             charge = -1/3,
             LeptonNumber = 0,
             GhostNumber = 0)

s__tilde__ = s.anti()

b = Particle(pdg_code = 5,
             name = 'b',
             antiname = 'b~',
             spin = 2,
             color = 3,
             mass = Param.MB,
             width = Param.ZERO,
             texname = 'b',
             antitexname = 'b',
             charge = -1/3,
             LeptonNumber = 0,
             GhostNumber = 0)

b__tilde__ = b.anti()

ghA = Particle(pdg_code = 9000001,
               name = 'ghA',
               antiname = 'ghA~',
               spin = -1,
               color = 1,
               mass = Param.ZERO,
               width = Param.ZERO,
               texname = 'ghA',
               antitexname = 'ghA',
               charge = 0,
               LeptonNumber = 0,
               GhostNumber = 1)

ghA__tilde__ = ghA.anti()

ghZ = Particle(pdg_code = 9000002,
               name = 'ghZ',
               antiname = 'ghZ~',
               spin = -1,
               color = 1,
               mass = Param.MZ,
               width = Param.ZERO,
               texname = 'ghZ',
               antitexname = 'ghZ',
               charge = 0,
               LeptonNumber = 0,
               GhostNumber = 1)

ghZ__tilde__ = ghZ.anti()

ghWp = Particle(pdg_code = 9000003,
                name = 'ghWp',
                antiname = 'ghWp~',
                spin = -1,
                color = 1,
                mass = Param.MW,
                width = Param.ZERO,
                texname = 'ghWp',
                antitexname = 'ghWp',
                charge = 1,
                LeptonNumber = 0,
                GhostNumber = 1)

ghWp__tilde__ = ghWp.anti()

ghWm = Particle(pdg_code = 9000004,
                name = 'ghWm',
                antiname = 'ghWm~',
                spin = -1,
                color = 1,
                mass = Param.MW,
                width = Param.ZERO,
                texname = 'ghWm',
                antitexname = 'ghWm',
                charge = -1,
                LeptonNumber = 0,
                GhostNumber = 1)

ghWm__tilde__ = ghWm.anti()

ghG = Particle(pdg_code = 9000005,
               name = 'ghG',
               antiname = 'ghG~',
               spin = -1,
               color = 8,
               mass = Param.ZERO,
               width = Param.ZERO,
               texname = 'ghG',
               antitexname = 'ghG',
               charge = 0,
               LeptonNumber = 0,
               GhostNumber = 1)

ghG__tilde__ = ghG.anti()

A = Particle(pdg_code = 22,
             name = 'A',
             antiname = 'A',
             spin = 3,
             color = 1,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'A',
             antitexname = 'A',
             charge = 0,
             LeptonNumber = 0,
             GhostNumber = 0)

Z = Particle(pdg_code = 23,
             name = 'Z',
             antiname = 'Z',
             spin = 3,
             color = 1,
             mass = Param.MZ,
             width = Param.WZ,
             texname = 'Z',
             antitexname = 'Z',
             charge = 0,
             LeptonNumber = 0,
             GhostNumber = 0)

W__plus__ = Particle(pdg_code = 24,
                     name = 'W+',
                     antiname = 'W-',
                     spin = 3,
                     color = 1,
                     mass = Param.MW,
                     width = Param.WW,
                     texname = 'W+',
                     antitexname = 'W+',
                     charge = 1,
                     LeptonNumber = 0,
                     GhostNumber = 0)

W__minus__ = W__plus__.anti()

G = Particle(pdg_code = 21,
             name = 'G',
             antiname = 'G',
             spin = 3,
             color = 8,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'G',
             antitexname = 'G',
             charge = 0,
             LeptonNumber = 0,
             GhostNumber = 0)

H = Particle(pdg_code = 25,
             name = 'H',
             antiname = 'H',
             spin = 1,
             color = 1,
             mass = Param.MH,
             width = Param.WH,
             texname = '\\phi',
             antitexname = '\\phi',
             charge = 0,
             LeptonNumber = 0,
             GhostNumber = 0)

phi0 = Particle(pdg_code = 250,
                name = 'phi0',
                antiname = 'phi0',
                spin = 1,
                color = 1,
                mass = Param.MZ,
                width = Param.ZERO,
                texname = 'phi0',
                antitexname = 'phi0',
                GoldstoneBoson = True,
                charge = 0,
                LeptonNumber = 0,
                GhostNumber = 0)

phi__plus__ = Particle(pdg_code = 251,
                       name = 'phi+',
                       antiname = 'phi-',
                       spin = 1,
                       color = 1,
                       mass = Param.MW,
                       width = Param.ZERO,
                       texname = '\\phi^+',
                       antitexname = '\\phi^+',
                       GoldstoneBoson = True,
                       charge = 1,
                       LeptonNumber = 0,
                       GhostNumber = 0)

phi__minus__ = phi__plus__.anti()

suL = Particle(pdg_code = 1000002,
               name = 'suL',
               antiname = 'suL~',
               spin = 1,
               color = 3,
               mass = Param.MsuL,
               width = Param.WsuL,
               texname = 'suL',
               antitexname = 'suL',
               charge = 2/3,
               LeptonNumber = 0,
               GhostNumber = 0)

suL__tilde__ = suL.anti()

scL = Particle(pdg_code = 1000004,
               name = 'scL',
               antiname = 'scL~',
               spin = 1,
               color = 3,
               mass = Param.MscL,
               width = Param.WscL,
               texname = 'scL',
               antitexname = 'scL',
               charge = 2/3,
               LeptonNumber = 0,
               GhostNumber = 0)

scL__tilde__ = scL.anti()

stL = Particle(pdg_code = 1000006,
               name = 'stL',
               antiname = 'stL~',
               spin = 1,
               color = 3,
               mass = Param.MstL,
               width = Param.WstL,
               texname = 'stL',
               antitexname = 'stL',
               charge = 2/3,
               LeptonNumber = 0,
               GhostNumber = 0)

stL__tilde__ = stL.anti()

suR = Particle(pdg_code = 2000002,
               name = 'suR',
               antiname = 'suR~',
               spin = 1,
               color = 3,
               mass = Param.MsuR,
               width = Param.WsuR,
               texname = 'suR',
               antitexname = 'suR',
               charge = 2/3,
               LeptonNumber = 0,
               GhostNumber = 0)

suR__tilde__ = suR.anti()

scR = Particle(pdg_code = 2000004,
               name = 'scR',
               antiname = 'scR~',
               spin = 1,
               color = 3,
               mass = Param.MscR,
               width = Param.WscR,
               texname = 'scR',
               antitexname = 'scR',
               charge = 2/3,
               LeptonNumber = 0,
               GhostNumber = 0)

scR__tilde__ = scR.anti()

stR = Particle(pdg_code = 2000006,
               name = 'stR',
               antiname = 'stR~',
               spin = 1,
               color = 3,
               mass = Param.MstR,
               width = Param.WstR,
               texname = 'stR',
               antitexname = 'stR',
               charge = 2/3,
               LeptonNumber = 0,
               GhostNumber = 0)

stR__tilde__ = stR.anti()

sdL = Particle(pdg_code = 1000001,
               name = 'sdL',
               antiname = 'sdL~',
               spin = 1,
               color = 3,
               mass = Param.MsdL,
               width = Param.WsdL,
               texname = 'sdL',
               antitexname = 'sdL',
               charge = -1/3,
               LeptonNumber = 0,
               GhostNumber = 0)

sdL__tilde__ = sdL.anti()

ssL = Particle(pdg_code = 1000003,
               name = 'ssL',
               antiname = 'ssL~',
               spin = 1,
               color = 3,
               mass = Param.MssL,
               width = Param.WssL,
               texname = 'ssL',
               antitexname = 'ssL',
               charge = -1/3,
               LeptonNumber = 0,
               GhostNumber = 0)

ssL__tilde__ = ssL.anti()

sbL = Particle(pdg_code = 1000005,
               name = 'sbL',
               antiname = 'sbL~',
               spin = 1,
               color = 3,
               mass = Param.MsbL,
               width = Param.WsbL,
               texname = 'sbL',
               antitexname = 'sbL',
               charge = -1/3,
               LeptonNumber = 0,
               GhostNumber = 0)

sbL__tilde__ = sbL.anti()

sdR = Particle(pdg_code = 2000001,
               name = 'sdR',
               antiname = 'sdR~',
               spin = 1,
               color = 3,
               mass = Param.MsdR,
               width = Param.WsdR,
               texname = 'sdR',
               antitexname = 'sdR',
               charge = -1/3,
               LeptonNumber = 0,
               GhostNumber = 0)

sdR__tilde__ = sdR.anti()

ssR = Particle(pdg_code = 2000003,
               name = 'ssR',
               antiname = 'ssR~',
               spin = 1,
               color = 3,
               mass = Param.MssR,
               width = Param.WssR,
               texname = 'ssR',
               antitexname = 'ssR',
               charge = -1/3,
               LeptonNumber = 0,
               GhostNumber = 0)

ssR__tilde__ = ssR.anti()

sbR = Particle(pdg_code = 2000005,
               name = 'sbR',
               antiname = 'sbR~',
               spin = 1,
               color = 3,
               mass = Param.MsbR,
               width = Param.WsbR,
               texname = 'sbR',
               antitexname = 'sbR',
               charge = -1/3,
               LeptonNumber = 0,
               GhostNumber = 0)

sbR__tilde__ = sbR.anti()

