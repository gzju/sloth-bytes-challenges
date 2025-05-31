
def removeVirus(s: str, bad_word = ["virus", "malware"], good_word = ["anti", "not"]) -> str:
    """
    Removes files that contain bad words from a string of file names.
    Args:
        s (str): A string containing file names, formatted as "PC Files: file1, file2, ...".
        bad_word (list): A list of words that indicate a file is a virus or malware.
        good_word (list): A list of words that indicate a file is safe or not a virus.
    Returns:
        str: A string with the same format as the input, but without files that contain bad words.
    Example:
        >>> removeVirus("PC Files: spotifysetup.exe, virus.exe, dog.jpg, antivirus.exe")
        "PC Files: spotifysetup.exe, dog.jpg, antivirus.exe"
        >>> removeVirus("PC Files: antivirus.exe, cat.pdf, lethalmalware.exe, dangerousvirus.exe")
        "PC Files: antivirus.exe, cat.pdf"
    """
    string_work = s.split(":")[-1].split(", ")
    if len(string_work) == 1 and string_work[0].strip() == "":
        return s.split(":")[0] + ": Empty" 
    return_not_virus = []

    for s_w in string_work:
        is_bad = False
        for b_w in bad_word:
            if b_w in s_w:
                # Check for exceptions like 'antivirus' or 'notvirus'
                is_not_bad = False
                for g_w in good_word:
                    if g_w in s_w:
                        is_not_bad = True
                        break
                is_bad = True
                break
        if not is_bad or is_not_bad:

            return_not_virus.append(s_w)
    
    return s.split(":")[0] + ":" + ", ".join(return_not_virus)
    

def main():
    print(removeVirus("PC Files: spotifysetup.exe, virus.exe, dog.jpg, antivirus.exe"))
    print(removeVirus("PC Files: spotifysetup.exe, virus.exe, dog.jpg"))
    print(removeVirus("PC Files: antivirus.exe, cat.pdf, lethalmalware.exe, dangerousvirus.exe "))
    print(removeVirus("PC Files: notvirus.exe, funnycat.gif"))
    print(removeVirus("PC Files: "))
    
if __name__ == "__main__":
    main()