import sys
import os
import xml.etree.ElementTree as ET
import time

# Start the timer
time_start = time.time()

print() # Print an enter before the results

# Arguments conditions that are invalid
argerror = len(sys.argv) < 3 or len(sys.argv) > 5 or len(sys.argv) == 4
pyfileerror = sys.argv[0] != "search.py"
if len(sys.argv) == 5:
    sectionerror = sys.argv[1] not in ["kepala_putusan", "identitas", "riwayat_penahanan", "riwayat_perkara", "riwayat_tuntutan", "riwayat_dakwaan", "fakta", "fakta_umum", "pertimbangan_hukum", "amar_putusan", "penutup", "all"]
    operatorerror = sys.argv[3] not in ["AND", "OR", "ANDNOT"]
else:
    sectionerror = False
    operatorerror = False

# Checking the arguments if they are validd and if the operator is valid
if argerror or pyfileerror or sectionerror:
    print("Argumen program tidak benar.")
    sys.exit()
elif operatorerror:
    print("Mode harus berupa AND, OR atau ANDNOT.")
    sys.exit()

# Assigning sys arguments into variables
search_section = sys.argv[1]
search_words1 = sys.argv[2]
if len(sys.argv) == 5:
    operator = sys.argv[3]
    search_words2 = sys.argv[4]

# Create the relative path to the folder
folder_path = os.path.join(os.getcwd(), 'dataset')

# File search found counter
counter = 0

# The main loop for searching through the files
for dirpath, dirnames, filenames in os.walk(folder_path):
    for filename in filenames:

        # Create the full path to the file by joining the dirpath and filename
        file_path = os.path.join(dirpath, filename)

        # Parse the XML file
        tree = ET.parse(file_path)
        root = tree.getroot()

        # =====================================================================

        # Open the file and read the contents, based on the arg
        if search_section != "all":
            # Find the element
            section_element = root.find(search_section)
            if section_element is not None:
                # Extract the text content of the element
                contents = section_element.text.strip().replace('\n', ' ')

        # =====================================================================

        elif search_section == "all":
            extracted_text = ''
            # Iterate through the child elements of the root element
            for element in root:
                # Concatenate the text content of each child element
                extracted_text += element.text.strip()
            contents = extracted_text.replace('\n', ' ')

        # =====================================================================

        # For input with operator, check if the file contains the search words
        if len(sys.argv) == 5:
            if operator == "AND":
                if search_words1 in contents and search_words2 in contents:
                    available = True
                else:
                    available = False
            elif operator == "OR":
                if search_words1 in contents or search_words2 in contents:
                    available = True
                else:
                    available = False
            elif operator == "ANDNOT":
                if search_words1 in contents and search_words2 not in contents:
                    available = True
                else:
                    available = False
        # For input with no operator, just going to return True
        else:
            if search_words1 in contents:
                available = True
            else:
                available = False
        
        # =====================================================================

        if available == True:
            # Get the attributes from the XML file
            lokasi = root.attrib.get("provinsi", "")[:15]
            pidana = root.attrib.get("klasifikasi", "")[:15]
            kejahatan = root.attrib.get("sub_klasifikasi", "")[:30]
            pn = root.attrib.get("lembaga_peradilan", "")[:20]
            # Print the results
            print(f"{filename} {lokasi:>15} {pidana:>15} {kejahatan:>30} {pn:>20}")
            # Increment the file found counter
            counter += 1

        # =====================================================================

print(f"\n{'Banyaknya dokumen yang ditemukan':<33}= {counter}")

time_end = time.time()
time_total = time_end - time_start
print(f"{'Total waktu pencarian':<33}= {time_total:.3f} detik")