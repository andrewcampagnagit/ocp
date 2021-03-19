"""

ignition file downloader / generator

"""

import os
import yaml
import json
import time
import sys

project_name = sys.argv[1]
bootstrap_url = sys.argv[2]
ocpversion = sys.argv[3]

print("Starting installation for project "+ project_name)

## Install jq for approving csr requests ##
os.popen("yum install -y jq").read()

## Configure System  & Download OpenShift ##
os.popen("mkdir /opt/"+ project_name)
os.popen("wget -P /opt https://mirror.openshift.com/pub/openshift-v4/clients/ocp/"+ ocpversion +"/openshift-client-linux-"+ ocpversion +".tar.gz").read()
os.popen("wget -P /opt https://mirror.openshift.com/pub/openshift-v4/clients/ocp/"+ ocpversion +"/openshift-install-linux-"+ ocpversion +".tar.gz").read()
os.popen("tar -xvzf /opt/openshift-client-linux-"+ ocpversion +".tar.gz -C /opt").read()
os.popen("tar -xvzf /opt/openshift-install-linux-"+ ocpversion +".tar.gz -C /opt").read()
os.popen("cp /opt/oc /usr/local/bin").read()
os.popen("cp /opt/kubectl /usr/local/bin").read()
os.popen("mv /tmp/install-config.yaml /opt/"+ project_name).read()
os.chdir("/opt")


## Create Manifests / Edit cluster-scheduler-02-config.yml ##
os.popen("./openshift-install create manifests --dir=./"+ project_name).read()
with open("/opt/"+ project_name +"/manifests/cluster-scheduler-02-config.yml", "r") as cluster_scheduler_file:
	cluster_config_02 = yaml.safe_load(cluster_scheduler_file)
	cluster_config_02["spec"]["mastersSchedulable"] = False

print(os.popen("cat /opt/"+ project_name +"/manifests/cluster-scheduler-02-config.yml").read())

with open("/opt/"+ project_name +"/manifests/cluster-scheduler-02-config.yml", "w+") as cluster_scheduler_file:
	yaml.dump(cluster_config_02, cluster_scheduler_file, default_flow_style=False)

os.chdir("/opt")

print(os.popen("cat /opt/"+ project_name +"/manifests/cluster-scheduler-02-config.yml").read())
os.popen("sudo cp /opt/"+ project_name +"/manifests/cluster-scheduler-02-config.yml /var/www/html/cluster-scheduler-02-config.yml").read()


## Create ignition files ##
os.popen("./openshift-install create ignition-configs --dir=./"+ project_name).read()

append_bootstrap =  {
   "ignition": {
     "config": {
       "merge": [
         {
           "source": bootstrap_url
         }
       ]
     },
     "version": "3.1.0"
   }
 }


## Create append-bootstrap.ign ##
with open("/opt/"+ project_name +"/append-bootstrap.ign", "w+") as append_bootstrap_file:
	json.dump(append_bootstrap, append_bootstrap_file, indent=4)
	append_bootstrap_file.close()


## Encode ignition files in base64 ##
os.chdir("/opt/" + project_name)
os.popen("base64 -w0 append-bootstrap.ign > append-bootstrap.64")
os.popen("base64 -w0 master.ign > master.64")
os.popen("base64 -w0 worker.ign > worker.64")

## Finish ##
os.popen("chmod 755 /opt/"+ project_name +"/bootstrap.ign")
print(os.popen("sudo ln -s /opt/"+ project_name + " /var/www/html/"+ project_name).read())
print("Installation node is complete!")