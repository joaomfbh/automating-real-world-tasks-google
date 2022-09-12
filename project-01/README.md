# Scale and convert images using PIL
- [Qwiklabs link](https://googlecoursera.qwiklabs.com/focuses/23855179) - Link for this project

## Requirements

1. Download images using the command line bellow:
```sh
curl -c ./cookie -s -L "https://drive.google.com/uc?export=download&id=$11hg55-dKdHN63yJP20dMLAgPJ5oiTOHF" > /dev/null | curl -Lb ./cookie "https://drive.google.com/uc?export=download&confirm=`awk '/download/ {print $NF}' ./cookie`&id=11hg55-dKdHN63yJP20dMLAgPJ5oiTOHF" -o temp/images.zip && sudo rm -rf cookie
```
2. 
