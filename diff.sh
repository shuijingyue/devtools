# check change in source branch but not not in target branch
workspace=`pwd`
cd /Users/shihuan/workspace/android/PersonalAssistant/widget
source=$1
target=$2
git log --oneline $source --format='%s|||%an|||%cs' --after=2022-06-30 > $workspace/source.log
git log --oneline $target --format='%s|||%an|||%cs' --after=2022-06-30 > $workspace/target.log
cd $workspace
python entry/diff.py
