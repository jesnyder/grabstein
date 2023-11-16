DEFAULT_GOAL:  web


# install requirements
.PHONY: getreqs
getreqs:
	#sudo apt-get clean
	#pip install --upgrade -r reqs.txt

# analyze the dataset
.PHONY: pythonanalysis
pythonanalysis: getreqs
	python3  code/python/a_main.py

#.PHONY: pdf
#pdf: pythonanalysis
#	cp code/latex/report.txt code/latex/report.tex
#	aspell check code/latex/*.tex
#	pdflatex -output-directory=latex code/latex/reportTEX.tex
#	cp code/latex/report.pdf report.pdf

# serve the local directory
.PHONY: web
web: pythonanalysis
	#git add .
	#git commit -m "auto push"
	#git push origin head
	python3 -m http.server --directory docs/
	#python3 -mwebbrowser http://127.0.0.1:8000/report.pdf
