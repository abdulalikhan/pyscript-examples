from utils import add_class, remove_class
from js import console
import json
import hashlib

# define the container that will be use to render the md5 hash to the page
hash_container = Element("hash-container")
text_content = Element("text-content")
hash_method = Element("hash-method")

hMethods = {
    hashlib.md5: 'md5',
    hashlib.sha256: 'sha256',
    hashlib.sha224: 'sha224',
    hashlib.sha384: 'sha384',
    hashlib.blake2b: 'blake2',
}


def generate_hash(*ags, **kws):
    message = text_content.element.value
    hashingTechnique = hash_method.element.value
    for key, val in hMethods.items():
        if val == hashingTechnique:
            h = key()
    h.update(message.encode('utf-8'))
    hash_container.element.innerText = h.hexdigest()


def generate_hash_event(e):
    if (e.key == "Enter"):
        generate_hash()
