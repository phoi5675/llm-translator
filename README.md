# llm-translator

translator using LLM with transformers

## Setups

```bash
# Put something you like to use as a virtual env into ${VENV_NAME}
python3 -m venv ${VENV_NAME}
source ${VENV_NAME}/bin/activate

# install packages in requirements.txt
pip3 install -r requirements.txt
```

## Run

### Single string or piped input

Translate simple string, or multi line string using pipe.  
`python main.py --help` for full usage examples.

```python
# single string
python main.py --to 'ko' 'Hello world!'

# piped
cat some_file | python main.py --to 'ko'
```

### JSON

Load source json file and save translated json to `--out` file.  
`python json_translator.py --help` to see full usages.

```python
python json_translator.py --to ko --out ko.json en.json
```

## References

- [hugging face installation](https://huggingface.co/docs/transformers/installation#installation)
- [google/madlad-400-3b-mt](https://huggingface.co/google/madlad400-3b-mt)
