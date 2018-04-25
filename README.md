$ docker build . -t mne-app

$ mkdir outputs/

$ docker run -ti -v /home/mainak/Desktop/projects/github_repos/BIDS-examples/ds000248:/bids_dataset -v /home/mainak/Desktop/projects/github_repos/BIDS-app-mne/outputs:/outputs mne-app --subject_id 01 --inputdir /bids_dataset --outputdir /outputs
