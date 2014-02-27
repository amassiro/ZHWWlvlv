Latinos instructions
=======

Create list of files

    eos ls /store/user/amassiro/ZH/8TeV/AODSIM/ | awk '{print "   @/store/user/amassiro/ZH/8TeV/AODSIM/"$1"@,"}' | tr "@" "'"

hardcoded in skim.py.

Then

    cmsRun latinosYieldSkim.py.ZHww.py    print  isMC=True globalTag=GR_R_52_V7  outputFile=/tmp/amassiro/latinosYieldSkim_MC_ZHWW_100k.root   correctMetPhi=False




