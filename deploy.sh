#!/bin/bash

Rscript 0-links.R

python 1-html.py

git add . && git commit -m "updates" && git push