from utils import add_class, remove_class
from js import console
import json
from pyodide.http import open_url

url = (
    "https://api.aakhilv.me/fun/facts"
)

# define the container that will be use to render fun facts to the page
fun_fact_container = Element("fun-fact-container")


def generate_funfact(*ags, **kws):
    # fetch a random fun fact from the FFA Database
    try:
        json_data = json.loads(open_url(url).read())
    except Exception as ex:
        json_data = "Couldn't access the fun fact database :("
    # place the obtained fun fact on the page
    fun_fact_container.element.innerText = json_data[0]


def generate_funfact_event(e):
    if (e.key == "Enter"):
        generate_funfact()
