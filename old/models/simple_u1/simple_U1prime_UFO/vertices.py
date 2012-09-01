# This file was automatically created by FeynRules 1.6.7
# Mathematica version: 8.0 for Mac OS X x86 (64-bit) (October 14, 2011)
# Date: Sat 1 Sep 2012 17:46:10


from object_library import all_vertices, Vertex
import particles as P
import couplings as C
import lorentz as L


V_1 = Vertex(name = 'V_1',
             particles = [ P.Zp, P.phi__tilde__, P.phi ],
             color = [ '1' ],
             lorentz = [ L.VSS1 ],
             couplings = {(0,0):C.GC_4})

V_2 = Vertex(name = 'V_2',
             particles = [ P.Zp, P.Zp, P.phi__tilde__, P.phi ],
             color = [ '1' ],
             lorentz = [ L.VVSS1 ],
             couplings = {(0,0):C.GC_5})

V_3 = Vertex(name = 'V_3',
             particles = [ P.psi__tilde__, P.psi, P.Zp ],
             color = [ '1' ],
             lorentz = [ L.FFV2, L.FFV3 ],
             couplings = {(0,0):C.GC_6,(0,1):C.GC_7})

V_4 = Vertex(name = 'V_4',
             particles = [ P.d__tilde__, P.d, P.g ],
             color = [ 'T(3,2,1)' ],
             lorentz = [ L.FFV1 ],
             couplings = {(0,0):C.GC_1})

V_5 = Vertex(name = 'V_5',
             particles = [ P.s__tilde__, P.s, P.g ],
             color = [ 'T(3,2,1)' ],
             lorentz = [ L.FFV1 ],
             couplings = {(0,0):C.GC_1})

V_6 = Vertex(name = 'V_6',
             particles = [ P.b__tilde__, P.b, P.g ],
             color = [ 'T(3,2,1)' ],
             lorentz = [ L.FFV1 ],
             couplings = {(0,0):C.GC_1})

V_7 = Vertex(name = 'V_7',
             particles = [ P.d__tilde__, P.d, P.Zp ],
             color = [ 'Identity(1,2)' ],
             lorentz = [ L.FFV2, L.FFV3 ],
             couplings = {(0,0):C.GC_2,(0,1):C.GC_3})

V_8 = Vertex(name = 'V_8',
             particles = [ P.s__tilde__, P.s, P.Zp ],
             color = [ 'Identity(1,2)' ],
             lorentz = [ L.FFV2, L.FFV3 ],
             couplings = {(0,0):C.GC_2,(0,1):C.GC_3})

V_9 = Vertex(name = 'V_9',
             particles = [ P.b__tilde__, P.b, P.Zp ],
             color = [ 'Identity(1,2)' ],
             lorentz = [ L.FFV2, L.FFV3 ],
             couplings = {(0,0):C.GC_2,(0,1):C.GC_3})

V_10 = Vertex(name = 'V_10',
              particles = [ P.u__tilde__, P.u, P.g ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_1})

V_11 = Vertex(name = 'V_11',
              particles = [ P.c__tilde__, P.c, P.g ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_1})

V_12 = Vertex(name = 'V_12',
              particles = [ P.t__tilde__, P.t, P.g ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_1})

V_13 = Vertex(name = 'V_13',
              particles = [ P.u__tilde__, P.u, P.Zp ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV3 ],
              couplings = {(0,0):C.GC_8,(0,1):C.GC_9})

V_14 = Vertex(name = 'V_14',
              particles = [ P.c__tilde__, P.c, P.Zp ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV3 ],
              couplings = {(0,0):C.GC_8,(0,1):C.GC_9})

V_15 = Vertex(name = 'V_15',
              particles = [ P.t__tilde__, P.t, P.Zp ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV3 ],
              couplings = {(0,0):C.GC_8,(0,1):C.GC_9})

