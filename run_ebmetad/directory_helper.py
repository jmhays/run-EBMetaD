"""
Organizes the directory structure for EBMetaD runs.
Creates directories on the fly.

How the directory structure is organized:
    - This script should be run from your "top" directory (where
      you are planning to run all your ensemble members)
    - The top directory contains ensemble member subdirectories
      This script is intended to handle just ONE ensemble member,
      so we'll only be concerned with a single member subdirectory.
.
├── 0
    ├── historical_data.log
    ├── gromacs files
    └── force table

"""

import os


class DirectoryHelper:
    def __init__(self, top_dir, ensemble_num):
        """
        Small class for manipulating a standard directory structure for EBMetaD runs.
        :param top_dir: the path to the directory containing all the ensemble members.
        :param param_dict: a dictionary specifying the ensemble number, the iteration,
        and the phase of the simulation.
        """
        self._top_dir = top_dir
        self._ensemble_num = ensemble_num

    def get_dir(self, level):
        """
        Get the directory for however far you want to go down the directory tree
        :param level: one of 'top' or 'ensemble_num'
        See the directory structure example provided at the beginning of this class.
        :return: the path to the specified directory 'level' as a str.
        """
        if level == 'top':
            return_dir = self._top_dir
        elif level == 'ensemble_num':
            return_dir = '{}/mem_{}'.format(self._top_dir, self._ensemble_num)
        else:
            raise ValueError(
                '{} is not a valid directory type for BRER simulations'.format(
                    'type'))
        return return_dir

    def build_working_dir(self):
        """
        Checks to see if the working directory for current state of EBMetaD simulation exists.
        If it does not, creates the directory.
        """
        if not os.path.exists(self.get_dir('ensemble_num')):
            os.mkdir(self.get_dir('ensemble_num'))

    def change_dir(self, level):
        os.chdir(self.get_dir(level))
