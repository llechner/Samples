'''
miniAOD FastSim samples of Autumn18 campaign, miniAOD (102X)
Get the full list of samples with
dasgoclient -query="dataset=/*/RunIIAutumn18MiniAOD*Fast*/MINIAODSIM"
'''

import copy, os, sys
from RootTools.fwlite.FWLiteSample import FWLiteSample
import ROOT

def get_parser():
    import argparse
    argParser = argparse.ArgumentParser(description = "Argument parser for samples file")
    argParser.add_argument('--overwrite',   action='store_true',    help="Overwrite current entry in db?")
    return argParser

# Logging
if __name__=="__main__":
    import Samples.Tools.logger as logger
    logger = logger.get_logger("INFO", logFile = None )
    import RootTools.core.logger as logger_rt
    logger_rt = logger_rt.get_logger("INFO", logFile = None )
    options = get_parser().parse_args()
    ov = options.overwrite

else:
    import logging
    logger = logging.getLogger(__name__)
    ov = False

from Samples.Tools.config import dbDir, redirector, redirector_global
dbFile = dbDir+"DB_Autumn18_Fast_miniAOD.sql"

logger.info("Using db file: %s", dbFile)

## T2tt
SMS_T2tt_mStop_150to250     = FWLiteSample.fromDAS("SMS_T2tt_mStop_150to250"  , "/SMS-T2tt_mStop-150to250_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-PUFall18Fast_102X_upgrade2018_realistic_v15-v3/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
SMS_T2tt_mStop_250to350     = FWLiteSample.fromDAS("SMS_T2tt_mStop_250to350"  , "/SMS-T2tt_mStop-250to350_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-PUFall18Fast_102X_upgrade2018_realistic_v15-v3/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
SMS_T2tt_mStop_350to400     = FWLiteSample.fromDAS("SMS_T2tt_mStop_350to400"  , "/SMS-T2tt_mStop-350to400_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-PUFall18Fast_102X_upgrade2018_realistic_v15-v3/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
SMS_T2tt_mStop_400to1200    = FWLiteSample.fromDAS("SMS_T2tt_mStop_400to1200" , "/SMS-T2tt_mStop-400to1200_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-PUFall18Fast_102X_upgrade2018_realistic_v15-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
SMS_T2tt_mStop_1200to2000   = FWLiteSample.fromDAS("SMS_T2tt_mStop_1200to2000", "/SMS-T2tt_mStop-1200to2000_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-PUFall18Fast_102X_upgrade2018_realistic_v15-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

T2tt = [
    SMS_T2tt_mStop_150to250  ,
    SMS_T2tt_mStop_250to350  ,
    SMS_T2tt_mStop_350to400  ,
    SMS_T2tt_mStop_400to1200 ,
    SMS_T2tt_mStop_1200to2000,
    ]

SMS_T2bW = FWLiteSample.fromDAS("SMS_T2bW", "/SMS-T2bW_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-PUFall18Fast_102X_upgrade2018_realistic_v15-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

T2bW = [SMS_T2bW]

#SMS_T8bbllnunu_XCha0p5_XSlep0p05              = FWLiteSample.fromDAS("", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
SMS_T8bbllnunu_XCha0p5_XSlep0p05_mN1_700_1000 = FWLiteSample.fromDAS("SMS_T8bbllnunu_XCha0p5_XSlep0p05_mN1_700_1000", "/SMS-T8bbllnunu_XCha0p5_XSlep0p05_mN1_700_1000_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-PUFall18Fast_102X_upgrade2018_realistic_v15-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
SMS_T8bbllnunu_XCha0p5_XSlep0p5               = FWLiteSample.fromDAS("SMS_T8bbllnunu_XCha0p5_XSlep0p5", "/SMS-T8bbllnunu_XCha0p5_XSlep0p5_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-PUFall18Fast_102X_upgrade2018_realistic_v15-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
SMS_T8bbllnunu_XCha0p5_XSlep0p5_mN1_700_1300  = FWLiteSample.fromDAS("SMS_T8bbllnunu_XCha0p5_XSlep0p5_mN1_700_1300", "/SMS-T8bbllnunu_XCha0p5_XSlep0p5_mN1_700_1300_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-PUFall18Fast_102X_upgrade2018_realistic_v15-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
SMS_T8bbllnunu_XCha0p5_XSlep0p95_mN1_0_650    = FWLiteSample.fromDAS("SMS_T8bbllnunu_XCha0p5_XSlep0p95_mN1_0_650", "/SMS-T8bbllnunu_XCha0p5_XSlep0p95_mN1_0_650_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-PUFall18Fast_102X_upgrade2018_realistic_v15-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
SMS_T8bbllnunu_XCha0p5_XSlep0p95_mN1_700_1600 = FWLiteSample.fromDAS("SMS_T8bbllnunu_XCha0p5_XSlep0p95_mN1_700_1600", "/SMS-T8bbllnunu_XCha0p5_XSlep0p95_mN1_700_1600_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-PUFall18Fast_102X_upgrade2018_realistic_v15-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

T8bbllnunu = [ SMS_T8bbllnunu_XCha0p5_XSlep0p05_mN1_700_1000, SMS_T8bbllnunu_XCha0p5_XSlep0p5, SMS_T8bbllnunu_XCha0p5_XSlep0p5_mN1_700_1300, SMS_T8bbllnunu_XCha0p5_XSlep0p95_mN1_0_650, SMS_T8bbllnunu_XCha0p5_XSlep0p95_mN1_700_1600 ]

SMS_T8bbstausnu_XCha0p5_mStop_200to1800_XStau0p25   = FWLiteSample.fromDAS("SMS_T8bbstausnu_XCha0p5_mStop_200to1800_XStau0p25", "/SMS-T8bbstausnu_XCha0p5_mStop-200to1800_XStau0p25_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-PUFall18Fast_102X_upgrade2018_realistic_v15-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
SMS_T8bbstausnu_mStop_200to1800_XCha0p5_XStau0p5    = FWLiteSample.fromDAS("SMS_T8bbstausnu_mStop_200to1800_XCha0p5_XStau0p5",  "/SMS-T8bbstausnu_mStop-200to1800_XCha0p5_XStau0p5_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-PUFall18Fast_102X_upgrade2018_realistic_v15-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
SMS_T8bbstausnu_mStop_200to1800_XCha0p5_XStau0p75   = FWLiteSample.fromDAS("SMS_T8bbstausnu_mStop_200to1800_XCha0p5_XStau0p75", "/SMS-T8bbstausnu_mStop-200to1800_XCha0p5_XStau0p75_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-PUFall18Fast_102X_upgrade2018_realistic_v15-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

T8bbstausnu = [SMS_T8bbstausnu_XCha0p5_mStop_200to1800_XStau0p25, SMS_T8bbstausnu_mStop_200to1800_XCha0p5_XStau0p5, SMS_T8bbstausnu_mStop_200to1800_XCha0p5_XStau0p75 ]

## sum up
allSamples = T2tt + T2bW + T8bbllnunu + T8bbstausnu

for sample in allSamples:
    sample.isData = False

from Samples.Tools.AutoClass import AutoClass
samples = AutoClass( allSamples )
