#!/bin/bash
source /home/djones/yse_crons/yse_envs.sourceme
source /data/yse_pz/yse_virtual/bin/activate
python /data/yse_pz/YSE_PZ/manage.py runcrons YSE_App.data_ingest.TNS_uploads.TNS_recent_realtime --force
echo "============"
