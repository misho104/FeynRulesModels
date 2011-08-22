(* ::Package:: *)

(* ::Subsection:: *)
(*Calculate and Save the Lagrangian*)


SetDirectory[NotebookDirectory[]]
<<FeynRules`
LoadModel["MSSM.fr"];
lagr=Lag;
(*
	WriteRestrictionFile[];
	LoadRestriction["ZeroValues.rst"];
	DeleteFile["ZeroValues.rst"];
*)
LagFeynman=lagr/.{ghG[__]->0, ghGbar[__]->0,ghWp->0,ghWpbar->0,ghWmbar->0,ghWm->0,ghZ->0,ghZbar->0,ghA->0,ghAbar->0, G0->0,GP->0,GPbar->0};
{Definition[lagr],Definition[LagFeynman]}>>MSSM.dat


SetDirectory[NotebookDirectory[]]
<<FeynRules`
LoadModel["MSSM.fr"];
<<MSSM.dat;
WriteUFO[LagFeynman, Exclude4Scalars->False];


SetDirectory[NotebookDirectory[]]
<<FeynRules`
LoadModel["MSSM.fr"];
<<MSSM.dat;
WriteFeynArtsOutput[LagFeynman];



