os_name=`uname`
if [ ${os_name} = 'Darwin' ]; then
  count_total=`wc -l test.txt | sed "s/^ *//g" | cut -f 1 -d ' '`  
  count_match=`grep -e 'ne [23]' test.txt | wc -l  | sed "s/^ *//g" | cut -f 1 -d ' '`
else
  # Assume it is Linux
  count_total=`wc -l test.txt | cut -f 1 -d ' '`
  count_match=`grep -e 'ne [23]' test.txt | wc -l | cut -f 1 -d ' '`  
fi


# Inline message from parameter 1 
python ../slackmsg.py "[Test] ${count_match} / ${count_total} matched."

# Message content from stdin
tail -n 3 test.txt | python ../slackmsg.py
