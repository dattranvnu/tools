#!/bin/bash

mkdir outputs 

Rscript 0-links.R

python 1-html.py

Rscript 2-Rmd.R

git add .

git commit -m "updates"

git push