FROM jupyter/minimal-notebook

USER root

ENV CONDA_PYTHON /opt/conda/bin/python
ENV CONDA_PIP /opt/conda/bin/pip
ENV CONDA_IPYTHON /opt/conda/bin/ipython

USER $NB_UID

RUN $CONDA_PIP install pyunicore
RUN $CONDA_IPYTHON profile create

COPY oauth.py /home/jovyan/.ipython/profile_default/startup/start.py
COPY dataset.zip /home/jovyan/pipeline/data/dataset.zip
COPY license.txt /home/jovyan/pipeline/data/license.txt
COPY tvb_pipeline.ipynb /home/jovyan/pipeline/tvb_pipeline.ipynb

USER root

# Adjust permissions on home directory so writable by group root.
RUN chgrp -Rf root /home/$NB_USER && chmod -Rf g+w /home/$NB_USER

USER 1000
WORKDIR /home/jovyan/pipeline

