# Just a developer short cut to keep working copy free of temporary files.
rm *~ 2> /dev/null
rm *.bak 2> /dev/null
rm \#*\# 2> /dev/null

if [ -n "$1" ];
	then
		if [ "$1" = "all" ];
			then rm *.pyc 2> /dev/null
		fi
fi
