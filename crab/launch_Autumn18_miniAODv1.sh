#!/bin/sh

dryrun="--dryrun"

# all
python launch.py ${dryrun} --config mc_102X_Autumn18_miniAODv1 --production_label legacy_nano_v1 --remoteDir legacy_nano_v1 --unitsPerJob 2 --publish --module Autumn18_miniAODv1 --sample allSamples
