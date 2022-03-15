#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import time
import string
import sys
import json
import io
import argparse
reload(sys)
sys.setdefaultencoding('utf8')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--line', type=int)
    parser.add_argument('--file')
    parser.add_argument('--note')
    parser.add_argument('--create', action='store_true', default=False, help='Create action, not the update')

    args = parser.parse_args()
    line = args.line
    file = args.file
    note = args.note
    linuxversion = file.split('/')[0]

    if args.create:
        print "create " + file + " " + str(line) +" " + note +" linuxversion: " + linuxversion
        notes=[]
        n={'line':line,'note':note}
        notes.append(n)
        f={'file':file, 'version':'v0.1', 'linuxversion':linuxversion, 'notes': notes}
        with io.open(file+'.json', "w", encoding="utf-8") as fw:
            json.dumps(f, indent=8, ensure_ascii=False)
            fw.write(unicode(json.dumps(f, indent=8, ensure_ascii=False)))
    else:
        print "update " + file + " " + str(line) +" " + note
        with io.open(file+'.json', "r", encoding="utf-8") as f:
            n = json.load(f)
            new_notes=[]
	    for n1 in n['notes']:
		if n1['line'] != line:
        		new_notes.append(n1)
		else:
			print "delete the old notes, line " + str(line)
            note={'line':line,'note':note}
	    new_notes.append(note)
            n['notes'] = new_notes
            with io.open(file+'.json.new', "w", encoding="utf-8") as fw:
                fw.write(json.dumps(n, indent=8, ensure_ascii=False))

if __name__ == '__main__':
    main()
