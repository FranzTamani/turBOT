# How to Configure BOT

## LIST OF EXPECTED DEPENDENCIES
TODO: List Dependencies required

## Configure turBOT
run setup.sh
export PATH="path/to/turBOT/folder:$PATH"

## Test Help:
turbot --help
turbot -h

## Test Default (Decompiles, Obfuscates and Reassembles):
turbot /mnt/d/SEPB/test/exiting/test.o /mnt/d/SEPB/test/new/
turbot -DRO /mnt/d/SEPB/test/exiting/test.o /mnt/d/SEPB/test/new/

## Test Decompile:
turbot -D /mnt/d/SEPB/test/exiting/test.o /mnt/d/SEPB/test/new/

## Test Obfuscate:
turbot -O /mnt/d/SEPB/test/exiting/test.asm /mnt/d/SEPB/test/new/

## Test Reassemble:
turbot -R /mnt/d/SEPB/test/exiting/test.asm /mnt/d/SEPB/test/new/
