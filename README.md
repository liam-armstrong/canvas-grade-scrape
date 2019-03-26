# canvas-grade-scrape

These 2 python files are built to scrape UBC's Canvas grade pages and allow access to the data within them. 

### To Use

Save your Canvas grade page as `grades.html` and place into the project root path and run one of the two python files: 
 * For the courses who do not allow grade totalling on the page, `average-calculator.py` will scrape and print your average to console
 * For courses where you'd like to do your own, more advanced analysis, `grades-to-csv.py` will scrape the page and put the info into CSV format, in the outputed `out.csv`
