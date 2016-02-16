##################################
###                            ###
###      Joshua G. Mausolf     ###
###   Department of Sociology  ###
###    University of Chicago   ###
###                            ###
##################################


##########################################################
#Ensure PDFTOTEXT Installed
##########################################################

type pdftotext >/dev/null 2>&1 || { echo >&2 "This package requires pdftotext, but it is not installed."; \
 echo "Consider using homebrew and the command 'brew install poppler' to get pdftotext."; \
 echo "Aborting script to prevent data loss."; exit 1; }


##########################################################
#Change Directory to Congression Records Folder
##########################################################

cd Python_Scripts/Congressional_Records >/dev/null 2>&1 || { echo >&2 "Directory 'Python_Scripts/Congressional_Records' not found"; \
    echo "Please make sure your speech files are in this directory and try again."; exit 1; }


##########################################################
#Set Minimum File Size and Convert Accordingly
##########################################################
minimumsize=6000
for file in *.pdf
do
actualsize=$(wc -c <"$file")

#Convert True PDFs of Congressional Record
if [ $actualsize -ge $minimumsize ]; then
    echo size is over $minimumsize bytes. Size = $actualsize
    echo Converting Congressional Record File $file to Text
    pdftotext "$file"
    rm "$file"

#Convert HTML Files with .pdf Extentions to .txt
else
    echo size is under $minimumsize bytes. Size = $actualsize
    mv "$file" "${file%.pdf}.txt"
fi
done

##########################################################
#Move HTML Error Files to New Folder
##########################################################
mkdir "HTML_Error_Page_Requested_Not_Found"

echo moving HTML error page files to new folder...

htmlstring="DOCTYPE html"

for file in *.txt
do
actualsize=$(wc -c <"$file")
if [ $actualsize -ge $minimumsize ]; then
    continue

elif grep -Fq "$htmlstring" "$file"; then
	mv "$file" HTML_Error_Page_Requested_Not_Found

else
    continue

fi
done

echo Conversion and filtering is finished.
echo Enjoy your analysis with the Congressional Record.
