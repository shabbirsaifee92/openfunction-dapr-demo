## Pre-requisites
Access to a kubernetes cluster

## Lab setup
1. Create azure service bus and new topic and get the endpoint connection strings
        a. servicebus name: knative-dapr-demo
        b. topic name: knative-dapr-demo

3. Add openfunction chart repo
    ```
      helm repo add openfunction https://openfunction.github.io/charts
      helm repo update
    ```
4. Deploy openfunction chart
    ```
      helm install openfunction openfunction/openfunction -n openfunction --create-namespace --wait
    ```

5. Create namespace for the demo
    ```
      kubectl create ns knative-dapr-demo
    ```
6. Deploy dapr component to use azure service bus (replace the connection string in dapr/azure-service-bus-component.yaml)
    ```
      kubectl apply -f dapr/azure-service-bus-component.yaml
    ```

7. Update `SERVICEBUS_CONNECTIONSTRING` in subscriber/open-subscriber.yaml
    ```
      kubectl apply -f subscriber/open-subscriber.yaml
    ```

8. Deploy subscriber
    ```
      kubectl apply -f subscriber/open-subscriber.yaml
    ```

9. Send a message topic from azure portal, and see the subscriber scale up
