#!/bin/bash
#* original source: https://sites.google.com/view/approxdbscan
#* source: https://github.com/ucrparlay/Pkd-tree/blob/main/script/gen_ss_varden.sh

download=0

while getopts "w:g:n:d:v:" option; do
    case $option in
    w)
        download=$OPTARG
        ;;
    g)
        gnum=$OPTARG
        ;;
    n)
        node=$OPTARG
        ;;
    d)
        dim=$OPTARG
        ;;
    v)
        varDensity=$OPTARG
        ;;
    esac
done

# if [[ ${download} -eq 1 ]]; then
#     wget -O DBSCAN.zip https://www.dropbox.com/s/xtf3134zcq08rt9/DBSCAN_v2.0_ubuntu14.04_bin.zip?dl=1
#     unzip DBSCAN.zip
#     rm DBSCAN.zip
# fi

echo "${download} ${gnum} ${node} ${dim} ${varDensity}"

vardenPath="DBSCAN"
outPath="/home/pedro/projects/varden_dataset_generator/varden/"

for gi in $(seq 1 1 ${gnum}); do
    oldPath="${outPath}varden_${node}_${dim}.arff"
    newPath="${outPath}varden_$new{gi}_${node}_${dim}.arff"

    sleep 2
    ./${vardenPath} -algo 0 -ds ${oldPath} -n ${node} -d ${dim} -vd ${varDensity}

    # while IFS= read -r line; do
    #     echo ${line}
    # done <${oldPath}
    # head -10 ${oldPath}
    python wash_varden.py ${oldPath} ${newPath}

    rm ${oldPath}
    mv ${newPath} ${oldPath}
done