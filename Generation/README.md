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

    it takes a lot: ~ 20 seconds/event

Then run RECO-AOD

    cmsDriver.py step2 --filein file:step1-ZHWWlvlv.root --fileout file:AODSIM-ZHWWlvlv.root --mc --eventcontent AODSIM,DQM --datatier AODSIM,DQM --conditions START53_V19::All --step RAW2DIGI,L1Reco,RECO,VALIDATION:validation_prod,DQM:DQMOfflinePOGMC  --python_filename AODSIM-HZWWlvlv_cfg.py --no_exec -n -1  --no_exec

    cmsRun AODSIM-HZWWlvlv_cfg.py

    it takes a lot: ~ 5 seconds/event





Latinos
========

Where:

    cmsneu
    /home/amassiro/Latinos/CMSSW_5_3_11_patch6/src/WWAnalysis/AnalysisStep/test/step3

step1:

    cmsRun latinosYieldSkim.py.ZHww.py    print  isMC=True globalTag=GR_R_52_V7  outputFile=/tmp/amassiro/latinosYieldSkim_MC_ZHWW_100k.root   correctMetPhi=False   &> tmp_dump.txt

step2+3: need to split in different sub-samples, because >30k events has big memory leak

    cmsRun step3.py print inputFiles=file:/tmp/amassiro/latinosYieldSkim_MC_ZHWW.root  label=WW id=3125  scale=0.0000946393141653604743 outputFile=/tmp/amassiro/step3_latinosYieldSkim_MC_ZHWW.root
    3.51494077427652715e-04   = 0.412 / (0.412 + 0.704 + 0.128) * (3*0.108 *3*0.108) * (3*0.0337) * 1000 / 10000
    9.46393141653604743e-05   = 3.36558/100. * 3 * (3*0.108 *3*0.108)  * 21.5 / 100.  * 0.4153  * 1000 / 10000

    cmsRun step3.py print inputFiles=file:/tmp/amassiro/latinosYieldSkim_MC_ZHWW_100k.root     label=WW id=3125  scale=0.00000946393141653604743 outputFile=/tmp/amassiro/step3_latinosYieldSkim_MC_ZHWW_100k.root doHiggs=True   acceptDuplicates=True
    
    cmsRun step3.py print inputFiles=file:/tmp/amassiro/latinosYieldSkim_MC_ZHWW_100k.root     label=WW id=3125  scale=0.00000946393141653604743 outputFile=/tmp/amassiro/step3_latinosYieldSkim_MC_ZHWW_100k_0.root doHiggs=True   acceptDuplicates=True  maxEvents=10000  skipEvents=0
    cmsRun step3.py print inputFiles=file:/tmp/amassiro/latinosYieldSkim_MC_ZHWW_100k.root     label=WW id=3125  scale=0.00000946393141653604743 outputFile=/tmp/amassiro/step3_latinosYieldSkim_MC_ZHWW_100k_1.root doHiggs=True   acceptDuplicates=True  maxEvents=10000  skipEvents=10000
    cmsRun step3.py print inputFiles=file:/tmp/amassiro/latinosYieldSkim_MC_ZHWW_100k.root     label=WW id=3125  scale=0.00000946393141653604743 outputFile=/tmp/amassiro/step3_latinosYieldSkim_MC_ZHWW_100k_2.root doHiggs=True   acceptDuplicates=True  maxEvents=10000  skipEvents=20000
    cmsRun step3.py print inputFiles=file:/tmp/amassiro/latinosYieldSkim_MC_ZHWW_100k.root     label=WW id=3125  scale=0.00000946393141653604743 outputFile=/tmp/amassiro/step3_latinosYieldSkim_MC_ZHWW_100k_3.root doHiggs=True   acceptDuplicates=True  maxEvents=10000  skipEvents=30000
    cmsRun step3.py print inputFiles=file:/tmp/amassiro/latinosYieldSkim_MC_ZHWW_100k.root     label=WW id=3125  scale=0.00000946393141653604743 outputFile=/tmp/amassiro/step3_latinosYieldSkim_MC_ZHWW_100k_4.root doHiggs=True   acceptDuplicates=True  maxEvents=10000  skipEvents=40000
    cmsRun step3.py print inputFiles=file:/tmp/amassiro/latinosYieldSkim_MC_ZHWW_100k.root     label=WW id=3125  scale=0.00000946393141653604743 outputFile=/tmp/amassiro/step3_latinosYieldSkim_MC_ZHWW_100k_5.root doHiggs=True   acceptDuplicates=True  maxEvents=10000  skipEvents=50000
    cmsRun step3.py print inputFiles=file:/tmp/amassiro/latinosYieldSkim_MC_ZHWW_100k.root     label=WW id=3125  scale=0.00000946393141653604743 outputFile=/tmp/amassiro/step3_latinosYieldSkim_MC_ZHWW_100k_6.root doHiggs=True   acceptDuplicates=True  maxEvents=10000  skipEvents=60000
    cmsRun step3.py print inputFiles=file:/tmp/amassiro/latinosYieldSkim_MC_ZHWW_100k.root     label=WW id=3125  scale=0.00000946393141653604743 outputFile=/tmp/amassiro/step3_latinosYieldSkim_MC_ZHWW_100k_7.root doHiggs=True   acceptDuplicates=True  maxEvents=10000  skipEvents=70000
    cmsRun step3.py print inputFiles=file:/tmp/amassiro/latinosYieldSkim_MC_ZHWW_100k.root     label=WW id=3125  scale=0.00000946393141653604743 outputFile=/tmp/amassiro/step3_latinosYieldSkim_MC_ZHWW_100k_8.root doHiggs=True   acceptDuplicates=True  maxEvents=10000  skipEvents=80000
    cmsRun step3.py print inputFiles=file:/tmp/amassiro/latinosYieldSkim_MC_ZHWW_100k.root     label=WW id=3125  scale=0.00000946393141653604743 outputFile=/tmp/amassiro/step3_latinosYieldSkim_MC_ZHWW_100k_9.root doHiggs=True   acceptDuplicates=True  maxEvents=10000  skipEvents=90000
    
    
    9.46393141653604709e-06   = 3.36558/100. * 3 * (3*0.108 *3*0.108)  * 21.5 / 100.  * 0.4153  * 1000 / 100000

    python ucsd2latino.py /tmp/amassiro/step3_latinosYieldSkim_MC_ZHWW.root
    python ucsd2latino.py /tmp/amassiro/step3_latinosYieldSkim_MC_ZHWW_100k.root

    python ucsd2latino.py /tmp/amassiro/step3_latinosYieldSkim_MC_ZHWW_100k_0_numEvent10000.root
    python ucsd2latino.py /tmp/amassiro/step3_latinosYieldSkim_MC_ZHWW_100k_1_numEvent10000.root
    python ucsd2latino.py /tmp/amassiro/step3_latinosYieldSkim_MC_ZHWW_100k_2_numEvent10000.root
    python ucsd2latino.py /tmp/amassiro/step3_latinosYieldSkim_MC_ZHWW_100k_3_numEvent10000.root
    python ucsd2latino.py /tmp/amassiro/step3_latinosYieldSkim_MC_ZHWW_100k_4_numEvent10000.root
    python ucsd2latino.py /tmp/amassiro/step3_latinosYieldSkim_MC_ZHWW_100k_5_numEvent10000.root
    python ucsd2latino.py /tmp/amassiro/step3_latinosYieldSkim_MC_ZHWW_100k_6_numEvent10000.root
    python ucsd2latino.py /tmp/amassiro/step3_latinosYieldSkim_MC_ZHWW_100k_7_numEvent10000.root
    python ucsd2latino.py /tmp/amassiro/step3_latinosYieldSkim_MC_ZHWW_100k_8_numEvent10000.root
    python ucsd2latino.py /tmp/amassiro/step3_latinosYieldSkim_MC_ZHWW_100k_9_numEvent10000.root

    rm latinostep3_latinosYieldSkim_MC_ZHWW_100k.root
    hadd latinostep3_latinosYieldSkim_MC_ZHWW_100k.root  latinostep3_latinosYieldSkim_MC_ZHWW_100k_?_numEvent10000.root

