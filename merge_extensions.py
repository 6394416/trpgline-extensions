import json
import argparse

parser = argparse.ArgumentParser(description='import monster data')
parser.add_argument('--one', type=str, default='one.json', help='first file to be merged')
parser.add_argument('--two', type=str, default='two.json', help='second file to be merged')
parser.add_argument('--out', type=str, default='merged.json', help='output file name')
args = parser.parse_args()

def merge_json_extensions(data1, data2):
    for ids in data2['extends']['ids']:
        if ids not in data1['extends']['ids']:
            data1['extends']['ids'] += [ids]
    data1['extends']['entities'] |= data2['extends']['entities']
    return data1

def main(one=args.one, two=args.two, out=args.out):
    # Load data from the first JSON file
    with open(one, 'r', encoding='utf8') as file1:
        data1 = json.load(file1)

    # Load data from the second JSON file
    with open(two, 'r', encoding='utf8') as file2:
        data2 = json.load(file2)

    # Merge the two datasets
    merged = merge_json_extensions(data1, data2)

    # Save the merged data to a new JSON file
    with open(out, 'w', encoding="utf8") as outfile:
        json.dump(merged, outfile, indent=None, ensure_ascii=False)

if __name__ == "__main__":
    main()