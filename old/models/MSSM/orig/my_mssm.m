(* ::Package:: *)

(* ::Subsection:: *)
(*Calculate and Save the Lagrangian*)


SetDirectory[NotebookDirectory[]]
<<FeynRules`
LoadModel["mssm.fr"];
lagr=Lag
(*
	WriteRestrictionFile[];
	LoadRestriction["ZeroValues.rst"];
	DeleteFile["ZeroValues.rst"];
*)
Definition[lagr]>>lagrangian.dat


(*sps1a.dat    for CalcHEP; not for Whizard*)
(*sps1a_wo.dat for Whizard; not for CalcHEP*)


SetDirectory[NotebookDirectory[]]
<<FeynRules`
LoadModel["mssm.fr"];
<<lagrangian.dat;
LagFeynman=lagr/.{ghG[__]->0, ghGbar[__]->0,ghWp->0,ghWpbar->0,ghWmbar->0,ghWm->0,ghZ->0,ghZbar->0,ghA->0,ghAbar->0, G0->0,GP->0,GPbar->0};
ReadLHAFile[Input->"sps1a.dat"];
WriteRestrictionFile[]; LoadRestriction["ZeroValues.rst"]; DeleteFile["ZeroValues.rst"];
WriteUFO[LagFeynman, Exclude4Scalars->False];


SetDirectory[NotebookDirectory[]]
<<FeynRules`
LoadModel["mssm.fr"];
<<lagrangian.dat;
LagFeynman=lagr/.{ghG[__]->0, ghGbar[__]->0,ghWp->0,ghWpbar->0,ghWmbar->0,ghWm->0,ghZ->0,ghZbar->0,ghA->0,ghAbar->0, G0->0,GP->0,GPbar->0};
ReadLHAFile[Input->"sps1a.dat"];
WriteRestrictionFile[]; LoadRestriction["ZeroValues.rst"]; DeleteFile["ZeroValues.rst"];
WriteFeynArtsOutput[LagFeynman];



