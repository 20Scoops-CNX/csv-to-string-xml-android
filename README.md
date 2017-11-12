# csv2string-xml-android [![Build Status](https://travis-ci.org/T-Jedsada/csv2string-xml-android.svg?branch=master)](https://travis-ci.org/T-Jedsada/csv2string-xml-android)
Python scripts converting csv file to Android strings.xml resources multiple language :)

![string](./images/banner.png)

Requirements
------------

To satisfy requirements, run the following command:

`$ pip install lxml`

If you are not using pip in a virtualenv and want to install lxml globally instead, you have to run the above command as admin, e.g. on Linux:

`$ sudo  pip install lxml`

CSV Syntax
----

![string](./images/csv-example.png)

* First line must have minimum 2 column [key | language-code]
* Add `#` before string for comment message in strings.xml
* Column `arg` is optional but if you provide it. It must be at last column
* You can add multi column language code 

[file csv example](./csv-example.csv)

Usage
-----
1. Open Terminal  :joy:

2. Export path in your `.bash_profile` or `.zshrc` 

    `export PATH=$HOME/directory_your_download_this_project/csv2string-xml-android/bin:$PATH`

3. Go to your directory Android Project
    
    `cd AndroidStudio/project_name`

4. Generating *.xml files multi language
    
    `csv2xml`
    
    Continue enter your path file csv in terminal
    
    `Path to CSV file : path-file-csv/csv-example.csv`
    
    
Output
-----    
    ...
    app
    └── src
        └── main
            └── res
                ├── values
                │   └── strings.xml
                └── values-de
                │   └── strings.xml
                └── values-ja
                │   └── strings.xml
                └── values-zh
                    └── strings.xml

Reference
-----
 - [x] android-resource-converter by pwittchen [link](https://github.com/pwittchen/android-resource-converter)
