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
LagNoGhNG=lagr/.{ghG[__]->0, ghGbar[__]->0,ghWp->0,ghWpbar->0,ghWmbar->0,ghWm->0,ghZ->0,ghZbar->0,ghA->0,ghAbar->0, G0->0,GP->0,GPbar->0};
{Definition[lagr],Definition[LagNoGhNG]}>>MSSM.dat


(*sps1a.dat    for CalcHEP; not for Whizard*)
(*sps1a_wo.dat for Whizard; not for CalcHEP*)


SetDirectory[NotebookDirectory[]]
<<FeynRules`
LoadModel["MSSM.fr"];
<<MSSM.dat;
ReadLHAFile[Input->"sps1a.dat"];
WriteRestrictionFile[];LoadRestriction["ZeroValues.rst"];DeleteFile["ZeroValues.rst"];
WriteUFO[lagr, Exclude4Scalars->False];


DeleteDirectory["MSSM_sps1a_UFO",DeleteContents->True];
RenameDirectory["MSSM_UFO","MSSM_sps1a_UFO"];


SetDirectory[NotebookDirectory[]]
<<FeynRules`
LoadModel["MSSM.fr"];
<<MSSM.dat;
ReadLHAFile[Input->"sps1a.dat"];
WriteRestrictionFile[];LoadRestriction["ZeroValues.rst"];DeleteFile["ZeroValues.rst"];
WriteFeynArtsOutput[lagr, Exclude4Scalars->False];


DeleteDirectory["MSSM_sps1a_FA",DeleteContents->True];
RenameDirectory["MSSM_FA","MSSM_sps1a_FA"];


SetDirectory[NotebookDirectory[]]
<<FeynRules`
LoadModel["MSSM.fr"];
<<MSSM.dat;
ReadLHAFile[Input->"nolfv_nocpv.dat"];
WriteRestrictionFile[];LoadRestriction["ZeroValues.rst"];DeleteFile["ZeroValues.rst"];
WriteUFO[lagr, Exclude4Scalars->False];


DeleteDirectory["MSSM_generic_UFO",DeleteContents->True];
RenameDirectory["MSSM_UFO","MSSM_generic_UFO"];


SetDirectory[NotebookDirectory[]]
<<FeynRules`
LoadModel["MSSM.fr"];
<<MSSM.dat;
ReadLHAFile[Input->"nolfv_nocpv.dat"];
WriteRestrictionFile[];LoadRestriction["ZeroValues.rst"];DeleteFile["ZeroValues.rst"];
WriteFeynArtsOutput[lagr, Exclude4Scalars->False];


DeleteDirectory["MSSM_generic_FA",DeleteContents->True];
RenameDirectory["MSSM_FA","MSSM_generic_FA"];
