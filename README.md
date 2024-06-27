# dvc-pg
### Add files to vcs (both git and dvc)
1. dvc add <data_dir>/<file>
2. git add <data_dir><file>**.dvc** <data_dir>/.gitignore

Example
dvc add ./data/tracked_file.bin
git add ./data/tracked_file.bin.dvc ./data/.gitignore
git push origin main

dvc remote add -d myremote s3://<bucket>/<key>
dvc remote modify myremote endpointurl https://nyc3.digitaloceanspaces.com

dvc remote modify --local myremote access_key_id 'mysecret' // OR export AWS_ACCESS_KEY_ID=''
dvc remote modify --local myremote secret_access_key 'mysecret' // OR export AWS_SECRET_ACCESS_KEY=''
dvc remote modify --local myremote session_token 'mysecret'

dvc push


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