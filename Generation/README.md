Generation
========

ZHWWlvlv

Where:

    cmsmi5
    /data2/amassiro/Generation/CMSSW_5_3_13/src

Copy:

    cp ZHWWlvlv/Generation/PYTHIA6_Tauola_SM_H_2W_lvlv_zh_zll_mH125_8TeV_cff.py Configuration/GenProduction/python/EightTeV/

Prepare:

    cmsDriver.py Configuration/GenProduction/python/EightTeV/PYTHIA6_Tauola_SM_H_2W_lvlv_zh_zll_mH125_8TeV_cff.py --fileout file:HIG-Summer12-ZHWWlvlv.root --mc --eventcontent RAWSIM --datatier GEN-SIM --conditions START53_V7C::All --beamspot Realistic8TeVCollision --step GEN,SIM  --python_filename HIG-Summer12-ZHWWlvlv_cfg.py -n 10000 --no_exec

Run:

    cmsRun HIG-Summer12-ZHWWlvlv_cfg.py