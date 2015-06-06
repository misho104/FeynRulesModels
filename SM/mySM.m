(* ::Package:: *)

SetDirectory[NotebookDirectory[]]
$FeynModelsDirectory=ParentDirectory[]
$FeynRulesPath=ToFileName[{ParentDirectory[],"FeynRules"}]


<<FeynRules`;
FR$Parallelize=False;
LoadModel["SM.fr"];
FeynmanGauge=True;
(*LoadRestriction["Cabibbo.rst","Massless.rst"]*)
WriteUFO[LGauge,LHiggs,LFermions,LYukawa,LGhost];


<<FeynRules`;
FR$Parallelize=False;
LoadModel["SM.fr"];
FeynmanGauge=True;
(*LoadRestriction["Cabibbo.rst","Massless.rst"]*)
WriteFeynArtsOutput[LGauge,LHiggs,LFermions,LYukawa,LGhost,FlavorExpand->SU2W]


SetDirectory[ToFileName[{$FeynModelsDirectory,"SM"}]]
<<FeynRules`;
FR$Parallelize=False;
LoadModel["SM.fr"];
FeynmanGauge=False;
(*LoadRestriction["Cabibbo.rst","Massless.rst"]*)
WriteFeynArtsOutput[LGauge,LHiggs,LFermions,LYukawa,FlavorExpand->SU2W,Output->"Standard_Model_FA_Unitarity"]


CheckHermiticity[LSM,FlavorExpand->True]
CheckMassSpectrum[LSM]
CheckKineticTermNormalisation[LSM,FlavorExpand->True]
CheckDiagonalKineticTerms[LSM]
CheckDiagonalMassTerms[LSM]
CheckDiagonalQuadraticTerms[LSM]


(* Feynman or Unitary :: FA>T/F SH>F MG4>F CH>T WH>T *)
