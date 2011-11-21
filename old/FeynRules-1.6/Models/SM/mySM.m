(* ::Package:: *)

SetDirectory[ToFileName[{$FeynModelsDirectory,"SM"}]]
<<FeynRules`;
LoadModel["SM.fr"];
FeynmanGauge=True;
(*LoadRestriction["Cabibbo.rst","Massless.rst"]*)
WriteUFO[LGauge,LHiggs,LFermions,LYukawa,LGhost];


SetDirectory[ToFileName[{$FeynModelsDirectory,"SM"}]]
<<FeynRules`;
LoadModel["SM.fr"];
FeynmanGauge=True;
(*LoadRestriction["Cabibbo.rst","Massless.rst"]*)
WriteFeynArtsOutput[LGauge,LHiggs,LFermions,LYukawa,LGhost];


CheckHermiticity[LSM,FlavorExpand->True]
CheckMassSpectrum[LSM]
CheckKineticTermNormalisation[LSM,FlavorExpand->True]
CheckDiagonalKineticTerms[LSM]
CheckDiagonalMassTerms[LSM]
CheckDiagonalQuadraticTerms[LSM]


(* Feynman or Unitary :: FA>T/F SH>F MG4>F CH>T WH>T *)
