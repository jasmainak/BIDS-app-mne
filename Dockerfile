FROM continuumio/anaconda

RUN pip install mne

COPY run.py /run.py

COPY version /version

ENTRYPOINT ["/run.py"]

