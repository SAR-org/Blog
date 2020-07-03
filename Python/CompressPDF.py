#CompressPDF.py

import os
import subprocess
import sys

def compress(input_file_path, output_file_path, compressionMode=0):
    
    quality = {
        0: '/default',
        1: '/prepress',
        2: '/printer',
        3: '/ebook',
        4: '/screen'
    }
    
    # Basic controls
    # Check if valid path
    if not os.path.isfile(input_file_path):
        print("Error: invalid path for input PDF file")
        sys.exit(1)
    
    # Check if file is a PDF by extension
    if input_file_path.split('.')[-1].lower() != 'pdf':
        
        print("Error: input file is not a PDF")
        sys.exit(1)

    print("Compress PDF...")
    initial_size = os.path.getsize(input_file_path)
    subprocess.call(['gs', '-sDEVICE=pdfwrite', '-dCompatibilityLevel=1.4',
                    '-dPDFSETTINGS={}'.format(quality[compressionMode]),
                    '-dNOPAUSE', '-dQUIET', '-dBATCH',
                    '-sOutputFile={}'.format(output_file_path),
                    input_file_path]
    )
    final_size = os.path.getsize(output_file_path)
    ratio = 1 - (final_size / initial_size)
    print("Compression by {0:.0%}.".format(ratio))
    print("Final file size is {0:.1f}MB".format(final_size / 1000000))
    print("Done.")


if __name__ == "__main__":
    dir = '/home/rajeevan/Documents/Rajeevan/StoyBooks/Downloads/'
    compress(dir+'test.pdf',dir+"compressed.pdf",4)