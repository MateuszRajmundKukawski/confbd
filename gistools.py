
class GisTools(object):
    def export2qgis(self, workfile):
        self.workfile = workfile
        with open(self.workfile) as f:
            filedata = (line.rstrip('\n') for line in f)
            for line in filedata:
                print line




