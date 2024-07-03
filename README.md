# dvc-pg

### Init
- pip install dvc
- pip install dvc_s3

*git init*
- dvc init

- dvc remote add -d myremote s3://<bucket>/<key>
- dvc remote modify myremote endpointurl https://nyc3.digitaloceanspaces.com

- dvc remote modify --local myremote access_key_id 'mysecret' // OR export AWS_ACCESS_KEY_ID=''
- dvc remote modify --local myremote secret_access_key 'mysecret' // OR export AWS_SECRET_ACCESS_KEY=''
- dvc remote modify --local myremote session_token 'mysecret'


### Add files to vcs (both git and dvc)
- dvc add <data_dir>/<file>
- git add <data_dir><file>**.dvc** <data_dir>/.gitignore

Example
- dvc add ./data/tracked_file.bin
- git add ./data/tracked_file.bin.dvc ./data/.gitignore
- git push origin main
- dvc push

- dvc get https://github.com/Daterdum/dvc-pg.git data/tracked_file.txt --rev=0.0.1


## Useful links
Params for s3 setup in dvc - https://dvc.org/doc/user-guide/data-management/remote-storage/amazon-s3#s3-compatible-servers-non-amazon

## Features

### Metrics
https://dvc.org/doc/command-reference/metrics
- dvc metrics show
- dvc metrics diff

### Params
https://dvc.org/doc/command-reference/params
- dvc params show
- dvc params show

### Plots
- dvc plots show
- dvc plots diff

### Stages
- dvc repro