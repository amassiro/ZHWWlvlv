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

Prepare RECO:

First add PU:

    cmsDriver.py step1  --filein "file:HIG-Summer12-ZHWWlvlv-test.root" --fileout file:step1-ZHWWlvlv.root --pileup_input "dbs:/MinBias_TuneZ2star_8TeV-pythia6/Summer12-START50_V13-v3/GEN-SIM" --mc --eventcontent RAWSIM --pileup 2012_Summer_50ns_PoissonOOTPU --datatier GEN-SIM-RAW --conditions START53_V19::All --step DIGI,L1,DIGI2RAW,HLT:7E33v2  --python_filename DIGI-HZWWlvlv_cfg.py --no_exec -n -1

    cmsRun DIGI-HZWWlvlv_cfg.py

    it takes a lot!

Then run RECO-AOD

    cmsDriver.py step2 --filein file:step1-ZHWWlvlv.root --fileout file:AODSIM-ZHWWlvlv.root --mc --eventcontent AODSIM,DQM --datatier AODSIM,DQM --conditions START53_V19::All --step RAW2DIGI,L1Reco,RECO,VALIDATION:validation_prod,DQM:DQMOfflinePOGMC  --python_filename AODSIM-HZWWlvlv_cfg.py --no_exec -n -1  --no_exec

    cmsRun AODSIM-HZWWlvlv_cfg.py

