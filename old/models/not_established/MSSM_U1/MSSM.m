(* ::Package:: *)

(* ::Subsection:: *)
(*Calculate and Save the Lagrangian*)


SetDirectory[NotebookDirectory[]]
<<FeynRules`
LoadModel["MSSM_U1.fr"];
lagr=Lag;
(*
	WriteRestrictionFile[];
	LoadRestriction["ZeroValues.rst"];
	DeleteFile["ZeroValues.rst"];
*)
LagNoGhNG=lagr/.{ghG[__]->0, ghGbar[__]->0,ghWp->0,ghWpbar->0,ghWmbar->0,ghWm->0,ghZ->0,ghZbar->0,ghA->0,ghAbar->0, G0->0,GP->0,GPbar->0};
{Definition[lagr],Definition[LagNoGhNG]}>>MSSM_U1.dat


SetDirectory[NotebookDirectory[]]
<<FeynRules`
LoadModel["MSSM_U1.fr"];
<<MSSM_U1.dat;
ReadLHAFile[Input->"nolfv_nocpv.dat"];
WriteRestrictionFile[];LoadRestriction["ZeroValues.rst"];DeleteFile["ZeroValues.rst"];
WriteUFO[lagr, Exclude4Scalars->False];


SetDirectory[NotebookDirectory[]]
<<FeynRules`
LoadModel["MSSM_U1.fr"];
<<MSSM_U1.dat;
FeynRules`ReadLHAFile[Input->"nolfv_nocpv.dat"];
WriteRestrictionFile[];LoadRestriction["ZeroValues.rst"];DeleteFile["ZeroValues.rst"];
WriteFeynArtsOutput[lagr, Exclude4Scalars->False];
