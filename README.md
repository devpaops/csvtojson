Application code may be found under the "application" folder


Infrastructure code may be found under the "infrastructure" folder


There are separate folders for the kubernetes yaml files and the terraform code that creates the EKS cluster in AWS


Application is written in Python. It renders a web page where you will feed the row number of which you wish to convert to JSON format.


Everything, along with the dataset (https://datasets.wri.org/dataset/globalpowerplantdatabase) is packaged into a docker image you can pull - docker pull paolomedallon/devopspao_csvtojson:1.0
