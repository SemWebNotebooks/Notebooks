import os
import re
import nbgrader, csv, codecs, sys, os, shutil
from nbgrader.apps import NbGraderAPI
import zipfile  
import shutil
verbose = False

def moodle_gradesheet(notebook_name, assign_name, csvfile, zip):        

    api = NbGraderAPI()    
    gradebook = api.gradebook
    

    archive = zipfile.ZipFile(zip)
    fnames = {}

    # read all the filenames, and get the submission
    # ids for each filename
    for f in archive.filelist:
        fname = f.filename
        match = re.match("[\*\w\-\'\s\.\,]+_([0-9]+)_.*", fname)
        if match:
            fnames[match.groups()[0]] = fname
        else:
            print("Did not match ", fname)

    with open(csvfile, newline='', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f) 
        assign_matric = {} 
        n_rows = 0
        successful_files = 0
        missing_files = 0
        problem_files = 0
            
        for line in reader:        
            
            ident, fullname,email, status,  grade, max_grade = (line['Identifier'], line['Full name'], line["Registration number"], 
                                                                line['Status'], line['Grade'], line['Maximum Grade'])

            should_be_submission =  "Submitted" in status

            # make sure we have this student in our records
            unique_id = email[0:7]
            try:
                result = gradebook.find_student(unique_id)
            except nbgrader.api.MissingEntry:
                print("Creating gradebook entry for ", unique_id)
                gradebook.update_or_create_student(unique_id, first_name=fullname, last_name="", email=email)

                
            # map assignment numbers to matric numbers
            matric = email[0:7]
            match = re.match('Participant ([0-9]+)', ident)
            if not match:
                print(f"Could not find identity for participant {ident}")
                continue
            
            ident = match.groups()[0]
            assign_matric[ident] = matric
            
            n_rows += 1
            if ident in fnames:                
                # extract each file to the submission directory
                submission_path = os.path.join("submitted", matric, assign_name)
                try:
                    os.makedirs(submission_path)
                except:
                    pass
                fname = fnames[ident]
                notebook_file = os.path.basename(fname)
                notebook_file = notebook_name+".ipynb"
                if verbose:
                    print("Extracting {notebook} to {path}".format(notebook=notebook_file, path=submission_path))

                source = archive.open(fname)
                target = open(os.path.join(submission_path, notebook_file), "wb")
                with source, target:
                    shutil.copyfileobj(source, target)
                
                successful_files += 1
            else:
                # submission was in the CSV file, but we don't have a zip file
                if should_be_submission:
                    print("*** WARNING! No submission for", fullname, matric, "but submission status was", status, "***")
                    problem_files += 1
                else:
                    # submission was not listed in the CSV file as being submitted
                    if verbose:
                        print("No submission for ", fullname, matric, status, "as expected")
                    missing_files +=1

        # print out a summary of what was processed
        print("""{n_files:d} succesfully extracted of {total_zip:d} files in the ZIP archive.
{missing:d} files were not submitted, as expected.
{problem:d} files were missing, but showed as submitted on Moodle.
{total:d} records were processed, and {total_csv} rows in the CSV.
""".format(n_files=successful_files, missing=missing_files, problem=problem_files,
total=successful_files+missing_files+problem_files,
total_zip = len(fnames), total_csv=n_rows))
            

    
import sys

if len(sys.argv)!=3:
    print("""
        Usage:
        
        collect_files.py <assignment> <notebook_name>
        
        # must have the following files in imports/

            <assignment>.csv <assignment>.zip

        The results will be copied into submitted/<matric_id>/<submission_name>/submission.ipynb

    """)
    sys.exit()


assign_name, notebook_name = sys.argv[1], sys.argv[2]
gradesheet_csv, archive_fname = os.path.join("imports", assign_name+".csv"), os.path.join("imports", assign_name+".zip")

moodle_gradesheet(notebook_name, assign_name, gradesheet_csv, archive_fname)
