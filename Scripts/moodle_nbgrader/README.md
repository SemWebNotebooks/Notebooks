This is a very slightly changed fork of [moodle_nbgrader by johnhw](https://github.com/johnhw/moodle_nbgrader).

## Submissions
Assuming you have an assignment called `<assignment>` (e.g. `week_2_numerical_ii`)

1. From Moodle, select assignment
2. `View All Submissions`
3. `Reveal student identities`
4. Choose `Download All Submissions` from top dropdown (MAKE SURE `Download submissions in folders` is OFF)
5. Copy archive to `imports/<assignment>.zip`
6. Choose `Download grading worksheet`
5. Copy CSV to `imports/<assignment>.csv`

        python collect_files.py <assignment> <workbook_name>

Example:

        python collect_files.py week_2_numerical_ii lab_2
    

Run:

        nbgrader autograde <assignment>

to grade the files

Then run:

        python update_gradesheet.py <assignment>

This will produce:
* `exports/<assignment>.csv` for upload as `Upload grading worksheet` 
* `exports/<assignment>_feedback.zip` for upload as `Upload multiple feedback files as zip`


## Creating assignments
1. in Moodle, enable offline gradebook and feedback files in the assignment
1. Create assignment in formgrader
2. Edit assignment and validate
3. Hit "Generate" in formgrader
4. Or use `nbgrader assign <assignment> --force`
5. `python release_zip.py <assignment>` to generate the zip file in `uploads`



