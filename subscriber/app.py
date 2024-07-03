from flask import Flask, request, jsonify
from cloudevents.http import from_http
import json
import os
import time

app = Flask(__name__)
app_port = os.getenv('APP_PORT', '8080')
pubsub_name = os.getenv("SERVICE_BUS_TOPIC")
pubsub_topic = os.getenv("SERVICE_BUS_TOPIC")

# Register Dapr pub/sub subscriptions
@app.route('/dapr/subscribe', methods=['GET'])
def subscribe():
    subscriptions = [{
        'pubsubname': pubsub_name,
        'topic': pubsub_topic,
        'route': pubsub_topic
    }]
    print('Dapr pub/sub is subscribed to: ' + json.dumps(subscriptions))
    return jsonify(subscriptions)

# Dapr subscription in /dapr/subscribe sets up this route
@app.route('/' + pubsub_topic, methods=['POST'])
def orders_subscriber():
    # event = from_http(request.headers, request.get_data())
    event = request.get_json()
    print('Subscriber received : %s' % event, flush=True)
    time.sleep(5)
    return json.dumps({'success': True}), 200, {
        'ContentType': 'application/json'}

app.run(port=app_port, debug=True)
