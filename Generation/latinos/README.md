Latinos instructions
=======

Create list of files

    eos ls /store/user/amassiro/ZH/8TeV/AODSIM/ | awk '{print "   @/store/user/amassiro/ZH/8TeV/AODSIM/"$1"@,"}' | tr "@" "'"

hardcoded in skim.py.

Then

    cmsRun latinosYieldSkim.py.ZHww.py    print  isMC=True globalTag=GR_R_52_V7  outputFile=/tmp/amassiro/latinosYieldSkim_MC_ZHWW_100k.root   correctMetPhi=False





Add variables
====
    
triggW
    
    ./gardener.py efftfiller \
          /data/amassiro/LatinosTrees/nominals_all/latinostep3_latinosYieldSkim_MC_ZHWW_100k_new.root  \
          /data/amassiro/LatinosTrees/nominals_all/latinostep3_latinosYieldSkim_MC_ZHWW_100k_new_weight.root  \
          -f ../data/fit_results.txt


puW

    ./gardener.py  puadder \
                /data/amassiro/LatinosTrees/nominals_all/latinostep3_latinosYieldSkim_MC_ZHWW_100k_new_weight.root  \
                /data/amassiro/LatinosTrees/nominals_all/latinostep3_latinosYieldSkim_MC_ZHWW_100k_new_weight_puW.root \
               --mc=../data/PileupMC_60bin_S10.root    \
               --data=../data/PUdata2012Final.root   \
               --HistName=pileup   \
               --branch=puW  \
               --kind=trpu


effW

    ./gardener.py effwfiller \
            /data/amassiro/LatinosTrees/nominals_all/latinostep3_latinosYieldSkim_MC_ZHWW_100k_new_weight_puW.root  \
            /data/amassiro/LatinosTrees/nominals_all/latinostep3_latinosYieldSkim_MC_ZHWW_100k_new_weight_puW_effW.root \
            --mufile=../data/muons_scale_factors.root \
            --elfile=../data/electrons_scale_factors.root \
            --muname=muonsDATAMCratio_all \
            --elname=electronsDATAMCratio_All_selec
