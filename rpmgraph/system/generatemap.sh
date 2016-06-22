#!/bin/sh

#*********************************************************************************************************
#*   __     __               __     ______                __   __                      _______ _______   *
#*  |  |--.|  |.---.-..----.|  |--.|   __ \.---.-..-----.|  |_|  |--..-----..----.    |       |     __|  *
#*  |  _  ||  ||  _  ||  __||    < |    __/|  _  ||     ||   _|     ||  -__||   _|    |   -   |__     |  *
#*  |_____||__||___._||____||__|__||___|   |___._||__|__||____|__|__||_____||__|      |_______|_______|  *
#* http://www.blackpantheros.eu | http://www.blackpanther.hu - kbarcza[]blackpanther.hu * Charles Barcza *
#*************************************************************************************(c)2002-2016********


name=$1
name2=$2

if [ "x$name" = "x" ];then
  echo "
  Missing paramter as rpm name. Run script with parameter ! 
     Example: $basename $0 install  (for install dependency)
  And for generate RPM-Map
    Example: $basename $0 gimp
  OR
    Example: $basename $0 full /for full system mapping/
  OR 
    Example: $basename $0 gimp Different_SCREENSHOTNAME
"
  exit

fi

if [ "$name" = "install" ];then
  installing graphviz rpmorphan
  echo "
  Okay! 
  Now run script simple! Example: $basename $0 gimp
  "
  exit
fi


[ "x$name" = "x" ]&&echo "Missing packname! Example: $basename $0 gimp" && exit

gendot () {
echo "Run: rpmdep -dot $name.dot $name"
rpmdep -dot $name.dot $name 2>/dev/null
ret=$?
[ "$ret" = "1" ]&& echo "ERROR 1" && exit
[ ! -n "$name" ]&& echo "ERROR 2" && exit
[ ! -n "$name2" ]&& name2=$name
}

systemmap () {
name=Out
echo "Run: Reading all system rpm packages to tmp ($name)"
rpm --queryformat '%{NAME} \n' -qa | sort > pack_names.tmp 
echo "Run: Reading $(cat pack_names.tmp | wc -l) packages"
sleep 5
cat pack_names.tmp | while read FILE; do $basename $0 $FILE 2>/dev/null ; done

}

gensysmap () {
echo "Run: Generating  system dot to all in one"
awk '{if (!a[$0]++) print}' *.dot > ${name}.tmp
mv -f ${name}.tmp ${name}.dot

perl -pi -e 's|;| [color=red,penwidth=1.0];|' ${name}.dot

}

coloring () {
echo "Run: Coloring $name.dot"
perl -pi -e 's|;| [color=red,penwidth=2.0];|' $name.dot

perl -pi -e 's|digraph "rpmdep" {|digraph "rpmdep" {
node [width = 0.95, fixedsize = false, style = filled, fillcolor = palegreen];|g' $name.dot
}

genpng () {
echo "Run: dot -Tpng $name.dot -o $name2.png"
dot -Tpng $name.dot -o $name2.png 2>/dev/null

}

if [ "$name" = "full" ];then
echo "Generating full system MAP"
    systemmap
    gensysmap
perl -pi -e 's|digraph "rpmdep" {|digraph "rpmdep" {
node [width = 0.95, fixedsize = false, style = filled, fillcolor = palegreen];|g' Out.dot
    genpng
    rm -rf *.tmp
    mv Out.dot Out.TMP
    rm -rf *.dot
    mv Out.TMP Out.dot
    exit

fi

gendot
coloring
if [ ! -n "$(echo $@ | grep '-s' )" ]];then
    genpng
 else 
    name2=$name
fi
#finish
