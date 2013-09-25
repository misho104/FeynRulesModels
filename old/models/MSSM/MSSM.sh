#!/bin/sh

(*sps1a.dat    for CalcHEP; not for Whizard*)
(*sps1a_wo.dat for Whizard; not for CalcHEP*)

MATH=MathKernel

# ------ Lagrangian
rm MSSM.dat
$MATH << _EOC_
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
_EOC_

$MATH <<_EOC_
SetDirectory[NotebookDirectory[]]
<<FeynRules`
LoadModel["MSSM.fr"];
<<MSSM.dat;
ReadLHAFile[Input->"sps1a.dat"];
WriteRestrictionFile[];LoadRestriction["ZeroValues.rst"];DeleteFile["ZeroValues.rst"];
WriteUFO[lagr, Exclude4Scalars->False];
_EOC_
rm -rf MSSM_sps1a_UFO
mv MSSM_UFO MSSM_sps1a_UFO

$MATH <<_EOC_
SetDirectory[NotebookDirectory[]]
<<FeynRules`
LoadModel["MSSM.fr"];
<<MSSM.dat;
ReadLHAFile[Input->"sps1a.dat"];
WriteRestrictionFile[];LoadRestriction["ZeroValues.rst"];DeleteFile["ZeroValues.rst"];
WriteFeynArtsOutput[lagr, Exclude4Scalars->False];
_EOC_
rm -rf MSSM_sps1a_FA
mv MSSM_FA MSSM_sps1a_FA

$MATH <<_EOC_
SetDirectory[NotebookDirectory[]]
<<FeynRules`
LoadModel["MSSM.fr"];
<<MSSM.dat;
ReadLHAFile[Input->"nolfv_nocpv.dat"];
WriteRestrictionFile[];LoadRestriction["ZeroValues.rst"];DeleteFile["ZeroValues.rst"];
WriteUFO[lagr, Exclude4Scalars->False];
_EOC_
rm -rf MSSM_generic_UFO
mv MSSM_UFO MSSM_generic_UFO

$MATH << _EOC_
SetDirectory[NotebookDirectory[]]
<<FeynRules`
LoadModel["MSSM.fr"];
<<MSSM.dat;
ReadLHAFile[Input->"nolfv_nocpv.dat"];
WriteRestrictionFile[];LoadRestriction["ZeroValues.rst"];DeleteFile["ZeroValues.rst"];
WriteFeynArtsOutput[lagr, Exclude4Scalars->False];
_EOC_
rm -rf MSSM_generic_FA
mv MSSM_FA MSSM_generic_FA
