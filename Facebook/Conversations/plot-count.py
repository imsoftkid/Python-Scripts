"""
Plot the number of messages sent/recieved to a friend.

You should run messages.py first.
"""

import os
import json

import time
from datetime import datetime as DT

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from messages import mkdir

ROOT = "Messages"
date_format = "%Y-%m-%d"


def pretty_epoch(epoch, fmt):
    """ Convert timestamp to a pretty format. """
    return time.strftime(fmt, time.localtime(epoch))


if __name__ == '__main__':

    mkdir('Plot')

    for friend in os.listdir(ROOT):

        print("Processing conversation with %s" % friend)

        messages = {}

        # Read all the files of a friend & build a hashmap
        for file in os.listdir(os.path.join(ROOT, friend)):

            with open(os.path.join(ROOT, friend, file)) as inp:

                data = json.load(inp)
                for act in data['payload']['actions']:

                    # BUG: Why wouldn't body be present?
                    if 'body' in act:

                        # Facebook uses timestamps with 13 digits for milliseconds
                        # precision, while Python only needs the first 10 digits.
                        date = pretty_epoch(act['timestamp'] // 1000, date_format)

                        if date in messages:
                            messages[date] += 1
                        else:
                            messages[date] = 1

        # Begin creating a new plot
        plt.figure()

        # Prepare the date
        x, y = [], []
        for date in messages.keys():
            x.append(mdates.date2num(DT.strptime(date, date_format)))
            y.append(messages[date])

        # Use custom date format
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
        plt.gca().xaxis.set_major_locator(mdates.MonthLocator())

        # Plot!
        plt.plot_date(x, y)

        # Ensure that the x-axis ticks don't overlap
        plt.gcf().autofmt_xdate()
        plt.gcf().set_size_inches(17, 9)

        # Save plot
        plt.title("Conversation with %s" % friend)
        plt.savefig("Plot/%s.png" % friend)
