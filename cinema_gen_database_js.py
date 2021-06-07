import sys
import json
import glob
import os

from os.path import join as pjoin


def digest_cdb(path):
    res = {}
    csvs = glob.glob(pjoin(path,"*.csv"))
    for csv in csvs:
        csv_base = os.path.split(csv)[1]
        csv_base = os.path.splitext(csv_base)[0]
        print("[digesting {0}]".format(csv_base))
        res[csv_base] = open(csv).read()
    return res

def main():
    if len(sys.argv) < 1:
        print("usage: python cinema_gen_database_js.py <input.json>")
        print("example: python cinema_gen_database_js.py small.json")
        sys.exit(-1)
    dbs_json_file = sys.argv[1]
    # load json file with databases
    root = json.load(open(dbs_json_file))
    for db in root:
        print(db["name"])
        db["csvs"] = digest_cdb(db["directory"])
    # display dbs to console
    print("var databases = " + json.dumps(root,indent=2) + ";")
    # write final dbs javascript file
    ofname = "_gen_database.js"
    open(ofname,"w").write("var databases = " + json.dumps(root,indent=2) + ";")
    print("[created: {0}]".format(ofname))
    print("[open cinema_explorer.html to view databases]")


if __name__ == "__main__":
    main()


