#!/usr/bin/bash
set -ex
EXTERNAL_IP=$(kubectl get service flask-service -o-jsonpath='{.status.loadBalancer.ingress[0].ip}')
http_response=$(curl -s -o /dev/null -w "%{http_code}" ${EXTERNAL_IP}:5000)
if [[ $http_response == 200 ]]; then
    echo "Flask app returned a 200 status code. Test passed!"
else
    echo "Flask app returned a non-200 status code: $http_response. Test failed!"
    exit 1
fi
