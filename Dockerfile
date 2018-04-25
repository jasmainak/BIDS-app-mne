FROM continuumio/anaconda

RUN pip install --upgrade mne

COPY run.py /run.py

ENTRYPOINT ["python", "/run.py"]

