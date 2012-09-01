(* ::Package:: *)

Exit[]


SetDirectory[NotebookDirectory[]]
<<FeynRules`
LoadModel[FileNameJoin[{"..","SM","SM.fr"}],"u1prime.fr"]
(* Note: No Nambu-Goldstone, No SSB *)
FeynmanGauge=True;
WriteUFO[LGauge,LHiggs,LFermions,LYukawa,LGhost,LCHI]
WriteFeynArtsOutput[LGauge,LHiggs,LFermions,LYukawa,LGhost,LCHI]


Lag=LGauge+LHiggs+LFermions+LYukawa+LGhost+LCHI;
CheckHermiticity[Lag]
CheckDiagonalKineticTerms[Lag]
CheckDiagonalMassTerms[Lag]
CheckDiagonalQuadraticTerms[Lag]
CheckKineticTermNormalisation[Lag]
CheckMassSpectrum[Lag]





GetKineticTerms[Lag]


GetMassTerms[Lag]


LCHI
