# Copyright (c) 2024 phoi5675
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from typing import Any

from transformers import (PreTrainedModel, T5ForConditionalGeneration,
                          T5Tokenizer)


def translate(model: PreTrainedModel, tokenizer: Any, text: str, lang_to: str) -> str:
    """return translated string, text to `lang_to`

    Parameters:
        model (`transformers.PreTrainedModel`):
            A PreTraindModel object from T5ForConditionalGeneration, model to use
        tokenizer (`transformers.T5Tokenizer`):
            A T5Tokenizer from transformers
        text (`str`):
            Text to translate
        lang_to (`str`):
            destination language. see https://huggingface.co/languages for param format.

    Return:
        `str`: Translated string
    """

    model_input = f"<2{lang_to}> {text}"
    input_ids = tokenizer(
        model_input, return_tensors="pt").input_ids.to(model.device)
    outputs = model.generate(input_ids=input_ids, max_length=80)

    return tokenizer.decode(outputs[0], skip_special_tokens=True)


def get_default_model() -> tuple[PreTrainedModel, Any]:
    """return deafult model and tokenizer

    Return:
        `tuple[PreTrainedModel, Any]`: A tuple consists of (model, tokenizer)
    """
    model_name = 'jbochi/madlad400-3b-mt'
    model = T5ForConditionalGeneration.from_pretrained(
        model_name, device_map="auto")

    tokenizer = T5Tokenizer.from_pretrained(model_name)
    return [model, tokenizer]
