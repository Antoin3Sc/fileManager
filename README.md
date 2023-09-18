## FileManger
Small file manager script with 4 actions

### Backup
`python3 main.py --task=backup`

Will backup all your data from your different external volumes connected (SD Cards) to the volume "Photos" (can be changed in config file: `storage_disc_name`)

### Geolocation
`python3 main.py --task=geolocation --path=/your/folder/path`

Will retrieve your position in all the files in the folder, and get the city, state and country where was taken the photo if the geolocation metadata was found. Will create a csv file will all locations found.

### Encryption
`python3 main.py --task=encrypt --path=/your/folder/path`

Will encrypt all your files in the folder

### Decryption
`python3 main.py --task=decrypt --path=/your/folder/path`

Will decrypt all your files in the folder