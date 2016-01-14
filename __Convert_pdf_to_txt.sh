##################################
###                            ###
###      Joshua G. Mausolf     ###
###    Computation Institute   ###
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

cd Python_Scripts/Congressional_Records


##########################################################
#Set Minimum File Size and Convert Accordingly
##########################################################
minimumsize=7000
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

for file in *.txt
do
actualsize=$(wc -c <"$file")
if [ $actualsize -ge $minimumsize ]; then
    continue
else
    mv "$file" HTML_Error_Page_Requested_Not_Found
fi
done

echo Conversion and filtering is finished.
echo Enjoy your analysis with the Congressional Record.
