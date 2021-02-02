FROM rpy2/jupyter
USER root
RUN pip install --no-cache-dir seaborn scikit-learn xlrd