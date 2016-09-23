import os, shutil

def rename(folder, pattern, ext):
    lof = os.listdir(folder)

    counter = 0
    for l in lof:
        if l.startswith("."):
            pass
        else:
            counter += 1
            newName = pattern + "_%06d.%s" % (counter, ext)
            print(newName)
            os.rename(folder+"/"+l, folder+"/"+newName)

def fix(folder):
    lof = os.listdir(folder)
    counter = 0
    for l in lof:
        if l.endswith(".tiff"):
            print(l[:-1])
            os.rename(folder+"/"+l, folder+"/"+l[:-1])

def fixNumbering()

#fix("./ara/new_scans/2_preprocessed_images/")
rename("/Users/romanov/Documents/a.UCA_Centennial/corpus/OCR_TrainingData/raw_images/", "0774IbnKathir.TabaqatShaficiyya", "png")
            
        
        
