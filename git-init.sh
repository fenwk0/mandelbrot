#!/bin/bash
#echo "# mandelbrot" >> README.md
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:fenwk0/mandelbrot.git
git push -u origin main
