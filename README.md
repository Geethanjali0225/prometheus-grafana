Step 1: Create a Docker Compose file:
Create a docker-compose.yml file with configurations for Prometheus and Grafana services.

Step 2: Prometheus and Grafana Setup:
Define service configurations for Prometheus and Grafana in the Docker Compose file. Use Prometheus and Grafana Docker images.

Step 3: Configure Prometheus:
Configure Prometheus to scrape metrics from your application. Update the prometheus.yml to include the target job with the appropriate scrape configurations pointing to your application's metric endpoint.

Step 4: Launch Services:
Run docker-compose up to launch the Prometheus and Grafana services.

Step 5: Validate Configuration:
Access http://localhost:9090 to verify if it's scraping metrics from your application. Check the Targets section in Prometheus UI to see if the job is up and running.

Step 6: Configure Grafana:
Access http://localhost:3000
Add Prometheus as a data source in Grafana using the URL where Prometheus is running 
Ensure that Grafana can connect to Prometheus.

Step 7: Create Dashboards:
Create dashboards in Grafana by adding panels based on the metrics collected by Prometheus. Use the Prometheus data source to query and visualize the metrics.
![Screenshot from 2023-11-28 12-08-26](https://github.com/Geethanjali0225/prometheus-grafana/assets/134916336/b259b818-2c2d-499a-ad66-b84a5fd0ad20)
![Screenshot from 2023-11-28 13-47-38](https://github.com/Geethanjali0225/prometheus-grafana/assets/134916336/935dcc98-bcdb-4ee5-8153-884696d13393)
![Screenshot from 2023-11-28 13-48-21](https://github.com/Geethanjali0225/prometheus-grafana/assets/134916336/b809e40e-dd16-4a2e-b48a-74e00eb3f4da)
