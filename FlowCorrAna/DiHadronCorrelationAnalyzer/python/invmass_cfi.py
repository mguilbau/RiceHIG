import FWCore.ParameterSet.Config as cms

invmass_ana = cms.EDAnalyzer('InvMassAnalyzer',

  TrgTrackCollection = cms.string('generalTracks'),
  VertexCollection = cms.string('offlinePrimaryVertices'),
  GenParticleCollection = cms.string('genParticles'),
  V0CandidateCollection = cms.string('generalV0CandidatesNew'),

  TriggerID = cms.string('Kshort'),
  AssociateID = cms.string('Track'),

  NEtaBins = cms.int32(40),
  NPhiBins = cms.int32(36),
  checksign = cms.int32(-1),

  nmin = cms.int32(-1),
  nmax = cms.int32(-1),
  centmin = cms.int32(-1),
  centmax = cms.int32(-1),
  zvtxmin = cms.double(-150),
  zvtxmax = cms.double(150),
  zvtxbin = cms.double(300),
  rhomin = cms.double(0.0),
  rhomax = cms.double(0.2),
  xvtxcenter = cms.double(0.075),
  yvtxcenter = cms.double(0.07),
  zvtxcenter = cms.double(-0.3),
  etatrgmin = cms.double(-2.4),
  etatrgmax = cms.double(2.4),
  etaassmin = cms.double(-2.4),
  etaassmax = cms.double(2.4),
  pttrgmin = cms.vdouble(0.0),
  pttrgmax = cms.vdouble(10000.0),
  ptassmin = cms.vdouble(0.0),
  ptassmax = cms.vdouble(10000.0),
  etamultmin = cms.double(-2.4),
  etamultmax = cms.double(2.4),
  chargeasymmin = cms.double(-9999.9),
  chargeasymmax = cms.double(9999.9),
  nvtxmax = cms.int32(9999),
  etacms = cms.double(0.0),
  ptmultmin = cms.double(0.4),
  ptmultmax = cms.double(10000),
  runmin = cms.int32(-1),
  runmax = cms.int32(-1),

  mass_trg = cms.double(0.139570),
  mass_ass = cms.double(0.139570),
  genpdgId_trg = cms.int32(-999999),
  genpdgId_ass = cms.int32(-999999),
  isstable_trg = cms.bool(True),
  isstable_ass = cms.bool(True),
  ischarge_trg = cms.bool(True),
  ischarge_ass = cms.bool(True),

  IsGenMult = cms.bool(False),
  IsVtxSel = cms.bool(True),
  IsCorr = cms.bool(True),
  IsHI = cms.bool(True),
  IsFullMatrix = cms.bool(True),
  IsPtWeightTrg = cms.bool(False),
  IsPtWeightAss = cms.bool(False),
  IsTrgEtaCutAbs = cms.bool(False),
  IsAssEtaCutAbs = cms.bool(False),
  IsHITrkQuality = cms.bool(False),
  IsPPTrkQuality = cms.bool(True),
  IsDebug = cms.bool(False),
  IsInvMass = cms.bool(True),
  IsEventEngineer = cms.bool(False),

  EffFileName = cms.string(''),
  EtaPhiFileName = cms.string(''),
)
