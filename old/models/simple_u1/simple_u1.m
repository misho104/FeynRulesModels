(* ::Package:: *)

SetDirectory[NotebookDirectory[]]
<<FeynRules`
LoadModel["simple_u1.fr"]
(* Note: No Nambu-Goldstone, No ghost *)

WriteUFO[Lag]
WriteFeynArtsOutput[Lag]


CheckHermiticity[Lag]
CheckDiagonalKineticTerms[Lag]
CheckDiagonalMassTerms[Lag]
CheckDiagonalQuadraticTerms[Lag]
CheckKineticTermNormalisation[Lag]
CheckMassSpectrum[Lag]



