# This file was automatically created by FeynRules $Revision: 634 $
# Mathematica version: 7.0 for Mac OS X x86 (64-bit) (April 23, 2009)
# Date: Mon 23 May 2011 22:36:22


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
               mass = Param.MsqL,
               width = Param.Wsq,
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
               mass = Param.MsqL,
               width = Param.Wsq,
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
               mass = Param.MsqL,
               width = Param.Wsq,
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
               mass = Param.MsqR,
               width = Param.Wsq,
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
               mass = Param.MsqR,
               width = Param.Wsq,
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
               mass = Param.MsqR,
               width = Param.Wsq,
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
               mass = Param.MsqL,
               width = Param.Wsq,
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
               mass = Param.MsqL,
               width = Param.Wsq,
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
               mass = Param.MsqL,
               width = Param.Wsq,
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
               mass = Param.MsqR,
               width = Param.Wsq,
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
               mass = Param.MsqR,
               width = Param.Wsq,
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
               mass = Param.MsqR,
               width = Param.Wsq,
               texname = 'sbR',
               antitexname = 'sbR',
               charge = -1/3,
               LeptonNumber = 0,
               GhostNumber = 0)

sbR__tilde__ = sbR.anti()

selL = Particle(pdg_code = 1000011,
                name = 'selL',
                antiname = 'selL~',
                spin = 1,
                color = 1,
                mass = Param.MslL,
                width = Param.Wsl,
                texname = 'selL',
                antitexname = 'selL',
                charge = -1,
                LeptonNumber = 1,
                GhostNumber = 0)

selL__tilde__ = selL.anti()

smuL = Particle(pdg_code = 1000013,
                name = 'smuL',
                antiname = 'smuL~',
                spin = 1,
                color = 1,
                mass = Param.MslL,
                width = Param.Wsl,
                texname = 'smuL',
                antitexname = 'smuL',
                charge = -1,
                LeptonNumber = 1,
                GhostNumber = 0)

smuL__tilde__ = smuL.anti()

staL = Particle(pdg_code = 1000015,
                name = 'staL',
                antiname = 'staL~',
                spin = 1,
                color = 1,
                mass = Param.MslL,
                width = Param.Wsl,
                texname = 'staL',
                antitexname = 'staL',
                charge = -1,
                LeptonNumber = 1,
                GhostNumber = 0)

staL__tilde__ = staL.anti()

selR = Particle(pdg_code = 2000011,
                name = 'selR',
                antiname = 'selR~',
                spin = 1,
                color = 1,
                mass = Param.MslR,
                width = Param.Wsl,
                texname = 'selR',
                antitexname = 'selR',
                charge = -1,
                LeptonNumber = 1,
                GhostNumber = 0)

selR__tilde__ = selR.anti()

smuR = Particle(pdg_code = 2000013,
                name = 'smuR',
                antiname = 'smuR~',
                spin = 1,
                color = 1,
                mass = Param.MslR,
                width = Param.Wsl,
                texname = 'smuR',
                antitexname = 'smuR',
                charge = -1,
                LeptonNumber = 1,
                GhostNumber = 0)

smuR__tilde__ = smuR.anti()

staR = Particle(pdg_code = 2000015,
                name = 'staR',
                antiname = 'staR~',
                spin = 1,
                color = 1,
                mass = Param.MslR,
                width = Param.Wsl,
                texname = 'staR',
                antitexname = 'staR',
                charge = -1,
                LeptonNumber = 1,
                GhostNumber = 0)

staR__tilde__ = staR.anti()

sn1L = Particle(pdg_code = 1000012,
                name = 'sn1L',
                antiname = 'sn1L~',
                spin = 1,
                color = 1,
                mass = Param.MslL,
                width = Param.Wsl,
                texname = 'sn1L',
                antitexname = 'sn1L',
                charge = 0,
                LeptonNumber = 1,
                GhostNumber = 0)

sn1L__tilde__ = sn1L.anti()

sn2L = Particle(pdg_code = 1000014,
                name = 'sn2L',
                antiname = 'sn2L~',
                spin = 1,
                color = 1,
                mass = Param.MslL,
                width = Param.Wsl,
                texname = 'sn2L',
                antitexname = 'sn2L',
                charge = 0,
                LeptonNumber = 1,
                GhostNumber = 0)

sn2L__tilde__ = sn2L.anti()

sn3L = Particle(pdg_code = 1000016,
                name = 'sn3L',
                antiname = 'sn3L~',
                spin = 1,
                color = 1,
                mass = Param.MslL,
                width = Param.Wsl,
                texname = 'sn3L',
                antitexname = 'sn3L',
                charge = 0,
                LeptonNumber = 1,
                GhostNumber = 0)

sn3L__tilde__ = sn3L.anti()

sn1R = Particle(pdg_code = 2000012,
                name = 'sn1R',
                antiname = 'sn1R~',
                spin = 1,
                color = 1,
                mass = Param.MslR,
                width = Param.Wsl,
                texname = 'sn1R',
                antitexname = 'sn1R',
                charge = 0,
                LeptonNumber = 1,
                GhostNumber = 0)

sn1R__tilde__ = sn1R.anti()

sn2R = Particle(pdg_code = 2000014,
                name = 'sn2R',
                antiname = 'sn2R~',
                spin = 1,
                color = 1,
                mass = Param.MslR,
                width = Param.Wsl,
                texname = 'sn2R',
                antitexname = 'sn2R',
                charge = 0,
                LeptonNumber = 1,
                GhostNumber = 0)

sn2R__tilde__ = sn2R.anti()

sn3R = Particle(pdg_code = 2000016,
                name = 'sn3R',
                antiname = 'sn3R~',
                spin = 1,
                color = 1,
                mass = Param.MslR,
                width = Param.Wsl,
                texname = 'sn3R',
                antitexname = 'sn3R',
                charge = 0,
                LeptonNumber = 1,
                GhostNumber = 0)

sn3R__tilde__ = sn3R.anti()

