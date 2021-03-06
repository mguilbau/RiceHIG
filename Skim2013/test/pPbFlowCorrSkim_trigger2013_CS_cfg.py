import FWCore.ParameterSet.Config as cms
process = cms.Process("ANASKIM")

process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.StandardSequences.GeometryDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('HeavyIonsAnalysis.Configuration.collisionEventSelection_cff')
process.load('Configuration.EventContent.EventContentHeavyIons_cff')

process.source = cms.Source("PoolSource",
   fileNames = cms.untracked.vstring(
'/store/group/phys_heavyions/icali/PAPhysics/pAPilotRun_Run202792GoodLumis_RAWRECO_L1Em_PrescaleActiveBitsSkimNoZB_CMSSW528_V94_FinalWorkflow_200kHz_v2_v1_v2/f3394926c5028783289fd2cd57b36909/PAPhysics_RAWRECO_inRECO_5_1_xbV.root'
)
)

# =============== Other Statements =====================
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(100))
process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))
process.GlobalTag.globaltag = 'GR_P_V41::All'

# =============== Import Sequences =====================
process.load("davidlw.HighPtFlow2011.ppExtraReco_cff")

#Trigger Selection
### Comment out for the timing being assuming running on secondary dataset with trigger bit selected already
import HLTrigger.HLTfilters.hltHighLevel_cfi
process.hltHM100 = HLTrigger.HLTfilters.hltHighLevel_cfi.hltHighLevel.clone()
process.hltHM100.HLTPaths = ['HLT_PAPixelTracks_Multiplicity100_*']
process.hltHM100.andOr = cms.bool(True)
process.hltHM100.throw = cms.bool(False)

process.hltHM190 = process.hltHM100.clone()
process.hltHM190.HLTPaths = ['HLT_PAPixelTracks_Multiplicity190_*']
process.hltHM220 = process.hltHM100.clone()
process.hltHM220.HLTPaths = ['HLT_PAPixelTracks_Multiplicity220_*']
process.hltHM100Pt12 = process.hltHM100.clone()
process.hltHM100Pt12.HLTPaths = ['HLT_PAPixelTrackMultiplicity100_FullTrack12_*']
process.hltHM130Pt12 = process.hltHM100.clone()
process.hltHM130Pt12.HLTPaths = ['HLT_PAPixelTrackMultiplicity130_FullTrack12_*']
process.hltHM160Pt12 = process.hltHM100.clone()
process.hltHM160Pt12.HLTPaths = ['HLT_PAPixelTrackMultiplicity160_FullTrack12_*']
process.hltHF170 = process.hltHM100.clone()
process.hltHF170.HLTPaths = ['HLT_PAHFSumET170_*']
process.hltHF210 = process.hltHM100.clone()
process.hltHF210.HLTPaths = ['HLT_PAHFSumET210_*']

process.eventFilter_HM190 = cms.Sequence(
    process.hltHM190 *
    process.PAcollisionEventSelection )
process.eventFilter_HM190_step = cms.Path( process.eventFilter_HM190 )
process.extraTrks_HM190_step   = cms.Path( process.eventFilter_HM190 * process.ppSingleTrackFilterSequence )

process.eventFilter_HM220 = cms.Sequence(
    process.hltHM220 *
    process.PAcollisionEventSelection )
process.eventFilter_HM220_step = cms.Path( process.eventFilter_HM220 )
process.extraTrks_HM220_step   = cms.Path( process.eventFilter_HM220 * process.ppSingleTrackFilterSequence )

process.eventFilter_HM100Pt12 = cms.Sequence(
    process.hltHM100Pt12 *
    process.PAcollisionEventSelection )
process.eventFilter_HM100Pt12_step = cms.Path( process.eventFilter_HM100Pt12 )
process.extraTrks_HM100Pt12_step   = cms.Path( process.eventFilter_HM100Pt12 * process.ppSingleTrackFilterSequence )

process.eventFilter_HM130Pt12 = cms.Sequence(
    process.hltHM130Pt12 *
    process.PAcollisionEventSelection )
process.eventFilter_HM130Pt12_step = cms.Path( process.eventFilter_HM130Pt12 )
process.extraTrks_HM130Pt12_step   = cms.Path( process.eventFilter_HM130Pt12 * process.ppSingleTrackFilterSequence )

process.eventFilter_HM160Pt12 = cms.Sequence(
    process.hltHM160Pt12 *
    process.PAcollisionEventSelection )
process.eventFilter_HM160Pt12_step = cms.Path( process.eventFilter_HM160Pt12 )
process.extraTrks_HM160Pt12_step   = cms.Path( process.eventFilter_HM160Pt12 * process.ppSingleTrackFilterSequence )

process.eventFilter_HF170 = cms.Sequence(
    process.hltHF170 *
    process.PAcollisionEventSelection )
process.eventFilter_HF170_step = cms.Path( process.eventFilter_HF170 )
process.extraTrks_HF170_step   = cms.Path( process.eventFilter_HF170 * process.ppSingleTrackFilterSequence )

process.eventFilter_HF210 = cms.Sequence(
    process.hltHF210 *
    process.PAcollisionEventSelection )
process.eventFilter_HF210_step = cms.Path( process.eventFilter_HF210 )
process.extraTrks_HF210_step   = cms.Path( process.eventFilter_HF210 * process.ppSingleTrackFilterSequence )

process.load("davidlw.HighPtFlow2011.ppanalysisSkimContentFull_cff")
process.output_HM100 = cms.OutputModule("PoolOutputModule",
    outputCommands = process.analysisSkimContent.outputCommands,
    fileName = cms.untracked.string('pPb_HM100.root'),
    SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('eventFilter_HM100_step')),
    dataset = cms.untracked.PSet(
      dataTier = cms.untracked.string('AOD'),
      filterName = cms.untracked.string('pPb_HM100'))
)
process.output_HM190 = process.output_HM100.clone()
process.output_HM190.fileName = cms.untracked.string('pPb_HM190.root')
process.output_HM190.SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('eventFilter_HM190_step'))
process.output_HM190.dataset.filterName = cms.untracked.string('pPb_HM190')
process.output_HM220 = process.output_HM100.clone()
process.output_HM220.fileName = cms.untracked.string('pPb_HM220.root')
process.output_HM220.SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('eventFilter_HM220_step'))
process.output_HM220.dataset.filterName = cms.untracked.string('pPb_HM220')
process.output_HM100Pt12 = process.output_HM100.clone()
process.output_HM100Pt12.fileName = cms.untracked.string('pPb_HM100Pt12.root')
process.output_HM100Pt12.SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('eventFilter_HM100Pt12_step'))
process.output_HM100Pt12.dataset.filterName = cms.untracked.string('pPb_HM100Pt12')
process.output_HM130Pt12 = process.output_HM100.clone()
process.output_HM130Pt12.fileName = cms.untracked.string('pPb_HM130Pt12.root')
process.output_HM130Pt12.SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('eventFilter_HM130Pt12_step'))
process.output_HM130Pt12.dataset.filterName = cms.untracked.string('pPb_HM130Pt12')
process.output_HM160Pt12 = process.output_HM100.clone()
process.output_HM160Pt12.fileName = cms.untracked.string('pPb_HM160Pt12.root')
process.output_HM160Pt12.SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('eventFilter_HM160Pt12_step'))
process.output_HM160Pt12.dataset.filterName = cms.untracked.string('pPb_HM160Pt12')
process.output_HF170 = process.output_HM100.clone()
process.output_HF170.fileName = cms.untracked.string('pPb_HF170.root')
process.output_HF170.SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('eventFilter_HF170_step'))
process.output_HF170.dataset.filterName = cms.untracked.string('pPb_HF170')
process.output_HF210 = process.output_HM100.clone()
process.output_HF210.fileName = cms.untracked.string('pPb_HF210.root')
process.output_HF210.SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('eventFilter_HF210_step'))
process.output_HF210.dataset.filterName = cms.untracked.string('pPb_HF210')

process.output_HM190_step = cms.EndPath(process.output_HM190)
process.output_HM220_step = cms.EndPath(process.output_HM220)
process.output_HM100Pt12_step = cms.EndPath(process.output_HM100Pt12)
process.output_HM130Pt12_step = cms.EndPath(process.output_HM130Pt12)
process.output_HM160Pt12_step = cms.EndPath(process.output_HM160Pt12)
process.output_HF170_step = cms.EndPath(process.output_HF170)
process.output_HF210_step = cms.EndPath(process.output_HF210)

process.schedule = cms.Schedule(
    process.eventFilter_HM190_step,
    process.eventFilter_HM220_step,
    process.eventFilter_HM100Pt12_step,
    process.eventFilter_HM130Pt12_step,
    process.eventFilter_HM160Pt12_step,
    process.eventFilter_HF170_step,
    process.eventFilter_HF210_step,
    process.extraTrks_HM190_step,
    process.extraTrks_HM220_step,
    process.extraTrks_HM100Pt12_step,
    process.extraTrks_HM130Pt12_step,
    process.extraTrks_HM160Pt12_step,
    process.extraTrks_HF170_step,
    process.extraTrks_HF210_step,
    process.output_HM190_step,
    process.output_HM220_step,
    process.output_HM100Pt12_step,
    process.output_HM130Pt12_step,
    process.output_HM160Pt12_step,
    process.output_HF170_step,
    process.output_HF210_step
)
