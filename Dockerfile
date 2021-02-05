FROM rpy2/jupyter
USER root
RUN pip install --no-cache-dir seaborn scikit-learn xlrd

RUN R -e "install.packages('lmerTest',dependencies=TRUE, repos='http://cran.rstudio.com/')"