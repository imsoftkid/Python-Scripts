# Networx XML Parser v0.2

Parse [Networx](http://www.softperfect.com/products/networx) backup XMLs to create statistics on Internet Usage.


## Table of Contents

* [Usage Scenario](#usage)
* [Stuff to do](#todo)
* [Changelog](#changelog)

## <a name="usage"></a>Usage Scenario

I've been creating a backup of network usage data every month for the past one year. Stuff like "Bytes Downloaded", "Bytes Uploaded", "Session Dialup Durations". [Networx](http://www.softperfect.com/products/networx) saves these backups in XML format.

I now wish to use all this data to create nice usage statistics.

These set of scripts will parse those XML Files to convert the crude data into a more usable format.

I'll probably be creating js files so that the data can be charted using some graphing library.

Stuff In Python:

* Parse All XML and Create as-is JS datasets.

Stuff In JavaScript:

* Load datasets into graphs.
* Current graphing library: [ChartJS](www.chartjs.org)
* Minimalist Interface ready to be integrated into the blog.
* Picker Controls: Month. Time/Download/Upload.

## <a name="todo"></a>Todo

* Better Graphing Ideas

* Time Per Day
  * Matrix[Month][Day]

* Sessions Per Day
  * Started At
  * Duration
  * Ended At

* Connection Wise

## <a name="changelog"></a>Changelog

* Added Downloaded/Uploaded Data to Graph
* December Graph Done :)
* Time Per Day for December

* Testing/Learning
  * List = [0] * 10
  * Datetime Module: strptime, timedelta