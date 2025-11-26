#!/usr/bin/python3
"""Module defining MyList class."""


class MyList(list):
    """Custom list class that can print a sorted version of itself."""

    def print_sorted(self):
        """Print the list in ascending sorted order."""
        print(sorted(self))
