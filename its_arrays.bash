#!/usr/bin/bash
declare -A bmp280
bmp280 < <( /home/beta/.local/src/its_and/its_bmp280.arrgs.py ); 

for ((i = 0 ; i < 10 ; i++)); do
  bmp280 += ( /home/beta/.local/src/its_and/its_bmp280.arrgs.py )
done

printf '%s' "${bmp280[@]}"