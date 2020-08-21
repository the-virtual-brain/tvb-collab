
# TVB pipeline base image for Openshift deployment

### Deployment (okd.hbp.eu | okd-dev.hbp.eu)
Steps:
    
    1. Create a new openshift project
    2. Import the jupyterhub json template used for jupyterhub server deployment: https://raw.githubusercontent.com/jupyter-on-openshift/jupyterhub-quickstart/master/build-configs/jupyterhub.json
    3. Import the jupyterhub-deployer.json file. After import you will be asked to fill the keycloak client secret parameter
    4. Go to the Resource -> Config Maps -> tvb-pipeline-cfg -> Actions -> Edit and edit the content of the jupyterhub_config_py and service.py
    For the jupyterhub_config.py entry copy the content of the jupyterhub_config.py file from this repo and for the service.py entry copy the content of the service.py file.
    5. Redeploy the application
    
    
### Changes on the tvb_pipeline notebook

If there are any changes inside the tvb_pipeline.ipynb file or dataset.zip or license.txt you will have to rebuild and push the base jupyterhub notebook docker image using:

1. **docker build --no-cache -t thevirtualbrain/tvb-pipeline-ipynb -f Dockerfile .**
2. **docker push thevirtualbrain/tvb-pipeline-ipynb**

After the docker image is pushed you will have to redeploy the tvb-pipeline service from the Openshift GUI. 