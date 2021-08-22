# $1 should be target program to disassemble

ddisasm $1 --asm temp.s > /dev/null 2>&1    &&\
rm $1   &&\
sed -i -e '/ret/i call HelloWorld' -e '3r HelloWorldInject.s' temp.s    &&\
gcc -o $1 temp.s    &&\
echo "Injection successful"
rm -f temp.s   # Note: we want to remove this file regardless of whether or not the previous steps succeeded
