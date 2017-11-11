# csv2string-xml-android
Python scripts converting csv file to Android strings.xml resources multiple language :)

Requirements
------------

To satisfy requirements, run the following command:

`$ pip install lxml`

If you are not using pip in a virtualenv and want to install lxml globally instead, you have to run the above command as admin, e.g. on Linux:

`$ sudo  pip install lxml`


Usage By Clone Git
-----
1. Export path in your `.bash_profile` or `.zshrc` 

    `export PATH=$HOME/directory_your_download_this_project/csv2string-xml-android/bin:$PATH`

2. Go to your directory Android Project
    
    `cd AndroidStudio/project_name`

3. Generating *.xml files multi language
    
    `csv2xml`


```
app
└── src
    └── main
        └── res
            ├── values
            │   └── strings.xml
            └── values-de
                └── strings.xml
```
