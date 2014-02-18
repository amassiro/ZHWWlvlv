# Auto generated configuration file
# using: 
# Revision: 1.381.2.28 
# Source: /local/reps/CMSSW/CMSSW/Configuration/PyReleaseValidation/python/ConfigBuilder.py,v 
# with command line options: Configuration/GenProduction/python/EightTeV/PYTHIA6_Tauola_SM_H_2W_lvlv_zh_zll_mH125_8TeV_cff.py --fileout file:HIG-Summer12-ZHWWlvlv.root --mc --eventcontent RAWSIM --datatier GEN-SIM --conditions START53_V7C::All --beamspot Realistic8TeVCollision --step GEN,SIM --python_filename HIG-Summer12-ZHWWlvlv_cfg.py
import FWCore.ParameterSet.Config as cms

process = cms.Process('SIM')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.GeometrySimDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic8TeVCollision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')


from FWCore.ParameterSet.VarParsing import VarParsing
options = VarParsing ('analysis')
# add a list of strings for events to process
options.parseArguments()


process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(NUMBEREVENTS)
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.2 $'),
    annotation = cms.untracked.string('PYTHIA6 WH/ZH/ttH, H->WW mH=125GeV with TAUOLA at 8TeV'),
    name = cms.untracked.string('$Source: /cvs_server/repositories/CMSSW/CMSSW/Configuration/GenProduction/python/Attic/PYTHIA6_Tauola_SM_H_2W_wh_zh_tth_mH125_8TeV_cff.py,v $')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    fileName = cms.untracked.string(options.outputFile),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('GEN-SIM')
    ),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    )
)

# Additional output definition

# Other statements
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'START53_V7C::All', '')

process.generator = cms.EDFilter("Pythia6GeneratorFilter",
    ExternalDecays = cms.PSet(
        Tauola = cms.untracked.PSet(
            UseTauolaPolarization = cms.bool(True),
            InputCards = cms.PSet(
                mdtau = cms.int32(0),
                pjak2 = cms.int32(0),
                pjak1 = cms.int32(0)
            )
        ),
        parameterSets = cms.vstring('Tauola')
    ),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(8000.0),
    crossSection = cms.untracked.double(1.0),
    maxEventsToPrint = cms.untracked.int32(1),
    PythiaParameters = cms.PSet(
        pythiaUESettings = cms.vstring('MSTU(21)=1     ! Check on possible errors during program execution', 
            'MSTJ(22)=2     ! Decay those unstable particles', 
            'PARJ(71)=10 .  ! for which ctau  10 mm', 
            'MSTP(33)=0     ! no K factors in hard cross sections', 
            'MSTP(2)=1      ! which order running alphaS', 
            'MSTP(51)=10042 ! structure function chosen (external PDF CTEQ6L1)', 
            'MSTP(52)=2     ! work with LHAPDF', 
            'PARP(82)=1.921 ! pt cutoff for multiparton interactions', 
            'PARP(89)=1800. ! sqrts for which PARP82 is set', 
            'PARP(90)=0.227 ! Multiple interactions: rescaling power', 
            'MSTP(95)=6     ! CR (color reconnection parameters)', 
            'PARP(77)=1.016 ! CR', 
            'PARP(78)=0.538 ! CR', 
            'PARP(80)=0.1   ! Prob. colored parton from BBR', 
            'PARP(83)=0.356 ! Multiple interactions: matter distribution parameter', 
            'PARP(84)=0.651 ! Multiple interactions: matter distribution parameter', 
            'PARP(62)=1.025 ! ISR cutoff', 
            'MSTP(91)=1     ! Gaussian primordial kT', 
            'PARP(93)=10.0  ! primordial kT-max', 
            'MSTP(81)=21    ! multiple parton interactions 1 is Pythia default', 
            'MSTP(82)=4     ! Defines the multi-parton model'),
        processParameters = cms.vstring('PMAS(25,1)=125.0 !mass of Higgs', 
            'MSEL=0 ! user selection for process', 
            'MSUB(102)=0 !ggH', 
            'MSUB(123)=0 !ZZ fusion to H', 
            'MSUB(124)=0 !WW fusion to H', 
            'MSUB(24)=1 !ZH production', 
            'MSUB(26)=0 !WH production', 
            'MSUB(121)=0 !gg to ttH', 
            'MSUB(122)=0 !qq to ttH', 
            'MDME(210,1)=0 !Higgs decay into dd', 
            'MDME(211,1)=0 !Higgs decay into uu', 
            'MDME(212,1)=0 !Higgs decay into ss', 
            'MDME(213,1)=0 !Higgs decay into cc', 
            'MDME(214,1)=0 !Higgs decay into bb', 
            'MDME(215,1)=0 !Higgs decay into tt', 
            'MDME(216,1)=0 !Higgs decay into', 
            'MDME(217,1)=0 !Higgs decay into Higgs decay', 
            'MDME(218,1)=0 !Higgs decay into e nu e', 
            'MDME(219,1)=0 !Higgs decay into mu nu mu', 
            'MDME(220,1)=0 !Higgs decay into tau nu tau', 
            'MDME(221,1)=0 !Higgs decay into Higgs decay', 
            'MDME(222,1)=0 !Higgs decay into g g', 
            'MDME(223,1)=0 !Higgs decay into gam gam', 
            'MDME(224,1)=0 !Higgs decay into gam Z', 
            'MDME(225,1)=0 !Higgs decay into Z Z', 
            'MDME(226,1)=1 !Higgs decay into W W', 
            'MDME(190,1)=0 ! W decay into dbar u', 
            'MDME(191,1)=0 ! W decay into dbar c', 
            'MDME(192,1)=0 ! W decay into dbar t', 
            'MDME(194,1)=0 ! W decay into sbar u', 
            'MDME(195,1)=0 ! W decay into sbar c', 
            'MDME(196,1)=0 ! W decay into sbar t', 
            'MDME(198,1)=0 ! W decay into bbar u', 
            'MDME(199,1)=0 ! W decay into bbar c', 
            'MDME(200,1)=0 ! W decay into bbar t', 
            'MDME(206,1)=1 ! W decay into e+ nu_e', 
            'MDME(207,1)=1 ! W decay into mu+ nu_mu', 
            'MDME(208,1)=1 ! W decay into tau+ nu_tauMDME(174,1)=0 !Z decay into d dbar', 
            'MDME(175,1)=0 !Z decay into u ubar', 
            'MDME(176,1)=0 !Z decay into s sbar', 
            'MDME(177,1)=0 !Z decay into c cbar', 
            'MDME(178,1)=0 !Z decay into b bbar', 
            'MDME(179,1)=0 !Z decay into t tbar', 
            'MDME(180,1)=0 !Z decay into b* b*bar', 
            'MDME(181,1)=0 !Z decay into t* t*bar', 
            'MDME(182,1)=1 !Z decay into e- e+', 
            'MDME(183,1)=0 !Z decay into nu_e nu_ebar', 
            'MDME(184,1)=1 !Z decay into mu- mu+', 
            'MDME(185,1)=0 !Z decay into nu_mu nu_mubar', 
            'MDME(187,1)=0 !Z decay into nu_tau nu_taubar', 
            'MDME(188,1)=1 !Z decay into tau* tau*bar', 
            'MDME(189,1)=0 !Z decay into nu_tau* nu_tau*bar'),
        parameterSets = cms.vstring('pythiaUESettings', 
            'processParameters')
    )
)


process.ProductionFilterSequence = cms.Sequence(process.generator)

# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

####################################
# important for lxbatch processing #
import random
process.RandomNumberGeneratorService.generator.initialSeed = cms.untracked.uint32(YOURSEED)
####################################

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.simulation_step,process.endjob_step,process.RAWSIMoutput_step)
# filter all path with the production filter sequence
for path in process.paths:
    getattr(process,path)._seq = process.ProductionFilterSequence * getattr(process,path)._seq 

