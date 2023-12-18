#!/bin/sh

wget \
--header="Authorization: Bearer ${HF_TOKEN}" \
--continue \
--no-verbose \
--force-directories \
--no-host-directories \
--cut-dirs=5 \
--directory-prefix=/data \
--input-file=sources.txt
