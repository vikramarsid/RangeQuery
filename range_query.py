'''
range_query.py created by Vikram Sai Arsid 07/20/2015 10:27 AM PST
'''
import sys

from RangeTree import *


class RangeQuery:
    # processing capsule containing commands for one set[ADD->CLEAR]
    def process_command(self, clist):
        for line in clist:
            if 'ADD' in line:
                event_tree = self.event_loader(clist)
                output_file_path.write(line + '\n')
            elif 'QUERY' in line:
                output_file_path.write(self.query(event_tree, line) + '\n')
            else:
                output_file_path.write('\n')

    # Loading all ADD events into the data structure at once for consistent query
    def event_loader(self, files):
        scdevt = []
        for line in files:
            if 'ADD' in line:
                line = line.replace('\n', '')
                token = line.split(" ")
                scdevt.append(ScheduleEvent(token[1], token[2], token[3]))

            if 'CLEAR' in line:
                break

        loader = RangeTree(scdevt)
        return loader

    def query(self, obj, lines):
        lines = lines.replace("\n", "")
        tokens = lines.split(" ")
        payload = int(tokens[1])
        result = obj.search(payload)  # passing parsed payload to string
        return lines + ": " + ",".join(map(str, sorted(result)))  # converting list to comma seperated sorted string

    def clear(self):
        event_tree = None  # Nullifying the Range Tree
        return "CLEAR"


if __name__ == '__main__':

    try:
        # Opeining files to read and write
        input_file_path = open(sys.argv[1], 'r')
        output_file_path = open(sys.argv[2], 'w')
        rq = RangeQuery()
        capsule = []
        for line in input_file_path:
            if not 'CLEAR' in line:
                capsule.append(line.replace("\n", ""))
            else:
                rq.process_command(capsule)
                capsule = []
                output_file_path.write(rq.clear() + '\n')

    except IOError:
        print "Error: can\'t find file or read data"

    finally:
        input_file_path.close()
        output_file_path.close()
        print "View resulst in output file"
