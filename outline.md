# OpenShift Container Platform requirements - Cloud Pak for Security

#### Machine Spec Table

| NAME                      	| OS        	| CPU 	| MEM  	| STORAGE                 	| FUNCTION                                                                              	| SOFTWARE                              	|
|---------------------------	|-----------	|-----	|------	|-------------------------	|---------------------------------------------------------------------------------------	|---------------------------------------	|
| Installation Node         	| Any Linux 	| 2   	| 4Gi  	| 100Gi                   	| oc / kubectl / HTTP Server for bootstrap ignition files                               	| httpd, oc, kubectl, openshift-install 	|
| Bootstrap Node            	| RHCOS     	| 2   	| 4Gi  	| 100Gi                   	| Creates mini-etcd cluster and serves master nodes ignition files at installation time 	|                                       	|
| Master-1 / ControlPlane-1 	| RHCOS     	| 4   	| 16Gi  	| 100Gi                   	| etcd-0 / Manages desired Kubernetes state / Schedules pods for deployment on workers  	|                                       	|
| Master-2 / ControlPlane-2 	| RHCOS     	| 4   	| 16Gi  	| 100Gi                   	| etcd-1 / Manages desired Kubernetes state / Schedules pods for deployment on workers  	|                                       	|
| Master-3 / ControlPlane-3 	| RHCOS     	| 4   	| 16Gi  	| 100Gi                   	| etcd-2 / Manages desired Kubernetes state / Schedules pods for deployment on workers  	|                                       	|
| Compute-1 / Worker-1      	| RHCOS     	| 8  	| 32Gi 	| 100Gi                   	| Runs scheduled pods / IBM Common Services Master / IBM Common Services Proxy          	|                                       	|
| Compute-2 / Worker-2      	| RHCOS     	| 8  	| 32Gi 	| 100Gi                   	| Runs scheduled pods / IBM Common Services Management                                  	|                                       	|
| Compute-3 / Worker-3      	| RHCOS     	| 8   	| 32Gi 	| 100Gi                   	| Runs scheduled pods                                                                   	|                                       	|
| Compute-4 / Worker-4      	| RHCOS     	| 8   	| 32Gi 	| 100Gi                   	| Runs scheduled pods                                                                   	|                                       	|
| Storage-1                 	| RHCOS     	| 11   	| 22Gi  	| SDA: 100Gi / SDB: 500Gi 	| Runs scheduled pods / rook-ceph / SDB formatted for block storage                     	|                                       	|
| Storage-2                 	| RHCOS     	| 11   	| 22Gi  	| SDA: 100Gi / SDB: 500Gi 	| Runs scheduled pods / rook-ceph / SDB formatted for block storage                     	|                                       	|
| Storage-3                 	| RHCOS     	| 11   	| 22Gi  	| SDA: 100Gi / SDB: 500Gi 	| Runs scheduled pods / rook-ceph / SDB formatted for block storage                     	|                                       	|
| Compute-LoadBalancer      	| Any Linux 	| 4   	| 8Gi  	| 100Gi                   	| OpenShift Ingress                                                                     	| haproxy                               	|
| Master-LoadBalancer       	| Any Linux 	| 4   	| 8Gi  	| 100Gi                   	| etcd cluster                                                                          	| haproxy                               	|

#### Downloads

- httpd: yum
- haproxy: yum
- oc / kubectl: https://mirror.openshift.com/pub/openshift-v4/clients/ocp/4.4.21/openshift-client-linux-4.6.8.tar.gz
- openshift-install: https://mirror.openshift.com/pub/openshift-v4/clients/ocp/4.4.21/openshift-install-linux-4.6.8.tar.gz
- Any Linux OS: Download anywhere
- RHCOS: https://mirror.openshift.com/pub/openshift-v4/dependencies/rhcos/
