class AthleteList(list):

    def __init__(self, name, dob=None, times=[]):
        # intializing the derived from class, and then
        list.__init__([])
        # Assigning the arguments to the attributes
        self.name = name
        self.dob = dob
        self.extend(times)

    @staticmethod
    def sanitize(time_string):
        if '-' in time_string:
            splitter = '-'
        elif ':' in time_string:
            splitter = ':'
        else:
            return(time_string)
        (mins, secs) = time_string.split(splitter)
        return(mins + '.' + secs)

    @property
    def top3(self):
        return (sorted(set([self.sanitize(t) for t in self]))[0:3])
