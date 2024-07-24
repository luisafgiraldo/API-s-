####################### PARAMETERS ####################################
import os

projectType = {
    1 : 'classification',
    2 : 'segmentation',
    3 : 'object-detection'
                }
################### PARAMETERS TO CHANGE ###########################
api_key = "land_sk_VtHE8Gx36OvgODIYxyl0cesFMhiZUJEvtEc3YI1Dk1C5tf76ku" #Enterprise-Org
url_base = 'https://api.staging.landing.ai/v1'
#%%
################### PARAMETERS TO CHANGE ###########################
elegir_proyecto = projectType.get(2) 
name_proyecto = 'July-24th-Seg-Project-1st'
#%%
######################## CREATE PROJECT ###############################
import create_project as cp
url = f"{url_base}/projects"
data = {"projectType": elegir_proyecto, "name": name_proyecto}
project_id = cp.create(api_key=api_key,url=url,data=data)
#%% 
######################## GET PROJECT ##################################
import getProject as gp
gp.getProject(api_key, url, project_id)
#%%
######################## CREATE CLASSES ###############################
import create_classes as cc
url = f'{url}/{project_id}/classes'
if elegir_proyecto == 'classification':
    data = {"0": {"name": "Roll-Print"},"1": {"name": "Side-line"}}
elif elegir_proyecto ==  'segmentation':
    data = {"1": {"name": "Screw"}}
elif elegir_proyecto == 'object-detection':
    data = {"1": {"name": "Screw", "color": "#FFFF00"}}
cc.create(api_key=api_key, url=url, data=data)
#%%
####################### UPLOAD IMAGES #################################
import upload_images as ui
url = url.replace('classes', 'images')
if elegir_proyecto == 'classification':
    folders = [data[key]["name"] for key in data] # Se crea una lista, porque la clase es la misma carpeta
    path = 'Images-CLASS'
    ui.upload_classification(api_key, url, folders, path)
elif elegir_proyecto == 'object-detection':
    path = 'Images-OD/Images'
    ui.upload_object_detection(api_key, url, directory=path)
    import auto_split as asp
    url = url.replace('images', 'autosplit')
    # Prepare the payload (adheres to the required format)
    data = {
        "splitPercentages": {
            "train": 65,
            "dev": 25,
            "test": 10,
        },
        "selectOption": "all-labeled"
    }
    
    asp.auto_split(url, api_key, data)
    
elif elegir_proyecto == 'segmentation':
    path = 'images-SEG/Images'
    ui.upload_segmentation(api_key, url, directory=path)
    import auto_split as asp
    url = url.replace('images', 'autosplit')
    # Prepare the payload (adheres to the required format)
    data = {
        "splitPercentages": {
            "train": 65,
            "dev": 25,
            "test": 10,
        },
        "selectOption": "all-labeled"
    }
    
    asp.auto_split(url, api_key, data)
#%%
####################### TRAIN #########################################
import train as t
if elegir_proyecto == 'classification':
    url = url.replace('images', 'train')
elif elegir_proyecto == 'object-detection':
    url = url.replace('autosplit', 'train')
elif elegir_proyecto == 'segmentation':
    url = url.replace('autosplit', 'train')
training_id = t.training(api_key, url)
###################### MONITOR TRAIN ##################################
import monitor_train as mt
url = f'{url}/{training_id}/status'
mt.monitoring(api_key, url)
#%%
##################### MODELS #########################################
import get_models as gm
url = f'{url_base}/projects/{project_id}/models'
models = gm.model(api_key, url)
model = models[0]
threshold = 0.5
#%%
###################### DEPLOYMENT #####################################
import create_deployment as cd
url = url.replace('models', 'deployments')
if elegir_proyecto == 'classification':
    data = {"name": model.get('name'), "modelId" : model.get('id'), "threshold": threshold}
elif elegir_proyecto == 'object-detection':
    data = {"name": model.get('name'), "modelId" : model.get('id')}
elif elegir_proyecto == 'segmentation':
    data = {"name": model.get('name'), "modelId" : model.get('id')}  
deployment = cd.create(api_key, url, data)
deployment = deployment['data']
predictionUrl = deployment['predictionUrl']
endpoint_id = deployment['id']
#%%
###################### PREDICT ########################################
import predict as p
url = url.replace('deployments', 'usage/summary')
# result = p.get_data_from_api(url, api_key)
# print(result)
if elegir_proyecto ==  'classification':
    folder = 'Predictions/Class'
elif elegir_proyecto  == 'object-detection':
    folder = 'Images'
elif elegir_proyecto  == 'segmentation':
    folder = 'Images'
image_dir = os.path.join(path, folder)
p.predict(image_dir= image_dir,endpoint_id = endpoint_id,api_key = api_key)


