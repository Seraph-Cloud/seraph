<a href="https://github.com/diveyez/blackhole/blob/master/README.md#black-hole">GO BACK TO README</a>
<h5>REQUIREMENTS,
 Linux or Windows Server with installed Webserver, GitHub, JRE8+, & Solr 7.5.0, 4+GB of RAM.  </h5></br>

<h2>After Install: Accessing the Search Features</h2>
*Read the install instructions below for your operating system, feel free to ask questions*
Once you are finished with the installation of all the required parts
You can just use the localhost/blackhole url to get to the pages
If you are operating over LAN, use the machines LAN ip address.
*Example: 10.2.1.2/blackhole*
When on the page for the Search, you will need to enter the query you wish to use
Followed by the name of the core (not core name, but field at top 'name')
Followed by localhost for the server field. Alternatively you can use your server IP.
Don't try to connect to Solr Cores from a webserver.
You need to run them both on the same machine or you cannot properly query and request
From the API. Once you have done all that, search results will show.
Click the Queries Menu item for information on how to refine and define your queries
So they are elastic and can be modified to the type of content you are searching for.

Updates and features will come soon, If you think you may be able to help. Feel free to contact me.
Kind regards, Happy Searching, -Ricky N.

<h1>Ubuntu,Debian, other apt ready Distributions of Linux.</h1>

```
* Firstly, cd to your working web server, if you are on linux and dont have one, use nginx for this, it is the best.
* git clone https://github.com/diveyez/blackhole
* apt install install default-jdk solr
* wget http://www.apache.org/dyn/closer.lua/lucene/solr/7.5.0/solr-7.5.0.tgz && tar -xvf solr-7.5.0.tgz
* cd solr-7.5.0/bin
* nano solr.in.sh
* UNCOMMENT (-#) & Set SOLR_HEAP="4096m" (4,096MB of Ram for Java's Heap)
* UNCOMMENT (-#) & Set SOLR_ULIMIT_CHECKS=false
* ./solr start -c <corename>
* ./post -C <corename> /path/to/files
```

<h3>EXAMPLE:</h3>

```
cd /opt/solr-7.5.0/bin && ./solr start -c Library && ./post -C Library /mnt/Library/Aeronautics_and_Spaceflight/*.*
```



<h1>Windows, Windows Server</h1>

```
I am not going to teach you how to setup a web server and php-7 on windows.
Here is a guide for that: (https://www.mkyong.com/nginx/nginx-php-on-windows/)
(I strong recommend getting this hard part over with first.)

---MAKE SURE YOU DOWNLOAD THE MOST RECENT VERSIONS----

On to Solr and Blackhole...

*First, you are going to need Java Runtime Environment 8
Go to this url and download it, there is no direct link. (https://www.java.com/en/download/manual.jsp)
Install Java and do not forget where you install it to, what would be a good idea is to install it inside
*The same folder as Solr. (http://archive.apache.org/dist/lucene/solr/7.5.0/solr-7.5.0.zip)
Download Solr and unzip it, for windows it pretty much works flawless out of the box.
Once you unzip it, we are now assuming you have my repository.

*Copy the post.jar and post.cmd and solr.start.cmd files from the windows_core directory to the
solr-7.5.0\solr\bin folder.

Copy the conf directory from the repository to the place you wish your core to be.
EXAMPLE: C:\solr-7.5.0\server\solr\library_core would be my directory.

You need to provide the document fields for it to index via the schema and xml files, or the core will not start.

Once you are done with that, double click on the solr.start.cmd
It will open a terminal and eventually say Port 8983 Happy Searching.

Go to your browser for that same machine, enter localhost:8983 into your browser.
Once you have done that, you have control of setting up the cores that are required to index.
As being so, it also will not start extracting without an index.
Here is some documentation on setting up cores: (https://lucene.apache.org/solr/guide/6_6/running-solr.html#RunningSolr-CreateaCore)

Please follow their instructions and only continue when you are ready.


You will have to edit some fields in post.cmd which I wrote for you.
Right click on it, you should be able to edit it.
<corename> is actually the name you gave it, not the actual name of the core.
*Remove the brackets and type your core name in the space between them.
Next go to the end of the line and setup your data/document directory.
Once you have done this, you simply save the file, exit the editor, double click on it, watch the magic.
On windows things are a bit weird when indexing large amounts of data with JavaRE.
You may want to investigate increasing the 'JavaRE Heap Size'. If it does crash, just restart it until all your files are indexed.
*After that, just use github desktop, clone the repository into your web document directory, you should have a working interface, the tools, documents for schemas, etc.
```
