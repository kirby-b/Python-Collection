# This is a small collection of miscellaneous functions that I made for various purposes, only for me to find a fix that is already built in.
# I put them here because I didnt feel they deserved a full repo, but could still be of use.

# From my tax.py program. Replaced by an isinstance
def is_float(string):
        try:
            float(string)
            return True
        except ValueError:
            return False
