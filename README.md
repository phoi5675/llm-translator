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

```python
# single string
python --to 'ko' 'Hello world!'

# piped
cat some_file | python --to 'ko'
```

### JSON

TBD

## References

- [hugging face installation](https://huggingface.co/docs/transformers/installation#installation)
- [google/madlad-400-3b-mt](https://huggingface.co/google/madlad400-3b-mt)
