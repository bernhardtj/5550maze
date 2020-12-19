#!/bin/bash
rsync -aP --delete "$(dirname "${BASH_SOURCE[0]}")"/ "ubuntu@$(cat ../elasticip):finalfiles"
ssh -l ubuntu "$(cat ../elasticip)" bash finalfiles/setup.sh
