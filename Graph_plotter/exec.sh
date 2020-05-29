# for file in ./*; do 
# 	if [[ "$file" ==  ]]; then
# 		#statements
# 		cp "$file" "${file/ (*)/}" 
# 		python3 script.py "${file/ (*)/}" ;done 
# 		rm "${file/ (*)/}"
# 	fi
# 	

find -type f -name '*.txt' | while read f; do cp "$f" "${f/ (*)/}" 
											  python3 script.py "${f/ (*)/}" 
											  rm "${f/ (*)/}" ; done