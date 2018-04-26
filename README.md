Pre-installation
----------------

You will need Docker installed: https://www.docker.com/

Quickstart
----------

BIDS compatible data for this example is available at: https://openneuro.org/datasets/ds000248/

First, build the docker image
```sh
$ docker build . -t mne-app
```

Then make the folder to save the outputs
```sh
$ mkdir outputs/
```

Run the BIDS app
```sh
$ docker run -ti -v /home/mainak/Desktop/projects/github_repos/BIDS-examples/ds000248:/bids_dataset -v /home/mainak/Desktop/projects/github_repos/BIDS-app-mne/outputs:/outputs mne-app --subject_id 01 --inputdir /bids_dataset --outputdir /outputs
```