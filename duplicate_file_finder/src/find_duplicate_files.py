# imports
import sys
import logging
import os
import argparse
import hashlib
import common_utils


# contributors
__author__ = "zanza259"
__version__ = "1.0.0"


logger = common_utils.build_default_logger(__name__, "WARN")


def build_argparse():

    parser = argparse.ArgumentParser(description="Scan machine for duplicate files based on md5 checksum.")

    parser.add_argument("input_file")

    common_utils.add_common_logger_args(parser)

    return parser



def main(argv):

    parser = build_argparse()
    args = parser.parse_args()    

    if args.verbose:
        logger.setLevel(logging.INFO)

    if args.debug:
        logger.setLevel(logging.DEBUG)


    logger.info("Executing duplicate file finder...")


    whitelisted = []

    logger.info("\t + Loading whitelisted root directories from {}".format(os.path.expanduser(args.input_file)))
    with open(os.path.expanduser(args.input_file), "r") as input_file:

        for line in input_file:
            whitelisted.append(line.rstrip())

    total_directories = len(whitelisted)

    logger.info("\t\t - {} total whitelisted root directories found.".format(total_directories))

    dir_counter = 0
    all_hashes = {}

    conflict_hashmap = {}

    for directory in whitelisted:
        dir_counter += 1
        logger.info("\t + [{} of {}] Now processing directory: {}".format(dir_counter, total_directories, directory))

        for path, subdirs, files in os.walk(directory):
            for name in files:
                full_path = os.path.join(path, name)
                #logger.info("\t\t + {}".format(full_path))
                
                md5_hash = hashlib.md5(open(full_path, "rb").read()).hexdigest()

                logger.info("\t\t + Processing {} | {}".format(name, md5_hash))

                try:

                    if all_hashes[md5_hash]:

                        if md5_hash not in conflict_hashmap.keys():
                            conflict_hashmap[md5_hash] = []

                        conflict_hashmap[md5_hash].append(full_path)

                except:
                    all_hashes[md5_hash] = True
                

    logger.info("{} total conflicts found...".format(len(conflict_hashmap)))


    for md5_hash in conflict_hashmap.keys():
        logger.info("Conflict found:")

        for path in conflict_hashmap[md5_hash]:
            logger.info("\t - {}".format(path))    

    


if __name__ == "__main__":
    main(sys.argv)
