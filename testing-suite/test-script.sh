#!/bin/bash
set +x
turbot="../../../CLI/turbot.py"
payload="../../../CLI/payloads/logTamperInject.s"
stages=2
identicalSha=$()
turbotFailure=$()
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
        pwd
        ls ../../
		if turbot -A -p "../../../CLI/payloads/logTamperInject.s" ./output; then	
		    hash2=$(sha1sum $folder/output-reassembled.out)	
            if [ "$hash1" = "$hash2" ]; then
                echo "Sha sums are equal, test failed"
                ${identicalSha[@]}="$folder"
            else
                echo "Test Successful"
            fi
        else
            ${turbotFailure[@]}=$folder
        fi
        cd ..
	done
    popd
done

if [ ${identicalSha[@]} -eq 0]; then
    echo "Success: All tests compiled with unique sha values successfully"
else
    echo "Failure: The following tests failed to generate a different sha"
    for [i in ${identicalSha[@]}]; do 
        echo "$i"
    done
fi

if [ ${turbotFailure[@]} -eq 0]; then
    echo "Success: turbot successfully ran all tests"
else
    echo "Failure: turbot failed to execute the following tests"
    for [i in ${turbotFailure[@]}]; do 
        echo "$i"
    done
fi