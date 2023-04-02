import json
import requests
import torch
from lavis.models import load_model_and_preprocess
from PIL import Image
import urllib.request as urllib
import io
# This is a script which evaluates the images with the BLIP module
# setup device to use
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
# loads BLIP caption base model, with finetuned checkpoints on MSCOCO captioning dataset.
# this also loads the associated image processors
model, vis_processors, _ = load_model_and_preprocess(name="blip_caption", model_type="base_coco", is_eval=True, device=device)
# load sample images
response_parse = 0
text = ""
for i in range(10):
    response = requests.get("https://api.nli.org.il/openlibrary/search?api_key=AnGdUMDNPbU7IhCHgbreKF4Lou5spSCYklIFpWrc"
                            "&query=any,contains,%D7%90%D7%A8%D7%9B%D7%99%D7%95%D7%9F%20%D7%93%D7%9F%20%D7%94%D7%93%D7%A0%D7%99"
                            "&tab=default_tab&search_scope=Local&vid=NLI"
                            "&facet=local7,include,%D7%90%D7%A8%D7%9B%D7%99%D7%95%D7%9F%20%D7%93%D7%9F%20%D7%94%D7%93%D7%A0%D7%99.&mfacet=rtype,include,photograph,1&mfacet=lang,include,zxx,2&lang=iw_IL&offset=0"
                            "&material_type=photograph&output_format=json&result_page=" + str(i), verify=False)
    text += json.dumps(response.json(), indent=4)
print(text)
for i in range(10):
    response_parse = text.find("1.1/thumbnail", response_parse) + 1
    image_add = text[text.find("value", response_parse) + 9:text.find("\"", text.find("value", response_parse) + 9)]
    fd = urllib.urlopen(image_add)
    image_file = io.BytesIO(fd.read())
    raw_image = Image.open(image_file).convert("RGB")
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


# preprocess the image
# vis_processors stores image transforms for "train" and "eval" (validation / testing / inference)
    image = vis_processors["eval"](raw_image).unsqueeze(0).to(device)

# generate caption
    print(model.generate({"image": image}))
# in order to get the image description use the manifest API
    response_parse = text.find("1.1/relation", response_parse) + 1
    caption_request = text[text.find("id", response_parse) + 6:text.find("\"", text.find("id", response_parse) + 6)]
    caption_response = requests.get(caption_request)
    caption_text = json.dumps(caption_response.json(), indent=4)
    print(caption_text)
# key: AnGdUMDNPbU7IhCHgbreKF4Lou5spSCYklIFpWrc
