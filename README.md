# collector-grafana-promethus-flask
collect site metrics exporter and send to promethus - grafana


Docker-compose.yml:

will create 4 containers:

![docker-compose status](https://user-images.githubusercontent.com/22144148/113360414-6d94c600-9352-11eb-815e-477fd092e716.jpg)


1.collector - python exporter script - collector.py  - collect metrics about the site and post them on http://localhost:9000

![exporter9000](https://user-images.githubusercontent.com/22144148/113360114-d0399200-9351-11eb-8842-d004255c6aa8.jpg)


2.Api-service - base on flask, ruuning as a service on localhost:5000 and open for POST request , save the site list in a volume (can be done with a DB container)

![send post and save the site list](https://user-images.githubusercontent.com/22144148/113360349-49d18000-9352-11eb-9971-e8493118bb18.jpg)


3. promthus - on promethus side it will add a new traget source for scarping

![adding target to promethus](https://user-images.githubusercontent.com/22144148/113360170-ec3d3380-9351-11eb-81bf-57d28a1230bd.jpg)


4. grafana - dashbaords that will show the metrics

![grafana](https://user-images.githubusercontent.com/22144148/113360531-a03ebe80-9352-11eb-84ff-290f26bc3a8d.jpg)

