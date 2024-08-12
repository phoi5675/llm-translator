# Copyright (c) 2024 phoi5675
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import argparse
import json
from typing import *

from transformers import PreTrainedModel

from core.translate import get_default_model, translate

parser = argparse.ArgumentParser(
    description="Parse json and translate value of json properties"
)
parser.add_argument('--to', default='ko',
                    help='ISO code of destination language. defaults to ko(Korean). See https://huggingface.co/languages for language codes')
parser.add_argument('--out',
                    help='A name of output file. Defaults to ${json_file}_${--to}.json')
parser.add_argument('json_file', help='A file containing json')

args = parser.parse_args()

# Define input / output files
json_file, lang_to, out = args.json_file, args.to, args.out
out_file = f'{json_file}_{lang_to}.json'
if out:
    out_file = out


def parse_json(json_file: str) -> Dict[str, str | object]:
    """Parse json from file and return json object

    Return:
        `json` or `None`:
            `json` if file is parsed, `None` if file is not parsed.
    """
    try:
        with open(json_file) as f:
            data = json.load(f)
            return data
    except Exception as e:
        print(e)
        return None


def traverse_json(json_data: Dict[str, str | object], model: PreTrainedModel, tokenizer: Any) -> None:
    for key, value in json_data.items():
        # If value is dict(nested object), traverse
        if type(value) is dict:
            traverse_json(value, model, tokenizer)
        # If value is string, translate value and store it into original json object
        if type(value) is str:
            json_data[key] = translate(
                model, tokenizer, value, lang_to)


if __name__ == '__main__':

    json_data = parse_json(json_file)
    if not json_data:
        print('Unable to parse file to json.')
        exit(1)

    # Load model and tokenizer
    model, tokenizer = get_default_model()

    traverse_json(json_data, model, tokenizer)

    # Write json to output file
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=4)
