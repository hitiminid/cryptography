#!/bin/sh

openssl req \
		-x509 \
		-nodes \
		-sha256 \
		-days 30 \
		-newkey rsa:2048 \
		-keyout local.key \
		-out local.crt \
		-subj /CN=localhost