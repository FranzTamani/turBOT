#!/bin/bash
set +x
turbot="../../../CLI/turbot.py"
payload="../../../CLI/payloads/logTamperInject.s"
stages=1
declare -a identicalSha
declare -a turbotFailure
identicalSha=()
turbotFailure=()

for i in $(seq $stages); do
    pwd
	echo "Running Test Stage: $i";
    pushd ./
    cd stage-$i
	for folder in */; do
		echo "$folder"; 	
		cd $folder;	
		make
		hash1=$(sha1sum output)	
		if turbot -A -p "../../../CLI/payloads/logTamperInject.s" ./output; then	
		    hash2=$(sha1sum output-reassembled.out)	
            if [ "$hash1" = "$hash2" ]; then
                echo "Sha sums are equal, test failed"
                identicalSha+=($folder)
            else
                ./output-reassembled.out
                echo "Test Successful"
            fi
        else
            turbotFailure+=($folder)
        fi
        cd ..
	done
    popd
done

if [ ${#identicalSha[@]} -gt 0 ]; then
    echo "Failure: The following tests failed to generate a different sha"
    for shaTests in ${identicalSha[@]}; do 
        echo "$shaTests"
    done
else
    echo "Success: All tests compiled with unique sha values successfully"
fi

if [ ${#turbotFailure[@]} -gt 0 ]; then
    echo "Failure: turbot failed to execute the following tests"
    echo ${identicalSha[@]}
    for turbotTests in ${turbotFailure[@]}]; do 
        echo "$turbotTests"
    done
else
    echo "Success: turbot successfully ran all tests"
fi