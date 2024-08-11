# Copyright (c) 2024 phoi5675
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import argparse
import sys

from core.translate import get_default_model, translate

parser = argparse.ArgumentParser(
    description="prints translated string or string array into desired language using madlad400-3b-mt")
parser.add_argument('--to', action='store_const', default='ko',
                    help='ISO code of destination language. defaults to ko(Korean). See https://huggingface.co/languages for language codes')
parser.add_argument('input_text', nargs='?',
                    help='Input text, or pipe input via stdin')

args = parser.parse_args()

model, tokenizer = get_default_model()

if __name__ == '__main__':
    lang_to = args.to
    if args.input_text:
        text = args.input_text
        print(translate(text, lang_to))
    else:
        text_list = sys.stdin.read().splitlines()
        for text in text_list:
            print(translate(model, tokenizer, text, lang_to))
