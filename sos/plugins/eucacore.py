## Copyright (C) 2013 Eucalyptus Systems, Inc.

### This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 2 of the License, or
## (at your option) any later version.

## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.

## You should have received a copy of the GNU General Public License
## along with this program; if not, write to the Free Software
## Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

import sos.plugintools
import os
import glob

class eucacore(sos.plugintools.PluginBase):
    """Eucalyptus Cloud - Core
    """

    def checkenabled(self):
        if self.isInstalled("eucalyptus"):
            return True
        return False

    def setup(self):
        self.addCopySpec("/etc/eucalyptus")
        self.addCopySpec("/var/log/eucalyptus/*")
        if os.path.isfile('/usr/bin/sha1sum'):
            self.collectExtOutput("find /var/lib/eucalyptus/keys -type f -print | xargs -I {} sha1sum {}", suggest_filename="sha1sum-eucalyptus-keys")
        hprof_list = glob.glob('/var/log/eucalyptus/*.hprof')
        if hprof_list:
            self.collectExtOutput("rm -rf /var/log/eucalyptus/*.hprof", suggest_filename="hprof-removal")
        return
