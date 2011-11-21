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


(*sps1a.dat    for CalcHEP; not for Whizard*)
(*sps1a_wo.dat for Whizard; not for CalcHEP*)


SetDirectory[NotebookDirectory[]]
<<FeynRules`
LoadModel["MSSM.fr"];
<<MSSM.dat;
ReadLHAFile[Input->"sps1a.dat"];
\[AliasDelimiter]WriteUFO[LagFeynman, Exclude4Scalars->False];


SetDirectory[NotebookDirectory[]]
<<FeynRules`
LoadModel["MSSM.fr"];
<<MSSM.dat;
ReadLHAFile[Input->"sps1a.dat"];
WriteRestrictionFile[];LoadRestriction["ZeroValues.rst"];DeleteFile["ZeroValues.rst"];
WriteFeynArtsOutput[LagFeynman, Exclude4Scalars->False];



