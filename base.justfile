# Default justfile for import

# just --list
[private]
ac3e01d:
  @just --justfile base.justfile --list --unsorted --list-heading $'Default Justfile for Imports\n'

# color code definitions for use in any justfile
[private]
colordefs:
  @echo
  @echo "{{BCY}}Terminal color code definitions included for use in any justfile{{NC}}"
  @echo '    For example, {{{{BCY}} gives:' 
  @echo "    {{BCY}}Bright Cyan{{NC}}"
  @echo

# show the color codes
colortest:
  @echo "            {{NC}}NC{{NC}}"
  @echo "   {{BK}}BK{{NC}}               {{BL}}BL{{NC}}"
  @echo "   {{BBK}}BBK{{NC}}              {{BBL}}BBL{{NC}}"
  @echo "   {{RD}}RD{{NC}}               {{MG}}MG{{NC}}"
  @echo "   {{BRD}}BRD{{NC}}              {{BMG}}BMG{{NC}}"
  @echo "   {{GR}}GR{{NC}}               {{CY}}CY{{NC}}"
  @echo "   {{BGR}}BGR{{NC}}              {{BCY}}BCY{{NC}}"
  @echo "   {{YW}}YW{{NC}}               {{WT}}WT{{NC}}"
  @echo "   {{BYW}}BYW{{NC}}              {{BWT}}BWT{{NC}}"

# color decorations
BK  := '\033[0;30m'   # Black        
BBK := '\033[1;30m'   # Bright Gray  
RD  := '\033[0;31m'   # Red          
BRD := '\033[1;31m'   # Bright Red   
GR  := '\033[0;32m'   # Green        
BGR := '\033[1;32m'   # Bright Green 
YW  := '\033[0;33m'   # Yellow       
BYW := '\033[1;33m'   # Bright Yellow
BL  := '\033[0;34m'   # Blue         
BBL := '\033[1;34m'   # Light Blue   
MG  := '\033[0;35m'   # Magenta      
BMG := '\033[1;35m'   # Light Purple 
CY  := '\033[0;36m'   # Cyan         
BCY := '\033[1;36m'   # Light Cyan   
WT  := '\033[0;37m'   # White        
BWT := '\033[1;37m'   # Light White  
NC := '\033[0m'
