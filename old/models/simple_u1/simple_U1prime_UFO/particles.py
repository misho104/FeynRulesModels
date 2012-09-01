# This file was automatically created by FeynRules 1.6.7
# Mathematica version: 8.0 for Mac OS X x86 (64-bit) (October 14, 2011)
# Date: Sat 1 Sep 2012 17:46:10


from __future__ import division
from object_library import all_particles, Particle
import parameters as Param

Zp = Particle(pdg_code = 9000001,
              name = 'Zp',
              antiname = 'Zp',
              spin = 3,
              color = 1,
              mass = Param.mZp,
              width = Param.wZp,
              texname = 'Zp',
              antitexname = 'Zp',
              charge = 0,
              GhostNumber = 0)

g = Particle(pdg_code = 21,
             name = 'g',
             antiname = 'g',
             spin = 3,
             color = 8,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'g',
             antitexname = 'g',
             charge = 0,
             GhostNumber = 0)

ghZp = Particle(pdg_code = 9000002,
                name = 'ghZp',
                antiname = 'ghZp~',
                spin = -1,
                color = 1,
                mass = Param.mZp,
                width = Param.ZERO,
                texname = 'ghZp',
                antitexname = 'ghZp~',
                charge = 0,
                GhostNumber = 1)

ghZp__tilde__ = ghZp.anti()

ghG = Particle(pdg_code = 9000003,
               name = 'ghG',
               antiname = 'ghG~',
               spin = -1,
               color = 8,
               mass = Param.ZERO,
               width = Param.ZERO,
               texname = 'ghG',
               antitexname = 'ghG~',
               charge = 0,
               GhostNumber = 1)

ghG__tilde__ = ghG.anti()

phi = Particle(pdg_code = 9000004,
               name = 'phi',
               antiname = 'phi~',
               spin = 1,
               color = 1,
               mass = Param.mphi,
               width = Param.wphi,
               texname = 'phi',
               antitexname = 'phi~',
               charge = 0,
               GhostNumber = 0)

phi__tilde__ = phi.anti()

psi = Particle(pdg_code = 9000005,
               name = 'psi',
               antiname = 'psi~',
               spin = 2,
               color = 1,
               mass = Param.mpsi,
               width = Param.wpsi,
               texname = 'psi',
               antitexname = 'psi~',
               charge = 0,
               GhostNumber = 0)

psi__tilde__ = psi.anti()

u = Particle(pdg_code = 2,
             name = 'u',
             antiname = 'u~',
             spin = 2,
             color = 3,
             mass = Param.MU,
             width = Param.ZERO,
             texname = 'u',
             antitexname = 'u~',
             charge = 0,
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
             antitexname = 'c~',
             charge = 0,
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
             antitexname = 't~',
             charge = 0,
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
             antitexname = 'd~',
             charge = 0,
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
             antitexname = 's~',
             charge = 0,
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
             antitexname = 'b~',
             charge = 0,
             GhostNumber = 0)

b__tilde__ = b.anti()

